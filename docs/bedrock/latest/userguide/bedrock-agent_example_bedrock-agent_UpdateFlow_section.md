# Use `UpdateFlow` with an AWS SDK

The following code example shows how to use `UpdateFlow`.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-agent#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-agent#code-examples").

Update an Amazon Bedrock Flow.

```
def update_flow(client, flow_id, flow_name, flow_description, role_arn, flow_def):
    """
    Updates an Amazon Bedrock flow.

    Args:
    client: bedrock agent boto3 client.
    flow_id (str): The ID for the flow that you want to update.
    flow_name (str): The name for the flow.
    role_arn (str):  The ARN for the IAM role that use flow uses.
    flow_def (json): The JSON definition of the flow that you want to create.

    Returns:
        dict: Flow information if successful.
    """
    try:

        logger.info("Updating flow: %s.", flow_id)

        response = client.update_flow(
            flowIdentifier=flow_id,
            name=flow_name,
            description=flow_description,
            executionRoleArn=role_arn,
            definition=flow_def
        )

        logger.info("Successfully updated flow: %s. ID: %s",
                    flow_name,
                    {response['id']})

        return response

    except ClientError as e:
        logger.exception("Client error updating flow: %s", {str(e)})
        raise

    except Exception as e:
        logger.exception("Unexepcted error updating flow: %s", {str(e)})
        raise


```

- For API details, see
  [UpdateFlow](../../../goto/boto3/bedrock-agent-2023-12-12/UpdateFlow.md "../../../goto/boto3/bedrock-agent-2023-12-12/UpdateFlow.md")
  in _AWS SDK for Python (Boto3) API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using Amazon Bedrock with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
