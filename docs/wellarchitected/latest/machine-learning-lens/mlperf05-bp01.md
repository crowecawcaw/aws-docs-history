# MLPERF05-BP01 Evaluate cloud versus edge options for machine

learning deployment

Evaluate machine learning deployment options to determine if your
application requires near-instantaneous inference results or needs
to operate without network connectivity. When the lowest possible
latency is essential, deploying inference directly on edge devices
avoids costly roundtrips to cloud API endpoints. Edge deployments
are particularly valuable for use cases like predictive maintenance
in factories, where immediate local responses are critical.

**Desired outcome:** You can make
informed decisions about where to deploy your machine learning
models based on your business requirements. You understand when to
use cloud resources for training and when to deploy optimized models
to edge devices for low-latency inference. Your edge deployments can
operate autonomously when needed while maintaining security,
performance, and the ability to update models as new data becomes
available.

**Common anti-patterns:**

- Defaulting to cloud-based inference without evaluating latency
  requirements.
- Deploying models to edge devices without proper optimization,
  resulting in poor performance.
- Neglecting to establish a strategy for model updates and
  monitoring on edge devices.
- Overlooking security considerations for models deployed at the
  edge.
- Failing to evaluate hardware constraints of edge devices before
  deployment.

**Benefits of establishing this best
practice:**

- Dramatically reduced inference latency for time-sensitive
  applications.
- Ability to operate ML models in environments with limited or no
  connectivity.
- Lower operational costs by reducing network traffic and cloud
  compute usage.
- Enhanced privacy by keeping sensitive data local to edge
  devices.
- Improved resilience against network outages.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Machine learning deployments require careful consideration of
where inference should take place based on your use case
requirements. While training complex models is computationally
intensive and best suited for the cloud, inference operations
require less computing power and can often be performed directly
on edge devices.

Avoid defaulting to cloud-based inference without evaluating
latency requirements. Many organizations deploy models to edge
devices without proper optimization, resulting in poor
performance, neglect to establish a strategy for model updates and
monitoring on edge devices, overlook security considerations for
models deployed at the edge, and fail to evaluate hardware
constraints of edge devices before deployment.

When evaluating cloud versus edge deployment, consider factors
like latency requirements, connectivity constraints, data privacy
needs, and the computational capabilities of your edge devices.
For applications requiring real-time responses, such as autonomous
vehicles, industrial equipment monitoring, or smart security
systems, edge deployment reduces network latency and provides
continuous operation even during connectivity disruptions.

AWS provides comprehensive tools to optimize models for edge
deployment while maintaining the ability to train and manage those
models in the cloud. This hybrid approach gives you the best of
both worlds: powerful cloud resources for development and
optimization, with efficient edge deployment for operational
performance.

### Implementation steps

1. **Assess your deployment
   requirements**. Begin by clearly defining your
   application's latency, connectivity, and privacy
   requirements. Determine if your use case needs
   millisecond-level response times, must function in
   environments with unreliable connectivity, or needs to
   process sensitive data locally. These factors will guide
   your decision between cloud and edge deployment options.
2. **Optimize models for edge
   deployment**. Training and optimizing machine
   learning models require massive computing resources, making
   cloud environments ideal for this phase.
   [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ "https://aws.amazon.com/sagemaker/") provides powerful tools for building and
   training models that can later be optimized for edge
   deployment. Consider the computational constraints of your
   target edge devices and select model architectures that
   balance accuracy with efficiency.
3. **Deploy with Amazon SageMaker AI Neo for
   cross-solution compatibility**.
   [Amazon SageMaker AI Neo](https://aws.amazon.com/sagemaker/neo/ "https://aws.amazon.com/sagemaker/neo/") enables ML models to be trained once
   and run anywhere in the cloud or at the edge. The Neo
   compiler reads models exported from various frameworks,
   converts them to framework-agnostic representations, and
   generates optimized binary code for target hardware. This
   process makes your models run faster without accuracy loss.
4. **Implement edge ML with AWS IoT Greengrass**.
   [AWS IoT Greengrass](https://aws.amazon.com/greengrass/ml/ "https://aws.amazon.com/greengrass/ml/") provides a robust solution for running
   ML inferences on edge devices using cloud-trained models.
   These models can be built using Amazon SageMaker AI,
   [AWS Deep Learning AMIss](https://aws.amazon.com/machine-learning/amis/ "https://aws.amazon.com/machine-learning/amis/"), or
   [AWS Deep Learning Containers](https://aws.amazon.com/machine-learning/containers/ "https://aws.amazon.com/machine-learning/containers/"). Models are stored in
   [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/") before deployment to edge devices.

## Resources

**Related documents:**

- [AWS IoT Greengrass](https://aws.amazon.com/greengrass/ml/ "https://aws.amazon.com/greengrass/ml/")
- [Set
  up Neo on Edge Devices](../../../sagemaker/latest/dg/neo-getting-started-edge.md "../../../sagemaker/latest/dg/neo-getting-started-edge.md")
- [AWS Internet of
  Things](https://aws.amazon.com/iot/ "https://aws.amazon.com/iot/")
- [Optimize
  image classification on AWS IoT Greengrass using ONNX
  Runtime](https://aws.amazon.com/blogs/iot/optimize-image-classification-on-aws-iot-greengrass-using-onnx-runtime/ "https://aws.amazon.com/blogs/iot/optimize-image-classification-on-aws-iot-greengrass-using-onnx-runtime/")

**Related videos:**

- [Machine
  Learning at the Edge](https://www.youtube.com/watch?v=EAz-qAL5z2U "https://www.youtube.com/watch?v=EAz-qAL5z2U")
- [Getting
  Started Using Machine Learning at the Edge](https://pages.awscloud.com/Getting-Started-Using-Machine-Learning-at-the-Edge_2020_0202-IOT_OD.html "https://pages.awscloud.com/Getting-Started-Using-Machine-Learning-at-the-Edge_2020_0202-IOT_OD.html")
- [AWS IoT Greengrass and Machine Learning at the Edge](https://www.youtube.com/watch?v=keaq6sy46ek "https://www.youtube.com/watch?v=keaq6sy46ek")
