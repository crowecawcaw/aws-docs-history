# Passing parameters to a service API in Step Functions

###### Managing state and transforming data

Learn about [Passing data between states with variables](workflow-variables.md "workflow-variables.md") and [Transforming data with JSONata](transforming-data.md "transforming-data.md").

Use the `Parameters` field in a `Task` state to control what parameters are passed to a service API.

Inside the `Parameters` field, you must use the plural form of the array parameters in an API action. For example, if you use the [Filter](../../../AWSEC2/latest/APIReference/API_DescribeSnapshots.md#API_DescribeSnapshots_RequestParameters "../../../AWSEC2/latest/APIReference/API_DescribeSnapshots.md#API_DescribeSnapshots_RequestParameters") field of the `DescribeSnapshots` API action for integrating with Amazon EC2, you must define the field as `Filters`. If you don't use the plural form, Step Functions returns the following error:

```
The field Filter is not supported by Step Functions.
```

## Pass static JSON as parameters

You can include a JSON object directly in your state machine definition to pass as a parameter to a resource.

For example, to set the `RetryStrategy` parameter for the `SubmitJob` API for AWS Batch, you could include the following in your parameters.

```
"RetryStrategy": {
  "attempts": 5
}
```

You can also pass multiple parameters with static JSON. As a more complete example, the following are the `Resource` and `Parameters` fields of the specification of a task that
publishes
to an Amazon SNS topic named `myTopic`.

```
"Resource": "arn:aws:states:::sns:publish",
  "Parameters": {
     "TopicArn": "arn:aws:sns:us-east-2:`account-id`:`myTopic`",
     "Message": "test message",
     "MessageAttributes": {
       "my attribute no 1": {
         "DataType": "String",
         "StringValue": "value of my attribute no 1"
       },
       "my attribute no 2": {
         "DataType": "String",
         "StringValue": "value of my attribute no 2"
       }
     }
  },
```

## Pass state input as parameters using Paths

You can pass portions of the state input as parameters by using [paths](amazon-states-language-paths.md "amazon-states-language-paths.md"). A path is a string, beginning with `$`, that's used to identify components within JSON text. Step Functions paths use [JsonPath](https://datatracker.ietf.org/wg/jsonpath/about/ "https://datatracker.ietf.org/wg/jsonpath/about/") syntax.

To specify that a parameter use a path, end the parameter name with `.$`. For example, if your state input contains text within a node named `message`, you could pass that text as a parameter using a path.

Consider the following state input:

```
{
  "comment": "A message in the state input",
  "input": {
    "message": "foo",
    "otherInfo": "bar"
  },
  "data": "example"
}
```

To pass the value of the node named `message` as a parameter named `myMessage`, specify the following syntax:

```
"Parameters": {"myMessage.$": "$.input.message"},
```

Step Functions then passes the value `foo` as a parameter.

For more information about using parameters in Step Functions, see the following:

- [Processing input and output](concepts-input-output-filtering.md "concepts-input-output-filtering.md")
- [Manipulate parameters in Step Functions workflows](input-output-inputpath-params.md "input-output-inputpath-params.md")

## Pass Context object nodes as parameters

In addition to static content, and nodes from the state input, you can pass nodes from the
Context object as parameters. The Context object is dynamic JSON data that exists during a
state machine execution. It includes information about your state machine and the current
execution. You can access the Context object using a path in the `Parameters`
field of a state definition.

For more information about the Context object and how to access that data from a
`"Parameters"` field, see the following:

- [Accessing execution data from the Context object
  in Step Functions](input-output-contextobject.md "input-output-contextobject.md")
- [Accessing the Context object](input-output-contextobject.md#contextobject-access "input-output-contextobject.md#contextobject-access")
- [Get a Token from the Context object](connect-to-resource.md#wait-token-contextobject "connect-to-resource.md#wait-token-contextobject")
