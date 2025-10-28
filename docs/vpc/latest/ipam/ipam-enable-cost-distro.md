# Enable cost distribution

When you enable cost distribution, you distribute the [charges for active IP addresses](pricing-ipam.md "pricing-ipam.md") to the
accounts using the IP addresses rather than to the IPAM owner. This is useful for large
organizations where the delegated IPAM admin manages the IP addresses centrally using IPAM and each account is responsible for their own usage,
eliminating the need for manual billing calculations.

The cost distribution option is available when you [create an IPAM](create-ipam.md "create-ipam.md") or [modify an
IPAM](mod-ipam-region.md "mod-ipam-region.md") under **Metering mode**, where:

- **IPAM owner** (default): The AWS account which owns the IPAM is charged for all active IP addresses managed in IPAM.
- **Resource owner**: The AWS account that owns the IP address is charged for the active IP address.
  **Requirements**

- Your IPAM must be [integrated with
  AWS Organizations](enable-integ-ipam.md "enable-integ-ipam.md").
- The IPAM must have been created by the delegated IPAM admin in your AWS
  Organization.
- The IPAM's home region must be a Region that's enabled by default. It cannot be an [opt-in Region](../../../global-infrastructure/latest/regions/aws-regions.md#regions-opt-in-status "../../../global-infrastructure/latest/regions/aws-regions.md#regions-opt-in-status").
  **How charging works**

- Even though you can distribute IP address charges within an organization, all IPAM charges are consolidated to the
  organization's payer account through [AWS Organizations consolidated billing](../../../awsaccountbilling/latest/aboutv2/con-bill-blended-rates.md "../../../awsaccountbilling/latest/aboutv2/con-bill-blended-rates.md").
- When cost distribution is enabled, organization member accounts can still view their individual IPAM usage and
  charges in their account bills.
- The IPAM ARN will appear on individual account bills when cost distribution is
  enabled, which allows resource owners to track their IPAM active IP usage. If you
  use [AWS Data Exports](../../../cur/latest/userguide/what-is-data-exports.md "../../../cur/latest/userguide/what-is-data-exports.md"), IPAM charges appear with the associated IPAM ARN in both
  consolidated and individual account bills.
- Only accounts within the delegated administrator's organization can
  receive charges for the resources that they own. IP address costs outside of the
  organization are charged to the IPAM owner.
  **Time restrictions**

- You have 24 hours to opt out after enabling cost distribution. After 24 hours, you
  cannot change the setting for 7 days. After 7 days, you can disable cost
  distribution.
