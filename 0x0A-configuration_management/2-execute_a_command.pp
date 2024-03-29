# Using Puppet, create a manifest that kills a process named killmenow.
  # Requirements:
    # Must use the exec Puppet resource
    # Must use pkill


exec { 'kill_process':
  command => 'pkill killmenow',
  path    => '/usr/bin:/usr/sbin:/bin:/sbin',
  onlyif  => 'pgrep killmenow',
}
