# Processing individual items with a Lambda function in Step Functions

In this tutorial, you use the _Distributed Map state_'s [ItemBatcher (Map)](input-output-itembatcher.md "input-output-itembatcher.md") field to iterate over individual items present in a batch using a Lambda function. The _Distributed Map state_ starts four child workflow executions. Each of these child workflows runs an _Inline Map state_. For its each iteration, the _Inline Map state_ invokes a Lambda function and passes a single item from the batch to the function. The Lambda function then processes the item and returns the result.

You'll create a state machine that performs multiplication on an array of integers. Say that the integer array you provide as input is `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` and the multiplication factor is `7`. Then, the resulting array formed after multiplying these integers with a factor of 7, will be `[7, 14, 21, 28, 35, 42, 49, 56, 63, 70]`.

## Step 1: Create the state machine

In this step, you create the workflow prototype of the state machine that passes a single item from a batch of items to each invocation of the Lambda function you'll create in [Step 2](#itembatcher-single-item-process-config-resource "#itembatcher-single-item-process-config-resource").

- Use the following definition to create a state machine using the [Step Functions console](https://console.aws.amazon.com/states/home?region=us-east-1#/ "https://console.aws.amazon.com/states/home?region=us-east-1#/"). For information about creating a state machine, see [Step 1: Create the workflow prototype](tutorial-map-distributed.md#use-dist-map-create-workflow "tutorial-map-distributed.md#use-dist-map-create-workflow") in the [Getting started with using Distributed Map state](tutorial-map-distributed.md "tutorial-map-distributed.md") tutorial.

In this state machine, you define a _Distributed Map state_ that accepts an array of 10 integers as input and passes these array items to the child workflow executions in batches. Each child workflow execution receives a batch of three items as input and runs an _Inline Map state_. Every iteration of the _Inline Map state_ invokes a Lambda function and passes an item from the batch to the function. This function then multiplies the item with a factor of `7` and returns the result.

The output of each child workflow execution is a JSON array that contains the multiplication result for each of the items passed.

###### Important

Make sure to replace the Amazon Resource Name (ARN) of the Lambda function in the following code with the ARN of the function you'll create in [Step 2](#itembatcher-single-item-process-config-resource "#itembatcher-single-item-process-config-resource").

```
{
  "StartAt": "Pass",
  "States": {
    "Pass": {
      "Type": "Pass",
      "Next": "Map",
      "Result": {
        "MyMultiplicationFactor": 7,
        "MyItems": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
      }
    },
    "Map": {
      "Type": "Map",
      "ItemProcessor": {
        "ProcessorConfig": {
          "Mode": "DISTRIBUTED",
          "ExecutionType": "STANDARD"
        },
        "StartAt": "InnerMap",
        "States": {
          "InnerMap": {
            "Type": "Map",
            "ItemProcessor": {
              "ProcessorConfig": {
                "Mode": "INLINE"
              },
              "StartAt": "Lambda Invoke",
              "States": {
                "Lambda Invoke": {
                  "Type": "Task",
                  "Resource": "arn:aws:states:::lambda:invoke",
                  "OutputPath": "$.Payload",
                  "Parameters": {
                    "Payload.$": "$",
                    "FunctionName": "arn:aws:lambda:`region`:`account-id`:function:`functionName`"
                  },
                  "Retry": [
                    {
                      "ErrorEquals": [
                        "Lambda.ServiceException",
                        "Lambda.AWSLambdaException",
                        "Lambda.SdkClientException",
                        "Lambda.TooManyRequestsException"
                      ],
                      "IntervalSeconds": 2,
                      "MaxAttempts": 6,
                      "BackoffRate": 2
                    }
                  ],
                  "End": true
                }
              }
            },
            "End": true,
            "ItemsPath": "$.Items",
            "ItemSelector": {
              "MyMultiplicationFactor.$": "$.BatchInput.MyMultiplicationFactor",
              "MyItem.$": "$$.Map.Item.Value"
            }
          }
        }
      },
      "End": true,
      "Label": "Map",
      "MaxConcurrency": 1000,
      "ItemsPath": "$.MyItems",
      "ItemBatcher": {
        "MaxItemsPerBatch": 3,
        "BatchInput": {
          "MyMultiplicationFactor.$": "$.MyMultiplicationFactor"
        }
      }
    }
  }
}
```

## Step 2: Create the Lambda function

In this step, you create the Lambda function that processes each item passed from the batch.

###### Important

Ensure that your Lambda function is under the same AWS Region as your state machine.

###### To create the Lambda function

1. Use the [Lambda console](https://console.aws.amazon.com/lambda/home "https://console.aws.amazon.com/lambda/home") to create a **Python** Lambda function named `ProcessSingleItem`. For information about creating a Lambda function, see [Step 4: Configure the Lambda function](tutorial-map-distributed.md#use-dist-map-config-resource "tutorial-map-distributed.md#use-dist-map-config-resource") in the [Getting started with using Distributed Map state](tutorial-map-distributed.md "tutorial-map-distributed.md") tutorial.
2. Copy the following code for the Lambda function and paste it into the **Code source** section of your Lambda function.

```
import json

def lambda_handler(event, context):

    multiplication_factor = event['MyMultiplicationFactor']
    item = event['MyItem']

    result = multiplication_factor * item

    return {
        'statusCode': 200,
        'multiplied': result
    }
```

3. After you create your Lambda function, copy the function's ARN displayed in the upper-right corner of the page. The following is an example ARN, where `function-name` is the name of the
   Lambda function (in this case, `ProcessSingleItem`):

```
arn:aws:lambda:`region`:123456789012:function:`function-name`
```

You'll need to provide the function ARN in the state machine you created in [Step 1](#itembatcher-single-item-process-create-state-machine "#itembatcher-single-item-process-create-state-machine"). 4. Choose **Deploy** to deploy the changes.

## Step 3: Run the state machine

When you run the [state machine](#itembatcher-single-item-process-create-state-machine "#itembatcher-single-item-process-create-state-machine"), the _Distributed Map state_ starts four child workflow executions, where each execution processes three items, while one execution processes a single item.

The following example shows the data passed to one of the [ProcessSingleItem](#itembatcher-single-item-process-config-resource "#itembatcher-single-item-process-config-resource") function invocations inside a child workflow execution.

```
{
  "MyMultiplicationFactor": 7,
  "MyItem": 1
}
```

Given this input, the following example shows the output that is returned by the Lambda function.

```
{
  "statusCode": 200,
  "multiplied": 7
}
```

The following example shows the output JSON array for one of the child workflow executions.

```
[
  {
    "statusCode": 200,
    "multiplied": 7
  },
  {
    "statusCode": 200,
    "multiplied": 14
  },
  {
    "statusCode": 200,
    "multiplied": 21
  }
]
```

The state machine returns the following output that contains four arrays for the four child workflow executions. These arrays contain the multiplication results of the individual input items.

Finally, the state machine output is an array named `multiplied` that combines all the multiplication results returned for the four child workflow executions.

```
[
  [
    {
      "statusCode": 200,
      "multiplied": 7
    },
    {
      "statusCode": 200,
      "multiplied": 14
    },
    {
      "statusCode": 200,
      "multiplied": 21
    }
  ],
  [
    {
      "statusCode": 200,
      "multiplied": 28
    },
    {
      "statusCode": 200,
      "multiplied": 35
    },
    {
      "statusCode": 200,
      "multiplied": 42
    }
  ],
  [
    {
      "statusCode": 200,
      "multiplied": 49
    },
    {
      "statusCode": 200,
      "multiplied": 56
    },
    {
      "statusCode": 200,
      "multiplied": 63
    }
  ],
  [
    {
      "statusCode": 200,
      "multiplied": 70
    }
  ]
]
```

To combine all the multiplication results returned by the child workflow executions into a single output array, you can use the [ResultSelector](input-output-inputpath-params.md#input-output-resultselector "input-output-inputpath-params.md#input-output-resultselector") field. Define this field inside the _Distributed Map state_ to find all the results, extract the individual results, and then combine them into a single output array named `multiplied`.

To use the `ResultSelector` field, update your state machine definition as shown in the following example.

```
{
  "StartAt": "Pass",
  "States": {
    ...
    ...
    "Map": {
      "Type": "Map",
      ...
      ...
      "ItemBatcher": {
        "MaxItemsPerBatch": 3,
        "BatchInput": {
          "MyMultiplicationFactor.$": "$.MyMultiplicationFactor"
        }
      },
      "ItemsPath": "$.MyItems",
      **"ResultSelector": {
 "multiplied.$": "$..multiplied"
 }**
    }
  }
}
```

The updated state machine returns a consolidated output array as shown in the following example.

```
{
  "multiplied": [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
}
```
