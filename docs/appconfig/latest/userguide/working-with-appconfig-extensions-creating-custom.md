

# Walkthrough: Creating custom AWS AppConfig extensions
<a name="working-with-appconfig-extensions-creating-custom"></a>

To create a custom AWS AppConfig extension, complete the following tasks. Each task is described in more detail in later topics.

**Note**  
You can view samples of custom AWS AppConfig extensions on GitHub:  
[Sample extension that prevents deployments with a `blocked day` moratorium calendar using Systems Manager Change Calendar](https://github.com/aws-samples/aws-appconfig-change-calendar-extn)
[Sample extension that prevents secrets from leaking into configuration data using git-secrets](https://github.com/aws-samples/aws-appconfig-git-secrets-extn)
[Sample extension that prevents personally identifiable information (PII) from leaking into configuration data using Amazon Comprehend](https://github.com/aws-samples/aws-appconfig-pii-extn)

**1. [Create an AWS Lambda function](https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions-creating-custom-lambda.html)**  
For most use cases, to create a custom extension, you must create an AWS Lambda function to perform any computation and processing defined in the extension. An exception to this rule is if you create *custom* versions of the [AWS authored notification extensions](https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions-about-predefined.html) to add or remove action points. For more details about this exception, see [Step 3: Create a custom AWS AppConfig extension](working-with-appconfig-extensions-creating-custom-extensions.md).

**2. [Configure permissions for your custom extension](https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions-creating-custom-permissions.html)**  
To configure permissions for your custom extension, you can do one of the following:  
+ Create an AWS Identity and Access Management (IAM) service role that includes `InvokeFunction` permissions. 
+ Create a resource policy by using the Lambda [AddPermission](https://docs.aws.amazon.com/lambda/latest/dg/API_AddPermission.html) API action.
This walkthrough describes how to create the IAM service role.

**3. [Create an extension](https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions-creating-custom-extensions.html)**  
You can create an extension by using the AWS AppConfig console or by calling the [CreateExtension](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_CreateExtension.html) API action from the AWS CLI, AWS Tools for PowerShell, or the SDK. The walkthrough uses the console.

**4. [Create an extension association](https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions-creating-custom-association.html)**  
You can create an extension association by using the AWS AppConfig console or by calling the [CreateExtensionAssociation](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_CreateExtensionAssociation.html) API action from the AWS CLI, AWS Tools for PowerShell, or the SDK. The walkthrough uses the console.

**5. Perform an action that invokes the extension**  
After you create the association, AWS AppConfig invokes the extension when the action points defined by the extension occur for that resource. For example, if you associate an extension that contains a `PRE_CREATE_HOSTED_CONFIGURATION_VERSION` action, the extension is invoked every time you create a new hosted configuration version.

The topics in this section describe each task involved in creating a custom AWS AppConfig extension. Each task is described in the context of a use case where a customer wants to create an extension that automatically backs up a configuration to an Amazon Simple Storage Service (Amazon S3) bucket. The extension runs whenever a hosted configuration is created (`PRE_CREATE_HOSTED_CONFIGURATION_VERSION`) or deployed (`PRE_START_DEPLOYMENT`).

**Topics**
+ [Step 1: Create a Lambda function for a custom AWS AppConfig extension](working-with-appconfig-extensions-creating-custom-lambda.md)
+ [Step 2: Configure permissions for a custom AWS AppConfig extension](working-with-appconfig-extensions-creating-custom-permissions.md)
+ [Step 3: Create a custom AWS AppConfig extension](working-with-appconfig-extensions-creating-custom-extensions.md)
+ [Step 4: Create an extension association for a custom AWS AppConfig extension](working-with-appconfig-extensions-creating-custom-association.md)