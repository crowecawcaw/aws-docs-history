# Get a Secrets Manager secret value using the PHP AWS SDK

For PHP applications, call the SDK directly with [`GetSecretValue`](../../../aws-sdk-php/v3/api/api-secretsmanager-2017-10-17.md#getsecretvalue "../../../aws-sdk-php/v3/api/api-secretsmanager-2017-10-17.md#getsecretvalue") or [`BatchGetSecretValue`](../../../aws-sdk-php/v3/api/api-secretsmanager-2017-10-17.md#batchGetsecretvalue "../../../aws-sdk-php/v3/api/api-secretsmanager-2017-10-17.md#batchGetsecretvalue").

The following code example shows how to get a Secrets Manager secret value.

**Required permissions:** `secretsmanager:GetSecretValue`

```
<?php

  /**
    * Use this code snippet in your app.
    *
    * If you need more information about configurations or implementing the sample code, visit the AWS docs:
    * https://aws.amazon.com/developer/language/php/
    */

  require 'vendor/autoload.php';

  use Aws\SecretsManager\SecretsManagerClient;
  use Aws\Exception\AwsException;

  /**
    * This code expects that you have AWS credentials set up per:
    * https://<<{{DocsDomain}}>>/sdk-for-php/v3/developer-guide/guide_credentials.html
    */

  // Create a Secrets Manager Client
  $client = new SecretsManagerClient([
      'profile' => 'default',
      'version' => '2017-10-17',
      'region' => '<<{{MyRegionName}}>>',
  ]);

  $secret_name = '<<{{MySecretName}}>>';

  try {
      $result = $client->getSecretValue([
          'SecretId' => $secret_name,
      ]);
  } catch (AwsException $e) {
      // For a list of exceptions thrown, see
      // https://<<{{DocsDomain}}>>/secretsmanager/latest/apireference/API_GetSecretValue.html
      throw $e;
  }

  // Decrypts secret using the associated KMS key.
  $secret = $result['SecretString'];

  // Your code goes here
```
