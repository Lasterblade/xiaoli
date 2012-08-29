%%%----------------------------------------------------------------------
%%% File    : mit_event.erl
%%% Author  : Ery Lee <ery.lee@gmail.com>
%%% Purpose : MIT change callback.
%%% Created : 10 May 2012
%%% License : http://www.opengoss.com/license
%%%
%%% Copyright (C) 2012, www.opengoss.com 
%%%----------------------------------------------------------------------
-module(mit_event). 

-author('ery.lee@gmail.com').

-include_lib("elog/include/elog.hrl").

-behavior(gen_server).

-export([start_link/0, notify/1]).

-export([init/1,
        handle_call/3,
        handle_cast/2,
        handle_info/2,
        terminate/2,
        code_change/3]).

-record(state, {channel}).

start_link() ->
    gen_server2:start_link({local, ?MODULE}, ?MODULE, [], []).

notify(Event) when is_tuple(Event) ->
	gen_server2:cast(?MODULE, {notify, Event}).

init([]) ->
	{ok, Conn} = amqp:connect(),
    Channel = open(Conn),
    ?INFO_MSG("mit_event is started."),
    {ok, #state{channel = Channel}}.

open(C) ->
	{ok, Channel} = amqp:open_channel(C),
	amqp:topic(Channel, "oss.mit"),
	Channel.

handle_call(Req, _From, State) ->
    {stop, {error, {badreq, Req}}, State}.

handle_cast({notify, Event}, #state{channel = Ch} = State) ->
	Type = atom_to_list(element(1, Event)),
	Key = iolist_to_binary(["mit.", Type]),
	amqp:publish(Ch, "oss.mit", term_to_binary(Event), Key),
	{noreply, State};

handle_cast(Msg, State) ->
    {stop, {error, {badmsg, Msg}}, State}.

handle_info(Info, State) ->
    {stop, {error, {badinfo, Info}}, State}.

terminate(_Reason, _State) ->
    ok.

code_change(_OldVsn, State, _Extra) ->
    {ok, State}.

