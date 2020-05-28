# script to add more worker process to nginx .conf file and restart service

exec { 'nginx stop':
command => 'service nginx stop',
path    => '/usr/bin/',
}
exec { 'sed command':
command => 'sudo sed -i 's/worker_processes [0-9]/worker_processes 10/' /etc/nginx/nginx.conf',
path    => ['/usr/bin/', '/usr/sbin'],
}
exec { 'nginx start':
command => 'sudo service nginx start',
path    => '/usr/bin/',
}
