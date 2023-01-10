# kill a specific process in bash killmenow

exec { 'pkill':
    command  => 'pkill killmenow',
    provider => 'shell',
}
