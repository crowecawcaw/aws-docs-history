• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Connecting to a Windows Server

managed instance using Remote Desktop

You can use Fleet Manager, a tool in AWS Systems Manager, to connect to your Windows Server Amazon Elastic Compute Cloud
(Amazon EC2) instances using the Remote Desktop Protocol (RDP). Fleet Manager
Remote Desktop, which is powered by [Amazon DCV](../../../dcv/latest/adminguide/what-is-dcv.md "../../../dcv/latest/adminguide/what-is-dcv.md"), provides you with secure
connectivity to your Windows Server instances directly from the Systems Manager console. You can have up
to four simultaneous connections in a single browser window.

The Fleet Manager Remote Desktop API is named AWS Systems Manager GUI Connect. For information about using the
Systems Manager GUI Connect API, see the _[AWS Systems Manager GUI Connect API
Reference](../../../ssm-guiconnect/latest/APIReference.md "../../../ssm-guiconnect/latest/APIReference.md")_.

Currently, you can only use Remote Desktop with instances that are running Windows Server
2012 RTM or higher. Remote Desktop supports only English language inputs.

Fleet Manager Remote Desktop is a console-only service and doesn't support command-line
connections to your managed instances. To connect to a Windows Server managed instance through
a shell, you can use Session Manager, another tool in AWS Systems Manager. For more information, see
[AWS Systems Manager Session Manager](session-manager.md "session-manager.md").

###### Note

The duration of an RDP connection is not determined by the duration of your
AWS Identity and Access Management (IAM) credentials. Instead, the connection persists until the maximum
connection duration or idle time limit is met, whichever comes first. For more
information, see [Remote connection duration and
concurrency](#rdp-duration-concurrency "#rdp-duration-concurrency").

For information about configuring AWS Identity and Access Management (IAM) permissions to allow your
instances to interact with Systems Manager, see [Configure instance permissions for Systems Manager](setup-instance-permissions.md "setup-instance-permissions.md").

###### Topics

- [Setting up your environment](#rdp-prerequisites "#rdp-prerequisites")
- [Configuring IAM permissions for Remote
  Desktop](#rdp-iam-policy-examples "#rdp-iam-policy-examples")
- [Authenticating Remote Desktop
  connections](#rdp-authentication "#rdp-authentication")
- [Remote connection duration and
  concurrency](#rdp-duration-concurrency "#rdp-duration-concurrency")
- [Systems Manager GUI Connect handling of
  AWS IAM Identity Center attributes](#iam-identity-center-attribute-handling "#iam-identity-center-attribute-handling")
- [Connect to a managed node using Remote
  Desktop](#rdp-connect-to-node "#rdp-connect-to-node")
- [Viewing information about current and completed
  connections](#list-connections "#list-connections")

## Setting up your environment

Before using Remote Desktop, verify that your environment meets the following
requirements:

- **Managed node configuration**

Make sure that your Amazon EC2 instances are configured as [managed nodes](fleet-manager-managed-nodes.md "fleet-manager-managed-nodes.md") in
Systems Manager.

- **SSM Agent minimum version**

Verify that nodes are running SSM Agent version 3.0.222.0 or higher. For
information about how to check which agent version is running on a node, see
[Checking the SSM Agent version number](ssm-agent-get-version.md "ssm-agent-get-version.md"). For information about
installing or updating SSM Agent, see [Working with SSM Agent](ssm-agent.md "ssm-agent.md").

- **RDP port configuration**

To accept remote connections, the Remote Desktop Services
service on your Windows Server nodes must use default RDP port 3389. This is the
default configuration on Amazon Machine Images (AMIs) provided by AWS. You are
not explicitly required to open any inbound ports to use Remote
Desktop.

- **PSReadLine module version for
  keyboard functionality**

To ensure that your keyboard functions properly in
PowerShell, verify that nodes running Windows Server 2022 have
PSReadLine module version 2.2.2 or higher installed. If
they are running an older version, you can install the required version
using the following commands.

```
Install-PackageProvider -Name NuGet -MinimumVersion 2.8.5.201 -Force
```

After the NuGet package provider is installed, run the following
command.

```
Install-Module `
 -Name PSReadLine `
 -Repository PSGallery `
 -MinimumVersion 2.2.2 -Force
```

- **Session Manager configuration**

Before you can use Remote Desktop, you must complete the prerequisites for
Session Manager setup. When you connect to an instance using Remote Desktop, any
session preferences defined for your AWS account and AWS Region are
applied. For more information, see [Setting up Session Manager](session-manager-getting-started.md "session-manager-getting-started.md").

###### Note

If you log Session Manager activity using Amazon Simple Storage Service (Amazon S3), then your
Remote Desktop connections will generate the following error in
`bucket_name/Port/stderr`. This error is expected
behavior and can be safely ignored.

```
Setting up data channel with id SESSION_ID failed: failed to create websocket for datachannel with error: CreateDataChannel failed with no output or error: createDataChannel request failed: unexpected response from the service <BadRequest>
<ClientErrorMessage>Session is already terminated</ClientErrorMessage>
</BadRequest>
```

## Configuring IAM permissions for Remote

Desktop

In addition to the required IAM permissions for Systems Manager and Session Manager, the user or
role you use must be allowed permissions for initiating connections.

###### Permissions for initiating connections

To make RDP connections to EC2 instances in the console, the following
permissions are required:

- `ssm-guiconnect:CancelConnection`
- `ssm-guiconnect:GetConnection`
- `ssm-guiconnect:StartConnection`

###### Permissions for listing connections

In order to view lists of connections in the
console, the following permission is
required:

`ssm-guiconnect:ListConnections`

The following are example IAM policies that you can attach to a user or role to
allow different types of interaction with Remote Desktop. Replace each
`example resource placeholder` with your own
information.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "EC2",
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeInstances",
 "ec2:GetPasswordData"
 ],
 "Resource": "*"
 },
 {
 "Sid": "SSM",
 "Effect": "Allow",
 "Action": [
 "ssm:DescribeInstanceProperties",
 "ssm:GetCommandInvocation",
 "ssm:GetInventorySchema"
 ],
 "Resource": "*"
 },
 {
 "Sid": "TerminateSession",
 "Effect": "Allow",
 "Action": [
 "ssm:TerminateSession"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "ssm:resourceTag/aws:ssmmessages:session-id": [
 "${aws:userid}"
 ]
 }
 }
 },
 {
 "Sid": "SSMStartSession",
 "Effect": "Allow",
 "Action": [
 "ssm:StartSession"
 ],
 "Resource": [
 "arn:aws:ec2:*:`111122223333`:instance/*",
 "arn:aws:ssm:*:`111122223333`:managed-instance/*",
 "arn:aws:ssm:*::document/AWS-StartPortForwardingSession"
 ],
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws:CalledVia": "ssm-guiconnect.amazonaws.com"
 }
 }
 },
 {
 "Sid": "GuiConnect",
 "Effect": "Allow",
 "Action": [
 "ssm-guiconnect:CancelConnection",
 "ssm-guiconnect:GetConnection",
 "ssm-guiconnect:StartConnection",
 "ssm-guiconnect:ListConnections"
 ],
 "Resource": "*"
 }
 ]
}`

```

###### Note

In the following IAM policy, the `SSMStartSession`
section requires an Amazon Resource Name (ARN) for the
`ssm:StartSession` action. As shown, the ARN you specify
does _not_ require an AWS account ID. If you
specify an account ID, Fleet Manager returns an
`AccessDeniedException`.

The `AccessTaggedInstances` section, which is located lower
in the example policy, also requires ARNs for
`ssm:StartSession`. For those ARNs, you do specify
AWS account IDs.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "EC2",
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeInstances",
 "ec2:GetPasswordData"
 ],
 "Resource": "*"
 },
 {
 "Sid": "SSM",
 "Effect": "Allow",
 "Action": [
 "ssm:DescribeInstanceProperties",
 "ssm:GetCommandInvocation",
 "ssm:GetInventorySchema"
 ],
 "Resource": "*"
 },
 {
 "Sid": "SSMStartSession",
 "Effect": "Allow",
 "Action": [
 "ssm:StartSession"
 ],
 "Resource": [
 "arn:aws:ssm:*::document/AWS-StartPortForwardingSession"
 ],
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws:CalledVia": "ssm-guiconnect.amazonaws.com"
 }
 }
 },
 {
 "Sid": "AccessTaggedInstances",
 "Effect": "Allow",
 "Action": [
 "ssm:StartSession"
 ],
 "Resource": [
 "arn:aws:ec2:*:`111122223333`:instance/*",
 "arn:aws:ssm:*:`111122223333`:managed-instance/*"
 ],
 "Condition": {
 "StringLike": {
 "ssm:resourceTag/`tag key`": [
 "`tag value`"
 ]
 }
 }
 },
 {
 "Sid": "GuiConnect",
 "Effect": "Allow",
 "Action": [
 "ssm-guiconnect:CancelConnection",
 "ssm-guiconnect:GetConnection",
 "ssm-guiconnect:StartConnection",
 "ssm-guiconnect:ListConnections"
 ],
 "Resource": "*"
 }
 ]
}`

```

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "SSO",
 "Effect": "Allow",
 "Action": [
 "sso:ListDirectoryAssociations*",
 "identitystore:DescribeUser"
 ],
 "Resource": "*"
 },
 {
 "Sid": "EC2",
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeInstances",
 "ec2:GetPasswordData"
 ],
 "Resource": "*"
 },
 {
 "Sid": "SSM",
 "Effect": "Allow",
 "Action": [
 "ssm:DescribeInstanceProperties",
 "ssm:GetCommandInvocation",
 "ssm:GetInventorySchema"
 ],
 "Resource": "*"
 },
 {
 "Sid": "TerminateSession",
 "Effect": "Allow",
 "Action": [
 "ssm:TerminateSession"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "ssm:resourceTag/aws:ssmmessages:session-id": [
 "${aws:userName}"
 ]
 }
 }
 },
 {
 "Sid": "SSMStartSession",
 "Effect": "Allow",
 "Action": [
 "ssm:StartSession"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:instance/*",
 "arn:aws:ssm:*:*:managed-instance/*",
 "arn:aws:ssm:*:*:document/AWS-StartPortForwardingSession"
 ],
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws:CalledVia": "ssm-guiconnect.amazonaws.com"
 }
 }
 },
 {
 "Sid": "SSMSendCommand",
 "Effect": "Allow",
 "Action": [
 "ssm:SendCommand"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:instance/*",
 "arn:aws:ssm:*:*:managed-instance/*",
 "arn:aws:ssm:*:*:document/AWSSSO-CreateSSOUser"
 ]
 },
 {
 "Sid": "GuiConnect",
 "Effect": "Allow",
 "Action": [
 "ssm-guiconnect:CancelConnection",
 "ssm-guiconnect:GetConnection",
 "ssm-guiconnect:StartConnection",
 "ssm-guiconnect:ListConnections"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Authenticating Remote Desktop

connections

When establishing a remote connection, you can authenticate using
Windows credentials or the Amazon EC2 key pair
(`.pem` file) that is associated with the instance. For
information about using key pairs, see [Amazon EC2 key pairs and
Windows instances](../../../AWSEC2/latest/WindowsGuide/ec2-key-pairs.md "../../../AWSEC2/latest/WindowsGuide/ec2-key-pairs.md") in the _Amazon EC2 User Guide_.

Alternatively, if you're authenticated to the AWS Management Console using AWS IAM Identity Center, you can
connect to your instances without providing additional credentials. For an example
of a policy to allow remote connection authentication using IAM Identity Center, see [Configuring IAM permissions for Remote
Desktop](#rdp-iam-policy-examples "#rdp-iam-policy-examples").

###### Before you begin

Note the following conditions for using IAM Identity Center authentication before you begin
connecting using Remote Desktop.

- Remote Desktop supports IAM Identity Center authentication for nodes in the same
  AWS Region where you enabled IAM Identity Center.
- Remote Desktop supports IAM Identity Center user names of up to 16 characters.
- Remote Desktop supports IAM Identity Center user names consisting of alphanumeric
  characters and the following special characters: `.`
  `-`
  `_`

###### Important

Connections won't succeed for IAM Identity Center user names that contain the
following characters: `+`
`=`
`,`

IAM Identity Center supports these characters in user names, but Fleet Manager RDP
connections do not.

In addition, if an IAM Identity Center user name contains one or more `@`
symbols, Fleet Manager disregards the first `@` symbol and all
characters that follow it, whether or not the `@` introduces
the domain portion of an email address. For instance, for the IAM Identity Center user
name `diego_ramirez@example.com`, the
`@example.com` portion is ignored and the user name for
Fleet Manager becomes `diego_ramirez`. For
`diego_r@mirez@example.com`, Fleet Manager disregards
`@mirez@example.com`, and the username for Fleet Manager
becomes `diego_r`.

- When a connection is authenticated using IAM Identity Center, Remote Desktop creates a
  local Windows user in the instance’s Local Administrators
  group. This user persists after the remote connection has ended.
- Remote Desktop does not allow IAM Identity Center authentication for nodes that are
  Microsoft Active Directory domain controllers.
- Although Remote Desktop allows you to use IAM Identity Center authentication for nodes
  _joined_ to an Active
  Directory domain, we do not recommend doing so. This
  authentication method grants administrative permissions to users which might
  override more restrictive permissions granted by the domain.

###### Supported Regions for IAM Identity Center authentication

Remote Desktop connections using IAM Identity Center authentication are
supported in the following AWS Regions:

- US East (Ohio) (us-east-2)
- US East (N. Virginia) (us-east-1)
- US West (N. California) (us-west-1)
- US West (Oregon) (us-west-2)
- Africa (Cape Town) (af-south-1)
- Asia Pacific (Hong Kong) (ap-east-1)
- Asia Pacific (Mumbai) (ap-south-1)
- Asia Pacific (Tokyo) (ap-northeast-1)
- Asia Pacific (Seoul) (ap-northeast-2)
- Asia Pacific (Osaka) (ap-northeast-3)
- Asia Pacific (Singapore) (ap-southeast-1)
- Asia Pacific (Sydney) (ap-southeast-2)
- Asia Pacific (Jakarta) (ap-southeast-3)
- Canada (Central) (ca-central-1)
- Europe (Frankfurt) (eu-central-1)
- Europe (Stockholm) (eu-north-1)
- Europe (Ireland) (eu-west-1)
- Europe (London) (eu-west-2)
- Europe (Paris) (eu-west-3)
- Israel (Tel Aviv) (il-central-1)
- South America (São Paulo) (sa-east-1)
- Europe (Milan) (eu-south-1)
- Middle East (Bahrain) (me-south-1)
- AWS GovCloud (US-East) (us-gov-east-1)
- AWS GovCloud (US-West) (us-gov-west-1)

## Remote connection duration and

concurrency

The following conditions apply to active Remote Desktop connections:

- **Connection duration**

By default, a Remote Desktop connection is disconnected after 60 minutes.
To prevent a connection from being disconnected, you can choose
**Renew session** before being disconnected to reset
the duration timer.

- **Connection timeout**

A Remote Desktop connection disconnects after it has been idle for more
than 10 minutes.

- **Connection persistence**

After you connect to a Windows Server using Remote Desktop, the connection
persists until the maximum connection duration (60 minutes) or idle timeout
limit (10 minutes) is met. Connection duration is not determined by the
duration of your AWS Identity and Access Management (IAM) credentials. The connection persists
after IAM credentials expire if the connection duration limits are not
met. When using Remote Desktop, you should terminate your connection after
your IAM credentials expire by leaving the browser page.

- **Concurrent connections**

By default, you can have a maximum of 5 active Remote Desktop connections
at one time for the same AWS account and AWS Region. To request a
service quota increase of up to 50 concurrent connections, see [Requesting a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas
User Guide_.

###### Note

The standard license for Windows Server allows for two concurrent RDP
connections. To support more connections, you must purchase additional
Client Access Licenses (CALs) from Microsoft or Microsoft Remote Desktop
Services licenses from AWS. For more information on supplemental
licensing, see the following topics:

    + [Client Access Licenses and Management Licenses](https://www.microsoft.com/en-us/licensing/product-licensing/client-access-license "https://www.microsoft.com/en-us/licensing/product-licensing/client-access-license") on
     the Microsoft website
    + [Use License Manager user-based subscriptions for supported software
     products](../../../license-manager/latest/userguide/user-based-subscriptions.md "../../../license-manager/latest/userguide/user-based-subscriptions.md") in the
     *License Manager User Guide*

## Systems Manager GUI Connect handling of

AWS IAM Identity Center attributes

Systems Manager GUI Connect is the API that supports Fleet Manager connections to EC2 instances using RDP.
The following IAM Identity Center user data is retained after a connection is closed:

- `username`

Systems Manager GUI Connect encrypts this identity attribute at rest using an AWS managed key by
default. Customer managed keys are not supported for encrypting this attribute in Systems Manager GUI Connect.
If you delete a user in your IAM Identity Center instance, Systems Manager GUI Connect continues to retain the
`username` attribute associated with that user for 7 years,
after which it is deleted. This data is retained to support auditing events, such as
listing Systems Manager GUI Connect connection history. The data can't be deleted manually.

## Connect to a managed node using Remote

Desktop

###### Browser copy/paste support for text

Using the Google Chrome and Microsoft Edge browsers, you can copy and paste
text from a managed node to your local machine, and from your local machine to a
managed node that you are connected to.

Using the Mozilla Firefox browser, you can copy and paste text from a managed node
to your local machine only. Copying from your local machine to the managed node is
not supported.

###### To connect to a managed node using Fleet Manager Remote Desktop

1.  Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2.  In the navigation pane, choose **Fleet Manager**.
3.  Choose the node that you want to connect to. You can select either the
    check box or the node name.
4.  On the **Node actions** menu, choose **Connect
    with Remote Desktop**.
5.  Choose your preferred **Authentication type**. If you
    choose **User credentials**, enter the user name and
    password for a Windows user account on the node that you're
    connecting to. If you choose **Key pair**, you can provide
    authentication using one of the following methods:
    1. Choose **Browse local machine** if you want to
       select the PEM key associated with your instance from your local
       file system.
    - or -
    2. Choose **Paste key pair content** if you want to
       copy the contents of the PEM file and paste them in to the provided
       field.

6.  Select **Connect**.
7.  To choose your preferred display resolution, in the
    **Actions** menu, choose
    **Resolutions**, and then select from the
    following:

        * **Adapt Automatically**
        * **1920 x 1080**
        * **1400 x 900**
        * **1366 x 768**
        * **800 x 600**

    The **Adapt Automatically** option sets the resolution
    based on your detected screen size.

## Viewing information about current and completed

connections

You can use the Fleet Manager section of the Systems Manager console to view information about
RDP connections that have been made in your account. Using a set of filters, you can
limit the list of connections displayed to a time range, a specific instance, the
user who made the connections, and connections of a specific status. The console
also provides tabs that show information about all currently active connections, and
all past connections.

###### To view information about current and completed connections

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Fleet Manager**.
3. Choose **Account management, Connect with Remote
   Desktop**.
4. Choose one of the following tabs:
   - **Active connections**
   - **Connection history**

5. To further narrow the list of connection results displayed, specify one or
   more filters in the search (
   ![The Search icon](images/search-icon.png)
   ) box. You can also enter a free-text search
   term.
