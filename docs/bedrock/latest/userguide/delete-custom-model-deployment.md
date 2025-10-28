# Delete a custom model deployment

After you are finished using your model for on-demand inference, you can delete the deployment.
After you delete the deployment, you can't use it for on-demand inference but deployment deletion doesn't delete the underlying custom
model.

You can delete a custom model deployment with the Amazon Bedrock console, AWS Command Line Interface, or AWS SDKs.

###### Important

Deleting a custom model deployment is irreversible. Make sure you no longer need the deployment before
proceeding with the deletion. If you need to use the custom model for on-demand inference again, you
must create a new deployment.

###### Topics

- [Delete a custom model deployment (console)](#delete-deployment-console "#delete-deployment-console")
- [Delete a custom model deployment (AWS Command Line Interface)](#delete-deployment-cli "#delete-deployment-cli")
- [Delete a custom model deployment (AWS SDKs)](#delete-deployment-sdk "#delete-deployment-sdk")

## Delete a custom model deployment (console)

###### To delete a custom model deployment

1. In the navigation pane, under **Infer**, choose
   **Custom model on-demand**.
2. Choose the custom model deployment you want to delete.
3. Choose **Delete**.
4. In the confirmation dialog, enter the deployment name to confirm the deletion.
5. Choose **Delete** to confirm deletion.

## Delete a custom model deployment (AWS Command Line Interface)

To delete a custom model deployment using the AWS Command Line Interface, use the
`delete-custom-model-deployment` command with your deployment identifier.
This command uses the
[DeleteCustomModelDeployment](../APIReference/API_DeleteCustomModelDeployment.md "../APIReference/API_DeleteCustomModelDeployment.md") API operation.

```
aws bedrock delete-custom-model-deployment \
--custom-model-deployment-identifier "`deployment-arn-or-name`" \
--region `region`
```

## Delete a custom model deployment (AWS SDKs)

To delete a custom model deployment programmatically, use the [DeleteCustomModelDeployment](../APIReference/API_DeleteCustomModelDeployment.md "../APIReference/API_DeleteCustomModelDeployment.md")
API operation with the deployment's Amazon Resource Name (ARN) or name. The following code shows how to use the SDK for Python (Boto3) to delete a custom model deployment.

```
def delete_custom_model_deployment(bedrock_client):
    """Delete a custom model deployment

    Args:
        bedrock_client: A boto3 Amazon Bedrock client for making API calls

    Returns:
        dict: The response from the delete operation

    Raises:
        Exception: If there is an error deleting the deployment
    """

    try:
        response = bedrock_client.delete_custom_model_deployment(
            customModelDeploymentIdentifier="`Deployment identifier`"
        )

        print("Deleting deployment...")
        return response

    except Exception as e:
        print(f"Error deleting deployment: {str(e)}")
        raise
```
