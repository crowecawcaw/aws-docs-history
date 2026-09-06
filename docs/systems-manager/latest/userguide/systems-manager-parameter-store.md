

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# AWS Systems Manager Parameter Store
<a name="systems-manager-parameter-store"></a>

Parameter Store is a centralized configuration data store for named values called parameters. A *parameter* is any piece of data stored in Parameter Store, such as a block of text, a list of names, an AMI ID, a license key, and so on. With Parameter Store, you can securely store, organize, and retrieve configuration data at scale.

Parameter Store simplifies configuration management across environments. You can standardize how applications access critical data at runtime without hardcoding values or relying on fragmented storage solutions. In this way, you maintain consistency, enforce governance, and build more secure and maintainable systems. 

Parameter Store supports the following parameter types:
+ `String`

  Use this type for plain text values, such as environment names, endpoint URLs, or resource identifiers.
+ `StringList`

  Use this type for a comma-separated list of plain-text values. For example, you could store the value `subnet-123abc,subnet-456def,subnet-789ghi`.
+ `SecureString`

  Use `SecureString` for configuration values that require encryption, such as service endpoints and account identifiers. For secrets such as database credentials, API keys, or tokens, we recommend AWS Secrets Manager, which provides purpose built security controls including automatic rotation and cross-region replication.

  Parameter Store encrypts the values using AWS Key Management Service.

For more information about parameter types, see [Parameter Store reference](what-is-a-parameter.md).

## Where should I store my application data?
<a name="parameter-store-use-cases"></a>

Use the following table to choose a service for your application data.

**Note**  
If you manage credentials such as usernames, passwords, or any other secrets, we recommend using [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html). Secrets Manager is purpose-built for managing secrets such as database credentials, API keys, and supported third-party software-vended secrets. For more information, see [What is AWS Secrets Manager?](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) in the *AWS Secrets Manager User Guide*.



| Feature | Parameter Store | AWS AppConfig | AWS Secrets Manager | 
| --- | --- | --- | --- | 
| Use cases |  +  Static configuration <br />+  Key-value storage without deployment or validation   |  +  Frequently changed application configuration <br />+  Zero-downtime deployments <br />+  Runtime experiments   |  +  Credentials or any other secrets <br />+  Encrypted data requiring automatic rotation, cross-account access, or fine-grained audit logging   | 
| Typical data |  +  Approved AMI IDs <br />+  Environment variables <br />+  Endpoint URLs <br />+  Resource identifiers <br />+  Tuning parameters   |  +  Feature flags <br />+  Operational toggles <br />+  Tunable parameters <br />+  Allow and deny lists   |  +  Database credentials <br />+  API keys <br />+  OAuth tokens <br />+  Private keys and certificates   | 
| Encryption | Optional with `SecureString` and AWS KMS | AWS managed encryption at rest; optional additional customer managed key | AWS KMS encryption at rest with an AWS managed or customer managed key | 
| Credential rotation | None | Not applicable | Automatic, with native database integrations | 
| Cost | Standard tier free; advanced tier and higher throughput billed | Billed per configuration request | Billed per secret per month and per API call | 
| Deployment | Versioning without pre-deployment validation or automatic rollback | Gradual rollout, pre-deployment validation, and automatic rollback on CloudWatch Logs alarms | Versioning with staging labels | 

## Parameter Store features
<a name="parameter-store-features"></a>

Parameter Store supports the following features:
+ **Centralized configuration updates**

  Update your configuration without code changes or redeployments, improving operational agility and reducing risk. For example, you can update /myapp/prod/inventory-service-endpoint to point to a new endpoint after migrating the inventory service.
+ **High-performance throughput option**

  Parameter Store provides a default throughput suitable for lower-scale workloads. For large or latency-sensitive applications that need higher request rates, you can enable high-throughput mode for an additional cost.

  If your application retrieves parameters frequently or at scale, evaluate throughput settings early to avoid throttling. For information about enabling high throughput, see [Managing Parameter Store throughput](parameter-store-throughput.md).
+ **Hierarchical parameter management**

  Use [parameter hierarchies](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-hierarchies.html) to group related parameters, making it easier to discover, manage, and filter them across environments and applications. For example, you can create the naming convention /env/computer-type/app/data, and then create application-specific parameters such as /dev/webserver/linux/approved-ami and /dev/webserver/windows/approved-ami. You can retrieve the path /dev/webserver to find all web server parameters for development environments, or /dev/webserver/linux to find only Linux image parameters.
+ **Versioning**

  Parameter Store retains the 100 most recent [versions](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-versions.html) of each parameter. When you investigate operational issues, you can review and reconstruct previous values.
+ **Integration with IAM**

  Use IAM policies to determine whether an application can read, write, list, or delete parameters. For example, you could write an application role that can read parameters prefixed with /myapp/prod/\* but not /myapp/dev/\*. You could also grant a role permission to decrypt an encrypted parameter.
+ **Accessibility from other AWS services**

  You can reference parameter values from other AWS services. Here are some examples:
  + Lambda functions can retrieve parameters and secrets using the [Parameters and Secrets Lambda Extension](https://docs.aws.amazon.com/systems-manager/latest/userguide/ps-integration-lambda-extensions.html).
  + Amazon Elastic Container Service and AWS Fargate allow you to [inject environmental variables](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/secrets-envvar-ssm-paramstore.html) whose values are managed centrally in Parameter Store.
  + AWS CloudFormation templates can reference [parameter values](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references-ssm.html).
  + AWS AppConfig lets you create [configuration profiles that reference parameters](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-free-form-configuration-and-profile-create-console.html). You can safely deploy configuration changes using features such as gradual rollouts, alarm-based rollbacks, and built-in data validation.
  + AWS CodeBuild lets you [define environmental variables](https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html#build-spec.env.parameter-store) whose values are dynamically retrieved from Parameter Store at build time.
+ **Shared account access**

  Centralize configuration data in a single AWS account and share parameters with other accounts that need access. For more information, see [Working with shared parameters in Parameter Store](parameter-store-shared-parameters.md).
+ **OS patching**

  Amazon EC2 lets you specify the operating system for new instances by [referencing a parameter instead of hardcoding an AMI (AMI) ID](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-systems-manager-parameter-to-find-AMI.html). This approach ensures your instances automatically use the latest patched and updated images. AWS and operating system vendors provide [public parameters](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-finding-public-parameters.html) that track current AMI versions, so you don't have to manage updates manually. You can also define your own parameters to reference a centrally managed golden AMI, making it easier to enforce consistent, approved configurations across your organization.
+ **Events and notifications**

  Automate workflows in Parameter Store by subscribing to parameter [change events](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-cwe.html). You can also use [change events](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-policies.html) to enforce expiration and receive notifications when a parameter hasn't been rotated within a specified timeframe.

## Parameter tiers in Parameter Store
<a name="parameter-store-tiers-introduction"></a>

Parameter Store offers different parameter tiers that control storage limits: the maximum number and size of your parameters in an AWS account and Region. Configure each parameter individually to use either the standard tier or advanced tier.

You can mix standard and advanced parameters. For example, you can have up to 100,000 advanced parameters and 10,000 standard parameters in the same AWS account and Region. The following table describes the different features supported for each parameter type.

The following table describes the differences between parameter tiers.



| Feature or use case | Standard | Advanced | 
| --- | --- | --- | 
| Use case | Best for most configuration data and low-scale workloads. This is the default. | Best when you need higher limits, larger values, or parameter policies. | 
| Maximum parameters<br />(per AWS account and AWS Region) | 10,000 | 100,000 | 
| Maximum value size | 4 KB | 8 KB | 
| Parameter policies | Not supported | Supported<br />For more information, see [Assigning parameter policies in Parameter Store](parameter-store-policies.md). | 
| Shareability across AWS accounts | Not supported | Supported<br />For more information, see [Working with shared parameters in Parameter Store](parameter-store-shared-parameters.md). | 
| Upgrade and downgrade capability | Upgradeable | Not downgradeable | 
| Cost | No additional charge | Charges apply<br />For more information, see [AWS Systems Manager Pricing for Parameter Store](https://aws.amazon.com/systems-manager/pricing/#Parameter_Store). | 

Use standard parameters for most configuration data. Use advanced parameters only when you need capabilities that standard parameters don't support.

For a detailed comparison of standard and advanced parameters, see [Choosing parameter tiers](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-advanced-parameters.html).