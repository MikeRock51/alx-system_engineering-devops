# Replaces phpp with php in wp-settings.php


exec { 'replace-phpp-with-php':
  command     => '/bin/sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  refreshonly => true,
  subscribe   => File['/var/www/html/wp-settings.php'],
}
