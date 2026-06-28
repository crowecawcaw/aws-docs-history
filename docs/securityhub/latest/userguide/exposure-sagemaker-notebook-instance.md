# Remediating exposures for Amazon SageMaker notebook instances

AWS Security Hub can generate exposure findings for Amazon SageMaker notebook instances.

On the Security Hub console, the notebook instance involved in an exposure finding and its identifying information are listed in
the **Resources** section of the finding details. Programmatically, you can retrieve resource
details with the [GetFindingsV2](../../1.0/APIReference/API_GetFindingsV2.md "../../1.0/APIReference/API_GetFindingsV2.md") operation of the Security Hub CSPM API.

After identifying the resource involved in an exposure finding, you can delete the resource if you don't need it.
Deleting a nonessential resource can reduce your exposure profile and AWS costs. If the resource is essential,
follow these recommended remediation steps to help mitigate the risk. The remediation topics are
divided based on the type of trait.

A single exposure finding contains issues identified in multiple remediation topics. Conversely, you can address an exposure finding and bring down
its severity level by addressing just one remediation topic. Your approach to risk remediation
depends on your organizational requirements and workloads.

###### Note

The remediation guidance provided in this topic might require additional consultation in other AWS resources.

###### Contents

- [Misconfiguration traits for Amazon SageMaker notebook instances](exposure-sagemaker-notebook-instance.md#sagemaker-misconfiguration "exposure-sagemaker-notebook-instance.md#sagemaker-misconfiguration")

  - [The Amazon SageMaker notebook instance has direct internet access enabled](exposure-sagemaker-notebook-instance.md#outbound-internet-enabled "exposure-sagemaker-notebook-instance.md#outbound-internet-enabled")
  - [The Amazon SageMaker notebook instance has root access enabled](exposure-sagemaker-notebook-instance.md#notebook-root-access-enabled "exposure-sagemaker-notebook-instance.md#notebook-root-access-enabled")
  - [The role associated with the Amazon SageMaker notebook instance has an administrative access policy](exposure-sagemaker-notebook-instance.md#administrative-access-policy "exposure-sagemaker-notebook-instance.md#administrative-access-policy")
  - [The role associated with the Amazon SageMaker notebook instance has a service-level administrative access policy](exposure-sagemaker-notebook-instance.md#service-admin-policy "exposure-sagemaker-notebook-instance.md#service-admin-policy")

## Misconfiguration traits for Amazon SageMaker notebook instances

Here are misconfiguration traits for Amazon SageMaker notebook instances and suggested remediation steps.

### The Amazon SageMaker notebook instance has direct internet access enabled

When `DirectInternetAccess` is enabled on an Amazon SageMaker notebook instance, outbound traffic is routed through a SageMaker-managed network address translation (NAT) gateway to the internet.
This provides an egress path that can be used for data exfiltration or as a command-and-control channel if the notebook is compromised.
Following security best practices, AWS recommends disabling direct internet access and placing notebook instances in a VPC with VPC endpoints for required AWS services.

###### Disable direct internet access

The `DirectInternetAccess` setting cannot be changed after a notebook instance is created. To disable it, create a new notebook instance with `DirectInternetAccess` set to `Disabled` in a private subnet within a VPC, then migrate your notebooks and data from the existing instance.
For instructions, see [Connect a notebook instance in a VPC to external resources](../../../sagemaker/latest/dg/appendix-notebook-and-internet-access.md "../../../sagemaker/latest/dg/appendix-notebook-and-internet-access.md") in the _Amazon SageMaker Developer Guide_.

###### Configure VPC endpoints

When direct internet access is disabled, the notebook instance requires VPC endpoints to access AWS services such as Amazon S3 and the Amazon SageMaker API.
Create interface VPC endpoints for the services your notebook needs.
For information on VPC endpoints, see [What is AWS PrivateLink?](../../../vpc/latest/privatelink/what-is-privatelink.md "../../../vpc/latest/privatelink/what-is-privatelink.md") in the _AWS PrivateLink Guide_.

### The Amazon SageMaker notebook instance has root access enabled

When `RootAccess` is enabled on an Amazon SageMaker notebook instance, users have full OS-level root privileges.
Root access allows arbitrary system modifications, persistent backdoors, and unrestricted package installation.
Following security best practices, AWS recommends disabling root access for notebook instances unless it is explicitly required for your workflow.

###### Disable root access

You cannot change the `RootAccess` setting on a running notebook instance. To disable it, stop the instance, then update the instance configuration to set `RootAccess` to `Disabled`.
Most notebook workflows, including installing packages with `pip` and running lifecycle configurations, continue to work without root access.
For instructions, see [Control root access to a Amazon SageMaker notebook instance](../../../sagemaker/latest/dg/nbi-root-access.md "../../../sagemaker/latest/dg/nbi-root-access.md") in the _Amazon SageMaker Developer Guide_.

###### Additional considerations

If root access is required for specific tasks, consider using Amazon SageMaker Studio notebooks instead, which provide isolated container-based environments with more granular access controls.
You can also use lifecycle configurations to pre-install required packages at instance creation time, reducing the need for root access during normal use.

### The role associated with the Amazon SageMaker notebook instance has an administrative access policy

The execution role attached to the notebook instance has a policy that grants administrative access to your AWS account.
If the notebook is compromised, an attacker can leverage the role credentials to access and modify any resource in the account.
Following security best practices, AWS recommends applying the principle of least privilege to notebook execution roles.

###### Scope down the execution role

Review the IAM policies attached to the notebook's execution role. Remove `AdministratorAccess` or overly broad policies and replace them with policies that grant only the permissions required for your notebook's workflows.
For guidance on creating scoped Amazon SageMaker roles, see [Amazon SageMaker roles](../../../sagemaker/latest/dg/sagemaker-roles.md "../../../sagemaker/latest/dg/sagemaker-roles.md") in the _Amazon SageMaker Developer Guide_.

### The role associated with the Amazon SageMaker notebook instance has a service-level administrative access policy

The execution role attached to the notebook instance has a policy that grants full access to one or more AWS services (for example, `s3:*` or `ec2:*`).
If the notebook is compromised, an attacker can leverage the role credentials to access or modify resources within those services.
Following security best practices, AWS recommends scoping service permissions to only the specific actions and resources required.

###### Restrict service-level permissions

Review the IAM policies attached to the notebook's execution role. Replace wildcard service actions (such as `s3:*`) with specific actions required for your workflow (such as `s3:GetObject` and `s3:PutObject` on specific bucket ARNs).
For guidance on creating scoped policies, see [Creating IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the _IAM User Guide_.
