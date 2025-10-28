# Attach a Custom SageMaker Image in Amazon SageMaker Studio Classic

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

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For
information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md").

Studio Classic is still maintained for existing
workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic
applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md "studio-updated-migrate.md").

To use a custom SageMaker image, you must attach a version of the image to your domain or shared
space. When you attach an image version, it appears in the SageMaker Studio Classic Launcher and is
available in the **Select image** dropdown list, which users use to launch an
activity or change the image used by a notebook.

To make a custom SageMaker image available to all users within a domain, you attach the image to
the domain. To make an image available to all users within a shared space, you can attach the
image to the shared space. To make an image available to a single user, you attach the image to
the user's profile. When you attach an image, SageMaker AI uses the latest image version by default. You
can also attach a specific image version. After you attach the version, you can choose the
version from the SageMaker AI Launcher or the image selector when you launch a notebook.

There is a limit to the number of image versions that can be attached at any given time. After you
reach the limit, you must detach a version in order to attach another version of the image.

The following sections demonstrate how to attach a custom SageMaker image to your domain using
either the SageMaker AI console or the AWS CLI. You can only attach a custom image to a share space using
the AWS CLI.

## Attach the SageMaker image to a domain

### Attach the SageMaker image using the Console

This topic describes how you can attach an existing custom SageMaker image version to your
domain using the SageMaker AI control panel. You can also create a custom SageMaker image and image
version, and then attach that version to your domain. For the procedure to create an image and
image version, see [Create a Custom SageMaker Image for Amazon SageMaker Studio Classic](studio-byoi-create.md "studio-byoi-create.md").

###### To attach an existing image

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the left navigation pane, choose **Admin configurations**.
3. Under **Admin configurations**, choose **domains**.
4. From the **Domains** page, select the domain to attach the image
   to.
5. From the **Domain details** page, select the
   **Environment** tab.
6. On the **Environment** tab, under **Custom SageMaker Studio Classic
   images attached to domain**, choose **Attach image**.
7. For **Image source**, choose **Existing image**.
8. Choose an existing image from the list.
9. Choose a version of the image from the list.
10. Choose **Next**.
11. Verify the values for **Image name**, **Image display
    name**, and **Description**.
12. Choose the IAM role. For more information, see
    [Create a Custom SageMaker Image for Amazon SageMaker Studio Classic](studio-byoi-create.md "studio-byoi-create.md").
13. (Optional) Add tags for the image.
14. Specify the EFS mount path. This is the path within the image to mount the user's
    Amazon Elastic File System (EFS) home directory.
15. For **Image type**, select **SageMaker Studio
    image**
16. For **Kernel name**, enter the name of an existing kernel in the
    image. For information on how to get the kernel information from the image, see [DEVELOPMENT](https://github.com/aws-samples/sagemaker-studio-custom-image-samples/blob/main/DEVELOPMENT.md "https://github.com/aws-samples/sagemaker-studio-custom-image-samples/blob/main/DEVELOPMENT.md") in the SageMaker Studio Classic Custom Image Samples repository. For more
    information, see the **Kernel discovery** and **User
    data** sections of [Custom SageMaker Image Specifications for Amazon SageMaker Studio Classic](studio-byoi-specs.md "studio-byoi-specs.md").
17. (Optional) For **Kernel display name**, enter the display name for
    the kernel.
18. Choose **Add kernel**.
19. Choose **Submit**.
    1. Wait for the image version to be attached to the
       domain. When attached, the version is displayed in the **Custom images**
       list and briefly highlighted.

### Attach the SageMaker image using the AWS CLI

The following sections demonstrate how to attach a custom SageMaker image when creating a new
domain or updating your existing domain using the AWS CLI.

#### Attach the SageMaker image to a new

domain

The following section demonstrates how to create a new domain with the version attached.
These steps require that you specify the Amazon Virtual Private Cloud (VPC) information and execution role
required to create the domain. You perform the following steps to create the domain and
attach the custom SageMaker image:

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

The response should look similar to the following.

```
vpc-xxxxxxxx
```

2. Get your default subnet IDs using the VPC ID from the previous step.

```
aws ec2 describe-subnets \
    --filters Name=vpc-id,Values=`<vpc-id>` \
    --query "Subnets[*].SubnetId" --output json
```

The response should look similar to the following.

```
[
    "subnet-b55171dd",
    "subnet-8a5f99c6",
    "subnet-e88d1392"
]
```

3. Create a configuration file named `create-domain-input.json`. Insert the VPC
   ID, subnet IDs, `ImageName`, and `AppImageConfigName` from the previous steps.
   Because `ImageVersionNumber` isn't specified, the latest version of the image is used,
   which is the only version in this case.

```
{
    "DomainName": "domain-with-custom-image",
    "VpcId": "`<vpc-id>`",
    "SubnetIds": [
        "`<subnet-ids>`"
    ],
    "DefaultUserSettings": {
        "ExecutionRole": "`<execution-role>`",
        "KernelGatewayAppSettings": {
            "CustomImages": [
                {
                    "ImageName": "custom-image",
                    "AppImageConfigName": "custom-image-config"
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

The response should look similar to the following.

```
{
    "DomainArn": "arn:aws:sagemaker:us-east-2:acct-id:domain/d-xxxxxxxxxxxx",
    "Url": "https://d-xxxxxxxxxxxx.studio.us-east-2.sagemaker.aws/..."
}
```

#### Attach the SageMaker image to your

current domain

If you have onboarded to a SageMaker AI domain, you can attach the custom image to your current
domain. For more information about onboarding to a SageMaker AI domain, see [Amazon SageMaker AI domain overview](gs-studio-onboard.md "gs-studio-onboard.md"). You don't need to specify
the VPC information and execution role when attaching a custom image to your current domain.
After you attach the version, you must delete all the apps in your domain and reopen
Studio Classic. For information about deleting the apps, see [Delete an Amazon SageMaker AI domain](gs-studio-delete-domain.md "gs-studio-delete-domain.md").

You perform the following steps to add the SageMaker image to your current domain.

- Get your `DomainID` from SageMaker AI control panel.
- Use the `DomainID` to get the `DefaultUserSettings`
  for the domain.
- Add the `ImageName` and `AppImageConfig` as a `CustomImage` to the
  `DefaultUserSettings`.
- Update your domain to include the custom image.

###### To add the custom SageMaker image to your domain

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the left navigation pane, choose **Admin configurations**.
3. Under **Admin configurations**, choose **domains**.
4. From the **Domains** page, select the domain to attach the image
   to.
5. From the **Domain details** page, select the **Domain
   settings** tab.
6. From the **Domain settings** tab, under **General
   settings**, find the `DomainId`. The ID is in the following
   format: `d-xxxxxxxxxxxx`.
7. Use the domain ID to get the description of the domain.

```
aws sagemaker describe-domain \
    --domain-id `<d-xxxxxxxxxxxx>`
```

The response should look similar to the following.

```
{
    "DomainId": "d-xxxxxxxxxxxx",
    "DefaultUserSettings": {
      "KernelGatewayAppSettings": {
        "CustomImages": [
        ],
        ...
      }
    }
}
```

8. Save the default user settings section of the response to a file named
   `default-user-settings.json`.
9. Insert the `ImageName` and `AppImageConfigName` from the previous steps as
   a custom image. Because `ImageVersionNumber` isn't specified, the latest version of the
   image is used, which is the only version in this case.

```
{
    "DefaultUserSettings": {
        "KernelGatewayAppSettings": {
           "CustomImages": [
              {
                 "ImageName": "string",
                 "AppImageConfigName": "string"
              }
           ],
           ...
        }
    }
}
```

10. Use the domain ID and default user settings file to update your domain.

```
aws sagemaker update-domain \
    --domain-id `<d-xxxxxxxxxxxx>` \
    --cli-input-json file://default-user-settings.json
```

The response should look similar to the following.

```
{
    "DomainArn": "arn:aws:sagemaker:us-east-2:acct-id:domain/d-xxxxxxxxxxxx"
}
```

## Attach the SageMaker image to a shared space

You can only attach the SageMaker image to a shared space using the AWS CLI. After you attach
the version, you must delete all of the applications in your shared space and reopen
Studio Classic. For information about deleting the apps, see [Delete an Amazon SageMaker AI domain](gs-studio-delete-domain.md "gs-studio-delete-domain.md").

You perform the following steps to add the SageMaker image to a shared space.

- Get your `DomainID` from SageMaker AI control panel.
- Use the `DomainID` to get the `DefaultSpaceSettings` for the
  domain.
- Add the `ImageName` and `AppImageConfig` as a `CustomImage`
  to the `DefaultSpaceSettings`.
- Update your domain to include the custom image for the shared space.

###### To add the custom SageMaker image to your shared space

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the left navigation pane, choose **Admin configurations**.
3. Under **Admin configurations**, choose **domains**.
4. From the **Domains** page, select the domain to attach the image
   to.
5. From the **Domain details** page, select the **Domain
   settings** tab.
6. From the **Domain settings** tab, under **General
   settings**, find the `DomainId`. The ID is in the following
   format: `d-xxxxxxxxxxxx`.
7. Use the domain ID to get the description of the domain.

```
aws sagemaker describe-domain \
    --domain-id `<d-xxxxxxxxxxxx>`
```

The response should look similar to the following.

```
{
    "DomainId": "d-xxxxxxxxxxxx",
    ...
    "DefaultSpaceSettings": {
      "KernelGatewayAppSettings": {
        "CustomImages": [
        ],
        ...
      }
    }
}
```

8. Save the default space settings section of the response to a file named
   `default-space-settings.json`.
9. Insert the `ImageName` and `AppImageConfigName` from the previous steps as
   a custom image. Because `ImageVersionNumber` isn't specified, the latest version of the
   image is used, which is the only version in this case.

```
{
    "DefaultSpaceSettings": {
        "KernelGatewayAppSettings": {
           "CustomImages": [
              {
                 "ImageName": "string",
                 "AppImageConfigName": "string"
              }
           ],
           ...
        }
    }
}
```

10. Use the domain ID and default space settings file to update your domain.

```
aws sagemaker update-domain \
    --domain-id `<d-xxxxxxxxxxxx>` \
    --cli-input-json file://default-space-settings.json
```

The response should look similar to the following.

```
{
    "DomainArn": "arn:aws:sagemaker:us-east-2:acct-id:domain/d-xxxxxxxxxxxx"
}
```

## View the attached image in SageMaker AI

After you create the custom SageMaker image and attach it to your domain, the image appears in
the **Environment** tab of the domain. You can only view the attached
images for shared spaces using the AWS CLI by using the following command.

```
aws sagemaker describe-domain \
    --domain-id `<d-xxxxxxxxxxxx>`
```
