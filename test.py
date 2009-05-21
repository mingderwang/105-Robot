 //<![CDATA[
 <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
  "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
  <title>Robot 105 Thinking...</title>
  <link type="text/css" rel="stylesheet" href="/static/styles.css">
  <script type="text/javascript" src="/static/script.js"></script>

    <script src="http://maps.google.com/maps?file=api&amp;v=2&amp;key=ABQIAAAAU0xcljgmc3MI0v0I1a300RQZd9WN54AAYgK46OiTAO7YET-bpBRg4UYrjrkKnHGbjChUwlvs77uq3A"
      type="text/javascript"></script>
    <script type="text/javascript">
    
    //<![CDATA[
    
var map;
var userAdded = 1;

var layers = {
 "blackbirds": 
 {"url": "http://bbs.keyhole.com/ubb/download.php?Number=50664",
  "name": "Blackbirds"},
 "tourdefrance": 
 {"url": "http://bbs.keyhole.com/ubb/download.php?Number=43757",
  "name": "Tour de France"},
 "japanpics": 
 {"url" : "http://www.chemlink.com.tw/about/ChemlinkNanKangOffice.kmz",
   "name": "Nankang Office"}
};  
    
function load() {
      if (GBrowserIsCompatible()) {
        var map = new GMap2(document.getElementById("map"));
        map.setCenter(new GLatLng(41.83210555555556, 27.03565), 5);
      }
    }

function onLoad() {
  map = new GMap2(document.getElementById("map")); 
  map.setCenter(new GLatLng(25.03565, 121.3619), 5);
  map.addControl(new GSmallMapControl());

  document.getElementById("url").value = "http://";
  
  for(var layer in layers) {
    addTR(layer, layers[layer].name);
  }
  document.getElementById(layer).checked = true;
  toggleGeoXML(layer, true);
} 

function addGeoXML() {
  var theUrl = document.getElementById("url").value;
  theUrl = theUrl.replace(/^\s+/, "");
  theUrl = theUrl.replace(/\s+$/, "");
  if (theUrl.indexOf(' ') != -1) {
    alert('Error - that address has a space in it');
  } else {
    var id = "userAdded" + userAdded;
    layers[id] = {};
    layers[id].url = theUrl;
    layers[id].name = "User Layer " + userAdded;

    addTR(id);
    document.getElementById(id).checked = true;
    toggleGeoXML(id, true);
    userAdded++;
  }
}

function addTR(id) {
  var layerTR = document.createElement("tr");

  var inputTD = document.createElement("td");
  var input = document.createElement("input");
  input.type = "checkbox";
  input.id = id;
  input.onclick = function () { toggleGeoXML(this.id, this.checked) };
  inputTD.appendChild(input);

  var nameTD = document.createElement("td");
  var nameA = document.createElement("a");
  nameA.href = layers[id].url;
  var name = document.createTextNode(layers[id].name);
  nameA.appendChild(name);
  nameTD.appendChild(nameA);

  layerTR.appendChild(inputTD);
  layerTR.appendChild(nameTD);
  document.getElementById("sidebarTBODY").appendChild(layerTR);
}

function zoomToGeoXML(geoXml) {
  var center = geoXml.getDefaultCenter();
  var span = geoXml.getDefaultSpan();
  var sw = new GLatLng(center.lat() - span.lat() / 2,
                       center.lng() - span.lng() / 2);
  var ne = new GLatLng(center.lat() + span.lat() / 2,
                       center.lng() + span.lng() / 2);
  var bounds = new GLatLngBounds(sw, ne);
  map.setCenter(center);
  map.setZoom(map.getBoundsZoomLevel(bounds));
}

function toggleGeoXML(id, checked) {
  if (checked) {
    var geoXml = new GGeoXml(layers[id].url);
    GEvent.addListener(geoXml, 'load', function() {
      if (geoXml.loadedCorrectly()) {
        geoXml.gotoDefaultViewport(map);
        layers[id].geoxml = geoXml;
        document.getElementById("status").innerHTML = "";
      }
    });
    layers[id].geoXml = geoXml;
    map.addOverlay(layers[id].geoXml);
    document.getElementById("status").innerHTML = "Loading...";
  
  } else if (layers[id].geoXml) {
    map.removeOverlay(layers[id].geoXml);
  }
}

    //]]>

</script>


  
</head>
<body onload="onLoad()">
<div>

<b>mingderwang &lt;mingderwang@gmail.com&gt;</b>

 | <a href="http://105.appspot.com/_ah/logout?continue=https://www.google.com/accounts/Logout%3Fcontinue%3Dhttp://105.appspot.com/%26service%3Dah">Sign Out</a>

<h2>Free GPS Uploading Places</h2>

List of Places:
<ul>

<li>
  <a href="/edit/142">Sparkles2</a>
  - created 2008/06/23 08:02:31 by mingderwang

<li>
  <a href="/edit/141">location</a>

  - created 2008/06/23 06:23:08 by mingderwang

<li>
  <a href="/edit/122">&lt;&gt;&lt;&gt;&lt;&lt;&lt;&lt;&lt;&gt;&gt;&gt;&gt;&gt;&lt;&gt;&lt;&gt;&lt;&gt;&lt;&lt;&lt;&lt;&gt;&lt;&lt;&gt;&lt;&gt;&lt;&gt;&lt;&gt;&lt;&gt;&lt;&lt;.&lt;&gt;&lt;&gt;&gt;&lt;&lt;&gt;&gt;&gt;,.&gt;&gt;&gt;&lt;&lt;&gt;&lt;&lt;</a>
  - created 2008/06/21 15:23:06 by mingderwang

<li>
  <a href="/edit/121">¤¤¤å</a>
  - created 2008/06/21 14:48:19 by mingderwang

<li>
  <a href="/edit/101">stars</a>

  - created 2008/06/19 15:20:34 by ym1220

<li>
  <a href="/edit/2">PicLens</a>
  - created 2008/06/16 09:28:58 by mingderwang

<li>
  <a href="/edit/81">aaaaaaaaaaaaaaaaaaaaaaaaaaaaa lllllllllllllllllllllong list</a>
  - created 2008/06/15 14:25:33 by ym1220

<li>
  <a href="/edit/61">Birthdaygift</a>

  - created 2008/06/15 14:24:24 by ym1220

<li>
  <a href="/edit/41">Protopage</a>
  - created 2008/06/15 14:05:55 by mingderwang

<li>
  <a href="/edit/21">free tibet</a>
  - created 2008/06/15 13:54:48 by mingderwang

<li>
  <a href="/edit/1">Sparkle</a>

  - created 2008/06/15 13:53:15 by mingderwang

</ul>

<a href="/new">Create new place.</a>


</div>
  <br/>
    <input id="url" value="" size="60"/>
    <input type="button" value="Add" onClick="addGeoXML();"/>
  <br/>

  <br/>
    <div id="map" style="width: 400px; height: 400px; float:left; border: 1px solid black;"></div>
    <div id="sidebar" style="float:left; overflow-vertical:scroll; height: 400px; width:150px; border:1px solid black">
    <table id="sidebarTABLE">
    <tbody id="sidebarTBODY">
    </tbody>
    </table>
<div id="status" style="text-align:center; color: #ff0000"></div>
</div>

</body>
</html>

    //]]>
