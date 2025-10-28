# `cfn-response`

module

In your CloudFormation template, you can specify a Lambda function as the target of a custom
resource. When you use the `ZipFile` property to specify your [function's](../TemplateReference/aws-resource-lambda-function.md "../TemplateReference/aws-resource-lambda-function.md")
source code, you can load the `cfn-response` module to send responses from your Lambda
function to a custom resource. The `cfn-response` module is a library that simplifies
sending responses to the custom resource that invoked your Lambda function. The module has a
`send` method that sends a [response
object](crpg-ref-responses.md "crpg-ref-responses.md") to a custom resource by way of an Amazon S3 presigned URL (the
`ResponseURL`).

The `cfn-response` module is available only when you use the `ZipFile`
property to write your source code. It isn't available for source code that's stored in Amazon S3
buckets. For code in buckets, you must write your own functions to send responses.

###### Note

After executing the `send` method, the Lambda function terminates, so anything
you write after that method is ignored.

## Loading the

`cfn-response` module

For Node.js functions, use the `require()` function to load the
`cfn-response` module. For example, the following code example creates a
`cfn-response` object with the name `response`:

```
var response = require('cfn-response');
```

For Python, use the `import` statement to load the `cfnresponse`
module, as shown in the following example:

###### Note

Use this exact import statement. If you use other variants of the import statement,
CloudFormation doesn't include the response module.

```
import cfnresponse
```

## `send`

method parameters

You can use the following parameters with the `send` method.

`event`

The fields in a [custom resource
request](crpg-ref-requesttypes.md "crpg-ref-requesttypes.md").

`context`

An object, specific to Lambda functions, that you can use to specify when the
function and any callbacks have completed execution, or to access information from
within the Lambda execution environment. For more information, see [Building Lambda functions with Node.js](../../../lambda/latest/dg/lambda-nodejs.md "../../../lambda/latest/dg/lambda-nodejs.md") in
the _AWS Lambda Developer Guide_.

`responseStatus`

Whether the function successfully completed. Use the `cfnresponse` module
constants to specify the status: `SUCCESS` for successful executions and
`FAILED` for failed executions.

`responseData`

The `Data` field of a custom resource [response object](crpg-ref-responses.md "crpg-ref-responses.md"). The data is a list of name-value pairs.

`physicalResourceId`

Optional. The unique identifier of the custom resource that invoked the function. By
default, the module uses the name of the Amazon CloudWatch Logs log stream that's associated with the
Lambda function.

The value returned for a `PhysicalResourceId` can change custom resource
update operations. If the value returned is the same, it's considered a normal update.
If the value returned is different, CloudFormation recognizes the update as a replacement
and sends a delete request to the old resource. For more information, see [`AWS::CloudFormation::CustomResource`](../TemplateReference/aws-resource-cloudformation-customresource.md "../TemplateReference/aws-resource-cloudformation-customresource.md").

`noEcho`

Optional. Indicates whether to mask the output of the custom resource when it's
retrieved by using the `Fn::GetAtt` function. If set to `true`,
all returned values are masked with asterisks (\*\*\*\*\*), except for information stored in
the locations specified below. By default, this value is `false`.

###### Important

Using the `NoEcho` attribute does not mask any information stored in the following:

- The `Metadata` template section. CloudFormation does not transform, modify, or redact any
  information you include in the `Metadata` section. For more information, see
  [Metadata](metadata-section-structure.md "metadata-section-structure.md").
- The `Outputs` template section. For more information, see
  [Outputs](outputs-section-structure.md "outputs-section-structure.md").
- The `Metadata` attribute of a resource definition. For more information, see
  [`Metadata` attribute](../TemplateReference/aws-attribute-metadata.md "../TemplateReference/aws-attribute-metadata.md").
  We strongly recommend you do not use these mechanisms to include sensitive information, such as
  passwords or secrets.

For more information about using `NoEcho` to mask sensitive information,
see the [Do not embed credentials in your templates](security-best-practices.md#creds "security-best-practices.md#creds") best practice.

## Examples

### Node.js

In the following Node.js example, the inline Lambda function takes an input value and
multiplies it by 5. Inline functions are especially useful for smaller functions because
they allow you to specify the source code directly in the template, instead of creating a
package and uploading it to an Amazon S3 bucket. The function uses the `cfn-response`
`send` method to send the result back to the custom resource that invoked
it.

#### JSON

```
"ZipFile": { "Fn::Join": ["", [
  "var response = require('cfn-response');",
  "exports.handler = function(event, context) {",
  "  var input = parseInt(event.ResourceProperties.Input);",
  "  var responseData = {Value: input * 5};",
  "  response.send(event, context, response.SUCCESS, responseData);",
  "};"
]]}
```

#### YAML

```
ZipFile: >
  var response = require('cfn-response');
  exports.handler = function(event, context) {
    var input = parseInt(event.ResourceProperties.Input);
    var responseData = {Value: input * 5};
    response.send(event, context, response.SUCCESS, responseData);
  };
```

### Python

In the following Python example, the inline Lambda function takes an integer value and
multiplies it by 5.

#### JSON

```
"ZipFile" : { "Fn::Join" : ["\n", [
  "import json",
  "import cfnresponse",
  "def handler(event, context):",
  "   responseValue = int(event['ResourceProperties']['Input']) * 5",
  "   responseData = {}",
  "   responseData['Data'] = responseValue",
  "   cfnresponse.send(event, context, cfnresponse.SUCCESS, responseData, \"CustomResourcePhysicalID\")"
]]}
```

#### YAML

```
ZipFile: |
  import json
  import cfnresponse
  def handler(event, context):
    responseValue = int(event['ResourceProperties']['Input']) * 5
    responseData = {}
    responseData['Data'] = responseValue
    cfnresponse.send(event, context, cfnresponse.SUCCESS, responseData, "CustomResourcePhysicalID")
```

## Module source code

###### Topics

- [Asynchronous Node.js source code](#cfn-lambda-function-code-cfnresponsemodule-source-nodejs-async "#cfn-lambda-function-code-cfnresponsemodule-source-nodejs-async")
- [Node.js source
  code](#cfn-lambda-function-code-cfnresponsemodule-source-nodejs "#cfn-lambda-function-code-cfnresponsemodule-source-nodejs")
- [Python source
  code](#cfn-lambda-function-code-cfnresponsemodule-source-python "#cfn-lambda-function-code-cfnresponsemodule-source-python")

### Asynchronous Node.js source code

The following is the response module source code for the Node.js functions if the
handler is asynchronous. Review it to understand what the module does and for help with
implementing your own response functions.

```
// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

exports.SUCCESS = "SUCCESS";
exports.FAILED = "FAILED";

exports.send = function(event, context, responseStatus, responseData, physicalResourceId, noEcho) {

    return new Promise((resolve, reject) => {
        var responseBody = JSON.stringify({
            Status: responseStatus,
            Reason: "See the details in CloudWatch Log Stream: " + context.logStreamName,
            PhysicalResourceId: physicalResourceId || context.logStreamName,
            StackId: event.StackId,
            RequestId: event.RequestId,
            LogicalResourceId: event.LogicalResourceId,
            NoEcho: noEcho || false,
            Data: responseData
        });

        console.log("Response body:\n", responseBody);

        var https = require("https");
        var url = require("url");

        var parsedUrl = url.parse(event.ResponseURL);
        var options = {
            hostname: parsedUrl.hostname,
            port: 443,
            path: parsedUrl.path,
            method: "PUT",
            headers: {
                "content-type": "",
                "content-length": responseBody.length
            }
        };

        var request = https.request(options, function(response) {
            console.log("Status code: " + parseInt(response.statusCode));
            resolve(context.done());
        });

        request.on("error", function(error) {
            console.log("send(..) failed executing https.request(..): " + maskCredentialsAndSignature(error));
            reject(context.done(error));
        });

        request.write(responseBody);
        request.end();
    })
}

function maskCredentialsAndSignature(message) {
    return message.replace(/X-Amz-Credential=[^&\s]+/i, 'X-Amz-Credential=*****')
        .replace(/X-Amz-Signature=[^&\s]+/i, 'X-Amz-Signature=*****');
}

```

### Node.js source

code

The following is the response module source code for the Node.js functions if the
handler is not asynchronous. Review it to understand what the module does and for help with
implementing your own response functions.

```
// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

exports.SUCCESS = "SUCCESS";
exports.FAILED = "FAILED";

exports.send = function(event, context, responseStatus, responseData, physicalResourceId, noEcho) {

    var responseBody = JSON.stringify({
        Status: responseStatus,
        Reason: "See the details in CloudWatch Log Stream: " + context.logStreamName,
        PhysicalResourceId: physicalResourceId || context.logStreamName,
        StackId: event.StackId,
        RequestId: event.RequestId,
        LogicalResourceId: event.LogicalResourceId,
        NoEcho: noEcho || false,
        Data: responseData
    });

    console.log("Response body:\n", responseBody);

    var https = require("https");
    var url = require("url");

    var parsedUrl = url.parse(event.ResponseURL);
    var options = {
        hostname: parsedUrl.hostname,
        port: 443,
        path: parsedUrl.path,
        method: "PUT",
        headers: {
            "content-type": "",
            "content-length": responseBody.length
        }
    };

    var request = https.request(options, function(response) {
        console.log("Status code: " + parseInt(response.statusCode));
        context.done();
    });

    request.on("error", function(error) {
        console.log("send(..) failed executing https.request(..): " + maskCredentialsAndSignature(error));
        context.done();
    });

    request.write(responseBody);
    request.end();
}
```

### Python source

code

The following is the response module source code for Python functions:

```
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

from __future__ import print_function
import urllib3
import json
import re

SUCCESS = "SUCCESS"
FAILED = "FAILED"

http = urllib3.PoolManager()


def send(event, context, responseStatus, responseData, physicalResourceId=None, noEcho=False, reason=None):
    responseUrl = event['ResponseURL']

    responseBody = {
        'Status' : responseStatus,
        'Reason' : reason or "See the details in CloudWatch Log Stream: {}".format(context.log_stream_name),
        'PhysicalResourceId' : physicalResourceId or context.log_stream_name,
        'StackId' : event['StackId'],
        'RequestId' : event['RequestId'],
        'LogicalResourceId' : event['LogicalResourceId'],
        'NoEcho' : noEcho,
        'Data' : responseData
    }

    json_responseBody = json.dumps(responseBody)

    print("Response body:")
    print(json_responseBody)

    headers = {
        'content-type' : '',
        'content-length' : str(len(json_responseBody))
    }

    try:
        response = http.request('PUT', responseUrl, headers=headers, body=json_responseBody)
        print("Status code:", response.status)


    except Exception as e:

        print("send(..) failed executing http.request(..):", mask_credentials_and_signature(e))


def mask_credentials_and_signature(message):
    message = re.sub(r'X-Amz-Credential=[^&\s]+', 'X-Amz-Credential=*****', message, flags=re.IGNORECASE)
    return re.sub(r'X-Amz-Signature=[^&\s]+', 'X-Amz-Signature=*****', message, flags=re.IGNORECASE)
```
