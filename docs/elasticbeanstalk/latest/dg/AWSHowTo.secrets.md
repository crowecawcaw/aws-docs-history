# Using AWS Secrets Manager and AWS Systems Manager Parameter Store

This topic provides a brief introduction of AWS Secrets Manager and AWS Systems Manager Parameter Store, pricing information, and references to learn more about creating
and retrieving secrets, using both the console and programmatic options.

###### About Secrets Manager

AWS Secrets Manager helps you manage, retrieve, and rotate secrets throughout their lifecycles. Examples of secret data you can manage include database
credentials, application credentials, OAuth tokens, and API keys. Secrets Manager enables you to configure an automatic rotation schedule for your secrets.

###### About Systems Manager Parameter Store

Parameter Store is a tool in AWS Systems Manager. It provides secure, hierarchical storage for configuration data management and secrets management. You can
manage important configuration data as parameter values. Examples of data that you can manage with Parameter Store includes Amazon Machine Image (AMI)
IDs, license codes, passwords, and database strings.

###### Pricing

Standard charges apply for using Secrets Manager and Systems Manager
Parameter Store. For more information about pricing,
see the following websites:

- [AWS Secrets Manager pricing](https://aws.amazon.com/secrets-manager/pricing "https://aws.amazon.com/secrets-manager/pricing")
- [AWS Systems Manager pricing](https://aws.amazon.com/systems-manager/pricing/ "https://aws.amazon.com/systems-manager/pricing/") (select _Parameter Store_ from the content
  list)

###### Topics

- [Using Secrets Manager to create and retrieve secrets](#AWSHowTo.secrets.Secrets-Manager "#AWSHowTo.secrets.Secrets-Manager")
- [Using Systems Manager Parameter Store to create and retrieve parameters](#AWSHowTo.secrets.SSM-parmameter-store "#AWSHowTo.secrets.SSM-parmameter-store")

## Using Secrets Manager to create and retrieve secrets

You can create and retrieve Secrets Manager secrets using the AWS Secrets Manager console, the AWS CLI, or the AWS SDK. Refer to the following resources to learn more
about different methods to create and retrieve Secrets Manager secrets.

###### Creating secrets

- Console – [Create an AWS Secrets Manager secret
  (console)](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md") in the _AWS Secrets Manager User Guide_
- AWS CLI – [AWSCLI](../../../secretsmanager/latest/userguide/create_secret.md#create_secret_cli "../../../secretsmanager/latest/userguide/create_secret.md#create_secret_cli") in the
  _AWS Secrets Manager User Guide_
- AWS SDK – [AWS SDK](../../../secretsmanager/latest/userguide/create_secret.md#create_secret_sdk "../../../secretsmanager/latest/userguide/create_secret.md#create_secret_sdk") in
  the _AWS Secrets Manager User Guide_

###### Retrieving secrets

- Console – [Get a secret value
  (console)](../../../secretsmanager/latest/userguide/retrieving-secrets-console.md "../../../secretsmanager/latest/userguide/retrieving-secrets-console.md") in the _AWS Secrets Manager User Guide_
- AWS CLI – [Get a secret value
  (AWS CLI)](../../../secretsmanager/latest/userguide/retrieving-secrets_cli.md "../../../secretsmanager/latest/userguide/retrieving-secrets_cli.md") in the _AWS Secrets Manager User Guide_
- AWS SDK – [Code examples for Secrets Manager using
  AWS SDKs](../../../code-library/latest/ug/secrets-manager_code_examples.md "../../../code-library/latest/ug/secrets-manager_code_examples.md") in the _AWS SDK Code Examples Code Library_
- Other methods – [Get secrets from
  AWS Secrets Manager](../../../secretsmanager/latest/userguide/retrieving-secrets.md "../../../secretsmanager/latest/userguide/retrieving-secrets.md") in the _AWS Secrets Manager User Guide_

For more information about AWS Secrets Manager, see [What is AWS Secrets Manager?](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md") in
the _AWS Secrets Manager User Guide_.

## Using Systems Manager Parameter Store to create and retrieve parameters

You can create and retrieve Parameter Store parameters using the AWS Systems Manager console, the AWS CLI, or the AWS SDK. Refer to the following resources to
learn more about different methods to create and retrieve Parameter Store parameters.

###### Creating parameters

- Console – [Create a Systems Manager parameter
  (console)](../../../systems-manager/latest/userguide/parameter-create-console.md "../../../systems-manager/latest/userguide/parameter-create-console.md") in the _AWS Systems Manager User Guide_
- AWS CLI – [Create a Systems Manager parameter
  (AWS CLI)](../../../systems-manager/latest/userguide/param-create-cli.md "../../../systems-manager/latest/userguide/param-create-cli.md") in the _AWS Systems Manager User Guide_
- AWS SDK – [Use PutParameter with an
  AWS SDK or AWS CLI](../../../code-library/latest/ug/ssm_example_ssm_PutParameter_section.md "../../../code-library/latest/ug/ssm_example_ssm_PutParameter_section.md") in the _AWS SDK Code Examples Code Library_

###### Retrieving parameters

- Console – [Searching for
  a parameter (console)](../../../systems-manager/latest/userguide/parameter-search.md#parameter-search-console "../../../systems-manager/latest/userguide/parameter-search.md#parameter-search-console") in the _AWS Systems Manager User Guide_
- AWS CLI – [Use GetParameter with an
  AWS SDK or AWS CLI](../../../code-library/latest/ug/ssm_example_ssm_GetParameter_section.md "../../../code-library/latest/ug/ssm_example_ssm_GetParameter_section.md") in the _AWS SDK Code Examples Code Library_
- AWS SDK – [Use GetParameter with an
  AWS SDK or AWS CLI](../../../code-library/latest/ug/ssm_example_ssm_GetParameter_section.md "../../../code-library/latest/ug/ssm_example_ssm_GetParameter_section.md") in the _AWS SDK Code Examples Code Library_

For more information, see [AWS Systems Manager
Parameter Store](../../../systems-manager/latest/userguide/systems-manager-parameter-store.md "../../../systems-manager/latest/userguide/systems-manager-parameter-store.md") in the _AWS Systems Manager User Guide_.
