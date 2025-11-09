# MFGSCE5: Computer vision for automated quality inspection

In manufacturing quality control, the transition from manual inspection to automated
computer vision systems represents a significant advancement. However, the journey from raw
image capture to reliable defect detection is complex, particularly from a data management
and ML operations perspective.

This section explores the data challenges and AI/ML pipeline requirements for
implementing effective computer vision-based quality inspection solutions.

## Data acquisition and management challenges

### Image capture and local storage

Manufacturing environments present unique challenges for image data acquisition:

- **Environmental variability**: Shop floor lighting
  conditions fluctuate throughout the day, affecting image consistency.
- **Camera configuration**: Selecting appropriate
  sensors (color or monochrome), lenses, and positioning to capture defects
  consistently requires careful optimization.
- **Real-time storage requirements**: High-resolution
  images from production lines create significant local storage demands, requiring
  efficient buffering and compression strategies.
- **Metadata integration**: Correlating images with
  production metadata (like timestamps, batch numbers, and machine parameters) is
  essential for contextual analysis.

### Secure cloud transfer

Moving image data from operational technology (OT) environments to cloud systems
involves:

- **Bandwidth optimization**: Manufacturing facilities
  often face network constraints, requiring intelligent transfer strategies like edge
  preprocessing, compression, or selective sampling.
- **Security protocols**: Implementing encryption and
  secure transfer mechanisms while maintaining OT and IT separation.
- **Data integrity**: Keeping images and associated
  metadata consistent during transfer processes.

## Data preparation pipeline

### Image segmentation

Breaking down complex manufacturing images requires:

- **Region-of-interest extraction**: Isolating specific
  product areas for focused analysis.
- **Background elimination**: Removing irrelevant
  visual elements that could confuse ML models.
- **Multi-object handling**: Managing images containing
  multiple instances of products or components.

### Defect labeling

Creating quality training datasets involves:

- **Annotation complexity**: Defining consistent
  protocols for marking subtle manufacturing defects.
- **Expert knowledge transfer**: Converting tacit
  quality inspector knowledge into explicit annotation guidelines.
- **Labeling efficiency**: Implementing semi-supervised
  approaches to reduce manual labeling burden.
- **Data augmentation**: Using generative AI to create
  synthetic examples of rare defect types.

### Training data management

Organizing image assets for optimal ML development:

- **Version control**: Maintaining trackable iterations
  of image datasets as production evolves.
- **Class balancing**: Managing the inherent imbalance
  between good products and defective ones.
- **Representativeness**: Verifying that the dataset
  covers seasonal variations and all possible defect types.
- **Cross-functional access**: Enabling secure data
  sharing between OT personnel and data science teams.

## MLOps for manufacturing vision systems

### Model development

Transforming manufacturing image data into reliable quality models:

- **Transfer learning optimization**: Adapting
  pre-trained computer vision architectures to specific manufacturing contexts.
- **Custom architecture development**: Creating
  specialized models for unique inspection requirements.
- **Explainability integration**: Building
  interpretable models that help operators understand defect classifications.
- **Lightweight model design**: Optimizing performance
  for edge deployment constraints.

### Model packaging and deployment

Preparing models for production environments:

- **Edge compilation**: Converting trained models to
  formats optimized for edge hardware.
- **Component packaging**: Bundling models with
  necessary preprocessing and postprocessing code.
- **Deployment automation**: Creating CI/CD pipelines
  that can safely update models in production.
- **Version management**: Maintaining trackability of
  model versions across the manufacturing fleet.

### Edge inference and monitoring

Running models in production environments:

- **Latency optimization**: Verifying that real-time
  performance meets production line speeds.
- **Resource utilization**: Balancing model complexity
  against available edge computing resources.
- **Quality metrics tracking**: Monitoring inference
  performance against established standards.
- **Integration with control systems**: Connecting
  inference outputs to downstream manufacturing systems.

### Model drift detection

Maintaining model reliability over time:

- **Data distribution monitoring**: Detecting when
  production images diverge from training distributions.
- **Performance degradation alerts**: Identifying when
  model accuracy falls below acceptable thresholds.
- **Root cause analysis**: Determining whether drift
  stems from process changes, lighting variations, or other factors.
- **Targeted data collection**: Efficiently gathering
  new images of problematic cases for retraining.

### Continuous learning cycles

Keeping models current with manufacturing realities:

- **Automated retraining events**: Initiating new
  training cycles based on drift metrics.
- **Knowledge retention**: Preserving performance on
  historical defect types while adapting to new ones.
- **A/B testing**: Safely evaluating model improvements
  before full deployment.
- **Model governance**: Maintaining audit trails of
  model changes for quality compliance.

## AWS architecture for vision-based quality inspection

A comprehensive data architecture for computer vision quality inspection on AWS
includes:

1. **Image acquisition and edge processing**
   - Use AWS IoT Greengrass to capture and preprocess images at the edge.
   - Implement edge-based inference for immediate quality decisions.
   - Buffer images locally with selective cloud uploading to manage bandwidth.

2. **Secure data transfer and storage**
   - Encrypt and transfer images securely to Amazon S3.
   - Organize raw images in data lake architecture with appropriate partitioning.
   - Implement lifecycle policies for cost-effective long-term storage.

3. **Image processing and labeling**
   - Use Amazon SageMaker Ground Truth for human labeling workflows.
   - Use Amazon Bedrock foundation models for automatic segmentation and labeling
     assistance.
   - Generate synthetic defect images for rare conditions using generative AI
     capabilities.

4. **Model development**
   - Use Amazon SageMaker AI AI for training and hyperparameter optimization.
   - Implement transfer learning from AWS computer vision model zoo.
   - Establish experiment tracking for model versioning and comparison.

5. **MLOps pipeline**
   - Create automated CI/CD pipelines for model deployment using AWS CodePipeline.
   - Compile models for edge deployment with SageMaker AI Neo.
   - Package models as AWS IoT Greengrass components.

6. **Production monitoring and feedback**
   - Track inference metrics and model performance using Amazon CloudWatch.
   - Detect data drift with SageMaker AI Model Monitor.
   - Implement automated retraining workflows initiated by performance
     degradation.

7. **Integration with manufacturing systems**
   - Connect inference results to AWS IoT Core MQTT topics.
   - Initiate control systems and quality workflows based on detection results.
   - Integrate with AWS IoT SiteWise for holistic process monitoring.
   - Calculate quality KPIs and OEE metrics based on vision system outputs.

8. **Analytics and continuous improvement**
   - Store historical inspection data in Amazon S3 for long-term analysis.
   - Use Quick Suite for quality trend visualization.
   - Employ Amazon SageMaker AI for root cause analysis of quality issues.
   - Close the loop between quality detection and upstream process control.

By focusing on the data lifecycle and MLOps for computer vision applications,
manufacturers can build sustainable, self-improving quality inspection systems that
overcome the traditional challenges of computer vision deployment in industrial
environments. This data-centric approach helps keep your models accurate and relevant even
as manufacturing processes evolve over time.

## Automated quality inspection architecture

![ADD ALTERNATE TEXT HERE for people using assistive technology.](images/image9.png)
_ADD FIGURE CAPTION HERE_

1. Automatically upload training images from the manufacturing line camera to [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/").
2. Label the training images and identify defects. You can use [Amazon SageMaker Ground Truth](https://aws.amazon.com/sagemaker/groundtruth/ "https://aws.amazon.com/sagemaker/groundtruth/") for creating and managing labeling jobs. Also, you can use
   state-of-the-art 

[large language
models](https://aws.amazon.com/what-is/large-language-model/ "https://aws.amazon.com/what-is/large-language-model/") in 

[Amazon
Bedrock](https://aws.amazon.com/bedrock/ "https://aws.amazon.com/bedrock/") to create synthetic image datasets for scenarios that are too
expensive, dangerous, or impossible to capture real-world image datasets and for
automated segmentation and labeling images. 3. Begin model training using [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ "https://aws.amazon.com/sagemaker/"), using the training images stored in Amazon S3. You can use
AWS-provided image anomaly detection 

[pre-trained
models in Amazon SageMaker AI AI](../../../sagemaker/latest/dg/algos.md "../../../sagemaker/latest/dg/algos.md") to create your own models through 

[transfer
learning](https://aws.amazon.com/what-is/transfer-learning/ "https://aws.amazon.com/what-is/transfer-learning/"). 4. Next, the model needs to be compiled and packaged as an [AWS IoT Greengrass](https://aws.amazon.com/greengrass/ "https://aws.amazon.com/greengrass/") component. 5. Deploy the trained model from previous step to an Edge device for running
production-level inferences using AWS IoT Greengrass. 6. Present camera images to the image anomaly detection model AWS IoT Greengrass component
for anomaly detection. 7. Publish the inference results to an [AWS IoT Core](https://aws.amazon.com/iot-core/ "https://aws.amazon.com/iot-core/") MQTT topic. 8. Perform automated actions on the machine of concern and notify plant personnel of
detected anomalies using the AWS IoT Greengrass component. For example, this component
can run a product rejection workflow by activating an industrial robot arm or
switching the colors in the tower lights to indicate product quality issues. 9. Ingest process data into the [AWS IoT SiteWise](https://aws.amazon.com/iot-sitewise/ "https://aws.amazon.com/iot-sitewise/") Edge
gateway running on AWS IoT Greengrass from the machine and equipment using standard
industrial protocols like OPC-UA, Modbus TCP/RTU, EtherNet/IP, or BACnet. 10. Push the ingested process data to AWS IoT SiteWise. 11. Compute key performance indicator (KPI) metrics, such as overall equipment
effectiveness (OEE), from the process data in AWS IoT SiteWise. Create monitoring and
KPI dashboards in [IoT Dashboard
application](https://github.com/awslabs/iot-application/tree/main "https://github.com/awslabs/iot-application/tree/main") or 

[Amazon Managed Grafana](https://aws.amazon.com/grafana/ "https://aws.amazon.com/grafana/") for operations users. 12. Create events from plant data and enterprise metadata by routing data to [AWS IoT Events](https://aws.amazon.com/iot-events/ "https://aws.amazon.com/iot-events/") through AWS IoT Core, and send email or text notifications to operations users using the 

[Amazon Simple Notification Service (Amazon SNS)](https://aws.amazon.com/sns/ "https://aws.amazon.com/sns/"). 13. Store the historical logs, event metadata and vision inference data streams in
Amazon S3. Using data stored in Amazon S3, and real-time and historical time-series
process data from AWS IoT SiteWise, train root cause analysis models in [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ "https://aws.amazon.com/sagemaker/"). Run model
inference on Amazon SageMaker AI to identify the root cause of issues.

## Resources

- [Defect Detection App User Guide](../../../lookout-for-vision/latest/dda-user-guide/what-is.md "../../../lookout-for-vision/latest/dda-user-guide/what-is.md")
- [Using AWS generative AI to improve defect detection in Manufacturing](https://aws.amazon.com/blogs/industries/using-aws-generative-ai-to-improve-defect-detection-in-manufacturing "https://aws.amazon.com/blogs/industries/using-aws-generative-ai-to-improve-defect-detection-in-manufacturing")
- [Zero-Training Visual Defect Detection](https://github.com/aws-samples/sample-generative-visual-inspection "https://github.com/aws-samples/sample-generative-visual-inspection")
