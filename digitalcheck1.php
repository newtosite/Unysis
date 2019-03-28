<?php
$date="2012/09/12";
$file = 'rc_sri.txt';
header('Content-Type: text/plain');
$contents = file_get_contents($file);
if (preg_match("/^[0-9]{4}\/(0[1-9]|1[0-2])\/(0[1-9]|[1-2][0-9]|3[0-1])$/",$date)) {
    echo true;
} else {
    echo "false";
}
?>