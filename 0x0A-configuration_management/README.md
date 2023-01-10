0x0A. Configuration management

As a broader subject, configuration management (CM) refers to the process of systematically handling changes to a system in a way that it maintains integrity over time. Even though this process was not originated in the IT industry, the term is broadly used to refer to server configuration management.

Automation plays an essential role in server configuration management. It’s the mechanism used to make the server reach a desirable state, previously defined by provisioning scripts using a tool’s specific language and features. Automation is, in fact, the heart of configuration management for servers, and that’s why it’s common to also refer to configuration management tools as Automation Tools or IT Automation Tools.

Another common term used to describe the automation features implemented by configuration management tools is Server Orchestration or IT Orchestration, since these tools are typically capable of managing one to hundreds of servers from a central controller machine.

There are a number of configuration management tools available in the market. Puppet, Ansible, Chef and Salt are popular choices. Although each tool will have its own characteristics and work in slightly different ways, they are all driven by the same purpose: to make sure the system’s state matches the state described by your provisioning scripts.



Requirements
General

    All your files will be interpreted on Ubuntu 20.04 LTS
    All your files should end with a new line
    A README.md file at the root of the folder of the project is mandatory
    Your Puppet manifests must pass puppet-lint version 2.1.1 without any errors
    Your Puppet manifests must run without error
    Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
    Your Puppet manifests files must end with the extension .pp

Note on Versioning

Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.


Tasks
0. Create a file
mandatory

Using Puppet, create a file in /tmp.

Requirements:

    File path is /tmp/school
    File permission is 0744
    File owner is www-data
    File group is www-data
    File contains I love Puppet


Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x0A-configuration_management
    File: 0-create_a_file.pp

1. Install a package
mandatory

Using Puppet, install flask from pip3.

Requirements:

    Install flask
    Version must be 2.1.0


Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x0A-configuration_management
    File: 1-install_a_package.pp

2. Execute a command
mandatory

Using Puppet, create a manifest that kills a process named killmenow.

Requirements:

    Must use the exec Puppet resource
    Must use pkill



Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x0A-configuration_management
    File: 2-execute_a_command.pp


