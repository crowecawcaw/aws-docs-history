# Create an IAM role and IoT rule

for your destination

AWS IoT rules send device messages to other services. AWS IoT rules can also process
the binary messages received from a Sidewalk end device for other services to
use. AWS IoT Core for Amazon Sidewalk destinations associate a wireless device with the rule that
processes the device's message data to send to other services. The rule acts on the
device's data as soon as AWS IoT Core for Amazon Sidewalk receives it. For all devices that send their
data to the same service, you can create a destination that can be shared by all
devices. You must also create an IAM role that grants permission to send data to
the rule.

## Create an IAM role for your

destination

Create an IAM role that grants AWS IoT Core for Amazon Sidewalk permission to send data to the
AWS IoT rule. To create the role, use the [`CreateRole`](../../../IAM/latest/APIReference/API_CreateRole.md "../../../IAM/latest/APIReference/API_CreateRole.md") API
operation or [`create-role`](../../../cli/latest/reference/iam/create-role.md "../../../cli/latest/reference/iam/create-role.md")
CLI command. You can name the role as
`SidewalkRole`.

```
aws iam create-role --role-name `SidewalkRole` \
    --assume-role-policy-document '{"Version": "2012-10-17",		 	 	 "Statement": [{ "Effect": "Allow", "Principal": {"Service": "lambda.amazonaws.com"}, "Action": "sts:AssumeRole"}]}'
```

You can also define the trust policy for the role using a JSON file.

```
aws iam create-role --role-name `SidewalkRole` \
    --assume-role-policy-document `file://trust-policy.json`
```

The following shows the contents of the JSON file.

**Contents of trust-policy.json**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "lambda.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

## Create a rule for your

destination

Use the AWS IoT Core API operation, [`CreateTopicRule`](../../../iot/latest/apireference/API_CreateTopicRule.md "../../../iot/latest/apireference/API_CreateTopicRule.md"), or the AWS CLI command, [`create-topic-rule`](../../../cli/latest/reference/iot/create-topic-rule.md "../../../cli/latest/reference/iot/create-topic-rule.md"), to create a rule. The topic
rule will be used by your destination to route the data received from your
Sidewalk end device to other AWS services. For example, you can create
a rule action that sends a message to a Lambda function. You can define the
Lambda function such that it receives the application data from your device and
uses base64 to decode the payload data so that it can be used by other
applications.

The following steps show how you create the Lambda function and then a topic
rule that sends a message to this function.

1. ###### Create execution role and policy

Create an IAM role that grants your function permission to access
AWS resources. You can also define the trust policy for the role using
a JSON file.

```
aws iam create-role --role-name `lambda-ex` \
    --assume-role-policy-document `file://lambda-trust-policy.json`
```

The following shows the contents of the JSON file.

**Contents of
lambda-trust-policy.json**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "lambda.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

2. ###### Create and test Lambda function

Perform the following steps to create a AWS Lambda function that base64
decodes the payload data.

    1. Write the code for decoding the payload data. For example, you
     can use the following sample Python code. Specify a name for the
     script, such as
     ``base64_decode.py``.


    **Contents of
     base64\_decode.py**



    ```
    // -----------------------------------------------------------
    // ----- Python script to decode incoming binary payload -----
    // -----------------------------------------------------------
    import json
    import base64

    def lambda_handler(event, context):

        message = json.dumps(event)
        print (message)

        payload_data = base64.b64decode(event["PayloadData"])
        print(payload_data)
        print(int(payload_data,16))
    ```
    2. Create a deployment package as a zip file that contains the
     Python file and name it as
     ``base64_decode.zip``.
     Use the `CreateFunction` API or the
     `create-function` CLI command to create a Lambda
     function for the sample code,
     ``base64_decode.py``.
    3. ```
    aws lambda create-function --function-name `my-function` \
    --zip-file `fileb://base64_decode.zip` --handler index.handler \
    --runtime python3.9 --role arn:aws:iam::`123456789012`:role/`lambda-ex`
    ```

    You should see the following output. You'll use the Amazon
     Resource Name (ARN) value from the output,
     `FunctionArn`, when creating the topic
     rule.



    ```
    {
        "FunctionName": `"my-function"`,
        "FunctionArn": "arn:aws:lambda:`us-east-1:123456789012`:function:`my-function`",
        "Runtime": `"python3.9"`,
        "Role": "arn:aws:iam::`123456789012`:role/`lambda-ex`",
        "Handler": "index.handler",
        "CodeSha256": `"FpFMvUhayLkOoVBpNuNiIVML/tuGv2iJQ7t0yWVTU8c="`,
        "Version": "$LATEST",
        "TracingConfig": {
            "Mode": "PassThrough"
        },
        "RevisionId": "88ebe1e1-bfdf-4dc3-84de-3017268fa1ff",
        ...
    }
    ```
    4. To get logs for an invocation from the command line, use the
     `--log-type` option with the `invoke`
     command. The response includes a LogResult field that contains
     up to 4 KB of base64-encoded logs from the invocation.



    ```
    aws lambda invoke --function-name `my-function` out --log-type Tail
    ```

    You should receive a response with a `StatusCode`
     of 200. For more information about creating and using Lambda
     functions from the AWS CLI, see [Using
     Lambda with the AWS CLI](../../../lambda/latest/dg/gettingstarted-awscli.md "../../../lambda/latest/dg/gettingstarted-awscli.md").

3. Create a topic rule

Use the `CreateTopicRule` API or the
`create-topic-rule` CLI command to create a topic rule
that sends a message to this Lambda function. You can also add a second
rule action that republishes to an AWS IoT topic. Name this topic rule as
`Sidewalkrule`.

```
aws iot create-topic-rule --rule-name `Sidewalkrule` \
    --topic-rule-payload `file://myrule.json`
```

You can use the `myrule.json` file to specify more details
about the rule. For example, the following JSON file shows how to
republish to an AWS IoT topic and send a message to a Lambda
function.

```
{
    "sql": "SELECT * ",
    "actions": [
       {
            // You obtained this `functionArn` when creating the Lambda function using the
            // `create-function` command.
            "lambda": {
                "functionArn": "arn:aws:lambda:`us-east-1:``123456789012`:function:`my-function`"
             }
        },
        {
            // This topic can be used to observe messages exchanged between the device and
            // AWS IoT Core for Amazon Sidewalk after the device is connected.
             "republish": {
                 "roleArn": "arn:aws:iam::`123456789012`:role/service-role/`SidewalkRepublishRole`",
                 "topic": `"project/sensor/observed"`
             }
        }
    ],
}
```
