

# Using AWS Secrets Manager and AWS Systems Manager Parameter Store
<a name="AWSHowTo.secrets.Secrets-Manager-and-Parameter-Store"></a>

This topic provides a brief introduction of AWS Secrets Manager and AWS Systems Manager Parameter Store, pricing information, and references to learn more about creating and retrieving secrets, using both the console and programmatic options.

**About Secrets Manager**  
AWS Secrets Manager helps you manage, retrieve, and rotate secrets throughout their lifecycles. Examples of secret data you can manage include database credentials, application credentials, OAuth tokens, and API keys. Secrets Manager enables you to configure an automatic rotation schedule for your secrets.

**About Systems Manager Parameter Store**  
Parameter Store is a tool in AWS Systems Manager. It provides secure, hierarchical storage for configuration data management and secrets management. You can manage important configuration data as parameter values. Examples of data that you can manage with Parameter Store includes Amazon Machine Image (AMI) IDs, license codes, passwords, and database strings.

**Pricing**  
Standard charges apply for using Secrets Manager and Systems Manager Parameter Store. For more information about pricing, see the following websites:  
[AWS Secrets Manager pricing](https://aws.amazon.com/secrets-manager/pricing)
[AWS Systems Manager pricing](https://aws.amazon.com/systems-manager/pricing/) (select *Parameter Store* from the content list)

**Topics**
+ [Using Secrets Manager to create and retrieve secrets](#AWSHowTo.secrets.Secrets-Manager)
+ [Using Systems Manager Parameter Store to create and retrieve parameters](#AWSHowTo.secrets.SSM-parmameter-store)

## Using Secrets Manager to create and retrieve secrets
<a name="AWSHowTo.secrets.Secrets-Manager"></a>

You can create and retrieve Secrets Manager secrets using the AWS Secrets Manager console, the AWS CLI, or the AWS SDK. Refer to the following resources to learn more about different methods to create and retrieve Secrets Manager secrets.

**Creating secrets**
+ Console – [Create an AWS Secrets Manager secret (console)](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html) in the *AWS Secrets Manager User Guide* 
+ AWS CLI – [AWSCLI](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html#create_secret_cli) in the *AWS Secrets Manager User Guide* 
+ AWS SDK – [AWS SDK](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html#create_secret_sdk) in the *AWS Secrets Manager User Guide* 

**Retrieving secrets**
+ Console – [Get a secret value (console)](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets-console.html) in the *AWS Secrets Manager User Guide*
+ AWS CLI – [Get a secret value (AWS CLI)](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets_cli.html) in the *AWS Secrets Manager User Guide*
+ AWS SDK – [Code examples for Secrets Manager using AWS SDKs ](https://docs.aws.amazon.com/code-library/latest/ug/secrets-manager_code_examples.html) in the *AWS SDK Code Examples Code Library*
+ Other methods – [Get secrets from AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets.html) in the *AWS Secrets Manager User Guide* 

For more information about AWS Secrets Manager, see [What is AWS Secrets Manager?](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) in the *AWS Secrets Manager User Guide*.

## Using Systems Manager Parameter Store to create and retrieve parameters
<a name="AWSHowTo.secrets.SSM-parmameter-store"></a>

You can create and retrieve Parameter Store parameters using the AWS Systems Manager console, the AWS CLI, or the AWS SDK. Refer to the following resources to learn more about different methods to create and retrieve Parameter Store parameters.

**Creating parameters**
+ Console – [Create a Systems Manager parameter (console)](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-create-console.html) in the *AWS Systems Manager User Guide*
+ AWS CLI – [Create a Systems Manager parameter (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/param-create-cli.html) in the *AWS Systems Manager User Guide*
+ AWS SDK – [Use PutParameter with an AWS SDK or AWS CLI](https://docs.aws.amazon.com/code-library/latest/ug/ssm_example_ssm_PutParameter_section.html) in the *AWS SDK Code Examples Code Library*

**Retrieving parameters**
+ Console – [Searching for a parameter (console)](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-search.html#parameter-search-console) in the *AWS Systems Manager User Guide*
+ AWS CLI – [Use GetParameter with an AWS SDK or AWS CLI](https://docs.aws.amazon.com/code-library/latest/ug/ssm_example_ssm_GetParameter_section.html) in the *AWS SDK Code Examples Code Library*
+ AWS SDK – [Use GetParameter with an AWS SDK or AWS CLI](https://docs.aws.amazon.com/code-library/latest/ug/ssm_example_ssm_GetParameter_section.html) in the *AWS SDK Code Examples Code Library*

For more information, see [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) in the *AWS Systems Manager User Guide*.