# Creating a free form

configuration profile in AWS AppConfig

_Configuration data_ is a collection of settings that influence the
behavior of your application. A _configuration profile_ includes, among
other things, a URI that enables AWS AppConfig to locate your configuration data in its stored
location and a configure type. With freeform configuration profiles, you can store your data
in the AWS AppConfig hosted configuration store or any of the following AWS services and Systems Manager
tools:

| Location                                                                                                                                                                                           | Supported file types                                                                                                                                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AWS AppConfig hosted configuration store                                                                                                                                                           | YAML, JSON, and text if added using the AWS Management Console. Any file type if added<br>using the AWS AppConfig [CreateHostedConfigurationVersion](../../2019-10-09/APIReference/API_CreateHostedConfigurationVersion.md "../../2019-10-09/APIReference/API_CreateHostedConfigurationVersion.md") API action. |
| [Amazon Simple Storage Service (Amazon S3)](../../../AmazonS3/latest/userguide/Welcome.md "../../../AmazonS3/latest/userguide/Welcome.md")                                                         | Any                                                                                                                                                                                                                                                                                                             |
| [AWS CodePipeline](../../../codepipeline/latest/userguide/welcome.md "../../../codepipeline/latest/userguide/welcome.md")                                                                          | Pipeline (as defined by the service)                                                                                                                                                                                                                                                                            |
| [AWS Secrets Manager](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md")                                                                       | Secret (as defined by the service)                                                                                                                                                                                                                                                                              |
| [AWS Systems Manager Parameter Store](../../../systems-manager/latest/userguide/systems-manager-parameter-store.md "../../../systems-manager/latest/userguide/systems-manager-parameter-store.md") | Standard and secure string parameters (as defined by Parameter Store)                                                                                                                                                                                                                                           |
| [AWS Systems Manager document store<br>(SSM documents)](../../../systems-manager/latest/userguide/documents.md "../../../systems-manager/latest/userguide/documents.md")                           | YAML, JSON, text                                                                                                                                                                                                                                                                                                |

A configuration profile can also include optional validators to ensure your
configuration data is syntactically and semantically correct. AWS AppConfig performs a check using
the validators when you start a deployment. If any errors are detected, the deployment stops
before making any changes to the targets of the configuration.

###### Note

If possible, we recommend hosting your configuration data in the AWS AppConfig hosted
configuration store as it offers the most features and enhancements.

For freeform configurations stored in the AWS AppConfig hosted configuration store or SSM
documents, you can create the freeform configuration by using the Systems Manager console at the time
you create a configuration profile. The process is described later in this topic.

For freeform configurations stored in Parameter Store, Secrets Manager, or Amazon S3, you must create the
parameter, secret, or object first and store it in the relevant configuration store. After
you store the configuration data, use the procedure in this topic to create the
configuration profile.

###### Topics

- [Understanding
  validators](appconfig-creating-configuration-and-profile-validators.md "appconfig-creating-configuration-and-profile-validators.md")
- [Understanding
  configuration store quotas and limitations](appconfig-creating-configuration-and-profile-quotas.md "appconfig-creating-configuration-and-profile-quotas.md")
- [Understanding the AWS AppConfig hosted configuration store](appconfig-creating-configuration-and-profile-about-hosted-store.md "appconfig-creating-configuration-and-profile-about-hosted-store.md")
- [Understanding
  configurations stored in Amazon S3](appconfig-creating-configuration-and-profile-S3-source.md "appconfig-creating-configuration-and-profile-S3-source.md")
- [Creating an AWS AppConfig freeform configuration profile (console)](appconfig-creating-free-form-configuration-and-profile-create-console.md "appconfig-creating-free-form-configuration-and-profile-create-console.md")
- [Creating an AWS AppConfig freeform configuration profile (command line)](appconfig-creating-free-form-configuration-and-profile-create-commandline.md "appconfig-creating-free-form-configuration-and-profile-create-commandline.md")
