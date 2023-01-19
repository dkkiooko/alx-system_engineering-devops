Tasks
0. Double the number of webservers

In this first task you need to configure web-02 to be identical to web-01. Fortunately, you built a Bash script during your web server project, and they’ll now come in handy to easily configure web-02. Remember, always try to automate your work!
Configure Nginx so that its HTTP response contains a custom header (on web-01 and web-02)

    The name of the custom HTTP header must be X-Served-By
    The value of the custom HTTP header must be the hostname of the server Nginx is running on


    GitHub repository: alx-system_engineering-devops
    Directory: 0x0F-load_balancer
    File: 0-custom_http_response_header




1. Install your load balancer
mandatory
Score: 0.0% (Checks completed: 0.0%)

Install and configure HAproxy on your lb-01 server.

Requirements:

    Configure HAproxy so that it send traffic to web-01 and web-02
    Distribute requests using a roundrobin algorithm
    


Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x0F-load_balancer
    File: 1-install_load_balancer





2. Add a custom HTTP header with Puppet

automate the task of creating a custom HTTP header response, but with Puppet.

    
