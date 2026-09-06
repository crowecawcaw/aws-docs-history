

# Complete prerequisite steps for using Amazon EMR with Trino
<a name="emr-trino-getting-started-pre"></a>

If you haven't used AWS, or if you haven't created an Amazon EMR cluster, complete these prerequisite steps before you create an Amazon EMR cluster with Trino.

## AWS environment set up
<a name="emr-trino-getting-started-account"></a>

Complete these steps to configure your AWS account if you haven't already:

1. Sign up for an AWS account, if you don't have one already. For more information, see [Create an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-creating.html) in the *AWS Account Management Reference Guide*.

1. Sign in to your account as an administrative user.

1. Create a group and assign users to it.

1. Create an Amazon EC2 key pair, which you can use later to secure communication between resources with SSH. This step is required if you plan to connect to the primary node to perform tasks. For more information, see [Connect to the Amazon EMR cluster primary node using SSH](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-connect-master-node-ssh.html).