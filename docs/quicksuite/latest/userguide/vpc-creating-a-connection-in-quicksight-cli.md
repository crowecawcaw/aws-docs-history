# Configuring the VPC

connection with the Amazon Quick Suite CLI

To create a secure private connection to the Amazon VPC service from Quick Suite with
the Amazon Quick Suite CLI, use the following procedure:

###### Prerequisites

- Before you begin, make sure that you have the following information available
  to copy and paste into the **VPC Connection** page. For more
  information, see [Finding information to connect to a VPC](../../../quicksight/latest/user/vpc-finding-setup-information.md "../../../quicksight/latest/user/vpc-finding-setup-information.md").
  - AWS Region – The AWS Region where you plan
    to create a connection to your data source.
  - VPC ID – The ID of the VPC that contains the
    data, the subnets, and the security groups that you plan to use.
  - Execution role– An IAM role that contains a
    trust policy that allows Amazon Quick Suite to create, update, and delete
    network infrastructure in your account. This policy is required for all
    VPC connections. At minimum, the IAM policy needs the following Amazon EC2
    permissions:

        - `DescribeSecurityGroups`
        - `DescribeSubnets`
        - `CreateNetworkInterface`
        - `DeleteNetworkInterface`
        - `ModifyNetworkInterfaceAttribute`

    The following example shows an IAM policy that you can add to an
    existing IAM role to create, delete, or modify a VPC
    connection:

  JSON

  ```
  `{
   "Version":"2012-10-17",
   "Statement": [
   {
   "Effect": "Allow",
   "Action": [
   "ec2:CreateNetworkInterface",
   "ec2:ModifyNetworkInterfaceAttribute",
   "ec2:DeleteNetworkInterface",
   "ec2:DescribeSubnets",
   "ec2:DescribeSecurityGroups"
   ],
   "Resource": "*"
   }
   ]
  }`

  ```

  After you add the necessary permissions to an IAM role, attach a
  trust policy to allow Amazon Quick Suite to configure the VPC connection to
  your account. The following shows an example trust policy that you can
  add to an existing IAM role to allow Amazon Quick Suite access to the
  role:

  JSON

  ```
  `{
   "Version":"2012-10-17",
   "Statement": [
   {
   "Effect": "Allow",
   "Principal": {
   "Service": "quicksight.amazonaws.com"
   },
   "Action": "sts:AssumeRole"
   }
   ]
  }`

  ```

  - Subnet IDs – The IDs of the subnets that the
    Amazon Quick Suite network interface is using. Each VPC connection needs at
    least two subnets.
  - Security group IDs – The IDs of the security
    groups. Each VPC connection needs at least one security group.

## Using the

AWS CLI

The following example creates a VPC connection.

```
aws quicksight create-vpc-connection \
--aws-account-id `123456789012`\
--vpc-connection-id `test` \
--name `test` \
--subnet-ids '["`subnet-12345678`", "`subnet-12345678`"]' \
--security-group-ids '["`sg-12345678`"]' \
--role-arn arn:aws:iam::`123456789012`:role/`test-role` \
--region `us-west-2`


```

After you create a VPC connection, you can update, delete, or request a summary of
the VPC connection.

The following example updates a VPC connection.

```
aws quicksight update-vpc-connection \
--aws-account-id `123456789012` \
--vpc-connection-id `test` \
--name `test` \
--subnet-ids '["`subnet-12345678`", "`subnet-12345678`"]' \
--security-group-ids '["`sg-12345678`"]' \
--role-arn arn:aws:iam::`123456789012`:role/`test-role` \
--region `us-west-2`

```

The following example deletes a VPC connection.

```
aws quicksight delete-vpc-connection \
--aws-account-id `123456789012` \
--vpc-connection-id `test` \
--region `us-west-2`

```

The following example describes a VPC connection.

```
aws quicksight describe-vpc-connection \
--aws-account-id `123456789012` \
--vpc-connection-id `test` \
--region `us-west-2`

```

The following table describes the different **Status** values for
a network interface that `describe-vpc-connection` returns.

| Status                                | Description                                                                                                                                            |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CREATING**                          | The network interface creation is in progress.                                                                                                         |
| **AVAILABLE**                         | The network interface is available for use.                                                                                                            |
| **CREATION_FAILURE**                  | The network interface couldn't be created.                                                                                                             |
| **UPDATING**                          | The security group associated with the network inferface is updating.                                                                                  |
| **UPDATE_FAILED**                     | The security group associated with the network interface did not update successfully.                                                                  |
| **DELETING**                          | The network interface is in the process of being deleted.                                                                                              |
| **DELETED**                           | The network interface is deleted and can no longer be used.                                                                                            |
| **DELETION_FAILED**                   | The network interface deletion failed and can still be used.                                                                                           |
| **DELETION_SCHEDULED**                | This network interface is scheduled for deletion.                                                                                                      |
| **ATTACHMENT_FAILED_ROLLBACK_FAILED** | The elastic interface failed to attach and Amazon Quick Suite was unable to delete the elastic network interface that was created within your account. | You can also use the AWS CLI to generate a list of all VPC connections in your Amazon Quick Suite account. `` aws quicksight list-vpc-connections \ --aws-account-id `123456789012` \ --`region us-west-2` `` |
