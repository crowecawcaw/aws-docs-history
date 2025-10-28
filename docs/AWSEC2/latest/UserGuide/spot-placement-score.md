# Spot placement score

The Spot placement score feature can recommend an AWS Region or Availability Zone based
on your Spot capacity requirements. Spot capacity fluctuates, and you can't be sure that
you'll always get the capacity that you need. A Spot placement score indicates how likely it is that a Spot
request will succeed in a Region or Availability Zone.

###### Note

A Spot placement score does not provide any guarantees in terms of available capacity or risk of
interruption. A Spot placement score serves only as a recommendation.

###### Use cases

You can use the Spot placement score feature for the following:

- To relocate and scale Spot compute capacity in a different Region, as needed, in
  response to increased capacity needs or decreased available capacity in the current
  Region.
- To identify the most optimal Availability Zone in which to run single-Availability
  Zone workloads.
- To simulate future Spot capacity needs so that you can pick an optimal Region for
  the expansion of your Spot-based workloads.
- To find an optimal combination of instance types to fulfill your Spot capacity
  needs.

###### Contents

- [Limitations](#sps-limitations "#sps-limitations")
- [Costs](#sps-costs "#sps-costs")
- [How Spot placement score works](how-sps-works.md "how-sps-works.md")
- [Required permissions for Spot placement score](sps-iam-permission.md "sps-iam-permission.md")
- [Calculate the Spot placement score](work-with-spot-placement-score.md "work-with-spot-placement-score.md")

## Limitations

- **Target capacity limit** – Your Spot placement score
  target capacity limit is based on your recent Spot usage, while accounting for
  potential usage growth. If you have no recent Spot usage, we provide you with a
  low default limit aligned with your Spot request limit.
- **Request configurations limit** – We can
  limit the number of new request configurations within a 24-hour period if we
  detect patterns not associated with the intended use of the Spot placement score feature. If
  you reach the limit, you can retry the request configurations that you've
  already used, but you can't specify new request configurations until the next
  24-hour period.
- **Minimum number of instance types** – If
  you specify instance types, you must specify at least three different instance
  types, otherwise Amazon EC2 will return a low Spot placement score. Similarly, if you specify
  instance attributes, they must resolve to at least three different instance
  types. Instance types are considered different if they have a different name.
  For example, m5.8xlarge, m5a.8xlarge, and m5.12xlarge are all considered
  different.

## Costs

There is no additional charge for using the Spot placement score feature.
