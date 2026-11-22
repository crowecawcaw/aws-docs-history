

# Creating configuration data with AWS AppConfig

The topics in this section help you complete the following tasks in AWS AppConfig. These tasks create important artifacts for deploying configuration data.

**1. [Create an application namespace](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-namespace.html)**  
To create an application namespace, you create an AWS AppConfig artifact called an application. An application is simply an organizational construct like a folder.

**2. [Create environments](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-environment.html)**  
For each AWS AppConfig application, you define one or more environments. An environment is a logical deployment group of AWS AppConfig targets, such as applications in a `Beta` or `Production` environment. You can also define environments for application subcomponents, such as `AWS Lambda functions`, `Containers`, `Web`, `Mobile`, and `Back-end`.  
You can configure Amazon CloudWatch alarms for each environment to automatically rollback problematic configuration changes. The system monitors alarms during a configuration deployment. If an alarm is triggered, the system rolls back the configuration.

**3. [Create a configuration profile](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-profile.html)**  
*Configuration data* is a collection of settings that influence the behavior of your application. A *configuration profile* includes, among other things, a URI that enables AWS AppConfig to locate your configuration data in its stored location and a configure type. AWS AppConfig supports the following types of configuration profiles:  
+ **Feature flags**: You can use feature flags to enable or disable features within your applications or to configure different characteristics of your application features using flag attributes. AWS AppConfig stores feature flag configurations in the AWS AppConfig hosted configuration store in a feature flag format that contains data and metadata about your flags and the flag attributes. The URI for feature flag configurations is simply `hosted`. 

  AWS AppConfig offers basic feature flags, which (if enabled) return a specific set of configuration data per request. To support user segmentation and traffic splitting use cases, AWS AppConfig also offers [multi-variant feature flags](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-multi-variant-feature-flags.html), which enable you to define a set of possible flag values to return for a request. When requesting a flag configured with variants, your application provides context that AWS AppConfig evaluates against a set of user-defined rules. Depending on the context specified in the request and the rules defined for the variant, AWS AppConfig returns different flag values to the application.
+ **Freeform configurations**: A freeform configuration can store data in any of the following AWS services and Systems Manager tools:
  + AWS AppConfig hosted configuration store
  + Amazon Simple Storage Service
  + AWS CodePipeline
  + AWS Secrets Manager
  + AWS Systems Manager (SSM) Parameter Store
  + SSM Document Store
+ **AI model invocation configurations**: An AI model invocation configuration defines the settings for a call to an AI model, including the model identifier, inference parameters, messages (such as system prompts and example conversation turns), and provider-specific custom parameters. AWS AppConfig stores AI model invocation configurations in the hosted configuration store using the `AWS.AppConfig.AIModelInvocation` type.
+ **AI prompt configurations**: An AI prompt configuration manages a prompt as a first-class, versioned artifact. Prompts change faster than model parameters, so storing them independently lets you iterate on prompt content without redeploying the model configuration. AWS AppConfig stores AI prompt configurations in the hosted configuration store using the `AWS.AppConfig.AIPrompt` type.
If possible, we recommend hosting your configuration data in the AWS AppConfig hosted configuration store as it offers the most features and enhancements.

**Topics**
+ [Understanding the configuration profile IAM role](appconfig-creating-configuration-and-profile-iam-role.md)
+ [Creating a namespace for your application in AWS AppConfig](appconfig-creating-namespace.md)
+ [Creating environments for your application in AWS AppConfig](appconfig-creating-environment.md)
+ [Creating a configuration profile in AWS AppConfig](appconfig-creating-configuration-profile.md)