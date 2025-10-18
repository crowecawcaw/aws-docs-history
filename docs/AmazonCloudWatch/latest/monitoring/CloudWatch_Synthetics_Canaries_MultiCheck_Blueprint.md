# Creating multi checks blueprint canary

Amazon CloudWatch Synthetics multi checks blueprint helps you create a Synthetics canary by providing a simple JSON configuration. You can save costs by bundling up to 10 different 
 types of HTTP/DNS/SSL/TCP checks in a step-based sequential manner. Each check includes assertions that provide basic verification against a check result.

Multi checks canaries are designed for simple use cases that require only basic checks without a headless browser. For more complex use cases, review the other canary types that Amazon CloudWatch 
 Synthetics provides.

###### Topics

* [Prerequisites](#CloudWatch_Synthetics_MultiCheck_Prerequisites "#CloudWatch_Synthetics_MultiCheck_Prerequisites")
* [Limitations](#CloudWatch_Synthetics_MultiCheck_Limitations "#CloudWatch_Synthetics_MultiCheck_Limitations")
* [Packaging structure, JSON schema, and configuration settings](#CloudWatch_Synthetics_MultiCheck_Packaging "#CloudWatch_Synthetics_MultiCheck_Packaging")
* [Creating a multi check canary in AWS Management Console](#CloudWatch_Synthetics_MultiCheck_Console "#CloudWatch_Synthetics_MultiCheck_Console")
* [Creating a multi check canary using AWS Synthetics APIs](#CloudWatch_Synthetics_MultiCheck_API "#CloudWatch_Synthetics_MultiCheck_API")
* [Creating a multi check canary in AWS CloudFormation](#CloudWatch_Synthetics_MultiCheck_CloudFormation "#CloudWatch_Synthetics_MultiCheck_CloudFormation")
* [Authentication configuration](#CloudWatch_Synthetics_MultiCheck_Authentication "#CloudWatch_Synthetics_MultiCheck_Authentication")
* [Troubleshooting](#CloudWatch_Synthetics_MultiCheck_Troubleshooting "#CloudWatch_Synthetics_MultiCheck_Troubleshooting")

## Prerequisites



* Must be using syn-nodejs-3.0+ in order to create a multi check canary
* When using Authentication and Secrets Manager configuration, you must ensure the canary 
 [ExecutionRoleArn](https://docs.aws.amazon.com/https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CreateCanary.html "https://docs.aws.amazon.com/https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CreateCanary.html") allows for the permissions to access these secrets
* When using Authentication for Sigv4, you must ensure the canary 
 [ExecutionRoleArn](https://docs.aws.amazon.com/https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CreateCanary.html "https://docs.aws.amazon.com/https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CreateCanary.html") allows for the permissions to access the related role

## Limitations



* HTTP Response sizes cannot be greater than 1 MB
* Maximum of 10 defined variables.
* When using the JSON RFC, the Checks JSON may have duplicate fields provided however only the last sequential field will be used
* In the AWS Management Console, a multi check canary will default to showing multi check step metrics to readily identify the availability of each check. When checks are removed, this 
 graph may still show the checks in the availability graph until the metric stops being active for at least 3 hours

## Packaging structure, JSON schema, and configuration settings


The JSON Checks configuration that will be used for the canary must be named `blueprint-config.json`. The configuration must follow 
 the [schema](https://github.com/aws-samples/synthetics-canary-local-debugging-sample/tree/main "https://github.com/aws-samples/synthetics-canary-local-debugging-sample/tree/main") and follow the instructions under [Writing a JSON configuration for Node.js multi Checks blueprint](CloudWatch_Synthetics_WritingCanary_Multichecks.md "CloudWatch_Synthetics_WritingCanary_Multichecks.md").


Compress the `blueprint-config.json` into a ZIP file and provide it in one of the following creation workflows. 
 When there is a `synthetics.json` configuration, then it is also compressed in the same ZIP file. The following is a zip file example called `multi-checks.zip`.



```

multi-checks.zip
├── blueprint-config.json
└── synthetics.json
    
```

## Creating a multi check canary in AWS Management Console


1. Open the Amazon CloudWatch synthetics console.
2. Choose **Create Canary**.
3. Under **Use a blueprint**, choose **multi checks**.


Under **Configure Checks**, you will see two tabs, **Checks** and **Canary configuration**.
4. Select the runtime version **syn-nodejs-3.0** or later.
5. Follow the procedure under [Writing a JSON configuration for Node.js multi Checks blueprint](CloudWatch_Synthetics_WritingCanary_Multichecks.md "CloudWatch_Synthetics_WritingCanary_Multichecks.md") to describe the check you want to perform. Alternatively, the console provides you a default JSON configuration that you can build on.
6. Choose **Create Canary**.

## Creating a multi check canary using AWS Synthetics APIs


Use the `CreateCanary` API and within the `Code` parameter, provide the field/value `BlueprintTypes="multi-checks"` instead of `Handler`. 
 When both `BlueprintTypes` and `Handler` are specified, a `ValidationException` is displayed. The runtime version provided must be `syn-nodejs-3.0 or later`.



```

aws synthetics create-canary \
    --name my-multi-check-canary \
    --code ZipFile="ZIP_BLOB",BlueprintTypes="multi-checks" \
    --runtime-version syn-nodejs-3.0 \
    ...

// Or if you wanted to use S3 to provide your code.

aws synthetics create-canary \
    --name my-multi-check-canary \
    --code S3Bucket="my-code-bucket",S3Key="my-zip-code-key",BlueprintTypes="multi-checks" \
    ...
    
```

## Creating a multi check canary in AWS CloudFormation


In your AWS CloudFormation template for a multi check canary, within the `Code` parameter, provide the field/value `BlueprintTypes="multi-checks"` instead of `Handler`. 
 When both `BlueprintTypes` and `Handler` are specified, a `ValidationException` is displayed. The runtime version provided must be `syn-nodejs-3.0 or later`.
 


An example template:



```

SyntheticsCanary:
    Type: 'AWS::Synthetics::Canary'
    Properties:
      Name: MyCanary
      RuntimeVersion: syn-nodejs-3.0
      Schedule: {Expression: 'rate(5 minutes)', DurationInSeconds: 3600}
      ...
      Code:
        S3Bucket: "my-code-bucket"
        S3Key: "my-zip-code-key"
        BlueprintTypes: ["multi-checks"]
      ...
    
```

## Authentication configuration


When your canary makes HTTP requests to an authenticated endpoint, you can configure the steps of your blueprint canary to use one of four 
 authentication types: Basic, API Key, OAuth Client Credentials, and SigV4. Rather than setting up request headers yourself, you can specify an authentication type in
 your blueprint definition, and Synthetics follows the specified authentication type to populate the components of your HTTP request with the authentication information provided.


You specify an authentication type in your blueprint step with the Authentication section. You specify the authentication scheme you want to use, the properties required for 
 your chosen authentication scheme, and Synthetics uses the information provided to construct an authentication header for your HTTP request.


Since storing secrets (such as passwords or API keys) in plain text is a security concern, Synthetics supports integration with AWS Secrets Manager. When you want to authenticate an HTTP request
 in a Synthetics blueprint canary, you can refer to the secret storing your authentication information and Synthetics handles retrieving the secret and caching it in your canary. 
 This approach provides secrets to Synthetics while keeping your secrets securely stored, without specifying them in plain text in your blueprint configuration.


For more information about AWS Secrets Manager, see [What is AWS Secrets Manager?](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html "https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html")


### Basic authentication


Synthetics implements the Basic HTTP authentication scheme defined in RFC 7617. The process works as follows:



* A username and password pair is provided from the blueprint configuration.
* The user-pass is created by concatenating the username, a single colon (":") character, and the password.
* The user-pass is UTF-8 encoded, then converted into a base64-encoded string.
* This base64-encoded user-pass is provided in the "Authorization" header with the following format: Authorization: Basic {base64-encoded-user-pass}

For example, if the user agent wants to send the user-id "Aladdin" and password "open sesame", it uses the following header field: Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==


Example configuration:



```

"Authentication": {
    "type": "BASIC",
    "username": MY_USERNAME, // Required
    "password": MY_PASSWORD // Required
}
      
```

### API key authentication


You can provide an API key for authenticating your HTTP requests. When you use API key authentication, your provided API key is put into the "X-API-Key" HTTP header. 
 If you have a custom resource that looks for API key headers in a header besides this one, you can optionally specify a different header name to have Synthetics put the API key into.


Example configuration:



```

"Authentication": {
    "type": "API_KEY",
    "apiKey": S0A1M2P3L4E5, // Required
    "header": X-Specific-Header // Optional, defaults to "X-API-Key"
}
      
```

### SigV4 authentication


AWS SigV4 (Signature Version 4) is the AWS signing protocol for adding authentication information to AWS API requests. To make a
 SigV4-authenticated request, you need to specify the region and service you are making requests to, as well as an ARN (AWS Resource Name) identifying an IAM 
 role you want the canary to assume when making this SigV4 request. Synthetics assumes the IAM role provided in the roleArn, and uses it to authenticate your AWS API request.


Example configuration:



```

"Authentication": {
    "type": "SIGV4",
    "region": us-west-2, // Required
    "service": s3, // Required
    "roleArn": arn:AWS:iam:12345678912:role/SampleRole // Required
}
      
```

#### SigV4 considerations


For Synthetics to assume the role that you provided in the SigV4 authentication section, the trust policy attached to that role must be configured to allow 
 the canary to assume the provided roleArn. The AWS principal you need to trust is the role that your canary assumed through AWS STS. It takes the format
 `aws:sts::{account_running_the_canary}:assumed-role/<canary_name>/<assumed_role_name>`arn:.


For example, if you have a canary running in account 0123456789012, named test-canary, and the role it assumed was named canary-assume-role, then the trust
 policy needs to include this statement for the canary to assume the roleArn for SigV4 authentication correctly:



```

{
    "Effect": "Allow",
    "Principal": {
        "AWS": "arn:AWS:sts::123456789012:assumed-role/test-canary/"
    },
    "Action": "sts:AssumeRole"
}
        
```

### OAuth client credentials


Synthetics implements the OAuth Client Credentials grant type as defined in RFC 6479 Section 4.4. If you want to make an HTTP request to an endpoint 
 authenticated with a Bearer Token issued by an OAuth token endpoint, Synthetics can request and manage a bearer token on your behalf. When you use the OAuth scheme, 
 Synthetics performs the following steps:



* Uses the Basic authentication scheme with the clientId and clientSecret to authenticate a request to the tokenUrl, the endpoint that issues bearer tokens
* If you provide the optional scope, audience, and resource parameters, they are included in the token request
* Uses the access token returned by the tokenUrl to authenticate your HTTP request
* Securely stores the refresh token returned from the tokenUrl for future token requests

Example configuration:



```

"Authentication": {
    "type": "OAUTH_CLIENT_CREDENTIALS",
    "tokenUrl": ..., // Required
    "clientId": ..., // Required
    "clientSecret": ..., // Required
    "scope": ..., // Optional
    "audience": ..., // Optional
    "resource": ..., // Optional
}
      
```

#### OAuth considerations


Synthetics refreshes OAuth tokens when a 401 or 407 response is returned.


### AWS Secrets Manager integration


To avoid storing secret values (such as passwords or API keys) in plain text, Synthetics provides an integration with AWS Secrets Manager. You can reference an entire 
 secret value in your blueprint configuration with the format `${aws_SECRET:<secret_name>}`, or to reference a particular key `${aws_SECRET:<secret_name>:<secret_key>}`.


For example, if you have a secret named login/basic-auth-credentials, storing a username and password with the following JSON structure:



```

{
    "username": "Aladdin",
    "password": "open sesame"
}
      
```

You can reference the username and password in your blueprint configuration as follows, and Synthetics handles retrieving the secret value and using its keys to authenticate your request:



```

"Authentication": {
    "type": "BASIC",
    "username": ${AWS_SECRET:login/basic-auth-credentials:username},
    "password": ${AWS_SECRET:login/basic-auth-credentials:password}
}
      
```

To allow Synthetics to retrieve the specified secret, the role ARN assumed by the canary needs to have secretsManager:GetSecretValue permissions. If the secret is encrypted using a customer-managed key instead of the AWS managed key AWS/secretsmanager, then you also need kms:Decrypt permissions for that key.


Example permissions:



```

{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "secretsmanager:GetSecretValue",
            "Resource": "arn:AWS:secretsmanager:us-east-1:123456789012:secret:secretName-AbCdEf"
        },
        {
            "Effect": "Allow",
            "Action": "kms:Decrypt",
            "Resource": "arn:AWS:kms:us-east-1:123456789012:key/key-id"
        }
    ]
}
      
```

## Troubleshooting


### Common troubleshooting failures


The underlying code for multi check blueprint is written in Typescript. See the canary troubleshooting page for common failures: [Troubleshooting a failed canary](CloudWatch_Synthetics_Canaries_Troubleshoot.md "CloudWatch_Synthetics_Canaries_Troubleshoot.md").


### JSON check configuration syntax errors


When there are any syntactic errors related to the canary's JSON check configuration, the AWS Management Console will provide you a failure reason when you attempt to create the canary.
 If you are creating a canary using an API or AWS CloudFormation, you will see the failure when the canary is executed for the first time. It is recommended to use the safe canary updates workflow for multi check canary. 
 For more information, see [Performing safe canary updates](performing-safe-canary-upgrades.md "performing-safe-canary-upgrades.md") .


### Networking or timeout failures


For any intermittent or consistent failures related to timeouts, network connection failures (for example, ENOTFOUND, ECONNRESET) consider turning on 
 `DEBUG` logs such that the following run will provide more additional details on why the Checks are failing. To do so, provide the Environment Variable CW\_SYNTHETICS\_LOG\_LEVEL: "DEBUG".


If there are still failures that you are unable to debug, consider reaching out to AWS Support or checking if any of the other provided Canary types from CloudWatch Synthetics more closely matches your use-case.
