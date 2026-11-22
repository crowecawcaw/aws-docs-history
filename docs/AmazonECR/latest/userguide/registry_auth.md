

# Private registry authentication in Amazon ECR

You can use the AWS Management Console, the AWS CLI, or the AWS SDKs to create and manage private repositories. You can also use those methods to perform some actions on images, such as listing or deleting them. These clients use standard AWS authentication methods. Even though you can use the Amazon ECR API to push and pull images, you're more likely to use the Docker CLI or a language-specific Docker library.

The Docker CLI doesn't support native IAM authentication methods. Additional steps must be taken so that Amazon ECR can authenticate and authorize Docker push and pull requests.

You can use a regional token or a global token to authenticate to an Amazon ECR private registry. The following table compares regional tokens and global tokens.


| Token type | Token request | AWS Region scope | Validity | 
| --- | --- | --- | --- | 
| Global token | AWS Sign-In [CreateBearerToken](https://docs.aws.amazon.com/signin/latest/APIReference/API_dataplane-signin_CreateBearerToken.html) or aws signin create-bearer-token | Valid in all AWS Regions in the same partition | 12 hours by default, with configurable duration support | 
| Regional token | Amazon ECR [GetAuthorizationToken](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetAuthorizationToken.html) or aws ecr get-login-password | Valid in the same AWS Region that issued the token | 12 hours | 

**Note**  
The permission scope of a regional token or global token matches your IAM permissions. An authentication token doesn't give you additional Amazon ECR permissions. You must still have permission to perform the requested Amazon ECR actions.

## Using a global token
<a name="registry-auth-global-token"></a>

With an Amazon ECR *global token*, you can authenticate to Amazon ECR registry endpoints in AWS Regions of a single partition. AWS Sign-In issues each global token as a bearer token for the `ecr.amazonaws.com` resource. A global token supports a configurable lifetime as short as 5 minutes. If you don't specify a duration, the default lifetime is 12 hours.

Before you request a global token, make sure that you have `signin:CreateBearerToken` permission and the Amazon ECR permissions required for your image or repository operations. The following IAM policy grants permission to request a global token for Amazon ECR:

```JSON
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "CreateECRGlobalToken",
            "Effect": "Allow",
            "Action": "signin:CreateBearerToken",
            "Resource": "arn:aws:signin:*:*:service-principal/ecr.amazonaws.com"
        }
    ]
}
```

Global tokens provide the following security and auditing capabilities:
+ Use the `signInSessionArn` field in the `userIdentity.sessionContext` element of CloudTrail events to correlate token usage with the AWS session that requested the token. For more information, see [CloudTrail userIdentity element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html).
+ Use the [IntrospectOAuth2TokenWithIAM](https://docs.aws.amazon.com/signin/latest/APIReference/API_dataplane-signin_IntrospectOAuth2TokenWithIAM.html) API operation to check a token's active state and metadata.

**To authenticate Docker to an Amazon ECR private registry with a global token**

1. Use the [create-bearer-token](https://docs.aws.amazon.com/cli/latest/reference/signin/create-bearer-token.html) AWS CLI command to request the default 12-hour global token for Amazon ECR.

   ```
   TOKEN=$(aws signin create-bearer-token \
        --grant-type client_credentials \
        --resource ecr.amazonaws.com \
        --region {{token_region}} \
        --query accessToken \
        --output text)
   ```

1. Pass the global token to `docker login`, and specify `AWS` as the username.

   ```
   printf '%s' "$TOKEN" | docker login \
        --username AWS \
        --password-stdin \
        {{aws_account_id}}.dkr.ecr.{{registry_region}}.amazonaws.com
   ```

## Using a regional token
<a name="registry-auth-token"></a>

A regional token is valid for 12 hours in the same AWS Region that issued the token. To obtain a regional token, use the [GetAuthorizationToken](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetAuthorizationToken.html) API operation to retrieve a base64-encoded authorization token containing the username `AWS` and an encoded password. The AWS CLI `get-login-password` command simplifies this by retrieving and decoding the token, which you can then pipe into a `docker login` command to authenticate.

**To authenticate Docker to an Amazon ECR private registry with a regional token**

1. Configure the AWS CLI to interact with AWS. For more information, see [AWS CLI configuration basics](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html) in the *AWS Command Line Interface User Guide*.

1. Use one of the following commands to authenticate to an Amazon ECR private registry. For **docker login**, use `AWS` as the username and specify the Amazon ECR registry URI. Repeat the command for each registry that you want to authenticate to.
   + [get-login-password](https://docs.aws.amazon.com/cli/latest/reference/ecr/get-login-password.html) (AWS CLI)

     ```
     aws ecr get-login-password --region {{region}} | docker login --username AWS --password-stdin {{{{aws_account_id}}}}.dkr.ecr.{{region}}.amazonaws.com
     ```
   + [Get-ECRLoginCommand](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-ECRLoginCommand.html) (AWS Tools for Windows PowerShell)

     ```
     (Get-ECRLoginCommand).Password | docker login --username AWS --password-stdin {{{{aws_account_id}}}}.dkr.ecr.{{region}}.amazonaws.com
     ```

## Using HTTP API authentication
<a name="registry_auth_http"></a>

Amazon ECR supports the [Docker Registry HTTP API](https://docs.docker.com/registry/spec/api/). However, because Amazon ECR is a private registry, you must provide a registry authentication token with every HTTP request. The following examples use a regional token or a global token to list the image tags in an Amazon ECR repository.

------
#### [ Regional token ]

Retrieve a regional token with the AWS CLI and set it to an environment variable. The returned value is already encoded for an HTTP Basic authorization header.

```
TOKEN=$(aws ecr get-authorization-token \
     --output text \
     --query 'authorizationData[].authorizationToken')
```

Pass the `$TOKEN` variable in the HTTP Basic authorization header.

```
curl -i \
     -H "Authorization: Basic $TOKEN" \
     https://{{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/v2/{{amazonlinux}}/tags/list
```

------
#### [ Global token ]

Retrieve a global token with the AWS CLI. Create the HTTP Basic authorization value by base64-encoding the username `AWS`, a colon, and the global token.

```
GLOBAL_TOKEN=$(aws signin create-bearer-token \
     --grant-type client_credentials \
     --resource ecr.amazonaws.com \
     --query accessToken \
     --output text)
TOKEN=$(printf 'AWS:%s' "$GLOBAL_TOKEN" | base64 | tr -d '\n')
```

Pass the `$TOKEN` variable in the HTTP Basic authorization header.

```
curl -i \
     -H "Authorization: Basic $TOKEN" \
     https://{{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/v2/{{amazonlinux}}/tags/list
```

------

The output is as follows:

```
HTTP/1.1 200 OK
Content-Type: text/plain; charset=utf-8
Date: Thu, 04 Jan 2018 16:06:59 GMT
Docker-Distribution-Api-Version: registry/2.0
Content-Length: 50
Connection: keep-alive

{"name":"amazonlinux","tags":["2017.09","latest"]}
```

## Using the Amazon ECR credential helper
<a name="registry-auth-credential-helper-reg"></a>

Amazon ECR provides a Docker credential helper which makes it easier to store and use Docker credentials when pushing and pulling images to Amazon ECR. The Amazon ECR Docker credential helper can retrieve both regional tokens and global tokens. For installation and configuration steps, see [Amazon ECR Docker Credential Helper on GitHub](https://github.com/awslabs/amazon-ecr-credential-helper).

**Note**  
The Amazon ECR Docker credential helper doesn't support multi-factor authentication (MFA) currently.