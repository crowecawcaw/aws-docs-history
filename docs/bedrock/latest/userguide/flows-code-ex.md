# Run Amazon Bedrock Flows code samples

The following code samples assume that you've fulfilled the following prerequisites:

1. Set up a role to have permissions to Amazon Bedrock actions. If you haven't, refer to [Quickstart](getting-started.md "getting-started.md").
2. Set up your credentials to use the AWS API. If you haven't, refer to [Get started with the API](getting-started-api.md "getting-started-api.md").
3. Create a service role to carry out flow-related actions on your behalf. If you haven't, refer to [Create a service role for Amazon Bedrock Flows in Amazon Bedrock](flows-permissions.md "flows-permissions.md").
   To create a flow, send a [CreateFlow](../APIReference/API_agent_CreateFlow.md "../APIReference/API_agent_CreateFlow.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt"). For example code, see Run Amazon Bedrock Flows code samples

The following fields are required:

| Field            | Basic description                                                                                                       |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------- |
| name             | A name for the flow.                                                                                                    |
| executionRoleArn | The ARN of the [service role with permissions to create and manage flows](flows-permissions.md "flows-permissions.md"). |

The following fields are optional:

| Field                    | Use case                                                                                                                                                                                                    |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| definition               | Contains the `nodes` and `connections` that make up the flow.                                                                                                                                               |
| description              | To describe the flow.                                                                                                                                                                                       |
| tags                     | To associate tags with the flow. For more information, see [Tagging Amazon Bedrock resources](tagging.md "tagging.md").                                                                                     |
| customerEncryptionKeyArn | To encrypt the resource with a KMS key. For more information, see [Encryption of Amazon Bedrock Flows resources](encryption-flows.md "encryption-flows.md").                                                |
| clientToken              | To ensure the API request completes only once. For more information, see [Ensuring idempotency](../../../ec2/latest/devguide/ec2-api-idempotency.md "../../../ec2/latest/devguide/ec2-api-idempotency.md"). |

While the `definition` field is optional, it is required for the flow to be functional. You can choose to create a flow without the definition first and instead update the flow later.

For each node in your `nodes` list, you specify the type of node in the `type` field and provide the corresponding configuration of the node in the `config` field. For details about the API structure of different types of nodes, see [Node types for your flow](flows-nodes.md "flows-nodes.md").

To try out some code samples for Amazon Bedrock Flows, choose the tab for your preferred method, and then follow the steps:

Python

1.  Create a flow using a [CreateFlow](../APIReference/API_agent_CreateFlow.md "../APIReference/API_agent_CreateFlow.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt") with the following nodes:

        * An input node.
        * A prompt node with a prompt defined inline that creates a music playlist using two variables (`genre` and `number`).
        * An output node that returns the model completion.

    Run the following code snippet to load the AWS SDK for Python (Boto3), create an Amazon Bedrock Agents client, and create a flow with the nodes (replace the `executionRoleArn` field with the ARN of your the service role that you created for flow):

```
# Import Python SDK and create client
import boto3

client = boto3.client(service_name='bedrock-agent')

# Replace with the service role that you created. For more information, see https://docs.aws.amazon.com/bedrock/latest/userguide/flows-permissions.html
FLOWS_SERVICE_ROLE = "arn:aws:iam::123456789012:role/MyFlowsRole"

# Define each node

# The input node validates that the content of the InvokeFlow request is a JSON object.
input_node = {
    "type": "Input",
    "name": "FlowInput",
    "outputs": [
        {
            "name": "document",
            "type": "Object"
        }
    ]
}

# This prompt node defines an inline prompt that creates a music playlist using two variables.
# 1. {{genre}} - The genre of music to create a playlist for
# 2. {{number}} - The number of songs to include in the playlist
# It validates that the input is a JSON object that minimally contains the fields "genre" and "number", which it will map to the prompt variables.
# The output must be named "modelCompletion" and be of the type "String".
prompt_node = {
    "type": "Prompt",
    "name": "MakePlaylist",
    "configuration": {
        "prompt": {
            "sourceConfiguration": {
                "inline": {
                    "modelId": "amazon.nova-lite-v1:0",
                    "templateType": "TEXT",
                    "inferenceConfiguration": {
                        "text": {
                            "temperature": 0.8
                        }
                    },
                    "templateConfiguration": {
                        "text": {
                            "text": "Make me a {{genre}} playlist consisting of the following number of songs: {{number}}."
                        }
                    }
                }
            }
        }
    },
    "inputs": [
        {
            "name": "genre",
            "type": "String",
            "expression": "$.data.genre"
        },
        {
            "name": "number",
            "type": "Number",
            "expression": "$.data.number"
        }
    ],
    "outputs": [
        {
            "name": "modelCompletion",
            "type": "String"
        }
    ]
}

# The output node validates that the output from the last node is a string and returns it as is. The name must be "document".
output_node = {
    "type": "Output",
    "name": "FlowOutput",
    "inputs": [
        {
            "name": "document",
            "type": "String",
            "expression": "$.data"
        }
    ]
}

# Create connections between the nodes
connections = []

#   First, create connections between the output of the flow input node and each input of the prompt node
for input in prompt_node["inputs"]:
    connections.append(
        {
            "name": "_".join([input_node["name"], prompt_node["name"], input["name"]]),
            "source": input_node["name"],
            "target": prompt_node["name"],
            "type": "Data",
            "configuration": {
                "data": {
                    "sourceOutput": input_node["outputs"][0]["name"],
                    "targetInput": input["name"]
                }
            }
        }
    )

# Then, create a connection between the output of the prompt node and the input of the flow output node
connections.append(
    {
        "name": "_".join([prompt_node["name"], output_node["name"]]),
        "source": prompt_node["name"],
        "target": output_node["name"],
        "type": "Data",
        "configuration": {
            "data": {
                "sourceOutput": prompt_node["outputs"][0]["name"],
                "targetInput": output_node["inputs"][0]["name"]
            }
        }
    }
)

# Create the flow from the nodes and connections
response = client.create_flow(
    name="FlowCreatePlaylist",
    description="A flow that creates a playlist given a genre and number of songs to include in the playlist.",
    executionRoleArn=FLOWS_SERVICE_ROLE,
    definition={
        "nodes": [input_node, prompt_node, output_node],
        "connections": connections
    }
)

flow_id = response.get("id")
```

2. List the flows in your account, including the one you just created, by running the following code snippet to make a [ListFlows](../APIReference/API_agent_ListFlows.md "../APIReference/API_agent_ListFlows.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt"):

```
client.list_flows()
```

3. Get information about the flow that you just created by running the following code snippet to make a [GetFlow](../APIReference/API_agent_GetFlow.md "../APIReference/API_agent_GetFlow.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt"):

```
client.get_flow(flowIdentifier=flow_id)
```

4. Prepare your flow so that the latest changes from the working draft are applied and so that it's ready to version. Run the following code snippet to make a [PrepareFlow](../APIReference/API_agent_PrepareFlow.md "../APIReference/API_agent_PrepareFlow.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt"):

```
client.prepare_flow(flowIdentifier=flow_id)
```

5. Version the working draft of your flow to create a static snapshot of your flow and then retrieve information about it with the following actions:
   1. Create a version by running the following code snippet to make a [CreateFlowVersion](../APIReference/API_agent_CreateFlowVersion.md "../APIReference/API_agent_CreateFlowVersion.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt"):

   ```
   response = client.create_flow_version(flowIdentifier=flow_id)

   flow_version = response.get("version")
   ```

   2. List all versions of your flow by running the following code snippet to make a [ListFlowVersions](../APIReference/API_agent_ListFlowVersions.md "../APIReference/API_agent_ListFlowVersions.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt"):

   ```
   client.list_flow_versions(flowIdentifier=flow_id)
   ```

   3. Get information about the version by running the following code snippet to make a [GetFlowVersion](../APIReference/API_agent_GetFlowVersion.md "../APIReference/API_agent_GetFlowVersion.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt"):

   ```
   client.get_flow_version(flowIdentifier=flow_id, flowVersion=flow_version)
   ```

6. Create an alias to point to the version of your flow that you created and then retrieve information about it with the following actions:
   1. Create an alias and point it to the version you just created by running the following code snippet to make a [CreateFlowAlias](../APIReference/API_agent_CreateFlowAlias.md "../APIReference/API_agent_CreateFlowAlias.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt"):

   ```
   response = client.create_flow_alias(
       flowIdentifier=flow_id,
       name="latest",
       description="Alias pointing to the latest version of the flow.",
       routingConfiguration=[
           {
               "flowVersion": flow_version
           }
       ]
   )

   flow_alias_id = response.get("id")
   ```

   2. List all aliases of your flow by running the following code snippet to make a [ListFlowAliass](../APIReference/API_agent_ListFlowAliass.md "../APIReference/API_agent_ListFlowAliass.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt"):

   ```
   client.list_flow_aliases(flowIdentifier=flow_id)
   ```

   3. Get information about the alias that you just created by running the following code snippet to make a [GetFlowAlias](../APIReference/API_agent_GetFlowAlias.md "../APIReference/API_agent_GetFlowAlias.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt"):

   ```
   client.get_flow_alias(flowIdentifier=flow_id, aliasIdentifier=flow_alias_id)
   ```

7. Run the following code snippet to create an Amazon Bedrock Agents Runtime client and invoke a flow. The request fills in the variables in the prompt in your flow and returns the response from the model to make a [InvokeFlow](../APIReference/API_agent-runtime_InvokeFlow.md "../APIReference/API_agent-runtime_InvokeFlow.md") request with an [Agents for Amazon Bedrock runtime endpoint](../../../general/latest/gr/bedrock.md#bra-rt "../../../general/latest/gr/bedrock.md#bra-rt"):

```
client_runtime = boto3.client('bedrock-agent-runtime')

response = client_runtime.invoke_flow(
    flowIdentifier=flow_id,
    flowAliasIdentifier=flow_alias_id,
    inputs=[
        {
            "content": {
                "document": {
                    "genre": "pop",
                    "number": 3
                }
            },
            "nodeName": "FlowInput",
            "nodeOutputName": "document"
        }
    ]
)

result = {}

for event in response.get("responseStream"):
    result.update(event)

if result['flowCompletionEvent']['completionReason'] == 'SUCCESS':
    print("Flow invocation was successful! The output of the flow is as follows:\n")
    print(result['flowOutputEvent']['content']['document'])

else:
    print("The flow invocation completed because of the following reason:", result['flowCompletionEvent']['completionReason'])
```

The response should return a playlist of pop music with three songs. 8. Delete the alias, version, and flow that you created with the following actions:

    1. Delete the alias by running the following code snippet to make a [DeleteFlowAlias](../APIReference/API_agent_DeleteFlowAlias.md "../APIReference/API_agent_DeleteFlowAlias.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt"):



    ```
    client.delete_flow_alias(flowIdentifier=flow_id, aliasIdentifier=flow_alias_id)
    ```
    2. Delete the version by running the following code snippet to make a [DeleteFlowVersion](../APIReference/API_agent_DeleteFlowVersion.md "../APIReference/API_agent_DeleteFlowVersion.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt"):



    ```
    client.delete_flow_version(flowIdentifier=flow_id, flowVersion=flow_version)
    ```
    3. Delete the flow by running the following code snippet to make a [DeleteFlow](../APIReference/API_agent_DeleteFlow.md "../APIReference/API_agent_DeleteFlow.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt"):



    ```
    client.delete_flow(flowIdentifier=flow_id)
    ```
