# Example: Enabling passwordless SSH

You can build on the shared home directory example to implement SSH connections
between cluster instances using SSH keys. For each user using the shared home
file system, run a script that resembles the following:

```
#!/bin/bash

mkdir -p $HOME/.ssh && chmod 700 $HOME/.ssh
touch $HOME/.ssh/authorized_keys
chmod 600 $HOME/.ssh/authorized_keys

if [ ! -f "$HOME/.ssh/id_rsa" ]; then
    ssh-keygen -t rsa -b 4096 -f $HOME/.ssh/id_rsa -N ""
    cat ~/.ssh/id_rsa.pub >> $HOME/.ssh/authorized_keys
fi

```

###### Note

The instances must use a security group that allows SSH connections between
cluster nodes.
