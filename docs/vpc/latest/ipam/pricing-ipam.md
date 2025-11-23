# Pricing for IPAM

Amazon VPC IP Address Manager (IPAM) is a service that helps you manage your IP address space across your AWS resources and on-premises networks. IPAM provides a centralized way to plan, monitor, and control the IP addresses used by your AWS and on-premises resources.

This section describes how to view pricing-related information and your current IPAM
costs.

###### Contents

- [View pricing information](#pricing-ipam-view "#pricing-ipam-view")
- [View your current costs and usage using AWS Cost Explorer](#pricing-ipam-CE "#pricing-ipam-CE")

## View pricing information

IPAM is offered in two tiers: Free and Advanced Tier. For more information about the
features available in each tier and the costs associated with the tiers, see the
**IPAM** tab on the [Amazon VPC pricing page](https://aws.amazon.com//vpc/pricing/ "https://aws.amazon.com//vpc/pricing/").

## View your current costs and usage using AWS Cost Explorer

When you use the IPAM Advanced Tier, you pay an hourly price per active IP address managed by IPAM. If you want to view and analyze your IPAM costs and usage, you can use the AWS Cost Explorer.

1. Open the AWS Cost Management console at
   [https://console.aws.amazon.com/cost-management/home](https://console.aws.amazon.com/cost-management/home "https://console.aws.amazon.com/cost-management/home").
2. Choose **Cost Explorer**.
3. Filter for IPAM usage by choosing **Usage type** and entering
   `IPAddressManager`.
4. Select one or more checkboxes. Each of them represents a different AWS Region.
5. Click **Apply**.

If, for example, you select _USE1-IPAddressManager-IP-Hours(Hrs)_ and us-east-1 is your IPAM home Region, you’ll see the number of active IP hours billed by IPAM in all Regions and the cost. If, say, the usage in hours is 18, this means that you could have 1 active IP address for 18 hours, 3 IP addresses in 3 different Regions each active for 6 hours, or any combination of these that add up to 18 hours.

For more information about AWS Cost Explorer, see [Analyzing your costs with AWS Cost Explorer](../../../cost-management/latest/userguide/ce-what-is.md "../../../cost-management/latest/userguide/ce-what-is.md") in the _AWS Cost Management User Guide_.
