

# Example Scenarios
<a name="interconnect-pricing-scenarios"></a>

The following examples show how the Tier structure is applied to your Interconnect in different scenarios.

## Example 1: Local, single Interconnect
<a name="example-1"></a>

You create a new Interconnect that is local to the us-east-1 (N. Virginia) Region and associate it to a VPC in the same Region using a VGW. This Interconnect will be subscribed to Tier 1 as the local path between the N. Virginia Region and an Interconnect provisioned in N. Virginia is Tier 1.

![Example 1 - Local single Interconnect Tier 1 diagram](http://docs.aws.amazon.com/interconnect/latest/userguide/images/pricing-example1.png)


## Example 2: Global, same continent, single Interconnect
<a name="example-2"></a>
+ You have a Cloud WAN Core Network with CNEs in the us-east-1 (N. Virginia) and us-west-2 (Oregon) Regions.
+ You create a new Interconnect that is local to the Oregon Region and associate it to your Core Network.

In this case, the path between the Oregon Region and your Interconnect that is local to that Region is Tier 1 and the path between your Interconnect and the N. Virginia Region is Tier 2. This Interconnect will then be subscribed to Tier 2, as it is the lowest Tier that includes all your potential paths.

![Example 2 - Global same continent Tier 2 diagram](http://docs.aws.amazon.com/interconnect/latest/userguide/images/pricing-example2.png)


## Example 3: Global, intercontinental, single Interconnect
<a name="example-3"></a>
+ You have the same Cloud WAN Core Network with CNEs in the us-east-1 (N. Virginia) and us-west-2 (Oregon) Regions and an Interconnect that is local to the Oregon Region.
+ You add a new CNE in the eu-central-1/Europe (Frankfurt) Region to the Core Network.

In this case, the new path between the Interconnect and the Frankfurt Region is Tier 3. The Interconnect will then be automatically upgraded to Tier 3, as it is the lowest Tier that now includes the local Tier 1 path between the Interconnect and the Oregon Region, the Tier 2 path between the Interconnect and the N. Virginia Region, and the Tier 3 path between the Interconnect and the Frankfurt Region.

![Example 3 - Global intercontinental Tier 3 diagram](http://docs.aws.amazon.com/interconnect/latest/userguide/images/pricing-example3.png)


## Example 4: Global, intercontinental, multiple Interconnects
<a name="example-4"></a>
+ You have the same Cloud WAN Core Network with CNEs in the us-east-1 (N. Virginia), us-west-2 (Oregon), and eu-central-1/Europe (Frankfurt) Regions with an existing Interconnect that is local to the Oregon Region which is already subscribed to Tier 3.
+ You don’t have a Cloud WAN CNE in the Sydney Region, but you need to reach your resources in another CSP’s Region in Sydney from your existing CNEs in Germany and the United States.
+ You create a new Interconnect that is local to the ap-southeast-2/Asia Pacific (Sydney) Region and attach it to the same DXGW that is already associated to your Cloud WAN Core Network.

In this case, there is no change in Tier to your existing Interconnect as it doesn’t need to reach a CNE in Sydney.

Your new Interconnect provisioned in Sydney will be automatically subscribed to Tier 4 as it needs to reach your CNEs in Germany and the United States and that is the lowest Tier that now includes the Tier 3 path between the Interconnect in Sydney and the Oregon Region, the Tier 2 path between Sydney and the N. Virginia Region, and the Tier 4 path between Sydney and the Frankfurt Region. You now have two Interconnects subscribed to Tiers 3 and 4, respectively, as those are the lowest possible Tiers that include all the possible paths for the specific Interconnect.

![Example 4 - Global intercontinental multiple Interconnects diagram](http://docs.aws.amazon.com/interconnect/latest/userguide/images/pricing-example4.png)
