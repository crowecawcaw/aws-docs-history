# Using standalone instances as AWS PCS

login nodes

You can set up independent EC2 instances to interact with an AWS PCS cluster's Slurm scheduler.
This is useful for creating login nodes, workstations, or dedicated workflow management hosts that
work with AWS PCS clusters but operate outside of AWS PCS management. To do this, each standalone instance
must:

1. Have a compatible Slurm software version installed.
2. Be able to connect to the AWS PCS cluster's Slurmctld endpoint.
3. Have the Slurm Auth and Cred Kiosk Daemon (`sackd`) properly configured with the
   AWS PCS cluster's endpoint and secret. For more information, see [sackd](https://slurm.schedmd.com/sackd.html "https://slurm.schedmd.com/sackd.html") in the Slurm documentation.
   This tutorial helps you configure an independent instance that connects to an AWS PCS
   cluster.

###### Contents

- [Step 1 – Retrieve the
  address and secret for the target AWS PCS cluster](working-with_login-nodes_standalone_get-addr.md "working-with_login-nodes_standalone_get-addr.md")
- [Step 2 – Launch an EC2
  instance](working-with_login-nodes_standalone_launch.md "working-with_login-nodes_standalone_launch.md")
- [Step 3 – Install Slurm
  on the instance](working-with_login-nodes_standalone_install-slurm.md "working-with_login-nodes_standalone_install-slurm.md")
- [Step 4 – Retrieve and
  store the cluster secret](working-with_login-nodes_standalone_get-secret.md "working-with_login-nodes_standalone_get-secret.md")
- [Step 5 –
  Configure the connection to the AWS PCS cluster](working-with_login-nodes_standalone_configure-connection.md "working-with_login-nodes_standalone_configure-connection.md")
- [Step 6 – (Optional) Test the
  connection](working-with_login-nodes_standalone_test.md "working-with_login-nodes_standalone_test.md")
