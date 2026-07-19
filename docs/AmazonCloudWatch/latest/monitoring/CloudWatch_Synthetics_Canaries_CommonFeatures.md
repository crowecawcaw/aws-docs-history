# Common canary features

You can use the following features with all canary runtimes.

## Environment variables

You can use environment variables when you create canaries. You can write a
single canary script and use it with different values to quickly create
multiple canaries for a similar task.

For example, suppose your organization has endpoints such as `prod`,
`dev`, and `pre-release` for different software development stages.
You must create canaries to test each endpoint. You can
write a single canary script that tests your software. Then specify different
endpoint environment variable values when you create each of the three canaries. When
you create a canary, specify the script and the environment variable values.

The names of environment variables can contain letters, numbers, and the underscore
character. They must start with a letter and be at least two characters. The total size
of your environment variables can't exceed 4 KB. You can't specify any Lambda reserved
environment variables as the names of your environment variables. For more information
about reserved environment variables, see [Runtime environment variables](../../../lambda/latest/dg/configuration-envvars.md#configuration-envvars-runtime "../../../lambda/latest/dg/configuration-envvars.md#configuration-envvars-runtime").

###### Environment variables are not encrypted client-side

By default, AWS encrypts environment variable keys and values at rest
using an AWS owned key. However, CloudWatch Synthetics does not apply client-side
encryption. Store sensitive information only after encrypting it in transit. For more information, see [Encrypting environment variables in transit](#CloudWatch_Synthetics_transit_encryption "#CloudWatch_Synthetics_transit_encryption"). You can also use a customer managed AWS KMS key to encrypt your
canary's environment variables at rest. For more information, see [Encrypting environment variables at rest with a customer managed key](#CloudWatch_Synthetics_function_encryption "#CloudWatch_Synthetics_function_encryption").

The following example script uses two environment variables. This script is for a
canary that checks whether a webpage is available. It uses environment variables to
parameterize both the URL that it checks and the CloudWatch Synthetics log level that it uses.

The following snippets are part of the complete script shown below.

The following function sets `LogLevel` to the value of the `LOG_LEVEL` environment variable.

```
 synthetics.setLogLevel(process.env.LOG_LEVEL);
```

This function sets `URL` to the value of the `URL` environment
variable.

```
const URL = process.env.URL;
```

The following complete script demonstrates both environment variables. When you create a canary using this script, you specify
values for the `LOG_LEVEL` and `URL` environment variables.

```
var synthetics = require('@aws/synthetics-puppeteer');
const log = require('@aws/synthetics-logger');

const pageLoadEnvironmentVariable = async function () {

  // Setting the log level (0-3)
  synthetics.setLogLevel(process.env.LOG_LEVEL);
  // INSERT URL here
  const URL = process.env.URL;

  let page = await synthetics.getPage();
  //You can customize the wait condition here. For instance,
  //using 'networkidle2' may be less restrictive.
  const response = await page.goto(URL, {waitUntil: 'domcontentloaded', timeout: 30000});
  if (!response) {
      throw "Failed to load page!";
  }
  //Wait for page to render.
  //Increase or decrease wait time based on endpoint being monitored.
  await page.waitFor(15000);
  await synthetics.takeScreenshot('loaded', 'loaded');
  let pageTitle = await page.title();
  log.info('Page title: ' + pageTitle);
  log.debug('Environment variable:' + process.env.URL);

  //If the response status code is not a 2xx success code
  if (response.status() < 200 || response.status() > 299) {
      throw "Failed to load page!";
  }
};

exports.handler = async () => {
  return await pageLoadEnvironmentVariable();
};
```

### Passing environment variables to your script

To pass environment variables to your script when you create a canary in the
console, specify the keys and values of the environment variables in the **Environment
variables** section on the console. For more information, see [Creating a canary](CloudWatch_Synthetics_Canaries_Create.md "CloudWatch_Synthetics_Canaries_Create.md").

To pass environment variables through the API or AWS CLI, use the `EnvironmentVariables` parameter in the `RunConfig` section. The
following is an example AWS CLI command that creates a canary that uses two environment
variables with keys of `Environment` and `Region`.

```
aws synthetics create-canary --cli-input-json '{
 "Name":"nameofCanary",
 "ExecutionRoleArn":"roleArn",
 "ArtifactS3Location":"s3://amzn-s3-demo-bucket-123456789012-us-west-2",
 "Schedule":{
    "Expression":"rate(0 minute)",
    "DurationInSeconds":604800
 },
 "Code":{
    "S3Bucket": "canarycreation",
    "S3Key": "cwsyn-mycanaryheartbeat-12345678-d1bd-1234-abcd-123456789012-12345678-6a1f-47c3-b291-123456789012.zip",
    "Handler":"pageLoadBlueprint.handler"
 },
 "RunConfig": {
    "TimeoutInSeconds":60,
    "EnvironmentVariables": {
       "Environment":"Production",
       "Region": "us-west-1"
    }
 },
 "SuccessRetentionPeriodInDays":13,
 "FailureRetentionPeriodInDays":13,
 "RuntimeVersion":"syn-nodejs-2.0"
}'

```

## Encrypting environment variables at rest with a customer managed key

By default, an AWS owned key encrypts canary environment variables at rest.
You can specify a customer managed AWS KMS key to encrypt the
canary environment variables at rest. With a customer managed key, you have full control over the
encryption of sensitive configuration data. The following sections describe the requirements,
configuration steps, and permissions for using a customer managed key.

### Requirements

Before you configure a customer managed key, verify that you meet the following requirements:

- The AWS KMS key must be a symmetric encryption key.
- The key policy must grant `kms:CreateGrant` to the caller (the
  IAM principal calling the Synthetics API).
- AWS Lambda uses the grant to encrypt and decrypt the environment variables at
  rest.
- The AWS KMS key must be in the same AWS Region as the canary.

### Configuring a customer managed key

You can configure a customer managed key when you create or update a canary. The following procedures show how to configure encryption using the Amazon CloudWatch console and the Synthetics API.

#### Configure encryption in the console

To create or edit a canary in the Amazon CloudWatch console, expand the
**Environment variables** section. Under
**Encryption at rest configuration**, choose
**Use a customer managed key** and then choose or specify the ARN of
your AWS KMS key.

#### Configure encryption using the API

When calling `CreateCanary` or `UpdateCanary`, specify the
`KmsKeyArn` parameter with the ARN of your customer managed key.
To revert to the AWS managed key, set `KmsKeyArn` to an empty
string.

#### Example: CreateCanary request with a customer managed key

```
{
"Name": "my-canary-EXAMPLE",
"KmsKeyArn": "arn:aws:kms:us-east-1:111122223333:key/a1b2c3d4-e5f6-7890-abcd-EXAMPLE11111",
"RunConfig": {
  "EnvironmentVariables": {
    "SECRET_KEY": "my-secret-value-EXAMPLE"
  }
}
}
```

### Required permissions for at-rest encryption

If you create or update the canary, you must have the following permissions
on the AWS KMS key:

- `kms:CreateGrant`, `kms:Encrypt`—Required to configure a
  customer managed key for the canary.
- `kms:Decrypt`—Required to view and manage environment variables
  that are encrypted with a customer managed key.
- `kms:DescribeKey`—Required to validate the key.

The canary execution role requires no AWS KMS permissions for at-rest encryption.
Lambda uses the grant to handle encryption and decryption.

### Multi-location canaries

For multi-location canaries, each replica location can have its own AWS KMS key.
Specify the `KmsKeyArn` in the `AddReplicaLocations` parameter
when creating or updating a canary. The key must be in the same Region as the
replica.

## Encrypting environment variables in transit

In addition to encryption at rest, you can encrypt individual environment variable
values before CloudWatch Synthetics stores them. CloudWatch Synthetics calls this encryption in transit. When you encrypt a
value in transit, the console replaces the plaintext value with a base64-encoded ciphertext that
only your canary can decrypt at runtime.

### How encryption in transit works

When you choose to encrypt an environment variable value in transit:

1. The console calls `kms:Encrypt` with your selected AWS KMS key to
   encrypt the plaintext value.
2. The encrypted ciphertext (base64-encoded) replaces the plaintext value in the
   environment variable configuration.
3. At runtime, your canary script decrypts the value by calling
   `kms:Decrypt`.

### Required permissions for encryption in transit

You need the following permissions for encryption in transit:

- **Console user or API caller**—
  `kms:Encrypt` on the AWS KMS key. You need this permission to encrypt the
  value before storing it.
- **Canary execution role**—
  `kms:Decrypt` on the AWS KMS key. The canary's Lambda function needs this
  permission to decrypt the value at runtime.

The following is an example IAM policy to attach to the canary execution role:

```
{
"Version": "2012-10-17",
"Statement": [
  {
    "Effect": "Allow",
    "Action": "kms:Decrypt",
    "Resource": "arn:aws:kms:us-east-1:111122223333:key/a1b2c3d4-e5f6-7890-abcd-EXAMPLE11111"
  }
]
}
```

### Decrypting values in your canary script

To use an encrypted environment variable in your canary script, decrypt it at
runtime. The following Node.js example shows how to decrypt an environment
variable:

```
const { KMSClient, DecryptCommand } = require('@aws-sdk/client-kms');
const client = new KMSClient({ region: process.env.AWS_REGION });

async function decryptEnvVar(name) {
const encrypted = process.env[name];
const req = {
  CiphertextBlob: Buffer.from(encrypted, 'base64'),
};
const command = new DecryptCommand(req);
const response = await client.send(command);
return new TextDecoder().decode(response.Plaintext);
}

// Usage
const mySecret = await decryptEnvVar('MY_CONFIG_VAR');
```

## Integrating your canary with other AWS services

You can use the AWS SDK library in your canary to integrate with other AWS services.

To do so, add the following code to your canary. In these
examples, the canary integrates with AWS Secrets Manager.

- Import the AWS SDK.

```
const AWS = require('aws-sdk');
```

- Create a client for the AWS service that you are integrating with.

```
const secretsManager = new AWS.SecretsManager();
```

- Use the client to make API calls to that service.

```
var params = {
SecretId: secretName
};
return await secretsManager.getSecretValue(params).promise();
```

The following canary script code snippet shows how to integrate with
Secrets Manager in more detail.

```
var synthetics = require('@aws/synthetics-puppeteer');
const log = require('@aws/synthetics-logger');

const AWS = require('aws-sdk');
const secretsManager = new AWS.SecretsManager();

const getSecrets = async (secretName) => {
  var params = {
      SecretId: secretName
  };
  return await secretsManager.getSecretValue(params).promise();
}

const secretsExample = async function () {
  let URL = "<URL>";
  let page = await synthetics.getPage();

  log.info(`Navigating to URL: ${URL}`);
  const response = await page.goto(URL, {waitUntil: 'domcontentloaded', timeout: 30000});

  // Fetch secrets
  let secrets = await getSecrets("secretname")

  /**
  * Use secrets to login.
  *
  * Assuming secrets are stored in a JSON format like:
  * {
  *   "username": "<USERNAME>",
  *   "password": "<PASSWORD>"
  * }
  **/
  let secretsObj = JSON.parse(secrets.SecretString);
  await synthetics.executeStep('login', async function () {
      await page.type(">USERNAME-INPUT-SELECTOR<", secretsObj.username);
      await page.type(">PASSWORD-INPUT-SELECTOR<", secretsObj.password);

      await Promise.all([
        page.waitForNavigation({ timeout: 30000 }),
        await page.click(">SUBMIT-BUTTON-SELECTOR<")
      ]);
  });

  // Verify login was successful
  await synthetics.executeStep('verify', async function () {
      await page.waitForXPath(">SELECTOR<", { timeout: 30000 });
  });
};

exports.handler = async () => {
  return await secretsExample();
};
```

## Forcing your canary to use a static IP address

You can set up a canary so that it uses a static IP address.

###### To force a canary to use a static IP address

1. Create a new VPC. For more information, see [Using DNS with your VPC](../../../vpc/latest/userguide/vpc-dns.md "../../../vpc/latest/userguide/vpc-dns.md").
2. Create a new internet gateway. For more information, see [Adding an internet
   gateway to your VPC](../../../vpc/latest/userguide/VPC_Internet_Gateway.md#working-with-igw "../../../vpc/latest/userguide/VPC_Internet_Gateway.md#working-with-igw").
3. Create a public subnet inside your new VPC.
4. Add a new route table to the VPC.
5. Add a route in the new route table that goes from `0.0.0.0/0` to the
   internet gateway.
6. Associate the new route table with the public subnet.
7. Create an elastic IP address. For more information, see [Elastic IP addresses](../../../AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.md "../../../AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.md").
8. Create a new NAT gateway and assign it to the public subnet and the elastic IP
   address.
9. Create a private subnet inside the VPC.
10. Add a route to the VPC default route table that goes from `0.0.0.0/0`
    to the NAT gateway.
11. Create your canary.
