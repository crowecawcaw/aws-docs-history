# Storage Gateway AL2 to AL2023 Migration Campaign

AWS is transitioning Storage Gateway appliance operating system (OS) from Amazon Linux 2 to AL2023 to enable new hybrid cloud storage features and maintain optimal performance and security standards. This transition will impact all AL2-based Storage Gateway appliance versions S3 File Gateway Version 1.x, Tape Gateway Version 2.x, and Volume Gateway Version 2.x. You are required to complete the migration before June 30, 2026, as AWS will discontinue supporting these systems thereafter.

You can identify whether your gateways need migration through multiple methods. The AWS Console displays a deprecation message in the gateway's **Details** tab for affected gateways. Additionally, the [`DescribeGatewayInformation`](../APIReference/API_DescribeGatewayInformation.md "../APIReference/API_DescribeGatewayInformation.md") API provides programmatic access to check the deprecation date field. The AWS Health Dashboard lists impacted gateways under the **Affected resources** tab. However, the list is not updated immediately after a gateway is migrated. The migration process itself is designed with data safety as the priority, storing a copy of on-premises gateway VM data in AWS before migration begins to enable easy recovery if needed.

AWS provides comprehensive migration guides specific to each gateway type. After completing migration, you should verify success by checking that deprecation warnings no longer appear in the AWS Console's gateway **Details** tab, or by using the [`DescribeGatewayInformation`](../APIReference/API_DescribeGatewayInformation.md "../APIReference/API_DescribeGatewayInformation.md") API to confirm the deprecation date field is absent. Critically, you must not revert to your AL2 gateway after successfully migrating to AL2023, as reverting may cause operational issues.

Throughout the migration period, AWS will send monthly reminder notifications via email, and the AWS Health Dashboard's **Scheduled changes** tab to help you plan and complete your migrations. If you encounter issues during migration, contact [AWS Support](https://console.aws.amazon.com/support/home "https://console.aws.amazon.com/support/home") for assistance and troubleshooting guidance.

## Quick Links and Resources

### Gateway Version Migration Reference

Understanding which gateways require migration is straightforward based on the gateway software version number. It's important to note that even recently activated gateways based on Amazon Linux 2 OS still require migration by June 30, 2026.

| Gateway Type    | AL2 Version (Requires Migration) | AL2023 Version (Target) |
| --------------- | -------------------------------- | ----------------------- |
| S3 File Gateway | Version 1.x                      | Version 2.x             |
| Tape Gateway    | Version 2.x                      | Version 3.x             |
| Volume Gateway  | Version 2.x                      | Version 3.x             |

### Migration Timeline

The migration timeline includes several critical milestones:

- **October 28, 2025:** All new gateway deployments initiated from Storage Gateway console will default to AL2023 images.
- **January 5, 2026:** AWS will begin restricting new AL2 gateway activations.
- **June 30, 2026:** AL2-based gateways will stop receiving software updates and AWS support will end. After this date, while you can continue using AL2-based appliances, they will receive no new software updates, security patches, or bug fixes, and maintaining these systems becomes your sole responsibility.

### Migration Guides

- [S3 File Gateway Migration Guide](../../../filegateway/latest/files3/migrate-data.md "../../../filegateway/latest/files3/migrate-data.md")
- [Tape Gateway Migration Guide](migrate-data.md "migrate-data.md")
- [Volume Gateway Migration Guide](../vgw/migrate-data.md "../vgw/migrate-data.md")

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

Your gateway will continue to operate normally, and data will remain safely stored in AWS, but you must migrate affected gateways by June 30, 2026, to continue receiving updates and support.

**Can I continue to use my AL2 based gateway after migrating?**

No, you should not use your AL2 gateway alongside your new AL2023 gateway after successfully migrating. Use only your new AL2023-based gateway going forward. Using both AL2 and AL2023 gateways simultaneously may cause operational issues.

**I'm having issues during migration. What should I do?**

Contact [AWS Support](https://console.aws.amazon.com/support/home "https://console.aws.amazon.com/support/home") for assistance. Our support team can help troubleshoot migration issues and guide you through the process.
