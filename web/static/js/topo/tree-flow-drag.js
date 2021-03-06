
$(function(){
  $('#drag-reset').click(function(){
    $.get("/topo/clear-drag-history", {path: path}, function(rs){
      if (rs == 'OK'){
        $('#layout select').change();
      }
    });
  });  
});


function loadFlowDragTree(sid){
  
  var width = $(sid).width()-18;
  height = 600 - 5;
  
  newHeight = countNodes(json) * 22;
  height = newHeight > 600 ? newHeight : height;

  var dragHistory = "";

  var tree = d3.layout.tree()
    .size([height, width - 160]);

  // Drag
  var drag = d3.behavior.drag()
    .origin(function(d) { return d; })
    .on("dragstart", dragstart)
    .on("drag", dragmove)
    .on("dragend", dragend);
  
  function dragstart() { }
  
  function dragmove(d, i) {
    var ex = d3.event.dx;
    var ey = d3.event.dy;
    d.x += ex;
    d.y += ey;
    d.x = d.x < -30.0 ? -30.0 : (d.x > width-60.0 ? width-60.0: d.x);
    d.y = d.y < 0.0 ? 0.0 : (d.y > height ? height: d.y);
    
    if (d.links.sources) {
      d.links.sources.forEach(function(td) {
        td.source.x = d.x;
        td.source.y = d.y;
        d3.select("#"+td.id).attr("d", diagonal);
      });
    }
    
    if (d.links.targets) {
      d.links.targets.forEach(function(td) {
        td.target.x = d.x;
        td.target.y = d.y;
        d3.select("#"+td.id).attr("d", diagonal);
      });
    }
    d3.select(this).attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });
  }
  
  function dragend() {
    dragHistory = [];
    nodes.forEach(function(d){
      dragHistory.push(""+ [d.id, d.x, d.y]);
    });
    dragHistory = dragHistory.join(";");
    $.post("/topo/save-drag-history", {path: path, nodes: dragHistory});
  }

  var diagonal = d3.svg.diagonal()
    .projection(function(d) { return [d.x, d.y]; });

  d3.select(sid).append("svg")
    .attr("width", width)
    .attr("height", height)
    .append("rect")
    .attr("width", width)
    .attr("height", height);

  var vis = d3.select(sid + " svg")
    .append("g")
    .attr("transform", "translate(60, 0)");
  
  var nodes = tree.nodes(json);

  function exchange(d){
    var t = d.x;
    d.x = d.y;
    d.y = t;
    d.links = {};
  }

  function loadHistory(d){
    var hd = chart.history[d.id];
    d.x = hd.x;
    d.y = hd.y;
    d.links = {};
  }
  
  nodes.forEach(!chart.history.error ? loadHistory : exchange);
  
  var links = tree.links(nodes);
  links.forEach(function(d){
    d.id = d.source.id + "-" + d.target.id;
    var srcs = d.source.links.sources;
    if (srcs){
      srcs.push(d);
    } else {
      d.source.links.sources = [d];
    }
    var tars = d.target.links.targets;
    if (tars){
      tars.push(d);
    } else {
      d.target.links.targets = [d];
    }
  });

  //console.log("nodes: ", nodes);
  //console.log("links: ", links);
  var link = vis.selectAll("path.link")
    .data(links)
    .enter().append("path")
    .attr("class", "link")
    .attr("id", function(d){ return d.id; })
    .attr("d", diagonal);
  
  // render nodes
  var node = vis.selectAll("g.node")
    .data(nodes)
    .enter().append("g")
    .attr("class", "node")

  node.attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; })
    .call(drag);

  d3.selectAll(sid + " path.link").attr("class", function(d) {return d.target.lstatus == 0 ? "broken link" : "link"})
  
  node.append("circle")
    .attr("r", 10)
    .attr("class", statusClass);
  
  node.append("svg:image")
    .attr("xlink:href", nodeImage)
    .attr("x", "-10px")
    .attr("y", "-10px")
    .attr("width", "20px")
    .attr("height", "20px");
  
  node.append("a")
    .attr("xlink:href", function(d){return d.url;});
  
  addMenus(sid);

  node.selectAll('a')
    .append("text")
    .attr("dx", function(d) { return d.children ? -8 : 8; })
    .attr("dy", 3)
    .attr("text-anchor", function(d) { return d.children ? "end" : "start"; })
    .text(function(d) { return d.name; });

  console.log('Load flow tree completed!');
  console.log('-----------------------------------------------')
}
