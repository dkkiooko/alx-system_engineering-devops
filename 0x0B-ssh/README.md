Tasks
0. Use a private key
mandatory

Write a Bash script that uses ssh to connect to your server using the private key ~/.ssh/school with the user ubuntu.



Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x0B-ssh
    File: 0-use_a_private_key

1. Create an SSH key pair
mandatory

Write a Bash script that creates an RSA key pair.

Requirements:

    Name of the created private key must be school
    Number of bits in the created key to be created 4096
    The created key must be protected by the passphrase betty

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x0B-ssh
    File: 1-create_ssh_key_pair

2. Client configuration file
mandatory

Your machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file.

Requirements:

    Your SSH client configuration must be configured to use the private key ~/.ssh/school
    Your SSH client configuration must be configured to refuse to authenticate using a password


Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x0B-ssh
    File: 2-ssh_config

3. Let me in!
mandatory

Now that you have successfully connected to your server, we would also like to join the party.

Add the SSH public key below to your server so that we can connect using the ubuntu user.

ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDNdtrNGtTXe5Tp1EJQop8mOSAuRGLjJ6DW4PqX4wId/Kawz35ESampIqHSOTJmbQ8UlxdJuk0gAXKk3Ncle4safGYqM/VeDK3LN5iAJxf4kcaxNtS3eVxWBE5iF3FbIjOqwxw5Lf5sRa5yXxA8HfWidhbIG5TqKL922hPgsCGABIrXRlfZYeC0FEuPWdr6smOElSVvIXthRWp9cr685KdCI+COxlj1RdVsvIo+zunmLACF9PYdjB2s96Fn0ocD3c5SGLvDOFCyvDojSAOyE70ebIElnskKsDTGwfT4P6jh9OBzTyQEIS2jOaE5RQq4IB4DsMhvbjDSQrP0MdCLgwkN

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x0B-ssh

4. Client configuration file (w/ Puppet)
#advanced

Let’s practice using Puppet to make changes to our configuration file. Just as in the previous configuration file task, we’d like you to set up your client SSH configuration file so that you can connect to a server without typing a password.

Requirements:

    Your SSH client configuration must be configured to use the private key ~/.ssh/school
    Your SSH client configuration must be configured to refuse to authenticate using a password



Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x0B-ssh
    File: 100-puppet_ssh_config.pp


