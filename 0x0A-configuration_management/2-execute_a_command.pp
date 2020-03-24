# how to kill an execute a process
exec { 'pkill':
  path =>  '/usr/bin/',
  command  => 'pkill -f killmenow',
  returns => [0,1],
  }