# Creating a cluster with an external Slurmdbd accounting

Learn how to conﬁgure and create a cluster with external Slurmdbd accounting. For more information,
see [Slurm accounting with AWS ParallelCluster](slurm-accounting-v3.md "slurm-accounting-v3.md").

When using the AWS ParallelCluster command line interface (CLI) or API, you only pay for the AWS
resources that are created when you create or update AWS ParallelCluster images and clusters. For more
information, see [AWS services used by AWS ParallelCluster](aws-services-v3.md "aws-services-v3.md").

The AWS ParallelCluster UI is built on a serverless architecture and you can use it within the
AWS Free Tier category for most cases. For more information, see
[AWS ParallelCluster UI costs](install-pcui-costs-v3.md "install-pcui-costs-v3.md").

In this tutorial, you use a AWS CloudFormation quick-create template to create the necessary components to deploy a Slurmdbd instance on the same VPC as the cluster. The template creates a basic networking and security conﬁguration for the connection between the cluster and the database.

###### Note

Starting with `version 3.10.0`, AWS ParallelCluster supports external Slurmdbd with the cluster conﬁguration parameter `SlurmSettings / ExternelSlurmdbd`.

###### Note

The quick-create template serves as an example. This template doesn't cover all possible use cases. It's your responsibility to create an external Slurmdbd with the conﬁguration and capacity appropriate for your production workloads.

###### Prerequisites:

- AWS ParallelCluster [is installed](install-v3-parallelcluster.md "install-v3-parallelcluster.md").
- The AWS CLI [is installed and configured.](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md")
- You have an [Amazon Elastic Compute Cloud key pair](../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md "../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md").
- You have an AWS Identity and Access Management role with the [permissions](iam-roles-in-parallelcluster-v3.md#iam-roles-in-parallelcluster-v3-example-user-policies "iam-roles-in-parallelcluster-v3.md#iam-roles-in-parallelcluster-v3-example-user-policies") that are required to run the [pcluster](pcluster-v3.md "pcluster-v3.md") CLI.
- You have a Slurm accounting database. To step through a tutorial of creating Slurm accounting
  database, follow steps 1 and 2 in [Create the Slurm
  Accounting Database stack](tutorials_07_slurm-accounting-v3.md "tutorials_07_slurm-accounting-v3.md").

## Step 1: Create the Slurmdbd stack

In this tutorial, use a [CloudFormation
quick-create template (`us-east-1`)](https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=pcluster-slurm-dbd&templateURL=https://us-east-1-aws-parallelcluster.s3.amazonaws.com/templates/1-click/external-slurmdbd.json "https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=pcluster-slurm-dbd&templateURL=https://us-east-1-aws-parallelcluster.s3.amazonaws.com/templates/1-click/external-slurmdbd.json") to create a Slurmdbd stack. The template requires following inputs:

###### Networking

- **VPCId**: The VPC ID to launch the Slurmdbd instance.
- **SubnetId**: The Subnet ID to launch the Slurmdbd instance.
- **PrivatePrefix**: The CIDR prefix of the VPC.
- **PrivateIp**: A secondary private IP to assign to the Slurmdbd instance.

###### Database connection

- **DBMSClientSG**: The security group to be attach to the Slurmdbd instance. This security group should allows connections between the database server and the Slurmdbd instance.
- **DBMSDatabaseName**: The name of the database.
- **DBMSUsername**: The username to the database.
- **DBMSPasswordSecretArn**: The secret containing the password to the database.
- **DBMSUri**: The URI of the database server.

###### Instance settings

- **InstanceType**: An instance type to use for the slurmdbd instance.
- **KeyName**: An Amazon EC2 key pair to use for the slurmdbd instance.

###### Slurmdbd settings

- **AMIID**: An AMI of the Slurmdbd instance. The AMI should be a ParallelCluster AMI. The version of the ParallelCluster AMI determines the version of Slurmdbd.
- **MungeKeySecretArn**: The secret containing the munge key to use for authenticating communications between Slurmdbd and clusters.
- **SlurmdbdPort**: A port number that the slurmdbd uses.
- **EnableSlurmdbdSystemService**: Enables slurmdbd as system service and have it run when an instance launches.

###### Warning

If the database was created by a different version of SlurmDB, do not use Slurmdbd as a system service.

If the database contains a large number of entries, the Slurm Database Daemon (SlurmDBD) may require tens of minutes to update the database and be unresponsive during this time interval.

Before upgrading SlurmDB, make a backup of the database. For more information, see the [Slurm documentation](https://slurm.schedmd.com/quickstart_admin.html#upgrade "https://slurm.schedmd.com/quickstart_admin.html#upgrade").

## Step 2: Create a cluster with external Slurmdbd enabled

The provided AWS CloudFormation template generates a AWS CloudFormation stack with some deﬁned outputs.

From the AWS Management Console, view the **Outputs** tab in the AWS CloudFormation stack to review the entities created. To enable the Slurm accounting, some of these outputs must be used in the AWS ParallelCluster conﬁguration ﬁle:

- **SlurmdbdPrivateIp**: Used for the
  [SlurmSettings](Scheduling-v3.md#Scheduling-v3-SlurmSettings "Scheduling-v3.md#Scheduling-v3-SlurmSettings") /
  [ExternalSlurmdbd](Scheduling-v3.md#Scheduling-v3-SlurmSettings-ExternalSlurmdbd "Scheduling-v3.md#Scheduling-v3-SlurmSettings-ExternalSlurmdbd") /
  [Host cluster conﬁg](Scheduling-v3.md#yaml-Scheduling-SlurmSettings-ExternalSlurmdbd-Host "Scheduling-v3.md#yaml-Scheduling-SlurmSettings-ExternalSlurmdbd-Host")
  parameter.
- **SlurmdbdPort**: Used for the [SlurmSettings](Scheduling-v3.md#Scheduling-v3-SlurmSettings "Scheduling-v3.md#Scheduling-v3-SlurmSettings") / [ExternalSlurmdbd](Scheduling-v3.md#Scheduling-v3-SlurmSettings-ExternalSlurmdbd "Scheduling-v3.md#Scheduling-v3-SlurmSettings-ExternalSlurmdbd") / [Port](Scheduling-v3.md#yaml-Scheduling-SlurmSettings-ExternalSlurmdbd-Port "Scheduling-v3.md#yaml-Scheduling-SlurmSettings-ExternalSlurmdbd-Port") cluster conﬁguration parameter value.
- **AccountingClientSecurityGroup**: This is the security group that's
  attached to the head node of the cluster that's deﬁned in the [HeadNode](HeadNode-v3.md "HeadNode-v3.md") /
  [Networking](HeadNode-v3.md#HeadNode-v3-Networking "HeadNode-v3.md#HeadNode-v3-Networking") /
  [AdditionalSecurityGroups](HeadNode-v3.md#yaml-HeadNode-Networking-AdditionalSecurityGroups "HeadNode-v3.md#yaml-HeadNode-Networking-AdditionalSecurityGroups")
  conﬁguration parameter.

Additional, from the **Parameters** tab in the AWS CloudFormation stack view:

- **MungeKeySecretArn**: Used for the
  [SlurmSettings](Scheduling-v3.md#Scheduling-v3-SlurmSettings "Scheduling-v3.md#Scheduling-v3-SlurmSettings") /
  [MungeKeySecretArn](Scheduling-v3.md#yaml-Scheduling-SlurmSettings-MungeKeySecretArn "Scheduling-v3.md#yaml-Scheduling-SlurmSettings-MungeKeySecretArn")
  cluster conﬁguration parameter value.

Update your cluster conﬁguration ﬁle database parameters with the output values. Use the pcluster AWS CLI to create the cluster.

```
`$`  pcluster create-cluster -n `cluster-3.x`-c `path/to/cluster-config.yaml`
```

After the cluster is created, you can start using Slurm accounting commands such as `sacctmgr` or `sacct`.

###### Warning

Traffic between `ParallelCluster` and the external SlurmDB is not encrypted. It is recommended to run the cluster and the external SlurmDB in a trusted network.
