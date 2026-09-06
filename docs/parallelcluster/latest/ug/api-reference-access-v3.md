

# Accessing the API logs and metrics
<a name="api-reference-access-v3"></a>

API logs are published to Amazon CloudWatch with a retention of 30 days. To retrieve the LogGroup name associated with an API deployment, run the following command: 

```
$ REGION={{<region>}}
$ API_STACK_NAME={{<stack-name>}}
$ aws cloudformation describe-stacks --region ${REGION} --stack-name ${API_STACK_NAME} --query "Stacks[0].Outputs[?OutputKey=='ParallelClusterLambdaLogGroup'].OutputValue" --output text
```

Lambda metrics, logs and [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) trace logs can be also accessed through the Lambda console. To retrieve the ARN of the Lambda function associated with an API deployment run the following command: 

```
$ REGION={{<region>}}
$ API_STACK_NAME={{<stack-name>}}
$ aws cloudformation describe-stacks --region ${REGION} --stack-name ${API_STACK_NAME} --query "Stacks[0].Outputs[?OutputKey=='ParallelClusterLambdaArn'].OutputValue" --output text
```