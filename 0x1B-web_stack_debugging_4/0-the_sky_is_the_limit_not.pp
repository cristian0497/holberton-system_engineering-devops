# script to add more worker process to nginx .conf file and restart service

exec { '/bin':
command => "sudo sed -i 's/worker_processes [0-9]/worker_processes 10/' /etc/nginx/nginx.conf",
path    => ['/usr/bin/', '/usr/sbin'],
}
service { 'nginx':
restart => 'sudo service nginx restart',
}