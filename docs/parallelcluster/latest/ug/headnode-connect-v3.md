# Connect to a cluster

When you use AWS ParallelCluster, you can connect to the cluster head node to run jobs, view results, manage users, and monitor the cluster and job status.
To connect to the cluster head node instance, use one of the following methods:

- You can use `ssh` with a [key pair](install-v3.md#set-up-keypair "install-v3.md#set-up-keypair") to log in. Specify the private key in [HeadNode](HeadNode-v3.md "HeadNode-v3.md") / [KeyName](HeadNode-v3.md#yaml-HeadNode-Ssh-KeyName "HeadNode-v3.md#yaml-HeadNode-Ssh-KeyName") in the cluster
  configuration. For more information, see [Connect to
  your Linux instance using SSH](../../../AWSEC2/latest/UserGuide/AccessingInstancesLinux.md "../../../AWSEC2/latest/UserGuide/AccessingInstancesLinux.md") in the _Amazon EC2 User Guide for Linux Instances_.
- You can use the `pcluster ssh` command line interface (CLI) command to log in. Specify the private key in the cluster configuration
  [HeadNode](HeadNode-v3.md "HeadNode-v3.md") / [KeyName](HeadNode-v3.md#yaml-HeadNode-Ssh-KeyName "HeadNode-v3.md#yaml-HeadNode-Ssh-KeyName"). For more
  information, see [pcluster ssh](pcluster.md "pcluster.md").
- You can use an SSM session to connect to the cluster head node. You must add the `AmazonSSMManagedInstanceCore` managed policy to
  [HeadNode](HeadNode-v3.md "HeadNode-v3.md") / [AdditionalIamPolicies](HeadNode-v3.md#yaml-HeadNode-Iam-AdditionalIamPolicies "HeadNode-v3.md#yaml-HeadNode-Iam-AdditionalIamPolicies") in the cluster configuration to connect by using an SSM session. For more information, see [SSM session manager](../../../systems-manager/latest/userguide/session-manager.md "../../../systems-manager/latest/userguide/session-manager.md") in the _SSM User Guide_.
- You can use Amazon DCV to connect to the cluster head node. For more information, see [Connect to the head and login nodes through Amazon DCV](dcv-v3.md "dcv-v3.md").
- When you use the PCUI, you can also use an Amazon EC2 Connect command that the UI provides to connect to the cluster head node.
