# Automatically connecting a Lambda function and a Multi-AZ DB cluster

You can use the RDS console to simplify setting up a connection between a Lambda function and
a Multi-AZ DB cluster. You can use the RDS console to simplify setting up a connection between a Lambda
function and a Multi-AZ DB cluster. Often, your Multi-AZ DB cluster is in a private subnet within a VPC. The Lambda
function can be used by applications to access your private Multi-AZ DB cluster.

The following image shows a direct connection between your Multi-AZ DB cluster and your Lambda
function.

![Automatically connect a Multi-AZ DB cluster with a Lambda function.](images/auto-connect-maz-lambda.png)
You can set up the connection between your Lambda function and your database through
RDS Proxy to improve your database performance and resiliency. Often, Lambda functions make
frequent, short database connections that benefit from connection pooling that RDS Proxy
offers. You can take advantage of any IAM authentication that you already have for
Lambda functions, instead of managing database credentials in your Lambda application
code. For more information, see [Amazon RDS Proxy](rds-proxy.md "rds-proxy.md").

You can use the console to automatically create a proxy for your connection.
You can also select existing proxies. The console updates the proxy security
group to allow connections from your database and Lambda function. You can input
your database credentials or select the Secrets Manager secret you require to access the
database.

![Automatically connect a Multi-AZ DB cluster with a Lambda function through RDS Proxy.](images/auto-connect-maz-lambda-Proxy.png)

###### Topics

- [Overview of automatic connectivity with a Lambda function](#multiaz-lambda-rds-connect-overview "#multiaz-lambda-rds-connect-overview")
- [Automatically connecting a Lambda function and a Multi-AZ DB cluster](#multiaz-lambda-rds-connect-connecting "#multiaz-lambda-rds-connect-connecting")
- [Viewing connected compute resources](#multiaz-lambda-rds-connect-viewing "#multiaz-lambda-rds-connect-viewing")

## Overview of automatic connectivity with a Lambda function

When you set up a connection between a Lambda function and a Multi-AZ DB cluster automatically, Amazon RDS configures the VPC
security group for your Lambda function and for your DB cluster.

The following are requirements for connecting a Lambda function with a Multi-AZ DB cluster:

- The Lambda function must exist in the same VPC as the Multi-AZ DB cluster.

If no Lambda function exists in the same VPC, the console provides a link to create one.

- The user who sets up connectivity must have permissions to perform the following Amazon RDS, Amazon EC2, Lambda, Secrets Manager,
  and IAM operations:
  - Amazon RDS
    - `rds:CreateDBProxies`
    - `rds:DescribeDBInstances`
    - `rds:DescribeDBProxies`
    - `rds:ModifyDBInstance`
    - `rds:ModifyDBProxy`
    - `rds:RegisterProxyTargets`

  - Amazon EC2
    - `ec2:AuthorizeSecurityGroupEgress`
    - `ec2:AuthorizeSecurityGroupIngress`
    - `ec2:CreateSecurityGroup`
    - `ec2:DeleteSecurityGroup`
    - `ec2:DescribeSecurityGroups`
    - `ec2:RevokeSecurityGroupEgress`
    - `ec2:RevokeSecurityGroupIngress`

  - Lambda
    - `lambda:CreateFunctions`
    - `lambda:ListFunctions`
    - `lambda:UpdateFunctionConfiguration`

  - Secrets Manager
    - `sercetsmanager:CreateSecret`
    - `secretsmanager:DescribeSecret`

  - IAM
    - `iam:AttachPolicy`
    - `iam:CreateRole`
    - `iam:CreatePolicy`

  - AWS KMS
    - `kms:describeKey`

When you set up a connection between a Lambda function and a Multi-AZ DB cluster, Amazon RDS configures the VPC
security group for your function and for your Multi-AZ DB cluster. If you use RDS Proxy, then Amazon RDS
also configures the VPC security group for the proxy. Amazon RDS acts according to the
current configuration of the security groups associated with the Multi-AZ DB cluster and Lambda
function, and proxy, as described in the following table.

| Current RDS security group configuration                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Current Lambda security group configuration                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Current proxy security group configuration                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | RDS action                                                                                                                                                                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Amazon RDS takes no action because security groups of all resources<br>follow the correct naming pattern and have the right inbound and<br>outbound rules.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | There are one or more security groups associated with the<br>Multi-AZ DB cluster with a name that matches the pattern<br>`rds-lambda-`n`<br>(where `n``is a number) or<br>if the`TargetHealth` of an associated proxy is<br>`AVAILABLE`.<br>A security group that matches the pattern hasn't been<br>modified. This security group has only one inbound rule with the<br>VPC security group of the Lambda function or proxy as the<br>source.                                                                                                                                                                                                                                                                                                       | There are one or more security groups associated with the<br>Lambda function with a name that matches the pattern<br>`lambda-rds-`n`` or<br>`lambda-rdsproxy-`n``<br>(where `n` is a<br>number).<br>A security group that matches the pattern hasn't been<br>modified. This security group has only one outbound rule with<br>either the VPC security group of the Multi-AZ DB cluster or the proxy as the<br>destination.                                                                                                                                                                                                                                                                 | There are one or more security groups associated with the<br>proxy with a name that matches the pattern<br>`rdsproxy-lambda-`n`<br>(where `n`` is a<br>number).<br>A security group that matches the pattern hasn't been<br>modified. This security group has inbound and outbound rules<br>with the VPC security groups of the Lambda function and the<br>Multi-AZ DB cluster. |
| Either of the following conditions apply:<br>• There is no security group associated with the Multi-AZ DB cluster<br>with a name that matches the pattern<br>`rds-lambda-`n``<br>or if the `TargetHealth` of an associated<br>proxy is `AVAILABLE`.<br>• There are one or more security groups associated with<br>the Multi-AZ DB cluster with a name that matches the pattern<br>`rds-lambda-`n``<br>or if the `TargetHealth` of an associated<br>proxy is `AVAILABLE`. However, Amazon RDS can't<br>use any of these security groups for the connection with<br>the Lambda function.<br>Amazon RDS can't use a security group that doesn't have one inbound rule with the VPC<br>security group of the Lambda function or proxy as the source.<br>Amazon RDS also can't use a security group that has been<br>modified. Examples of modifications include adding a rule or<br>changing the port of an existing rule. | Either of the following conditions apply:<br>• There is no security group associated with the Lambda<br>function with a name that matches the pattern<br>`lambda-rds-`n``<br>or<br>`lambda-rdsproxy-`n``.<br>• There are one or more security groups associated with the Lambda function with a name<br>that matches the pattern<br>`lambda-rds-`n``<br>or<br>`lambda-rdsproxy-`n``.<br>However, Amazon RDS can't use any of these security<br>groups for the connection with the Multi-AZ DB cluster.<br>Amazon RDS can't use a security group if it doesn't have one outbound rule with the<br>VPC security group of the Multi-AZ DB cluster or proxy as the source. Amazon RDS<br>also can't use a security group that has been<br>modified.     | Either of the following conditions apply:<br>• There is no security group associated with the proxy<br>with a name that matches the pattern<br>`rdsproxy-lambda-`n``.<br>• There are one or more security groups associated with<br>the proxy with a name that matches<br>`rdsproxy-lambda-`n``.<br>However, Amazon RDS can't use any of these security<br>groups for the connection with the Multi-AZ DB cluster or Lambda<br>function.<br>Amazon RDS can't use a security group that doesn't<br>have inbound and outbound rules with the VPC security group of the<br>Multi-AZ DB cluster and the Lambda function. Amazon RDS also can't use a security<br>group that has been modified. | [RDS action: create new security groups](#maz-lam-action-create-new-security-groups "#maz-lam-action-create-new-security-groups")                                                                                                                                                                                                                                               |
| There are one or more security groups associated with the<br>Multi-AZ DB cluster with a name that matches the pattern<br>`rds-lambda-`n``or<br>if the`TargetHealth` of an associated proxy is<br>`AVAILABLE`.<br>A security group that matches the pattern hasn't been<br>modified. This security group has only one inbound rule with the<br>VPC security group of the Lambda function or proxy as the<br>source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | There are one or more security groups associated with the<br>Lambda function with a name that matches the pattern<br>`lambda-rds-`n`` or<br>`lambda-rdsproxy-`n``.<br>However, Amazon RDS can't use any of these security groups for the connection with the<br>Multi-AZ DB cluster. Amazon RDS can't use a security group that doesn't have<br>one outbound rule with the VPC security group of the Multi-AZ DB cluster or<br>proxy as the destination. Amazon RDS also can't use a security<br>group that has been modified.                                                                                                                                                                                                                      | There are one or more security groups associated with the<br>proxy with a name that matches the pattern<br>`rdsproxy-lambda-`n``.<br>However, Amazon RDS can't use any of these security groups for the connection with the<br>Multi-AZ DB cluster or Lambda function. Amazon RDS can't use a security group<br>that doesn't have inbound and outbound rules with the VPC<br>security group of the Multi-AZ DB cluster and the Lambda function. Amazon RDS also<br>can't use a security group that has been modified.                                                                                                                                                                      | [RDS action: create new security groups](#maz-lam-action-create-new-security-groups "#maz-lam-action-create-new-security-groups")                                                                                                                                                                                                                                               |
| There are one or more security groups associated with the<br>Multi-AZ DB cluster with a name that matches the pattern<br>`rds-lambda-`n``or<br>if the`TargetHealth` of an associated proxy is<br>`AVAILABLE`.<br>A security group that matches the pattern hasn't been<br>modified. This security group has only one inbound rule with the<br>VPC security group of the Lambda function or proxy as the<br>source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | A valid Lambda security group for the connection exists, but it<br>is not associated with the Lambda function. This security group<br>has a name that matches the pattern<br>`lambda-rds-`n`` or<br>`lambda-rdsproxy-`n``.<br>It hasn't been modified. It has only one outbound rule with the<br>VPC security group of the Multi-AZ DB cluster or proxy as the<br>destination.                                                                                                                                                                                                                                                                                                                                                                      | A valid proxy security group for the connection exists, but it<br>is not associated with the proxy. This security group has a name<br>that matches the pattern<br>`rdsproxy-lambda-`n``.<br>It hasn't been modified. It has inbound and outbound rules with<br>the VPC security group of the Multi-AZ DB cluster and the Lambda<br>function.                                                                                                                                                                                                                                                                                                                                               | [RDS action: associate Lambda security group](#maz-lam-action-associate-lam-security-group "#maz-lam-action-associate-lam-security-group")                                                                                                                                                                                                                                      |
| Either of the following conditions apply:<br>• There is no security group associated with the Multi-AZ DB cluster<br>with a name that matches the pattern<br>`rds-lambda-`n``<br>or if the `TargetHealth` of an associated<br>proxy is `AVAILABLE`.<br>• There are one or more security groups associated with the Multi-AZ DB cluster with a name that<br>matches the pattern<br>`rds-lambda-`n``<br>or if the `TargetHealth` of an associated<br>proxy is `AVAILABLE`. However, Amazon RDS<br>can'can't use any of these security groups for<br>the connection with the Lambda function or proxy.<br>Amazon RDS can't use a security group that doesn't have one inbound rule with the<br>VPC security group of the Lambda function or proxy as the<br>source. Amazon RDS also can't use a security group that<br>has been modified.                                                                                 | There are one or more security groups associated with the<br>Lambda function with a name that matches the pattern<br>`lambda-rds-`n`` or<br>`lambda-rdsproxy-`n``.<br>A security group that matches the pattern hasn't been<br>modified. This security group has only one outbound rule with<br>the VPC security group of the Multi-AZ DB cluster or proxy as the<br>destination.                                                                                                                                                                                                                                                                                                                                                                   | There are one or more security groups associated with the<br>proxy with a name that matches the pattern<br>`rdsproxy-lambda-`n``.<br>A security group that matches the pattern hasn't been<br>modified. This security group has inbound and outbound rules<br>with the VPC security group of the Multi-AZ DB cluster and the Lambda<br>function.                                                                                                                                                                                                                                                                                                                                           | [RDS action: create new security groups](#maz-lam-action-create-new-security-groups "#maz-lam-action-create-new-security-groups")                                                                                                                                                                                                                                               |
| There are one or more security groups associated with the<br>Multi-AZ DB cluster with a name that matches the pattern<br>`rds-rdsproxy-`n`<br>(where `n`` is a number).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Either of the following conditions apply:<br>• There is no security group associated with the Lambda<br>function with a name that matches the pattern<br>`lambda-rds-`n``<br>or<br>`lambda-rdsproxy-`n``.<br>• There are one or more security groups associated with the Lambda function with a name<br>that matches the pattern<br>`lambda-rds-`n``<br>or<br>`lambda-rdsproxy-`n``.<br>However, Amazon RDS can't use any of these security<br>groups for the connection with the Multi-AZ DB cluster.<br>Amazon RDS can't use a security group that doesn't have one outbound rule with the VPC<br>security group of the Multi-AZ DB cluster or proxy as the destination. Amazon RDS<br>also can't use a security group that has been<br>modified. | Either of the following conditions apply:<br>• There is no security group associated with the proxy<br>with a name that matches the pattern<br>`rdsproxy-lambda-`n``.<br>• There are one or more security groups associated with<br>the proxy with a name that matches<br>`rdsproxy-lambda-`n``.<br>However, Amazon RDS can't use any of these security<br>groups for the connection with the Multi-AZ DB cluster or Lambda<br>function.<br>Amazon RDS can't use a security group that doesn't<br>have inbound and outbound rules with the VPC security group of the<br>Multi-AZ DB cluster and the Lambda function. Amazon RDS also can't use a security<br>group that has been modified. | [RDS action: create new security groups](#maz-lam-action-create-new-security-groups "#maz-lam-action-create-new-security-groups")                                                                                                                                                                                                                                               |

###### RDS action: create new security groups

Amazon RDS takes the following actions:

- Creates a new security group that matches the pattern
  `rds-lambda-`n``.This security group has an inbound rule with the
  VPC security group of the Lambda function or proxy as the source. This security group is associated with the
  Multi-AZ DB cluster and allows the function or proxy to access the Multi-AZ DB cluster.
- Creates a new security group that matches the pattern `lambda-rds-`n``.
  This security group has an outbound rule with the VPC security group of the Multi-AZ DB cluster or proxy as the
  destination. This security group is associated with the Lambda function and allows the Lambda function to send
  traffic to the Multi-AZ DB cluster or send traffic through a proxy.
- Creates a new security group that matches the pattern
  `rdsproxy-lambda-`n``. This security group has inbound and outbound
  rules with the VPC security group of the Multi-AZ DB cluster and the Lambda function.

###### RDS action: associate Lambda security group

Amazon RDS associates the valid, existing Lambda security group with the Lambda function. This security group allows
the function to send traffic to the Multi-AZ DB cluster or send traffic through a proxy.

## Automatically connecting a Lambda function and a Multi-AZ DB cluster

You can use the Amazon RDS console to automatically connect a Lambda function to your Multi-AZ DB cluster. This simplifies the
process of setting up a connection between these resources.

You can also use RDS Proxy to include a proxy in your connection. Lambda functions make frequent short
database connections that benefit from the connection pooling that RDS Proxy offers. You can also use any IAM
authentication that you've already set up for your Lambda function, instead of managing database credentials in
your Lambda application code.

You can connect an existing Multi-AZ DB cluster to new and existing Lambda functions using the **Set up Lambda
connection** page. The setup process automatically sets up the required security groups for
you.

Before setting up a connection between a Lambda function and a Multi-AZ DB cluster, make sure that:

- Your Lambda function and Multi-AZ DB cluster are in the same VPC.
- You have the right permissions for your user account. For more
  information about the requirements, see [Overview of automatic connectivity with a Lambda function](lambda-rds-connect.md#lambda-rds-connect-overview "lambda-rds-connect.md#lambda-rds-connect-overview").

If you change security groups after you configure connectivity, the changes might affect the connection
between the Lambda function and the Multi-AZ DB cluster.

###### Note

You can automatically set up a connection between a Multi-AZ DB cluster and a Lambda function only in the AWS Management Console. To
connect a Lambda function, all instances in the Multi-AZ DB cluster must be in the **Available**
state.

###### To automatically connect a Lambda function and a Multi-AZ DB cluster

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**, and then choose the Multi-AZ DB cluster that you want to
   connect to a Lambda function.
3. For **Actions**, choose **Set up Lambda connection**.
4. On the **Set up Lambda connection** page, under **Select Lambda
   function**, do either of the following:
   - If you have an existing Lambda function in the same VPC as your Multi-AZ DB cluster, choose **Choose
     existing function**, and then choose the function.
   - If you don't have a Lambda function in the same VPC, choose **Create new
     function**, and then enter a **Function name**. The default runtime is set
     to Nodejs.18. You can modify the settings for your new Lambda function in the Lambda console after you
     complete the connection setup.

5. (Optional) Under **RDS Proxy**, select **Connect using RDS Proxy**,
   and then do any of the following:
   - If you have an existing proxy that you want to use, choose **Choose existing
     proxy**, and then choose the proxy.
   - If you don't have a proxy, and you want Amazon RDS to automatically create one for you, choose
     **Create new proxy**. Then, for **Database credentials**, do
     either of the following:
     1. Choose **Database username and password**, and then enter the
        **Username** and **Password** for your Multi-AZ DB cluster.
     2. Choose **Secrets Manager secret**. Then, for **Select
        secret**, choose an AWS Secrets Manager secret. If you don't have a Secrets Manager secret, choose
        **Create new Secrets Manager secret** to [create a new secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md"). After you
        create the secret, for **Select secret**, choose the new secret.After you create the new proxy, choose **Choose existing proxy**, and then choose
        the proxy. Note that it might take some time for your proxy to be available for connection.

6. (Optional) Expand **Connection summary** and verify the highlighted updates for your
   resources.
7. Choose **Set up**.

## Viewing connected compute resources

You can use the AWS Management Console to view the compute resources that are connected to your Multi-AZ DB cluster. The resources shown
include compute resource connections that Amazon RDS set up automatically.

The listed compute resources don't include those that are manually connected to the Multi-AZ DB cluster.
For example, you can allow a compute resource to access your Multi-AZ DB cluster manually by
adding a rule to your VPC security group associated with the cluster.

For the console to list a Lambda function, the following conditions must apply:

- The name of the security group associated with the compute resource matches the pattern
  `lambda-rds-`n`` or
`lambda-rdsproxy-`n``
  (where `n` is a number).
- The security group associated with the compute resource has an outbound rule with the port range set to the
  port of the Multi-AZ DB cluster or an associated proxy. The
  destination for the outbound rule must be set to a security group associated with the Multi-AZ DB cluster or an associated
  proxy.
- The name of the security group attached to the proxy associated with your database
  matches the pattern
  `rds-rdsproxy-`n`(where`n`` is a number).
- The security group associated with the function has an outbound rule with the port set to the port that the
  Multi-AZ DB cluster or associated proxy uses. The destination must be set to a security group associated with the Multi-AZ DB cluster
  or associated proxy.

###### To view compute resources automatically connected to a Multi-AZ DB cluster

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**, and then choose the Multi-AZ DB cluster.
3. On the **Connectivity & security** tab, view the compute resources under
   **Connected compute resources**.
