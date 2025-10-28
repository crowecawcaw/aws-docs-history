# DRHCSUS01-BP02 Anchor your AWS Outposts to the Region that best aligns to both your cloud deployment patterns and sustainability goals

You have the flexibility to anchor an AWS Outposts to any
supported AWS Region and can consider anchoring to an AWS Region
that helps you meet your sustainability objectives.

**Desired outcome:** Your AWS Outposts are anchored using a service link connection to the most
sustainable AWS Region.

**Benefits of establishing this best
practice:** Choosing to anchor your AWS Outposts to a
more sustainable AWS Region can help you meet your sustainability
objectives.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

AWS Outposts must be anchored to service link endpoints exposed
in an AWS Region. The Region to which an AWS Outpost is anchored
is determined at the time an order is placed. Unlike with Local
Zones, an AWS Outpost can be anchored to any supported Region,
so you have more flexibility to select the anchor Region based
on your sustainability goals. When deploying an AWS Outpost to
address data residency requirements, consider anchoring it to
the most
[sustainable
Region](https://aws.amazon.com/blogs/architecture/how-to-select-a-region-for-your-workload-based-on-sustainability-goals/ "https://aws.amazon.com/blogs/architecture/how-to-select-a-region-for-your-workload-based-on-sustainability-goals/") that also aligns with your overall networking and
application architecture patterns.
