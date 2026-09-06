

# Launch Amazon SageMaker Studio Classic
<a name="studio-launch"></a>

**Important**  
Custom IAM policies that allow Amazon SageMaker Studio or Amazon SageMaker Studio Classic to create Amazon SageMaker resources must also grant permissions to add tags to those resources. The permission to add tags to resources is required because Studio and Studio Classic automatically tag any resources they create. If an IAM policy allows Studio and Studio Classic to create resources but does not allow tagging, "AccessDenied" errors can occur when trying to create resources. For more information, see [Provide permissions for tagging SageMaker AI resources](security_iam_id-based-policy-examples.md#grant-tagging-permissions).  
[AWS managed policies for Amazon SageMaker AI](security-iam-awsmanpol.md) that give permissions to create SageMaker resources already include permissions to add tags while creating those resources.

**Note**  
As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md).  
Studio Classic is still maintained for existing workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md).

After you have onboarded to an Amazon SageMaker AI domain, you can launch an Amazon SageMaker Studio Classic application from either the SageMaker AI console or the AWS CLI. For more information about onboarding to a domain, see [Amazon SageMaker AI domain overview](gs-studio-onboard.md).

**Topics**
+ [Launch Amazon SageMaker Studio Classic Using the Amazon SageMaker AI Console](#studio-launch-console)
+ [Launch Amazon SageMaker Studio Classic Using the AWS CLI](#studio-launch-cli)

## Launch Amazon SageMaker Studio Classic Using the Amazon SageMaker AI Console
<a name="studio-launch-console"></a>

The process to navigate to Studio Classic from the Amazon SageMaker AI Console differs depending on if Studio Classic or Amazon SageMaker Studio are set as the default experience for your domain. For more information about setting the default experience for your domain, see [Migration from Amazon SageMaker Studio Classic](studio-updated-migrate.md).

**Topics**
+ [Prerequisite](#studio-launch-console-prerequisites)

### Prerequisite
<a name="studio-launch-console-prerequisites"></a>

 To complete this procedure, you must onboard to a domain by following the steps in [Onboard to Amazon SageMaker AI domain](https://docs.aws.amazon.com/sagemaker/latest/dg/gs-studio-onboard.html). 

### Launch Studio Classic if Studio is your default experience
<a name="studio-launch-console-updated"></a>

1. Navigate to Studio following the steps in [Launch Amazon SageMaker Studio](studio-updated-launch.md).

1. From the Studio UI, find the applications pane on the left side.

1. From the applications pane, select **Studio Classic**.

1. From the Studio Classic landing page, select the Studio Classic instance to open.

1. Choose “Open”.

### Launch Studio Classic if Studio Classic is your default experience
<a name="studio-launch-console-classic"></a>

When Studio Classic is your default experience, you can launch a Amazon SageMaker Studio Classic application from the SageMaker AI console using the Studio Classic landing page or the Amazon SageMaker AI domain details page. The following sections demonstrate how to launch the Studio Classic application from the SageMaker AI console.

#### Launch Studio Classic from the domain details page
<a name="studio-launch-console-details"></a>

The following sections describe how to launch a Studio Classic application from the domain details page. The steps to launch the Studio Classic application after you have navigated to the domain details page differ depending on if you’re launching a personal application or a shared space. 

 **Navigate to the domain details page** 

 The following procedure shows how to navigate to the domain details page. 

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/).

1. On the left navigation pane, choose **Admin configurations**.

1. Under **Admin configurations**, choose **domains**. 

1. From the list of domain, select the domain that you want to launch the Studio Classic application in.

 **Launch a user profile app** 

 The following procedure shows how to launch a Studio Classic application that is scoped to a user profile. 

1.  On the domain details page, choose the **User profiles** tab. 

1.  Identify the user profile that you want to launch the Studio Classic application for. 

1.  Choose **Launch** for your selected user profile, then choose **Studio Classic**. 

 **Launch a shared space app** 

 The following procedure shows how to launch a Studio Classic application that is scoped to a shared space. 

1.  On the domain details page, choose the **Space management** tab. 

1.  Identify the shared space that you want to launch the Studio Classic application for. 

1.  Choose **Launch Studio Classic** for your selected shared space. 

#### Launch Studio Classic from the Studio Classic landing page
<a name="studio-launch-console-landing"></a>

 The following procedure describes how to launch a Studio Classic application from the Studio Classic landing page. 

 **Launch Studio Classic** 

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/).

1. On the left navigation pane, choose Studio Classic.

1.  Under **Get started**, select the domain that you want to launch the Studio Classic application in. If your user profile only belongs to one domain, you do not see the option for selecting a domain.

1.  Select the user profile that you want to launch the Studio Classic application for. If there is no user profile in the domain, choose **Create user profile**. For more information, see [Add user profiles](domain-user-profile-add.md).

1.  Choose **Launch Studio Classic**. If the user profile belongs to a shared space, choose **Open Spaces**. 

1.  To launch a Studio Classic application scoped to a user profile, choose **Launch personal Studio Classic**. 

1.  To launch a shared Studio Classic application, choose the **Launch shared Studio Classic** button next to the shared space that you want to launch into. 

## Launch Amazon SageMaker Studio Classic Using the AWS CLI
<a name="studio-launch-cli"></a>

You can use the AWS Command Line Interface (AWS CLI) to launch Amazon SageMaker Studio Classic by creating a presigned domain URL.

 **Prerequisites** 

 Before you begin, complete the following prerequisites: 
+  Onboard to Amazon SageMaker AI domain. For more information, see [Onboard to Amazon SageMaker AI domain](https://docs.aws.amazon.com/sagemaker/latest/dg/gs-studio-onboard.html). 
+  Update the AWS CLI by following the steps in [Installing the current AWS CLI Version](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv1.html#install-tool-bundled). 
+  From your local machine, run `aws configure` and provide your AWS credentials. For information about AWS credentials, see [Understanding and getting your AWS credentials](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html). 

The following code snippet demonstrates how to launch Amazon SageMaker Studio Classic from the AWS CLI using a presigned domain URL. For more information, see [create-presigned-domain-url](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-presigned-domain-url.html).

```
aws sagemaker create-presigned-domain-url \
--region {{region}} \
--domain-id {{domain-id}} \
--space-name {{space-name}} \
--user-profile-name {{user-profile-name}} \
--session-expiration-duration-in-seconds 43200
```