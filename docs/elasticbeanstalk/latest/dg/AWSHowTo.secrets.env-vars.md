

# Fetching secrets and parameters to Elastic Beanstalk environment variables
<a name="AWSHowTo.secrets.env-vars"></a>

Elastic Beanstalk can fetch values from AWS Secrets Manager and AWS Systems Manager Parameter Store during instance bootstrapping and assign them to environment variables for your application to use.

The following points summarize configuration, synchronization and access for using environment variables as secrets:
+ Configure your environment variables to store secrets by specifying the Amazon Resource Names (ARNs) for the secrets and parameters they will store.
+ When secret values are updated or rotated in Secrets Manager or Systems Manager Parameter Store, you must manually refresh your environment variables.
+ The secrets environment variables are available to [ebextension](platforms-linux-extend.config-files.md) container commands and [platform hooks](platforms-linux-extend.hooks.md).

**Supported platform versions**  
Platform versions that were released on or after [March 26, 2025](https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2025-03-26-windows.html) support AWS Secrets Manager secrets and AWS Systems Manager Parameter Store parameters configured as environment variables.

**Note**  
With the exception of the Docker and ECS based docker platforms, the Amazon Linux 2 platform versions don't support multiline variable values. For more information about multiline variable support, see [Multiline values](#AWSHowTo.secrets.multiline).

**Topics**
+ [Pricing](#AWSHowTo.secrets.pricing)
+ [Configure secrets as Elastic Beanstalk environment variables](#AWSHowTo.secrets.configure-env-vars)
+ [Extracting JSON keys from Secrets Manager secrets](#AWSHowTo.secrets.json)
+ [Best practices for secrets synchronization with Elastic Beanstalk environment variables](#AWSHowTo.secrets.rotating-secrets)
+ [Multiline values in Amazon Linux 2 environment variables](#AWSHowTo.secrets.multiline)

## Pricing
<a name="AWSHowTo.secrets.pricing"></a>

Standard charges apply for using Secrets Manager and Systems Manager Parameter Store. For more information about pricing, see the following websites:
+ [AWS Secrets Manager pricing](https://aws.amazon.com/secrets-manager/pricing)
+ [AWS Systems Manager pricing](https://aws.amazon.com/systems-manager/pricing/) (select *Parameter Store* from the content list)

Elastic Beanstalk doesn't charge for your application to reference environment secrets via environment variables. However, standard charges do apply to requests that Elastic Beanstalk makes to these services on your behalf.

## Configure secrets as Elastic Beanstalk environment variables
<a name="AWSHowTo.secrets.configure-env-vars"></a>

You can use the Elastic Beanstalk console, configuration files in `.ebextensions`, the AWS CLI, and the AWS SDK to configure secrets and parameters as environment variables. 

**Topics**
+ [Prerequisites](#AWSHowTo.secrets.configure-env-vars.prerequisites)
+ [Using the console](#AWSHowTo.secrets.configure-env-vars.console)
+ [Configuration using files in .ebextensions](#AWSHowTo.secrets.configure-env-vars.config-file)
+ [Configuration using the AWS CLI](#AWSHowTo.secrets.configure-env-vars.aws-cli)
+ [Configuration using the AWS SDK](#AWSHowTo.secrets.configure-env-vars.aws-sdk)

### Prerequisites
<a name="AWSHowTo.secrets.configure-env-vars.prerequisites"></a>

Before you can set up your environment variables to reference secrets you'll first need to complete the following steps.

**General procedure prior to environment variable configuration**

1. Create the Secrets Manager secrets or the Parameter Store parameters to store your sensitive data. For more information, see one or both of the following topics:
   + *Creating secrets* in [Using Secrets Manager to create and retrieve secrets](AWSHowTo.secrets.Secrets-Manager-and-Parameter-Store.md#AWSHowTo.secrets.Secrets-Manager)
   + *Creating parameters* in [Using Systems Manager Parameter Store to create and retrieve parameters](AWSHowTo.secrets.Secrets-Manager-and-Parameter-Store.md#AWSHowTo.secrets.SSM-parmameter-store)

1. Set up the required IAM permissions for your environment’s EC2 instances to fetch the secrets and parameters. For more information, see [Required IAM permissions](AWSHowTo.secrets.IAM-permissions.md).

### Using the console
<a name="AWSHowTo.secrets.configure-env-vars.console"></a>

You can use the Elastic Beanstalk console to configure secrets as environment variables.

**To configure secrets as environment variables in the Elastic Beanstalk console**

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk), and in the **Regions** list, select your AWS Region.

1. In the navigation pane, choose **Environments**, and then choose the name of your environment from the list.

1. In the navigation pane, choose **Configuration**.

1. In the **Updates, monitoring, and logging** configuration category, choose **Edit**.

1. Scroll down to **Runtime environment variables**.

1. Select **Add environment variable**.

1. For **Source** select either **Secrets Manager** or **SSM Parameter Store**.
**Note**  
For more information about the **Plain text** option in the drop-down, see [Configuring environment properties (environment variables)](environments-cfg-softwaresettings.md#environments-cfg-softwaresettings-console). 

1. For **Environment variable name** enter the name of the environment variable to hold the secret or parameter value.

1. For **Environment variable value** enter the ARN of the Systems Manager Parameter Store parameter or the Secrets Manager secret. During instance bootstrapping Elastic Beanstalk will initiate the value of the variable you entered in **Step 8** to the value stored in this ARN resource.

   The console validates if the value you enter is a valid ARN format for the store that you select in **Step 7**. However, it does not validate the existence of the resource specified by the ARN or if you have the [required IAM permissions](AWSHowTo.secrets.IAM-permissions.md) to access to it.

1. If you need to add more variables repeat **Step 6** through **Step 9**.

1. To save the changes choose **Apply** at the bottom of the page.

### Configuration using files in .ebextensions
<a name="AWSHowTo.secrets.configure-env-vars.config-file"></a>

You can use Elastic Beanstalk [configuration files](ebextensions.md) to configure secrets as environment variables. Use the [aws:elasticbeanstalk:application:environmentsecrets](command-options-general.md#command-options-general-elasticbeanstalk-application-environmentsecrets) namespace to define environment properties.

**Note**  
Secrets Manager automatically appends 6 random characters to secret names in the ARN format to ensure uniqueness.

**Example .ebextensions/options.config for environment secrets ([shorthand syntax](ebextensions-optionsettings.md#ebextensions-optionsettings.title))**  

```
option_settings:
  aws:elasticbeanstalk:application:environmentsecrets:
    MY_SECRET: arn:aws:secretsmanager:us-east-1:111122223333:secret:mysecret-AbCd12
    MY_PARAMETER: arn:aws:ssm:us-east-1:111122223333:parameter/myparam
```

**Example .ebextensions/options.config for environment secrets ([standard syntax](ebextensions-optionsettings.md#ebextensions-optionsettings.title))**  

```
option_settings:
  - namespace: aws:elasticbeanstalk:application:environmentsecrets
    option_name: MY_SECRET
    value: arn:aws:secretsmanager:us-east-1:111122223333:secret:mysecret-AbCd12
  - namespace: aws:elasticbeanstalk:application:environmentsecrets
    option_name: MY_PARAMETER
    value: arn:aws:ssm:us-east-1:111122223333:parameter/myparam
```

### Configuration using the AWS CLI
<a name="AWSHowTo.secrets.configure-env-vars.aws-cli"></a>

You can use the AWS Command Line Interface (AWS CLI) to configure secrets as Elastic Beanstalk environment variables. This section provides examples of the [create-environment](https://docs.aws.amazon.com/cli/latest/reference/elasticbeanstalk/create-environment.html) and [update-environment](https://docs.aws.amazon.com/cli/latest/reference/elasticbeanstalk/update-environment.html) commands with the [aws:elasticbeanstalk:application:environmentsecrets](command-options-general.md#command-options-general-elasticbeanstalk-application-environmentsecrets) namespace. When Elastic Beanstalk bootstraps the EC2 instances for the environments that these command reference, it initializes the environment variables with the fetched secret and the parameter values. It fetches these values from the respective ARNs of Secrets Manager and Systems Manager Parameter Store.

 

The two following examples use the [create-environment](https://docs.aws.amazon.com/cli/latest/reference/elasticbeanstalk/create-environment.html) command to add a secret and a parameter, configured as environment variables named `MY_SECRET`and `MY_PARAMETER`. 

**Example of create-environment with secrets configured as environment variables (namespace options inline)**  

```
aws elasticbeanstalk create-environment \
--region us-east-1 \
--application-name my-app \
--environment-name my-env \
--platform-arn "arn:aws:elasticbeanstalk:::platform/Node.js 24 running on 64bit Amazon Linux 2023" \
--option-settings \
Namespace=aws:autoscaling:launchconfiguration,OptionName=IamInstanceProfile,Value=aws-elasticbeanstalk-ec2-role \
Namespace=aws:elasticbeanstalk:application:environmentsecrets,OptionName=MY_SECRET,Value=arn:aws:secretsmanager:us-east-1:111122223333:secret:mysecret-AbCd12 \
Namespace=aws:elasticbeanstalk:application:environmentsecrets,OptionName=MY_PARAMETER,Value=arn:aws:ssm:us-east-1:111122223333:parameter/myparam
```



As an alternative, use an `options.json` file to specify the namespace options instead of including them inline.

**Example of create-environment with secrets configured as environment variables (namespace options in `options.json` file)**  

```
aws elasticbeanstalk create-environment \
--region us-east-1 \
--application-name my-app \
--environment-name my-env \
--platform-arn "arn:aws:elasticbeanstalk:::platform/Node.js 24 running on 64bit Amazon Linux 2023" \
--option-settings file://options.json
```

**Example**  

```
### example options.json ###
[
  {
    "Namespace": "aws:autoscaling:launchconfiguration",
    "OptionName": "IamInstanceProfile",
    "Value": "aws-elasticbeanstalk-ec2-role"
  },
  {
    "Namespace": "aws:elasticbeanstalk:application:environmentsecrets",
    "OptionName": "MY_SECRET",
    "Value": "arn:aws:secretsmanager:us-east-1:111122223333:secret:mysecret-AbCd12"
  },
  {
    "Namespace": "aws:elasticbeanstalk:application:environmentsecrets",
    "OptionName": "MY_PARAMETER",
    "Value": "arn:aws:ssm:us-east-1:111122223333:parameter/myparam"
  }
]
```





The next example configures environment variables, named `MY_SECRET`and `MY_PARAMETER`, to store a secret and a parameter for an existing environment. The [update-environment](https://docs.aws.amazon.com/cli/latest/reference/elasticbeanstalk/update-environment.html) command passes options with the same syntax as the `create-environment` command, either inline or with an `options.json` file. The following example demonstrates the command using the same `options.json` file that's also used in the previous example.



**Example of update-environment with secrets configured as environment variables (namespace options in `options.json` file)**  

```
aws elasticbeanstalk update-environment \
--region us-east-1 \
--application-name my-app \
--environment-name my-env \
--platform-arn "arn:aws:elasticbeanstalk:::platform/Node.js 24 running on 64bit Amazon Linux 2023" \
--option-settings file://options.json
```

### Configuration using the AWS SDK
<a name="AWSHowTo.secrets.configure-env-vars.aws-sdk"></a>

You can configure secrets and parameters as environment variables using the [AWS SDKs](https://docs.aws.amazon.com/code-library/). Similar to the `update-environment` and `create-environment` AWS CLI commands mentioned in the previous section, you can use the [CreateEnvironment](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CreateEnvironment.html) and [UpdateEnvironment](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_UpdateEnvironment.html) API actions. Use the `OptionSettings` request parameter to specify the options of the [aws:elasticbeanstalk:application:environmentsecrets](command-options-general.md#command-options-general-elasticbeanstalk-application-environmentsecrets) namespace.

## Extracting JSON keys from Secrets Manager secrets
<a name="AWSHowTo.secrets.json"></a>

Platform versions that were released on or after [January 13, 2026](https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2026-01-13-al2023.html) support extracting specific fields from JSON-formatted Secrets Manager secrets by appending a colon and the JSON key name to the secret ARN. This allows you to reference individual key-value pairs within a secret rather than the entire secret.

### Syntax
<a name="AWSHowTo.secrets.json.syntax"></a>

To extract a specific JSON key from a secret, append `:json-key-name` to the secret ARN:

```
arn:aws:secretsmanager:{{region}}:{{account}}:secret:{{secret-name-XXXXXX}}:{{json-key-name}}
```

JSON key extraction can be configured using the same methods as regular environment secrets: console, configuration files in `.ebextensions`, AWS CLI, or AWS SDKs.

### Limitations
<a name="AWSHowTo.secrets.json.limitations"></a>
+ JSON key extraction is only supported for Secrets Manager secrets, **not** Systems Manager Parameter Store parameters.
+ Only top-level JSON keys are supported. Nested key access (e.g., `config.database.host`) and array indexing (e.g., `servers[0]`) are **not** supported. If you need to access nested values, extract the parent object and parse it in your application code. Nested objects and arrays accessed using the top-level key are serialized back to JSON format.
+ JSON key names cannot contain colon (`:`) characters. Colons are reserved as delimiters in the ARN syntax. If a JSON key name contains a colon, only the portion before the first colon is used as the key name, and any characters after the colon are ignored.
+ The ECS managed Docker platform uses the native ECS syntax for referencing secrets. For more information, see [Pass Secrets Manager secrets through Amazon ECS environment variables](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/secrets-envvar-secrets-manager.html) in the *Amazon Elastic Container Service Developer Guide*.

### Example
<a name="AWSHowTo.secrets.json.example"></a>

The following example demonstrates how different value types are extracted from a JSON secret. Given this secret:

```
{
  "stringKey": "value1",
  "numberKey": 42,
  "objectKey": {
    "nested": "data"
  },
  "arrayKey": ["item1", "item2"]
}
```

You can configure the extraction in `.ebextensions`:

**Example .ebextensions example with JSON key extraction**  

```
option_settings:
  aws:elasticbeanstalk:application:environmentsecrets:
    STRING_VAR: arn:aws:secretsmanager:us-east-1:111122223333:secret:mysecret-AbCd12:stringKey
    NUMBER_VAR: arn:aws:secretsmanager:us-east-1:111122223333:secret:mysecret-AbCd12:numberKey
    OBJECT_VAR: arn:aws:secretsmanager:us-east-1:111122223333:secret:mysecret-AbCd12:objectKey
    ARRAY_VAR: arn:aws:secretsmanager:us-east-1:111122223333:secret:mysecret-AbCd12:arrayKey
```

This results in the following environment variables:
+ `STRING_VAR=value1`
+ `NUMBER_VAR=42`
+ `OBJECT_VAR={"nested":"data"}`
+ `ARRAY_VAR=["item1","item2"]`

## Best practices for secrets synchronization with Elastic Beanstalk environment variables
<a name="AWSHowTo.secrets.rotating-secrets"></a>

This topic recommends best practices for your application to use environment secrets with Secrets Manager or the Systems Manager Parameter Store. Your Elastic Beanstalk application won't automatically receive updated values if the secret store data is updated or rotated. Elastic Beanstalk only pulls secrets into environment variables at the time of instance bootstrapping. 

### Refreshing your environment variables
<a name="AWSHowTo.secrets.rotating-secrets.refresh-env-vars"></a>

To trigger your Elastic Beanstalk environment to refetch the latest values of the secrets from their secret stores, we recommend that you run either the `UpdateEnvironment` or `RestartAppServer` operation. You can run these operations using the Elastic Beanstalk console, the AWS CLI, or the Elastic Beanstalk API. For more information, see [*AWS CLI examples for Elastic Beanstalk*](https://docs.aws.amazon.com/cli/latest/userguide/cli_elastic-beanstalk_code_examples.html), or the [AWS Elastic Beanstalk API Reference](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/).

### Managing auto scaling effects on secret synchronization
<a name="AWSHowTo.secrets.rotating-secrets.as-effects"></a>

If a scale out event or instance replacement occurs after the secret store updates, the new instance that comes up will have the latest secret values from Secrets Manager or Systems Manager Parameter Store. Such an event can occur even if not all the other instances in the environment have been refreshed to retrieve the new secrets. 

**Important**  
You must ensure that your application is able to use two different secret values for the same environment variable. This accommodates events where a secret update occurs in Secrets Manager or Systems Manager Parameter Store, followed by a scale out or instance replacement in your environment, while the other instances are pending environment variable refresh. During the wait period for refresh, not all of the environment instances will have the same values for the secret store environment variables.

An example of such a use case is a database credential rotation. When a scale out event follows the credential rotation, the environment secrets referenced by the newly bootstrapped instances contain the updated database credentials. However, the environment secrets referenced by the existing instances retain the old value until they are refreshed by the `UpdateEnvironment` or `RestartAppServer` operations.

## Multiline values in Amazon Linux 2 environment variables
<a name="AWSHowTo.secrets.multiline"></a>

*Multiline* values are composed of more than one line and include a newline character. With the exception of Docker and ECS-based Docker platforms, platforms that run on Amazon Linux 2 don't support multiline values for environment variables

**Note**  
Elastic Beanstalk will fail the deployment of affected environments if it detects a multiline value.



The following options can serve as workarounds or solutions to the multiline issue:
+ Upgrade your Amazon Linux 2 environment to Amazon Linux 2023. For more information, see [Migration from Amazon Linux 2 to Amazon Linux 2023](using-features.migration-al.generic.from-al2.md).
+ Remove newline characters from your secret values. One example approach is to Base64 encode your values before storing them in the secret store. Your application would then need to decode the value back into the original format when it references it from the environment secret variable.
+ Design your application code to retrieve the data directly from Secrets Manager or Systems Manager Parameter Store. For more information, see *Retrieving secrets* in [Using Secrets Manager](AWSHowTo.secrets.Secrets-Manager-and-Parameter-Store.md#AWSHowTo.secrets.Secrets-Manager) or *Retrieving parameters* [Using Systems Manager Parameter Store](AWSHowTo.secrets.Secrets-Manager-and-Parameter-Store.md#AWSHowTo.secrets.SSM-parmameter-store).