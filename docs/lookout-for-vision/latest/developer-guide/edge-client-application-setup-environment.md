End of support notice: On October 31, 2025, AWS
will discontinue support for Amazon Lookout for Vision. After October 31, 2025, you will
no longer be able to access the Lookout for Vision console or Lookout for Vision resources.
For more information, visit this [blog post](https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision "https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision").

# Setting up your environment

To write client code, your development environment connects remotely to an AWS IoT Greengrass Version 2
core device to which you have deployed a Amazon Lookout for Vision model component and dependencies. Alternatively,
you can write code on a core device. For more information, see
[AWS IoT Greengrass development tools](../../../greengrass/v2/developerguide/greengrass-development-tools.md "../../../greengrass/v2/developerguide/greengrass-development-tools.md")
and [Develop AWS IoT Greengrass components](../../../greengrass/v2/developerguide/develop-greengrass-components.md "../../../greengrass/v2/developerguide/develop-greengrass-components.md").

Your client code should use gRPC client to access the Amazon Lookout for Vision Edge Agent. This
section shows how to set up your development environment with gRPC and install third-party
dependencies needed for the `DetectAnomalies` example code.

After you finish writing your client code, you create a custom component and deploy the
custom component to your edge devices. For more information, see
[Creating the client application component](edge-inference-create-custom-component.md "edge-inference-create-custom-component.md").

###### Topics

- [Setting up gRPC](#edge-client-application-create-stub "#edge-client-application-create-stub")
- [Adding third-party
  dependencies](#edge-client-application-3rd-party "#edge-client-application-3rd-party")

## Setting up gRPC

In your development environment, you need a gRPC client that you use in your
code to call the Lookout for Vision Edge Agent API. To do this, you create a gRPC stub by using
a `.proto`service definition file for the Lookout for Vision Edge Agent.

###### Note

You can also get the service definition file from the Lookout for Vision Edge Agent
application bundle. The application bundle is installed when the Lookout for Vision Edge Agent
component is installed as a dependency of the model component. The
application bundle is located at
`/greengrass/v2/packages/artifacts-unarchived/aws.iot.lookoutvision.EdgeAgent/`edge_agent_version`/lookoutvision_edge_agent`.
Replace `edge_agent_version` with version of the Lookout for Vision Edge Agent that
you are using. To get the application bundle, you need to deploy the
Lookout for Vision Edge Agent to a core device.

###### To set up gRPC

1. Download the zip file, [proto.zip](samples/proto.md "samples/proto.md"). The zip file contains the .proto service
   definition file (`edge-agent.proto`).
2. Unzip the content.
3. Open a command prompt and navigate to the folder that contains `edge-agent.proto`.
4. Use the following commands to generate the Python client interfaces.

```
%%bash
python3 -m pip install grpcio
python3 -m pip install grpcio-tools
python3 -m grpc_tools.protoc --proto_path=. --python_out=. --grpc_python_out=. edge-agent.proto
```

If the commands are successful, the stubs `edge_agent_pb2_grpc.py` and `edge_agent_pb2.py` are created in the working directory. 5. Write the client code that uses your model. For more information, see
[Using a model in your client application component](inference-using-model.md "inference-using-model.md").

## Adding third-party

dependencies

The `DetectAnomalies` example code uses the [Pillow](https://python-pillow.org/ "https://python-pillow.org/") library to work with images. For more information,
see [Detecting Anomalies by using image bytes](inference-using-model.md#client-application-overview-detect-anomalies-image-bytes "inference-using-model.md#client-application-overview-detect-anomalies-image-bytes").

Use the following command to install the Pillow library.

```
python3 -m pip install Pillow
```
