# Deploy a custom model

You can deploy a custom model with the Amazon Bedrock console, AWS Command Line Interface, or AWS SDKs. For information about using the deployment for inference, see [Use a deployment for on-demand inference](use-custom-model-on-demand.md "use-custom-model-on-demand.md").

###### Topics

- [Deploy a custom model (console)](#deploy-custom-model-console "#deploy-custom-model-console")
- [Deploy a custom model (AWS Command Line Interface)](#deploy-custom-model-cli "#deploy-custom-model-cli")
- [Deploy a custom model (AWS SDKs)](#deploy-custom-model-sdk "#deploy-custom-model-sdk")

## Deploy a custom model (console)

You deploy a custom model from the **Custom models** page as follows. You can also deploy a model from the **Custom model on-demand** page with the same fields.
To find this page, under **Infer** in the navigation pane, choose **Custom model on-demand**.

###### To deploy a custom model

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. From the left navigation pane, choose **Custom models** under **Tune**.
3. In the **Models** tab, choose the radio button for the model you want to deploy.
4. Choose **Set up inference** and choose **Deploy for on-demand**.
5. In **Deployment details**, provide the following information:
   - **Deployment Name** (required) – Enter a unique name for your deployment.
   - **Description** (optional) – Enter a description for your deployment.
   - **Tags** (optional) – Add tags for cost allocation and resource management.

6. Choose **Create**.
   When the deployment's status is `Active`, your custom model is ready for on-demand inference. For
   more information about using the custom model, see [Use a deployment for on-demand inference](use-custom-model-on-demand.md "use-custom-model-on-demand.md").

## Deploy a custom model (AWS Command Line Interface)

To deploy a custom model for on-demand inference using the AWS Command Line Interface, use the
`create-custom-model-deployment` command with your custom model's Amazon Resource Name (ARN).
This command uses the [CreateCustomModelDeployment](../APIReference/API_CreateCustomModelDeployment.md "../APIReference/API_CreateCustomModelDeployment.md") API operation. The response includes the deployment's ARN. When the deployment is active, you use this ARN as the `modelId` when
making inference requests. For information about using the deployment for inference, see [Use a deployment for on-demand inference](use-custom-model-on-demand.md "use-custom-model-on-demand.md").

```
aws bedrock create-custom-model-deployment \
--model-deployment-name "`Unique name`" \
--model-arn "`Custom Model ARN`" \
--description "`Deployment description`" \
--tags '[
    {
        "key": "Environment",
        "value": "Production"
    },
    {
        "key": "Team",
        "value": "ML-Engineering"
    },
    {
        "key": "Project",
        "value": "CustomerSupport"
    }
]' \
--client-request-token "`unique-deployment-token`" \
--region `region`
```

## Deploy a custom model (AWS SDKs)

To deploy a custom model for on-demand inference, use the
[CreateCustomModelDeployment](../APIReference/API_CreateCustomModelDeployment.md "../APIReference/API_CreateCustomModelDeployment.md") API operation with your custom model's Amazon Resource Name (ARN).
The response includes the deployment's ARN. When the deployment is active, you use this ARN as the `modelId` when
making inference requests. For information about using the deployment for inference, see [Use a deployment for on-demand inference](use-custom-model-on-demand.md "use-custom-model-on-demand.md").

The following code shows how to use the SDK for Python (Boto3) to deploy a custom model.

```
def create_custom_model_deployment(bedrock_client):
    """Create a custom model deployment
    Args:
        bedrock_client: A boto3 Amazon Bedrock client for making API calls

    Returns:
        str: The ARN of the new custom model deployment

    Raises:
        Exception: If there is an error creating the deployment
    """

    try:
        response = bedrock_client.create_custom_model_deployment(
            modelDeploymentName="`Unique deployment name`",
            modelArn="`Custom Model ARN`",
            description="`Deployment description`",
            tags=[
                {'key': 'Environment', 'value': 'Production'},
                {'key': 'Team', 'value': 'ML-Engineering'},
                {'key': 'Project', 'value': 'CustomerSupport'}
            ],
            clientRequestToken=f"deployment-{uuid.uuid4()}"
        )

        deployment_arn = response['customModelDeploymentArn']
        print(f"Deployment created: {deployment_arn}")
        return deployment_arn

    except Exception as e:
        print(f"Error creating deployment: {str(e)}")
        raise
```
