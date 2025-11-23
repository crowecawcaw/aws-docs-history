# MLREL04-BP01 Automate endpoint changes through a

pipeline

Manual change management can be error prone and potentially incur a
high effort cost. Use automated pipelines (that integrate with a
change management tracking system) to deploy changes to your model
endpoints. Versioned pipeline inputs and artifacts allow you to
track the changes and automatically rollback after a failed change.

**Desired outcome:** You establish a
reliable and consistent deployment process for your machine learning
models. You gain the ability to track changes, perform automatic
rollbacks when needed, and improve adherence to change management
policies. This approach reduces manual errors, increases operational
efficiency, and provides you with better visibility into your ML
deployment lifecycle.

**Common anti-patterns:**

- Making manual updates directly to production endpoints.
- Using different deployment processes across teams or
  environments.
- Lacking proper version control for model artifacts.
- Not having clear rollback mechanisms for failed deployments.
- Bypassing change management tracking systems.

**Benefits of establishing this best
practice:**

- Reduces human error during deployments.
- Increases deployment speed and reliability.
- Improves traceability and auditability of changes.
- Enables rollback to previous versions.
- Improves adherence to change management policies.
- Supports scalable ML operations across multiple models.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Implementing automated pipelines for model endpoint changes brings
consistency and reliability to your ML operations. By using a
standardized deployment approach, you can verify that that changes
to production endpoints follow the same validated process. This
reduces the risk of deployment errors and improves overall
operational efficiency.

The pipeline should include steps for testing, validation, and
approval of model changes before they reach production.
Integration with your existing change management system allows for
proper tracking and documentation of changes. The pipeline should
also maintain versioned artifacts of models deployed, enabling
rollback if issues arise in production.

### Implementation steps

1. **Set up a CI/CD pipeline for ML
   workloads**. Establish a continuous integration and
   continuous delivery pipeline specifically designed for
   machine learning workloads.
   [Amazon SageMaker AI Pipelines](https://aws.amazon.com/sagemaker/pipelines/ "https://aws.amazon.com/sagemaker/pipelines/") provides a purpose-built solution
   for creating end-to-end ML workflows at scale.
2. **Integrate with change management
   systems**. Connect your pipeline to existing change
   management tracking systems to document endpoint changes.
   This improves adherence with your organization's governance
   requirements and provides a full audit trail of deployment
   activity.
3. **Implement artifact
   versioning**. Store model artifacts, code, and
   configuration files in version control. Use
   [Amazon SageMaker AI Model Registry](../../../sagemaker/latest/dg/model-registry.md "../../../sagemaker/latest/dg/model-registry.md") to catalog and version your
   models, making it straightforward to track which model
   versions are deployed to which endpoints.
4. **Define automated testing and
   validation**. Include automated testing steps in
   your pipeline to validate model performance before
   deployment. This should include unit tests, integration
   tests, and model quality evaluations using metrics specific
   to your use case.
5. **Establish approval gates**.
   Configure approval checkpoints in your pipeline where
   stakeholders can review changes before they are promoted to
   production. These gates maintain quality control and improve
   adherence to business requirements.
6. **Implement automated rollback
   mechanisms**. Create automated procedures to roll
   back to the previous stable version if a deployment fails or
   if issues are detected after deployment. This minimizes
   downtime and impact on users.
7. **Monitor deployment
   metrics**. Track the success rate of deployments
   and time-to-deployment metrics to continuously improve your
   pipeline. Use
   [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") to monitor these operational metrics.

## Resources

**Related documents:**

- [Pipelines
  overview](../../../sagemaker/latest/dg/pipelines-sdk.md "../../../sagemaker/latest/dg/pipelines-sdk.md")
- [Model
  Registration Deployment with Model Registry](../../../sagemaker/latest/dg/model-registry.md "../../../sagemaker/latest/dg/model-registry.md")
- [Data
  and model quality monitoring with Amazon SageMaker AI Model
  Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md")
- [Build
  a CI/CD pipeline for deploying custom machine learning models
  using AWS services](https://aws.amazon.com/blogs/machine-learning/build-a-ci-cd-pipeline-for-deploying-custom-machine-learning-models-using-aws-services/ "https://aws.amazon.com/blogs/machine-learning/build-a-ci-cd-pipeline-for-deploying-custom-machine-learning-models-using-aws-services/")
- [Building,
  automating, managing, and scaling ML workflows using Amazon SageMaker AI Pipelines](https://aws.amazon.com/blogs/machine-learning/building-automating-managing-and-scaling-ml-workflows-using-amazon-sagemaker-pipelines/ "https://aws.amazon.com/blogs/machine-learning/building-automating-managing-and-scaling-ml-workflows-using-amazon-sagemaker-pipelines/")

**Related videos:**

- [Implementing
  MLOps practices with Amazon SageMaker AI](https://youtu.be/fuXUi_hoK78 "https://youtu.be/fuXUi_hoK78")

**Related examples:**

- [SageMaker AI
  Pipelines and SageMaker AI Model Registry](https://github.com/aws/amazon-sagemaker-examples/tree/default/%20%20%20ml_ops "https://github.com/aws/amazon-sagemaker-examples/tree/default/%20%20%20ml_ops")
