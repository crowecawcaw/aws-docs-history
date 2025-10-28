# Connecting a client to the Jupyter Notebook server on a DLAMI

instance

After you [start the Jupyter Notebook server on your DLAMI
instance](setup-jupyter-start-server.md "setup-jupyter-start-server.md"), configure your Windows, macOS, or Linux client to connect to the
server. When you connect, you can create and access Jupyter notebooks on the server in
your workspace and run your deep learning code on the server.

## Prerequisites

Be sure you have the following, which you need to set up an SSH tunnel:

- The public DNS name of your Amazon EC2 instance. For more information, see [Amazon EC2 instance
  hostname types](../../../AWSEC2/latest/UserGuide/ec2-instance-naming.md "../../../AWSEC2/latest/UserGuide/ec2-instance-naming.md") in the _Amazon EC2 User Guide_.
- The key pair for the private key file. For more information about accessing your key
  pair, see [Amazon EC2
  key pairs and Amazon EC2 instances](../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md "../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md") in the _Amazon EC2 User Guide_.

## Connect from a Windows, macOS, or Linux

client

To connect to your DLAMI instance from a Windows, macOS, or Linux client, follow the
instructions for your client's operating system.

Windows

###### To connect to your DLAMI instance from a Windows client using SSH

1. Use an SSH client for Windows, such as PuTTY. For instructions, see [Connect to
   your Linux instance using PuTTY](../../../AWSEC2/latest/UserGuide/connect-linux-inst-from-windows.md "../../../AWSEC2/latest/UserGuide/connect-linux-inst-from-windows.md") in the _Amazon EC2 User Guide_. For other SSH connection options, see [Connect to your
   Linux instance using SSH](../../../AWSEC2/latest/UserGuide/connect-to-linux-instance.md "../../../AWSEC2/latest/UserGuide/connect-to-linux-instance.md").
2. (Optional) Create an SSH tunnel to a running Jupyter server. Install Git Bash on your Windows
   client, and then follow the connection instructions for macOS and Linux
   clients.

macOS or Linux

###### To connect to your DLAMI instance from a macOS or Linux client using SSH

1. Open a terminal.
2. Run the following command to forward all requests on local port 8888 to
   port 8888 on your remote Amazon EC2 instance. Update the command by replacing
   the location of your key to access the Amazon EC2 instance and the public DNS name of your Amazon EC2 instance.
   Note, for an Amazon Linux AMI, the user name is `ec2-user` instead of `ubuntu`.

```
`$` ssh -i `~/mykeypair.pem` -N -f -L 8888:localhost:8888 ubuntu@ec2-`###-##-##-###`.compute-1.amazonaws.com
```

This command opens a tunnel between your client and the remote Amazon EC2 instance that is running the Jupyter Notebook server.

###### Next step

[Logging in to the Jupyter Notebook server on a DLAMI instance](setup-jupyter-login.md "setup-jupyter-login.md")
