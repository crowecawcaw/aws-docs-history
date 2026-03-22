# Creating a DAX cluster using the AWS CLI

This section describes how to create an Amazon DynamoDB Accelerator (DAX) cluster using the
AWS Command Line Interface (AWS CLI). If you haven't already done so, you must install and configure the AWS CLI.
To do this, see the following instructions in the
_AWS Command Line Interface User Guide_:

- [Installing the AWS CLI](../../../cli/latest/userguide/installing.md "../../../cli/latest/userguide/installing.md")
- [Configuring the
  AWS CLI](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md")

###### Important

To manage DAX clusters using the AWS CLI, install or upgrade to version 1.11.110 or
higher.

All of the AWS CLI examples use the `us-west-2` Region and fictitious account
IDs.

###### Topics

- [Step 1: Create a service role](#DAX.create-cluster.cli.create-service-role "#DAX.create-cluster.cli.create-service-role")
- [Step 2: Create a subnet group](#DAX.create-cluster.cli.create-subnet-group "#DAX.create-cluster.cli.create-subnet-group")
- [Step 3: Create a DAX cluster](#DAX.create-cluster.cli.create-cluster "#DAX.create-cluster.cli.create-cluster")
- [Step 4: Configure security group inbound rules](#DAX.create-cluster.cli.configure-inbound-rules "#DAX.create-cluster.cli.configure-inbound-rules")

## Step 1: Create an IAM service role for DAX to access DynamoDB using the AWS CLI

Before you can create an Amazon DynamoDB Accelerator (DAX) cluster, you must create a service
role for it. A _service role_ is an AWS Identity and Access Management (IAM) role that
authorizes an AWS service to act on your behalf. The service role allows DAX to
access your DynamoDB tables as if you were accessing those tables yourself.

In this step, you create an IAM policy and then attach that policy to an IAM role.
This enables you to assign the role to a DAX cluster so that it can perform DynamoDB
operations on your behalf.

###### To create an IAM service role for DAX

1. Create a file named `service-trust-relationship.json` with
   the following contents.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "dax.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

2. Create the service role.

```
aws iam create-role \
    --role-name DAXServiceRoleForDynamoDBAccess \
    --assume-role-policy-document file://service-trust-relationship.json
```

3. Create a file named `service-role-policy.json` with the
   following contents.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "dynamodb:DescribeTable",
 "dynamodb:PutItem",
 "dynamodb:GetItem",
 "dynamodb:UpdateItem",
 "dynamodb:DeleteItem",
 "dynamodb:Query",
 "dynamodb:Scan",
 "dynamodb:BatchGetItem",
 "dynamodb:BatchWriteItem",
 "dynamodb:ConditionCheckItem"
 ],
 "Effect": "Allow",
 "Resource": [
 "arn:aws:dynamodb:`us-west-2`:`111122223333`:*"
 ]
 }
 ]
}`

```

Replace `accountID` with your AWS account ID. To
find your AWS account ID, in the upper-right corner of the console, choose
your login ID. Your AWS account ID appears in the drop-down menu.

In the Amazon Resource Name (ARN) in the example,
`accountID` must be a 12-digit number. Don't use
hyphens or any other punctuation. 4. Create an IAM policy for the service role.

```
aws iam create-policy \
    --policy-name DAXServicePolicyForDynamoDBAccess \
    --policy-document file://service-role-policy.json
```

In the output, note the ARN for the policy that you created, as in the
following example.

`arn:aws:iam::123456789012:policy/DAXServicePolicyForDynamoDBAccess` 5. Attach the policy to the service role. Replace `arn`
in the following code with the actual role ARN from the previous step.

```
aws iam attach-role-policy \
    --role-name DAXServiceRoleForDynamoDBAccess \
    --policy-arn `arn`
```

Next, you specify a subnet group for your default VPC. A _subnet group_ is a collection of one or more subnets within your VPC. See
[Step 2: Create a subnet group](#DAX.create-cluster.cli.create-subnet-group "#DAX.create-cluster.cli.create-subnet-group").

## Step 2: Create a subnet group

Follow this procedure to create a subnet group for your Amazon DynamoDB Accelerator (DAX)
cluster using the AWS Command Line Interface (AWS CLI).

###### Note

If you already created a subnet group for your default VPC, you can skip this
step.

DAX is designed to run within an Amazon Virtual Private Cloud environment (Amazon VPC). If you created your
AWS account after December 4, 2013, you already have a default VPC in each AWS
Region. For more information, see [Default
VPC and default subnets](../../../vpc/latest/userguide/default-vpc.md "../../../vpc/latest/userguide/default-vpc.md") in the _Amazon VPC User Guide_.

###### To create a subnet group

1. To determine the identifier for your default VPC, enter the following
   command.

```
aws ec2 describe-vpcs
```

In the output, note the identifier for your default VPC, as in the following
example.

`vpc-12345678` 2. Determine the subnet IDs associated with your default VPC. Replace
`vpcID` with your actual VPC ID—for example,
`vpc-12345678`.

```
aws ec2 describe-subnets \
    --filters "Name=vpc-id,Values=`vpcID`" \
    --query "Subnets[*].SubnetId"
```

In the output, note the subnet identifiers—for example,
`subnet-11111111`. 3. Create the subnet group. Ensure that you specify at least one subnet ID in the
`--subnet-ids` parameter.

```
aws dax create-subnet-group \
    --subnet-group-name my-subnet-group \
    --subnet-ids `subnet-11111111` `subnet-22222222` `subnet-33333333` `subnet-44444444`
```

To create the cluster, see [Step 3: Create a DAX cluster using the AWS CLI](#DAX.create-cluster.cli.create-cluster "#DAX.create-cluster.cli.create-cluster").

## Step 3: Create a DAX cluster using the AWS CLI

Follow this procedure to use the AWS Command Line Interface (AWS CLI) to create an Amazon DynamoDB Accelerator
(DAX) cluster in your default Amazon VPC.

###### To create a DAX cluster

1. Get the Amazon Resource Name (ARN) for your service role.

```
aws iam get-role \
    --role-name DAXServiceRoleForDynamoDBAccess \
    --query "Role.Arn" --output text
```

In the output, note the service role ARN, as in the following example.

`arn:aws:iam::123456789012:role/DAXServiceRoleForDynamoDBAccess` 2. Create the DAX cluster. Replace
`roleARN` with the ARN from the
previous step.

```
aws dax create-cluster \
    --cluster-name mydaxcluster \
    --node-type dax.r4.large \
    --replication-factor 3 \
    --iam-role-arn `roleARN` \
    --subnet-group my-subnet-group \
    --sse-specification Enabled=true \
    --region us-west-2
```

All of the nodes in the cluster are of type `dax.r4.large`
(`--node-type`). There are three nodes
(`--replication-factor`)—one primary node and two
replicas.

###### Note

Since `sudo` and `grep` are reserved keywords, you
cannot create a DAX cluster with these words in the cluster name. For
example, `sudo` and `sudocluster` are invalid cluster
names.

To view the cluster status, enter the following command.

```
aws dax describe-clusters
```

The status is shown in the output—for example, `"Status":
 "creating"`.

###### Note

Creating the cluster takes several minutes. When the cluster is ready, its status
changes to `available`. In the meantime, proceed to [Step 4: Configure security group inbound rules using the AWS CLI](#DAX.create-cluster.cli.configure-inbound-rules "#DAX.create-cluster.cli.configure-inbound-rules") and follow the
instructions there.

## Step 4: Configure security group inbound rules using the AWS CLI

The nodes in your Amazon DynamoDB Accelerator (DAX) cluster use the default security group for
your Amazon VPC. For the default security group, you must authorize inbound traffic on TCP
port 8111 for unencrypted clusters or port 9111 for encrypted clusters. This allows
Amazon EC2 instances in your Amazon VPC to access your DAX cluster.

###### Note

If you launched your DAX cluster with a different security group (other than
`default`), you must perform this procedure for that group
instead.

###### To configure security group inbound rules

1. To determine the default security group identifier, enter the following
   command. Replace `vpcID` with your actual
   VPC ID (from [Step 2: Create a subnet group](#DAX.create-cluster.cli.create-subnet-group "#DAX.create-cluster.cli.create-subnet-group")).

```
aws ec2 describe-security-groups \
    --filters Name=vpc-id,Values=`vpcID` Name=group-name,Values=default \
    --query "SecurityGroups[*].{GroupName:GroupName,GroupId:GroupId}"
```

In the output, note the security group identifier—for example,
`sg-01234567`. 2. Then enter the following. Replace `sgID`
with your actual security group identifier. Use port `8111` for
unencrypted clusters and `9111` for encrypted clusters.

```
aws ec2 authorize-security-group-ingress \
    --group-id `sgID` --protocol tcp --port `8111`
```
