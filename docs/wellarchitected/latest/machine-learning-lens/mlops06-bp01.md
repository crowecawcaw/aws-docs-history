# MLOPS06-BP01 Synchronize architecture and configuration, and

check for skew across environments

Synchronize your systems and configurations across development and
deployment phases for consistent machine learning model inference
results. By maintaining identical environments, you can avoid
discrepancies that arise from architectural differences, leading to
more reliable and predictable model performance.

**Desired outcome:** You have
established a systematic approach to foster architectural and
configuration consistency across development, staging, and
production environments for machine learning models. This includes
automated infrastructure deployment, continuous model quality
monitoring, and proactive detection of environmental skew. Your
machine learning systems deliver the same range of accuracy
regardless of which environment they run in, and you can quickly
identify and address deviations.

**Common anti-patterns:**

- Manually configuring each environment, leading to
  inconsistencies.
- Neglecting to validate model performance across different
  environments.
- Assuming model behavior will be identical across environments
  without verification.
- Using different hardware specifications or software versions
  between environments.
- Making changes only when needed to production environments
  without documenting or replicating them in other environments.

**Benefits of establishing this best
practice:**

- Consistent model performance across environments.
- Reduced debugging time for environment-specific issues.
- Improved reliability of machine learning applications.
- Straightforward identification of the root causes of performance
  deviations.
- Streamlined promotion process from development to production.
- Enhanced confidence in deployed models.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Synchronizing your machine learning environments is critical for
checking that a model trained in one environment behaves the same
way when deployed in another. Differences in system architectures,
software dependencies, or configuration settings can cause
unexpected variations in model performance, leading to inaccurate
predictions or even system failures.

By treating your infrastructure as code and implementing automated
monitoring, you can maintain consistency across environments and
quickly detect deviations. This approach allows you to focus on
improving your models rather than debugging environment-specific
issues. It also provides a reliable foundation for continuous
delivery of machine learning solutions.

Environmental skew can occur in various ways, such as through
differences in hardware capabilities, software versions, or system
configurations. For example, a model trained on a development
environment with specific CPU architecture might behave
differently when deployed to a production environment with
different specifications. Similarly, differences in underlying
libraries or dependencies can lead to subtle variations in model
behavior.

Regular validation of model performance across environments should
be part of your standard promotion process. This includes
comparing not only the accuracy metrics but also the distribution
of predictions and the model's behavior for edge cases.

### Implementation steps

1. **Define infrastructure as code using
   AWS CloudFormation**. Create CloudFormation
   templates that define resources, configurations, and
   dependencies for your machine learning environments. With
   this strategy, each environment is provisioned consistently
   and can be recreated identically when needed. Include
   compute resources, networking configurations, security
   settings, and machine learning-specific components.
2. **Implement version control for
   infrastructure templates**. Store your
   CloudFormation templates in a version control system like
   AWS CodeCommit or GitHub. This allows you to track changes
   over time, roll back to previous configurations if needed,
   and verify that your environments are using the same version
   of the infrastructure definition.
3. **Set up CI/CD pipelines for
   infrastructure deployment**. Use AWS CodePipeline
   or AWS CodeBuild to automate the deployment of your
   infrastructure changes across environments. This reduces
   manual intervention and the potential for human error when
   updating environments.
4. **Configure Amazon SageMaker AI Model
   Monitor for continuous quality evaluation**. Set up
   Model Monitor to automatically track the quality of your
   models in production and compare the results with the
   baseline established during training. This can identify when
   model performance starts to drift due to environmental
   factors or data changes.
5. **Implement data quality
   monitoring**. Use SageMaker AI Model Monitor's data
   quality monitoring capability to detect changes in the
   statistical properties of your input data across
   environments. This capability provides similar input
   distributions to your models regardless of environment.
6. **Set up model quality
   monitoring**. Configure SageMaker AI Model Monitor to
   track model quality metrics such as accuracy, precision, and
   recall over time. Compare these metrics between your
   development, staging, and production environments to detect
   inconsistencies.
7. **Enable bias drift
   monitoring**. Use SageMaker AI Model Monitor's bias
   drift monitoring to detect if your models exhibit different
   biases in different environments, which could indicate
   environment-specific issues.
8. **Configure alerts for
   deviations**. Set up Amazon CloudWatch alarms to
   notify you when SageMaker AI Model Monitor detects significant
   deviations in model performance or data characteristics
   across environments. This allows for proactive intervention
   before small issues become major problems.
9. **Establish a promotion
   checklist**. Create a formal checklist that
   includes verifying model performance consistency across
   environments before promoting a model to the next stage.
   Document the acceptable thresholds for performance
   differences between environments.
10. **Implement regular cross-environment
    validation**. Schedule periodic validation of model
    performance across your environments, even when no changes
    are being made. Use this validation to catch gradual drift
    that might occur due to external factors.
11. **Create environment comparison
    dashboards**. Use
    [Quick Suite with GenBI capabilities](https://aws.amazon.com/quicksight/generative-bi/ "https://aws.amazon.com/quicksight/generative-bi/") to automatically
    generate visualizations and dashboards for model performance
    metrics across different environments, making it more
    straightforward to spot discrepancies and track trends over
    time.
12. **Utilize foundation models for
    anomaly detection**. Implement
    [Amazon
    Bedrock](https://aws.amazon.com/bedrock/knowledge-bases/ "https://aws.amazon.com/bedrock/knowledge-bases/") or
    [SageMaker AI
    JumpStart](https://aws.amazon.com/sagemaker/jumpstart/ "https://aws.amazon.com/sagemaker/jumpstart/") with expanded library of foundation models
    to analyze performance patterns and identify anomalous
    behavior that might indicate environmental inconsistencies,
    especially for complex ML systems where traditional
    monitoring might miss subtle differences.

## Resources

**Related documents:**

- [Data
  and model quality monitoring with Amazon SageMaker AI Model
  Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md")
- [What
  is AWS CloudFormation?](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")
- [What
  is AWS Config?](../../../config/latest/developerguide/WhatIsConfig.md "../../../config/latest/developerguide/WhatIsConfig.md")
- [Detect
  unmanaged configuration changes to stacks and resources with
  drift detection](../../../AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.md "../../../AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.md")
- [AWS Systems Manager Parameter Store](../../../systems-manager/latest/userguide/systems-manager-parameter-store.md "../../../systems-manager/latest/userguide/systems-manager-parameter-store.md")
- [Amazon SageMaker AI best practices](../../../sagemaker/latest/dg/best-practices.md "../../../sagemaker/latest/dg/best-practices.md")

**Related examples:**

- [Introduction
  to Amazon SageMaker AI Model Monitor](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker_model_monitor/introduction/SageMaker AI-ModelMonitoring.html "https://sagemaker-examples.readthedocs.io/en/latest/sagemaker_model_monitor/introduction/SageMaker AI-ModelMonitoring.html")
- [Model
  Monitor Visualization](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker_model_monitor/visualization/SageMaker AI-Model-Monitor-Visualize.html "https://sagemaker-examples.readthedocs.io/en/latest/sagemaker_model_monitor/visualization/SageMaker AI-Model-Monitor-Visualize.html")
