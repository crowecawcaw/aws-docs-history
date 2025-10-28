# How to use SageMaker AI execution roles

Amazon SageMaker AI performs operations on your behalf using other AWS services. You must grant
SageMaker AI permissions to use these services and the resources they act upon. You grant SageMaker AI
these permissions using an AWS Identity and Access Management (IAM) execution role. For more information on
IAM roles, see [IAM roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md").

To create and use an execution role, you can use the following procedures.

## Create execution

role

Use the following procedure to create an execution role with the IAM managed
policy, `AmazonSageMakerFullAccess`, attached. If your use case requires
more granular permissions, use other sections on this page to create an execution
role that meets your business needs. You can create an execution role using the SageMaker AI
console or the AWS CLI.

###### Important

The IAM managed policy, `AmazonSageMakerFullAccess`, used in the
following procedure only grants the execution role permission to perform certain
Amazon S3 actions on buckets or objects with `SageMaker`,
`Sagemaker`, `sagemaker`, or `aws-glue` in
the name. To learn how to add an additional policy to an execution role to grant
it access to other Amazon S3 buckets and objects, see [Add Additional Amazon S3
Permissions to a SageMaker AI Execution Role](#sagemaker-roles-get-execution-role-s3 "#sagemaker-roles-get-execution-role-s3").

###### Note

You can create an execution role directly when you create a SageMaker AI domain or
a notebook instance.

- For information on how to create a SageMaker AI domain, see [Guide to getting set up with Amazon SageMaker AI](gs.md "gs.md").
- For information on how to create a notebook instance, see [Create an Amazon SageMaker Notebook Instance for the
  tutorial](gs-setup-working-env.md "gs-setup-working-env.md").

**To create a new execution role from the SageMaker AI
console**

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Choose **Roles** and then choose **Create
   role**.
3. Keep **AWS service** as the **Trusted entity
   type** and then use the down arrow to find
   **SageMaker AI** in **Use cases for other AWS
   services**.
4. Choose **SageMaker AI – Execution** and then choose
   **Next**.
5. The IAM managed policy, `AmazonSageMakerFullAccess`, is
   automatically attached to the role. To see the permissions included in this
   policy, choose the plus (**+**) sign next to the policy
   name. Choose **Next**.
6. Enter a **Role name** and a
   **Description**.
7. (Optional) Add additional permissions and tags to the role.
8. Choose **Create role**.
9. On the **Roles** section of the IAM console, find the
   role you just created. If needed, use the text box to search for the role
   using the role name.
10. On the role summary page, make note of the ARN.

**To create a new execution role from the
AWS CLI**

Before you create an execution role using the AWS CLI, make sure to update and
configure it by following the instructions in [(Optional) Configure the AWS CLI](gs-set-up.md#gs-cli-prereq "gs-set-up.md#gs-cli-prereq"), then continue with the instructions in [Custom setup using the AWS CLI](onboard-custom.md#onboard-custom-instructions-cli "onboard-custom.md#onboard-custom-instructions-cli").

Once you have created an execution role, you can associate it with a SageMaker AI domain,
a user profile, or with a Jupyter notebook instance.

- To learn about how to associate an execution role with an existing SageMaker AI
  domain, see [Edit domain settings](domain-edit.md "domain-edit.md").
- To learn about how to associate an execution role with an existing user
  profile, see [Add user profiles](domain-user-profile-add.md "domain-user-profile-add.md").
- To learn about how to associate an execution role with an existing
  notebook instance, see [Update a Notebook Instance](nbi-update.md "nbi-update.md").

You can also pass the ARN of an execution role to your API call. For example,
using [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable "https://sagemaker.readthedocs.io/en/stable"), you can pass the ARN of your execution role to an
estimator. In the code sample that follows, we create an estimator using the XGBoost
algorithm container and pass the ARN of the execution role as a parameter. For the
full example on GitHub, see [Customer Churn Prediction with XGBoost](https://github.com/aws/amazon-sagemaker-examples/blob/89c54681b7e0f83ce137b34b879388cf5960af93/introduction_to_applying_machine_learning/xgboost_customer_churn/xgboost_customer_churn.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/89c54681b7e0f83ce137b34b879388cf5960af93/introduction_to_applying_machine_learning/xgboost_customer_churn/xgboost_customer_churn.ipynb").

```
import sagemaker, boto3
from sagemaker import image_uris

sess = sagemaker.Session()
region = sess.boto_region_name
bucket = sess.default_bucket()
prefix = "sagemaker/DEMO-xgboost-churn"
container = sagemaker.image_uris.retrieve("xgboost", region, "1.7-1")

xgb = sagemaker.estimator.Estimator(
    container,
    `execution-role-ARN`,
    instance_count=1,
    instance_type="ml.m4.xlarge",
    output_path="s3://{}/{}/output".format(bucket, prefix),
    sagemaker_session=sess,
)

...

```

### Add Additional Amazon S3

Permissions to a SageMaker AI Execution Role

When you use a SageMaker AI feature with resources in Amazon S3, such as input data, the
execution role you specify in your request (for example
`CreateTrainingJob`) is used to access these resources.

If you attach the IAM managed policy,
`AmazonSageMakerFullAccess`, to an execution role, that role has
permission to perform certain Amazon S3 actions on buckets or objects with
`SageMaker`, `Sagemaker`, `sagemaker`, or
`aws-glue` in the name. It also has permission to perform the
following actions on any Amazon S3 resource:

```
"s3:CreateBucket",
"s3:GetBucketLocation",
"s3:ListBucket",
"s3:ListAllMyBuckets",
"s3:GetBucketCors",
"s3:PutBucketCors"
```

To give an execution role permissions to access one or more specific buckets
in Amazon S3, you can attach a policy similar to the following to the role. This
policy grants an IAM role permission to perform all actions that
`AmazonSageMakerFullAccess` allows but restricts this access to
the buckets amzn-s3-demo-bucket1 and amzn-s3-demo-bucket2. Refer to the security
documentation for the specific SageMaker AI feature you are using to learn more about
the Amazon S3 permissions required for that feature.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:PutObject",
 "s3:DeleteObject",
 "s3:AbortMultipartUpload"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket1/*`",
 "arn:aws:s3:::`amzn-s3-demo-bucket2/*`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:CreateBucket",
 "s3:GetBucketLocation",
 "s3:ListBucket",
 "s3:ListAllMyBuckets",
 "s3:GetBucketCors",
 "s3:PutBucketCors"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetBucketAcl",
 "s3:PutObjectAcl"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket1`",
 "arn:aws:s3:::`amzn-s3-demo-bucket2`"
 ]
 }
 ]
}`

```

## Get your execution role

You can use the [SageMaker AI console](https://console.aws.amazon.com/sagemaker "https://console.aws.amazon.com/sagemaker"),
[Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable "https://sagemaker.readthedocs.io/en/stable"), or the [AWS CLI](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md") to retrieve the
ARN and name of the execution role attached to a SageMaker AI domain, space, or user
profile.

###### Topics

- [Get domain
  execution role](#sagemaker-roles-get-execution-role-domain "#sagemaker-roles-get-execution-role-domain")
- [Get space execution
  role](#sagemaker-roles-get-execution-role-space "#sagemaker-roles-get-execution-role-space")
- [Get user execution
  role](#sagemaker-roles-get-execution-role-user "#sagemaker-roles-get-execution-role-user")

### Get domain

execution role

The following provides instructions on finding your domain’s execution
role.

###### Find the execution role attached to your domain

1. Open the SageMaker AI console, [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/")
2. On the left navigation pane, choose
   **Domains** under **Admin
   configurations**.
3. Choose the link corresponding to your domain.
4. Choose the **Domain settings** tab.
5. In the **General settings** section, the
   execution role ARN is listed under **Execution
   role**.

The execution role name is after the last `/` in
the execution role ARN.

### Get space execution

role

The following provides instructions on finding your space’s execution
role.

###### Find the execution role attached to your space

1. Open the SageMaker AI console, [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/")
2. On the left navigation pane, choose
   **Domains** under **Admin
   configurations**.
3. Choose the link corresponding to your domain.
4. Choose the **Space management** tab.
5. In the **Details** section, the execution
   role ARN is listed under **Execution role**.

The execution role name is after the last `/` in
the execution role ARN.

###### Note

The following code is meant to be run in a SageMaker AI environment, like
any of the IDEs in Amazon SageMaker Studio. You will receive an error if you
run `get_execution_role` outside of a SageMaker AI
environment.

The following [`get_execution_role`](https://sagemaker.readthedocs.io/en/stable/api/utility/session.html#sagemaker.session.get_execution_role "https://sagemaker.readthedocs.io/en/stable/api/utility/session.html#sagemaker.session.get_execution_role") [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable "https://sagemaker.readthedocs.io/en/stable")
command retrieves the ARN of the execution role attached to the
space.

```
from sagemaker import get_execution_role
role = get_execution_role()
print(role)
```

The execution role name is after the last `/` in the
execution role ARN.

### Get user execution

role

The following provides instructions on finding a user’s execution role.

###### Find the execution role attached to a user

1. Open the SageMaker AI console, [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/")
2. On the left navigation pane, choose
   **Domains** under **Admin
   configurations**.
3. Choose the link corresponding to your domain.
4. Choose the **User profiles** tab.
5. Choose the link corresponding to your user.
6. In the **Details** section, the execution
   role ARN is listed under **Execution role**.

The execution role name is after the last `/` in
the execution role ARN.

###### Note

To use the following examples, you must have the AWS Command Line Interface (AWS CLI)
installed and configured. For information, see [Get
started with the AWS CLI](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md") in the _AWS Command Line Interface User
Guide for Version 2_.

The following [`get-caller-identity`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sts/get-caller-identity.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sts/get-caller-identity.html") AWS CLI command displays
information about the IAM identity used to authenticate the request.
The caller is an IAM user.

```
aws sts get-caller-identity
```

The execution role name is after the last `/` in the
execution role ARN.

## Change your execution

role

An execution role is an IAM role that a SageMaker AI identity (like a SageMaker AI user, space,
or domain) assumes. Changing the IAM role changes the permissions for all of
the identities assuming that role.

When you change an execution role the corresponding space's execution role will
also change. The effects of the change may take some time to propagate.

- When you change a _user's execution
  role_, the _private spaces_
  created by that user will assume the changed execution role.
- When you change a _space's default execution
  role_, the _shared spaces_ in
  the domain will assume the changed execution role.

For more information on execution roles and spaces, see [Understanding domain space permissions and
execution roles](execution-roles-and-spaces.md "execution-roles-and-spaces.md").

You can change the execution role for a identity to a different IAM role by
using one of the following instructions.

If, instead, you want to _modify_ a role that an
identity is assuming, see [Modify permissions to
execution role](#sagemaker-roles-modify-to-execution-role "#sagemaker-roles-modify-to-execution-role").

###### Topics

- [Change the
  domain default execution role](#sagemaker-roles-change-execution-role-domain "#sagemaker-roles-change-execution-role-domain")
- [Change space
  default execution role](#sagemaker-roles-change-execution-role-space "#sagemaker-roles-change-execution-role-space")
- [Change user profile
  execution role](#sagemaker-roles-change-execution-role-user "#sagemaker-roles-change-execution-role-user")

### Change the

domain default execution role

The following provides instructions on changing your domain’s default
execution role.

###### Change the default execution role attached to your domain

1. Open the SageMaker AI console, [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/")
2. On the left navigation pane, choose
   **Domains** under **Admin
   configurations**.
3. Choose the link corresponding to your domain.
4. Choose the **Domain settings** tab.
5. In the **General settings** section, choose
   **Edit**.
6. In the **Permissions** section, under
   **Default execution role** expand the
   drop-down list.
7. In the drop-down list you can choose an existing role, enter a
   custom IAM role ARN, or create a new role.

If you wish to create a new role, you can choose
**Create role using the role creation
wizard** option. 8. Choose Next in the following steps and choose Submit on the
last step.

### Change space

default execution role

The following provides instructions on changing your space’s default execution
role. Changing this execution role will change the role assumed by all of the
shared spaces in the domain.

###### Change the space default execution role for when you create a new

space

1. Open the SageMaker AI console, [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/")
2. On the left navigation pane, choose
   **Domains** under **Admin
   configurations**.
3. Choose the link corresponding to your domain.
4. Choose the **Domain settings** tab.
5. In the **General settings** section, choose
   **Edit**.
6. In the **Permissions** section, under
   **Space default execution role** expand the
   drop-down list.
7. In the drop-down list you can choose an existing role, enter a
   custom IAM role ARN, or create a new role.

If you wish to create a new role, you can choose
**Create role using the role creation
wizard** option. 8. Choose **Next** in the following steps and
choose **Submit** on the last step.

### Change user profile

execution role

The following provides instructions on changing a user’s execution role.
Changing this execution role will change the role assumed by all of the private
spaces created by this user.

###### Change the execution role attached to a user

1. Open the SageMaker AI console, [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/")
2. On the left navigation pane, choose
   **Domains** under **Admin
   configurations**.
3. Choose the link corresponding to your domain.
4. Choose the **User profiles** tab.
5. Choose the link corresponding to the user profile name.
6. Choose **Edit**.
7. In the drop-down list you can choose an existing role, enter a
   custom IAM role ARN, or create a new role.

If you wish to create a new role, you can choose
**Create role using the role creation
wizard** option. 8. Choose **Next** in the following steps and
choose **Submit** on the last step.

## Modify permissions to

execution role

You can modify existing permissions to the execution role of an identity (like a
SageMaker AI user, space, or domain). This is done by finding the appropriate IAM role
that the identity is assuming, then modifying that IAM role. The following will
provide instructions on achieving this through the console.

When you modify an execution role the corresponding space's execution role will
also change. The effects of the change may not be immediate.

- When you modify a _user's execution
  role_, the _private spaces_
  created by that user will assume the modified execution role.
- When you modify a _space's default execution
  role_, the _shared spaces_ in
  the domain will assume the modified execution role.

For more information on execution roles and spaces, see [Understanding domain space permissions and
execution roles](execution-roles-and-spaces.md "execution-roles-and-spaces.md").

If, instead, you want to _change_ a role that an
identity is assuming, see [Change your execution
role](#sagemaker-roles-change-execution-role "#sagemaker-roles-change-execution-role").

###### To modify permissions to your execution roles

1. First get name of the identity you would like to modify.
   - [Get domain
     execution role](#sagemaker-roles-get-execution-role-domain "#sagemaker-roles-get-execution-role-domain")
   - [Get space execution
     role](#sagemaker-roles-get-execution-role-space "#sagemaker-roles-get-execution-role-space")
   - [Get user execution
     role](#sagemaker-roles-get-execution-role-user "#sagemaker-roles-get-execution-role-user")

2. To modify a role that an identity is assuming, see [Modifying
   a role](../../../IAM/latest/UserGuide/id_roles_manage_modify.md "../../../IAM/latest/UserGuide/id_roles_manage_modify.md") in the _AWS Identity and Access Management User
   Guide_.

For more information and instructions on adding permissions to
IAM identities, see [Add or remove identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") in the _AWS Identity and Access Management User Guide_.

## Passing Roles

Actions like passing a role between services are a common function within SageMaker AI.
You can find more details on [Actions, Resources, and Condition Keys for SageMaker AI](../../../service-authorization/latest/reference/list_amazonsagemaker.md#amazonsagemaker-actions-as-permissions "../../../service-authorization/latest/reference/list_amazonsagemaker.md#amazonsagemaker-actions-as-permissions") in the
_Service Authorization Reference_.

You pass the role (`iam:PassRole`) when making these API calls: [`CreateAutoMLJob`](../APIReference/API_CreateAutoMLJob.md "../APIReference/API_CreateAutoMLJob.md"), [`CreateCompilationJob`](../APIReference/API_CreateCompilationJob.md "../APIReference/API_CreateCompilationJob.md"), [`CreateDomain`](../APIReference/API_CreateDomain.md "../APIReference/API_CreateDomain.md"), [`CreateFeatureGroup`](../APIReference/API_CreateFeatureGroup.md "../APIReference/API_CreateFeatureGroup.md"), [`CreateFlowDefiniton`](../APIReference/API_CreateFlowDefinition.md "../APIReference/API_CreateFlowDefinition.md"), [`CreateHyperParameterTuningJob`](../APIReference/API_CreateHyperParameterTuningJob.md "../APIReference/API_CreateHyperParameterTuningJob.md"), [`CreateImage`](../APIReference/API_CreateImage.md "../APIReference/API_CreateImage.md"), [`CreateLabelingJob`](../APIReference/API_CreateLabelingJob.md "../APIReference/API_CreateLabelingJob.md"), [`CreateModel`](../APIReference/API_CreateModel.md "../APIReference/API_CreateModel.md"), [`CreateMonitoringSchedule`](../APIReference/API_CreateMonitoringSchedule.md "../APIReference/API_CreateMonitoringSchedule.md"), [`CreateNotebookInstance`](../APIReference/API_CreateNotebookInstance.md "../APIReference/API_CreateNotebookInstance.md"), [`CreateProcessingJob`](../APIReference/API_CreateProcessingJob.md "../APIReference/API_CreateProcessingJob.md"), [`CreateTrainingJob`](../APIReference/API_CreateTrainingJob.md "../APIReference/API_CreateTrainingJob.md"), [`CreateUserProfile`](../APIReference/API_CreateUserProfile.md "../APIReference/API_CreateUserProfile.md"), [`RenderUiTemplate`](../APIReference/API_RenderUiTemplate.md "../APIReference/API_RenderUiTemplate.md"), [`UpdateImage`](../APIReference/API_UpdateImage.md "../APIReference/API_UpdateImage.md"), and [`UpdateNotebookInstance`](../APIReference/API_UpdateNotebookInstance.md "../APIReference/API_UpdateNotebookInstance.md").

You attach the following trust policy to the IAM role which grants SageMaker AI principal
permissions to assume the role, and is the same for all of the execution roles:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "sagemaker.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

The permissions that you need to grant to the role vary depending on the API that
you call. The following sections explain these permissions.

###### Note

Instead of managing permissions by crafting a permission policy, you can use
the AWS-managed `AmazonSageMakerFullAccess` permission policy. The
permissions in this policy are fairly broad, to allow for any actions you might
want to perform in SageMaker AI. For a listing of the policy including information about
the reasons for adding many of the permissions, see [AWS managed policy:
AmazonSageMakerFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonSageMakerFullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonSageMakerFullAccess"). If you
prefer to create custom policies and manage permissions to scope the permissions
only to the actions you need to perform with the execution role, see the
following topics.

###### Important

If you're running into issues, see [Troubleshooting Amazon SageMaker AI
Identity and Access](security_iam_troubleshoot.md "security_iam_troubleshoot.md").

For more information about IAM roles, see [IAM
Roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") in the _Service Authorization Reference_.

###### Topics

- [CreateAutoMLJob and CreateAutoMLJobV2 API: Execution
  Role Permissions](#sagemaker-roles-autopilot-perms "#sagemaker-roles-autopilot-perms")
- [CreateDomain API: Execution
  Role Permissions](#sagemaker-roles-createdomain-perms "#sagemaker-roles-createdomain-perms")
- [CreateImage and UpdateImage
  APIs: Execution Role Permissions](#sagemaker-roles-createimage-perms "#sagemaker-roles-createimage-perms")
- [CreateNotebookInstance API: Execution Role Permissions](#sagemaker-roles-createnotebookinstance-perms "#sagemaker-roles-createnotebookinstance-perms")
- [CreateHyperParameterTuningJob API: Execution Role Permissions](#sagemaker-roles-createhyperparametertiningjob-perms "#sagemaker-roles-createhyperparametertiningjob-perms")
- [CreateProcessingJob API:
  Execution Role Permissions](#sagemaker-roles-createprocessingjob-perms "#sagemaker-roles-createprocessingjob-perms")
- [CreateTrainingJob API:
  Execution Role Permissions](#sagemaker-roles-createtrainingjob-perms "#sagemaker-roles-createtrainingjob-perms")
- [CreateModel API: Execution Role
  Permissions](#sagemaker-roles-createmodel-perms "#sagemaker-roles-createmodel-perms")
- [SageMaker geospatial capabilities roles](sagemaker-geospatial-roles.md "sagemaker-geospatial-roles.md")

## CreateAutoMLJob and CreateAutoMLJobV2 API: Execution

Role Permissions

For an execution role that you can pass in a `CreateAutoMLJob` or `CreateAutoMLJobV2` API
request, you can attach the following minimum permission policy to the role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "sagemaker.amazonaws.com"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "sagemaker:DescribeEndpointConfig",
 "sagemaker:DescribeModel",
 "sagemaker:InvokeEndpoint",
 "sagemaker:ListTags",
 "sagemaker:DescribeEndpoint",
 "sagemaker:CreateModel",
 "sagemaker:CreateEndpointConfig",
 "sagemaker:CreateEndpoint",
 "sagemaker:DeleteModel",
 "sagemaker:DeleteEndpointConfig",
 "sagemaker:DeleteEndpoint",
 "cloudwatch:PutMetricData",
 "logs:CreateLogStream",
 "logs:PutLogEvents",
 "logs:CreateLogGroup",
 "logs:DescribeLogStreams",
 "s3:GetObject",
 "s3:PutObject",
 "s3:ListBucket",
 "ecr:GetAuthorizationToken",
 "ecr:BatchCheckLayerAvailability",
 "ecr:GetDownloadUrlForLayer",
 "ecr:BatchGetImage"
 ],
 "Resource": "*"
 }
 ]
}`

```

If you specify a private VPC for your AutoML job, add the following
permissions:

```
{
    "Effect": "Allow",
    "Action": [
        "ec2:CreateNetworkInterface",
        "ec2:CreateNetworkInterfacePermission",
        "ec2:DeleteNetworkInterface",
        "ec2:DeleteNetworkInterfacePermission",
        "ec2:DescribeNetworkInterfaces",
        "ec2:DescribeVpcs",
        "ec2:DescribeDhcpOptions",
        "ec2:DescribeSubnets",
        "ec2:DescribeSecurityGroups"
    ]
}
```

If your input is encrypted using server-side encryption with an AWS KMS–managed
key (SSE-KMS), add the following permissions:

```
{
    "Effect": "Allow",
    "Action": [
        "kms:Decrypt"
    ]
}
```

If you specify a KMS key in the output configuration of your AutoML job, add the
following permissions:

```
{
    "Effect": "Allow",
    "Action": [
    "kms:Encrypt"
    ]
}
```

If you specify a volume KMS key in the resource configuration of your AutoML job,
add the following permissions:

```
{
    "Effect": "Allow",
    "Action": [
    "kms:CreateGrant"
    ]
}
```

## CreateDomain API: Execution

Role Permissions

The execution role for domains with IAM Identity Center and the user/execution role for
IAM domains need the following permissions when you pass an AWS KMS customer managed key
as the `KmsKeyId` in the `CreateDomain` API request. The
permissions are enforced during the `CreateApp` API call.

For an execution role that you can pass in the `CreateDomain` API
request, you can attach the following permission policy to the role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kms:CreateGrant",
 "kms:DescribeKey"
 ],
 "Resource": "arn:aws:kms:`us-east-1`:`111122223333`:key/`kms-key-id`"
 }
 ]
}`

```

Alternatively, if the permissions are specified in a KMS policy, you can attach
the following policy to the role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Allow use of the key",
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "arn:aws:iam::`111122223333`:role/`ExecutionRole`"
 ]
 },
 "Action": [
 "kms:CreateGrant",
 "kms:DescribeKey"
 ],
 "Resource": "*"
 }
 ]
}`

```

## CreateImage and UpdateImage

APIs: Execution Role Permissions

For an execution role that you can pass in a `CreateImage` or
`UpdateImage` API request, you can attach the following permission
policy to the role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ecr:BatchGetImage",
 "ecr:GetDownloadUrlForLayer"
 ],
 "Resource": "*"
 }
 ]
}`

```

## CreateNotebookInstance API: Execution Role Permissions

The permissions that you grant to the execution role for calling the
`CreateNotebookInstance` API depend on what you plan to do with the
notebook instance. If you plan to use it to invoke SageMaker AI APIs and pass the same role
when calling the `CreateTrainingJob` and `CreateModel` APIs,
attach the following permissions policy to the role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sagemaker:*",
 "ecr:GetAuthorizationToken",
 "ecr:GetDownloadUrlForLayer",
 "ecr:BatchGetImage",
 "ecr:BatchCheckLayerAvailability",
 "ecr:SetRepositoryPolicy",
 "ecr:CompleteLayerUpload",
 "ecr:BatchDeleteImage",
 "ecr:UploadLayerPart",
 "ecr:DeleteRepositoryPolicy",
 "ecr:InitiateLayerUpload",
 "ecr:DeleteRepository",
 "ecr:PutImage",
 "ecr:CreateRepository",
 "cloudwatch:PutMetricData",
 "cloudwatch:GetMetricData",
 "cloudwatch:GetMetricStatistics",
 "cloudwatch:ListMetrics",
 "logs:CreateLogGroup",
 "logs:CreateLogStream",
 "logs:DescribeLogStreams",
 "logs:PutLogEvents",
 "logs:GetLogEvents",
 "s3:CreateBucket",
 "s3:ListBucket",
 "s3:GetBucketLocation",
 "s3:GetObject",
 "s3:PutObject",
 "s3:DeleteObject",
 "robomaker:CreateSimulationApplication",
 "robomaker:DescribeSimulationApplication",
 "robomaker:DeleteSimulationApplication",
 "robomaker:CreateSimulationJob",
 "robomaker:DescribeSimulationJob",
 "robomaker:CancelSimulationJob",
 "ec2:CreateVpcEndpoint",
 "ec2:DescribeRouteTables",
 "elasticfilesystem:DescribeMountTargets"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "codecommit:GitPull",
 "codecommit:GitPush"
 ],
 "Resource": [
 "arn:aws:codecommit:*:*:*sagemaker*",
 "arn:aws:codecommit:*:*:*SageMaker*",
 "arn:aws:codecommit:*:*:*Sagemaker*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "sagemaker.amazonaws.com"
 }
 }
 }
 ]
}`

```

To tighten the permissions, limit them to specific Amazon S3 and Amazon ECR resources, by
restricting `"Resource": "*"`, as follows:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sagemaker:*",
 "ecr:GetAuthorizationToken",
 "cloudwatch:PutMetricData",
 "logs:CreateLogGroup",
 "logs:CreateLogStream",
 "logs:DescribeLogStreams",
 "logs:PutLogEvents",
 "logs:GetLogEvents"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "sagemaker.amazonaws.com"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::inputbucket"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:PutObject",
 "s3:DeleteObject"
 ],
 "Resource": [
 "arn:aws:s3:::`inputbucket`/`object1`",
 "arn:aws:s3:::`outputbucket`/`path`",
 "arn:aws:s3:::`inputbucket`/`object2`",
 "arn:aws:s3:::`inputbucket`/`object3`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "ecr:BatchCheckLayerAvailability",
 "ecr:GetDownloadUrlForLayer",
 "ecr:BatchGetImage"
 ],
 "Resource": [
 "arn:aws:ecr:`us-east-1`:111122223333:repository/`my-repo1`",
 "arn:aws:ecr:`us-east-1`:111122223333:repository/`my-repo2`",
 "arn:aws:ecr:`us-east-1`:111122223333:repository/`my-repo3`"
 ]
 }
 ]
}`

```

If you plan to access other resources, such as Amazon DynamoDB or Amazon Relational Database Service, add the
relevant permissions to this policy.

In the preceding policy, you scope the policy as follows:

- Scope the `s3:ListBucket` permission to the specific bucket
  that you specify as
  `InputDataConfig.DataSource.S3DataSource.S3Uri` in a
  `CreateTrainingJob` request.
- Scope `s3:GetObject` , `s3:PutObject`, and
  `s3:DeleteObject` permissions as follows:
  - Scope to the following values that you specify in a
    `CreateTrainingJob` request:

  `InputDataConfig.DataSource.S3DataSource.S3Uri`

  `OutputDataConfig.S3OutputPath`
  - Scope to the following values that you specify in a
    `CreateModel` request:

  `PrimaryContainer.ModelDataUrl`

  `SuplementalContainers.ModelDataUrl`

- Scope `ecr` permissions as follows:
  - Scope to the `AlgorithmSpecification.TrainingImage`
    value that you specify in a `CreateTrainingJob`
    request.
  - Scope to the `PrimaryContainer.Image` value that you
    specify in a `CreateModel` request:

The `cloudwatch` and `logs` actions are applicable for "\*"
resources. For more information, see [CloudWatch Resources and Operations](../../../AmazonCloudWatch/latest/monitoring/iam-access-control-overview-cw.md#CloudWatch_ARN_Format "../../../AmazonCloudWatch/latest/monitoring/iam-access-control-overview-cw.md#CloudWatch_ARN_Format") in the Amazon CloudWatch User Guide.

## CreateHyperParameterTuningJob API: Execution Role Permissions

For an execution role that you can pass in a
`CreateHyperParameterTuningJob` API request, you can attach the
following permission policy to the role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "cloudwatch:PutMetricData",
 "logs:CreateLogStream",
 "logs:PutLogEvents",
 "logs:CreateLogGroup",
 "logs:DescribeLogStreams",
 "s3:GetObject",
 "s3:PutObject",
 "s3:ListBucket",
 "ecr:GetAuthorizationToken",
 "ecr:BatchCheckLayerAvailability",
 "ecr:GetDownloadUrlForLayer",
 "ecr:BatchGetImage"
 ],
 "Resource": "*"
 }
 ]
}`

```

Instead of the specifying `"Resource": "*"`, you could scope these
permissions to specific Amazon S3, Amazon ECR, and Amazon CloudWatch Logs resources:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "cloudwatch:PutMetricData",
 "ecr:GetAuthorizationToken"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::`inputbucket`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`inputbucket`/`object`",
 "arn:aws:s3:::`outputbucket`/`path`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "ecr:BatchCheckLayerAvailability",
 "ecr:GetDownloadUrlForLayer",
 "ecr:BatchGetImage"
 ],
 "Resource": "arn:aws:ecr:`us-east-1`:111122223333:repository/`my-repo`"
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogStream",
 "logs:PutLogEvents",
 "logs:CreateLogGroup",
 "logs:DescribeLogStreams"
 ],
 "Resource": "arn:aws:logs:`us-east-1`:111122223333:log-group:/aws/sagemaker/TrainingJobs*"
 }
 ]
}`

```

If the training container associated with the hyperparameter tuning job needs to
access other data sources, such as DynamoDB or Amazon RDS resources, add relevant
permissions to this policy.

In the preceding policy, you scope the policy as follows:

- Scope the `s3:ListBucket` permission to a specific bucket that
  you specify as the
  `InputDataConfig.DataSource.S3DataSource.S3Uri` in a
  `CreateTrainingJob` request.
- Scope the `s3:GetObject` and `s3:PutObject`
  permissions to the following objects that you specify in the input and
  output data configuration in a `CreateHyperParameterTuningJob`
  request:

`InputDataConfig.DataSource.S3DataSource.S3Uri`

`OutputDataConfig.S3OutputPath`

- Scope Amazon ECR permissions to the registry path
  (`AlgorithmSpecification.TrainingImage`) that you specify in
  a `CreateHyperParameterTuningJob` request.
- Scope Amazon CloudWatch Logs permissions to log group of SageMaker training jobs.

The `cloudwatch` actions are applicable for "\*" resources. For more
information, see
[CloudWatch Resources and Operations](../../../AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.md#CWL_ARN_Format "../../../AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.md#CWL_ARN_Format") in the Amazon CloudWatch User Guide.

If you specify a private VPC for your hyperparameter tuning job, add the following
permissions:

```
{
    "Effect": "Allow",
    "Action": [
        "ec2:CreateNetworkInterface",
        "ec2:CreateNetworkInterfacePermission",
        "ec2:DeleteNetworkInterface",
        "ec2:DeleteNetworkInterfacePermission",
        "ec2:DescribeNetworkInterfaces",
        "ec2:DescribeVpcs",
        "ec2:DescribeDhcpOptions",
        "ec2:DescribeSubnets",
        "ec2:DescribeSecurityGroups"
    ]
}
```

If your input is encrypted using server-side encryption with an AWS KMS–managed
key (SSE-KMS), add the following permissions:

```
{
    "Effect": "Allow",
    "Action": [
        "kms:Decrypt"
    ]
}
```

If you specify a KMS key in the output configuration of your hyperparameter tuning
job, add the following permissions:

```
{
    "Effect": "Allow",
    "Action": [
    "kms:Encrypt"
    ]
}
```

If you specify a volume KMS key in the resource configuration of your
hyperparameter tuning job, add the following permissions:

```
{
    "Effect": "Allow",
    "Action": [
    "kms:CreateGrant"
    ]
}
```

## CreateProcessingJob API:

Execution Role Permissions

For an execution role that you can pass in a `CreateProcessingJob` API
request, you can attach the following permission policy to the role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "cloudwatch:PutMetricData",
 "logs:CreateLogStream",
 "logs:PutLogEvents",
 "logs:CreateLogGroup",
 "logs:DescribeLogStreams",
 "s3:GetObject",
 "s3:PutObject",
 "s3:ListBucket",
 "ecr:GetAuthorizationToken",
 "ecr:BatchCheckLayerAvailability",
 "ecr:GetDownloadUrlForLayer",
 "ecr:BatchGetImage"
 ],
 "Resource": "*"
 }
 ]
}`

```

Instead of the specifying `"Resource": "*"`, you could scope these
permissions to specific Amazon S3 and Amazon ECR resources:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "cloudwatch:PutMetricData",
 "logs:CreateLogStream",
 "logs:PutLogEvents",
 "logs:CreateLogGroup",
 "logs:DescribeLogStreams",
 "ecr:GetAuthorizationToken"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::`inputbucket`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`inputbucket`/`object`",
 "arn:aws:s3:::`outputbucket`/`path`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "ecr:BatchCheckLayerAvailability",
 "ecr:GetDownloadUrlForLayer",
 "ecr:BatchGetImage"
 ],
 "Resource": "arn:aws:ecr:`us-east-1`:111122223333:repository/`my-repo`"
 }
 ]
}`

```

If `CreateProcessingJob.AppSpecification.ImageUri` needs to access
other data sources, such as DynamoDB or Amazon RDS resources, add relevant permissions to
this policy.

In the preceding policy, you scope the policy as follows:

- Scope the `s3:ListBucket` permission to a specific bucket that
  you specify as the `ProcessingInputs` in a
  `CreateProcessingJob` request.
- Scope the `s3:GetObject` and `s3:PutObject`
  permissions to the objects that will be downloaded or uploaded in the
  `ProcessingInputs` and `ProcessingOutputConfig` in
  a `CreateProcessingJob` request.
- Scope Amazon ECR permissions to the registry path
  (`AppSpecification.ImageUri`) that you specify in a
  `CreateProcessingJob` request.

The `cloudwatch` and `logs` actions are applicable for "\*"
resources. For more information, see [CloudWatch Resources and Operations](../../../AmazonCloudWatch/latest/monitoring/iam-access-control-overview-cw.md#CloudWatch_ARN_Format "../../../AmazonCloudWatch/latest/monitoring/iam-access-control-overview-cw.md#CloudWatch_ARN_Format") in the Amazon CloudWatch User Guide.

If you specify a private VPC for your processing job, add the following
permissions. Don't scope in the policy with any conditions or resource filters.
Otherwise, the validation checks that occur during the creation of the processing
job fail.

```
{
    "Effect": "Allow",
    "Action": [
        "ec2:CreateNetworkInterface",
        "ec2:CreateNetworkInterfacePermission",
        "ec2:DeleteNetworkInterface",
        "ec2:DeleteNetworkInterfacePermission",
        "ec2:DescribeNetworkInterfaces",
        "ec2:DescribeVpcs",
        "ec2:DescribeDhcpOptions",
        "ec2:DescribeSubnets",
        "ec2:DescribeSecurityGroups"
    ]
}
```

If your input is encrypted using server-side encryption with an AWS KMS–managed
key (SSE-KMS), add the following permissions:

```
{
    "Effect": "Allow",
    "Action": [
        "kms:Decrypt"
    ]
}
```

If you specify a KMS key in the output configuration of your processing job, add
the following permissions:

```
{
    "Effect": "Allow",
    "Action": [
    "kms:Encrypt"
    ]
}
```

If you specify a volume KMS key in the resource configuration of your processing
job, add the following permissions:

```
{
    "Effect": "Allow",
    "Action": [
    "kms:CreateGrant"
    ]
}
```

## CreateTrainingJob API:

Execution Role Permissions

For an execution role that you can pass in a `CreateTrainingJob` API
request, you can attach the following permission policy to the role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "cloudwatch:PutMetricData",
 "logs:CreateLogStream",
 "logs:PutLogEvents",
 "logs:CreateLogGroup",
 "logs:DescribeLogStreams",
 "s3:GetObject",
 "s3:PutObject",
 "s3:ListBucket",
 "ecr:GetAuthorizationToken",
 "ecr:BatchCheckLayerAvailability",
 "ecr:GetDownloadUrlForLayer",
 "ecr:BatchGetImage"
 ],
 "Resource": "*"
 }
 ]
}`

```

Instead of the specifying `"Resource": "*"`, you could scope these
permissions to specific Amazon S3 and Amazon ECR resources:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "cloudwatch:PutMetricData",
 "logs:CreateLogStream",
 "logs:PutLogEvents",
 "logs:CreateLogGroup",
 "logs:DescribeLogStreams",
 "ecr:GetAuthorizationToken"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::`inputbucket`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`inputbucket`/`object`",
 "arn:aws:s3:::`outputbucket`/`path`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "ecr:BatchCheckLayerAvailability",
 "ecr:GetDownloadUrlForLayer",
 "ecr:BatchGetImage"
 ],
 "Resource": "arn:aws:ecr:`us-east-1`:111122223333:repository/`my-repo`"
 }
 ]
}`

```

If `CreateTrainingJob.AlgorithSpecifications.TrainingImage` needs to
access other data sources, such as DynamoDB or Amazon RDS resources, add relevant
permissions to this policy.

In the preceding policy, you scope the policy as follows:

- Scope the `s3:ListBucket` permission to a specific bucket that
  you specify as the
  `InputDataConfig.DataSource.S3DataSource.S3Uri` in a
  `CreateTrainingJob` request.
- Scope the `s3:GetObject` and `s3:PutObject`
  permissions to the following objects that you specify in the input and
  output data configuration in a `CreateTrainingJob`
  request:

`InputDataConfig.DataSource.S3DataSource.S3Uri`

`OutputDataConfig.S3OutputPath`

- Scope Amazon ECR permissions to the registry path
  (`AlgorithmSpecification.TrainingImage`) that you specify in
  a `CreateTrainingJob` request.

The `cloudwatch` and `logs` actions are applicable for "\*"
resources. For more information, see [CloudWatch Resources and Operations](../../../AmazonCloudWatch/latest/monitoring/iam-access-control-overview-cw.md#CloudWatch_ARN_Format "../../../AmazonCloudWatch/latest/monitoring/iam-access-control-overview-cw.md#CloudWatch_ARN_Format") in the Amazon CloudWatch User Guide.

If you specify a private VPC for your training job, add the following
permissions:

```
{
    "Effect": "Allow",
    "Action": [
      "ec2:CreateNetworkInterface",
      "ec2:CreateNetworkInterfacePermission",
      "ec2:DeleteNetworkInterface",
      "ec2:DeleteNetworkInterfacePermission",
      "ec2:DescribeNetworkInterfaces",
      "ec2:DescribeVpcs",
      "ec2:DescribeDhcpOptions",
      "ec2:DescribeSubnets",
      "ec2:DescribeSecurityGroups"
    ]
}
```

If your input is encrypted using server-side encryption with an AWS KMS–managed
key (SSE-KMS), add the following permissions:

```
{
    "Effect": "Allow",
    "Action": [
        "kms:Decrypt"
    ]
}
```

If you specify a KMS key in the output configuration of your training job, add the
following permissions:

```
{
    "Effect": "Allow",
    "Action": [
    "kms:Encrypt"
    ]
}
```

If you specify a volume KMS key in the resource configuration of your training
job, add the following permissions:

```
{
    "Effect": "Allow",
    "Action": [
    "kms:CreateGrant"
    ]
}
```

## CreateModel API: Execution Role

Permissions

For an execution role that you can pass in a `CreateModel` API request,
you can attach the following permission policy to the role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "cloudwatch:PutMetricData",
 "logs:CreateLogStream",
 "logs:PutLogEvents",
 "logs:CreateLogGroup",
 "logs:DescribeLogStreams",
 "s3:GetObject",
 "s3:ListBucket",
 "ecr:GetAuthorizationToken",
 "ecr:BatchCheckLayerAvailability",
 "ecr:GetDownloadUrlForLayer",
 "ecr:BatchGetImage"
 ],
 "Resource": "*"
 }
 ]
}`

```

Instead of the specifying `"Resource": "*"`, you can scope these
permissions to specific Amazon S3 and Amazon ECR resources:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "cloudwatch:PutMetricData",
 "logs:CreateLogStream",
 "logs:PutLogEvents",
 "logs:CreateLogGroup",
 "logs:DescribeLogStreams",
 "ecr:GetAuthorizationToken"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::`inputbucket`/`object`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "ecr:BatchCheckLayerAvailability",
 "ecr:GetDownloadUrlForLayer",
 "ecr:BatchGetImage"
 ],
 "Resource": [
 "arn:aws:ecr:`us-east-1`:111122223333:repository/`my-repo`",
 "arn:aws:ecr:`us-east-1`:111122223333:repository/`my-repo`"
 ]
 }
 ]
}`

```

If `CreateModel.PrimaryContainer.Image` need to access other data
sources, such as Amazon DynamoDB or Amazon RDS resources, add relevant permissions
to this policy.

In the preceding policy, you scope the policy as follows:

- Scope S3 permissions to objects that you specify in the
  `PrimaryContainer.ModelDataUrl` in a [`CreateModel`](../APIReference/API_CreateModel.md "../APIReference/API_CreateModel.md") request.
- Scope Amazon ECR permissions to a specific registry path that you specify as
  the `PrimaryContainer.Image` and
  `SecondaryContainer.Image` in a `CreateModel`
  request.

The `cloudwatch` and `logs` actions are applicable for "\*"
resources. For more information, see [CloudWatch Resources and Operations](../../../AmazonCloudWatch/latest/monitoring/iam-access-control-overview-cw.md#CloudWatch_ARN_Format "../../../AmazonCloudWatch/latest/monitoring/iam-access-control-overview-cw.md#CloudWatch_ARN_Format") in the Amazon CloudWatch User Guide.

###### Note

If you plan to use the [SageMaker AI deployment
guardrails feature](deployment-guardrails.md "deployment-guardrails.md") for model deployment in production, ensure that
your execution role has permission to perform the
`cloudwatch:DescribeAlarms` action on your auto-rollback
alarms.

If you specify a private VPC for your model, add the following permissions:

```
{
    "Effect": "Allow",
    "Action": [
        "ec2:CreateNetworkInterface",
        "ec2:CreateNetworkInterfacePermission",
        "ec2:DeleteNetworkInterface",
        "ec2:DeleteNetworkInterfacePermission",
        "ec2:DescribeNetworkInterfaces",
        "ec2:DescribeVpcs",
        "ec2:DescribeDhcpOptions",
        "ec2:DescribeSubnets",
        "ec2:DescribeSecurityGroups"
    ]
}
```
