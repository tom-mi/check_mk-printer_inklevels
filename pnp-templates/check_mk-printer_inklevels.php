<?php

$label = str_replace('_', ' ', substr($servicedesc, 0, 13));
$path = str_replace('_', '/', substr($servicedesc, 13));
$title = $label . $path;

$opt[1] = "--vertical-label \"%\" --lower-limit 0 --upper-limit 100 --title \"$hostname / $title  \" ";

$def[1] = '';

foreach ($NAME as $i => $name) {

    if(preg_match('/black/i', $name))
      $color = '000000';
    elseif(preg_match('/magenta/i', $name))
      $color = 'fc00ff';
    elseif(preg_match('/yellow/i', $name))
      $color = 'ffff00';
    elseif(preg_match('/cyan/i', $name))
      $color = '00ffff';
    elseif(preg_match('/red/i', $name))
      $color = 'ff0000';
    elseif(preg_match('/green/i', $name))
      $color = '00ff00';
    elseif(preg_match('/blue/i', $name))
      $color = '0000ff';
    elseif(preg_match('/color/i', $name))
      $color = 'f000f0';
    else
      $color = 'aaaaaa';

    $def[1] .= "DEF:var$i=$RRDFILE[$i]:$DS[$i]:AVERAGE ";
    $def[1] .= "LINE2:var$i#$color:\"$name\:\" ";
    $def[1] .= "GPRINT:var$i:LAST:\"%2.0lf%%\\n\" ";
}

$def[1] .= "HRULE:$WARN[1]#ffe000:\"Warning at $WARN[1]%\" ";
$def[1] .= "HRULE:$CRIT[1]#ff0000:\"Critical at $CRIT[1]%\\n\" ";

?>
