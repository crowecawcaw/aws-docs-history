# Access curated model hubs in Amazon SageMaker JumpStart

You can access a private model hub either through Studio or through the SageMaker Python SDK.

## Access your private model hub in Studio

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the updated Studio
experience. For information about using the Studio Classic application, see [Amazon SageMaker Studio Classic](studio.md "studio.md").

In Amazon SageMaker Studio, open the JumpStart landing page either through the
**Home** page or the **Home** menu on the
left-side panel. This opens the **SageMaker JumpStart** landing page
where you can explore model hubs and search for models.

- From the **Home** page, choose **JumpStart**
  in the **Prebuilt and automated solutions** pane.
- From the **Home** menu in the left panel, navigate to the
  **JumpStart** node.

For more information on getting started with Amazon SageMaker Studio, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md").

From the **SageMaker JumpStart** landing page in Studio, you
can explore any private model hubs that include allow-listed models for your
organization. If you only have access to one model hub, then the **SageMaker
JumpStart** landing page takes you directly into that hub. If you
have access to multiple hubs, you are taken to the **Hubs** page.

For more information on fine-tuning, deploying, and evaluating models that you
have access to in Studio, see [Use foundation
models in Studio](jumpstart-foundation-models-use-studio-updated.md "jumpstart-foundation-models-use-studio-updated.md").

## Access your private model hub using the SageMaker Python SDK

You can access your private model hub using the SageMaker Python SDK. Your access to read, use, or edit your curated hub is provided by your administrator.

###### Note

If a hub is shared across accounts, then the `HUB_NAME` must be the hub ARN.
If a hub is not shared across accounts, then the `HUB_NAME` can be the hub name.

1. Install the SageMaker Python SDK and import the necessary Python packages.

```
# Install the SageMaker Python SDK
    !pip3 install sagemaker --force-reinstall --quiet

    # Import the necessary Python packages
    import boto3
    from sagemaker import Session
    from sagemaker.jumpstart.hub.hub import Hub
    from sagemaker.jumpstart.model import JumpStartModel
    from sagemaker.jumpstart.estimator import JumpStartEstimator
```

2. Initalize a SageMaker AI session and connect to your private hub using the hub name and Region.

```
# If a hub is shared across accounts, then the HUB_NAME must be the hub ARN
    HUB_NAME=`"Example-Hub-ARN"`
    REGION=`"us-west-2"`

    # Initialize a SageMaker session
    sm_client = boto3.client(`'sagemaker'`)
    sm_runtime_client = boto3.client(`'sagemaker-runtime'`)
    session = Session(sagemaker_client=sm_client,
                        sagemaker_runtime_client=sm_runtime_client)

    # Initialize the private hub
    hub = Hub(hub_name=`HUB_NAME`, sagemaker_session=session)
```

3. After connecting to a private hub, you can list all available models in
   that hub using the following commands:

```
response = hub.list_models()
    models = response["hub_content_summaries"]
    while response["next_token"]:
        response = hub.list_models(next_token=response["next_token"])
        models.extend(response["hub_content_summaries"])

    print(models)
```

4. You can get more information about a specific model using the model name
   with the following command:

```
response = hub.describe_model(model_name=`"example-model"`)
    print(response)
```

For more information on fine-tuning and deploying models that you have access to
using the SageMaker Python SDK, see [Use foundation models
with the SageMaker Python SDK](jumpstart-foundation-models-use-python-sdk.md "jumpstart-foundation-models-use-python-sdk.md").
