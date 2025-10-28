# Use a Docker registry that requires authentication for training

If your Docker registry requires authentication, you must create an AWS Lambda
function that provides access credentials to SageMaker AI. Then, create a training job and
provide the ARN of this Lambda function inside the [create_training_job](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_training_job "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_training_job") API. Lastly, you can optionally create an interface
VPC endpoint so that your VPC can communicate with your Lambda function without
sending traffic over the internet. The following guide shows how to create a Lambda
function, assign it the correct role and create an interface VPC endpoint.

## Create the Lambda function

Create an AWS Lambda function that passes access credentials to SageMaker AI and
returns a response. The following code example creates the Lambda function
handler, as follows.

```
def handler(event, context):
   response = {
      "Credentials": {"Username": "username", "Password": "password"}
   }
   return response
```

The type of authentication used to set up your private Docker registry
determines the contents of the response returned by your Lambda function as
follows.

- If your private Docker registry uses basic authentication, the Lambda
  function will return the username and password needed in order to
  authenticate to the registry.
- If your private Docker registry uses [bearer token
  authentication](https://docs.docker.com/registry/spec/auth/token/ "https://docs.docker.com/registry/spec/auth/token/"), the username and password are sent to your
  authorization server, which then returns a bearer token. This token is
  then used to authenticate to your private Docker registry.

###### Note

If you have more than one Lambda functions for your registries in the same
account, and the execution role is the same for your training jobs, then
training jobs for registry one would have access to the Lambda functions for
other registries.

## Grant the correct role permission to your Lambda function

The [IAMrole](sagemaker-roles.md "sagemaker-roles.md") that you use in the `create_training_job` API
must have permission to call an AWS Lambda function. The following code example
shows how to extend permissions policy of an IAM role to call
`myLambdaFunction`.

```
{
    "Effect": "Allow",
    "Action": [
        "lambda:InvokeFunction"
    ],
    "Resource": [
        "arn:aws:lambda:*:*:function:*myLambdaFunction*"
    ]
}
```

For information about editing a role permissions policy, see [Modifying a role permissions policy (console)](../../../IAM/latest/UserGuide/roles-managingrole-editing-console.md#roles-modify_permissions-policy "../../../IAM/latest/UserGuide/roles-managingrole-editing-console.md#roles-modify_permissions-policy") in the
_AWS Identity and Access Management User Guide_.

###### Note

An IAM role with an attached **AmazonSageMakerFullAccess** managed policy has permission to
call any Lambda function with "SageMaker AI" in its name.

## Create an interface VPC endpoint for Lambda

If you create an interface endpoint, your Amazon VPC can communicate with your
Lambda function without sending traffic over the internet. For more information,
see [Configuring
interface VPC endpoints for Lambda](../../../lambda/latest/dg/configuration-vpc-endpoints.md "../../../lambda/latest/dg/configuration-vpc-endpoints.md") in the _AWS Lambda
Developer Guide_.

After your interface endpoint is created, SageMaker training will call your Lambda
function by sending a request through your VPC to
`lambda.region.amazonaws.com`. If you select **Enable DNS Name** when you create your interface
endpoint, [Amazon Route 53](../../../Route53/latest/DeveloperGuide/Welcome.md "../../../Route53/latest/DeveloperGuide/Welcome.md") routes
the call to the Lambda interface endpoint. If you use a different DNS provider,
you must map `lambda.region.amazonaws.co`m, to your Lambda interface
endpoint.
