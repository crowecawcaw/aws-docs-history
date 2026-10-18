

# Understand distribution plans in Amazon Lightsail
<a name="amazon-lightsail-distribution-plans"></a>

A *distribution plan* is a monthly charge that comes with a monthly data transfer quota. Your data transfer quota resets at the start of each month. If your distribution exceeds its monthly data transfer quota, you may be charged for overage.

To avoid an overage fee, change your distribution's current plan to a different plan that offers a greater amount of monthly data transfer before your distribution exceeds its monthly quota. You can change your distribution's plan only one time during each AWS billing cycle. For more information about changing your distribution's plan after you create it, see [Change the plan of your distribution](amazon-lighstail-changing-distribution-plan.md).

## How is Lightsail distribution data transfer aggregated?
<a name="amazon-lightsail-distribution-data-transfer"></a>

Lightsail aggregates your distribution's data transfer over each monthly AWS billing cycle and compares the total against your plan's monthly data transfer quota to determine whether you incur an overage. The following points explain what data transfer counts towards your quota and how overage is calculated:
+ Only data transfer OUT of your distribution (to your viewers) counts toward your monthly data transfer quota.
+ Data transfer IN to your distribution is free and does not count toward your quota.
+ Data transfer IN to your distribution from your origin, and data transfer OUT from your distribution to your origin, is free and does not count toward your distribution quota.
+ Data transfer OUT from all edge locations is added together over the billing cycle. When this combined total exceeds your plan's monthly data transfer quota, the amount over the quota is billed as an overage.
+ Overage is billed per GB, and the rate is charged at the geographic location of the edge location that serves each request.

## Distribution data transfer overage pricing
<a name="distribution-data-transfer-overage-pricing"></a>

Your content is served from your distribution to each viewer from the AWS edge location closest to them. Data transfer overage is billed per GB, and the overage rate is charged at the rate of the geographic location of the edge location that serves the request — not the location of your distribution's origin.

For example, if your distribution's origin is in the United States, a viewer in the United States is served from a nearby edge location, so overage for that request is billed at USD $0.09/GB. A viewer in Australia is served from an edge location in Australia, so overage for that request is billed at a rate of USD $0.17/GB. Your overage bill is the sum of the data transfer OUT served from each edge location, charged at that location's rate.

The following table lists the data transfer overage rates by geographic location, current as of this writing. These rates apply only to data transfer OUT that exceeds your plan's monthly quota. For additional distribution pricing information, see the [Lightsail pricing page](https://aws.amazon.com/lightsail/pricing/).


| Location | Data transfer overage rate | 
| --- | --- | 
| Asia Pacific | USD $0.13/GB | 
| Australia | USD $0.17/GB | 
| Canada | USD $0.09/GB | 
| Europe | USD $0.09/GB | 
| India | USD $0.13/GB | 
| Japan | USD $0.14/GB | 
| Middle East | USD $0.11/GB | 
| South Africa | USD $0.11/GB | 
| South America | USD $0.11/GB | 
| United States | USD $0.09/GB | 