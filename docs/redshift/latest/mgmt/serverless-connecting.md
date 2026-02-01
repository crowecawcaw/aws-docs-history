Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Connecting to Amazon Redshift Serverless

Once you've set up your Amazon Redshift Serverless instance, you can connect to it in a variety
of methods, outlined below. If you have multiple teams or projects and want to manage
costs separately, you can use separate AWS accounts.

For a list of AWS Regions where the Amazon Redshift Serverless is available, see the
endpoints listed for [Redshift Serverless API](../../../general/latest/gr/redshift-service.md "../../../general/latest/gr/redshift-service.md") in the
_Amazon Web Services General Reference_.

Amazon Redshift Serverless connects to the serverless environment in your AWS account in the
current AWS Region. Amazon Redshift Serverless runs in a VPC within the port ranges 5431-5455
and 8191-8215. The default is 5439. Currently, you can only change ports with the API
operation `UpdateWorkgroup` and the AWS CLI operation
`update-workgroup`.

## Connecting to

Amazon Redshift Serverless

You can connect to a database (named `dev`) in Amazon Redshift Serverless with
the following syntax.

```
*workgroup-name*.*account-number*.*aws-region*.redshift-serverless.amazonaws.com:port/dev
```

For example, the following connection string specifies Region us-east-1.

```
default.123456789012.us-east-1.redshift-serverless.amazonaws.com:5439/dev
```

## Connecting to Amazon Redshift Serverless

through JDBC drivers

You can use one of the following methods to connect to Amazon Redshift Serverless with your
preferred SQL client using the Amazon Redshift-provided JDBC driver version 2.x driver.

To connect with sign-in credentials for database authentication using the JDBC driver
version 2.x, use the following syntax. The port number is optional; if
not included, Amazon Redshift Serverless defaults to port number 5439. You can change to
another port from the port range of 5431-5455 or 8191-8215. To change the default
port for a serverless endpoint, use the AWS CLI and Amazon Redshift API.

```
jdbc:redshift://*workgroup-name*.*account-number*.*aws-region*.redshift-serverless.amazonaws.com:5439/dev
```

For example, the following connection string specifies the workgroup default, the
account ID 123456789012, and the Region us-east-2.

```
jdbc:redshift://default.123456789012.us-east-2.redshift-serverless.amazonaws.com:5439/dev
```

To connect with IAM using the JDBC driver version 2.x, use the following
syntax. The port number is optional; if not included, Amazon Redshift Serverless defaults to
port number 5439. You can change to another port from the port range of 5431-5455 or
8191-8215. To change the default port for a serverless endpoint, use the AWS CLI and
Amazon Redshift API.

```
jdbc:redshift:iam://*workgroup-name*.*account-number*.*aws-region*.redshift-serverless.amazonaws.com:5439/dev
```

For example, the following connection string specifies the workgroup default, the
account ID 123456789012, and the Region us-east-2.

```
jdbc:redshift:iam://default.123456789012.us-east-2.redshift-serverless.amazonaws.com:5439/dev
```

For ODBC, use the following syntax.

```
Driver={Amazon Redshift (x64)}; Server=*workgroup-name*.*account-number*.*aws-region*.redshift-serverless.amazonaws.com; Database=dev
```

If you are using a JDBC driver version prior to 2.1.0.9 and connecting with IAM,
you will need to use the following syntax.

```
jdbc:redshift:iam://redshift-serverless-<name>:aws-region/database-name
```

For example, the following connection string specifies the workgroup default and
the AWS Region us-east-1.

```
jdbc:redshift:iam://redshift-serverless-default:us-east-1/dev
```

For more information about drivers, see [Configuring connections in Amazon Redshift](configuring-connections.md "configuring-connections.md").

### Finding your JDBC and

ODBC connection string

To connect to your workgroup with your SQL client tool, you must have the JDBC
or ODBC connection string. You can find the connection string in the Amazon Redshift Serverless
console, on a workgroup's details page.

###### To find the connection string for a workgroup

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Redshift Serverless**.
3. On the navigation menu, choose **Workgroup
   configuration**, then choose the workgroup name from the
   list to open its details.
4. The **JDBC URL** and **ODBC URL**
   connection strings are available, along with additional details, in the
   **General information** section. Each string is
   based on the AWS Region where the workgroup runs. Choose the icon next
   to the appropriate connection string to copy the connection
   string.

## Connecting to Amazon Redshift Serverless with the Data

API

You can also use the Amazon Redshift Data API to connect to Amazon Redshift Serverless. Use the
`workgroup-name` parameter instead of the
`cluster-identifier` parameter in your AWS CLI calls.

For more information about the Data API, see [Using the Amazon Redshift Data API](data-api.md "data-api.md"). For example code calling the Data API in Python and
other examples, see [Getting Started with Redshift Data API](https://github.com/aws-samples/getting-started-with-amazon-redshift-data-api#readme "https://github.com/aws-samples/getting-started-with-amazon-redshift-data-api#readme") and look in the
`quick-start` and `use-cases` folders in
_GitHub_.

## Connecting with SSL to

Amazon Redshift Serverless

### Configuring a secure connection to

Amazon Redshift Serverless

To support SSL connections, Redshift Serverless creates and installs an [AWS Certificate Manager (ACM)](https://aws.amazon.com/certificate-manager/ "https://aws.amazon.com/certificate-manager/")
issued SSL certificate for each workgroup.
ACM certificates are publicly trusted by most operating systems, web browsers, and clients.
You might need to download a certificate bundle if your SQL clients or applications connect to Redshift Serverless
using SSL with the `sslmode` connection option set to
`require`, `verify-ca`, or `verify-full`.
If your client needs a certificate, Redshift Serverless provides a bundle certificate as follows:

- Download the bundle from
  [https://s3.amazonaws.com/redshift-downloads/amazon-trust-ca-bundle.crt](https://s3.amazonaws.com/redshift-downloads/amazon-trust-ca-bundle.crt "https://s3.amazonaws.com/redshift-downloads/amazon-trust-ca-bundle.crt").

      + The expected MD5 checksum number is 418dea9b6d5d5de7a8f1ac42e164cdcf.
      + The sha256 checksum number is 36dba8e4b8041cd14b9d60158893963301bcbb92e1c456847784de2acb5bd550.

  Don't use the previous certificate bundle that was located at
  `https://s3.amazonaws.com/redshift-downloads/redshift-ca-bundle.crt`.

- In the China AWS Region, download the bundle from
  [https://s3.cn-north-1.amazonaws.com.cn/redshift-downloads-cn/amazon-trust-ca-bundle.crt](https://s3.cn-north-1.amazonaws.com.cn/redshift-downloads-cn/amazon-trust-ca-bundle.crt "https://s3.cn-north-1.amazonaws.com.cn/redshift-downloads-cn/amazon-trust-ca-bundle.crt").

      + The expected MD5 checksum number is 418dea9b6d5d5de7a8f1ac42e164cdcf.
      + The sha256 checksum number is 36dba8e4b8041cd14b9d60158893963301bcbb92e1c456847784de2acb5bd550.

  Don't use the previous certificate bundles that were located at
  `https://s3.cn-north-1.amazonaws.com.cn/redshift-downloads-cn/redshift-ca-bundle.crt`

and `https://s3.cn-north-1.amazonaws.com.cn/redshift-downloads-cn/redshift-ssl-ca-cert.pem`

###### Important

Redshift Serverless has changed the way that SSL certificates are managed. You might
need to update your current trust root CA certificates to continue to connect to
your workgroups using SSL. For more information about ACM certificates for SSL connections, see [Transitioning to ACM
certificates for SSL connections](connecting-transitioning-to-acm-certs.md "connecting-transitioning-to-acm-certs.md").

By default, workgroup databases accept a connection whether it uses SSL or not.

To create a new workgroup that only accepts SSL connections, use the `create-workgroup`
command and set the `require_ssl` parameter to `true`. To use the
following example, replace `yourNamespaceName` with the name of
your namespace and replace `yourWorkgroupName` with the name of
your workgroup.

```
aws redshift-serverless create-workgroup \
--namespace-name `yourNamespaceName` \
--workgroup-name `yourWorkgroupName` \
--config-parameters parameterKey=require_ssl,parameterValue=true
```

To update an existing workgroup to only accept SSL connections, use the `update-workgroup` command and set the
`require_ssl` parameter to `true`. Note that Redshift Serverless will restart
your workgroup when you update the `require_ssl` parameter. To use the following
example, replace `yourWorkgroupName` with the name of your
workgroup.

```
aws redshift-serverless update-workgroup \
--workgroup-name `yourWorkgroupName` \
--config-parameters parameterKey=require_ssl,parameterValue=true
```

Amazon Redshift supports the Elliptic Curve Diffie—Hellman Ephemeral (ECDHE) key
agreement protocol. With ECDHE, the client and server each have an elliptic curve
public-private key pair that is used to establish a shared secret over an insecure
channel. You don't need to configure anything in Amazon Redshift to enable ECDHE. If
you connect from a SQL client tool that uses ECDHE to encrypt communication between
the client and server, Amazon Redshift uses the provided cipher list to make the
appropriate connection. For more information, see [Elliptic curve diffie—hellman](https://en.wikipedia.org/wiki/Elliptic_curve_Diffie%E2%80%93Hellman "https://en.wikipedia.org/wiki/Elliptic_curve_Diffie%E2%80%93Hellman") on Wikipedia and [Ciphers](https://www.openssl.org/ "https://www.openssl.org/") on the OpenSSL website.

#### Configuring a FIPS-compliant SSL connection to

Amazon Redshift Serverless

To create a new workgroup that uses a FIPS-compliant SSL connection, use the
`create-workgroup` command and set the `use_fips_ssl` and
`require_ssl` parameters to `true`. To use the following
example, replace `yourNamespaceName` with the name of your
namespace and replace `yourWorkgroupName` with the name of your
workgroup.

```
aws redshift-serverless create-workgroup \
--namespace-name `yourNamespaceName` \
--workgroup-name `yourWorkgroupName` \
--config-parameters '[{"parameterKey": "require_ssl", "parameterValue": "true"}, {"parameterKey": "use_fips_ssl", "parameterValue": "true"}]'
```

To update an existing workgroup to use a FIPS-compliant SSL connection, use the
`update-workgroup` command and set the `use_fips_ssl` and
`require_ssl` parameters to `true`. Note that Redshift Serverless will
restart your workgroup when you update the `use_fips_ssl` parameter. To use
the following example, replace `yourWorkgroupName` with the
name of your workgroup.

```
aws redshift-serverless update-workgroup \
--workgroup-name `yourWorkgroupName` \
--config-parameters '[{"parameterKey": "require_ssl", "parameterValue": "true"}, {"parameterKey": "use_fips_ssl", "parameterValue": "true"}]'
```

For more information about configuring Redshift Serverless to use FIPS-compliant connections, see
[use_fips_ssl](../dg/use_fips_ssl.md "../dg/use_fips_ssl.md") in the _Amazon Redshift Database Developer Guide_.

## Connecting to Amazon Redshift Serverless from an Amazon Redshift

managed VPC endpoint

### Connecting to Amazon Redshift Serverless from other VPC endpoints

For information about setting up or configuring a managed-VPC endpoint for an Amazon Redshift Serverless workgroup, see [Working with Redshift-managed VPC endpoints](managing-cluster-cross-vpc.md "managing-cluster-cross-vpc.md").

## Connecting to Amazon Redshift Serverless

from an interface VPC endpoint (AWS PrivateLink)

For information about connecting to Amazon Redshift Serverless from an interface VPC
endpoint (AWS PrivateLink), see [Interface VPC endpoints](security-network-isolation.md#security-private-link "security-network-isolation.md#security-private-link").

## Connecting to Amazon Redshift Serverless from a

Redshift VPC endpoint in another account

### Connecting to Amazon Redshift Serverless

from a cross VPC endpoint

Amazon Redshift Serverless is provisioned in a VPC. You can grant access to a VPC in another
account to access Amazon Redshift Serverless in your account. This is similar to a connection from a
managed VPC endpoint, but in this case the connection originates,
for
example, from a database client in another account.
There are a few operations
that
you can perform:

- A database owner can grant access to a VPC containing Amazon Redshift Serverless to another account in
  the same
  Region.
- A database owner can revoke Amazon Redshift Serverless access.

The main benefit of cross-account access is
allowing
easier database collaboration. Users don't have to be provisioned in the
account that contains the database to access it, which reduces configuration steps and saves
time.

#### Permissions required to grant access

to a VPC in another account

To grant access or change the access allowed, the grantor requires an assigned permissions policy with the following permissions:

- redshift-serverless:PutResourcePolicy
- redshift-serverless:GetResourcePolicy
- redshift-serverless:DeleteResourcePolicy
- ec2:CreateVpcEndpoint
- ec2:ModifyVpcEndpoint

You might need other permissions that are specified in the AWS managed policy _AmazonRedshiftFullAccess_. For more information,
see [Granting permissions to Amazon Redshift Serverless](serverless-iam.md#serverless-security-other-services "serverless-iam.md#serverless-security-other-services").

The grantee requires an assigned permissions policy with the following permissions:

- redshift-serverless:ListWorkgroups
- redshift-serverless:CreateEndpointAccess
- redshift-serverless:UpdateEndpointAccess
- redshift-serverless:GetEndpointAccess
- redshift-serverless:ListEndpointAccess
- redshift-serverless:DeleteEndpointAccess

As a best practice, we recommend attaching permissions policies to an IAM role and then assigning it to users and groups as
needed. For more information, see [Identity and access management in Amazon Redshift](redshift-iam-authentication-access-control.md "redshift-iam-authentication-access-control.md").

This is a sample resource policy used to configure cross-VPC access:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CrossAccountCrossVPCAccess",
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "123456789012",
 "234567890123"
 ]
 },
 "Action": [
 "redshift-serverless:CreateEndpointAccess",
 "redshift-serverless:UpdateEndpointAccess",
 "redshift-serverless:DeleteEndpointAccess",
 "redshift-serverless:GetEndpointAccess"
 ],
 "Resource": "arn:aws:redshift-serverless:*:*:*",
 "Condition": {
 "StringEquals": {
 "aws:RequestedRegion": "us-east-1"
 },
 "StringLike": {
 "aws:SourceVpc": [
 "vpc-11223344556677889",
 "vpc-12345678"
 ]
 }
 }
 }
 ]
}`

```

The procedures that follow in this section assume that the user performing them has
the appropriate assigned permissions, for example, by means of an assigned IAM
role
that has the permissions listed. The procedures also assume that the
workgroup has an IAM role attached with appropriate resource permissions.

#### Granting VPC

access to other accounts, using the console

This procedure
shows the steps for configuring
database
access when you're
the
database owner, and you want to grant access to it.

###### Granting access from the owner account

1. In the properties for the Amazon Redshift Serverless workgroup, on the **Data
   access** tab, there is a list called **Granted
   accounts**. It shows accounts and VPCs granted access to the
   workgroup. Find the list and choose **Grant access** to add
   an account to the
   list.
2. A window appears where you can add the grantee information. Enter the AWS
   account ID, which is the 12-digit ID of the account that you want to grant
   access to.
3. Grant access to all VPCs for the grantee, or to specific VPCs. If you grant
   access only to specific VPCs, you can add the IDs for these by entering each
   one
   and choosing **Add VPC**.
4. **Save changes** when you're finished.

When you save the changes, the account appears in the list of **Granted
accounts**. The entry shows the **Account ID** and the
list of VPCs granted access.

The database owner can also revoke access to an account. The owner can revoke access
at any time.

###### Revoking access to an account

1. You can start from the list of granted accounts. First, select one or more
   accounts.
2. Choose **Revoke access**.

After access is granted, a database administrator for the grantee can check the
console to determine if they have access.

###### Using the console to confirm that access is granted for you to access another

account

1. In the Amazon Redshift Serverless workgroup properties, on the **Data
   access** tab, there is a list called **Authorized
   accounts**. It shows accounts that can be accessed from this
   workgroup. The grantee can't use the workgroup's endpoint URL to access to the
   workgroup directly. To access the workgroup, you as the grantee go to the
   **endpoint** section and choose **create an
   endpoint**.
2. Then, as the grantee, you provide an endpoint name and a VPC to access the
   workgroup.
3. After the endpoint is created successfully, it appears in the
   **endpoint** section and there is an endpoint URL for it.
   You can use this endpoint URL to access the workgroup.

#### Granting access to other accounts, using CLI commands

The account granting access must first grant access to another account to connect by using `put-resource-policy`. The database owner can
call `put-resource-policy` to authorize another account to create connections to the workgroup. The grantee account can
then use `create-endpoint-authorization` to create connections to the workgroup through their allowed VPCs.

The following shows the properties for `put-resource-policy`, which you can call to allow access to a specific account and VPC.

```
aws redshift-serverless put-resource-policy
--resource-arn <value>
--policy <value>
```

After calling the command, you can call `get-resource-policy`, specifying the `resource-arn` to see which accounts and VPCs are allowed to access the resource.

The following call can be made by the grantee. It shows information about the granted access. Specifically, it returns a list that contains the VPCs granted access.

```
aws redshift-serverless list-workgroups
--owner-account <value>
```

The purpose of this is for the grantee to get information from the granting account about endpoint authorizations. The `owner-account` is
the sharing account. When you run this, it returns the `CrossAccountVpcs` for each workgroup, which is a list of
allowed VPCs. For reference, the following shows all of the properties available for a workgroup:

```
Output: workgroup (Object)
workgroupId String,
workgroupArn String,
workgroupName String,
status: String,
namespaceName: String,
baseCapacity: Integer, (Not-applicable)
enhancedVpcRouting: Boolean,
configParameters: List,
securityGroupIds: List,
subnetIds: List,
endpoint: String,
publiclyAccessible: Boolean,
creationDate: Timestamp,
port: Integer,
CrossAccountVpcs: List
```

###### Note

As a point of reminder, [cluster relocation](managing-cluster-recovery.md "managing-cluster-recovery.md") isn't a prerequisite for configuring additional Redshift networking
features. It also isn't required that you turn it on to
enable the following:

- **Connecting from a cross-account or cross-region VPC to Redshift** – You can connect from one AWS virtual private cloud (VPC) to another
  that contains a Redshift database, as described in this section.
- **Setting up a custom domain name** – You can create a custom domain name, also known as a custom URL, for
  your Amazon Redshift cluster or Amazon Redshift Serverless workgroup, to make the endpoint name more memorable and simple. For more information,
  see [Using a custom domain name for client connections](connecting-connection-CNAME.md "connecting-connection-CNAME.md").

## Additional resources

Instructions for setting your network traffic settings are available in [Public accessibility with default or custom security group
configuration](rs-security-group-public-private.md#rs-security-group-public-default "rs-security-group-public-private.md#rs-security-group-public-default"). This includes a use case where the cluster is publicly
accessible.

Instructions for setting your network traffic settings are available in [Private accessibility with default or custom security group
configuration](rs-security-group-public-private.md#rs-security-group-private "rs-security-group-public-private.md#rs-security-group-private"). This includes a use case where the cluster isn't
available to the internet.

For more information about secure connections to Amazon Redshift Serverless, including
granting permissions, authorizing access to additional services, and creating IAM
roles, see [Identity and access management in Amazon Redshift Serverless](serverless-iam.md "serverless-iam.md").
