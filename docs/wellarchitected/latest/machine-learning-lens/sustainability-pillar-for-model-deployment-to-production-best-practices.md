# Sustainability pillar - Best practices

The sustainability pillar focuses on environmental impacts,
especially energy consumption and efficiency, since they are
important levers for architects to inform direct action to reduce
resource usage. 

###### Best practices

- [MLSUS-11: Align SLAs with sustainability goals](mlsus-11.md "mlsus-11.md")
- [MLSUS-12: Use efficient silicon](mlsus-12.md "mlsus-12.md")
- [MLSUS-13: Optimize models for inference](mlsus-13.md "mlsus-13.md")
- [MLSUS-14: Deploy multiple models behind a single endpoint](mlsus-14.md "mlsus-14.md")

**Related best practices**

- **Allow automatic scaling of the model
  endpoint**
  ([MLREL-11](mlrel-11.md "mlrel-11.md"))

* Configure
  [automatic
  scaling](../../../sagemaker/latest/dg/endpoint-auto-scaling.md "../../../sagemaker/latest/dg/endpoint-auto-scaling.md") for Amazon SageMaker AI Endpoints or use
  [Serverless
  Inference](../../../sagemaker/latest/dg/serverless-endpoints.md "../../../sagemaker/latest/dg/serverless-endpoints.md") and make efficient use of GPU with
  [Amazon Elastic Inference](https://aws.amazon.com/machine-learning/elastic-inference/ "https://aws.amazon.com/machine-learning/elastic-inference/"). Elastic Inference allows you to
  attach just the right amount of GPU-powered inference
  acceleration to any EC2 or SageMaker AI instance type or ECS
  task. While training jobs process hundreds of data samples
  in parallel, inference jobs usually process a single input
  in real time, and thus consume a small amount of GPU
  compute. Amazon Elastic Inference allows you to reduce the
  cost and environmental impact of your inference by using GPU
  resources more efficiently.

- **Evaluate machine learning deployment
  option (cloud versus edge)**
  ([MLPER-11](mlper-11.md "mlper-11.md"))

* When working on IoT use-cases, evaluate if running ML
  inference at the edge can reduce the environmental impact of
  your workload. For that, consider factors like the compute
  capacity of your devices, their energy consumption or the
  emissions related to data transfer to the Cloud. When
  [deploying
  ML models to edge devices](https://aws.amazon.com/blogs/machine-learning/build-machine-learning-at-the-edge-applications-using-amazon-sagemaker-edge-manager-and-aws-iot-greengrass-v2/ "https://aws.amazon.com/blogs/machine-learning/build-machine-learning-at-the-edge-applications-using-amazon-sagemaker-edge-manager-and-aws-iot-greengrass-v2/"), consider using
  [Amazon SageMaker AI Edge Manager](https://aws.amazon.com/sagemaker/edge-manager/ "https://aws.amazon.com/sagemaker/edge-manager/") which integrates with
  SageMaker AI Neo and
  [AWS IoT GreenGrass](https://aws.amazon.com/greengrass/ "https://aws.amazon.com/greengrass/").

- **Select optimal computing instance
  size**
  ([MLCOST-09](mlcost-12.md "mlcost-12.md"))

* [Amazon SageMaker AI Inference Recommender](../../../sagemaker/latest/dg/inference-recommender.md "../../../sagemaker/latest/dg/inference-recommender.md") automates load
  testing and model tuning across SageMaker AI ML instances. It
  helps you select the best instance type and configuration
  (such as instance count, container parameters, and model
  optimizations) to ensure the maximum efficiency of the
  resources provisioned for inference.
