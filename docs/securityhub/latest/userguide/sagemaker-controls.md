# Security Hub CSPM controls for SageMaker AI

These AWS Security Hub CSPM controls evaluate the Amazon SageMaker AI service and resources. The controls might
not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [SageMaker.1] Amazon SageMaker notebook instances should not have

direct internet access

**Related requirements:** NIST.800-53.r5 AC-21, NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-4, NIST.800-53.r5 AC-4(21), NIST.800-53.r5 AC-6, NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(11), NIST.800-53.r5 SC-7(16), NIST.800-53.r5 SC-7(20), NIST.800-53.r5 SC-7(21), NIST.800-53.r5 SC-7(3), NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-7(9), PCI DSS v3.2.1/1.2.1, PCI DSS v3.2.1/1.3.1, PCI DSS v3.2.1/1.3.2, PCI DSS v3.2.1/1.3.4, PCI DSS v3.2.1/1.3.6, PCI DSS v4.0.1/1.4.4

**Category:** Protect > Secure network configuration

**Severity:** High

**Resource type:**
`AWS::SageMaker::NotebookInstance`

**AWS Config rule:**
[sagemaker-notebook-no-direct-internet-access](../../../config/latest/developerguide/sagemaker-notebook-no-direct-internet-access.md "../../../config/latest/developerguide/sagemaker-notebook-no-direct-internet-access.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether direct internet access is disabled for an SageMaker AI notebook
instance. The control fails if the `DirectInternetAccess` field is enabled
for the notebook instance.

If you configure your SageMaker AI instance without a VPC, then by default direct internet access
is enabled on your instance. You should configure your instance with a VPC and change the
default setting to **Disable—Access the internet through a VPC**. To
train or host models from a notebook, you need internet access. To enable internet
access, your VPC must have either an interface endpoint (AWS PrivateLink) or
a NAT gateway and a security group that allows outbound
connections. To learn more about how to connect a notebook instance to resources in a VPC, see
[Connect a notebook
instance to resources in a VPC](../../../sagemaker/latest/dg/appendix-notebook-and-internet-access.md "../../../sagemaker/latest/dg/appendix-notebook-and-internet-access.md") in the _Amazon SageMaker AI Developer Guide_. You should also ensure that access to your SageMaker AI configuration is limited to only authorized
users. Restrict IAM permissions that permit users to change SageMaker AI settings and resources.

### Remediation

You can't change the internet access setting after creating a notebook instance. Instead, you can stop, delete, and recreate the instance with
blocked internet access. To delete a notebook instance that permits direct internet access, see [Use notebook instances to build models: Clean up](../../../sagemaker/latest/dg/ex1-cleanup.md "../../../sagemaker/latest/dg/ex1-cleanup.md") in the _Amazon SageMaker AI Developer Guide_.
To recreate a notebook instance that denies internet access, see [Create a notebook instance](../../../sagemaker/latest/dg/howitworks-create-ws.md "../../../sagemaker/latest/dg/howitworks-create-ws.md"). For **Network, Direct internet access**,
choose **Disable—Access the internet through a VPC**.

## [SageMaker.2] SageMaker notebook instances should be launched in a

custom VPC

**Related requirements:** NIST.800-53.r5 AC-21, NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-4, NIST.800-53.r5 AC-4(21), NIST.800-53.r5 AC-6, NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(11), NIST.800-53.r5 SC-7(16), NIST.800-53.r5 SC-7(20), NIST.800-53.r5 SC-7(21), NIST.800-53.r5 SC-7(3), NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-7(9)

**Category:** Protect > Secure network configuration > Resources within VPC

**Severity:** High

**Resource type:**
`AWS::SageMaker::NotebookInstance`

**AWS Config rule:**
[sagemaker-notebook-instance-inside-vpc](../../../config/latest/developerguide/sagemaker-notebook-instance-inside-vpc.md "../../../config/latest/developerguide/sagemaker-notebook-instance-inside-vpc.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks if an Amazon SageMaker AI notebook instance is launched within a custom virtual
private cloud (VPC). This control fails if a SageMaker AI notebook instance is not launched within a custom VPC or if it is launched in the SageMaker AI service VPC.

Subnets are a range of IP addresses within a VPC. We recommend keeping your resources inside a
custom VPC whenever possible to ensure secure network protection of your infrastructure. An Amazon VPC is a virtual network
dedicated to your AWS account. With an Amazon VPC, you can control the network access and internet connectivity of your
SageMaker AI Studio and notebook instances.

### Remediation

You can't change the VPC setting after creating a notebook instance. Instead, you can stop, delete, and recreate the instance.
For instructions, see [Use notebook instances to build models: Clean up](../../../sagemaker/latest/dg/ex1-cleanup.md "../../../sagemaker/latest/dg/ex1-cleanup.md") in the _Amazon SageMaker AI Developer Guide_.

## [SageMaker.3] Users should not have root access to SageMaker notebook

instances

**Related requirements:** NIST.800-53.r5 AC-2(1), NIST.800-53.r5 AC-3(15), NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-6, NIST.800-53.r5 AC-6(10), NIST.800-53.r5 AC-6(2)

**Category:** Protect > Secure access management > Root user access restrictions

**Severity:** High

**Resource type:**
`AWS::SageMaker::NotebookInstance`

**AWS Config rule:**
[sagemaker-notebook-instance-root-access-check](../../../config/latest/developerguide/sagemaker-notebook-instance-root-access-check.md "../../../config/latest/developerguide/sagemaker-notebook-instance-root-access-check.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether root access is turned on for an Amazon SageMaker AI notebook instance.
The control fails if root access is turned on for a SageMaker AI notebook instance.

In adherence to the principal of least privilege, it is a recommended security best practice
to restrict root access to instance resources to avoid unintentionally over provisioning permissions.

### Remediation

To restrict root access to SageMaker AI notebook instances, see [Control root access to a SageMaker AI notebook instance](../../../sagemaker/latest/dg/nbi-root-access.md "../../../sagemaker/latest/dg/nbi-root-access.md") in the _Amazon SageMaker AI Developer Guide_.

## [SageMaker.4] SageMaker endpoint production variants should have an

initial instance count greater than 1

**Related requirements:** NIST.800-53.r5 CP-10, NIST.800-53.r5 SC-5, NIST.800-53.r5 SC-36,
NIST.800-53.r5 SA-13

**Category:** Recover > Resilience > High availability

**Severity:** Medium

**Resource type:**
`AWS::SageMaker::EndpointConfig`

**AWS Config rule:**
[sagemaker-endpoint-config-prod-instance-count](../../../config/latest/developerguide/sagemaker-endpoint-config-prod-instance-count.md "../../../config/latest/developerguide/sagemaker-endpoint-config-prod-instance-count.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether production variants of an Amazon SageMaker AI endpoint have an initial instance count greater
than 1. The control fails if the endpoint's production variants have only 1 initial instance.

Production variants running with an instance count greater than 1 permit multi-AZ instance redundancy managed by
SageMaker AI. Deploying resources across multiple Availability Zones is an AWS best practice to provide high availability within your
architecture. High availability helps you to recover from security incidents.

###### Note

This control applies only to instance-based endpoint configuration.

### Remediation

For more information about the parameters of endpoint configuration, see [Create an endpoint configuration](../../../sagemaker/latest/dg/serverless-endpoints-create.md#serverless-endpoints-create-config "../../../sagemaker/latest/dg/serverless-endpoints-create.md#serverless-endpoints-create-config") in the _Amazon SageMaker AI Developer Guide_.

## [SageMaker.5] SageMaker models should have network isolation enabled

**Category:** Protect > Secure network configuration > Resources not publicly accessible

**Severity:** Medium

**Resource type:**
`AWS::SageMaker::Model`

**AWS Config rule:**
[sagemaker-model-isolation-enabled](../../../config/latest/developerguide/sagemaker-model-isolation-enabled.md "../../../config/latest/developerguide/sagemaker-model-isolation-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon SageMaker AI hosted model has network isolation enabled.
The control fails if the `EnableNetworkIsolation` parameter for the hosted
model is set to `False`.

SageMaker AI training and deployed inference containers are internet-enabled by default. If
you don't want SageMaker AI to provide external network access to your training or inference
containers, you can enable network isolation. If you enable network isolation, no
inbound or outbound network calls can be made to or from the model container, including
calls to or from other AWS services. Additionally, no AWS credentials are made
available to the container runtime environment. Enabling network isolation helps prevent
unintended access to your SageMaker AI resources from the internet.

###### Note

On August 13, 2025, Security Hub CSPM changed the title and description of this control. The
new title and description more accurately reflect that the control checks the
setting for the `EnableNetworkIsolation` parameter of Amazon SageMaker AI hosted
models. Previously, the title of this control was: _SageMaker models should block inbound
traffic_.

### Remediation

For more information about network isolation for SageMaker AI models, see [Run training and inference containers in internet-free mode](../../../sagemaker/latest/dg/mkt-algo-model-internet-free.md "../../../sagemaker/latest/dg/mkt-algo-model-internet-free.md") in the
_Amazon SageMaker AI Developer Guide_. When you create a model, you can enable
network isolation by setting the value for the `EnableNetworkIsolation`
parameter to `True`.

## [SageMaker.6] SageMaker app image configurations should be

tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::SageMaker::AppImageConfig`

**AWS Config rule:** [sagemaker-app-image-config-tagged](../../../config/latest/developerguide/sagemaker-app-image-config-tagged.md "../../../config/latest/developerguide/sagemaker-app-image-config-tagged.md")

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                                | Type                            | Allowed custom values                                                                                                                                                         | Security Hub CSPM default value |
| ----------------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| `requiredKeyTags` | A list of non-system tag keys that must be assigned to an evaluated resource. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | No default value                |

This control checks whether an Amazon SageMaker AI app image configuration
(`AppImageConfig`) has the tag keys specified by the
`requiredKeyTags` parameter. The control fails if the app image
configuration doesn't have any tag keys, or it doesn't have all the keys specified by
the `requiredKeyTags` parameter. If you don't specify any values for
the `requiredKeyTags` parameter, the control checks only for the
existence of a tag key and fails if the app image configuration doesn't have any tag
keys. The control ignores system tags, which are applied automatically and have the
`aws:` prefix.

A tag is a label that you create and assign to an AWS resource. Each tag consists of
a required tag key and an optional tag value. You can use tags to categorize resources
by purpose, owner, environment, or other criteria. They can help you identify, organize,
search for, and filter resources. They can also help you track resource owners for
actions and notifications. You can also use tags to implement attribute-based access
control (ABAC) as an authorization strategy. For more information about ABAC strategies,
see [Define
permissions based on attributes with ABAC authorization](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_. For more information about tags, see the
[Tagging AWS Resources and Tag Editor User
Guide](../../../tag-editor/latest/userguide/tagging.md "../../../tag-editor/latest/userguide/tagging.md").

###### Note

Do not store personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are
accessible from many AWS services. They aren't intended to be used for private or sensitive data.

### Remediation

To add tags to an Amazon SageMaker AI app image configuration (`AppImageConfig`),
you can use the [AddTags](../../../sagemaker/latest/APIReference/API_AddTags.md "../../../sagemaker/latest/APIReference/API_AddTags.md") operation
of the SageMaker AI API or, if you're using the AWS CLI, run the [add-tags](../../../cli/latest/reference/sagemaker/add-tags.md "../../../cli/latest/reference/sagemaker/add-tags.md")
command.

## [SageMaker.7] SageMaker images should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::SageMaker::Image`

**AWS Config rule:** [sagemaker-image-tagged](../../../config/latest/developerguide/sagemaker-image-tagged.md "../../../config/latest/developerguide/sagemaker-image-tagged.md")

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                                | Type                            | Allowed custom values                                                                                                                                                         | Security Hub CSPM default value |
| ----------------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| `requiredKeyTags` | A list of non-system tag keys that must be assigned to an evaluated resource. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | No default value                |

This control checks whether an Amazon SageMaker AI image has the tag keys specified by the
`requiredKeyTags` parameter. The control fails if the image
doesn't have any tag keys, or it doesn't have all the keys specified by the
`requiredKeyTags` parameter. If you don't specify any values for
the `requiredKeyTags` parameter, the control checks only for the
existence of a tag key and fails if the image doesn't have any tag keys. The control
ignores system tags, which are applied automatically and have the `aws:`
prefix.

A tag is a label that you create and assign to an AWS resource. Each tag consists of
a required tag key and an optional tag value. You can use tags to categorize resources
by purpose, owner, environment, or other criteria. They can help you identify, organize,
search for, and filter resources. They can also help you track resource owners for
actions and notifications. You can also use tags to implement attribute-based access
control (ABAC) as an authorization strategy. For more information about ABAC strategies,
see [Define
permissions based on attributes with ABAC authorization](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_. For more information about tags, see the
[Tagging AWS Resources and Tag Editor User
Guide](../../../tag-editor/latest/userguide/tagging.md "../../../tag-editor/latest/userguide/tagging.md").

###### Note

Do not store personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are
accessible from many AWS services. They aren't intended to be used for private or sensitive data.

### Remediation

To add tags to an Amazon SageMaker AI image, you can use the [AddTags](../../../sagemaker/latest/APIReference/API_AddTags.md "../../../sagemaker/latest/APIReference/API_AddTags.md") operation
of the SageMaker AI API or, if you're using the AWS CLI, run the [add-tags](../../../cli/latest/reference/sagemaker/add-tags.md "../../../cli/latest/reference/sagemaker/add-tags.md")
command.

## [SageMaker.8] SageMaker notebook instances should run on supported platforms

**Category:** Detect > Vulnerability, patch, and version
management

**Severity:** Medium

**Resource type:**
`AWS::SageMaker::NotebookInstance`

**AWS Config rule:** [sagemaker-notebook-instance-platform-version](../../../config/latest/developerguide/sagemaker-notebook-instance-platform-version.md "../../../config/latest/developerguide/sagemaker-notebook-instance-platform-version.md")

**Schedule type:** Periodic

**Parameters:**

- `supportedPlatformIdentifierVersions`: `notebook-al2-v3`
  (not customizable)

This control checks whether an Amazon SageMaker AI notebook instance is configured to run on a
supported platform, based on the platform identifier specified for the notebook
instance. The control fails if the notebook instance is configured to run on a platform
that's no longer supported.

If the platform for an Amazon SageMaker AI notebook instance is no longer supported, it might not
receive security patches, bug fixes, or other types of updates. Notebook instances might
continue to function, but they won't receive SageMaker AI security updates or critical bug
fixes. You assume the risks associated with using an unsupported platform. For more
information, see [JupyterLab
versioning](../../../sagemaker/latest/dg/nbi-jl.md "../../../sagemaker/latest/dg/nbi-jl.md") in the _Amazon SageMaker AI Developer
Guide_.

### Remediation

For information about the platforms that Amazon SageMaker AI currently supports and how to
migrate to them, see [Amazon Linux 2 notebook
instances](../../../sagemaker/latest/dg/nbi-al2.md "../../../sagemaker/latest/dg/nbi-al2.md") in the _Amazon SageMaker AI Developer
Guide_.
