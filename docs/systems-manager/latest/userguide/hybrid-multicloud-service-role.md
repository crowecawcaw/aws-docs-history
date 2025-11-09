AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Create the IAM service role required

for Systems Manager in hybrid and multicloud environments

Non-EC2 (Amazon Elastic Compute Cloud) machines in a [hybrid and multicloud](operating-systems-and-machine-types.md#supported-machine-types "operating-systems-and-machine-types.md#supported-machine-types") environment require an AWS Identity and Access Management (IAM)
service role to communicate with the AWS Systems Manager service. The role grants AWS Security Token Service
(AWS STS) [`AssumeRole`](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") trust to the Systems Manager service. You only need to
create a service role for a hybrid and multicloud environment once for each
AWS account. However, you might choose to create multiple service roles for different
hybrid activations if machines in your hybrid and multicloud environment require
different permissions.

The following procedures describe how to create the required service role using the
Systems Manager console or your preferred command line tool.

## Using the AWS Management Console

to create an IAM service role for Systems Manager hybrid activations

Use the following procedure to create a service role for hybrid activation. This
procedure uses the `AmazonSSMManagedInstanceCore` policy for Systems Manager core
functionality. Depending on your use case, you might need to add additional policies
to your service role for your on-premises machines to be able to access other Systems Manager
tools or AWS services. For example, without access to the required AWS managed
Amazon Simple Storage Service (Amazon S3) buckets, Patch Manager patching operations fail.

###### To create a service role (console)

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**, and then choose
   **Create role**.
3. For **Select trusted entity**, make the following
   choices:
   1. For **Trusted entity type**, choose
      **AWS service**.
   2. For **Use cases for other AWS services**,
      choose **Systems Manager**.
   3. Choose **Systems Manager**.

   The following image highlights
   the location of the Systems Manager option.

   ![Systems Manager is one of the options for Use case.](images/iam_use_cases_for_MWs.png)

4. Choose **Next**.
5. On the **Add permissions** page, do the following:
   - Use the **Search** field to locate the
     **AmazonSSMManagedInstanceCore** policy. Select
     the check box next to its name, as shown in the following
     illustration.

   ![The check box is selected in the AmazonSSMManagedInstanceCore row.](images/setup-instance-profile-2.png)

   ###### Note

   The console retains your selection even if you search for
   other policies.
   - If you created a custom S3 bucket policy in the procedure [(Optional) Create a custom
     policy for S3 bucket access](setup-instance-permissions.md#instance-profile-custom-s3-policy "setup-instance-permissions.md#instance-profile-custom-s3-policy"), search for
     it and select the check box next to its name.
   - If you plan to join non-EC2 machines to an Active Directory
     managed by AWS Directory Service, search for
     **AmazonSSMDirectoryServiceAccess** and select
     the check box next to its name.
   - If you plan to use EventBridge or CloudWatch Logs to manage or monitor your managed
     node, search for **CloudWatchAgentServerPolicy**
     and select the check box next to its name.

6. Choose **Next**.
7. For **Role name**, enter a name for your new IAM server
   role, such as `SSMServerRole`.

###### Note

Make a note of the role name. You will choose this role when you
register new machines that you want to manage by using Systems Manager. 8. (Optional) For **Description**, update the description
for this IAM server role. 9. (Optional) For **Tags**, add one or more tag-key value
pairs to organize, track, or control access for this role. 10. Choose **Create role**. The system returns you to the
**Roles** page.

## Using the AWS CLI to

create an IAM service role for Systems Manager hybrid activations

Use the following procedure to create a service role for hybrid activation. This
procedure uses the `AmazonSSMManagedInstanceCore` policy Systems Manager core
functionality. Depending on your use case, you might need to add additional policies
to your service role for your non-EC2 machines in a [hybrid and multicloud](operating-systems-and-machine-types.md#supported-machine-types "operating-systems-and-machine-types.md#supported-machine-types") environment to be
able to access other tools or AWS services.

###### S3 bucket policy requirement

If either of the following cases are true, you must create a custom IAM
permission policy for Amazon Simple Storage Service (Amazon S3) buckets before completing this
procedure:

- **Case 1** – You're using a VPC
  endpoint to privately connect your VPC to supported AWS services and VPC
  endpoint services powered by AWS PrivateLink.
- **Case 2** – You plan to use an Amazon S3
  bucket that you create as part of your Systems Manager operations, such as for storing
  output for Run Command commands or Session Manager sessions to an S3 bucket. Before
  proceeding, follow the steps in [Create a custom S3 bucket policy for an instance profile](setup-instance-permissions.md#instance-profile-custom-s3-policy "setup-instance-permissions.md#instance-profile-custom-s3-policy"). The
  information about S3 bucket policies in that topic also applies to your
  service role.

AWS CLI

###### To create an IAM service role for a hybrid and multicloud

environment (AWS CLI)

1. Install and configure the AWS Command Line Interface (AWS CLI), if you haven't already.

For information, see [Installing or updating the
latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md"). 2. On your local machine, create a text file with a name such as
`SSMService-Trust.json` with the
following trust policy. Make sure to save the file with the
`.json` file extension. Be sure to
specify your AWS account and the AWS Region in the ARN where
you created your hybrid activation. Replace the
`placeholder values` for account ID
and Region with your own information.

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"",
 "Effect":"Allow",
 "Principal":{
 "Service":"ssm.amazonaws.com"
 },
 "Action":"sts:AssumeRole",
 "Condition":{
 "StringEquals":{
 "aws:SourceAccount":"`123456789012`"
 },
 "ArnEquals":{
 "aws:SourceArn":"arn:aws:ssm:`us-east-1`:`111122223333`:*"
 }
 }
 }
 ]
}`

```

3. Open the AWS CLI, and in the directory where you
   created the JSON file, run the [create-role](../../../cli/latest/reference/iam/create-role.md "../../../cli/latest/reference/iam/create-role.md") command to create the service role.
   This example creates a role named `SSMServiceRole`.
   You can choose another name if you prefer.

Linux & macOSWindowsLinux & macOS

```
aws iam create-role \
    --role-name SSMServiceRole \
    --assume-role-policy-document file://SSMService-Trust.json
```

Windows

```
aws iam create-role ^
    --role-name SSMServiceRole ^
    --assume-role-policy-document file://SSMService-Trust.json
```

4. Run the [attach-role-policy](../../../cli/latest/reference/iam/attach-role-policy.md "../../../cli/latest/reference/iam/attach-role-policy.md") command as follows to allow the
   service role you just created to create a session token. The
   session token gives your managed node permission to run commands
   using Systems Manager.

###### Note

The policies you add for a service profile for managed
nodes in a hybrid and multicloud environment are the same
policies used to create an instance profile for Amazon Elastic Compute Cloud
(Amazon EC2) instances. For more information about the AWS
policies used in the following commands, see [Configure instance permissions required for Systems Manager](setup-instance-permissions.md "setup-instance-permissions.md").

(Required) Run the following command to allow a managed node
to use AWS Systems Manager service core functionality.

Linux & macOSWindowsLinux & macOS

```
aws iam attach-role-policy \
    --role-name SSMServiceRole \
    --policy-arn arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore
```

Windows

```
aws iam attach-role-policy ^
    --role-name SSMServiceRole ^
    --policy-arn arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore
```

If you created a custom S3 bucket policy for your service
role, run the following command to allow AWS Systems Manager Agent
(SSM Agent) to access the buckets you specified in the policy.
Replace `account-id` and
`amzn-s3-demo-bucket` with your
AWS account ID and your bucket name.

Linux & macOSWindowsLinux & macOS

```
aws iam attach-role-policy \
    --role-name SSMServiceRole \
    --policy-arn arn:aws:iam::`account-id`:policy/`amzn-s3-demo-bucket`
```

Windows

```
aws iam attach-role-policy ^
    --role-name SSMServiceRole ^
    --policy-arn arn:aws:iam::`account-id`:policy/`amzn-s3-demo-bucket`
```

(Optional) Run the following command to allow SSM Agent to
access AWS Directory Service on your behalf for requests to join the domain by
the managed node. Your service role needs this policy only if
you join your nodes to a Microsoft AD
directory.

Linux & macOSWindowsLinux & macOS

```
aws iam attach-role-policy \
    --role-name SSMServiceRole \
    --policy-arn arn:aws:iam::aws:policy/AmazonSSMDirectoryServiceAccess
```

Windows

```
aws iam attach-role-policy ^
    --role-name SSMServiceRole ^
    --policy-arn arn:aws:iam::aws:policy/AmazonSSMDirectoryServiceAccess
```

(Optional) Run the following command to allow the CloudWatch agent to
run on your managed nodes. This command makes it possible to
read information on a node and write it to CloudWatch. Your service
profile needs this policy only if you will use services such as
Amazon EventBridge or Amazon CloudWatch Logs.

```
aws iam attach-role-policy \
    --role-name SSMServiceRole \
    --policy-arn arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy
```

Tools for PowerShell

###### To create an IAM service role for a hybrid and multicloud

environment (AWS Tools for Windows PowerShell)

1. Install and configure the AWS Tools for PowerShell (Tools for Windows PowerShell), if you haven't already.

For information, see [Installing the
AWS Tools for PowerShell](../../../powershell/latest/userguide/pstools-getting-set-up.md "../../../powershell/latest/userguide/pstools-getting-set-up.md"). 2. On your local machine, create a text file with a name such as
`SSMService-Trust.json` with the
following trust policy. Make sure to save the file with the
`.json` file extension. Be sure to
specify your AWS account and the AWS Region in the ARN where
you created your hybrid activation.

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": "ssm.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`123456789012`"
 },
 "ArnEquals": {
 "aws:SourceArn": "arn:aws:ssm:`us-east-1`:`123456789012`:*"
 }
 }
 }
 ]
}`

```

3. Open PowerShell in administrative mode, and in the directory
   where you created the JSON file, run [New-IAMRole](../../../powershell/latest/reference/items/Register-IAMRolePolicy.md "../../../powershell/latest/reference/items/Register-IAMRolePolicy.md") as follows to create a service role.
   This example creates a role named `SSMServiceRole`.
   You can choose another name if you prefer.

```
New-IAMRole `
    -RoleName SSMServiceRole `
    -AssumeRolePolicyDocument (Get-Content -raw SSMService-Trust.json)
```

4. Use [Register-IAMRolePolicy](../../../powershell/latest/reference/items/Register-IAMRolePolicy.md "../../../powershell/latest/reference/items/Register-IAMRolePolicy.md") as follows to allow the
   service role you created to create a session token. The session
   token gives your managed node permission to run commands using
   Systems Manager.

###### Note

The policies you add for a service profile for managed
nodes in a hybrid and multicloud environment are the same
policies used to create an instance profile for EC2
instances. For more information about the AWS policies
used in the following commands, see [Configure instance permissions required for Systems Manager](setup-instance-permissions.md "setup-instance-permissions.md").

(Required) Run the following command to allow a managed node
to use AWS Systems Manager service core functionality.

```
Register-IAMRolePolicy `
    -RoleName SSMServiceRole `
    -PolicyArn arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore
```

If you created a custom S3 bucket policy for your service
role, run the following command to allow SSM Agent to access the
buckets you specified in the policy. Replace
`account-id` and
`my-bucket-policy-name` with your
AWS account ID and your bucket name.

```
Register-IAMRolePolicy `
    -RoleName SSMServiceRole `
    -PolicyArn arn:aws:iam::`account-id`:policy/`my-bucket-policy-name`
```

(Optional) Run the following command to allow SSM Agent to
access AWS Directory Service on your behalf for requests to join the domain by
the managed node. Your server role needs this policy only if you
join your nodes to a Microsoft AD directory.

```
Register-IAMRolePolicy `
    -RoleName SSMServiceRole `
    -PolicyArn arn:aws:iam::aws:policy/AmazonSSMDirectoryServiceAccess
```

(Optional) Run the following command to allow the CloudWatch agent to
run on your managed nodes. This command makes it possible to
read information on a node and write it to CloudWatch. Your service
profile needs this policy only if you will use services such as
Amazon EventBridge or Amazon CloudWatch Logs.

```
Register-IAMRolePolicy `
    -RoleName SSMServiceRole `
    -PolicyArn arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy
```

Continue to [Create a hybrid activation to register
nodes with Systems Manager](hybrid-activation-managed-nodes.md "hybrid-activation-managed-nodes.md").
