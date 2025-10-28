# Tutorial: Configuring a Lambda function to access MemoryDB in an Amazon VPC

In this tutorial you can learn how to:

- Create a MemoryDB cluster in your default Amazon Virtual Private Cloud (Amazon VPC) in the us-east-1 region.
- Create a Lambda function to access the cluster. When you create the Lambda function, you provide subnet IDs in your Amazon VPC and a VPC security group to allow the Lambda function to access resources in your VPC. For illustration in this tutorial, the Lambda function generates a UUID, writes it to the cluster, and retrieves it from the cluster..
- Invoke the Lambda function manually and verify that it accessed the cluster in your VPC.
- Clean up Lambda function, cluster, and IAM role that were setup for this tutorial.

###### Topics

- [Step 1: Create a cluster](#LambdaMemoryDB.step1 "#LambdaMemoryDB.step1")
- [Step 2: Create a Lambda function](#LambdaMemoryDB.step2 "#LambdaMemoryDB.step2")
- [Step 3: Test the Lambda function](#LambdaMemoryDB.step3 "#LambdaMemoryDB.step3")
- [Step 4: Clean up (Optional)](#LambdaMemoryDB.step4 "#LambdaMemoryDB.step4")

## Step 1: Create a cluster

To create a cluster, follow these steps.

### Create a cluster

In this step, you create a cluster in the default Amazon VPC in the us-east-1 region in your account using the AWS Command Line Interface (CLI).
For information on creating cluster using the MemoryDB console or API, see
see [Step 2: Create a cluster](getting-started.md#getting-started.createcluster "getting-started.md#getting-started.createcluster").

```
aws memorydb create-cluster --cluster-name cluster-01 --engine-version 7.0 --acl-name open-access \
--description "MemoryDB IAM auth application" \
--node-type db.r6g.large
```

Note that the value of the Status field is set to `CREATING`. It can take a few minutes for MemoryDB to finish creating your cluster.

### Copy the cluster endpoint

Verify that MemoryDB has finished creating the cluster with the `describe-clusters` command.

```
aws memorydb describe-clusters \
--cluster-name cluster-01
```

Copy the Cluster Endpoint Address shown in the output. You'll need this address when you create the deployment package for your Lambda function.

### Create IAM Role

1. Create an IAM trust policy document, as shown below, for your role that allows your account to assume the new role.
   Save the policy to a file named _trust-policy.json_. Be sure to replace account_id 123456789012 in this policy with your account_id.

JSON

```
`{
"Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Principal": { "AWS": "arn:aws:iam::123456789012:root" },
 "Action": "sts:AssumeRole"
 },
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "lambda.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }]
}`

```

2. Create an IAM policy document, as shown below. Save the policy to a file named _policy.json_.
   Be sure to replace account_id 123456789012 in this policy with your account_id.

JSON

```
`{
"Version":"2012-10-17",
 "Statement": [
 {
 "Effect" : "Allow",
 "Action" : [
 "memorydb:Connect"
 ],
 "Resource" : [
 "arn:aws:memorydb:us-east-1:123456789012:cluster/cluster-01",
 "arn:aws:memorydb:us-east-1:123456789012:user/iam-user-01"
 ]
 }
 ]
}`

```

3. Create an IAM role.

```
aws iam create-role \
--role-name "memorydb-iam-auth-app" \
--assume-role-policy-document file://trust-policy.json
```

4. Create the IAM policy.

```
aws iam create-policy \
  --policy-name "memorydb-allow-all" \
  --policy-document file://policy.json
```

5. Attach the IAM policy to the role. Be sure to replace account_id 123456789012 in this policy-arn with your account_id.

```
aws iam attach-role-policy \
 --role-name "memorydb-iam-auth-app" \
 --policy-arn "arn:aws:iam::123456789012:policy/memorydb-allow-all"
```

### Create an Access Control List (ACL)

1. Create a new IAM-enabled user.

```
aws memorydb create-user \
  --user-name iam-user-01 \
--authentication-mode Type=iam \
--access-string "on ~* +@all"
```

2. Create an ACL and attach it to the cluster.

```
aws memorydb create-acl \
  --acl-name iam-acl-01 \
  --user-names iam-user-01

aws memorydb update-cluster \
  --cluster-name cluster-01 \
  --acl-name iam-acl-01
```

## Step 2: Create a Lambda function

To create a Lambda function, take these steps.

### Create the deployment package

In this tutorial, we provide example code in Python for your Lambda function.

**Python**

The following example Python code reads and writes an item to your MemoryDB cluster. Copy the code and save it into a file named `app.py`.
Be sure to replace the `cluster_endpoint` value in the code with the endpoint address you copied in a previous step.

```
from typing import Tuple, Union
from urllib.parse import ParseResult, urlencode, urlunparse

import botocore.session
import redis
from botocore.model import ServiceId
from botocore.signers import RequestSigner
from cachetools import TTLCache, cached
import uuid

class MemoryDBIAMProvider(redis.CredentialProvider):
    def __init__(self, user, cluster_name, region="us-east-1"):
        self.user = user
        self.cluster_name = cluster_name
        self.region = region

        session = botocore.session.get_session()
        self.request_signer = RequestSigner(
            ServiceId("memorydb"),
            self.region,
            "memorydb",
            "v4",
            session.get_credentials(),
            session.get_component("event_emitter"),
        )

    # Generated IAM tokens are valid for 15 minutes
    @cached(cache=TTLCache(maxsize=128, ttl=900))
    def get_credentials(self) -> Union[Tuple[str], Tuple[str, str]]:
        query_params = {"Action": "connect", "User": self.user}

        url = urlunparse(
            ParseResult(
                scheme="https",
                netloc=self.cluster_name,
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
        # MemoryDB only accepts the URL without a protocol
        # So strip it off the signed URL before returning
        return (self.user, signed_url.removeprefix("https://"))

def lambda_handler(event, context):
    username = "iam-user-01" # replace with your user id
    cluster_name = "cluster-01" # replace with your cache name
    cluster_endpoint = "clustercfg.cluster-01.xxxxxx.memorydb.us-east-1.amazonaws.com" # replace with your cluster endpoint
    creds_provider = MemoryDBIAMProvider(user=username, cluster_name=cluster_name)
    redis_client = redis.Redis(host=cluster_endpoint, port=6379, credential_provider=creds_provider, ssl=True, ssl_cert_reqs="none")

    key='uuid'
    # create a random UUID - this will be the sample element we add to the cluster
    uuid_in = uuid.uuid4().hex
    redis_client.set(key, uuid_in)
    result = redis_client.get(key)
    decoded_result = result.decode("utf-8")
    # check the retrieved item matches the item added to the cluster and print
    # the results
    if decoded_result == uuid_in:
        print(f"Success: Inserted {uuid_in}. Fetched {decoded_result} from MemoryDB.")
    else:
        raise Exception(f"Bad value retrieved. Expected {uuid_in}, got {decoded_result}")

    return "Fetched value from MemoryDB"
```

This code uses the Python `redis-py` library to put items into your cluster and retrieve them. This code uses `cachetools` to cache generated IAM Auth tokens for 15 mins. To create a deployment package containing `redis-py` and `cachetools`, carry out the following steps.

In your project directory containing the `app.py` source code file, create a folder package to install the `redis-py` and `cachetools` libraries into.

```
mkdir package
```

Install `redis-py` and `cachetools` using pip.

```
pip install --target ./package redis
pip install --target ./package cachetools
```

Create a .zip file containing the `redis-py` and `cachetools` libraries. In Linux and MacOS, run the following command. In Windows, use your preferred zip utility to create a .zip file with the `redis-py` and `cachetools` libraries at the root.

```
cd package
zip -r ../my_deployment_package.zip .
```

Add your function code to the .zip file. In Linux and macOS, run the following command. In Windows, use your preferred zip utility to add app.py to the root of your .zip file.

```
cd ..
zip my_deployment_package.zip app.py
```

### Create the IAM role (execution role)

Attach the AWS managed policy named `AWSLambdaVPCAccessExecutionRole` to the role.

```
aws iam attach-role-policy \
 --role-name "memorydb-iam-auth-app" \
 --policy-arn "arn:aws:iam::aws:policy/service-role/AWSLambdaVPCAccessExecutionRole"
```

### Upload the deployment package (create the Lambda function)

In this step, you create the Lambda function (AccessMemoryDB) using the create-function AWS CLI command.

From the project directory that contains your deployment package .zip file, run the following Lambda CLI `create-function` command.

For the role option, use the ARN of the execution role you created in the previous step. For the vpc-config enter comma separated lists of your
default VPC's subnets and your default VPC's security group ID. You can find these values in the Amazon VPC console.
To find your default VPC's subnets, choose **Your VPCs**, then choose your AWS account's default VPC.
To find the security group for this VPC, go to **Security** and choose **Security groups**.
Ensure that you have the us-east-1 region selected.

```
aws lambda create-function \
--function-name AccessMemoryDB  \
--region us-east-1 \
--zip-file fileb://my_deployment_package.zip \
--role arn:aws:iam::123456789012:role/memorydb-iam-auth-app \
--handler app.lambda_handler \
--runtime python3.12  \
--timeout 30 \
--vpc-config SubnetIds=comma-separated-vpc-subnet-ids,SecurityGroupIds=default-security-group-id
```

## Step 3: Test the Lambda function

In this step, you invoke the Lambda function manually using the invoke command.
When the Lambda function executes, it generates a UUID and writes it to the ElastiCache cache that you specified in your Lambda code.
The Lambda function then retrieves the item from the cache.

1. Invoke the Lambda function (AccessMemoryDB) using the AWS Lambda invoke command.

```
aws lambda invoke \
--function-name AccessMemoryDB  \
--region us-east-1 \
output.txt
```

2. Verify that the Lambda function executed successfully as follows:
   - Review the output.txt file.
   - Verify the results in CloudWatch Logs by opening the CloudWatch console and choosing the log group for your function (/aws/lambda/AccessRedis). The log stream should contain output similar to the following:

   ```
   Success: Inserted 826e70c5f4d2478c8c18027125a3e01e. Fetched 826e70c5f4d2478c8c18027125a3e01e from MemoryDB.
   ```

   - Review the results in the AWS Lambda console.

## Step 4: Clean up (Optional)

To clean up, take these steps.

### Delete Lambda function

```
aws lambda delete-function \
 --function-name AccessMemoryDB
```

### Delete MemoryDB cluster

Delete the cluster.

```
aws memorydb delete-cluster \
 --cluster-name cluster-01
```

Remove user and ACL.

```
aws memorydb delete-user \
 --user-id iam-user-01

aws memorydb delete-acl \
 --acl-name iam-acl-01
```

### Remove IAM Role and policies

```
aws iam detach-role-policy \
 --role-name "memorydb-iam-auth-app" \
 --policy-arn "arn:aws:iam::123456789012:policy/memorydb-allow-all"

aws iam detach-role-policy \
--role-name "memorydb-iam-auth-app" \
--policy-arn "arn:aws:iam::aws:policy/service-role/AWSLambdaVPCAccessExecutionRole"

aws iam delete-role \
 --role-name "memorydb-iam-auth-app"

 aws iam delete-policy \
  --policy-arn "arn:aws:iam::123456789012:policy/memorydb-allow-all"
```
