# Entitlement sharing in Oracle Database@AWS

With Oracle Database@AWS, you can share AWS Marketplace entitlements for Oracle Database@AWS across AWS accounts in
the same AWS organization. This allows other accounts to provision their own Oracle Exadata infrastructure and ODB network resources using your subscription.

## Sharing methods

Oracle Database@AWS supports two methods for sharing:

### Entitlement sharing with AWS License Manager

- Grant other accounts the ability to provision their own Oracle Exadata infrastructure and ODB network resources
- Each account operates independently with full resource lifecycle control
- Best for enabling self-service provisioning across teams or business units

### Resource sharing with AWS Resource Access Manager (AWS RAM)

- Share already provisioned Oracle Exadata infrastructure and ODB network resources
- Centralize infrastructure management while allowing recipient accounts to create VM clusters
- Optimize costs by having multiple accounts use the same infrastructure

You can use both sharing methods simultaneously based on your organizational needs.

## Limitations for Oracle Database@AWS entitlement sharing

When sharing Oracle Database@AWS entitlements, keep the following limitations in mind:

- You can only share with AWS accounts within your AWS organization
- You cannot share with an entire organizational unit (OU) or the entire organization
- An account can receive entitlements from only one buyer account (from one private offer)
- A buyer account cannot share entitlements with another buyer account
- Recipient accounts must initialize the Oracle Database@AWS service before they can use the shared entitlement
