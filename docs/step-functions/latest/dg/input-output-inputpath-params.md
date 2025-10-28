# Manipulate parameters in Step Functions workflows

###### Managing state and transforming data

Learn about [Passing data between states with variables](workflow-variables.md "workflow-variables.md") and [Transforming data with JSONata](transforming-data.md "transforming-data.md").

The `InputPath`, `Parameters` and `ResultSelector`
fields provide a way to manipulate JSON as it moves through your workflow.
`InputPath` can limit the input that is passed by filtering the JSON notation by
using a path (see [Using JSONPath paths](amazon-states-language-paths.md "amazon-states-language-paths.md")). With the `Parameters` field,
you can pass a collection of key-value pairs, using either static values or selections from the input using a path.

The `ResultSelector` field provides a way to manipulate the state’s result before
`ResultPath` is applied.

AWS Step Functions applies the `InputPath` field first, and then the
`Parameters` field. You can first filter your raw input to a selection you want
using `InputPath`, and then apply `Parameters` to manipulate that input
further, or add new values. You can then use the `ResultSelector` field to
manipulate the state's output before `ResultPath` is applied.

## InputPath

Use `InputPath` to select a portion of the state input.

For example, suppose the input to your state includes the following.

```
{
  "comment": "Example for InputPath.",
  "dataset1": {
    "val1": 1,
    "val2": 2,
    "val3": 3
  },
  "dataset2": {
    "val1": "a",
    "val2": "b",
    "val3": "c"
  }
}
```

You could apply the `InputPath`.

```
"InputPath": "$.dataset2",
```

With the previous `InputPath`, the following is the JSON that is passed as
the input.

```
{
  "val1": "a",
  "val2": "b",
  "val3": "c"
}
```

###### Note

A path can yield a selection of values. Consider the following example.

```
{ "a": [1, 2, 3, 4] }
```

If you apply the path `$.a[0:2]`, the following is the result.

```
[ 1, 2 ]
```

## Parameters

This section describes the different ways you can use the Parameters field.

### Key-value pairs

Use the `Parameters` field to create a collection of key-value pairs that are passed as input. The values of each can either be static values that you include in your state machine definition, or selected from either the input or the Context object with a path. For key-value pairs where the value is selected using a path, the key name must end in `.$`.

For example, suppose you provide the following input.

```
{
  "comment": "Example for Parameters.",
  "product": {
    "details": {
       "color": "blue",
       "size": "small",
       "material": "cotton"
    },
    "availability": "in stock",
    "sku": "2317",
    "cost": "$23"
  }
}
```

To select some of the information, you could specify these parameters in your state
machine definition.

```
"Parameters": {
        "comment": "Selecting what I care about.",
        "MyDetails": {
          "size.$": "$.product.details.size",
          "exists.$": "$.product.availability",
          "StaticValue": "foo"
        }
      },
```

Given the previous input and the `Parameters` field, this is the JSON that
is passed.

```
{
  "comment": "Selecting what I care about.",
  "MyDetails": {
      "size": "small",
      "exists": "in stock",
      "StaticValue": "foo"
  }
},
```

In addition to the input, you can access a special JSON object, known as the Context object. The Context object includes information about your state machine execution. See
[Accessing execution data from the Context object
in Step Functions](input-output-contextobject.md "input-output-contextobject.md") .

### Connected resources

The `Parameters` field can also pass information to connected resources. For example, if your task state is orchestrating an AWS Batch job, you can pass the relevant API parameters directly to the API actions of that service. For more information, see:

- [Passing parameters to a service API in Step Functions](connect-parameters.md "connect-parameters.md")
- [Integrating services](integrate-services.md "integrate-services.md")

### Amazon S3

If the Lambda function data you are passing between states might grow to more than 262,144 bytes, we recommend using Amazon S3 to store the data, and implement one of the following methods:

- Use the _Distributed Map state_ in your workflow so that the `Map` state can read input directly from Amazon S3 data sources. For more information, see [Distributed mode](state-map-distributed.md "state-map-distributed.md").
- Parse the Amazon Resource Name (ARN) of the bucket in the `Payload` parameter to get the bucket name and key value. For more information, see [Using Amazon S3 ARNs instead of passing large payloads in Step Functions](sfn-best-practices.md#avoid-exec-failures "sfn-best-practices.md#avoid-exec-failures").

Alternatively, you can adjust your implementation to pass smaller payloads in your executions.

## ResultSelector

Use the `ResultSelector` field to manipulate a state's result before
`ResultPath` is applied. The `ResultSelector` field lets you create
a collection of key value pairs, where the values are static or selected from the state's
result. Using the `ResultSelector` field, you can choose what parts of a state's result you want to pass to the `ResultPath` field.

###### Note

With the `ResultPath` field, you can add the output of the `ResultSelector` field to the original input.

`ResultSelector` is an optional field in the following states:

- [Map workflow state](state-map.md "state-map.md")
- [Task workflow state](state-task.md "state-task.md")
- [Parallel workflow state](state-parallel.md "state-parallel.md")

For example, Step Functions service integrations return metadata in addition to the payload in
the result. `ResultSelector` can select portions of the result and merge them
with the state input with `ResultPath`. In this example, we want to select just
the `resourceType` and `ClusterId`, and merge that with the state input
from an Amazon EMR createCluster.sync. Given the following:

```
{
  "resourceType": "elasticmapreduce",
  "resource": "createCluster.sync",
  "output": {
    "SdkHttpMetadata": {
      "HttpHeaders": {
        "Content-Length": "1112",
        "Content-Type": "application/x-amz-JSON-1.1",
        "Date": "Mon, 25 Nov 2019 19:41:29 GMT",
        "x-amzn-RequestId": "1234-5678-9012"
      },
      "HttpStatusCode": 200
    },
    "SdkResponseMetadata": {
      "RequestId": "1234-5678-9012"
    },
    "ClusterId": "AKIAIOSFODNN7EXAMPLE"
  }
}
```

You can then select the `resourceType` and `ClusterId` using
`ResultSelector`:

```
"Create Cluster": {
  "Type": "Task",
  "Resource": "arn:aws:states:::elasticmapreduce:createCluster.sync",
  "Parameters": {
    `<some parameters>`
  },
  "ResultSelector": {
    "ClusterId.$": "$.output.ClusterId",
    "ResourceType.$": "$.resourceType"
  },
  "ResultPath": "$.EMROutput",
  "Next": "Next Step"
}
```

With the given input, using `ResultSelector` produces:

```
{
  "OtherDataFromInput": {},
  "EMROutput": {
      "ClusterId": "AKIAIOSFODNN7EXAMPLE",
      "ResourceType": "elasticmapreduce",
  }
}
```

### Flattening an array of arrays

If the [Parallel workflow state](state-parallel.md "state-parallel.md") or [Map workflow state](state-map.md "state-map.md") state in your state machines return an array of arrays, you can transform them into a flat array with the [ResultSelector](#input-output-resultselector "#input-output-resultselector") field. You can include this field inside the Parallel or Map state definition to manipulate the result of these states.

To flatten arrays, use the syntax: `[*]` in the `ResultSelector` field as shown in the following example.

```
"ResultSelector": {
    "flattenArray.$": "$[*][*]"
  }
```

For examples that show how to flatten an array, see _Step 3_ in the following tutorials:

- [Processing batch data with a Lambda function in Step Functions](tutorial-itembatcher-param-task.md "tutorial-itembatcher-param-task.md")
- [Processing individual items with a Lambda function in Step Functions](tutorial-itembatcher-single-item-process.md "tutorial-itembatcher-single-item-process.md")
