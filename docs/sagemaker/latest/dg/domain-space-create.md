# Create a shared space

###### Important

Custom IAM policies that allow Amazon SageMaker Studio or Amazon SageMaker Studio Classic to create Amazon SageMaker
resources must also grant permissions to add tags to those resources. The permission to
add tags to resources is required because Studio and Studio Classic automatically tag
any resources they create. If an IAM policy allows Studio and Studio Classic to
create resources but does not allow tagging, "AccessDenied" errors can occur when
trying to create resources. For more information, see [Provide permissions for tagging SageMaker AI
resources](security_iam_id-based-policy-examples.md#grant-tagging-permissions "security_iam_id-based-policy-examples.md#grant-tagging-permissions").

[AWS managed policies for Amazon SageMaker AI](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
that give permissions to create SageMaker resources already include permissions to add tags
while creating those resources.

The following topic demonstrates how to create a shared space in an existing
Amazon SageMaker AI domain. If you created your domain without support for shared spaces, you must add support
for shared spaces to your existing domain before you can create a shared space.

###### Topics

- [Add shared space support to an existing domain](#domain-space-add "#domain-space-add")
- [Create a shared space](#domain-space-create-app "#domain-space-create-app")

## Add shared space support to an existing domain

You can use the SageMaker AI console or the AWS CLI to add support for shared spaces to an existing
domain. If the domain is using `VPC only` network access, then you can only add shared space support using the AWS CLI.

### Console

Complete the following procedure to add support for Studio Classic shared spaces to an existing domain from
the SageMaker AI console.

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the left navigation pane, choose **Admin configurations**.
3. Under **Admin configurations**, choose **domains**.
4. From the list of domains, select the domain that you want to open the
   **domain settings** page for.
5. On the **domain details** page, choose the **domain
   settings** tab.
6. Choose **Edit**.
7. For **Space default execution role**, set an IAM role that is used by
   default for all shared spaces created in the domain.
8. Choose **Next**.
9. Choose **Next**.
10. Choose **Next**.
11. Choose **Submit**.

### AWS CLI

Studio Classic
Run the following command from the terminal of your local machine to add default shared space
settings to a domain from the AWS CLI. If you are adding default shared space settings to a
domain within an Amazon VPC, you must also include a list of security groups. Studio Classic shared spaces only
support the use of JupyterLab 3 image ARNs. For more information, see [JupyterLab Versioning in Amazon SageMaker Studio Classic](studio-jl.md "studio-jl.md").

```
# Public Internet domain
aws --region `region` \
sagemaker update-domain \
--domain-id `domain-id` \
--default-space-settings "ExecutionRole=`execution-role-arn`,JupyterServerAppSettings={DefaultResourceSpec={InstanceType=`example-instance-type`,SageMakerImageArn=`sagemaker-image-arn`}}"

# VPCOnly domain
aws --region `region` \
sagemaker update-domain \
--domain-id `domain-id` \
--default-space-settings "ExecutionRole=`execution-role-arn`,JupyterServerAppSettings={DefaultResourceSpec={InstanceType=system,SageMakerImageArn=`sagemaker-image-arn`}},SecurityGroups=[`security-groups`]"

```

Use the following command to verify that the default shared space settings have been updated.

```

aws --region `region` \
sagemaker describe-domain \
--domain-id `domain-id`

```

JupyterLab
Run the following command from the terminal of your local machine to add default shared space
settings to a domain from the AWS CLI. If you are adding default shared space settings to a
domain within an Amazon VPC, you must also include a list of security groups. Studio Classic shared spaces only
support the use of JupyterLab 4 image ARNs. For more information, see [JupyterLab Versioning in Amazon SageMaker Studio Classic](studio-jl.md "studio-jl.md").

```
# Public Internet domain
aws --region `region` \
sagemaker update-domain \
--domain-id `domain-id` \
--default-space-settings "ExecutionRole=`execution-role-arn`", JupyterLabAppSettings={DefaultResourceSpec={InstanceType=`example-instance-type`,SageMakerImageArn=`sagemaker-image-arn`}}"

# VPCOnly domain
aws --region `region` \
sagemaker update-domain \
--domain-id `domain-id` \
--default-space-settings "ExecutionRole=`execution-role-arn`, SecurityGroups=[`security-groups`]"

```

Use the following command to verify that the default shared space settings have been updated.

```

aws --region `region` \
sagemaker describe-domain \
--domain-id `domain-id`

```

## Create a shared space

The following sections demonstrate how to create a shared space from the Amazon SageMaker AI console, Amazon SageMaker Studio, or the
AWS CLI.

Use the following procedures to create a shared space in a domain from Studio.

Studio Classic

1. Navigate to Studio following the steps in [Launch Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").
2. From the Studio UI, find the applications pane on the left side.
3. From the applications pane, select **Studio Classic**.
4. Choose **Create Studio Classic space**
5. In the pop up window, enter a name for the space.
6. Choose **Create space**.

JupyterLab

1. Navigate to Studio following the steps in [Launch Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").
2. From the Studio UI, find the applications pane on the left side.
3. From the applications pane, select **JupyterLab**.
4. Choose **Create JupyterLab space**
5. In the pop up window, enter a name for the space.
6. Choose **Create space**.

Complete the following procedure to create a shared space in a domain from the SageMaker AI console.

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the left navigation pane, choose **Admin configurations**.
3. Under **Admin configurations**, choose **domains**.
4. From the list of domains, select the domain that you want to create a shared space for.
5. On the **domain details** page, choose the **Space
   management** tab.
6. Choose **Create**.
7. Enter a name for your shared space. shared space names within a domain must be unique. The
   execution role for the shared space is set to the domain IAM execution role.
   This section shows how to create a shared space from the AWS CLI.

You cannot set the execution role of a shared space when creating or updating it.
The `DefaultDomainExecRole` can only be set when creating or updating the
domain. shared spaces only support the use of JupyterLab 3 image ARNs. For more information, see
[JupyterLab Versioning in Amazon SageMaker Studio Classic](studio-jl.md "studio-jl.md").

To create a shared space from the AWS CLI, run one of the following commands from the terminal of your
local machine.

Studio Classic

```

aws --region `region` \
sagemaker create-space \
--domain-id `domain-id` \
--space-name `space-name` \
--space-settings '{
  "JupyterServerAppSettings": {
    "DefaultResourceSpec": {
      "SageMakerImageArn": "`sagemaker-image-arn`",
      "InstanceType": "system"
    }
  }
}'

```

JupyterLab

```

aws --region `region` \
sagemaker create-space \
--domain-id `domain-id` \
--space-name `space-name` \
--ownership-settings "{\"OwnerUserProfileName\": \"`user-profile-name`\"}" \
--space-sharing-settings "{\"SharingType\": \"Shared\"}" \
--space-settings "{\"AppType\": \"JupyterLab\"}"


```
