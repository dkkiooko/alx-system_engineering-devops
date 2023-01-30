
0. World wide web
Bash script that displays information about subdomains.
	accepts 2 arguments:
        	domain:
            		type: string
            		what: domain name to audit
            		mandatory: yes
        	subdomain:
            		type: string
            		what: specific subdomain to audit
            		mandatory: no
	Output: The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]
When only the parameter domain is provided, displays information for its subdomains www, lb-01, web-01 and web-02 - in this specific order
When passing domain and subdomain parameters, displays information for the specified subdomain
    Ignore shellcheck case SC2086
    Must use:
        awk
        at least one Bash function
    You do not need to handle edge cases such as:
        Empty parameters
        Nonexistent domain names
        Nonexistent subdomains

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x10-https_ssl
    File: 0-world_wide_web

1. HAproxy SSL termination
“Terminating SSL on HAproxy” means that HAproxy is configured to handle encrypted traffic, unencrypt it and pass it on to its destination.



Requirements:

    HAproxy must be listening on port TCP 443
    HAproxy must be accepting SSL traffic
    HAproxy must serve encrypted traffic that will return the / of your web server


Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x10-https_ssl
    File: 1-haproxy_ssl_termination


