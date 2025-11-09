AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/ "https://aws.amazon.com/transform/"), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Identity and access management in App2Container

Your AWS security credentials identify you to AWS and grant you access to your AWS
resources. For example, they can allow you to access artifacts saved to an Amazon S3 bucket. You
can use features of AWS Identity and Access Management (IAM) to allow other users, services, and applications to use
specific resources in your AWS account without sharing your security credentials. You can
choose to allow full use or limited use of your AWS resources.

If you are the owner of the AWS account and use AWS as the root user, we strongly
recommend that you create an IAM admin user to use for access to your AWS resources. See
[Creating Your First IAM Admin User and Group](../../../IAM/latest/UserGuide/getting-started_create-admin-group.md "../../../IAM/latest/UserGuide/getting-started_create-admin-group.md")
in the _IAM User Guide_ to set up your own access before setting up any
other IAM users who need to use App2Container.

By default, IAM users don't have permission to create or modify resources. To allow
IAM users to create or modify resources and perform tasks, you must create IAM policies
that grant permission to use the specific resources and API actions that they need. For more
information about IAM policies, see
[Policies and Permissions](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the
_IAM User Guide_.

IAM groups and roles are a flexible way to manage permissions across multiple users. When you
assign a user to a group or when your user assumes a role, that user inherits the group's or
role's permissions, and is allowed or denied permission to perform the specified tasks on the
specified resources. You can assign multiple users to the same group, and a role can be assumed by
authorized users. While groups and roles both serve the purpose of granting access to resources,
roles are more task-oriented, and assuming a role provides you with temporary security credentials
for your role session.

###### IAM security best practices

Follow these top four security best practices when setting up your IAM resources. For more
information and additional best practices, see
[Security Best Practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the
_IAM User Guide_.

1. ###### Lock away your AWS account root user access keys

Protect your root user access key like you would your credit card numbers or any
other sensitive secret, and only use your root user account for necessary account
and service management tasks. 2. ###### Create individual IAM users

Don't use your AWS account root user credentials to access AWS, and don't give
your credentials to anyone else. Instead, create individual users for anyone who
needs access to your AWS account. 3. ###### Use groups or roles to assign permissions to IAM Users

Instead of defining permissions for individual IAM users, it's usually more
convenient to create groups that relate to job functions (administrators,
developers, accounting, etc.) or roles that relate to specific tasks. 4. ###### Grant least privilege

When you create IAM policies, follow the standard security advice of granting
_least privilege_, or granting only the permissions required
to perform a task. Determine what users (and roles) need to do and then craft
policies that allow them to perform only those tasks.
We recommend that you create a general purpose IAM group that can run all of the commands
_except_ commands that are run with the `--deploy` option.

If you plan to use App2Container to deploy your containers or create pipelines, then you should
create a separate IAM user for deployments. The deployment user needs to be able to create or update
AWS objects for container management services (Amazon ECR, Amazon ECS, Amazon EKS, and App Runner), and to create pipelines
with AWS CodeStar services. This requires elevated permissions that should only be used for deployment.

###### Set up IAM resources for App2Container

- [Create IAM resources for general use](#iam-user-containerize "#iam-user-containerize")
- [Create IAM resources for deployment](#iam-user-deploy "#iam-user-deploy")

## Create IAM resources for general use

Follow best practices by using the following steps to create an IAM group with access
to perform specific tasks, using specific resources, and to assign users to the group.

###### Note

Alternatively, you can create an IAM role and EC2 instance profile to grant permissions
to applications that run on an Amazon EC2 instance. For more information about using instance
profiles, see [Using an IAM role
to grant permissions to applications running on Amazon EC2 instances](../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2.md") in the
_IAM User Guide_.

1. ###### Create a customer managed IAM policy

You can create a customer managed IAM policy for your general purpose user or group, using
one of the [example policies](#example-iam-policies "#example-iam-policies") on this page
after you have customized the JSON to refer to your resources. To create a policy using
the AWS console, see
[Creating
policies on the JSON tab](../../../IAM/latest/UserGuide/access_policies_create-console.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create-console.md#access_policies_create-json-editor") in the _IAM User Guide_.
To create a policy using the AWS CLI, use the
**[create-policy](../../../cli/latest/reference/iam/create-policy.md "../../../cli/latest/reference/iam/create-policy.md")** command.

###### Tip

Review your policy periodically, to add actions required for newer features, and
to ensure that the policy continues to meet your needs. 2. ###### Create IAM users and a group

Every user who will run **app2container** commands needs to have an IAM user
created for accessing AWS resources under your account. To follow best practices, you can
create an IAM group with the policy attached, and assign users to it.

To create an IAM user, see [Creating
an IAM User in Your AWS Account](../../../IAM/latest/UserGuide/id_users_create.md#id_users_create_console "../../../IAM/latest/UserGuide/id_users_create.md#id_users_create_console") in the _IAM User Guide_. Be sure to
select programmatic access to AWS when you create the IAM user.

Perform the following steps to create an IAM group and assign users to it.

    1. To create an IAM group, see
     [Creating IAM Groups](../../../IAM/latest/UserGuide/id_groups_create.md "../../../IAM/latest/UserGuide/id_groups_create.md")
     in the *IAM User Guide*.
    2. Ensure that every person who will run **app2container** commands has
     an IAM user defined for AWS access.
    3. To assign the users to the group that you created in step 1a, see
     [Adding Permissions to a User (Console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console"), or [Adding and Removing a User's Permissions (AWS CLI or AWS
     API)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-programmatic "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-programmatic") in the *IAM User Guide*.

3. ###### Save your AWS access keys

Save the access keys for your new or existing IAM user in a safe place. You'll need them
to [configure your AWS profile](start-intro.md#setup-aws-profile "start-intro.md#setup-aws-profile") as part of getting
set up for App2Container. 4. ###### Attach or assign the policy

Use one of the following methods to assign permissions to your IAM users.

    * ###### Attach the policy to the IAM group


    Attach the policy that you created in step 1 to the group that you
     created in step 2. See [Attaching a Policy to an IAM Group](../../../IAM/latest/UserGuide/id_groups_manage_attach-policy.md "../../../IAM/latest/UserGuide/id_groups_manage_attach-policy.md") in the
     *IAM User Guide*.
    * ###### Embed the policy inline for an IAM user


    Embed the policy that you created in step 1 inline for your IAM
     user. See the section that begins with "To embed an inline policy"
     in [Adding Permissions to a User (Console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console"), or [Adding and Removing a User's Permissions (AWS CLI or AWS
     API)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-programmatic "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-programmatic") in the
     *IAM User Guide*.

### Example IAM policies

You can use one of the policy templates in this section as a starting point to
configure the access that App2Container uses on your behalf to generate the deployment
artifacts for your application containers.

###### Choose the policy resources and actions that you need

The following sections in the example policies depend on choices
you've made for your containerization environment and workflow:

- ###### AWS CodeCommit

**SectionForCodeCommitAccess** – If you use
App2Container to generate a container pipeline, you must grant access to interact with your
CodeCommit code repository.

- ###### FireLens log routing to Amazon Data Firehose

`SectionForFirelensFirehoseIAMPolicyAccess`,
`SectionForFirelensFirehoseIAMRoleAccess`, and
`SectionForFirelensFirehoseStreamsAccess` –
If you use FireLens for log file routing, and you configure FireLens to route to
Firehose, you must grant access for App2Container to create a new Firehose delivery stream.
You must also grant access for App2Container to create an IAM policy and role so that
FireLens can access the delivery stream.

- ###### FireLens log routing to Amazon Kinesis Data Streams

`SectionForFirelensKinesisStreamsAccess` – if you use
FireLens for log file routing, and you configure FireLens to route to Kinesis Data Streams
you must grant access for App2Container to create a new Kinesis data stream.

- ###### AWS Secrets Manager

`SectionForSecretManagerAccess` – If you configured
your environment to run remote workflows, App2Container requires you to use Secrets Manager for
connection secrets to access application servers from the worker machine. You must
grant access to retrieve secrets in the policy.

- ###### Amazon S3

`SectionForS3Access` and `SectionForS3ReadAccess`
– If you set up an S3 bucket for application or deployment artifacts,
you must grant access to your bucket in the policy.

You must also ensure that only authorized users can access the bucket. We recommend
that you use server-side encryption for your bucket. See
[Protecting data using server-side
encryption](../../../AmazonS3/latest/userguide/serv-side-encryption.md "../../../AmazonS3/latest/userguide/serv-side-encryption.md") in the _Amazon Simple Storage Service User Guide_ for more
information about how to set it up.

- ###### Upload support bundle

`SectionForUploadSupportBundleService` – If you chose to
have App2Container logs and command-generated artifacts uploaded automatically for
failed commands when you ran the **init** command, you must
grant access to upload the application support bundles.

- ###### Usage metrics

`SectionForMetricsService` – If you gave consent for
App2Container to collect and export application usage metrics when you ran the
**init** command, you must grant access to upload the metric data.

- ###### Amazon VPC

`SectionForByoVPC` – If you specify your own VPC or want
to reuse an existing VPC that App2Container created for a prior deployment, you must
grant access to associated describe actions in the policy.

Other policy sections in the examples are required for App2Container to generate application
deployment artifacts, or to integrate with Jenkins pipelines.

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "SectionForS3Access",
            "Action": [
                "s3:DeleteObject",
                "s3:GetBucketAcl",
                "s3:GetBucketLocation",
                "s3:GetObject",
                "s3:GetObjectAcl",
                "s3:ListAllMyBuckets",
                "s3:ListBucket",
                "s3:PutObject",
                "s3:PutObjectAcl"
            ],
            "Effect": "Allow",
            "Resource": "amzn-s3-demo-bucket-ARN"
        },
        {
            "Sid": "SectionForS3ReadAccess",
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:GetBucketAcl"
            ],
            "Resource": "arn:aws:s3:::*"
        },
        {
            "Sid": "SectionForECRAccess",
            "Action": [
                "ecr:BatchCheckLayerAvailability",
                "ecr:BatchDeleteImage",
                "ecr:BatchGetImage",
                "ecr:CompleteLayerUpload",
                "ecr:CreateRepository",
                "ecr:DeleteRepository",
                "ecr:DescribeImages",
                "ecr:DescribeRepositories",
                "ecr:GetAuthorizationToken",
                "ecr:GetDownloadUrlForLayer",
                "ecr:GetRepositoryPolicy",
                "ecr:InitiateLayerUpload",
                "ecr:ListImages",
                "ecr:PutImage",
                "ecr:TagResource",
                "ecr:UntagResource",
                "ecr:UploadLayerPart"
            ],
            "Effect": "Allow",
            "Resource": "resource-ARNs"
        },
        {
            "Sid": "SectionForECRAccess2",
            "Action": [
                "ecr:GetAuthorizationToken"
            ],
            "Effect": "Allow",
            "Resource": "*"
        },
        {
            "Sid": "SectionForECSWriteAccess",
            "Action": [
                "ecs:CreateCluster",
                "ecs:CreateService",
                "ecs:CreateTaskSet",
                "ecs:DeleteCluster",
                "ecs:DeleteService",
                "ecs:DeleteTaskSet",
                "ecs:DeregisterTaskDefinition",
                "ecs:Poll",
                "ecs:RegisterContainerInstance",
                "ecs:RegisterTaskDefinition",
                "ecs:RunTask",
                "ecs:StartTask",
                "ecs:StopTask",
                "ecs:SubmitContainerStateChange",
                "ecs:SubmitTaskStateChange",
                "ecs:UpdateContainerInstancesState",
                "ecs:UpdateService",
                "ecs:UpdateServicePrimaryTaskSet",
                "ecs:UpdateTaskSet"
            ],
            "Effect": "Allow",
            "Resource": "resource-ARNs"
        },
        {
            "Sid": "SectionForPassRoleToECS",
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "ARN for ecsTaskExecutionRole"
        },
        {
            "Sid": "SectionForECSReadAccess",
            "Action": [
                "ecs:DescribeClusters",
                "ecs:DescribeContainerInstances",
                "ecs:DescribeServices",
                "ecs:DescribeTaskDefinition",
                "ecs:DescribeTaskSets",
                "ecs:DescribeTasks",
                "ecs:ListClusters",
                "ecs:ListContainerInstances",
                "ecs:ListServices",
                "ecs:ListTaskDefinitionFamilies",
                "ecs:ListTaskDefinitions",
                "ecs:ListTasks"
            ],
            "Effect": "Allow",
            "Resource": "resource-ARNs"
        },
        {
            "Sid": "SectionForFirelensIAMRoleAccess",
            "Action": [
                "iam:CreateRole",
                "iam:GetRole",
                "iam:AttachRolePolicy"
            ],
            "Effect": "Allow",
            "Resource": "arn:aws:iam::your account ID:role/A2CEcsFirelensRole"
        },
        {
            "Sid": "SectionForFirelensIAMPolicyAccess",
            "Action": [
                "iam:CreatePolicy"
            ],
            "Effect": "Allow",
            "Resource": "arn:aws:iam::your account ID:policy/service-role/A2CEcsFirelensPolicy"
        },
        {
            "Sid": "SectionForFirelensFirehoseIAMPolicyAccess",
            "Action": [
                "iam:CreatePolicy",
                "iam:GetPolicy"
            ],
            "Effect": "Allow",
            "Resource": "arn:aws:iam::your account ID:policy/*a2c-KinesisFirehosePolicy-*"
        },
        {
            "Sid": "SectionForFirelensFirehoseIAMRoleAccess",
            "Action": [
                "iam:CreateRole",
                "iam:GetRole",
                "iam:AttachRolePolicy"
            ],
            "Effect": "Allow",
            "Resource": "arn:aws:iam::your account ID:role/*a2c-FirehoseRole-*"
        },
        {
            "Sid": "SectionForFirelensFirehoseStreamsAccess",
            "Action": [
                "firehose:DescribeDeliveryStream",
                "firehose:CreateDeliveryStream"
            ],
            "Effect": "Allow",
            "Resource": "arn:aws:firehose:*:your account ID:deliverystream/*"
        },
        {
            "Sid": "SectionForFirelensKinesisStreamsAccess",
            "Action": [
                "kinesis:CreateStream"
            ],
            "Effect": "Allow",
            "Resource": "arn:aws:kinesis:*:your account ID:stream/*"
        },
        {
            "Sid": "SectionForCodeCommitAccess",
            "Effect": "Allow",
            "Action": [
                "codecommit:GetRepository",
                "codecommit:GetBranch",
                "codecommit:CreateRepository",
                "codecommit:CreateCommit",
                "codecommit:TagResource"
            ],
            "Resource": "arn:aws:codecommit:*:*:*"
        },
        {
            "Sid": "SectionForByoVPC",
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeInternetGateways",
                "ec2:DescribeRouteTables",
                "ec2:DescribeSubnets",
                "ec2:DescribeVpcs"
            ],
            "Resource": "resource-ARNs"
        },
        {
          "Sid": "SectionForEC2",
          "Effect": "Allow",
          "Action": [
             "ec2:DescribeKeyPairs",
             "ec2:CreateKeyPair",
             "ec2:DescribeAvailabilityZones"
          ],
          "Resource": "resource-ARNs"
        },
        {
            "Sid": "SectionForMetricsService",
            "Effect": "Allow",
            "Action": "application-transformation:PutMetricData",
            "Resource": "*"
        },
        {
            "Sid": "SectionForUploadSupportBundleService",
            "Effect": "Allow",
            "Action": "application-transformation:PutLogData",
            "Resource": "*"
        },
        {
            "Sid": "SectionForSecretManagerAccess",
            "Action": [
                "secretsmanager:GetSecretValue",
                "secretsmanager:DescribeSecret"
            ],
            "Effect": "Allow",
            "Resource": "arn:aws:secretsmanager:your region:your account ID:secret:a2c/*"
        },
        {
            "Sid": "SectionForCloudFormation",
            "Action": [
                "cloudformation:DescribeStacks"
            ],
            "Effect": "Allow",
            "Resource": "arn:aws:cloudformation:*:your account ID:stack/a2c-*"
        }
    ]
}

```

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "SectionForS3Access",
            "Action": [
                "s3:DeleteObject",
                "s3:GetBucketAcl",
                "s3:GetBucketLocation",
                "s3:GetObject",
                "s3:GetObjectAcl",
                "s3:ListAllMyBuckets",
                "s3:ListBucket",
                "s3:PutObject",
                "s3:PutObjectAcl"
            ],
            "Effect": "Allow",
            "Resource": "amzn-s3-demo-bucket-ARN"
        },
        {
            "Sid": "SectionForS3ReadAccess",
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:GetBucketAcl"
            ],
            "Resource": "arn:aws:s3:::*"
        },
        {
            "Sid": "SectionForECRAccess",
            "Action": [
                "ecr:BatchCheckLayerAvailability",
                "ecr:BatchDeleteImage",
                "ecr:BatchGetImage",
                "ecr:CompleteLayerUpload",
                "ecr:CreateRepository",
                "ecr:DeleteRepository",
                "ecr:DescribeImages",
                "ecr:DescribeRepositories",
                "ecr:GetDownloadUrlForLayer",
                "ecr:GetRepositoryPolicy",
                "ecr:InitiateLayerUpload",
                "ecr:ListImages",
                "ecr:PutImage",
                "ecr:TagResource",
                "ecr:UntagResource",
                "ecr:UploadLayerPart"
            ],
            "Effect": "Allow",
            "Resource": "resource-ARNs"
        },
        {
            "Sid": "SectionForECRAccess2",
            "Action": [
                "ecr:GetAuthorizationToken"
            ],
            "Effect": "Allow",
            "Resource": "*"
        },
        {
            "Sid": "SectionForEKS",
            "Effect": "Allow",
            "Action": [
                "iam:GetRole",
                "lambda:GetFunction"
            ],
            "Resource": [
                "arn:aws:iam::*:role/eks-quickstart-ResourceReader",
                "arn:aws:lambda:target Region:*:function:eks-quickstart-ResourceReader"
            ]
        },
        {
            "Sid": "SectionForCodeCommitAccess",
            "Effect": "Allow",
            "Action": [
                "codecommit:GetRepository",
                "codecommit:GetBranch",
                "codecommit:CreateRepository",
                "codecommit:CreateCommit",
                "codecommit:TagResource"
            ],
            "Resource": "arn:aws:codecommit:*:*:*"
        },
        {
            "Sid": "SectionForByoVPC",
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeInternetGateways",
                "ec2:DescribeRouteTables",
                "ec2:DescribeSubnets",
                "ec2:DescribeVpcs"
            ],
            "Resource": "resource-ARNs"
        },
        {
          "Sid": "SectionForEC2",
          "Effect": "Allow",
          "Action": [
             "ec2:DescribeKeyPairs",
             "ec2:CreateKeyPair",
             "ec2:DescribeAvailabilityZones"
          ],
          "Resource": "resource-ARNs"
        },
        {
            "Sid": "SectionForMetricsService",
            "Effect": "Allow",
            "Action": "application-transformation:PutMetricData",
            "Resource": "*"
        },
        {
            "Sid": "SectionForUploadSupportBundleService",
            "Effect": "Allow",
            "Action": "application-transformation:PutLogData",
            "Resource": "*"
        },
        {
            "Sid": "SectionForSecretManagerAccess",
            "Action": [
                "secretsmanager:GetSecretValue",
                "secretsmanager:DescribeSecret"
            ],
            "Effect": "Allow",
            "Resource": "arn:aws:secretsmanager:your region:your account ID:secret:a2c/*"
        },
        {
			"Sid": "SectionForIAMAccess",
			"Action": [
				"iam:AttachRolePolicy",
				"iam:CreateRole",
				"iam:GetRole",
				"iam:ListRoles (https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListRoles.html)",
				"iam:ListRoleTags (https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListRoleTags.html)"
			],
			"Effect": "Allow",
			"Resource": "resource-ARNs"
    	},
        {
            "Sid": "SectionForCloudFormation",
            "Action": [
                "cloudformation:DescribeStacks"
            ],
            "Effect": "Allow",
            "Resource": "arn:aws:cloudformation:*:your account ID:stack/a2c-*"
        }
    ]
}

```

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "SectionForAppRunnerAccess",
            "Action": [
                "apprunner:List*",
                "apprunner:Describe*"
            ],
            "Effect": "Allow",
            "Resource": "resource-ARNs"
        },
        {
            "Sid": "SectionForECRAccess",
            "Action": [
                "ecr:BatchCheckLayerAvailability",
                "ecr:BatchDeleteImage",
                "ecr:BatchGetImage",
                "ecr:CompleteLayerUpload",
                "ecr:CreateRepository",
                "ecr:DeleteRepository",
                "ecr:DescribeImages",
                "ecr:DescribeRepositories",
                "ecr:GetDownloadUrlForLayer",
                "ecr:GetRepositoryPolicy",
                "ecr:InitiateLayerUpload",
                "ecr:ListImages",
                "ecr:PutImage",
                "ecr:TagResource",
                "ecr:UntagResource",
                "ecr:UploadLayerPart"
            ],
            "Effect": "Allow",
            "Resource": "resource-ARNs"
        },
        {
            "Sid": "SectionForECRAccess2",
            "Action": [
                "ecr:GetAuthorizationToken"
            ],
            "Effect": "Allow",
            "Resource": "*"
        },
        {
            "Sid": "SectionForCodeCommitAccess",
            "Effect": "Allow",
            "Action": [
                "codecommit:GetRepository",
                "codecommit:GetBranch",
                "codecommit:CreateRepository",
                "codecommit:CreateCommit",
                "codecommit:TagResource"
            ],
            "Resource": "arn:aws:codecommit:*:*:*"
        },
        {
            "Sid": "SectionForMetricsService",
            "Effect": "Allow",
            "Action": "application-transformation:PutMetricData",
            "Resource": "*"
        },
        {
            "Sid": "SectionForUploadSupportBundleService",
            "Effect": "Allow",
            "Action": "application-transformation:PutLogData",
            "Resource": "*"
        },
        {
            "Sid": "SectionForSecretManagerAccess",
            "Action": [
                "secretsmanager:GetSecretValue",
                "secretsmanager:DescribeSecret"
            ],
            "Effect": "Allow",
            "Resource": "arn:aws:secretsmanager:us-east-1:*:secret:a2c/*"
        },
        {
            "Sid": "SectionForCloudFormation",
            "Action": [
                "cloudformation:DescribeStacks"
            ],
            "Effect": "Allow",
            "Resource": "arn:aws:cloudformation:*:your account ID:stack/a2c-*"
        }
    ]
}

```

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AzureDevOpsAWS",
            "Effect": "Allow",
            "Action": [
                "ecr:DescribeRepositories",
                "ecr:GetAuthorizationToken",
                "ecr:UploadLayerPart",
                "ecr:PutImage",
                "ecr:CompleteLayerUpload",
                "ecr:InitiateLayerUpload",
                "ecr:BatchCheckLayerAvailability",
                "ecr:BatchGetImage",
                "ecr:GetDownloadUrlForLayer",
                "ecs:UpdateService",
                "eks:DescribeCluster"
            ],
            "Resource": "*"
        }
    ]
}

```

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "JenkinsAWS",
            "Effect": "Allow",
            "Action": [
                "ecr:GetDownloadUrlForLayer",
                "iam:ListRoles",
                "ecr:GetAuthorizationToken",
                "ecr:UploadLayerPart",
                "ecr:PutImage",
                "ecs:UpdateService",
                "sts:AssumeRole",
                "ecr:BatchGetImage",
                "ecr:CompleteLayerUpload",
                "eks:DescribeCluster",
                "ecr:InitiateLayerUpload",
                "ecr:BatchCheckLayerAvailability"
            ],
            "Resource": "*"
        }
    ]
}

```

## Create IAM resources for deployment

The **AdministratorAccess** policy grants an IAM user full access
to AWS. Therefore, IAM users with this policy can deploy a containerized application
using any of the AWS services for deployment that are supported by App2Container.

1. ###### Create an IAM user

You can create an IAM user with full access to AWS API actions and resources.
Be sure to grant the user programmatic access to AWS and to attach the
**AdministratorAccess** policy. For more information, see
[Creating
IAM users](../../../IAM/latest/UserGuide/id_users_create.md#id_users_create_console "../../../IAM/latest/UserGuide/id_users_create.md#id_users_create_console") in the _IAM User Guide_. 2. ###### Save your AWS access keys

Save the access keys for the IAM user in a safe place. You'll need them
to [configure your AWS profile](start-intro.md#setup-aws-profile "start-intro.md#setup-aws-profile") as part of
getting set up for App2Container.
