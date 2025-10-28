# Complete prerequisite steps for using Amazon EMR with Trino

If you haven't used AWS, or if you haven't created an Amazon EMR cluster, complete these prerequisite steps
before you create an Amazon EMR cluster with Trino.

## AWS environment set up

Complete these steps to configure your AWS account if you haven't already:

1. Sign up for an AWS account, if you don't have one already. For more information,
   see [Create an AWS account](../../../accounts/latest/reference/manage-acct-creating.md "../../../accounts/latest/reference/manage-acct-creating.md") in
   the _AWS Account Management Reference Guide_.
2. Sign in to your account as an administrative user.
3. Create a group and assign users to it.
4. Create an Amazon EC2 key pair, which you can use later to secure communication between resources with SSH. This step is required if you
   plan to connect to the primary node to perform tasks. For more information, see [Connect to the Amazon EMR cluster primary
   node using SSH](../ManagementGuide/emr-connect-master-node-ssh.md "../ManagementGuide/emr-connect-master-node-ssh.md").
