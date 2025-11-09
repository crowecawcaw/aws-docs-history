# Flow nodes available in Amazon Bedrock

Amazon Bedrock in SageMaker Unified Studio provides the following node types to build your flow app. A node comprises
of the following:

- Name – The name for the node.
- Type – the type of the node. For more information, see Flow nodes available in Amazon Bedrock.
- Inputs – Provide a name and data type for each input. Some nodes have pre-defined
  names or types that you must use. In the expression
  field, define the part of the whole input to use as the individual input. For more information,
  see [Define inputs with expressions](flows-expressions.md "flows-expressions.md").

In the flow builder, an input appears as a circle on the left edge of a node.
Connect each input to an output of an upstream node.

- Outputs – Provide a name and data type for each output. Some nodes have pre-defined
  names or types that you must use. In the
  flow builder, an output appears as a circle on the right edge of a node. Connect each output to
  at least one input in a downstream node. If an output from a node is sent to more
  than one node, or if a condition node is included, the path of a flow will split into multiple
  branches. Each branch can potentially yield another output in the flow response.
- Configuration – You define node-specific fields at the top of the
  node.

###### Note

Amazon Bedrock in SageMaker Unified Studio supports a subset of the nodes that are available in Amazon Bedrock. For more
information, see [Node
types in flow](../../../bedrock/latest/userguide/flows-nodes.md "../../../bedrock/latest/userguide/flows-nodes.md").

###### Nodes

- [Input node](#flow-node-input "#flow-node-input")
- [Output node](#flow-node-output "#flow-node-output")
- [Collector node](#flow-node-collector "#flow-node-collector")
- [Condition node](#flow-node-condition "#flow-node-condition")
- [Iterator node](#flow-node-iterator "#flow-node-iterator")
- [Iterator node outputs](#flow-node-iterator-outputs "#flow-node-iterator-outputs")
- [Prompt node](#flow-node-prompt "#flow-node-prompt")
- [Knowledge Base node](#flow-node-kb "#flow-node-kb")
- [Agent node](#flow-node-agent "#flow-node-agent")
- [S3 storage node](#flow-node-s3-storage "#flow-node-s3-storage")
- [S3 retrieval node](#flow-node-s3-retrieval "#flow-node-s3-retrieval")
- [Adding an Amazon S3 bucket](#adding-s3-bucket "#adding-s3-bucket")

## Input node

Every flow contains only one flow input node and must begin with it. When you run the flow,
the input is fed into this node and the configured output is passed to the next
step.

### Input node inputs

| Name | Type | Expression |
| ---- | ---- | ---------- |
| N/A  | N/A  | N/A        |

### Input node outputs

| Name     | Type                                       |
| -------- | ------------------------------------------ |
| document | String, Number, Boolean, Object and Array. |

## Output node

A flow output node extracts the input data from the previous node, based on the defined
expression, and returns it.
A flow can have multiple flow output nodes if there are multiple branches in the flow.

### Output node inputs

| Name     | Type                                        | Expression |
| -------- | ------------------------------------------- | ---------- |
| document | String, Number, Boolean, Object, and Array. | Yes        |

### Input node outputs

| Name | Type |
| ---- | ---- |
| N/A  | N/A  |

## Collector node

A collector node takes an iterated input, in addition to the size that the array will be,
and returns them as an array. You can use a collector node downstream from an iterator node to
collect the iterated items after sending them through some nodes.

### Collector inputs

| Name      | Type   | Expression |
| --------- | ------ | ---------- | ------- | ------ | ----- | --- |
| arrayItem | String | Number     | Boolean | Object | Array | Yes |
| arraySize | Number | Yes        |

### Collector outputs

| Name           | Type  |
| -------------- | ----- |
| collectedArray | Array |

## Condition node

A condition node sends data from the previous node to different nodes, depending on the
conditions that are defined. A condition node can take multiple inputs.

- **Node name** – Any
- **Input field name** – Any
- **Input field types** – String, Number, Boolean, Object and Array.
- **Input expression** – Yes
- **Condition field name** – Any
- **Output field types** – String, Number, Boolean, Object and Array.
- **Output expression** – Yes

### Condition expressions

To define a condition, you refer to an input by its name and compare it to
a value using any of the following relational operators:

| Operator | Meaning                                     | Supported data types    | Example usage | Example meaning                    |
| -------- | ------------------------------------------- | ----------------------- | ------------- | ---------------------------------- |
| ==       | Equal to (the data type must also be equal) | String, Number, Boolean | A == B        | If A is equal to B                 |
| !=       | Not equal to                                | String, Number, Boolean | A != B        | If A isn't equal to B              |
| >        | Greater than                                | Number                  | A > B         | If A is greater than B             |
| >=       | Greater than or equal to                    | Number                  | A >= B        | If A is greater than or equal to B |
| <        | Less than                                   | Number                  | A < B         | If A is less than B                |
| <=       | Less than or equal to                       | Number                  | A <= B        | If A is less than or equal to B    |

You can compare inputs to other inputs or to a constant in a conditional expression. For
example, if you have a numerical input called `profit` and another one called
`expenses`, both `profit > expenses` or `profit
 <= 1000` are valid expressions.

You can use the following logical operators to combine expressions for more complex
conditions. We recommend that you use parentheses to resolve ambiguities in grouping of
expressions:

| Operator | Meaning                         | Example usage        | Example meaning                                                                 |
| -------- | ------------------------------- | -------------------- | ------------------------------------------------------------------------------- |
| and      | Both expressions are true       | (A < B) and (C == 1) | If both expressions are true:<br>• A is less than B<br>• C is equal to 1        |
| or       | At least one expression is true | (A != 2) or (B > C)  | If either expressions is true:<br>• A isn't equal to B<br>• B is greater than C |
| not      | The expression isn't true       | not (A > B)          | If A isn't greater than B (equivalent to A <=<br>B)                             |

## Iterator node

An iterator node takes an array and iteratively returns its items as output to the
downstream node. The inputs to the iterator node are processed one by one and not in parallel
with each other. The flow output node returns the final result for each input in a different
response. You can use also use a collector node downstream from the iterator node to collect the
iterated responses and return them as an array, in addition to the size of the array.

### Iterator node inputs

| Name  | Type  | Expression |
| ----- | ----- | ---------- |
| array | Array | Yes        |

## Iterator node outputs

| Name      | Type   |
| --------- | ------ | ------ | ------- | ------ | ----- |
| arrayItem | String | Number | Boolean | Object | Array |
| arraySize | Number |

## Prompt node

A prompt node defines a prompt to use in the flow. The inputs to the prompt node are
values to fill in the variables that you define for the prompt. The output is the generated
response from the model. For more information, see [Reuse and share Amazon Bedrock prompts](prompt-mgmt.md "prompt-mgmt.md").

- **Node name** – Any
- **Prompt** – The [prompt](prompt-mgmt.md "prompt-mgmt.md") that the prompt node uses.
- **Version** – The [prompt](prompt-mgmt.md "prompt-mgmt.md") the version of the prompt to use.

You can assign a guardrail to a prompt node. When you create the prompt node, you can choose to create a new guardrail or
select an existing guardrail. For more information, see [Safeguard your Amazon Bedrock app with a guardrail](guardrails.md "guardrails.md").

### Prompt node inputs

| Name | Type                                       | Expression |
| ---- | ------------------------------------------ | ---------- |
| Any  | String, Number, Boolean, Object and Array. | Yes        |

### Prompt node outputs

| Name            | Type   |
| --------------- | ------ |
| modelCompletion | String |

## Knowledge Base node

A knowledge base node lets you send a query to a knowledge base and get response that the flow sends to
the next node. For more information, see [Use a Local file as a data source](data-source-document.md "data-source-document.md").

- **Node name** – Any
- **Knowledge base** – The [Knowledge Base](data-source-document.md "data-source-document.md") that the node uses.
- **Response type** – The model that the node uses to generate a response.

### Knowledge base node inputs

| Name           | Type   | Expression |
| -------------- | ------ | ---------- |
| retrievalQuery | String | Yes        |

### Knowledge base node outputs

| Name       | Type   |
| ---------- | ------ |
| outputText | String |

You can assign a guardrail to a knowledge base node. When you create the knowledge base node, you can choose to create a new guardrail or
select an existing guardrail. For more information, see [Safeguard your Amazon Bedrock app with a guardrail](guardrails.md "guardrails.md").

## Agent node

An agent node lets you send a prompt to an agent, which orchestrates between foundation
models and associated resources to identify and carry out actions for an end-user. The inputs
into the node are the prompt for the agent and any associated prompt or session attributes. For more information,
see [Control agent session context](../../../bedrock/latest/userguide/agents-session-state.md "../../../bedrock/latest/userguide/agents-session-state.md")
in the _Amazon Bedrock user guide_.

### Agent node inputs

| Name              | Type                                   | Expression |
| ----------------- | -------------------------------------- | ---------- |
| agentInputText    | String, Number, Boolean, Object, Array | string     |
| promptAttributes  | Object                                 | string     |
| sessionAttributes | Object                                 | string     |

### Agent node outputs

| Name          | Type   |
| ------------- | ------ |
| agentResponse | String |

## S3 storage node

An Amazon S3 Storage Node takes an object key and flow data as input. The flow data is stored in an Amazon S3 object specified by the object key,
and the node returns the Amazon S3 URI where the data is stored. The Amazon S3 bucket can be specified in the configuration settings of the node.

### S3 storage node inputs

| Name      | Type                                   | Expression |
| --------- | -------------------------------------- | ---------- |
| content   | String, Number, Boolean, Object, Array | Yes        |
| objectKey | String                                 | Yes        |

### S3 storage node outputs

| Name  | Type   |
| ----- | ------ |
| s3Uri | String |

## S3 retrieval node

An Amazon S3 Retrieval Node takes an object key as input and returns the data from the Amazon S3 object specified by the object key.
The Amazon S3 bucket can be specified in the configuration settings of the node.

### S3 retrieval node inputs

| Name      | Type   | Expression |
| --------- | ------ | ---------- |
| objectKey | String | Yes        |

### S3 retrieval node outputs

| Name      | Type   |
| --------- | ------ |
| s3Content | String |

## Adding an Amazon S3 bucket

To use S3 storage and retrieval flow nodes, you must first set up a connection with an Amazon S3 bucket.
Amazon S3 buckets that are already within your project can be connected to automatically through a default S3 connection.
If you want to use an S3 bucket from outside of your project, you will need to set up an S3 connection using the steps below.

###### To connect to an S3 bucket outside of your project:

1. Navigate to the data section under your project overview.
2. Select **Add**.
3. Select **Add S3 location**, then select **Next**.
4. Follow the steps for Prerequisite option 2 in [Adding Amazon S3 data](adding-existing-s3-data.md "adding-existing-s3-data.md") to create the S3 connection and configure the correct permissions. Alternatively, you can use the following JSON policy to add permissions for an S3 storage node:

```
{
    "Sid": "WriteToS3Bucket",
    "Effect": "Allow",
    "Action": [
        "s3:PutObject"
    ],
    "Resource": [
        "arn:aws:s3:::${bucket-name}",
        "arn:aws:s3:::${bucket-name}/*"
    ],
    "Condition": {
        "StringEquals": {
            "aws:ResourceAccount": "${account-id}"
        }
    }
}
```

And the following JSON policy to add permissions for an S3 retrieval node:

```
{
    "Sid": "AccessS3Bucket",
    "Effect": "Allow",
    "Action": [
        "s3:GetObject"
    ],
    "Resource": [
        "arn:aws:s3:::${bucket-name}/*"
    ],
    "Condition": {
        "StringEquals": {
            "aws:ResourceAccount": "${account-id}"
        }
    }
}
```
