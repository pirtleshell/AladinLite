<?php
// Resolve Names
// This serves as a proxy to http://cds.u-strasbg.fr/cgi-bin/nph-sesame.jsonp
// It simply relays the request to CDS's service Sesame
// More about Sesame is available here: http://cdsweb.u-strasbg.fr/doc/sesame.htx
// This way is going to make each request longer, but it works and is only temporary
//
// Currently (Jan 2017) live at https://laniakean.com/api/v1/resolveNames/?
//
// author: Robert Pirtle <https://pirtle.xyz/>
// license: MIT
header('Content-Type: application/javascript');
header('Access-Control-Allow-Headers: Content-Type');
header('Access-Control-Allow-Methods: GET');
header('Access-Control-Allow-Origin: *');

$url =  "{$_SERVER['REQUEST_URI']}";

$q = parse_url($url);
$request_data = array();
$sesame_url = "http://cds.u-strasbg.fr/cgi-bin/nph-sesame.jsonp?";
if (isset($q['query'])) {
  $sesame_url .= $q['query'];
}
echo file_get_contents($sesame_url);
?>
