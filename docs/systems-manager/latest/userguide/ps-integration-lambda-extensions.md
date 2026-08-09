# Using Parameter Store parameters in AWS Lambda functions

Parameter Store enables you to securely store, organize, and retrieve configuration data at scale. It supports a wide range of use cases, from managing plain-text configuration values – such as database connection strings and application settings – to handling sensitive data like secrets for low-risk environments. Parameter Store is designed to simplify configuration management across environments, allowing teams to standardize how applications access critical data without hardcoding values or relying on fragmented storage solutions.

If you manage credentials that require automatic rotation, cross-account access, or fine-grained audit logging, we recommend using [AWS Secrets Manager](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md"). Secrets Manager is purpose-built for managing secrets such as database credentials, API keys, and supported third-party software-vended secrets. For more information, see [What is AWS Secrets Manager?](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md") in the _AWS Secrets Manager User Guide_.

To use Parameter Store parameters in AWS Lambda functions without using an SDK, you can use
the AWS Parameters and Secrets Lambda Extension. This extension retrieves parameter values
and caches them for future use. Using the Lambda extension can reduce your costs by reducing
the number of API calls to Parameter Store. Using the extension can also
improve latency because retrieving a cached parameter is faster than retrieving it from
Parameter Store.

A Lambda extension is a companion process that augments the capabilities of a Lambda
function. An extension is like a client that runs in parallel to a Lambda invocation. This
parallel client can interface with your function at any point during its lifecycle. For more
information about Lambda extensions, see [Lambda Extensions API](../../../lambda/latest/dg/runtimes-extensions-api.md "../../../lambda/latest/dg/runtimes-extensions-api.md") in the
_AWS Lambda Developer Guide_.

The AWS Parameters and Secrets Lambda Extension works for both Parameter Store and AWS Secrets Manager. To
learn how to use the Lambda extension with secrets from Secrets Manager, see [Use AWS Secrets Manager
secrets in AWS Lambda functions](../../../secretsmanager/latest/userguide/retrieving-secrets_lambda.md "../../../secretsmanager/latest/userguide/retrieving-secrets_lambda.md") in the _AWS Secrets Manager User Guide_.

**Related info**

[Using the AWS Parameter and Secrets Lambda extension to cache parameters and
secrets](https://aws.amazon.com/blogs/compute/using-the-aws-parameter-and-secrets-lambda-extension-to-cache-parameters-and-secrets/ "https://aws.amazon.com/blogs/compute/using-the-aws-parameter-and-secrets-lambda-extension-to-cache-parameters-and-secrets/") (AWS Compute Blog)

## How the extension works

To use parameters in a Lambda function _without_ the Lambda
extension, you must configure your Lambda function to receive configuration updates by
integrating with the `GetParameter` API action for Parameter Store.

When you use the AWS Parameters and Secrets Lambda Extension, the extension retrieves
the parameter value from Parameter Store and stores it in the local cache. Then, the cached
value is used for further invocations until it expires. Cached values expire after they
pass their time-to-live (TTL). You can configure the TTL value using the
`SSM_PARAMETER_STORE_TTL`
[environment variable](#ps-integration-lambda-extensions-config "#ps-integration-lambda-extensions-config"), as
explained later in this topic.

If the configured cache TTL has not expired, the cached parameter value is used. If
the time has expired, the cached value is invalidated and the parameter value is
retrieved from Parameter Store.

Also, the system detects parameter values that are used frequently and maintains them
in the cache while clearing those that are expired or unused.

###### Important

The extension can be invoked only in the `INVOKE` phase of the Lambda
operation and not during the `INIT` phase.

### Implementation details

Use the following details to help you configure the AWS Parameters and Secrets
Lambda Extension.

Authentication

To authorize and authenticate Parameter Store requests, the extension uses
the same credentials as those used to run the Lambda function itself.
Therefore, the AWS Identity and Access Management (IAM) role used to run the function must have
the following permissions to interact with Parameter Store:

- `ssm:GetParameter` – Required to retrieve
  parameters from Parameter Store
- `kms:Decrypt` – Required if you are
  retrieving `SecureString` parameters from
  Parameter Store

For more information, see [AWS Lambda
execution role](../../../lambda/latest/dg/lambda-intro-execution-role.md "../../../lambda/latest/dg/lambda-intro-execution-role.md") in the
_AWS Lambda Developer Guide_.

Instantiation

For most Lambda functions, Lambda creates separate instances
corresponding to the concurrency level that your function requires. Each
instance is isolated and maintains its own local cache of your
configuration data. For more information about Lambda instances and
concurrency, see [Configuring
reserved concurrency](../../../lambda/latest/dg/configuration-concurrency.md "../../../lambda/latest/dg/configuration-concurrency.md") in the
_AWS Lambda Developer Guide_.

For functions that use Lambda Managed Instances, a single execution
environment serves multiple concurrent invocations, so those
invocations share one instance of the extension and one local cache.
For more information, see [Lambda Managed
Instances](../../../lambda/latest/dg/lambda-managed-instances.md "../../../lambda/latest/dg/lambda-managed-instances.md") in the _AWS Lambda Developer Guide_.

No SDK dependence

The AWS Parameters and Secrets Lambda Extension works independently
of any AWS SDK language library. An AWS SDK is not required to make
GET requests to Parameter Store. However, we recommend using an AWS SDK to
retrieve the session token for the request header, as described later
in this topic.

Localhost port

Use `localhost` in your GET requests. The extension makes
requests to localhost port 2773. You do not need to
specify an external or internal endpoint to use the extension. You can
configure the port by setting the [environment
variable](#ps-integration-lambda-extensions-config "#ps-integration-lambda-extensions-config")
`PARAMETERS_SECRETS_EXTENSION_HTTP_PORT`.

For example, in Python, your GET URL might look something like the
following example.

```
parameter_url = ('http://localhost:' + port + '/systemsmanager/parameters/get/?name=' + ssm_parameter_path)
```

Changes to a parameter value before TTL expires

The extension doesn't detect changes to the parameter value and
doesn't perform an auto-refresh before the TTL expires. If you change a
parameter value, operations that use the cached parameter value might
fail until the cache is next refreshed. If you expect frequent changes
to a parameter value, we recommend setting a shorter TTL value.

Header requirement

To retrieve parameters from the extension cache, the header of your
GET request must include an `X-Aws-Parameters-Secrets-Token`
reference. Set the token to your function's session token. For most
functions, this is provided in the `AWS_SESSION_TOKEN`
environment variable. However, Lambda doesn't set this environment
variable in all initialization modes. For example, if your function
uses SnapStart, it obtains credentials from a container endpoint
instead. To retrieve the session token reliably across all
initialization modes, read the token from the credential provider
chain of an AWS SDK instead of from the environment variable.
This header indicates that the request originates from within the
Lambda environment.

Example

The following example in Python demonstrates a basic request to
retrieve the value of a cached parameter. Resolve the session token
inside the handler function, not at initialization time, so the token
stays fresh after a SnapStart restore.

```
import urllib.request
import urllib.error
import json
import boto3

def lambda_handler(event, context):
    # Resolve the session token from the credential provider chain so that this
    # works across all initialization modes, including SnapStart.
    credentials = boto3.Session().get_credentials()
    if credentials is None:
        raise RuntimeError('Failed to resolve AWS credentials')
    session_token = credentials.get_frozen_credentials().token

    # Retrieve /my/parameter from Parameter Store using extension cache
    req = urllib.request.Request('http://localhost:2773/systemsmanager/parameters/get?name=%2Fmy%2Fparameter')
    req.add_header('X-Aws-Parameters-Secrets-Token', session_token)
    try:
        config = urllib.request.urlopen(req).read()
    except urllib.error.URLError as e:
        raise RuntimeError('Failed to retrieve parameter') from e

    return json.loads(config)

```

ARM support

The extension supports the ARM architecture in most AWS Regions
where the x86\_64 and x86 architectures are supported. If you
are using the ARM architecture, we suggest you verify your architecture
is supported. For complete lists of extension ARNs, see [AWS Parameters and Secrets Lambda Extension ARNs](#ps-integration-lambda-extensions-add "#ps-integration-lambda-extensions-add").

Logging

Lambda logs execution information about the extension along with the
function by using Amazon CloudWatch Logs. By default, the extension logs a minimal
amount of information to CloudWatch. To log more details, set the [environment
variable](#ps-integration-lambda-extensions-config "#ps-integration-lambda-extensions-config")
`PARAMETERS_SECRETS_EXTENSION_LOG_LEVEL` to
`DEBUG`.

### Adding the extension to a Lambda function

To use the AWS Parameters and Secrets Lambda Extension, you add the extension to
your Lambda function as a layer.

Use one of the following methods to add the extension to your function.

AWS Management Console (Add layer option)

1. Open the AWS Lambda console at
   [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").
2. Choose your function. In the **Layers** area,
   choose **Add a layer**.
3. In the **Choose a layer** area, choose the
   **AWS layers** option.
4. For **AWS layers**, choose
   **AWS-Parameters-and-Secrets-Lambda-Extension**,
   choose a version, and then choose
   **Add**.

AWS Management Console (Specify ARN option)

1. Open the AWS Lambda console at
   [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").
2. Choose your function. In the **Layers** area,
   choose **Add a layer**.
3. In the **Choose a layer** area, choose the
   **Specify an ARN** option.
4. For **Specify an ARN**, enter the [extension ARN
   for your AWS Region and architecture](#ps-integration-lambda-extensions-add "#ps-integration-lambda-extensions-add"), and then
   choose **Add**.

AWS Command Line Interface

Run the following command in the AWS CLI. Replace each
`example resource placeholder` with your
own information.

```
aws lambda update-function-configuration \
    --function-name `function-name` \
    --layers `layer-ARN`
```

**Related information**

[Using
layers with your Lambda function](../../../lambda/latest/dg/invocation-layers.md "../../../lambda/latest/dg/invocation-layers.md")

[Configuring
extensions (.zip file archive)](../../../lambda/latest/dg/using-extensions.md#using-extensions-config "../../../lambda/latest/dg/using-extensions.md#using-extensions-config")

## AWS Parameters and Secrets Lambda Extension environment variables

You can configure the extension by changing the following environment variables. To
see the current settings, set `PARAMETERS_SECRETS_EXTENSION_LOG_LEVEL` to
`DEBUG`. For more information, see [Using AWS Lambda environment
variables](../../../lambda/latest/dg/configuration-envvars.md "../../../lambda/latest/dg/configuration-envvars.md") in the _AWS Lambda Developer Guide_.

###### Note

AWS Lambda records operation details about the Lambda extension and Lambda function
in Amazon CloudWatch Logs.

| Environment variable                           | Details                                                                                                                                                                                                                                                                                                       | Required | Valid values                     | Default value        |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | -------------------------------- | -------------------- |
| `SSM_PARAMETER_STORE_TIMEOUT_MILLIS`           | Timeout, in milliseconds, for requests to Parameter Store.<br>A value of 0 (zero) indicates no timeout.                                                                                                                                                                                                       | No       | All whole numbers                | 0 (zero)             |
| `SECRETS_MANAGER_TIMEOUT_MILLIS`               | Timeout, in milliseconds, for requests to Secrets Manager.<br>A value of 0 (zero) indicates no timeout.                                                                                                                                                                                                       | No       | All whole numbers                | 0 (zero)             |
| `SSM_PARAMETER_STORE_TTL`                      | Maximum valid lifetime, in seconds, of a parameter in the cache<br>before it is invalidated. A value of 0 (zero) indicates that the<br>cache should be bypassed. This variable is ignored if the value for<br>`PARAMETERS_SECRETS_EXTENSION_CACHE_SIZE` is 0<br>(zero).                                       | No       | 0 (zero) to 300 s (Five minutes) | 300 s (Five minutes) |
| `SECRETS_MANAGER_TTL`                          | Maximum valid lifetime, in seconds, of a secret in the cache<br>before it is invalidated. A value of 0 (zero) indicates that the<br>cache is bypassed. This variable is ignored if the value for<br>`PARAMETERS_SECRETS_EXTENSION_CACHE_SIZE` is 0<br>(zero).                                                 | No       | 0 (zero) to 300 s (Five minutes) | 300 s (5 minutes)    |
| `PARAMETERS_SECRETS_EXTENSION_CACHE_ENABLED`   | Determines whether the cache for the extension is enabled. Value<br>values: `TRUE                                                                                                                                                                                                                             | FALSE`   | No                               | TRUE                 | FALSE | TRUE |
| `PARAMETERS_SECRETS_EXTENSION_CACHE_SIZE`      | The maximum size of the cache in terms of number of items. A value<br>of 0 (zero) indicates that the cache is bypassed. This variable is<br>ignored if both cache TTL values are 0 (zero).                                                                                                                    | No       | 0 (zero) to 1000                 | 1000                 |
| `PARAMETERS_SECRETS_EXTENSION_HTTP_PORT`       | The port for the local HTTP server.                                                                                                                                                                                                                                                                           | No       | 1<br>• 65535                     | 2773                 |
| `PARAMETERS_SECRETS_EXTENSION_MAX_CONNECTIONS` | Maximum number of connections for the HTTP clients that the<br>extension uses to make requests to Parameter Store or Secrets Manager. This is a<br>per-client configuration for the number of connections that both the<br>Secrets Manager client and Parameter Store client make to the backend<br>services. | No       | Minimum of 1; No maximum limit.  | 3                    |
| `PARAMETERS_SECRETS_EXTENSION_LOG_LEVEL`       | The level of detail reported in logs for the extension.<br>We recommend using `DEBUG` for the most detail about<br>your cache configuration as you set up and test the extension.<br>Logs for Lambda operations are automatically pushed to an<br>associated CloudWatch Logs log group.                       | No       | `DEBUG                           | WARN                 | ERROR | NONE | INFO` | `INFO` |

## Sample commands for using the AWS Systems Manager Parameter Store and AWS Secrets Manager Extension

The examples in this section demonstrate API actions for use with the AWS Systems Manager
Parameter Store and AWS Secrets Manager extension.

### Sample commands for Parameter Store

The Lambda extension uses read-only access to the **GetParameter** API action.

To call this action, make an HTTP GET call similar to the following. This command
format provides access to parameters in the standard parameter tier.

```
GET http://localhost:`port`/systemsmanager/parameters/get?name=`parameter-name`&version=`version`&label=`label`&withDecryption={true|false}
```

In this example, `parameter-name` represents the full
parameter name. For a parameter not in a hierarchy, use a name like
`MyParameter`. For a hierarchical parameter, use the URL-encoded path,
such as `%2FDev%2FProduction%2FEast%2FProject-ABC%2FMyParameter`
for `/Dev/Production/East/Project-ABC/MyParameter`.

###### Note

When using GET calls, parameter values must be encoded for HTTP to preserve
special characters. For example, instead of formatting a hierarchical path like
`/a/b/c`, encode characters that could be interpreted as part of
the URL, such as `%2Fa%2Fb%2Fc`.

`version` and `label` are the
selectors available for use with the `GetParameter` action.

```
GET http://localhost:`port`/systemsmanager/parameters/get/?name=MyParameter&version=5
```

To call a parameter in a hierarchy, make an HTTP GET call similar to the
following.

```
GET http://localhost:`port`/systemsmanager/parameters/get?name=%2Fa%2Fb%2F&label=release
```

To call a public (global) parameter, make an HTTP GET call similar to the
following.

```
GET http://localhost:`port`/systemsmanager/parameters/get/?name=%2Faws%2Fservice%20list%2F…
```

To make an HTTP GET call to a Secrets Manager secret by using Parameter Store references, make an
HTTP GET call similar to the following.

```
GET http://localhost:`port`/systemsmanager/parameters/get?name=%2Faws%2Freference%2Fsecretsmanager%2F…
```

To make a call using the Amazon Resource Name (ARN) for a parameter, make an HTTP
GET call similar to the following.

```
GET http://localhost:`port`/systemsmanager/parameters/get?name=arn:aws:ssm:us-east-1:123456789012:parameter/MyParameter
```

To make a call that accesses a `SecureString` parameter with
decryption, make an HTTP GET call similar to the following.

```
GET http://localhost:`port`/systemsmanager/parameters/get?name=MyParameter&withDecryption=true
```

You can specify that parameters aren't decrypted by omitting
`withDecryption` or explicitly setting it to `false`. You
can also specify either a version or a label, but not both. If you do, only the
first of these that is placed after question mark (`?`) in the URL is
used.

## AWS Parameters and Secrets Lambda Extension ARNs

The latest Amazon Resource Name (ARN) for the Lambda extension is published as a public parameter in Systems Manager Parameter Store for each supported architecture. You can retrieve the latest ARN programmatically using the AWS CLI or CloudFormation to ensure that your application always references the most recent extension version without manual updates. This section explains how to retrieve the ARN programmatically and provides tables listing the current ARN values for each architecture for manual reference.

### Retrieving the latest Lambda extension ARN version

The latest Lambda extension ARN versions are stored as public parameters in the following locations. You can reference these public parameters in your code to retrieve them:

- **x86\_64**: /aws/service/aws-parameters-and-secrets-lambda-extension/x86/latest
- **arm64**: /aws/service/aws-parameters-and-secrets-lambda-extension/arm64/latest

###### AWS CLI

To retrieve the latest ARN versions using the AWS CLI, run the following commands.

**x86\_64**

```
aws ssm get-parameter --name "/aws/service/aws-parameters-and-secrets-lambda-extension/x86/latest" --query "Parameter.Value" --output text
```

**arm64**

```
aws ssm get-parameter --name "/aws/service/aws-parameters-and-secrets-lambda-extension/arm64/latest" --query "Parameter.Value" --output text
```

###### AWS CloudFormation

When deploying Lambda functions using CloudFormation, you can resolve parameters directly during stack creation and updates, as shown in the following example YAML templates. This method ensures your
function always uses the latest extension version without requiring manual updates.

**x86\_64**

```
Resources:
  MyFunction:
    Type: AWS::Lambda::Function
    Properties:
      FunctionName: my-function
      Runtime: python3.11
      Handler: index.handler
      Code:
        ZipFile: |
          def handler(event, context):
              return {'statusCode': 200}
      Layers:
        - !Sub '{{resolve:ssm:/aws/service/aws-parameters-and-secrets-lambda-extension/x86/latest}}'
      Role: !GetAtt MyFunctionRole.Arn
```

**arm64**

```
Layers:
  - !Sub '{{resolve:ssm:/aws/service/aws-parameters-and-secrets-lambda-extension/arm64/latest}}'
```

###### Note

The `{{resolve:ssm:parameter-name}}` syntax automatically retrieves the parameter value during stack operations. This ensures you always deploy with the
current ARN.

### Latest extension ARNs

The following tables provide extension ARNs for supported architectures and
Regions.

###### Topics

- [Extension ARNs for the x86\_64 and x86 architectures](#intel "#intel")
- [Extension ARNs for ARM64 and Mac with Apple silicon architectures](#arm64 "#arm64")

#### Extension ARNs for the x86\_64 and x86 architectures

Last updated: July 28, 2026

| Region                                 | ARN                                                                                                     |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| US East (Ohio)                         | `arn:aws:lambda:us-east-2:590474943231:layer:AWS-Parameters-and-Secrets-Lambda-Extension:109`           |
| US East (N. Virginia)                  | `arn:aws:lambda:us-east-1:177933569100:layer:AWS-Parameters-and-Secrets-Lambda-Extension:99`            |
| US West (N. California)                | `arn:aws:lambda:us-west-1:997803712105:layer:AWS-Parameters-and-Secrets-Lambda-Extension:96`            |
| US West (Oregon)                       | `arn:aws:lambda:us-west-2:345057560386:layer:AWS-Parameters-and-Secrets-Lambda-Extension:99`            |
| Africa (Cape Town)                     | `arn:aws:lambda:af-south-1:317013901791:layer:AWS-Parameters-and-Secrets-Lambda-Extension:100`          |
| Asia Pacific (Hong Kong)               | `arn:aws:lambda:ap-east-1:768336418462:layer:AWS-Parameters-and-Secrets-Lambda-Extension:97`            |
| Asia Pacific (Taipei)                  | `arn:aws:lambda:ap-east-2:890742577149:layer:AWS-Parameters-and-Secrets-Lambda-Extension:69`            |
| Asia Pacific (Hyderabad) Region        | `arn:aws:lambda:ap-south-2:070087711984:layer:AWS-Parameters-and-Secrets-Lambda-Extension:91`           |
| Asia Pacific (Jakarta)                 | `arn:aws:lambda:ap-southeast-3:490737872127:layer:AWS-Parameters-and-Secrets-Lambda-Extension:94`       |
| Asia Pacific (Melbourne)               | `arn:aws:lambda:ap-southeast-4:090732460067:layer:AWS-Parameters-and-Secrets-Lambda-Extension:84`       |
| Asia Pacific (Malaysia)                | `arn:aws:lambda:ap-southeast-5:381492012281:layer:AWS-Parameters-and-Secrets-Lambda-Extension:83`       |
| Asia Pacific (New Zealand)             | `arn:aws:lambda:ap-southeast-6:995508174458:layer:AWS-Parameters-and-Secrets-Lambda-Extension:78`       |
| Asia Pacific (Mumbai)                  | `arn:aws:lambda:ap-south-1:176022468876:layer:AWS-Parameters-and-Secrets-Lambda-Extension:95`           |
| Asia Pacific (Osaka)                   | `arn:aws:lambda:ap-northeast-3:576959938190:layer:AWS-Parameters-and-Secrets-Lambda-Extension:94`       |
| Asia Pacific (Seoul)                   | `arn:aws:lambda:ap-northeast-2:738900069198:layer:AWS-Parameters-and-Secrets-Lambda-Extension:99`       |
| Asia Pacific (Singapore)               | `arn:aws:lambda:ap-southeast-1:044395824272:layer:AWS-Parameters-and-Secrets-Lambda-Extension:101`      |
| Asia Pacific (Sydney)                  | `arn:aws:lambda:ap-southeast-2:665172237481:layer:AWS-Parameters-and-Secrets-Lambda-Extension:105`      |
| Asia Pacific (Thailand)                | `arn:aws:lambda:ap-southeast-7:941377119484:layer:AWS-Parameters-and-Secrets-Lambda-Extension:84`       |
| Asia Pacific (Tokyo)                   | `arn:aws:lambda:ap-northeast-1:133490724326:layer:AWS-Parameters-and-Secrets-Lambda-Extension:100`      |
| Canada (Central)                       | `arn:aws:lambda:ca-central-1:200266452380:layer:AWS-Parameters-and-Secrets-Lambda-Extension:107`        |
| Canada West (Calgary)                  | `arn:aws:lambda:ca-west-1:243964427225:layer:AWS-Parameters-and-Secrets-Lambda-Extension:71`            |
| China (Beijing)                        | `arn:aws-cn:lambda:cn-north-1:287114880934:layer:AWS-Parameters-and-Secrets-Lambda-Extension:100`       |
| China (Ningxia)                        | `arn:aws-cn:lambda:cn-northwest-1:287310001119:layer:AWS-Parameters-and-Secrets-Lambda-Extension:94`    |
| Europe (Frankfurt)                     | `arn:aws:lambda:eu-central-1:187925254637:layer:AWS-Parameters-and-Secrets-Lambda-Extension:101`        |
| Europe (Ireland)                       | `arn:aws:lambda:eu-west-1:015030872274:layer:AWS-Parameters-and-Secrets-Lambda-Extension:101`           |
| Europe (London)                        | `arn:aws:lambda:eu-west-2:133256977650:layer:AWS-Parameters-and-Secrets-Lambda-Extension:99`            |
| Europe (Milan)                         | `arn:aws:lambda:eu-south-1:325218067255:layer:AWS-Parameters-and-Secrets-Lambda-Extension:95`           |
| Europe (Paris)                         | `arn:aws:lambda:eu-west-3:780235371811:layer:AWS-Parameters-and-Secrets-Lambda-Extension:98`            |
| Europe (Spain) Region                  | `arn:aws:lambda:eu-south-2:524103009944:layer:AWS-Parameters-and-Secrets-Lambda-Extension:90`           |
| AWS European Sovereign Cloud (Germany) | `arn:aws-eusc:lambda:eusc-de-east-1:041683371183:layer:AWS-Parameters-and-Secrets-Lambda-Extension:5`   |
| Europe (Stockholm)                     | `arn:aws:lambda:eu-north-1:427196147048:layer:AWS-Parameters-and-Secrets-Lambda-Extension:95`           |
| Israel (Tel Aviv)                      | `arn:aws:lambda:il-central-1:148806536434:layer:AWS-Parameters-and-Secrets-Lambda-Extension:71`         |
| Europe (Zurich) Region                 | `arn:aws:lambda:eu-central-2:772501565639:layer:AWS-Parameters-and-Secrets-Lambda-Extension:78`         |
| Mexico (Central) Region                | `arn:aws:lambda:mx-central-1:241533131596:layer:AWS-Parameters-and-Secrets-Lambda-Extension:68`         |
| Middle East (Bahrain)                  | `arn:aws:lambda:me-south-1:832021897121:layer:AWS-Parameters-and-Secrets-Lambda-Extension:58`           |
| Middle East (UAE)                      | `arn:aws:lambda:me-central-1:858974508948:layer:AWS-Parameters-and-Secrets-Lambda-Extension:60`         |
| South America (São Paulo)              | `arn:aws:lambda:sa-east-1:933737806257:layer:AWS-Parameters-and-Secrets-Lambda-Extension:103`           |
| AWS GovCloud (US-East)                 | `arn:aws-us-gov:lambda:us-gov-east-1:129776340158:layer:AWS-Parameters-and-Secrets-Lambda-Extension:95` |
| AWS GovCloud (US-West)                 | `arn:aws-us-gov:lambda:us-gov-west-1:127562683043:layer:AWS-Parameters-and-Secrets-Lambda-Extension:98` |

#### Extension ARNs for ARM64 and Mac with Apple silicon architectures

Last updated: July 28, 2026

| Region                           | ARN                                                                                                           |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| US East (Ohio)                   | `arn:aws:lambda:us-east-2:590474943231:layer:AWS-Parameters-and-Secrets-Lambda-Extension-Arm64:109`           |
| US East (N. Virginia)            | `arn:aws:lambda:us-east-1:177933569100:layer:AWS-Parameters-and-Secrets-Lambda-Extension-Arm64:99`            |
| US West (N. California) Region   | `arn:aws:lambda:us-west-1:997803712105:layer:AWS-Parameters-and-Secrets-Lambda-Extension-Arm64:93`            |
| US West (Oregon)                 | `arn:aws:lambda:us-west-2:345057560386:layer:AWS-Parameters-and-Secrets-Lambda-Extension-Arm64:99`            |
| Africa (Cape Town) Region        | `arn:aws:lambda:af-south-1:317013901791:layer:AWS-Parameters-and-Secrets-Lambda-Extension-Arm64:97`           |
| Asia Pacific (Hong Kong) Region  | `arn:aws:lambda:ap-east-1:768336418462:layer:AWS-Parameters-and-Secrets-Lambda-Extension-Arm64:94`            |
| Asia Pacific (Taipei)            | `arn:aws:lambda:ap-east-2:890742577149:layer:AWS-Parameters-and-Secrets-Lambda-Extension-Arm64:65`            |
| Asia Pacific (Hyderabad) Region  | `arn:aws:lambda:ap-south-2:070087711984:layer:AWS-Parameters-and-Secrets-Lambda-Extension-Arm64:83`           |
| Asia Pacific (Jakarta) Region    | `arn:aws:lambda:ap-southeast-3:490737872127:layer:AWS-Parameters-and-Secrets-Lambda-Extension-Arm64:91`       |
| Asia Pacific (Melbourne)         | `arn:aws:lambda:ap-southeast-4:090732460067:layer:AWS-Parameters-and-Secrets-Lambda-Extension-Arm64:83`       |
| Asia Pacific (Malaysia)          | `arn:aws:lambda:ap-southeast-5:381492012281:layer:AWS-Parameters-and-Secrets-Lambda-Extension-Arm64:83`       |
| Asia Pacific (New Zealand)       | `arn:aws:lambda:ap-southeast-6:995508174458:layer:AWS-Parameters-and-Secrets-Lambda-Extension-Arm64:76`       |
| Asia Pacific (Mumbai)            | `arn:aws:lambda:ap-south-1:176022468876:layer:AWS-Parameters-and-Secrets-Lambda-Extension-Arm64:95`           |
| Asia Pacific (Osaka)             | `arn:aws:lambda:ap-northeast-3:576959938190:layer:AWS-Parameters-and-Secrets-Lambda-Extension-Arm64:91`       |
| Asia Pacific (Seoul) Region      | `arn:aws:lambda:ap-northeast-2:738900069198:layer:AWS-Parameters-and-Secrets-Lambda-Extension-Arm64:96`       |
| Asia Pacific (Singapore)         | `arn:aws:lambda:ap-southeast-1:044395824272:layer:AWS-Parameters-and-Secrets-Lambda-Extension-Arm64:101`      |
| Asia Pacific (Sydney)            | `arn:aws:lambda:ap-southeast-2:665172237481:layer:AWS-Parameters-and-Secrets-Lambda-Extension-Arm64:105`      |
| Asia Pacific (Thailand)          | `arn:aws:lambda:ap-southeast-7:941377119484:layer:AWS-Parameters-and-Secrets-Lambda-Extension-Arm64:83`       |
| Asia Pacific (Tokyo)             | `arn:aws:lambda:ap-northeast-1:133490724326:layer:AWS-Parameters-and-Secrets-Lambda-Extension-Arm64:100`      |
| Canada (Central) Region          | `arn:aws:lambda:ca-central-1:200266452380:layer:AWS-Parameters-and-Secrets-Lambda-Extension-Arm64:104`        |
| Canada West (Calgary)            | `arn:aws:lambda:ca-west-1:243964427225:layer:AWS-Parameters-and-Secrets-Lambda-Extension-Arm64:70`            |
| China (Beijing)                  | `arn:aws-cn:lambda:cn-north-1:287114880934:layer:AWS-Parameters-and-Secrets-Lambda-Extension-Arm64:89`        |
| China (Ningxia)                  | `arn:aws-cn:lambda:cn-northwest-1:287310001119:layer:AWS-Parameters-and-Secrets-Lambda-Extension-Arm64:83`    |
| Europe (Frankfurt)               | `arn:aws:lambda:eu-central-1:187925254637:layer:AWS-Parameters-and-Secrets-Lambda-Extension-Arm64:101`        |
| Europe (Ireland)                 | `arn:aws:lambda:eu-west-1:015030872274:layer:AWS-Parameters-and-Secrets-Lambda-Extension-Arm64:101`           |
| Europe (London)                  | `arn:aws:lambda:eu-west-2:133256977650:layer:AWS-Parameters-and-Secrets-Lambda-Extension-Arm64:99`            |
| Europe (Milan) Region            | `arn:aws:lambda:eu-south-1:325218067255:layer:AWS-Parameters-and-Secrets-Lambda-Extension-Arm64:92`           |
| Europe (Paris) Region            | `arn:aws:lambda:eu-west-3:780235371811:layer:AWS-Parameters-and-Secrets-Lambda-Extension-Arm64:95`            |
| Europe (Spain) Region            | `arn:aws:lambda:eu-south-2:524103009944:layer:AWS-Parameters-and-Secrets-Lambda-Extension-Arm64:82`           |
| Europe (Stockholm) Region        | `arn:aws:lambda:eu-north-1:427196147048:layer:AWS-Parameters-and-Secrets-Lambda-Extension-Arm64:92`           |
| Israel (Tel Aviv)                | `arn:aws:lambda:il-central-1:148806536434:layer:AWS-Parameters-and-Secrets-Lambda-Extension-Arm64:70`         |
| Europe (Zurich) Region           | `arn:aws:lambda:eu-central-2:772501565639:layer:AWS-Parameters-and-Secrets-Lambda-Extension-Arm64:70`         |
| Mexico (Central) Region          | `arn:aws:lambda:mx-central-1:241533131596:layer:AWS-Parameters-and-Secrets-Lambda-Extension-Arm64:67`         |
| Middle East (Bahrain) Region     | `arn:aws:lambda:me-south-1:832021897121:layer:AWS-Parameters-and-Secrets-Lambda-Extension-Arm64:55`           |
| Middle East (UAE)                | `arn:aws:lambda:me-central-1:858974508948:layer:AWS-Parameters-and-Secrets-Lambda-Extension-Arm64:49`         |
| South America (São Paulo) Region | `arn:aws:lambda:sa-east-1:933737806257:layer:AWS-Parameters-and-Secrets-Lambda-Extension-Arm64:100`           |
| AWS GovCloud (US-East)           | `arn:aws-us-gov:lambda:us-gov-east-1:129776340158:layer:AWS-Parameters-and-Secrets-Lambda-Extension-Arm64:84` |
| AWS GovCloud (US-West)           | `arn:aws-us-gov:lambda:us-gov-west-1:127562683043:layer:AWS-Parameters-and-Secrets-Lambda-Extension-Arm64:87` |
