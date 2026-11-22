

# Edge Inference for Agriculture

Publication date: **August 31, 2020 ([Diagram history](diagram-history.md))**

With this architecture, you can enable edge inference in rural and remote agricultural environments by using [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/) and [Amazon SageMaker AI Neo](https://docs.aws.amazon.com/sagemaker/latest/dg/neo.html). The solution handles intermittent connectivity and low-latency inference at the edge.

## Edge inference for agriculture diagram
<a name="edge-ag-diagram"></a>

![Reference architecture diagram showing how to enable edge inference in agricultural environments by using AWS IoT Greengrass, SageMaker AI Neo, and Lambda.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/agriculture/images/edge-inference-agriculture.png)


The following steps describe the architecture:

1. Collect sensor data and send it to the device running AWS IoT Greengrass.

1. Use AWS IoT Greengrass and [AWS Snowball Edge Edge](https://docs.aws.amazon.com/snowball/latest/developer-guide/) devices to handle intermittent connectivity and low-latency inference.

1. Collect sensor data with a [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) producer function.

1. Use container images from a public registry, a private registry, [Amazon Elastic Container Registry](https://docs.aws.amazon.com/AmazonECR/latest/userguide/), or Docker Hub.

1. Use SageMaker AI Neo to compile machine learning models to run on the device with a compact runtime.

1. Run action model inference on the device by using a Lambda function to coordinate and trigger inference responses.

1. Deploy AWS IoT Greengrass connectors to use [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/).

1. Deploy models optimized with SageMaker AI Neo directly to the edge with over-the-air (OTA) updates through AWS IoT Greengrass. OTA updates deliver software wirelessly without physical access to the device.

## Further reading
<a name="edge-ag-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 