

# Security Hub CSPM controls for SageMaker AI
<a name="sagemaker-controls"></a>

These AWS Security Hub CSPM controls evaluate the Amazon SageMaker AI service and resources. The controls might not be available in all AWS Regions. For more information, see [Availability of controls by Region](securityhub-regions.md#securityhub-regions-control-support).

## [SageMaker.1] Amazon SageMaker notebook instances should not have direct internet access
<a name="sagemaker-1"></a>

**Related requirements:** NIST.800-53.r5 AC-21, NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-4, NIST.800-53.r5 AC-4(21), NIST.800-53.r5 AC-6, NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(11), NIST.800-53.r5 SC-7(16), NIST.800-53.r5 SC-7(20), NIST.800-53.r5 SC-7(21), NIST.800-53.r5 SC-7(3), NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-7(9), PCI DSS v3.2.1/1.2.1, PCI DSS v3.2.1/1.3.1, PCI DSS v3.2.1/1.3.2, PCI DSS v3.2.1/1.3.4, PCI DSS v3.2.1/1.3.6, PCI DSS v4.0.1/1.4.4

**Category:** Protect > Secure network configuration

**Severity:** High

**Resource type:** `AWS::SageMaker::NotebookInstance`

**AWS Config rule:** [sagemaker-notebook-no-direct-internet-access](https://docs.aws.amazon.com/config/latest/developerguide/sagemaker-notebook-no-direct-internet-access.html)

**Schedule type:** Periodic

**Parameters:** None

This control checks whether direct internet access is disabled for an SageMaker AI notebook instance. The control fails if the `DirectInternetAccess` field is enabled for the notebook instance. 

If you configure your SageMaker AI instance without a VPC, then by default direct internet access is enabled on your instance. You should configure your instance with a VPC and change the default setting to **Disable—Access the internet through a VPC**. To train or host models from a notebook, you need internet access. To enable internet access, your VPC must have either an interface endpoint (AWS PrivateLink) or a NAT gateway and a security group that allows outbound connections. To learn more about how to connect a notebook instance to resources in a VPC, see [Connect a notebook instance to resources in a VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/appendix-notebook-and-internet-access.html) in the *Amazon SageMaker AI Developer Guide*. You should also ensure that access to your SageMaker AI configuration is limited to only authorized users. Restrict IAM permissions that permit users to change SageMaker AI settings and resources.

### Remediation
<a name="sagemaker-1-remediation"></a>

You can't change the internet access setting after creating a notebook instance. Instead, you can stop, delete, and recreate the instance with blocked internet access. To delete a notebook instance that permits direct internet access, see [Use notebook instances to build models: Clean up](https://docs.aws.amazon.com/sagemaker/latest/dg/ex1-cleanup.html) in the *Amazon SageMaker AI Developer Guide*. To recreate a notebook instance that denies internet access, see [Create a notebook instance](https://docs.aws.amazon.com/sagemaker/latest/dg/howitworks-create-ws.html). For **Network, Direct internet access**, choose **Disable—Access the internet through a VPC**.

## [SageMaker.2] SageMaker notebook instances should be launched in a custom VPC
<a name="sagemaker-2"></a>

**Related requirements:** NIST.800-53.r5 AC-21, NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-4, NIST.800-53.r5 AC-4(21), NIST.800-53.r5 AC-6, NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(11), NIST.800-53.r5 SC-7(16), NIST.800-53.r5 SC-7(20), NIST.800-53.r5 SC-7(21), NIST.800-53.r5 SC-7(3), NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-7(9)

**Category:** Protect > Secure network configuration > Resources within VPC

**Severity:** High

**Resource type:** `AWS::SageMaker::NotebookInstance`

**AWS Config rule:** [sagemaker-notebook-instance-inside-vpc](https://docs.aws.amazon.com/config/latest/developerguide/sagemaker-notebook-instance-inside-vpc.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks if an Amazon SageMaker AI notebook instance is launched within a custom virtual private cloud (VPC). This control fails if a SageMaker AI notebook instance is not launched within a custom VPC or if it is launched in the SageMaker AI service VPC.

Subnets are a range of IP addresses within a VPC. We recommend keeping your resources inside a custom VPC whenever possible to ensure secure network protection of your infrastructure. An Amazon VPC is a virtual network dedicated to your AWS account. With an Amazon VPC, you can control the network access and internet connectivity of your SageMaker AI Studio and notebook instances.

### Remediation
<a name="sagemaker-2-remediation"></a>

You can't change the VPC setting after creating a notebook instance. Instead, you can stop, delete, and recreate the instance. For instructions, see [Use notebook instances to build models: Clean up](https://docs.aws.amazon.com/sagemaker/latest/dg/ex1-cleanup.html) in the *Amazon SageMaker AI Developer Guide*.

## [SageMaker.3] Users should not have root access to SageMaker notebook instances
<a name="sagemaker-3"></a>

**Related requirements:** NIST.800-53.r5 AC-2(1), NIST.800-53.r5 AC-3(15), NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-6, NIST.800-53.r5 AC-6(10), NIST.800-53.r5 AC-6(2)

**Category:** Protect > Secure access management > Root user access restrictions

**Severity:** High

**Resource type:** `AWS::SageMaker::NotebookInstance`

**AWS Config rule:** [sagemaker-notebook-instance-root-access-check](https://docs.aws.amazon.com/config/latest/developerguide/sagemaker-notebook-instance-root-access-check.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether root access is turned on for an Amazon SageMaker AI notebook instance. The control fails if root access is turned on for a SageMaker AI notebook instance.

In adherence to the principal of least privilege, it is a recommended security best practice to restrict root access to instance resources to avoid unintentionally over provisioning permissions.

### Remediation
<a name="sagemaker-3-remediation"></a>

To restrict root access to SageMaker AI notebook instances, see [Control root access to a SageMaker AI notebook instance](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-root-access.html) in the *Amazon SageMaker AI Developer Guide*.

## [SageMaker.4] SageMaker endpoint production variants should have an initial instance count greater than 1
<a name="sagemaker-4"></a>

**Related requirements:** NIST.800-53.r5 CP-10, NIST.800-53.r5 SC-5, NIST.800-53.r5 SC-36, NIST.800-53.r5 SA-13

**Category:** Recover > Resilience > High availability

**Severity:** Medium

**Resource type:** `AWS::SageMaker::EndpointConfig`

**AWS Config rule:** [sagemaker-endpoint-config-prod-instance-count](https://docs.aws.amazon.com/config/latest/developerguide/sagemaker-endpoint-config-prod-instance-count.html)

**Schedule type:** Periodic

**Parameters:** None

This control checks whether production variants of an Amazon SageMaker AI endpoint have an initial instance count greater than 1. The control fails if the endpoint's production variants have only 1 initial instance.

Production variants running with an instance count greater than 1 permit multi-AZ instance redundancy managed by SageMaker AI. Deploying resources across multiple Availability Zones is an AWS best practice to provide high availability within your architecture. High availability helps you to recover from security incidents.

**Note**  
This control applies only to instance-based endpoint configuration.

### Remediation
<a name="sagemaker-4-remediation"></a>

For more information about the parameters of endpoint configuration, see [Create an endpoint configuration](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints-create.html#serverless-endpoints-create-config) in the *Amazon SageMaker AI Developer Guide*.

## [SageMaker.5] SageMaker models should have network isolation enabled
<a name="sagemaker-5"></a>

**Category:** Protect > Secure network configuration > Resources not publicly accessible

**Severity:** Medium

**Resource type:** `AWS::SageMaker::Model`

**AWS Config rule:** [sagemaker-model-isolation-enabled](https://docs.aws.amazon.com/config/latest/developerguide/sagemaker-model-isolation-enabled.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon SageMaker AI hosted model has network isolation enabled. The control fails if the `EnableNetworkIsolation` parameter for the hosted model is set to `False`.

SageMaker AI training and deployed inference containers are internet-enabled by default. If you don't want SageMaker AI to provide external network access to your training or inference containers, you can enable network isolation. If you enable network isolation, no inbound or outbound network calls can be made to or from the model container, including calls to or from other AWS services. Additionally, no AWS credentials are made available to the container runtime environment. Enabling network isolation helps prevent unintended access to your SageMaker AI resources from the internet.

**Note**  
On August 13, 2025, Security Hub CSPM changed the title and description of this control. The new title and description more accurately reflect that the control checks the setting for the `EnableNetworkIsolation` parameter of Amazon SageMaker AI hosted models. Previously, the title of this control was: *SageMaker models should block inbound traffic*.

### Remediation
<a name="sagemaker-5-remediation"></a>

For more information about network isolation for SageMaker AI models, see [Run training and inference containers in internet-free mode](https://docs.aws.amazon.com/sagemaker/latest/dg/mkt-algo-model-internet-free.html) in the *Amazon SageMaker AI Developer Guide*. When you create a model, you can enable network isolation by setting the value for the `EnableNetworkIsolation` parameter to `True`.

## [SageMaker.6] SageMaker app image configurations should be tagged
<a name="sagemaker-6"></a>

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::SageMaker::AppImageConfig`

**AWS Config rule:** [sagemaker-app-image-config-tagged](https://docs.aws.amazon.com/config/latest/developerguide/sagemaker-app-image-config-tagged.html)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
| requiredKeyTags | A list of non-system tag keys that must be assigned to an evaluated resource. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions). | No default value | 

This control checks whether an Amazon SageMaker AI app image configuration (`AppImageConfig`) has the tag keys specified by the `requiredKeyTags` parameter. The control fails if the app image configuration doesn't have any tag keys, or it doesn't have all the keys specified by the `requiredKeyTags` parameter. If you don't specify any values for the `requiredKeyTags` parameter, the control checks only for the existence of a tag key and fails if the app image configuration doesn't have any tag keys. The control ignores system tags, which are applied automatically and have the `aws:` prefix.

A tag is a label that you create and assign to an AWS resource. Each tag consists of a required tag key and an optional tag value. You can use tags to categorize resources by purpose, owner, environment, or other criteria. They can help you identify, organize, search for, and filter resources. They can also help you track resource owners for actions and notifications. You can also use tags to implement attribute-based access control (ABAC) as an authorization strategy. For more information about ABAC strategies, see [Define permissions based on attributes with ABAC authorization](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*. For more information about tags, see the [Tagging AWS Resources and Tag Editor User Guide](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html).

**Note**  
Do not store personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible from many AWS services. They aren't intended to be used for private or sensitive data.

### Remediation
<a name="sagemaker-6-remediation"></a>

To add tags to an Amazon SageMaker AI app image configuration (`AppImageConfig`), you can use the [AddTags](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AddTags.html) operation of the SageMaker AI API or, if you're using the AWS CLI, run the [add-tags](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/add-tags.html) command.

## [SageMaker.7] SageMaker images should be tagged
<a name="sagemaker-7"></a>

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::SageMaker::Image`

**AWS Config rule:** [sagemaker-image-tagged](https://docs.aws.amazon.com/config/latest/developerguide/sagemaker-image-tagged.html)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
| requiredKeyTags | A list of non-system tag keys that must be assigned to an evaluated resource. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions). | No default value | 

This control checks whether an Amazon SageMaker AI image has the tag keys specified by the `requiredKeyTags` parameter. The control fails if the image doesn't have any tag keys, or it doesn't have all the keys specified by the `requiredKeyTags` parameter. If you don't specify any values for the `requiredKeyTags` parameter, the control checks only for the existence of a tag key and fails if the image doesn't have any tag keys. The control ignores system tags, which are applied automatically and have the `aws:` prefix.

A tag is a label that you create and assign to an AWS resource. Each tag consists of a required tag key and an optional tag value. You can use tags to categorize resources by purpose, owner, environment, or other criteria. They can help you identify, organize, search for, and filter resources. They can also help you track resource owners for actions and notifications. You can also use tags to implement attribute-based access control (ABAC) as an authorization strategy. For more information about ABAC strategies, see [Define permissions based on attributes with ABAC authorization](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*. For more information about tags, see the [Tagging AWS Resources and Tag Editor User Guide](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html).

**Note**  
Do not store personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible from many AWS services. They aren't intended to be used for private or sensitive data.

### Remediation
<a name="sagemaker-7-remediation"></a>

To add tags to an Amazon SageMaker AI image, you can use the [AddTags](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AddTags.html) operation of the SageMaker AI API or, if you're using the AWS CLI, run the [add-tags](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/add-tags.html) command.

## [SageMaker.8] SageMaker notebook instances should run on supported platforms
<a name="sagemaker-8"></a>

**Category:** Detect > Vulnerability, patch, and version management

**Severity:** Medium

**Resource type:** `AWS::SageMaker::NotebookInstance`

**AWS Config rule:** [sagemaker-notebook-instance-platform-version](https://docs.aws.amazon.com/config/latest/developerguide/sagemaker-notebook-instance-platform-version.html)

**Schedule type:** Periodic

**Parameters:**
+ `supportedPlatformIdentifierVersions`: `notebook-al2023-v1` (not customizable)

This control checks whether an Amazon SageMaker AI notebook instance is configured to run on a supported platform, based on the platform identifier specified for the notebook instance. The control fails if the notebook instance is configured to run on a platform that's no longer supported.

If the platform for an Amazon SageMaker AI notebook instance is no longer supported, it might not receive security patches, bug fixes, or other types of updates. Notebook instances might continue to function, but they won't receive SageMaker AI security updates or critical bug fixes. You assume the risks associated with using an unsupported platform. For more information, see [JupyterLab versioning](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-jl.html) in the *Amazon SageMaker AI Developer Guide*.

### Remediation
<a name="sagemaker-8-remediation"></a>

For information about the platforms that Amazon SageMaker AI currently supports and how to migrate to them, see [Amazon Linux 2 notebook instances](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-al2.html) in the *Amazon SageMaker AI Developer Guide*.

## [SageMaker.9] SageMaker data quality job definitions should have inter-container traffic encryption enabled
<a name="sagemaker-9"></a>

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:** `AWS::SageMaker::DataQualityJobDefinition`

**AWS Config rule:** [sagemaker-data-quality-job-encrypt-in-transit](https://docs.aws.amazon.com/config/latest/developerguide/sagemaker-data-quality-job-encrypt-in-transit.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon SageMaker AI data quality job definition has encryption enabled for inter-container traffic. The control fails if the definition for a job that monitors data quality and drift does not have encryption enabled for inter-container traffic.

Enabling inter-container traffic encryption protects sensitive ML data during distributed processing for data quality analysis. 

### Remediation
<a name="sagemaker-9-remediation"></a>

For more information about inter-container traffic encryption for Amazon SageMaker AI, see [Protect Communications Between ML Compute Instances in a Distributed Training Job](https://docs.aws.amazon.com/sagemaker/latest/dg/train-encrypt.html) in the *Amazon SageMaker AI Developer Guide*. When you create a data quality job definition, you can enable inter-container traffic encryption by setting the value for the `EnableInterContainerTrafficEncryption` parameter to `True`.

## [SageMaker.10] SageMaker model explainability job definitions should have inter-container traffic encryption enabled
<a name="sagemaker-10"></a>

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:** `AWS::SageMaker::ModelExplainabilityJobDefinition`

**AWS Config rule:** [sagemaker-model-explainability-job-encrypt-in-transit](https://docs.aws.amazon.com/config/latest/developerguide/sagemaker-model-explainability-job-encrypt-in-transit.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon SageMaker model explainability job definition has inter-container traffic encryption enabled. The control fails if the model explainability job definition does not have inter-container traffic encryption enabled.

Enabling inter-container traffic encryption protects sensitive ML data such as model data, training datasets, intermediate processing results, parameters and model weights during distributed processing for explainability analysis. 

### Remediation
<a name="sagemaker-10-remediation"></a>

For an existing SageMaker model explainability job definition, inter-container traffic encryption cannot be updated in place. To create a new SageMaker model explainability job definition with inter-container traffic encryption enabled, use [API](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateModelExplainabilityJobDefinition.html) or [CLI](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/create-model-explainability-job-definition.html) or [ CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-modelexplainabilityjobdefinition.html) and set [`EnableInterContainerTrafficEncryption`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MonitoringNetworkConfig.html#API_MonitoringNetworkConfig_Contents) to `True`.

## [SageMaker.11] SageMaker data quality job definitions should have network isolation enabled
<a name="sagemaker-11"></a>

**Category:** Protect > Secure network configuration

**Severity:** Medium

**Resource type:** `AWS::SageMaker::DataQualityJobDefinition`

**AWS Config rule:** [sagemaker-data-quality-job-isolation](https://docs.aws.amazon.com/config/latest/developerguide/sagemaker-data-quality-job-isolation.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon SageMaker AI data quality monitoring job definition has network isolation enabled. The control fails if the definition for a job that monitors data quality and drift has network isolation disabled.

Network isolation reduces the attack surface and prevents external access thereby protecting against unauthorized external access, accidental data exposure and potential data exfiltration. 

### Remediation
<a name="sagemaker-11-remediation"></a>

For more information about network isolation for SageMaker AI, see [Run training and inference containers in internet-free mode](https://docs.aws.amazon.com/sagemaker/latest/dg/mkt-algo-model-internet-free.html) in the *Amazon SageMaker AI Developer Guide*. When you create a data quality job definition, you can enable network isolation by setting the value for the `EnableNetworkIsolation` parameter to `True`.

## [SageMaker.12] SageMaker model bias job definitions should have network isolation enabled
<a name="sagemaker-12"></a>

**Category:** Protect > Secure network configuration > Resources policy configuration

**Severity:** Medium

**Resource type:** `AWS::SageMaker::ModelBiasJobDefinition`

**AWS Config rule:** [sagemaker-model-bias-job-isolation](https://docs.aws.amazon.com/config/latest/developerguide/sagemaker-model-bias-job-isolation.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether a SageMaker model bias job definition has network isolation enabled. The control fails if model bias job definition does not have network isolation enabled.

Network isolation prevents SageMaker model bias jobs from communicating with external resources over the internet. By enabling network isolation, you ensure that the job's containers cannot make outbound connections, reducing the attack surface and protecting sensitive data from exfiltration. This is particularly important for jobs processing regulated or sensitive data.

### Remediation
<a name="sagemaker-12-remediation"></a>

To enable network isolation, you must create a new model bias job definition with `EnableNetworkIsolation` parameter set to `True`. Network isolation cannot be modified after job definition creation. To create a new model bias job definition, see [ CreateModelBiasJobDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateModelBiasJobDefinition.html) in the *Amazon SageMaker AI Developer Guide*. 

## [SageMaker.13] SageMaker model quality job definitions should have inter-container traffic encryption enabled
<a name="sagemaker-13"></a>

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:** `AWS::SageMaker::ModelQualityJobDefinition`

**AWS Config rule:** [ssagemaker-model-quality-job-encrypt-in-transit](https://docs.aws.amazon.com/config/latest/developerguide/sagemaker-model-quality-job-encrypt-in-transit.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether Amazon SageMaker model quality job definitions have encryption in transit enabled for inter-container traffic. The control fails if a model quality job definition does not have inter-container traffic encryption enabled.

Inter-container traffic encryption protects data transmitted between containers during distributed model quality monitoring jobs. By default, inter-container traffic is unencrypted. Enabling encryption helps maintain data confidentiality during processing and supports compliance with regulatory requirements for data in transit protection.

### Remediation
<a name="sagemaker-13-remediation"></a>

To enable inter-container traffic encryption for your Amazon SageMaker model quality job definition, you must re-create the job definition with the appropriate in-transit encryption configuration. To create a model quality job definition, see [ CreateModelQualityJobDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateModelQualityJobDefinition.html) in the *Amazon SageMaker AI Developer Guide*. 

## [SageMaker.14] SageMaker monitoring schedules should have network isolation enabled
<a name="sagemaker-14"></a>

**Category:** Protect > Secure network configuration

**Severity:** Medium

**Resource type:** `AWS::SageMaker::MonitoringSchedule`

**AWS Config rule:** [sagemaker-monitoring-schedule-isolation](https://docs.aws.amazon.com/config/latest/developerguide/sagemaker-monitoring-schedule-isolation.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether Amazon SageMaker monitoring schedules have network isolation enabled. The control fails if a monitoring schedule has EnableNetworkIsolation set to false or not configured

Network isolation prevents monitoring jobs from making outbound network calls, reducing the attack surface by eliminating internet access from containers.

### Remediation
<a name="sagemaker-14-remediation"></a>

For information about configuring network isolation in the NetworkConfig parameter when creating or updating a monitoring schedule, see [CreateMonitoringSchedule](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateMonitoringSchedule.html) or [ UpdateMonitoringSchedule](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateMonitoringSchedule.html) in the *Amazon SageMaker AI Developer Guide*.

## [SageMaker.15] SageMaker model bias job definitions should have inter-container traffic encryption enabled
<a name="sagemaker-15"></a>

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:** `AWS::SageMaker::ModelBiasJobDefinition`

**AWS Config rule:** [sagemaker-model-bias-job-encrypt-in-transit](https://docs.aws.amazon.com/config/latest/developerguide/sagemaker-model-bias-job-encrypt-in-transit.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether Amazon SageMaker model bias job definitions have inter-container traffic encryption enabled when using multiple compute instances. The control fails if `EnableInterContainerTrafficEncryption` is set to false or is not configured for job definitions with an instance count of 2 or greater.

Inter-container traffic encryption protects data transmitted between compute instances during distributed model bias monitoring jobs. Encryption prevents unauthorized access to model-related information such as weights that are transmitted between instances.

### Remediation
<a name="sagemaker-15-remediation"></a>

To enable inter-container traffic encryption for SageMaker model bias job definitions, set the `EnableInterContainerTrafficEncryption` parameter to `True` when the job definition uses multiple compute instances. For information about protecting communications between ML compute instances, see [Protect Communications Between ML Compute Instances in a Distributed Training Job](https://docs.aws.amazon.com/sagemaker/latest/dg/train-encrypt.html) in the *Amazon SageMaker AI Developer Guide*. 

## [SageMaker.16] SageMaker models should use private registry in VPC for primary containers
<a name="sagemaker-16"></a>

**Category:** Protect > Secure network configuration > Resources within VPC

**Severity:** Medium

**Resource type:** `AWS::SageMaker::Model`

**AWS Config rule:** [sagemaker-model-private-registry-required](https://docs.aws.amazon.com/config/latest/developerguide/sagemaker-model-private-registry-required.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon SageMaker AI model pulls container image from a private registry in a VPC for the primary container. The control fails if the image is not configured or repository access mode is `Platform`.

Using a private Docker registry in a VPC for SageMaker model containers ensures container images are pulled from trusted, controlled sources within your VPC. Also, it ensures container images are accessed through VPC endpoints, without traversing the public internet.

### Remediation
<a name="sagemaker-16-remediation"></a>

To configure private docker registries for SageMaker AI real-time inference containers, see [Use a Private Docker Registry for Real-Time Inference Containers](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-containers-inference-private.html) in the *Amazon SageMaker AI Developer Guide*.

## [SageMaker.17] SageMaker feature group offline stores should be encrypted with AWS KMS keys
<a name="sagemaker-17"></a>

**Category:** Protect > Data Protection > Encryption of data-at-rest

**Severity:** Medium

**Resource type:** `AWS::SageMaker::FeatureGroup`

**AWS Config rule:** [sagemaker-featuregroup-encryption-at-rest](https://docs.aws.amazon.com/config/latest/developerguide/sagemaker-featuregroup-encryption-at-rest.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon SageMaker offline store for a feature group is encrypted at rest with an AWS KMS key. The control fails if the offline store S3 storage for a feature group is not encrypted with a KMS key.

Using customer-managed AWS KMS keys for encryption at rest of SageMaker feature group offline stores provide enhanced security. Customer-managed KMS keys provide you full control over encryption key lifecycle and key policies. Additionally, all encryption key usage can be logged and monitored through AWS CloudTrail for auditability.

### Remediation
<a name="sagemaker-17-remediation"></a>

For information on enabling encryption at rest for SageMaker Feature Store offline stores using AWS KMS customer-managed keys, see [Security and access control](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-security.html#feature-store-authorizing-use-cmk-offline-store) in the *Amazon SageMaker AI Developer Guide*.

## [SageMaker.18] SageMaker feature group online stores with standard storage should be encrypted with AWS KMS keys
<a name="sagemaker-18"></a>

**Related requirements:** NIST.800-53.r5 AU-9, NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-3(6), NIST.800-53.r5 SC-7(10), NIST.800-53.r5 SC-12(2), NIST.800-53.r5 SC-13, NIST.800-53.r5 SC-28, NIST.800-53.r5 SC-28(1), NIST.800-53.r5 SI-7(6)

**Category:** Protect > Data protection > Encryption of data at rest

**Severity:** Medium

**Resource type:** `AWS::SageMaker::FeatureGroup`

**AWS Config rule:** [sagemaker-featuregroup-online-store-encryption](https://docs.aws.amazon.com/config/latest/developerguide/sagemaker-featuregroup-online-store-encryption.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon SageMaker online store for a feature group with standard storage is encrypted at rest with an AWS KMS key. The control fails if KMS key encryption is not configured for the online store.

Using customer-managed AWS KMS keys for encryption at rest of SageMaker feature group online stores provides enhanced security. Customer-managed KMS keys give you full control over encryption key lifecycle and key policies. Additionally, all encryption key usage can be logged and monitored through AWS CloudTrail for auditability.

### Remediation
<a name="sagemaker-18-remediation"></a>

For information on enabling encryption at rest for SageMaker Feature Store online stores using AWS KMS customer-managed keys, see [Security and access control](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-security.html) in the *Amazon SageMaker AI Developer Guide*.

## [SageMaker.19] SageMaker models should use private registry in VPC for multi-container inference pipelines
<a name="sagemaker-19"></a>

**Category:** Protect > Secure network configuration > Resources within VPC

**Severity:** Medium

**Resource type:** `AWS::SageMaker::Model`

**AWS Config rule:** [sagemaker-model-multicontainer-private-registry](https://docs.aws.amazon.com/config/latest/developerguide/sagemaker-model-multicontainer-private-registry.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether Amazon SageMaker AI models with multi-container inference pipelines pull container images from a private Docker registry in a VPC. The control fails if any container definition does not have image configuration or has repository access mode set to platform.

Using a private Docker registry in a VPC for SageMaker AI multi-container inference pipelines ensures container images are pulled from trusted, controlled sources within your VPC. This ensures container images are accessed through VPC endpoints, without traversing the public internet, reducing the risk of supply chain attacks or image tampering.

### Remediation
<a name="sagemaker-19-remediation"></a>

To configure private docker registries for SageMaker AI real-time inference containers, see [Use a Private Docker Registry for Real-Time Inference Containers](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-containers-inference-private.html) in the *Amazon SageMaker AI Developer Guide*.

## [SageMaker.20] SageMaker model explainability job definitions should have network isolation enabled
<a name="sagemaker-20"></a>

**Category:** Protect > Secure network configuration > Resources not publicly accessible

**Severity:** High

**Resource type:** `AWS::SageMaker::ModelExplainabilityJobDefinition`

**AWS Config rule:** [sagemaker-model-explainability-job-network-isolation](https://docs.aws.amazon.com/config/latest/developerguide/sagemaker-model-explainability-job-network-isolation.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether a SageMaker AI model explainability job definition has network isolation enabled. The control fails if the job definition does not have network isolation enabled.

Network isolation prevents model explainability job containers from making outbound network calls, reducing the risk of data exfiltration and providing defense-in-depth for sensitive model and training data.

### Remediation
<a name="sagemaker-20-remediation"></a>

To enable network isolation for a SageMaker AI model explainability job definition, set `NetworkConfig.EnableNetworkIsolation` to `true` when creating the job definition. For more information about network isolation for SageMaker AI, see [Run training and inference containers in internet-free mode](https://docs.aws.amazon.com/sagemaker/latest/dg/mkt-algo-model-internet-free.html#mkt-algo-model-internet-free-isolation) in the *Amazon SageMaker AI Developer Guide*.

## [SageMaker.21] SageMaker notebook instances should be encrypted with customer managed AWS KMS keys
<a name="sagemaker-21"></a>

**Category:** Protect > Data protection > Encryption of data at rest

**Severity:** Medium

**Resource type:** `AWS::SageMaker::NotebookInstance`

**AWS Config rule:** [sagemaker-notebook-instance-storage-vol-kms-encrypted](https://docs.aws.amazon.com/config/latest/developerguide/sagemaker-notebook-instance-storage-vol-kms-encrypted.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether a SageMaker AI notebook instance is configured with an AWS KMS key for storage volume encryption. The control fails if a KMS key is not configured for the notebook instance.

Encryption of data at rest with a customer managed KMS key provides additional access control over the default AWS managed encryption. SageMaker AI notebook instances store user notebooks, datasets, model artifacts, and temporary processing data on ML storage volumes. A customer managed key enables fine-grained key policy control, CloudTrail audit logging of key usage, and compliance with frameworks requiring customer-controlled encryption.

### Remediation
<a name="sagemaker-21-remediation"></a>

To configure a KMS key for a SageMaker AI notebook instance, see [Notebook instances, SageMaker AI jobs, and Endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/encryption-at-rest-nbi.html) in the *Amazon SageMaker AI Developer Guide*. Note that `KmsKeyId` can only be set at notebook instance creation time. To remediate, create a new notebook instance with the KMS key specified and migrate your data from the existing instance.

## [SageMaker.22] SageMaker monitoring schedules should have inter-container traffic encryption enabled
<a name="sagemaker-22"></a>

**Category:** Protect > Data protection > Encryption of data in transit

**Severity:** Medium

**Resource type:** `AWS::SageMaker::MonitoringSchedule`

**AWS Config rule:** [sagemaker-monitoring-schedule-traffic-encryption](https://docs.aws.amazon.com/config/latest/developerguide/sagemaker-monitoring-schedule-traffic-encryption.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon SageMaker AI monitoring schedule has encryption enabled for inter-container traffic. The control fails if the monitoring job definition does not have encryption enabled for inter-container traffic.

Inter-container traffic encryption ensures that data transmitted between containers during monitoring jobs is encrypted in transit. Without this encryption, sensitive data processed during model monitoring could be exposed to unauthorized access within the network. Enabling this setting helps meet compliance requirements for protecting data in transit.

### Remediation
<a name="sagemaker-22-remediation"></a>

For an existing SageMaker AI monitoring schedule, inter-container traffic encryption cannot be updated in place. To create a new SageMaker AI monitoring schedule with inter-container traffic encryption enabled, use [API](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateMonitoringSchedule.html) or [CLI](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/create-monitoring-schedule.html) or CloudFormation and set `EnableInterContainerTrafficEncryption` to `true` in the `NetworkConfig` of the `MonitoringJobDefinition`.

## [SageMaker.23] SageMaker inference experiments should have instance storage volume encrypted with customer managed AWS KMS keys
<a name="sagemaker-23"></a>

**Category:** Protect > Data protection > Encryption of data at rest

**Severity:** Medium

**Resource type:** `AWS::SageMaker::InferenceExperiment`

**AWS Config rule:** [sagemaker-inf-experiment-instance-storage-kms-encrypted](https://docs.aws.amazon.com/config/latest/developerguide/sagemaker-inf-experiment-instance-storage-kms-encrypted.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether a SageMaker AI inference experiment is configured with an AWS KMS key for instance storage volume encryption. The control fails if a KMS key is not specified for instance storage volume encryption.

Encrypting instance storage volumes with customer managed KMS keys provides centralized key management, audit logging, and key rotation control for model artifacts and temporary inference data stored on ML compute instances during shadow tests.

### Remediation
<a name="sagemaker-23-remediation"></a>

To configure a KMS key for a SageMaker AI inference experiment, specify the `KmsKey` parameter when calling `CreateInferenceExperiment`. The `KmsKey` can be a KMS key ID, ARN, alias, or alias ARN. The SageMaker AI execution role must have `kms:CreateGrant` permission on the key. For more information on specifying a customer managed AWS KMS key to SageMaker AI, see [Notebook instances, SageMaker AI jobs, and Endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/encryption-at-rest-nbi.html) in the *Amazon SageMaker AI Developer Guide*.

## [SageMaker.24] SageMaker inference experiments should have data storage encrypted with customer managed AWS KMS keys
<a name="sagemaker-24"></a>

**Category:** Protect > Data protection > Encryption of data at rest

**Severity:** Medium

**Resource type:** `AWS::SageMaker::InferenceExperiment`

**AWS Config rule:** [sagemaker-inf-experiment-data-storage-kms-encrypted](https://docs.aws.amazon.com/config/latest/developerguide/sagemaker-inf-experiment-data-storage-kms-encrypted.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether a SageMaker AI inference experiment with data capture enabled has a KMS key configured to encrypt captured data at rest. The control fails if the data storage configuration does not specify a KMS key for encryption.

Encrypting captured inference request and response data with customer managed KMS keys ensures that sensitive inference payloads stored in Amazon S3 are protected with centralized key management and audit capabilities.

### Remediation
<a name="sagemaker-24-remediation"></a>

To configure a KMS key for data storage in a SageMaker AI inference experiment, specify the `KmsKey` field within `DataStorageConfig` when calling `CreateInferenceExperiment`. The `KmsKey` encrypts captured inference request and response data at rest in the specified Amazon S3 bucket. For more information on specifying a customer managed AWS KMS key to SageMaker AI, see [Notebook instances, SageMaker AI jobs, and Endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/encryption-at-rest-nbi.html) in the *Amazon SageMaker AI Developer Guide*.

## [SageMaker.25] SageMaker model quality job definitions should have network isolation enabled
<a name="sagemaker-25"></a>

**Category:** Protect > Secure network configuration > Resources not publicly accessible

**Severity:** High

**Resource type:** `AWS::SageMaker::ModelQualityJobDefinition`

**AWS Config rule:** [sagemaker-model-quality-job-definition-isolation](https://docs.aws.amazon.com/config/latest/developerguide/sagemaker-model-quality-job-definition-isolation.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon SageMaker AI model quality job definition has network isolation enabled. The control fails if the model quality job definition does not have network isolation enabled.

Network isolation reduces the attack surface and prevents external access, thereby protecting against unauthorized external access, accidental data exposure, and potential data exfiltration.

### Remediation
<a name="sagemaker-25-remediation"></a>

When you create a model quality job definition, you can enable network isolation by setting the value for the `EnableNetworkIsolation` parameter to `True`. For more information about network isolation for SageMaker AI, see [Run training and inference containers in internet-free mode](https://docs.aws.amazon.com/sagemaker/latest/dg/mkt-algo-model-internet-free.html#mkt-algo-model-internet-free-isolation) in the *Amazon SageMaker AI Developer Guide*.