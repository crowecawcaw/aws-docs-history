# MLOE-05: Prepare an ML profile template

Prepare an ML profile template to capture workload artifacts
across ML lifecycle phases. The template helps enable evaluating
the current maturity status of a workload and plan for
improvements accordingly. Artifact examples to capture for the
deployment phase include: model instance size, model update
schedule, and model deployment location. This template should
have artifact metrics with thresholds to evaluate and rank the
level of maturity. Enable the ML profile template to reflect
workload maturity status with snapshots of existing profiles, and
alternative target profiles. Provide documentation with rationale
for choosing one option over another that meets the business
requirements.

## Implementation plan

- **Capture ML workload deployment
  characteristics** - Capture the most impactful
  deployment characteristics of your ML workload. In this
  paper, we will highlight the characteristics as a sample
  profile template on AWS. The collected design and
  provisioning characteristics will help identify the
  optimal deployment architecture, including computing and
  inference instance types and sizes.
- **Map ML workload characteristics
  across a spectrum from lower to higher ranges**
  -Ideally, there should be at least two profile templates
  generated for each workload characteristic. One ML profile
  template gives a snapshot of the current workload profile.
  Another profile template can be instantiated to capture the
  target or future characteristics of the ML workload.

 
Documentation should provide the rationale for justifying the characteristic values in the target profile.

Sample design, architecture, and provisioning characteristics include:

- **Model deployment sample
  characteristics include:**
  - Model size (model.tar.gz) in bytes
  - Number of models deployed per endpoint
  - Instance size (for example,
    [r5dn.4x.large](https://aws.amazon.com/ec2/instance-types/r5/ "https://aws.amazon.com/ec2/instance-types/r5/"))
    as suggested by the inference recommender
  - Retraining and model endpoint update frequency
    (hourly, daily, weekly, monthly, or per-event)
  - Model deployment location (on
    premises, [Amazon EC2](https://aws.amazon.com/ec2/?ec2-whats-new.sort-by=item.additionalFields.postDateTime&ec2-whats-new.sort-order=desc "https://aws.amazon.com/ec2/?ec2-whats-new.sort-by=item.additionalFields.postDateTime&ec2-whats-new.sort-order=desc"), container, serverless, or edge)

- **Architectural deployment sample
  characteristics** for the internal underlying
  algorithm or neural architecture includes:
  - Inference pipeline architecture (single endpoint, or
    chained endpoints)
  - Neural architecture (single framework (Scikit-learn),
    or multi-framework (PyTorch+ Scikit-learn +
    TensorFlow))
  - Containers
    ([SageMaker AI
    prebuilt container](../../../sagemaker/latest/dg/pre-built-containers-frameworks-deep-learning.md "../../../sagemaker/latest/dg/pre-built-containers-frameworks-deep-learning.md"), bring your own container)
  - Location of the containers and models (on premises,
    cloud, or hybrid)
  - Serverless inferencing (pay as you go)

- **Traffic pattern deployment sample
  characteristics include:**
  - Traffic pattern (steady, or spiky)
  - Input size (number of bytes)
  - Latency (low, medium, high, or batch)
  - Concurrency (single thread, or multi-thread)

- **Cold start tolerance
  characteristics** - Determine and document the
  tolerance of the various aspects of cold start in
  milliseconds.
- **Network deployment
  characteristics** - Check for the applicability
  of network deployment characteristics including
  [AWS KMS](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/") encryption, multi-variant endpoints, network
  isolation, and third-party Docker repositories.
- **Cost considerations** -
  Discuss and document the cost considerations for elements,
  such as
  [Amazon EC2 Spot Instances](https://aws.amazon.com/ec2/spot/ "https://aws.amazon.com/ec2/spot/").
- **Determine provisioning
  matrix** - Critical ML workloads might be vying
  for resources from cloud providers. For staging and
  production environments, include a matrix of the expected
  capacity requirements. This matrix consists of the number
  of instance types per AWS Region across training, batch
  interference, real-time inference, and notebooks.
