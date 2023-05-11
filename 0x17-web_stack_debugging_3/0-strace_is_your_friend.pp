# Replaces phpp with php in wp-settings.php


exec { 'replace-phpp-with-php':
  command     => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path	      => ['bin', 'usr/bin'],
}
