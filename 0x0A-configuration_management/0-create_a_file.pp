# Creates the file /tmp/school that contains 'I love Puppet' with 0744 permision

file {'school':
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love puppet',
  path    => '/tmp/school',
}
