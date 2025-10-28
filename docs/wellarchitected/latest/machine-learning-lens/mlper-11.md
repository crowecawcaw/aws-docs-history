# MLPER-11: Evaluate cloud versus edge options for machine learning deployment

Evaluate if machine learning applications require
near-instantaneous inference results or require inference
without network connectivity. Offering the lowest latency
possible might require the removal of costly roundtrips to the
nearest API endpoints. A reduction in latency can be achieved by
running the inference directly on the device itself (on the
_edge_). A common use-case for such a
requirement is predictive maintenance in factories.

## Implementation plan

- **Optimize model deployment on the
  edge** - Training and optimizing machine learning
  models require massive computing resources, so it is a
  natural fit for the cloud. Inference takes a lot less
  computing power and is often done in real time when new
  data is available. When getting inference results with
  very low latency, confirm that your IoT applications can
  respond quickly to local events. Evaluate and choose the
  option to meet your business requirements.
  - Amazon SageMaker AI Edge enables machine learning on edge
    devices by optimizing, securing, and deploying models
    to the edge, and then monitoring these models on your
    fleet of devices, such as smart cameras, robots, and
    other smart-electronics, to reduce ongoing operational
    costs. Customers who train models in TensorFlow,
    MXNet, PyTorch, XGBoost, and TensorFlow Lite can use
    SageMaker AI Edge to improve their performance, deploy
    them on edge devices, and monitor their health
    throughout their lifecycle. SageMaker AI Edge Compiler
    optimizes the trained model to be run on an edge
    device. SageMaker AI Edge Agent allows you to run
    multiple models on the same device. The Agent collects
    prediction data based on the logic that you control,
    such as intervals, and uploads it to the cloud so that
    you can periodically retrain your models over time.
    SageMaker AI Edge cryptographically signs your models so
    you can verify that they were not tampered with as
    they move from the cloud to edge devices.
  - [Amazon SageMaker AI Neo](https://aws.amazon.com/sagemaker/neo/ "https://aws.amazon.com/sagemaker/neo/") enables ML models to be trained
    once and then run anywhere in the cloud and at the
    edge. SageMaker AI Neo consists of a compiler and a
    runtime. The compilation API reads models exported
    from various frameworks, converts them into
    framework-agnostic representations, and generates
    optimized binary code (to run faster with no loss in
    accuracy). The compiler uses a machine learning model
    to apply the performance optimizations that extract
    the best available performance for your model on the
    cloud instance or edge device. The runtime for each
    target platform then loads and runs the compiled
    model.
  - SageMaker AI Neo optimizes machine learning models for
    inference on cloud instances and edge devices.
    SageMaker AI Neo optimizes the trained model and compiles
    it into an executable. You then deploy the model as a
    SageMaker AI endpoint or on supported edge devices and
    start making predictions.
  - [AWS IoT Greengrass](https://aws.amazon.com/greengrass/ml/ "https://aws.amazon.com/greengrass/ml/") enables ML inferences on edge
    devices using models trained in the cloud. These
    models can be built using
    [Amazon SageMaker AI](../../../sagemaker/latest/dg/whatis.md "../../../sagemaker/latest/dg/whatis.md"),
    [AWS Deep Learning AMIs](https://aws.amazon.com/machine-learning/amis/ "https://aws.amazon.com/machine-learning/amis/"), or
    [AWS Deep Learning Containers](https://aws.amazon.com/machine-learning/containers/ "https://aws.amazon.com/machine-learning/containers/"). These models can be
    stored in
    [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/") before being deployed on edge devices.

## Documents

- [AWS IoT Greengrass ML Inference](https://aws.amazon.com/greengrass/ml/ "https://aws.amazon.com/greengrass/ml/")
- [Amazon SageMaker AI Edge Manager](https://aws.amazon.com/sagemaker/edge-manager/ "https://aws.amazon.com/sagemaker/edge-manager/")
- [Getting
  Started with Neo on Edge Devices](../../../sagemaker/latest/dg/neo-getting-started-edge.md "../../../sagemaker/latest/dg/neo-getting-started-edge.md")

## Blogs

- [Machine
  Learning at the Edge: Using and Retraining Image
  Classification Models with AWS IoT Greengrass](https://aws.amazon.com/blogs/iot/machine-learning-at-the-edge-using-and-retraining-image-classification-models-with-aws-iot-greengrass-part-1/ "https://aws.amazon.com/blogs/iot/machine-learning-at-the-edge-using-and-retraining-image-classification-models-with-aws-iot-greengrass-part-1/")
- [Monitor
  and Manage Anomaly Detection Models on a fleet of Wind
  Turbines with Amazon SageMaker AI Edge Manager](https://aws.amazon.com/blogs/machine-learning/monitor-and-manage-anomaly-detection-models-on-a-fleet-of-wind-turbines-with-amazon-sagemaker-edge-manager/ "https://aws.amazon.com/blogs/machine-learning/monitor-and-manage-anomaly-detection-models-on-a-fleet-of-wind-turbines-with-amazon-sagemaker-edge-manager/")
- [SageMaker AI
  Edge Manager Simplifies Operating Machine Learning Models
  on Edge Devices](https://aws.amazon.com/blogs/aws/amazon-sagemaker-edge-manager-simplifies-operating-machine-learning-models-on-edge-devices/ "https://aws.amazon.com/blogs/aws/amazon-sagemaker-edge-manager-simplifies-operating-machine-learning-models-on-edge-devices/")
- [Amazon SageMaker AI Neo Helps Detect Objects and Classify Images on
  Edge Devices](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-neo-helps-detect-objects-and-classify-images-on-edge-devices/ "https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-neo-helps-detect-objects-and-classify-images-on-edge-devices/")
- [Machine
  Learning at the Edge with AWS Outposts and Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/machine-learning-at-the-edge-with-aws-outposts-and-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/machine-learning-at-the-edge-with-aws-outposts-and-amazon-sagemaker/")

## Videos

- [Machine
  Learning at the Edge](https://www.youtube.com/watch?v=EAz-qAL5z2U "https://www.youtube.com/watch?v=EAz-qAL5z2U")
- [Getting
  Started Using Machine Learning at the Edge](https://pages.awscloud.com/Getting-Started-Using-Machine-Learning-at-the-Edge_2020_0202-IOT_OD.html?&trk=el_a131L0000083Z9QQAU&trkCampaign=February_2020_0202-IOT&sc_channel=el&sc_campaign=pac_Q1-2020_exlinks_blog_OTT_02DGAB&sc_outcome=Product_Adoption_Campaigns&sc_geo=NAMER&sc_country=mult "https://pages.awscloud.com/Getting-Started-Using-Machine-Learning-at-the-Edge_2020_0202-IOT_OD.html?&trk=el_a131L0000083Z9QQAU&trkCampaign=February_2020_0202-IOT&sc_channel=el&sc_campaign=pac_Q1-2020_exlinks_blog_OTT_02DGAB&sc_outcome=Product_Adoption_Campaigns&sc_geo=NAMER&sc_country=mult")
- [Train
  ML Models Once, Run Anywhere in the Cloud & at the
  Edge with Amazon SageMaker AI Neo](https://www.youtube.com/watch?v=waKMyWUFvQY "https://www.youtube.com/watch?v=waKMyWUFvQY")
