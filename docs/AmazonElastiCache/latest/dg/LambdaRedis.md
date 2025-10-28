# Tutorial: Configuring Lambda to access ElastiCache in a VPC

In this tutorial you can learn how to create an ElastiCache serverless cache, create a Lambda function, then test the Lambda function, and optionally clean up after.

###### Topics

- [Step 1: Creating an ElastiCache serverless cache.](#LambdaRedis.step1 "#LambdaRedis.step1")
- [Step 2: Create a Lambda function for ElastiCache](#LambdaRedis.step2 "#LambdaRedis.step2")
- [Step 3: Test the Lambda function with ElastiCache](#LambdaRedis.step3 "#LambdaRedis.step3")
- [Step 4: Clean up (Optional)](#LambdaRedis.step4 "#LambdaRedis.step4")

## Step 1: Creating an ElastiCache serverless cache.

To create a serverless cache, follow these steps.

### Step 1.1: Create a serverless cache

In this step, you create a serverless cache in the default Amazon VPC in the us-east-1 region in your account using the AWS Command Line Interface (CLI).
For information on creating serverless cache using the ElastiCache console or API,
see [Create a Redis OSS serverless cache](GettingStarted.serverless-redis.md "GettingStarted.serverless-redis.md").

```
aws elasticache create-serverless-cache \
  --serverless-cache-name cache-01  \
--description "ElastiCache IAM auth application" \
--engine valkey
```

Note that the value of the Status field is set to `CREATING`. It can take a minute for ElastiCache to finish creating your cache.

### Step 1.2: Copy serverless cache endpoint

Verify that ElastiCache for Redis OSS has finished creating the cache with the `describe-serverless-caches` command.

```
aws elasticache describe-serverless-caches \
--serverless-cache-name cache-01
```

Copy the Endpoint Address shown in the output. You'll need this address when you create the deployment package for your Lambda function.

### Step 1.3: Create IAM Role

1. Create an IAM trust policy document, as shown below, for your role that allows your account to assume the new role.
   Save the policy to a file named _trust-policy.json_.

JSON

```
`{
"Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": "sts:AssumeRole",
 "Resource": "arn:aws:iam::*:role/*"
 },
 {
 "Effect": "Allow",
 "Action": "sts:AssumeRole",
 "Resource": "arn:aws:iam::*:role/*"
 }]
}`

```

2. Create an IAM policy document, as shown below. Save the policy to a file named _policy.json_.

JSON

```
`{
"Version":"2012-10-17",
 "Statement": [
 {
"Effect" : "Allow",
 "Action" : [
 "elasticache:Connect"
 ],
 "Resource" : [
 "arn:aws:elasticache:us-east-1:123456789012:serverlesscache:cache-01",
 "arn:aws:elasticache:us-east-1:123456789012:user:iam-user-01"
 ]
 }
 ]
}`

```

3. Create an IAM role.

```
aws iam create-role \
--role-name "elasticache-iam-auth-app" \
--assume-role-policy-document file://trust-policy.json
```

4. Create the IAM policy.

```
aws iam create-policy \
  --policy-name "elasticache-allow-all" \
  --policy-document file://policy.json
```

5. Attach the IAM policy to the role.

```
aws iam attach-role-policy \
 --role-name "elasticache-iam-auth-app" \
 --policy-arn "arn:aws:iam::123456789012:policy/elasticache-allow-all"
```

### Step 1.4: Create a default user

1. Create a new default user.

```
aws elasticache create-user \
  --user-name default \
--user-id default-user-disabled \
--engine redis \
--authentication-mode Type=no-password-required \
--access-string "off +get ~keys*"
```

2. Create a new IAM-enabled user.

```
aws elasticache create-user \
  --user-name iam-user-01 \
--user-id iam-user-01 \
--authentication-mode Type=iam \
--engine redis \
--access-string "on ~* +@all"
```

3. Create a user group and attach the user.

```
aws elasticache create-user-group \
  --user-group-id iam-user-group-01 \
--engine redis \
--user-ids default-user-disabled iam-user-01

aws elasticache modify-serverless-cache \
  --serverless-cache-name cache-01  \
--user-group-id iam-user-group-01
```

## Step 2: Create a Lambda function for ElastiCache

To create a Lambda function to access the ElastiCache cache, take these steps.

### Step 2.1: Create a Lambda function

In this tutorial, we provide example code in Python for your Lambda function.

**Python**

The following example Python code reads and writes an item to your ElastiCache cache. Copy the code and save it into a file named `app.py`.
Be sure to replace the `elasticache_endpoint` value in the code with the endpoint address you copied in the previous step.

```
from typing import Tuple, Union
from urllib.parse import ParseResult, urlencode, urlunparse

import botocore.session
import redis
from botocore.model import ServiceId
from botocore.signers import RequestSigner
from cachetools import TTLCache, cached
import uuid

class ElastiCacheIAMProvider(redis.CredentialProvider):
    def __init__(self, user, cache_name, is_serverless=False, region="us-east-1"):
        self.user = user
        self.cache_name = cache_name
        self.is_serverless = is_serverless
        self.region = region

        session = botocore.session.get_session()
        self.request_signer = RequestSigner(
            ServiceId("elasticache"),
            self.region,
            "elasticache",
            "v4",
            session.get_credentials(),
            session.get_component("event_emitter"),
        )

    # Generated IAM tokens are valid for 15 minutes
    @cached(cache=TTLCache(maxsize=128, ttl=900))
    def get_credentials(self) -> Union[Tuple[str], Tuple[str, str]]:
        query_params = {"Action": "connect", "User": self.user}
        if self.is_serverless:
            query_params["ResourceType"] = "ServerlessCache"
        url = urlunparse(
            ParseResult(
                scheme="https",
                netloc=self.cache_name,
                path="/",
                query=urlencode(query_params),
                params="",
                fragment="",
            )
        )
        signed_url = self.request_signer.generate_presigned_url(
            {"method": "GET", "url": url, "body": {}, "headers": {}, "context": {}},
            operation_name="connect",
            expires_in=900,
            region_name=self.region,
        )
        # RequestSigner only seems to work if the URL has a protocol, but
        # Elasticache only accepts the URL without a protocol
        # So strip it off the signed URL before returning
        return (self.user, signed_url.removeprefix("https://"))

def lambda_handler(event, context):
    username = "iam-user-01" # replace with your user id
    cache_name = "cache-01" # replace with your cache name
    elasticache_endpoint = "cache-01-xxxxx.serverless.use1.cache.amazonaws.com" # replace with your cache endpoint
    creds_provider = ElastiCacheIAMProvider(user=username, cache_name=cache_name, is_serverless=True)
    redis_client = redis.Redis(host=elasticache_endpoint, port=6379, credential_provider=creds_provider, ssl=True, ssl_cert_reqs="none")

    key='uuid'
    # create a random UUID - this will be the sample element we add to the cache
    uuid_in = uuid.uuid4().hex
    redis_client.set(key, uuid_in)
    result = redis_client.get(key)
    decoded_result = result.decode("utf-8")
    # check the retrieved item matches the item added to the cache and print
    # the results
    if decoded_result == uuid_in:
        print(f"Success: Inserted {uuid_in}. Fetched {decoded_result} from Valkey.")
    else:
        raise Exception(f"Bad value retrieved. Expected {uuid_in}, got {decoded_result}")

    return "Fetched value from Valkey"
```

This code uses the Python redis-py library to put items into your cache and retrieve them. This code uses cachetools
to cache generated IAM Auth tokens for 15 mins. To create a deployment package containing redis-py and cachetools,
carry out the following steps.

In your project directory containing the app.py source code file, create a folder package to install the redis-py and
cachetools libraries into.

```
mkdir package
```

Install redis-py, cachetools using pip.

```
pip install --target ./package redis
pip install --target ./package cachetools
```

Create a .zip file containing the redis-py and cachetools libraries. In Linux and macOS, run the following command.
In Windows, use your preferred zip utility to create a .zip file with the redis-py and cachetools libraries at the root.

```
cd package
zip -r ../my_deployment_package.zip .
```

Add your function code to the .zip file. In Linux and macOS, run the following command.
In Windows, use your preferred zip utility to add app.py to the root of your .zip file.

```
cd ..
zip my_deployment_package.zip app.py
```

### Step 2.2: Create the IAM role (execution role)

Attach the AWS managed policy named `AWSLambdaVPCAccessExecutionRole` to the role.

```
aws iam attach-role-policy \
 --role-name "elasticache-iam-auth-app" \
 --policy-arn "arn:aws:iam::aws:policy/service-role/AWSLambdaVPCAccessExecutionRole"
```

### Step 2.3: Upload the deployment package (create the Lambda function)

In this step, you create the Lambda function (AccessValkey) using the create-function AWS CLI command.

From the project directory that contains your deployment package .zip file, run the following Lambda CLI `create-function` command.

For the role option, use the ARN of the execution role you created in the previous step. For the vpc-config enter comma separated lists of your
default VPC's subnets and your default VPC's security group ID. You can find these values in the Amazon VPC console.
To find your default VPC's subnets, choose **Your VPCs**, then choose your AWS account's default VPC.
To find the security group for this VPC, go to **Security** and choose **Security groups**.
Ensure that you have the us-east-1 region selected.

```
aws lambda create-function \
--function-name AccessValkey  \
--region us-east-1 \
--zip-file fileb://my_deployment_package.zip \
--role arn:aws:iam::123456789012:role/elasticache-iam-auth-app \
--handler app.lambda_handler \
--runtime python3.12  \
--timeout 30 \
--vpc-config SubnetIds=comma-separated-vpc-subnet-ids,SecurityGroupIds=default-security-group-id
```

## Step 3: Test the Lambda function with ElastiCache

In this step, you invoke the Lambda function manually using the invoke command.
When the Lambda function executes, it generates a UUID and writes it to the ElastiCache cache that you specified in your Lambda code.
The Lambda function then retrieves the item from the cache.

1. Invoke the Lambda function (AccessValkey) using the AWS Lambda invoke command.

```
aws lambda invoke \
--function-name AccessValkey  \
--region us-east-1 \
output.txt
```

2. Verify that the Lambda function executed successfully as follows:
   - Review the output.txt file.
   - Verify the results in CloudWatch Logs by opening the CloudWatch console and choosing the log group for your function (/aws/lambda/AccessValkey). The log stream should contain output similar to the following:

   ```
   Success: Inserted 826e70c5f4d2478c8c18027125a3e01e. Fetched 826e70c5f4d2478c8c18027125a3e01e from Valkey.
   ```

   - Review the results in the AWS Lambda console.

## Step 4: Clean up (Optional)

To clean up, take these steps.

### Step 4.1: Delete Lambda function

```
aws lambda delete-function \
 --function-name AccessValkey
```

### Step 4.2: Delete Serverless cache

Delete the cache.

```
aws elasticache delete-serverless-cache \
 --serverless-cache-name cache-01
```

Remove users and user group.

```
aws elasticache delete-user \
 --user-id default-user-disabled

aws elasticache delete-user \
 --user-id iam-user-01

aws elasticache delete-user-group \
 --user-group-id iam-user-group-01
```

### Step 4.3: Remove IAM Role and policies

```
aws iam detach-role-policy \
 --role-name "elasticache-iam-auth-app" \
 --policy-arn "arn:aws:iam::123456789012:policy/elasticache-allow-all"

aws iam detach-role-policy \
--role-name "elasticache-iam-auth-app" \
--policy-arn "arn:aws:iam::aws:policy/service-role/AWSLambdaVPCAccessExecutionRole"

aws iam delete-role \
 --role-name "elasticache-iam-auth-app"

 aws iam delete-policy \
  --policy-arn "arn:aws:iam::123456789012:policy/elasticache-allow-all"
```
