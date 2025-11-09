AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/ "https://aws.amazon.com/transform/"), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# App2Container Automation runbook

AWS App2Container provides the `AWSApp2Container-ReplatformApplications` Automation
runbook for use on Amazon EC2 instances. Automation is a capability of AWS Systems Manager. The runbook
performs the installation of App2Container as well as the initialize, analyze, and transform phases
for replatforming supported applications. If desired, the automation can also push the
containerized application to Amazon Elastic Container Registry (Amazon ECR). For more information, see [App2Container compatibility](compatibility-a2c.md "compatibility-a2c.md") and [Applications you can containerize using
AWS App2Container](supported-applications.md "supported-applications.md").

You must have access to Systems Manager to use the runbook. For more information about Systems Manager
Automation, see [AWS Systems Manager
Automation](../../../systems-manager/latest/userguide/systems-manager-automation.md "../../../systems-manager/latest/userguide/systems-manager-automation.md") in the _AWS Systems Manager User Guide_.

###### Tip

To containerize your applications with a console-based experience and deploy them on
Amazon ECS on AWS Fargate, you can use the _Replatform applications to
Amazon ECS_ template on the [AWS Migration Hub Orchestrator
console](https://console.aws.amazon.com/migrationhub/orchestrator?region=us-east-1#/templates "https://console.aws.amazon.com/migrationhub/orchestrator?region=us-east-1#/templates"). For more information, see [Replatform
applications to Amazon ECS](../../../migrationhub-orchestrator/latest/userguide/replatform-to-ecs.md "../../../migrationhub-orchestrator/latest/userguide/replatform-to-ecs.md") in the _AWS Migration Hub Orchestrator User
Guide_.

###### Contents

- [Prerequisites](automation-runbook.md#automation-runbook-prerequisites "automation-runbook.md#automation-runbook-prerequisites")
  - [Create policies and roles for the automation](automation-runbook.md#automation-runbook-prerequisites-create-policies-roles "automation-runbook.md#automation-runbook-prerequisites-create-policies-roles")
  - [Attaching
    the IAM role](automation-runbook.md#automation-runbook-prerequisites-instance-role-attach "automation-runbook.md#automation-runbook-prerequisites-instance-role-attach")

- [Run the automation](automation-runbook.md#automation-runbook-run "automation-runbook.md#automation-runbook-run")
  - [Runbook parameters](automation-runbook.md#automation-runbook-parameters "automation-runbook.md#automation-runbook-parameters")
  - [Running the
    automation](automation-runbook.md#automation-runbook-running-automation "automation-runbook.md#automation-runbook-running-automation")
  - [Reviewing output from the automation](automation-runbook.md#automation-runbook-reviewing-output "automation-runbook.md#automation-runbook-reviewing-output")

- [Complete the modernization
  process](automation-runbook.md#automation-runbook-completing-modernization-process "automation-runbook.md#automation-runbook-completing-modernization-process")

## Prerequisites

Before you run the automation, you must have:

- An S3 bucket to store your containerized application artifacts. This bucket
  must be in the same AWS account and Region as your Amazon EC2 instances being
  containerized. For more information, see [Creating a
  bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md") in the _Amazon Simple Storage Service User Guide_.
- An IAM service role with the permissions necessary for Automation, a capability of
  AWS Systems Manager, to run the automation on your behalf.
- An IAM role for your EC2 instances that permits the necessary actions to run
  the automation in your target instances.
- (Optional) A customer managed key in AWS KMS to use as your own server-side
  encryption key for Amazon S3. For more information, see [Customer managed
  keys](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") in the _Amazon Simple Storage Service User Guide_.
- If you are using AWS Application Migration Service and running this automation as a post-launch action, you must
  configure the EC2 launch template setting **Auto-assign public
  IP** to `Enabled`. For more information, see [Full launch template setting review](../../../mgn/latest/ug/ec2-considerations-1.md#detailed-considerations "../../../mgn/latest/ug/ec2-considerations-1.md#detailed-considerations") in the _AWS Application Migration Service User
  Guide_.

###### Topics

- [Create policies and roles for the automation](#automation-runbook-prerequisites-create-policies-roles "#automation-runbook-prerequisites-create-policies-roles")
- [Attaching
  the IAM role](#automation-runbook-prerequisites-instance-role-attach "#automation-runbook-prerequisites-instance-role-attach")

### Create policies and roles for the automation

You must create the required policies and roles before running the automation. You can
create the roles using AWS CloudFormation or manually.

You can use the following AWS CloudFormation template to create a stack which will
create the roles and policies required to run the automation. You can create
a stack using the [AWS CloudFormation console](../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md") or the [AWS Command Line Interface (AWS CLI)](../../../AWSCloudFormation/latest/UserGuide/using-cfn-cli-creating-stack.md "../../../AWSCloudFormation/latest/UserGuide/using-cfn-cli-creating-stack.md").

```
AWSTemplateFormatVersion: "2010-09-09"
Parameters:
  A2CServiceRoleName:
    Type: String
    Description: Name of the A2C Service Role
    Default: "a2cServiceRole"

  A2CInstanceRoleName:
    Type: String
    Description: Name of the A2C Instance Role
    Default: "a2cinstancerole"

Resources:
  A2CServiceRole:
    Type: "AWS::IAM::Role"
    Properties:
      RoleName: !Ref A2CServiceRoleName
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: "Allow"
            Principal:
              Service: ["ssm.amazonaws.com"]
            Action: "sts:AssumeRole"
      Policies:
        - PolicyName: "a2cServicePolicy"
          PolicyDocument:
            Version: "2012-10-17"
            Statement:
              - Sid: "EC2DescribeAccess"
                Effect: "Allow"
                Action:
                  - "ec2:DescribeInstances"
                Resource: "*"
              - Sid: "IAMRoleAccess"
                Effect: "Allow"
                Action:
                  - "iam:AttachRolePolicy"
                  - "iam:GetInstanceProfile"
                Resource: "*"
              - Sid: "ApplicationTransformationAccess"
                Effect: "Allow"
                Action:
                  - "application-transformation:StartRuntimeAssessment"
                  - "application-transformation:GetRuntimeAssessment"
                  - "application-transformation:PutMetricData"
                  - "application-transformation:PutLogData"
                Resource: "*"
              - Sid: "SSMSendCommandAccess"
                Effect: "Allow"
                Action:
                  - "ssm:SendCommand"
                Resource:
                  - "arn:aws:ec2:*:*:instance/*"
                  - "arn:aws:ssm:*::document/AWS-RunRemoteScript"
              - Sid: "SSMDescribeAccess"
                Effect: "Allow"
                Action:
                  - "ssm:DescribeInstanceInformation"
                  - "ssm:ListCommandInvocations"
                  - "ssm:GetCommandInvocation"
                  - "ssm:GetParameters"
                Resource: "arn:aws:ssm:*:*:*"
              - Sid: "S3ObjectAccess"
                Effect: "Allow"
                Action:
                  - "s3:GetObject"
                  - "s3:PutObject"
                Resource:
                  - "arn:aws:s3:::*/application-transformation*"
              - Sid: "S3ListAccess"
                Effect: "Allow"
                Action:
                  - "s3:ListBucket"
                  - "s3:GetBucketLocation"
                Resource: "arn:aws:s3:::*"
              - Sid: "KmsAccess"
                Effect: "Allow"
                Action:
                  - "kms:GenerateDataKey"
                  - "kms:Decrypt"
                Resource:
                  - "arn:aws:kms:*:*:key/*"
                Condition:
                  StringLike:
                    kms:ViaService:
                      - "s3.*.amazonaws.com"

  A2CInstanceRole:
    Type: "AWS::IAM::Role"
    Properties:
      RoleName: !Ref A2CInstanceRoleName
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: "Allow"
            Principal:
              Service: ["ec2.amazonaws.com"]
            Action: "sts:AssumeRole"
      ManagedPolicyArns:
      - "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore"
      Policies:
        - PolicyName: "ApplicationTransformationAnalyzerPolicy"
          PolicyDocument:
            Version: "2012-10-17"
            Statement:
              - Sid: "S3BucketAccess"
                Effect: "Allow"
                Action:
                  - "s3:GetBucketLocation"
                Resource:
                  - "arn:aws:s3:::*"
              - Sid: "S3ObjectAccess"
                Effect: "Allow"
                Action:
                  - "s3:PutObject"
                  - "s3:GetObject"
                Resource:
                  - "arn:aws:s3:::*/application-transformation*"
              - Sid: "KmsAccess"
                Effect: "Allow"
                Action:
                  - "kms:GenerateDataKey"
                  - "kms:Decrypt"
                Resource:
                  - "arn:aws:kms:*:*:key/*"
                Condition:
                  StringLike:
                    kms:ViaService:
                      - "s3.*.amazonaws.com"
              - Sid: "TelemetryAccess"
                Effect: "Allow"
                Action:
                  - "application-transformation:PutMetricData"
                  - "application-transformation:PutLogData"
                Resource:
                  - "*"
  a2cInstanceProfile:
    Type: AWS::IAM::InstanceProfile
    Properties:
      InstanceProfileName: !Ref A2CInstanceRoleName
      Roles:
        - !Ref A2CInstanceRole

```

The following sections detail how you can manually create the roles and
policies required to run the automation.

##### Creating policies to run the automation

To enhance the security posture of the App2Container automation execution, it
is strongly recommended to scope down IAM S3 access permissions to
allow access only to the bucket created for the App2Container automation
execution. You can create least-privilege policies required to run the
automation with the following procedures.

###### To create the service role

policy for running the automation

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies**
   then choose **Create policy**.
3. Choose **JSON**, enter the following policy
   in the **Policy editor**, then choose
   **Next**:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "EC2DescribeAccess",
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeInstances"
 ],
 "Resource": "*"
 },
 {
 "Sid": "IAMRoleAccess",
 "Effect": "Allow",
 "Action": [
 "iam:AttachRolePolicy",
 "iam:GetInstanceProfile"
 ],
 "Resource": ["*"]
 },
 {
 "Sid": "ApplicationTransformationAccess",
 "Effect": "Allow",
 "Action": [
 "application-transformation:StartRuntimeAssessment",
 "application-transformation:GetRuntimeAssessment",
 "application-transformation:PutMetricData",
 "application-transformation:PutLogData"
 ],
 "Resource": "*"
 },
 {
 "Sid": "SSMSendCommandAccess",
 "Effect": "Allow",
 "Action": [
 "ssm:SendCommand"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:instance/*",
 "arn:aws:ssm:*::document/AWS-RunRemoteScript"
 ]
 },
 {
 "Sid": "SSMDescribeAccess",
 "Effect": "Allow",
 "Action": [
 "ssm:DescribeInstanceInformation",
 "ssm:ListCommandInvocations",
 "ssm:GetCommandInvocation",
 "ssm:GetParameters"
 ],
 "Resource": "arn:aws:ssm:*:*:*"
 },
 {
 "Sid": "S3ObjectAccess",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::*/application-transformation*"
 ]
 },
 {
 "Sid": "S3ListAccess",
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket",
 "s3:GetBucketLocation"
 ],
 "Resource": "arn:aws:s3:::*"
 },
 {
 "Sid": "KmsAccess",
 "Effect": "Allow",
 "Action": [
 "kms:GenerateDataKey",
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:*:*:key/*"
 ],
 "Condition": {
 "StringLike": {
 "kms:ViaService": [
 "s3.*.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```

4. Enter a value for the **Policy name**.
5. Choose **Create policy**.

###### To create the policy for the

IAM role used by your instance profile

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies**
   then choose **Create policy**.
3. Choose **JSON**, enter the following policy
   in the **Policy editor**, then choose
   **Next**:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "S3BucketAccess",
 "Effect": "Allow",
 "Action": [
 "s3:GetBucketLocation"
 ],
 "Resource": [
 "arn:aws:s3:::*"
 ]
 },
 {
 "Sid": "S3ObjectAccess",
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::*/application-transformation*"
 ]
 },
 {
 "Sid": "KmsAccess",
 "Effect": "Allow",
 "Action": [
 "kms:GenerateDataKey",
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:*:*:key/*"
 ],
 "Condition": {
 "StringLike": {
 "kms:ViaService": [
 "s3.*.amazonaws.com"
 ]
 }
 }
 },
 {
 "Sid": "TelemetryAccess",
 "Effect": "Allow",
 "Action": [
 "application-transformation:PutMetricData",
 "application-transformation:PutLogData"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

4. Enter
   `ApplicationTransformationAnalyzerPolicy`
   for the **Policy name**.
5. Choose **Create policy**.

##### Creating

the IAM service role for running the automation

You can use the following procedure to create an IAM service
role.

###### To create an IAM role using

the IAM console

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles** then
   choose **Create role**.
3. On the **Select trusted entity** page, choose
   **AWS service**, select the
   **Systems Manager** use case, and then
   choose **Next**.
4. On the **Add permissions** page, select the
   policy that you created for the IAM service role previously,
   and then choose **Next**.
5. On the **Name, review, and create** page,
   enter a name and description for the role and add tags if
   needed.
6. Choose **Create role**.

This role is used for the `AutomationAssumeRole` parameter
in the [Run the automation](#automation-runbook-run "#automation-runbook-run") section.

##### Creating the instance profile role

You can use the following procedure to create an IAM role for your
instance profile. The permissions provided by the instance profile role
are used by your EC2 instances. For more information, see [Using
an IAM role to grant permissions to applications running on Amazon EC2
instances](../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2.md") in the _AWS Identity and Access Management User
Guide_.

###### Note

An instance profile can only contain one IAM role. If your
target instances have an existing IAM role, the automation will
add the `ApplicationTransformationAnalyzerPolicy` policy
on execution to the instance profile role on your behalf. The
existing role should provide the permissions required to make the
instances managed nodes in AWS Systems Manager. For more information, see
[Instance profiles](../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md#attach-iam-role "../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md#attach-iam-role") in the _Amazon Elastic Compute Cloud User
Guide_ and [Managed nodes](../../../systems-manager/latest/userguide/managed_instances.md "../../../systems-manager/latest/userguide/managed_instances.md") in the _AWS Systems Manager User
Guide_.

###### To create an instance profile

role using the IAM console

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles** then
   choose **Create role**.
3. On the **Select trusted entity** page, choose
   **AWS service**, select the
   **EC2** use case, and then choose
   **Next**.
4. On the **Add permissions** page, select both
   the `AmazonSSMManagedInstanceCore` policy and the
   policy you created for the instance profile role previously, and
   then choose **Next**.
5. On the **Name, review, and create** page,
   enter a name and description for the role and add tags if
   needed.
6. Choose **Create role**.

The instance profile role is used in the following section.

### Attaching

the IAM role

If your target instances don't have an existing IAM role, you can attach the
previously created IAM role to them. The following steps assume you have already
created the required policies and roles.

###### To attach an IAM role to

an instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Instances**.
3. Select the instance, choose **Actions**,
   **Security**, **Modify IAM
   role**.
4. Select the IAM role to attach to your instance, and
   choose **Save**.

For more information, see [Attach an IAM role to an instance](../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md#attach-iam-role "../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md#attach-iam-role").

## Run the automation

When you run the automation, the following processes occur:

- Discover – The instances you specified are scanned for supported
  applications to create an inventory of each server.
- Analyze – Once the discover phase has completed, the automation analyzes each
  application and creates an entry. The instances you specified are scanned for
  supported applications to create an inventory of each server. Once this
  discovery process has completed, the automation analyzes each application and
  creates an entry.

###### Note

Applications using Windows Server operating systems will use Windows
Server Core as their base image. Applications using Linux operating systems
will use a Linux based image.

###### Topics

- [Runbook parameters](#automation-runbook-parameters "#automation-runbook-parameters")
- [Running the
  automation](#automation-runbook-running-automation "#automation-runbook-running-automation")
- [Reviewing output from the automation](#automation-runbook-reviewing-output "#automation-runbook-reviewing-output")

### Runbook parameters

You can specify the following parameters for the Automation runbook.

| Parameter name           | Type    | Description                                                                                                                                                                                                                                                                                                                        | Default value | Required |
| ------------------------ | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | -------- |
| `AutomationAssumeRole`   | String  | The ARN of the role that allows Automation to perform actions<br>on your behalf.                                                                                                                                                                                                                                                   |               | TRUE     |
| `EnableContainerization` | Boolean | Controls whether to containerize discovered applications. If enabled, the automation<br>will use the artifacts uploaded to the S3 bucket to generate<br>Open Containers Initiative (OCI) container images and push them<br>to Amazon ECR.                                                                                          | FALSE         | FALSE    |
| `OutputLocation`         | String  | The S3 location in which to upload deployment artifacts. The bucket must be in the same<br>account and Region of the EC2 instance. All artifacts will be<br>created with a prefix of<br>`application-transformation`.                                                                                                              |               | TRUE     |
| `OutputEncryptionKey`    | String  | The ARN of a customer managed KMS key to use for server-side encryption. For more information,<br>see [Protecting data with server-side encryption](../../../AmazonS3/latest/userguide/serv-side-encryption.md "../../../AmazonS3/latest/userguide/serv-side-encryption.md") in the<br>_Amazon Simple Storage Service User Guide_. |               | FALSE    |
| `InstanceId`             | String  | An EC2 instance ID with applications to be assessed for<br>replatforming. Only running applications are assessed.                                                                                                                                                                                                                  |               | TRUE     |

### Running the

automation

You can run the automation from the Systems Manager console.

###### To run the automation

1. Access the AWS Systems Manager Automation console at [https://console.aws.amazon.com/systems-manager/automation](https://console.aws.amazon.com/systems-manager/automation "https://console.aws.amazon.com/systems-manager/automation").
2. Choose **Execute automation**.
3. Under **Automation runbook**, enter
   `AWSApp2Container-ReplatformApplications`, and search the
   repository.
4. Choose the `AWSApp2Container-ReplatformApplications` runbook, then choose
   **Next**.
5. Enter the required parameters, and any optional ones you require:
   1. For `AutomationAssumeRole`, enter the ARN of the
      service role you created previously.
   2. For `EnableContainerization`, specify `TRUE`
      if you want your containerized applications pushed to Amazon ECR.
   3. For `OutputLocation`, specify the S3 path to upload
      artifacts to.
   4. For `OutputEncryptionKey`, you can specify the ARN of a
      KMS key if you want to encrypt the uploaded objects with your
      customer managed key.
   5. For `InstanceId`, specify the instance ID for the
      automation to take action on.

6. Choose **Execute**.

### Reviewing output from the automation

Once the automation has completed, you can access the output in the S3 location that you provided.

###### To review output from the automation

1. Access the AWS Systems Manager Automation console at [https://console.aws.amazon.com/systems-manager/automation](https://console.aws.amazon.com/systems-manager/automation "https://console.aws.amazon.com/systems-manager/automation").
2. Choose the **Execution ID** to review.
3. Select **Outputs** and review the
   **Finalize.report** output.
4. For more details, review the text file indicated in the
   **Finalize.reportS3Location** output.

## Complete the modernization

process

You can complete the modernization process using AWS Migration Hub Orchestrator to create a workflow based
on the _Replatform applications to Amazon ECS_ template to deploy
your applications on Amazon ECS on AWS Fargate. This template can use the application
artifacts App2Container uploaded to Amazon S3. For more information, see [Replatform applications to Amazon ECS](../../../migrationhub-orchestrator/latest/userguide/replatform-to-ecs.md "../../../migrationhub-orchestrator/latest/userguide/replatform-to-ecs.md") in the _AWS Migration Hub Orchestrator User
Guide_.

To continue the containerization process without Migration Hub Orchestrator, you can use the App2Container CLI extraction and
containerization process. For more information, see [Step 4: Transform your application](start-intro.md#start-step4-transform "start-intro.md#start-step4-transform").

After performing the containerization process with App2Container, continue with the deployment phase to
complete the modernization process. You can use either App2Container or proprietary deployment
tools. If you use the App2Container CLI, you can generate the required AWS CloudFormation templates. For more
information about deploying your containerized application using App2Container, see [Step 5: Deploy your application](start-intro.md#start-step5-deploy "start-intro.md#start-step5-deploy").
