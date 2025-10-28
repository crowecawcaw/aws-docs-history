# EUCCOST05-BP04 Choose an appropriate running mode for your EUC workload where applicable

Amazon WorkSpaces can be used with monthly and hourly pricing, while Amazon AppStream 2.0 supports
Always-On, On-Demand, and Elastic fleets. Choosing an appropriate running mode can
significantly impact the cost of your EUC services. Historical usage data (usage patterns)
of a reference environment can help you assess which running mode to use for your EUC
workloads. 

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

When you use Amazon WorkSpaces, you can choose between
Always-On and On-Demand running modes, which translate into
monthly and hourly billing respectively. For the non-GPU
bundles, there is a breakeven point at roughly 80 hours of
usage per month, at which point the Always-On WorkSpace will
be more cost-effective. If your users use their WorkSpace for
less than 80 hours per month, the On-Demand running mode is
usually the more cost-effective model for non-GPU bundles.

You can deploy the
[Cost
Optimizer for Amazon WorkSpaces](https://aws.amazon.com/solutions/implementations/cost-optimizer-for-amazon-workspaces/ "https://aws.amazon.com/solutions/implementations/cost-optimizer-for-amazon-workspaces/") to get reports with
recommendations on which running mode to select for your
WorkSpaces and automatically convert your WorkSpaces to the
most cost-effective running mode. For the GPU bundles,
the breakeven point varies from bundle to bundle. The
[Amazon WorkSpaces
Pricing](https://aws.amazon.com/workspaces/pricing/ "https://aws.amazon.com/workspaces/pricing/") page helps you calculate the breakeven point
for these bundles.

Amazon AppStream 2.0 offers three different fleet types: Always-On, On-Demand, and Elastic.
Explore the fleet types to determine the right balance between cost-effective operation
and desired user experience.

- With Always-On fleets, your fleet instances will
  constantly be running while the fleet is in a started
  state, and you'll be charged the respective instance fee
  per hour per instance in your fleet.
- On-Demand fleets have those fleet instances not in use in
  a stopped state, for which you'll be charged the lower
  stopped instance fee per hour per stopped instance in your
  fleet.
  - This can make a significant difference to your cost,
    especially when your fleet instances are higher-end
    instances.
  - However, using On-Demand fleets will prolong the logon
    time by up to 120 seconds.
  - Both Always-On and On-Demand fleet instances are
    charged on one-hour increments, while Elastic Fleet
    instances are charged on one second increments, with a
    minimum of 15 minutes.

- As opposed to Always-On and On-Demand, Elastic fleets do
  not require you to manage scaling policies and provision
  buffer capacity, since the pool of Instances in an Elastic
  fleet is managed by AppStream 2.0.

Amazon AppStream 2.0 offers multi-session fleets, which allow multiple users to use a single
AppStream 2.0 fleet instance. Depending on the user density you can achieve on a given instance,
you may be able to further optimize your AppStream 2.0 costs compared to a single-session fleet.
If you plan to use multi-session fleets, consider resource requirements, instance
specifications, and user behavior. For specific guidance, see [Multi-Session
Recommendations](../../../appstream2/latest/developerguide/multi-session-recs.md "../../../appstream2/latest/developerguide/multi-session-recs.md") .
