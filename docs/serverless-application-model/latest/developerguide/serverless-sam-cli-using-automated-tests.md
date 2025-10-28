# Automate local integration tests with AWS SAM

While you can use [Introduction to testing with sam local invoke](using-sam-cli-local-invoke.md "using-sam-cli-local-invoke.md") to
manually test code, AWS SAM also lets you test your code using automated integration testing. Integration
testing helps you detect issues early in the development cycle, improve the quality of your code, and save
time while reducing costs.

To author automated integration tests in AWS SAM, you first run tests against local Lambda functions before deploying
to the AWS Cloud. The [Introduction to testing with sam local start-lambda](using-sam-cli-local-start-lambda.md "using-sam-cli-local-start-lambda.md")
command starts a local endpoint that emulates the Lambda invoke endpoint. You can invoke it from your automated tests.
Because this endpoint emulates the Lambda invoke endpoint, you can write tests once, and then run them (without any modifications)
against the local Lambda function, or against a deployed Lambda function. You can also run the same tests against a deployed
AWS SAM stack in your CI/CD pipeline.

This is how the process works:

1. Start the local Lambda endpoint.

Start the local Lambda endpoint by running the following command in the
directory that contains your AWS SAM template:

```
sam local start-lambda
```

This command starts a local endpoint at `http://127.0.0.1:3001`
that emulates AWS Lambda. You can run your automated tests against this local
Lambda endpoint. When you invoke this endpoint using the AWS CLI or SDK, it locally
executes the Lambda function that's specified in the request, and returns a
response. 2. Run an integration test against the local Lambda endpoint.

In your integration test, you can use the AWS SDK to invoke your Lambda
function with test data, wait for response, and verify that the response is what
you expect. To run the integration test locally, you should configure the AWS
SDK to send a Lambda Invoke API call to invoke the local Lambda endpoint that you
started in previous step.

The following is a Python example (the AWS SDKs for other languages have
similar configurations):

```
import boto3
import botocore

# Set "running_locally" flag if you are running the integration test locally
running_locally = True

if running_locally:

    # Create Lambda SDK client to connect to appropriate Lambda endpoint
    lambda_client = boto3.client('lambda',
        region_name="us-west-2",
        endpoint_url="http://127.0.0.1:3001",
        use_ssl=False,
        verify=False,
        config=botocore.client.Config(
            signature_version=botocore.UNSIGNED,
            read_timeout=15,
            retries={'max_attempts': 0},
        )
    )
else:
    lambda_client = boto3.client('lambda')


# Invoke your Lambda function as you normally usually do. The function will run
# locally if it is configured to do so
response = lambda_client.invoke(FunctionName="HelloWorldFunction")

# Verify the response
assert response == "Hello World"
```

You can use this code to test deployed Lambda functions by setting
`running_locally` to `False`. This sets up the AWS SDK
to connect to AWS Lambda in the AWS Cloud.
