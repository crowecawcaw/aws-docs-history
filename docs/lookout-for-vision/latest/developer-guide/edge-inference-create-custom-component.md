End of support notice: On October 31, 2025, AWS
will discontinue support for Amazon Lookout for Vision. After October 31, 2025, you will
no longer be able to access the Lookout for Vision console or Lookout for Vision resources.
For more information, visit this [blog post](https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision "https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision").

# Creating the client application component

You can create the client application component once you have generated your gRPC
stubs and you have your client application code ready. The component you create is a
custom component that you deploy to an AWS IoT Greengrass Version 2 core device with AWS IoT Greengrass V2. A recipe that
you create describes your custom component. The recipe includes
any dependencies that also need to be deployed. In this case, you specify the model
component that you create in [Packaging your Amazon Lookout for Vision model](package-job.md "package-job.md"). For more information about component recipes, see [AWS IoT Greengrass Version 2
component recipe reference](../../../greengrass/v2/developerguide/component-recipe-reference.md "../../../greengrass/v2/developerguide/component-recipe-reference.md").

The procedures on this topic show you how to create the client application component
from a recipe file and publish it as an AWS IoT Greengrass V2 custom component. You can use the AWS IoT Greengrass V2 console or
the AWS SDK to publish the component.

For detailed information about creating a custom component, see the following in the _AWS IoT Greengrass V2_ documentation.

- [Develop and test a component on your device](../../../greengrass/v2/developerguide/getting-started.md#create-first-component "../../../greengrass/v2/developerguide/getting-started.md#create-first-component")
- [Create AWS IoT Greengrass components](../../../greengrass/v2/developerguide/create-components.md "../../../greengrass/v2/developerguide/create-components.md")
- [Publish components to deploy to your core devices](../../../greengrass/v2/developerguide/publish-components.md "../../../greengrass/v2/developerguide/publish-components.md")

###### Topics

- [IAM permissions for publishing a client application component](#edge-inference-create-custom-component-recipe-permissions "#edge-inference-create-custom-component-recipe-permissions")
- [Creating the recipe](#edge-inference-create-custom-component-recipe "#edge-inference-create-custom-component-recipe")
- [Publishing the client application component (Console)](#edge-inference-create-custom-component-console "#edge-inference-create-custom-component-console")
- [Publishing the client application component (SDK)](#edge-inference-create-custom-component-sdk "#edge-inference-create-custom-component-sdk")

## IAM permissions for publishing a client application component

To create and publish your client application component, you need the following IAM permissions:

- `greengrass:CreateComponentVersion`
- `greengrass:DescribeComponent`
- `s3:PutObject`

## Creating the recipe

In this procedure, you create the recipe for a simple client application component. The code in `lookoutvision_edge_agent_example.py`
lists the models that are deployed to the device and is automatically run after you deploy the component to the core device. To view the output,
check the component log after you deploy the component. For more information, see
[Deploying your components to a device](device-deploy-components.md "device-deploy-components.md"). When you are ready,
use this procedure to create the recipe for code that implements your business logic.

You create the recipe as a JSON or YAML format file. You also upload the client application code to an Amazon S3 bucket.

###### To create the client application component recipe

1. If you haven't already, create the gRPC stub files. For more information, see
   [Setting up gRPC](edge-client-application-setup-environment.md#edge-client-application-create-stub "edge-client-application-setup-environment.md#edge-client-application-create-stub").
2. Save the following code to a file named `lookoutvision_edge_agent_example.py`

```
import grpc
from edge_agent_pb2_grpc import EdgeAgentStub
import edge_agent_pb2 as pb2

# Creating stub.
with grpc.insecure_channel("unix:///tmp/aws.iot.lookoutvision.EdgeAgent.sock") as channel:
    stub = EdgeAgentStub(channel)
    # Add additional code that works with Edge Agent in this block to prevent resources leakage

    models_list_response = stub.ListModels(
        pb2.ListModelsRequest()
    )
    for model in models_list_response.models:
        print(f"Model Details {model}")
```

3. [Create
   an Amazon S3 bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md") (or use an existing bucket) to store the
   source files for your client application component. The bucket must in
   your AWS account and in the same AWS Region in which you use
   AWS IoT Greengrass Version 2 and Amazon Lookout for Vision.
4. Upload `lookoutvision_edge_agent_example.py`,
   `edge_agent_pb2_grpc.py and edge_agent_pb2.py` to the Amazon S3
   bucket that you created in the previous step. Note the Amazon S3 path of each file.
   You created `edge_agent_pb2_grpc.py` and
   `edge_agent_pb2.py` in [Setting up gRPC](edge-client-application-setup-environment.md#edge-client-application-create-stub "edge-client-application-setup-environment.md#edge-client-application-create-stub").
5. In an editor create the following JSON or YAML recipe file.
   - `model_component` to the name of your model
     component. For more information, see [Component settings](package-settings.md#package-settings-component-settings "package-settings.md#package-settings-component-settings").
   - Change the URI entries to the S3 paths of
     `lookoutvision_edge_agent_example.py`,
     `edge_agent_pb2_grpc.py`, and
     `edge_agent_pb2.py`.

JSON

```
{
  "RecipeFormatVersion": "2020-01-25",
  "ComponentName": "com.lookoutvision.EdgeAgentPythonExample",
  "ComponentVersion": "1.0.0",
  "ComponentType": "aws.greengrass.generic",
  "ComponentDescription": "Lookout for Vision Edge Agent Sample Application",
  "ComponentPublisher": "Sample App Publisher",
  "ComponentDependencies": {
    "`model_component`": {
      "VersionRequirement": ">=1.0.0",
      "DependencyType": "HARD"
    }
  },
  "Manifests": [
    {
      "Platform": {
        "os": "linux"
      },
      "Lifecycle": {
        "install": "pip3 install grpcio grpcio-tools protobuf Pillow",
        "run": {
          "script": "python3 {artifacts:path}/lookoutvision_edge_agent_example.py"
        }
      },
      "Artifacts": [
        {
          "Uri": "`S3 path to lookoutvision_edge_agent_example.py`"
        },
        {
          "Uri": "`S3 path to edge_agent_pb2_grpc.py`"
        },
        {
          "Uri": "`S3 path to edge_agent_pb2.py`"
        }
      ]
    }
  ],
  "Lifecycle": {}
}
```

YAML

```
---
RecipeFormatVersion: 2020-01-25
ComponentName: com.lookoutvison.EdgeAgentPythonExample
ComponentVersion: 1.0.0
ComponentDescription: Lookout for Vision Edge Agent Sample Application
ComponentPublisher: Sample App Publisher
ComponentDependencies:
  `model_component`:
    VersionRequirement: '>=1.0.0'
    DependencyType: HARD
Manifests:
  - Platform:
      os: linux
    Lifecycle:
      install: |-
        pip3 install grpcio
        pip3 install grpcio-tools
        pip3 install protobuf
        pip3 install Pillow
      run:
        script: |-
          python3 {artifacts:path}/lookout_vision_agent_example.py
    Artifacts:
      - URI: `S3 path to lookoutvision_edge_agent_example.py`
      - URI: `S3 path to edge_agent_pb2_grpc.py`
      - URI: `S3 path to edge_agent_pb2.py`
```

6. Save the JSON or YAML file to your computer.
7. Create the client application component by doing one of the following:
   - If you want to use the AWS IoT Greengrass console, do
     [Publishing the client application component (Console)](#edge-inference-create-custom-component-console "#edge-inference-create-custom-component-console").
   - If you want use the AWS SDK,
     do [Publishing the client application component (SDK)](#edge-inference-create-custom-component-sdk "#edge-inference-create-custom-component-sdk").

## Publishing the client application component (Console)

You can use the AWS IoT Greengrass V2 console to publish the client application component.

###### To publish the client application component

1. If you haven't already, create the recipe for your client appication component by doing
   [Creating the recipe](#edge-inference-create-custom-component-recipe "#edge-inference-create-custom-component-recipe").
2. Open the AWS IoT Greengrass console at [https://console.aws.amazon.com/iot/](https://console.aws.amazon.com/greengrass/ "https://console.aws.amazon.com/greengrass/")
3. In the left navigation pane, under **Greengrass** choose **Components**.
4. Under **My components** choose **Create component**.
5. On the **Create component page** choose **Enter recipe as JSON** if you want to
   use a JSON format recipe. Choose **Enter recipe as YAML** if you want to use a YAML format recipe.
6. Under **Recipe** replace the existing recipe with the JSON or YAML recipe that you created
   in [Creating the recipe](#edge-inference-create-custom-component-recipe "#edge-inference-create-custom-component-recipe").
7. Choose **Create component**.
8. Next, [deploy](device-deploy-components.md "device-deploy-components.md") your client application component.

## Publishing the client application component (SDK)

You can publish the client application component by using the
[CreateComponentVersion](../../../greengrass/v2/APIReference/API_CreateComponentVersion.md "../../../greengrass/v2/APIReference/API_CreateComponentVersion.md") API.

###### To publish the client application component (SDK)

1. If you haven't already, create the recipe for your client appication component by doing [Creating the recipe](#edge-inference-create-custom-component-recipe "#edge-inference-create-custom-component-recipe").
2. At the command prompt, enter the following command to create the client application component.
   Replace `recipe-file` with the name of the recipe file you created in
   [Creating the recipe](#edge-inference-create-custom-component-recipe "#edge-inference-create-custom-component-recipe").

```
aws greengrassv2 create-component-version --inline-recipe fileb://`recipe-file`
```

Note the ARN of the component in the response. You need it in the next step. 3. Use the following command to get the status of the client application component. Replace
`component-arn` with the ARN that you noted in the previous step. The client application component
is ready if the value of `componentState` is `DEPLOYABLE`.

```
aws greengrassv2 describe-component --arn `component-arn`
```

4. Next, [deploy](device-deploy-components.md "device-deploy-components.md") your client application component.
