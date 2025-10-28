# Controls implemented with resource control policies

(RCPs)

This section provides information about AWS Control Tower controls that are implemented by resource
control policies (RCPs). RCPs are a type of policy, which can enforce
preventive controls on resources in your AWS Control Tower landing zone.

###### RCPs complement service control policies (SCPs)

- SCPs offer control over the maximum permissions for IAM roles and users in your
  landing zone.
- RCPs offer control over the maximum permissions on AWS resources in your
  landing zone.
  RCPs are similar to SCPs, because they each contain explicit and implicit
  _allow_ and _deny_ capabilities, expressed in
  their policies. For more information, see the [AWS Organizations
  documentation about RCPs](../../../organizations/latest/userguide/orgs_manage_policies_rcps.md "../../../organizations/latest/userguide/orgs_manage_policies_rcps.md").

Individual RCP controls apply to specific resources associated with the following AWS
services:

- Amazon S3
- AWS Security Token Service (STS)
- AWS Key Management Service KMS)
- Amazon Simple Queue Service (SQS)
- AWS Secrets Manager
  RCP-based controls are configurable. For more information, see [Controls
  with parameters](control-parameter-concepts.md "control-parameter-concepts.md").

**When to apply RCP controls**

With RCP controls, you can establish a [_data
perimeter_](https://aws.amazon.com/identity/data-perimeters-on-aws/ "https://aws.amazon.com/identity/data-perimeters-on-aws/") for your
landing zone.

- For example, you can limit access to resources so that only the principals in your
  organization can manage them, such as with control **[CT.S3.PV.4] Require
  that the organization's Amazon S3 resources are accessible only by IAM principals
  that belong to the organization or by an AWS service**.
- Similarly, you can restrict access to resources so that certain requirements must
  be met, such as with **[CT.S3.PV.3] Require requests to Amazon S3 resources to
  use a minimum TLS version of 1.3**.
