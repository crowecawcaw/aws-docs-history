

# Document history for the AWS RTB Fabric User Guide
<a name="doc-history"></a>

The following table describes the documentation releases for RTB Fabric.

| Change | Description | Date | 
| --- |--- |--- |
| [[Health checks for managed endpoints](health-checks-for-managed-endpoints.html) - New feature](#doc-history) | You can now configure application-level health checks for Auto Scaling group managed endpoints on responder gateways. When enabled, RTB Fabric probes each Amazon EC2 instance and routes traffic only to healthy instances. For information, see [Health checks for managed endpoints](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/health-checks-for-managed-endpoints.html). | March 27, 2026 | 
| [[RTB Fabric updates to AWS managed policies](security-iam-awsmanpol.html#security-iam-awsmanpol-updates) - Policy updated](#doc-history) | RTB Fabric updated the `RTBFabricServiceRolePolicy` managed policy to change the CloudWatch namespace from `rtbfabric` to `AWS/RTBFabric` for publishing custom metrics. For information, see [RTB Fabric updates to AWS managed policies](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-updates). | October 22, 2025 | 
| [[RTB Fabric updates to AWS managed policies](security-iam-awsmanpol.html#security-iam-awsmanpol-updates) - New policy](#doc-history) | RTB Fabric has released a new managed policy `RTBFabricServiceRolePolicy` that allows RTB Fabric to manage network interfaces and publish CloudWatch metrics on your behalf. For information, see [RTB Fabric updates to AWS managed policies](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-updates). | October 22, 2025 | 
| [Initial release](#doc-history) | Initial release of the RTB Fabric User Guide | October 22, 2025 | 