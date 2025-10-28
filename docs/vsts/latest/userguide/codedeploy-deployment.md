# AWS CodeDeploy Application Deployment task

## Synopsis

Deploys an application to Amazon EC2 instances by using AWS CodeDeploy.

## Description

This can be a variety of application content, such as code, web and configuration files,
executable files, packages, scripts, and multimedia files.

## Parameters

You can set the following parameters for the task. Required parameters are noted by an
asterisk (\*). Other parameters are optional.

### Display name\*

The default name of the task instance, which can be modified: Deploy with
CodeDeploy

### AWS Credentials

Specifies the AWS credentials to be used by the task in the build agent
environment.

You can specify credentials using a service endpoint (of type AWS) in the task
configuration or you can leave unspecified. If unspecified the task will attempt to
obtain credentials from the following sources in order:

- From task variables named _AWS.AccessKeyID_,
  _AWS.SecretAccessKey_ and optionally
  _AWS.SessionToken_.
- From credentials set in environment variables in the build agent process. When
  using environment variables in the build agent process you may use the standard
  AWS environment variables: _AWS_ACCESS_KEY_ID_,
  _AWS_SECRET_ACCESS_KEY_ and optionally
  _AWS_SESSION_TOKEN_.
- If the build agent is running on an Amazon EC2 instance, from the instance
  metadata associated with the EC2 instance. For credentials to be available from
  EC2 instance metadata the instance must have been started with an instance profile
  referencing a role granting permissions to the task to make calls to AWS on your
  behalf. For more information, see [Using an IAM role to grant permissions to applications running on Amazon EC2
  instances](../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2.md").

### AWS Region

The AWS Region code (for example, us-east-1, us-west-2) of the Region containing the
AWS resources the task will use or create. For more information, see [Regions and endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md") in
the _Amazon Web Services General Reference_.

If a Region is not specified in the task configuration the task will attempt to
obtain the Region to be used using the standard AWS environment variable
_AWS_REGION_ in the build agent process's environment. Tasks
running in build agents hosted on Amazon EC2 instances (Windows or Linux) will also
attempt to obtain the Region using the instance metadata associated with the EC2
instance if no Region is configured on the task or set in the environment
variable.

**Note:** The Regions listed in the picker are those known
at the time this software was released. New Regions that are not listed may still be
used by entering the _region code_ of the Region (for example,
_us_west_2_).

### Application Name\*

The name of the AWS CodeDeploy application.

### Deployment Group Name\*

The name of the deployment group the revision is to be deployed to.

### Deployment Revision Source\*

Specifies the source of the revision to be deployed. You can select from:

- _Folder or archive file in the workspace_: the task will create
  or use an existing zip archive in the location specified to _Revision
  Bundle_, upload the archive to Amazon S3 and supply the key of the S3
  object to CodeDeploy as the revision source.
- _Archive file in Amazon S3_: select to specify the key of an
  archive previously uploaded to Amazon S3 as the deployment revision source.

### Revision Bundle\*

The location of the application revision artifacts to deploy. You can supply a
filename or folder. If a folder is supplied the task will recursively zip the folder
contents into an archive file before uploading the archive to Amazon S3. If a filename is
supplied the task uploads it unmodified to Amazon S3. CodeDeploy requires the appspec.yml
file describing the application to exist at the root of the specified folder or archive
file.

Required if _Deployment Revision Source_ is set to
_Folder or archive file in the workspace_.

### S3 Bucket Name\*

The name of the Amazon S3 bucket to which the revision bundle is uploaded or can be
found, if _Archive file in Amazon S3_ was selected for
_Deployment Revision Source_.

### Target Folder

Optional folder (key prefix) for the uploaded revision bundle in the bucket. If not
specified the, bundle is uploaded to the root of the bucket.

Available when _Folder or archive file in the workspace_ is
selected for _Deployment Revision Source_.

### Revision Bundle Key

The Amazon S3 object key of the previously uploaded archive file containing the
deployment revision artifacts.

Required if _Deployment Revision Source_ is set to
_Archive file in Amazon S3_.

### Description

Optional description for the deployment.

### Existing File Behavior

How AWS CodeDeploy should handle files that already exist in a deployment target location
but weren't part of the previous successful deployment.

### Advanced

#### Update Outdated Instances

Only

If checked, deploys to only those instances that are not running the latest
application revision.

#### Ignore Application Stop

Failures

When checked, if the deployment causes the ApplicationStop deployment lifecycle
event to an instance to fail, the deployment to that instance is not considered
failed at that point. It continues on to the BeforeInstall deployment lifecycle
event.

#### Max Timeout

Maximum time, specified in minutes, that the task should wait for the stack
creation or update to complete. By default a maximum of 60 minutes is used.

### Output

#### Output Variable

The name of the variable that will contain the deployment ID on task completion.
You can use the variable $(variableName) to refer to the function result in
subsequent tasks.

## Task Permissions

This task requires permissions to call the following AWS service APIs (depending on
selected task options, not all APIs may be used):

- codedeploy:GetApplication
- codedeploy:GetDeploymentGroup
- codedeploy:CreateDeployment
- codedeploy:GetDeployment

Depending on selected parameters the task may also require permissions to verify your
deployment bundle exists in S3 or upload your application bundle to the specified Amazon S3
bucket. Depending on the size of the application bundle, either PutObject or the S3
multi-part upload APIs may be used.
