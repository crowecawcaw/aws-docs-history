# Storage Gateway AL2 to AL2023 Migration Campaign

We transitioned the Storage Gateway appliance operating system (OS) from Amazon Linux 2 to AL2023 to enable new hybrid cloud storage features and maintain optimal performance and security standards. This transition impacted all AL2-based Storage Gateway appliance versions S3 File Gateway Version 1.x, Tape Gateway Version 2.x, and Volume Gateway Version 2.x. We discontinued support for these systems on June 30, 2026. If you have not yet migrated, we recommend that you do so as soon as possible.

You can identify whether your gateways need migration through multiple methods. The AWS Console displays a deprecation message in the gateway's **Details** tab for affected gateways. Additionally, the [`DescribeGatewayInformation`](../../../storagegateway/latest/APIReference/API_DescribeGatewayInformation.md "../../../storagegateway/latest/APIReference/API_DescribeGatewayInformation.md") API provides programmatic access to check the deprecation date field. The AWS Health Dashboard lists impacted gateways under the **Affected resources** tab. Note that this list reflects gateways that were deprecated at the time of notification and is not updated as gateways are migrated. To confirm whether your gateway has been successfully migrated, check the gateway details page in the Storage Gateway Console. The migration process itself is designed with data safety as the priority, storing a copy of on-premises gateway VM data in AWS before migration begins to enable easy recovery if needed.

AWS provides comprehensive migration guides specific to each gateway type. After completing migration, you should verify success by checking that deprecation warnings no longer appear in the AWS Console's gateway **Details** tab, or by using the [`DescribeGatewayInformation`](../../../storagegateway/latest/APIReference/API_DescribeGatewayInformation.md "../../../storagegateway/latest/APIReference/API_DescribeGatewayInformation.md") API to confirm the deprecation date field is absent. Critically, you must not revert to your AL2 gateway after successfully migrating to AL2023, as reverting may cause operational issues.

If you have not yet migrated, we continue to send notifications through email and the **Event log** tab in the AWS Health Dashboard. If you encounter issues during migration, contact [AWS Support](https://console.aws.amazon.com/support/home "https://console.aws.amazon.com/support/home") for assistance and troubleshooting guidance.

## Quick Links and Resources

### Gateway Version Migration Reference

Understanding which gateways require migration is straightforward based on the gateway software version number. Gateways based on Amazon Linux 2 OS are no longer supported as of June 30, 2026. You must migrate these gateways.

| Gateway Type    | AL2 Version (Requires Migration) | AL2023 Version (Target) |
| --------------- | -------------------------------- | ----------------------- |
| S3 File Gateway | Version 1.x                      | Version 2.x             |
| Tape Gateway    | Version 2.x                      | Version 3.x             |
| Volume Gateway  | Version 2.x                      | Version 3.x             |

### Migration Timeline

The migration timeline includes several critical milestones:

- **October 28, 2025:** All new gateway deployments initiated from Storage Gateway console will default to AL2023 images.
- **January 5, 2026:** AWS will begin restricting new AL2 gateway activations.
- **June 30, 2026:** AL2-based gateways stopped receiving software updates and AWS support ended. AL2-based appliances no longer receive software updates, security patches, or bug fixes. You are now solely responsible for maintaining these systems.

### Pre-migration Checklist

###### Important

Before beginning the migration process, verify the following requirements to ensure a successful migration.

- **Use the latest gateway image.** When creating the new Storage Gateway VM:

  - For Amazon EC2 gateways, use the latest AMI from the public SSM parameter or use the Storage Gateway console.
  - For on-premises gateways, download the latest VM image from the Storage Gateway console.

- **Match the hardware configuration.** Ensure the new gateway VM uses the same CPU, memory, and network throughput as the existing gateway. For EC2 gateways, use the same instance type.
- **Verify root disk sizing.** The new gateway VM's root disk must be at least the same size as the existing gateway's root disk. If the existing root disk has less than 20 GB of available space, size the new root disk to: (existing root disk size) + (20 GB minus available space on existing root disk).
- **Apply pending software updates.** Before starting migration, apply any pending software updates on the existing gateway. Open the **Storage Gateway** console, select your gateway, and choose **Update Now** if available.
- **Verify network connectivity from the new gateway.** Before initiating migration, confirm that the new gateway VM can reach:

  - Storage Gateway service endpoints (or your VPC endpoints).
  - Amazon S3 endpoints.
  - Active Directory / DNS servers (if your gateway is domain-joined).
  - Use the gateway local console's network connectivity test to validate all endpoints pass.

- **Resolve failing file uploads.** Ensure your gateway's `FilesFailingUpload` CloudWatch metric is zero before beginning migration. Files in a failing state indicate unresolved errors that should be addressed first. To identify affected files, [create a cache report](create-cache-report.md "create-cache-report.md"), then resolve the underlying issues before proceeding.
- **Wait for cache to sync.** Verify that the `CachePercentDirty` metric on the gateway's Monitoring tab is 0. This confirms all cached data has been uploaded to S3.

### Migration Guides

- [S3 File Gateway Migration Guide](migrate-data.md "migrate-data.md")
- [Tape Gateway Migration Guide](../../../storagegateway/latest/tgw/migrate-data.md "../../../storagegateway/latest/tgw/migrate-data.md")
- [Volume Gateway Migration Guide](../../../storagegateway/latest/vgw/migrate-data.md "../../../storagegateway/latest/vgw/migrate-data.md")

### Support and Monitoring

- [Storage Gateway Console](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/")
- [AWS Personal Health Dashboard](https://phd.aws.amazon.com/ "https://phd.aws.amazon.com/")
- [Contact AWS Support](https://console.aws.amazon.com/support/home "https://console.aws.amazon.com/support/home")

### Frequently Asked Questions

**What happens to my data during migration?**

Your data remains durably stored in AWS throughout the migration process. The migration procedure includes storing a copy of your on-premises gateway VM data in AWS for easy recovery if needed.

**Will there be downtime during migration?**

Migration timing and any potential service interruption depend on your gateway type and configuration. Review the gateway-specific migration guide for your deployment for detailed information.

**What happens if I don't migrate by June 30, 2026?**

Your gateway will continue to operate, and data will remain safely stored in AWS. However, as of June 30, 2026, AL2-based gateways no longer receive software updates, security patches, or AWS support. We strongly recommend migrating as soon as possible.

**Can I continue to use my AL2 based gateway after migrating?**

No, you should not use your AL2 gateway alongside your new AL2023 gateway after successfully migrating. Use only your new AL2023-based gateway going forward. Using both AL2 and AL2023 gateways simultaneously may cause operational issues.

**I'm having issues during migration. What should I do?**

Contact [AWS Support](https://console.aws.amazon.com/support/home "https://console.aws.amazon.com/support/home") for assistance. Our support team can help troubleshoot migration issues and guide you through the process.
