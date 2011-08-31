<?php
  $header = "tile_header.html";
  $fh = fopen($header, 'r');
  while ($line = fgets($fh, 1024)) {
    print $line;
  }

  $body = array();
  exec("/usr/bin/python tile.py", $body);
  foreach($body as $line) {
    print $line;
  }

  $header = "tile_footer.html";
  $fh = fopen($header, 'r');
  while ($line = fgets($fh, 1024)) {
    print $line;
  }
?>
