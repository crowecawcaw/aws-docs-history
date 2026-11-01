

# Setting up the SageMakerAIDomain blueprint for code spaces
<a name="sagemaker-ai-domain"></a>

The SageMakerAIDomain blueprint provisions a standalone Amazon SageMaker AI domain for a project. This domain is separate from the one that the Tooling blueprint creates. With this blueprint, you control the code spaces experience for project members, including which application types are available and which space configurations members can choose.

The SageMakerAIDomain blueprint supports JupyterLab, Code Editor, and RStudio spaces in Identity Center-based domains. The Tooling blueprint does not offer RStudio. For more information about the RStudio IDE, see [Using the RStudio IDE in Amazon SageMaker Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/rstudio.html).

## Adding the blueprint to a project profile
<a name="sagemaker-ai-domain-add"></a>

A project profile is a collection of blueprints that you use to create projects. You add the SageMakerAIDomain blueprint to a project profile from the Amazon SageMaker management console. Before you begin, enable the SageMakerAIDomain blueprint for your domain in the AWS account and Region where you use the project profile.

1. Open the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone). Use the Region selector to choose your AWS Region.

1. Choose **View domains**, and then choose your domain.

1. Choose the **Project profiles** tab, and then choose the project profile that you want to update.

1. Choose the **Blueprint deployment settings** tab, and then choose **Add blueprint deployment settings**.

1. For the blueprint, choose **SageMakerAIDomain**. Specify the account and Region where the blueprint is enabled.

1. Set the blueprint parameters for the project profile. For a description of each parameter, see [SageMakerAIDomain blueprint parameters](#sagemaker-ai-domain-parameters). To let project owners set a parameter during project creation, choose **Editable** for that parameter.

1. Add notes for project owners, and then save the deployment settings.

After you add the blueprint, members who create a project from the project profile can create code spaces that use the parameters you set.

## SageMakerAIDomain blueprint parameters
<a name="sagemaker-ai-domain-parameters"></a>

You configure custom images, default images, idle timeouts, and instance types through these blueprint parameters, not with the `sagemaker` CLI. What you configure is what members see when they create a space.

You can set the following parameters for the SageMakerAIDomain blueprint.


**SageMakerAIDomain blueprint parameters**  

| Parameter | Description | 
| --- | --- | 
| `enableRStudio` | Whether RStudio support is enabled for the domain. The default is `false`.<br />Note: After you enable RStudio for a domain, you cannot disable it. | 
| `domainName` | The name of the Amazon SageMaker AI domain. You can set this name only when the domain is created. If you leave it blank, a name is generated automatically. | 
| `customImagesJupyterLab` and `customImagesCodeEditor` | The custom images attached for JupyterLab and Code Editor spaces. You can configure up to 30 images for each application type. Members choose from these images when they create a space. | 
| `defaultImageVersionArnJupyterLab` and `defaultImageVersionArnCodeEditor` | The default image, pinned by image-version ARN, for JupyterLab and Code Editor spaces. You must also attach the default image through the matching custom-images parameter. | 
| `idleTimeoutInMinutesJupyterLab` and `idleTimeoutInMinutesCodeEditor`, with their `minIdleTimeoutInMinutes` and `maxIdleTimeoutInMinutes` counterparts | The default idle timeout and the range that members can choose before a space is shut down because of inactivity. | 
| `lifecycleManagementJupyterLab` and `lifecycleManagementCodeEditor` | Whether idle shutdown is activated for JupyterLab and Code Editor spaces. | 
| `hiddenInstanceTypes` | The instance types to hide from members, so that only the allowed instance types are offered. | 
| `hiddenSageMakerImageVersionAliases` | The Amazon SageMaker AI image versions to hide from members. | 
| `maxEbsVolumeSize` | The maximum Amazon EBS storage volume size, in GB, for members' spaces. | 

## Adding the required inline policy for RStudio
<a name="sagemaker-ai-domain-rstudio-policy"></a>

To let project members use RStudio spaces, attach an inline policy to the project's IAM role. This policy grants the permissions that RStudio and Posit Workbench require to check out the RStudio license, deliver logs, and manage the RStudio application lifecycle. Without it, RStudio space creation or session startup fails.

To add the inline policy, complete the following steps:

1. Create a project from a project profile that includes the SageMakerAIDomain blueprint, and wait for the project to finish provisioning.

1. Find the project's IAM role. In the IAM console, locate the project user role that Amazon SageMaker Unified Studio created for the project. The role name has the form `datazone_usr_role_{{projectId}}_{{environmentId}}`. You can match it using the environment ID of the project you created.

1. On the role's details page, choose **Add permissions**, and then choose **Create inline policy**.

1. Choose the **JSON** tab and replace the contents with the following policy:

   ```
   {
     "Version": "2012-10-17",		 	 	 
     "Statement": [
       {
         "Sid": "RStudioLicenseManagerAccess",
         "Effect": "Allow",
         "Action": [
           "license-manager:CheckoutLicense",
           "license-manager:CheckInLicense",
           "license-manager:ExtendLicenseConsumption",
           "license-manager:GetLicense",
           "license-manager:ListReceivedLicenses"
         ],
         "Resource": "*"
       },
       {
         "Sid": "RStudioLogDelivery",
         "Effect": "Allow",
         "Action": [
           "logs:CreateLogDelivery",
           "logs:DeleteLogDelivery",
           "logs:GetLogDelivery",
           "logs:ListLogDeliveries",
           "logs:UpdateLogDelivery",
           "logs:PutResourcePolicy"
         ],
         "Resource": "*"
       },
       {
         "Sid": "RStudioDirectLogging",
         "Effect": "Allow",
         "Action": [
           "logs:CreateLogGroup",
           "logs:CreateLogStream",
           "logs:DescribeLogGroups",
           "logs:DescribeLogStreams",
           "logs:GetLogEvents",
           "logs:PutLogEvents"
         ],
         "Resource": "*"
       },
       {
         "Sid": "RStudioAppLifecycleAccess",
         "Effect": "Allow",
         "Action": [
           "sagemaker:CreateApp",
           "sagemaker:DescribeApp",
           "sagemaker:DeleteApp"
         ],
         "Resource": [
           "arn:aws:sagemaker:*:*:app/*/*/RStudioServerPro/*",
           "arn:aws:sagemaker:*:*:app/*/*/RSessionGateway/*"
         ]
       }
     ]
   }
   ```

1. Choose **Next**, enter a name for the policy, and then choose **Create policy**.