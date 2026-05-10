# AWS Systems Manager Parameter Store

Parameter Store enables you to securely store, organize, and retrieve configuration simple configuration data at scale. It is designed to simplify configuration management across environments, allowing teams to standardize how applications access critical data without hardcoding values or relying on fragmented storage solutions.

Beyond simple storage, Parameter Store provides versioning, access control through AWS Identity and Access Management (IAM), and seamless integration with other AWS services such as Amazon EC2, Lambda, and CloudFormation. This enables dynamic configuration updates without requiring code changes or redeployments, improving operational agility and reducing risk. With features like hierarchical naming, parameter policies, and change tracking, Parameter Store helps teams maintain consistency, enforce governance, and build more secure and maintainable systems.

Parameter Store supports `String`,
`StringList`, and `SecureString` parameter types. `String` and `StringList` parameter values are stored as plain text. `SecureString` parameters encrypt values using AWS Key Management Service, making them a practical choice for lightweight encrypted configuration values that don't require rotation or other advanced secret lifecycle capabilities. For more information about parameter types, see [Understanding parameter types](what-is-a-parameter.md "what-is-a-parameter.md")

###### Note

If you manage credentials that require automatic rotation, cross-account access, or fine-grained audit logging, we recommend using [AWS Secrets Manager](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md"). Secrets Manager is purpose-built for managing secrets such as database credentials, API keys, and supported third-party software-vended secrets. For more information, see [What is AWS Secrets Manager?](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md") in the _AWS Secrets Manager User Guide_.

Here are some examples of the types of configuration data you can store and manage in Parameter Store:

- **Database connection strings (non-rotating)** – jdbc:mysql://host:3306/appdb
- **Application environment variables** – ENV=production, LOG_LEVEL=debug
- **Service endpoint URLs** – internal microservice endpoints or third-party base URLs
- **Resource identifiers** – S3 bucket names, DynamoDB table names, ARNs
- **Application tuning parameters** – cache TTLs, batch sizes, polling intervals

###### Note

We _don't_ recommend using Parameter Store for the following types of configuration data:

- Feature flags
- Operational levers like timeouts
- Allow lists and block lists
- Circuit breakers
- Dynamic configurations
  For these types of configuration data, use AWS AppConfig. For more information, see [What is AWS AppConfig?](../../../appconfig/latest/userguide/what-is-appconfig.md "../../../appconfig/latest/userguide/what-is-appconfig.md").

## Parameter Store features

Parameter Store includes the following features for managing parameters:

- **Share parameters with other accounts**

Centralize configuration data in a single AWS account and share parameters with other accounts that need access. For more information, see [Working with shared parameters in Parameter Store](parameter-store-shared-parameters.md "parameter-store-shared-parameters.md").

- **OS Patching**

Amazon EC2 lets you specify the operating system for new instances by [referencing a parameter instead of hardcoding an AMI (AMI) ID](../../../AWSEC2/latest/UserGuide/using-systems-manager-parameter-to-find-AMI.html.md "../../../AWSEC2/latest/UserGuide/using-systems-manager-parameter-to-find-AMI.html.md"). This approach ensures your instances automatically use the latest patched and updated images. AWS and operating system vendors provide [public parameters](parameter-store-finding-public-parameters.md "parameter-store-finding-public-parameters.md") that track current AMI versions, so you don't have to manage updates manually. You can also define your own parameters to reference a centrally managed golden AMI, making it easier to enforce consistent, approved configurations across your organization.

- **Accessible from other AWS services**

Other AWS services allow you to easily reference parameter values. Here are some examples:

    + Lambda functions can retrieve parameters and secrets using the [Parameters and Secrets Lambda Extension](ps-integration-lambda-extensions.md "ps-integration-lambda-extensions.md").
    + Amazon Elastic Container Service and AWS Fargate allow you to [inject environmental variables](../../../AmazonECS/latest/developerguide/secrets-envvar-ssm-paramstore.md "../../../AmazonECS/latest/developerguide/secrets-envvar-ssm-paramstore.md") whose values are managed centrally in parameter store.
    + AWS CloudFormation templates can reference [parameter values](../../../AWSCloudFormation/latest/UserGuide/dynamic-references-ssm.md "../../../AWSCloudFormation/latest/UserGuide/dynamic-references-ssm.md").
    + AWS AppConfig enables you to create [configuration profiles that reference parameters](../../../appconfig/latest/userguide/appconfig-creating-free-form-configuration-and-profile-create-console.md "../../../appconfig/latest/userguide/appconfig-creating-free-form-configuration-and-profile-create-console.md"), allowing you to safely deploy configuration changes using features such as gradual rollouts, alarm-based rollbacks, and built-in data validation.
    + AWS CodeBuild allows you to [define environmental variables](../../../codebuild/latest/userguide/build-spec-ref.md#build-spec.env.parameter-store "../../../codebuild/latest/userguide/build-spec-ref.md#build-spec.env.parameter-store") whose values are dynamically retrieved from Parameter Store at build time.

- **Parameter History**

Parameter Store retains the 100 most recent [versions](sysman-paramstore-versions.md "sysman-paramstore-versions.md") of each parameter, so you can quickly review and reconstruct previous values when investigating operational issues.

- **Events and notifications**

Automate workflows in Parameter Store by subscribing to parameter [change events](sysman-paramstore-cwe.md "sysman-paramstore-cwe.md"). You can also use [change events](parameter-store-policies.md "parameter-store-policies.md") to enforce expiration and receive notifications when a parameter hasn’t been rotated within a specified timeframe.

- **Organize parameters hierarchically**

Use [parameter hierarchies](sysman-paramstore-hierarchies.md "sysman-paramstore-hierarchies.md") to group related parameters, making it easier to discover, manage, and filter them across environments and applications.

## Parameter tiers

Parameter Store offers multiple parameter tiers that affect cost, scale, and performance. You individually configure parameters to use either the standard-parameter tier (the default tier) or the advanced-parameter tier.

Use:

- Standard parameters for most configuration data and low-scale workloads
- Advanced parameters when you need higher limits, larger values, or parameter policies

###### Important

You can upgrade a parameter from standard to advanced, but you cannot downgrade it.

The following table describes the differences between parameter tiers.

| Feature                                                | Standard             | Advanced                                                                                                                                                                                                                            |
| ------------------------------------------------------ | -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Maximum parameters<br>(per AWS account and AWS Region) | 10,000               | 100,000                                                                                                                                                                                                                             |
| Maximum value size                                     | 4 KB                 | 8 KB                                                                                                                                                                                                                                |
| Parameter policies                                     | Not supported        | Supported<br>For more information, see [Assigning parameter policies in Parameter Store](parameter-store-policies.md "parameter-store-policies.md").                                                                                |
| Share parameters across AWS accounts                   | Not supported        | Supported<br>For more information, see [Working with shared parameters in Parameter Store](parameter-store-shared-parameters.md "parameter-store-shared-parameters.md").                                                            |
| Cost                                                   | No additional charge | Charges apply<br>For more information, see [AWS Systems Manager<br>Pricing for Parameter Store](https://aws.amazon.com/systems-manager/pricing/#Parameter_Store "https://aws.amazon.com/systems-manager/pricing/#Parameter_Store"). |

For more information about parameter tiers and their features, see [Managing tiers](parameter-store-advanced-parameters.md "parameter-store-advanced-parameters.md").

For a complete list of Parameter Store quotas and limits, see [AWS Systems Manager endpoints and quotas](../../../general/latest/gr/ssm.md#parameter-store "../../../general/latest/gr/ssm.md#parameter-store") in the _AWS General Reference_.

## Performance and throughput

Parameter Store provides a default throughput suitable for lower scale workloads. For applications that require higher request rates, you can enable higher throughput.

- Default throughput is sufficient for typical configuration retrieval patterns.
- High-throughput mode supports significantly higher request rates for large-scale or latency-sensitive applications.
- Additional charges apply when higher throughput is enabled.

If your application retrieves parameters frequently or at scale, evaluate throughput settings early to avoid throttling. For information about enabling high-throughput, see [Changing Parameter Store throughput](parameter-store-throughput.md "parameter-store-throughput.md").

## How to retrieve parameters

You can retrieve parameters from Parameter Store using the AWS Management Console, AWS CLI, or AWS SDKs to call the following API actions:

- [GetParameter](../APIReference/API_GetParameter.md "../APIReference/API_GetParameter.md")
- [GetParameters](../APIReference/API_GetParameters.md "../APIReference/API_GetParameters.md")
- [API_GetParametersByPath](../APIReference/API_GetParametersByPath.md "../APIReference/API_GetParametersByPath.md")

**AWS CLI**: The following table includes sample AWS CLI commands for Parameter Store.

| Command                | Usage                                                   | Best For                                                                                                                                                                           |
| ---------------------- | ------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| get-parameter          | aws ssm get-parameter --name "`name`"                   | Fetching one specific parameter value.                                                                                                                                             |
| get-parameter          | aws ssm get-parameter --name "`name`" --with-decryption | Fetching `SecureString` parameter types. Note – you must include the `--with-decryption` flag to see the plaintext value; otherwise, you will only receive the encrypted metadata. |
| get-parameters         | aws ssm get-parameters --names "`name1`" "`name2`"      | Fetching up to 10 specific, unrelated parameters at once.                                                                                                                          |
| get-parameters-by-path | aws ssm get-parameters-by-path --path "`/my/app/path/`" | Bulk retrieval of an entire environment's configuration.                                                                                                                           |
| get-parameter-history  | aws ssm get-parameter-history --name "`name`"           | Checking how a value has changed over time.                                                                                                                                        |

**SDKs (e.g., Boto3 for Python)**: Use methods like `get_parameter()` or `get_parameters_by_path()` within your application code to fetch values at runtime.

**CDK and CloudFormation**:

- **AWS CDK**: Use `valueForStringParameter` or `valueFromLookup` to read values during synthesis or deployment.
- **CloudFormation**: Use dynamic references like `{{resolve:ssm:parameter-name:version}}` to inject values directly into templates.

###### Note

For most dynamic parameter references, you specify the parameter name by using the following convention:

{{`ssm:`parameter-name``}}

To get started with Parameter Store, see [Setting up Parameter Store](parameter-store-setting-up.md "parameter-store-setting-up.md").
