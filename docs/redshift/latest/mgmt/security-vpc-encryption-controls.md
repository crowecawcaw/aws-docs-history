Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# VPC encryption controls with Amazon Redshift

Amazon Redshift supports [VPC encryption controls](../../../vpc/latest/userguide/vpc-encryption-controls.md "../../../vpc/latest/userguide/vpc-encryption-controls.md"), a security feature that helps you enforce encryption in transit for all traffic within and across VPCs in a Region.
This document describes how to use VPC encryption controls with Amazon Redshift clusters and serverless workgroups.

VPC encryption controls provide centralized control to monitor and enforce encryption in transit within your VPCs. When enabled in enforce mode,
it ensures that all network traffic is encrypted either at the hardware layer (using AWS Nitro System) or at the application layer (using TLS/SSL).

Amazon Redshift integrates with VPC encryption controls to help you meet compliance requirements for industries such as healthcare (HIPAA), government (FedRAMP), and finance (PCI DSS).

## How VPC encryption controls work with Amazon Redshift

VPC encryption controls operate in two modes:

- Monitor Mode: Provides visibility into the encryption status of traffic flows and helps identify resources that allow unencrypted traffic.
- Enforce Mode: Prevents the creation or use of resources that allow unencrypted traffic within the VPC. All traffic must be encrypted either at the hardware layer (Nitro-based instances) or application layer (TLS/SSL).

## Requirements for using VPC encryption controls

**Instance type requirements**

Amazon Redshift requires Nitro-based instances to support VPC encryption controls. All modern Redshift instance types support the necessary encryption capabilities.

**SSL/TLS requirements**

When VPC encryption controls is enabled in enforce mode, the require_ssl parameter must be set to true and cannot be disabled. This ensures that all client connections use encrypted TLS connections.

## Migrating to VPC ecncryption controls

**For existing clusters and workgroups**

You cannot enable VPC encryption controls in enforce mode on a VPC that contains existing Redshift clusters or serverless workgroups. See the following steps to use
encryption controls if you have an existing cluster or workgroup:

1. Create a snapshot of your existing cluster or namespace
2. Create a new VPC with VPC encryption controls enabled in enforce mode
3. Restore from the snapshot into the new VPC using one of these operations:
   - For provisioned clusters: Use the `restore-from-cluster-snapshot` operation
   - For serverless: Use the `restore-from-snapshot` operation on your workgroup

**When creating new clusters or workgroups in a VPC with encryption controls enabled, the require_ssl parameter must be set to true.**

Amazon Redshift requires Nitro-based instances to support VPC encryption controls. All modern Redshift instance types support the necessary encryption capabilities.

**SSL/TLS requirements**

When VPC encryption controls is enabled in enforce mode, the require_ssl parameter must be set to true and cannot be disabled. This ensures that all client connections use encrypted TLS connections.

## Considerations and limitations

When using VPC encryption controls in Amazon Redshift, consider the following:

**VPC State Restrictions**

- Cluster and workgroup creation is blocked when VPC encryption controls is in `enforce-in-progress` state
- You must wait until the VPC reaches `enforce` mode before creating new resources

**SSL configuration**

- require_ssl parameter: Must always be `true` for clusters and workgroups created in encryption-enforced VPCs
- Once a cluster or workgroup is created in an encryption-enforced VPC, `require_ssl` cannot be disabled for its lifetime

**Region availability**

This feature is not available in enforce mode with Amazon Redshift Serverless in the following Regions:

- South America (São Paulo)
- Europe (Zurich)
