# Using the AMS API in CLI, Ruby, Python, and Java

The following is a list of code snippets for the AMS API `ListChangeTypeClassificationSummaries`
operation, in all available languages.

For the Python, Ruby, and Java SDKs, see [Tools for Amazon Web Services](https://aws.amazon.com/tools/ "https://aws.amazon.com/tools/") and scroll down to the SDKs section.
Each SDK installer contains a README with additional code snippets.

## AMS API to CLI example

After you have installed the AMS CLI (requires the AWS CLI; see
[Installing or upgrading the AMS CLI](understand-sent-api.md#install-sent-cli "understand-sent-api.md#install-sent-cli")), you can run any
AMS API operation by reforming the call first specifying which AMS API, `aws amscm` or
`aws amsskms`, and
then giving the action with hyphens replacing camel case. Finally, provide credentials, such as SAML.

To learn more, see [Using the AWS Command Line Interface](../../../cli/latest/userguide/cli-chap-using.md "../../../cli/latest/userguide/cli-chap-using.md").

Example:

- API: `'ChangeTypeClassificationSummaries[].[Category,Subcategory,Item,Operation,ChangeTypeId]'`
- CLI: `amscm list-change-type-classification-summaries --query "ChangeTypeClassificationSummaries[*].[Category,Subcategory,Item,Operation,ChangeTypeId]" --output table`

###### Note

If you authenticate with SAML, add `aws --profile saml` to the beginning of the
command. For example,

```
aws --profile saml amscm list-change-type-classification-summaries --query "ChangeTypeClassificationSummaries[*].[Category,Subcategory,Item,Operation,ChangeTypeId]" --output table
```

## AMS API to Python example

In order to use the AMS API with Python, install the AMS CLI and install boto3. Follow these steps:

1. Install the AMS CLI. See [Installing or upgrading the AMS CLI](understand-sent-api.md#install-sent-cli "understand-sent-api.md#install-sent-cli").
2. Install boto3, the AWS SDK for Python. For more information, see this blog post
   [Now Available – AWS SDK For Python (Boto3)](https://aws.amazon.com/blogs/aws/now-available-aws-sdk-for-python-3-boto3/ "https://aws.amazon.com/blogs/aws/now-available-aws-sdk-for-python-3-boto3/").

`import boto3` 3. Get the AMS Change Management client:

`cm = boto3.client('amscm')` 4. Get the AMS CTs:

`cts = cm.list_change_type_classification_summaries()`

`print(cts)`

### Python examples

The following are some examples for using Python in AMS, to create EC2 instances, and/or use Lambda.

#### Python example to create an EC2

This example shows how you can use the amscm RESTFul API from within Python code to file and perform RFC processes.

1. Install the AMS CLI somewhere you have access to; you need the files it supplies.
2. Call Python libraries and create the EC2 instance:

```

import boto3
import json
import time

# Create the amscm client
cm = boto3.client('amscm')

# Define the execution parameters for EC2 Create
AMSExecParams = {
    "Description": "`EC2-Create`",
    "VpcId": "`VPC_ID`",
    "Name": "`My-EC2`",
    "TimeoutInMinutes": 60,
    "Parameters": {
        "InstanceAmiId": "`INSTANCE_ID`",
        "InstanceSubnetId": "`SUBNET_ID"`
    }
}

# Create the AMS RFC
cts = cm.create_rfc(
    ChangeTypeId="ct-14027q0sjyt1h",
    ChangeTypeVersion="3.0",
    Title="`Python Code RFC Create`",
    ExecutionParameters=json.dumps(AMSExecParams)
)

# Extract the RFC ID from the response
NewRfcID = cts['RfcId']

# Submit the RFC
RFC_Submit_Return=cm.submit_rfc(RfcId=`NewRfcID`)

# Check the RFC status every 30 seconds
RFC_Status = cm.get_rfc(RfcId=`NewRfcID`)
RFC_Status_Code = RFC_Status['Rfc']['Status']['Name']

while RFC_Status_Code != "Success":
    if RFC_Status_Code == "PendingApproval":
        print(RFC_Status_Code)
        time.sleep(30)
    elif RFC_Status_Code == "InProgress":
        print(RFC_Status_Code)
        time.sleep(30)
    elif RFC_Status_Code == "Failure":
        print(RFC_Status_Code)
        break
    else:
        print(RFC_Status_Code)

    RFC_Status = cm.get_rfc(RfcId=NewRfcID)
    RFC_Status_Code = RFC_Status['Rfc']['Status']['Name']

```

#### Python example with Lambda

This example shows how to bundle the AMS models with your code so you can use it with
Lambda, or EC2; places you won't, or can't, install `amscli`.

###### Note

AMS does not provide an importable AMS-specific Python SDK. The
`amscli` install script installs the AMS service data models in the
CLI’s normal path. For CLI usage and system Python usage, that is fine, because both
`awscli` and `boto3` read their service models from the
same default locations (`~/.aws/models`). However, when you want to use AMS services
via boto3 in Lambda (or any other non-local runtime), it breaks, because you no
longer have the data models. The following is a method to fix this by packaging the
data models with the function.

There are simple steps that you can take to run your AMS-integrated Python code in
Lambda or another runtime like EC2, Fargate, etc. The following workflow shows the steps
necessary for AMS-integrated Lambda functions.

By adding the data models to the code's deployment package and updating the SDK search
path, you can simulate an SDK experience.

###### Important

This example and all of the non-python commands shown were tested on a Mac computer.

**Example Workflow**:

1. Install the `amscli`. This creates a folder at `~/.aws/models` on your
   computer (Mac).
2. Copy the models to a local directory: `cp ~/.aws/models ./models`.
3. Include the models into your code's deployment package.
4. Update your function code to add the new models to the SDK path. Note that
   this code must run before boto3 or botocore are imported!

```
# Force Python to search local directory for boto3 data models
import os
os.environ['AWS_DATA_PATH'] = './models'

import boto3
import botocore

```

###### Note

Because the example models are in a directory named `models`, we add `./models` to
AWS_DATA_PATH. If the directory was named `/ams/boto3models`, we would add the following code:

```
import os.environ['AWS_DATA_PATH'] = './ams/boto3models'

import boto3
import botocore
```

Your code should successfully find the AMS models. As a more specific example re:
packaging, here's the Lambda specific workflow.

**Example AMS Lambda Workflow**:

These steps apply the preceding generic example to creating an AWS Lambda
function.

1. Install the amscli. This creates a folder at `~/.aws/models` on your computer (Mac).
2. Copy the models to a local directory:

```
cp ~/.aws/models ./models
```

3. Add the models to your function's deployment zip file:

```
zip -r9 function.zip ./models
```

###### Important

Update your function code to add the new models to the SDK path. Note that this
code must run before boto3 or botocore are imported!

```
# Force Python to search local directory for boto3 data models
import os
os.environ['AWS_DATA_PATH'] = './models'

import boto3
import botocore
```

###### Note

Because the example models are in a directory named `models`, We add `./models` to
AWS_DATA_PATH. If the directory was named `/ams/boto3models`, we would add the
following code:

```
import os
os.environ['AWS_DATA_PATH'] = './ams/boto3models'

import boto3
import botocore
```

Now, deploy your function:

1. Add your function code to the deployment zip file (if you haven't done so already):

```
zip -g function.zip lambda-amscm-test.py
```

2. Create or update your function with the zip file you created (console or CLI):

```
aws lambda update-function-code --function-name lambda-amscm-test --zip-file fileb://function.zip --region us-east-1
```

Your AMS-integrated Python Lambda should now work.

###### Note

Your function must have IAM permissions for `amscm` or you get a permissions error.

**Sample Lambda function code to test amscm (contents of lambda-amscm-test.py)**:

```
import json

# Force lambda to search local directory for boto3 data models
import os
os.environ['AWS_DATA_PATH'] = './models'

import boto3
import botocore


def lambda_handler(event, context):
    use_session = boto3.session.Session(region_name="us-east-1")
    try:
        cm = use_session.client("amscm")
        cts = cm.list_change_type_categories()
        print(cts)
    except botocore.exceptions.UnknownServiceError:
        print("amscm not found")

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
```

**Test outputs (success)**:

Function Response:

```
{
  "statusCode": 200,
  "body": "\"Hello from Lambda!\""
}

Request ID:
"1cea13c0-ed46-43b1-b102-a8ea28529c27"
```

Function Logs:

```
START RequestId: 1cea13c0-ed46-43b1-b102-a8ea28529c27 Version: $LATEST
{'ChangeTypeCategories': ['Deployment', 'Internal Infrastructure Management', 'Management'], 'ResponseMetadata': {'RequestId': 'e27276a0-e081-408d-bcc2-10cf0aa19ece', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'e27276a0-e081-408d-bcc2-10cf0aa19ece', 'content-type': 'application/x-amz-json-1.1', 'content-length': '89', 'date': 'Sun, 10 May 2020 23:21:19 GMT'}, 'RetryAttempts': 0}}
END RequestId: 1cea13c0-ed46-43b1-b102-a8ea28529c27
```

## AMS API to Ruby example

In order to use the AMS API with Ruby, install the AWS Ruby SDK and AMS CLI. Follow these steps:

1. Install the AMS CLI. See [Installing or upgrading the AMS CLI](understand-sent-api.md#install-sent-cli "understand-sent-api.md#install-sent-cli").
2. Install the AWS Ruby SDK. See [Tools for Amazon Web Services](https://aws.amazon.com/tools/ "https://aws.amazon.com/tools/").
3. Configure Ruby with these commands:

`require 'aws-sdk'`

`config = {`

`region: '`us-east-1`',`

`credentials: Aws::Credentials.new('`ACCESS_KEY`','`SECRET_KEY`')}` 4. Get the AMS CTs:

`ams_cm = Aws::amscm::Client.new(config)`

`cts = ams_cm.list_change_type_classification_summaries`

`print(cts)`

## AMS API to Java example

In order to use the AMS API with Java, install the AWS Java SDK and
AMS CLI. Follow these steps:

1. Install the AMS CLI. See [Installing or upgrading the AMS CLI](understand-sent-api.md#install-sent-cli "understand-sent-api.md#install-sent-cli").
2. Install the AWS Java SDK. See [Tools for Amazon Web Services](https://aws.amazon.com/tools/ "https://aws.amazon.com/tools/").
3. Configure Java with these commands:

`import com.amazonaws.auth.BasicAWSCredentials;`

`import com.amazonaws.services.amscm.model.AWSManagedServicesCMClient;`

`import com.amazonaws.services.amscm.model.ListChangeTypeClassificationSummariesRequest;`

`import com.amazonaws.services.amscm.model.ListChangeTypeClassificationSummariesResult;`

`public static void getChangeTypeClassificationSummaries() {` 4. Set the credentials. We recommend that you do not hardcode this.

`final BasicAWSCredentials awsCredsCm =`

`new BasicAWSCredentials("`ACCESS_KEY`", "`SECRET_KEY`");` 5. Create the AMS Change Management client:

`final AWSManagedServicesCMClient cmClient =`

`new AWSManagedServicesCMClient(awsCredsCm);` 6. Get the AMS CTs:

`final ListChangeTypeClassificationSummariesRequest listCtsRequest = new ListChangeTypeClassification SummariesRequest();`

`final ListChangeTypeClassificationSummariesResult listCtsResult =`

`cmClient.listChangeTypeClassificationSummaries(listCtsRequest);`

`System.out.println("List of CTs");`

`listCtsResult.getChangeTypeClassificationSummaries().stream()`

`.map(x -> x.getCategory() + "/" + x.getSubcategory() + "/" + x.getItem() + "/" + x.getOperation())`

`.forEach(System.out::println);`

`}`
