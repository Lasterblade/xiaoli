%powercn "SGR-WM2004-A-10000-6144"
%SGR-W500-I
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% ac discover -- ac配置(发现)%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-define(AcName, {acName, "1.3.6.1.4.1.18603.3.1.1.1.1.1.0"}).
-define(SysModel, {sysModel, "1.3.6.1.4.1.18603.3.1.1.1.1.18.0"}).
-define(SoftwareVersion, {softVersion, "1.3.6.1.4.1.18603.3.1.1.1.1.19.0"}).

%-define(PortalServerURL, {portalServerURL, "1.3.6.1.4.1.18603.3.1.1.1.11.1.2.0"}).
-define(AsIPAddress, {asIPAddress, "1.3.6.1.4.1.18603.3.1.1.1.1.17.0"}).

%% interface
-define(AcIfDescr, {ifDescr, "1.3.6.1.2.1.2.2.1.2"}).
-define(AcIfType, {ifType, "1.3.6.1.2.1.2.2.1.3"}).
-define(AcIfMTU, {ifMtu, "1.3.6.1.2.1.2.2.1.4"}).
-define(AcIfSpeed, {ifSpeed, "1.3.6.1.2.1.2.2.1.5"}).
-define(AcIfMacAddress, {ifPhysAddress, "1.3.6.1.2.1.2.2.1.6"}).
-define(AcIfAdminStatus, {ifAdminStatus, "1.3.6.1.2.1.2.2.1.7"}).
-define(AcIfOperStatus, {ifOperStatus, "1.3.6.1.2.1.2.2.1.8"}).

% --- RadiusServerIndex 
%-define(RadiusAuthServerIPAdd, {radiusAuthServerIPAdd, "1.3.6.1.4.1.18603.3.3.5.1.2"}).
%-define(RadiusAuthServerPort, {radiusAuthServerPort, "1.3.6.1.4.1.18603.3.3.5.1.3"}).

% ----  vlaninterface
%-define(IPPoolName, {ipPoolName, "1.3.6.1.4.1.18603.3.1.1.1.10.1.11"}).
%-define(IPPoolStartAddr, {ipPoolStartAddr, "1.3.6.1.4.1.18603.3.1.1.1.10.1.3"}).
%-define(IPPoolStopAddr, {ipPoolStopAddr, "1.3.6.1.4.1.18603.3.1.1.1.10.1.4"}).

%%%%%%%%%%%%%%%%%%%%%%%%%%
%% ac monet --ac 性能采集% 
%%%%%%%%%%%%%%%%%%%%%%%%%%

-define(Acinfo, [
     {cpuRTUsage,               "1.3.6.1.4.1.18603.3.1.1.1.1.87.0" },
     {memRTUsage,               "1.3.6.1.4.1.18603.3.1.1.1.1.89.0" },
     {dHCPReqTimes,             "1.3.6.1.4.1.18603.3.1.1.1.1.76.0" },
     {dHCPReqSucTimes,          "1.3.6.1.4.1.18603.3.1.1.1.1.77.0" },
     {bandWidth,                "1.3.6.1.4.1.18603.3.1.1.1.1.47.0" },
     {onlineNum,                "1.3.6.1.4.1.18603.3.1.1.1.1.102.0"},
     {authNum,                  "1.3.6.1.4.1.18603.3.1.1.1.1.74.0" },
     {normalNum,                "1.3.6.1.4.1.18603.3.1.1.1.1.99.0" },
     {deauthNum,                "1.3.6.1.4.1.18603.3.1.1.1.1.100.0"},
     {authReqNum,               "1.3.6.1.4.1.18603.3.1.1.1.1.70.0" },
     {authSucNum,               "1.3.6.1.4.1.18603.3.1.1.1.1.71.0" },
     {radiusAvgDelay,           "1.3.6.1.4.1.18603.3.1.1.1.1.103.0"},
     {dHCPIpPoolUsage,          "1.3.6.1.4.1.18603.3.1.1.1.1.75.0" } 

    %{portalChallengeReqCount,  "1.3.6.1.4.1.18603.3.1.1.1.30.1.2"},
    %{portalChallengeRespCount, "1.3.6.1.4.1.18603.3.1.1.1.30.1.4"},
    %{portalAuthReqCount,       "1.3.6.1.4.1.18603.3.1.1.1.30.1.1"},
    %{portalAuthRespCount,      "1.3.6.1.4.1.18603.3.1.1.1.30.1.4"},

    %{maxNum,                   ""}.
    %{accReqNum,                ""}.
    %{accSucNum,                ""}.
    %{radiusReqPkts,            ""}.
    %{radiusRepPkts,            ""}.
    %{leaveReqPkts,             ""}.
    %{leaveRepPkts,             ""}.
    %{leaveReqCount,            ""},
    %{leaveRepCount,            ""},
    %{addressCount,             ""},
]).

-define(Acintf, [
     {ifInUcastPkts,            "1.3.6.1.2.1.2.2.1.11"},
     {ifInNUcastPkts,           "1.3.6.1.2.1.2.2.1.12"},
     {ifInOctets,               "1.3.6.1.2.1.2.2.1.10"},
     {ifInDiscards,             "1.3.6.1.2.1.2.2.1.13"},
     {ifInErrors,               "1.3.6.1.2.1.2.2.1.14"},
     {ifOutUcastPkts,           "1.3.6.1.2.1.2.2.1.17"},
     {ifOutNUcastPkts,          "1.3.6.1.2.1.2.2.1.18"},
     {ifOutOctets,              "1.3.6.1.2.1.2.2.1.16"},
     {ifOutDiscards,            "1.3.6.1.2.1.2.2.1.19"},
     {ifOutErrors,              "1.3.6.1.2.1.2.2.1.20"}

     %{ifUpDwnTimes,            "1.3.6.1.4.1.18603.3.1.1.4.2.1.22"}.
]).

%%%%%%%%%%%%%%%%%%%%%%%%%%
%% ap monet --ap 性能采集% 
%%%%%%%%%%%%%%%%%%%%%%%%%%

%%ap 无线接口性能  
-define(FitapWirelessInAvgSignal,{ifInAvgSignal, "1.3.6.1.4.1.18603.3.1.1.3.7.1.72"}).
-define(FitapWirelessInHighSignal,{ifInHighSignal, "1.3.6.1.4.1.18603.3.1.1.3.7.1.73"}).
-define(FitapWirelessInLowSignal,{ifInLowSignal, "1.3.6.1.4.1.18603.3.1.1.3.7.1.74"}).
%-define(FitapWirelessFrameRetryRate,{fitapWirelessFrameRetryRate, ""}).

-define(FitapWirelessOutPkts,{ifOutPkts, "1.3.6.1.4.1.18603.3.1.1.3.7.1.11"}).
-define(FitapWirelessInPkts,{ifInPkts, "1.3.6.1.4.1.18603.3.1.1.3.7.1.10"}).
-define(FitapWirelessInOctets,{ifInOctets, "1.3.6.1.4.1.18603.3.1.1.3.7.1.12"}).
-define(FitapWirelessOutOctets,{ifOutOctets, "1.3.6.1.4.1.18603.3.1.1.3.7.1.13"}).
-define(FitapWirelessInErrors,{ifInErrors, "1.3.6.1.4.1.18603.3.1.1.3.7.1.71"}).



%%ap 有线接口性能  
-define(FitapWireInUcastPkts, {ifInUcastPkts, "1.3.6.1.4.1.18603.3.1.1.3.6.1.9"}).
-define(FitapWireInNUcastPkts,{ifInNUcastPkts, "1.3.6.1.4.1.18603.3.1.1.3.6.1.16"}).
-define(FitapWireInOctets,{ifInOctets, "1.3.6.1.4.1.18603.3.1.1.3.6.1.17"}).
-define(FitapWireInDiscards,{ifInDiscards, "1.3.6.1.4.1.18603.3.1.1.3.6.1.12"}).
-define(FitapWireInErrors,{ifInErrors, "1.3.6.1.4.1.18603.3.1.1.3.6.1.18"}).

-define(FitapWireOutUcastPkts, {ifOutUcastPkts, "1.3.6.1.4.1.18603.3.1.1.3.6.1.13"}).  
-define(FitapWireOutNUcastPkts,{ifOutNUcastPkts, "1.3.6.1.4.1.18603.3.1.1.3.6.1.19"}).
-define(FitapWireOutOctets,{ifOutOctets, "1.3.6.1.4.1.18603.3.1.1.3.6.1.20"}).
-define(FitapWireOutDiscards,{ifOutDiscards, "1.3.6.1.4.1.18603.3.1.1.3.6.1.21"}).
-define(FitapWireOutErrors,{ifOutErrors, "1.3.6.1.4.1.18603.3.1.1.3.6.1.22"}).

%%ap连接信息统计
-define(MonAssoc,[
    {assocFailNum,       "1.3.6.1.4.1.18603.3.1.1.3.23.1.30"},
    {reAssocNum,         "1.3.6.1.4.1.18603.3.1.1.3.23.1.11"},
    {assocRefusedNum,    "1.3.6.1.4.1.18603.3.1.1.3.23.1.36" },
    {apStationOnlineSum, "1.3.6.1.4.1.18603.3.1.1.3.1.1.123"},
    {cpuRTUsage,         "1.3.6.1.4.1.18603.3.1.1.3.1.1.109"},
    {memRTUsage,         "1.3.6.1.4.1.18603.3.1.1.3.1.1.111"}
   
   %{assocNum,           "1.3.6.1.4.1.18603.3.1.1.3.23.1.2" },
   %{deauthNum,          ""},
   %{apStationAssocSum,  ""},
]).

%%sta终端性能统计  --- StaIndex
-define(FitapMac, {apId, "1.3.6.1.4.1.18603.3.1.1.3.3.1.35"}).
-define(FitapStaMac, {staMac, "1.3.6.1.4.1.18603.3.1.1.3.3.1.6"}).
-define(FitapStaIP, {staIp, "1.3.6.1.4.1.18603.3.1.1.3.3.1.18"}).
-define(FitapStaRssi, {staRssi, "1.3.6.1.4.1.18603.3.1.1.3.3.1.16"}).
-define(FitapStaNoiseRate, {staNoiseRate, "1.3.6.1.4.1.18603.3.1.1.3.3.1.17"}).
-define(FitapStaChannel, {staChannel, "1.3.6.1.4.1.18603.3.1.1.3.3.1.27"}).
-define(FitapStaVlan, {staVlan, "1.3.6.1.4.1.18603.3.1.1.3.3.1.24"}).
-define(FitapStaSsid, {staSsid, "1.3.6.1.4.1.18603.3.1.1.3.3.1.19"}).
-define(FitapStaRxframe, {staRxframe, "1.3.6.1.4.1.18603.3.1.1.3.3.1.4"}).
-define(FitapStaTxframe, {staTxframe, "1.3.6.1.4.1.18603.3.1.1.3.3.1.28"}).
-define(FitapStaRxbytes, {staRxbytes, "1.3.6.1.4.1.18603.3.1.1.3.3.1.3"}).
-define(FitapStaTxbytes, {staTxbytes, "1.3.6.1.4.1.18603.3.1.1.3.3.1.29"}).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% ap discover -- ap配置(发现)%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%系统信息配置
-define(ApMacAddr,{apMac,"1.3.6.1.4.1.18603.3.1.1.3.1.1.8"}). %apMAC地址
-define(ApName,{apName,"1.3.6.1.4.1.18603.3.1.1.3.1.1.11"}).
-define(ApType,{apType,"1.3.6.1.4.1.18603.3.1.1.3.1.1.14"}).
-define(ApSerialNo,{apSerialNo,"1.3.6.1.4.1.18603.3.1.1.3.1.1.12"}).
-define(ApSoftVersion,{apSoftVersion,"1.3.6.1.4.1.18603.3.1.1.3.1.1.16"}).
-define(ApIp,{apIp,"1.3.6.1.4.1.18603.3.1.1.3.1.1.3"}).
-define(ApMask,{apMask,"1.3.6.1.4.1.18603.3.1.1.3.1.1.4"}).

%%radio   APIndex + WirelessIFIndex
-define(FitapRadioPeriod, {radioPeriod, "1.3.6.1.4.1.18603.3.1.1.3.2.1.30"}).
-define(FitapRadioDtim, {radioDtim, "1.3.6.1.4.1.18603.3.1.1.3.2.1.31"}).
-define(FitapRadioRts, {radioRts, "1.3.6.1.4.1.18603.3.1.1.3.2.1.7"}).
-define(FitapRadioSlice, {radioSlice, "1.3.6.1.4.1.18603.3.1.1.3.2.1.6"}).

-define(FitapRadioModel, {radioModel, "1.3.6.1.4.1.18603.3.1.1.3.2.1.23"}).
-define(FitapRadioChannel, {radioChannel, "1.3.6.1.4.1.18603.3.1.1.3.2.1.27"}).
-define(FitapRadioPower, {radioPower, "1.3.6.1.4.1.18603.3.1.1.3.2.1.24"}).

%%security -- ssidIndex
%-define(WlanSecurity, {wlanSecurity, ""}).

%%interface --- APIndex + WirelessIFIndex
-define(WireIfOperStatus, {ifOperStatus, "1.3.6.1.4.1.18603.3.1.1.3.6.1.8"}).

-define(WirelessIfDescr, {ifDescr, "1.3.6.1.4.1.18603.3.1.1.3.6.1.2"}).
-define(WirelessIfType, {ifType, "1.3.6.1.4.1.18603.3.1.1.3.6.1.3"}).
-define(WirelessIfMTU, {ifMtu, "1.3.6.1.4.1.18603.3.1.1.3.6.1.4"}).
-define(WirelessIfSpeed, {ifSpeed, "1.3.6.1.4.1.18603.3.1.1.3.6.1.5"}).
-define(WirelessIfMacAddress, {ifPhysAddress, "1.3.6.1.4.1.18603.3.1.1.3.6.1.6"}).
-define(WirelessIfAdminStatus, {ifAdminStatus, "1.3.6.1.4.1.18603.3.1.1.3.6.1.23"}).
-define(WirelessIfOperStatus, {ifOperStatus, "1.3.6.1.4.1.18603.3.1.1.3.6.1.8"}).

-define(ApState, {apState, "1.3.6.1.4.1.18603.3.1.1.3.1.1.9"}).

%%----------------------------------------------------------------------
%% ApSsid
%%----------------------------------------------------------------------
-define(SsidAssoc,{ssidAssoc,"1.3.6.1.4.1.18603.3.2.1.2.1.2"}).
-define(DiscoApSsid,[
    {ssidName,             "1.3.6.1.4.1.18603.3.2.1.3.1.6" },
    {ssidEnabled,          "1.3.6.1.4.1.18603.3.2.1.3.1.17"},
    {ssidHidden,           "1.3.6.1.4.1.18603.3.2.1.3.1.7" },
    {staIsolate,           "1.3.6.1.4.1.18603.3.2.1.3.1.18"},
    {dot11Auth,            "1.3.6.1.4.1.18603.3.2.1.3.1.4" },
    {security,             "1.3.6.1.4.1.18603.3.2.1.3.1.5" },
    {authenMode,           "1.3.6.1.4.1.18603.3.2.1.3.1.19"},
    {securityCiphers,      "1.3.6.1.4.1.18603.3.2.1.3.1.20"},
    {vlanId,               "1.3.6.1.4.1.18603.3.2.1.3.1.8" },
    {maxSimultUsers,       "1.3.6.1.4.1.18603.3.2.1.3.1.11"}
]).


