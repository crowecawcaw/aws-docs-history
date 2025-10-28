# Attach a custom SageMaker image

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

This guide shows how to attach a custom RStudio image to your Amazon SageMaker AI domain using the SageMaker AI
console or the AWS Command Line Interface (AWS CLI).

To use a custom SageMaker image, you must attach a custom RStudio image to your domain.
When you attach an image version, it appears in the RStudio Launcher and is available in the
**Select image** dropdown list. You use the dropdown to change the
image used by RStudio.

There is a limit to the number of image versions that you can attach. After you reach the
limit, you must first detach a version so that you can attach a different version of the
image.

###### Topics

- [Attach an image version to your domain
  using the console](#rstudio-byoi-attach-console "#rstudio-byoi-attach-console")
- [Attach an existing image version to your
  domain using the AWS CLI](#rstudio-byoi-attach-cli "#rstudio-byoi-attach-cli")

## Attach an image version to your domain

using the console

You can attach a custom SageMaker image version to your domain using the SageMaker AI console's
control panel. You can also create a custom SageMaker image, and an image version, and then
attach that version to your domain.

###### To attach an existing image

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the left navigation pane, choose **Admin configurations**.
3. Under **Admin configurations**, choose **domains**.
4. Select the desired domain.
5. Choose **Environment**.
6. Under **Custom SageMaker Studio Classic images attached to domain**,
   choose **Attach image**.
7. For **Image source**, choose **Existing
   image** or **New image**.

If you select **Existing image**, choose an image
from the Amazon SageMaker image store.

If you select **New image**, provide the Amazon ECR
registry path for your Docker image. The path must be in the same AWS Region
as the domain. The Amazon ECR repo must be in the same account as your
domain, or cross-account permissions for SageMaker AI must be enabled. 8. Choose an existing image from the list. 9. Choose a version of the image from the list. 10. Choose **Next**. 11. Enter values for **Image name**, **Image display
name**, and **Description**. 12. Choose the IAM role. For more information, see
[Create a custom RStudio image](rstudio-byoi-create.md "rstudio-byoi-create.md"). 13. (Optional) Add tags for the image. 14. (Optional) Choose **Add new tag**, then add a configuration
tag. 15. For **Image type**, select **RStudio
Image**. 16. Choose **Submit**.

Wait for the image version to be attached to the domain. After the version is
attached, it appears in the **Custom images** list and is briefly
highlighted.

## Attach an existing image version to your

domain using the AWS CLI

Two methods are presented to attach the image version to your domain using the
AWS CLI. In the first method, you create a new domain with the version attached. This
method is simpler but you must specify the Amazon Virtual Private Cloud (Amazon VPC) information and execution
role that's required to create the domain.

If you have already onboarded to the domain, you can use the second method to
attach the image version to your current domain. In this case, you don't need to
specify the Amazon VPC information and execution role. After you attach the version, delete
all of the applications in your domain and relaunch RStudio.

### Attach the SageMaker image to a new

domain

To use this method, you must specify an execution role that has the [AmazonSageMakerFullAccess](https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AmazonSageMakerFullAccess "https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AmazonSageMakerFullAccess") policy attached.

Use the following steps to create the domain and attach the custom SageMaker AI
image:

- Get your default VPC ID and subnet IDs.
- Create the configuration file for the domain, which specifies the image.
- Create the domain with the configuration file.

###### To add the custom SageMaker image to your domain

1. Get your default VPC ID.

```
aws ec2 describe-vpcs \
    --filters Name=isDefault,Values=true \
    --query "Vpcs[0].VpcId" --output text
```

Response:

```
vpc-xxxxxxxx
```

2. Get your default subnet IDs using the VPC ID from the previous step.

```
aws ec2 describe-subnets \
    --filters Name=vpc-id,Values=`<vpc-id>` \
    --query "Subnets[*].SubnetId" --output json
```

Response:

```
[
    "subnet-b55171dd",
    "subnet-8a5f99c6",
    "subnet-e88d1392"
]
```

3. Create a configuration file named
   `create-domain-input.json`. Insert the VPC ID, subnet
   IDs, `ImageName`, and `AppImageConfigName` from the
   previous steps. Because `ImageVersionNumber` isn't specified, the
   latest version of the image is used, which is the only version in this case.
   Your execution role must satisfy the requirements in [Complete prerequisites](rstudio-byoi-prerequisites.md "rstudio-byoi-prerequisites.md").

```
{
  "DomainName": "domain-with-custom-r-image",
  "VpcId": "`<vpc-id>`",
  "SubnetIds": [
    "`<subnet-ids>`"
  ],
  "DomainSettings": {
    "RStudioServerProDomainSettings": {
      "DomainExecutionRoleArn": "`<execution-role>`"
    }
  },
  "DefaultUserSettings": {
    "ExecutionRole": "`<execution-role>`",
    "RSessionAppSettings": {
      "CustomImages": [
        {
         "AppImageConfigName": "rstudio-custom-config",
         "ImageName": "rstudio-custom-image"
        }
      ]
     }
  },
  "AuthMode": "IAM"
}
```

4. Create the domain with the attached custom SageMaker image.

```
aws sagemaker create-domain \
    --cli-input-json file://create-domain-input.json
```

Response:

```
{
    "DomainArn": "arn:aws:sagemaker:`region`:acct-id:domain/`domain-id`",
    "Url": "https://`domain-id`.studio.`region`.sagemaker.aws/..."
}
```

### Attach the SageMaker image to an

existing domain

This method assumes that you've already onboarded to domain. For more information,
see [Amazon SageMaker AI domain overview](gs-studio-onboard.md "gs-studio-onboard.md").

###### Note

You must delete all of the applications in your domain to update the
domain with the new image version. For information about deleting these
applications, see [Delete an Amazon SageMaker AI domain](gs-studio-delete-domain.md "gs-studio-delete-domain.md").

Use the following steps to add the SageMaker image to your current domain.

- Get your `DomainID` from the SageMaker AI console.
- Use the `DomainID` to get the `DefaultUserSettings` for the
  domain.
- Add the `ImageName` and `AppImageConfig` as a `CustomImage` to the
  `DefaultUserSettings`.
- Update your domain to include the custom image.

###### To add the custom SageMaker image to your domain

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the left navigation pane, choose **Admin configurations**.
3. Under **Admin configurations**, choose **domains**.
4. Select the desired domain.
5. Choose **domain settings**.
6. Under **General Settings**, find the **domain
   ID**. The ID is in the following format:
   `d-xxxxxxxxxxxx`.
7. Use the domain ID to get the description of the domain.

```
aws sagemaker describe-domain \
    --domain-id `<d-xxxxxxxxxxxx>`
```

Response:

```
{
    "DomainId": "`d-xxxxxxxxxxxx`",
    "DefaultUserSettings": {
      "KernelGatewayAppSettings": {
        "CustomImages": [
        ],
        ...
      }
    }
}
```

8. Save the `DefaultUserSettings` section of the response to a file named
   `update-domain-input.json`.
9. Insert the `ImageName` and `AppImageConfigName` from the previous steps as
   a custom image. Because `ImageVersionNumber` isn't specified, the latest version of the
   image is used, which is the only version in this case.

```
{
    "DefaultUserSettings": {
        "RSessionAppSettings": {
           "CustomImages": [
              {
                 "ImageName": "rstudio-custom-image",
                 "AppImageConfigName": "rstudio-custom-config"
              }
           ]
        }
    }
}
```

10. Use the domain ID and default user settings file to update your
    domain.

```
aws sagemaker update-domain \
    --domain-id `<d-xxxxxxxxxxxx>` \
    --cli-input-json file://update-domain-input.json
```

Response:

```
{
    "DomainArn": "arn:aws:sagemaker:`region`:acct-id:domain/`domain-id`"
}
```

11. Delete the `RStudioServerPro` application. You must restart the
    `RStudioServerPro` domain-shared application for the RStudio
    Launcher UI to pick up the latest changes.

```
aws sagemaker delete-app \
    --domain-id `<d-xxxxxxxxxxxx>` --user-profile-name domain-shared \
    --app-type RStudioServerPro --app-name default
```

12. Create a new `RStudioServerPro` application. You must create this
    application using the AWS CLI.

```
aws sagemaker create-app \
    --domain-id `<d-xxxxxxxxxxxx>` --user-profile-name domain-shared \
    --app-type RStudioServerPro --app-name default
```
