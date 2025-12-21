# Get started with Amazon Connect Global

Resiliency

###### Important

Amazon Connect instances created before March 31, 2021, were assigned a domain
with the following format:

```

                https://`your-instance-alias`.awsapps.com/connect/

```

If your domain uses the older format, you won’t be able to properly configure the
Amazon Connect Global Resiliency feature. To enable this feature, you’ll
need to [update your domain](update-your-connect-domain.md "update-your-connect-domain.md") to the
newer format:

```

                https://`your-instance-alias`.my.connect.aws/

```

###### Note

**New user?** Check out the [Amazon Connect Global Resiliency
Workshop](https://catalog.workshops.aws/amazon-connect-global-resiliency/en-US "https://catalog.workshops.aws/amazon-connect-global-resiliency/en-US"). This online course guides you through the process of onboarding and testing phone number
and agent failover using new APIs through the AWS CLI.

Global Resiliency is available only for Amazon Connect instances created in the following AWS Regions: US East (N. Virginia),
US West (Oregon), Asia Pacific (Osaka), Asia Pacific (Tokyo), Europe (Frankfurt), and Europe (London).

- You can only create a replica in the US East (N. Virginia) Region if your source is US West (Oregon), or the other way around.
- You can only create a replica in the Europe (Frankfurt) Region if your source
  is Europe (London), or the other way around.
- You can only create a replica in Asia Pacific (Osaka) Region if your source is Asia Pacific (Tokyo).
  To obtain access to this feature, contact your Amazon Connect Solutions Architect or Technical Account Manager.

You get started with Amazon Connect Global Resiliency by creating a replica of your existing
Amazon Connect instance in another AWS Region, and by creating a traffic distribution group.

A _traffic distribution group_ is an Amazon Connect resource that enables you to link Amazon Connect
instances that are in different AWS Regions. Phone numbers can be
attached to the traffic distribution group. Traffic to these numbers can be distributed between the instances
in the traffic distribution group.

## How to set up Amazon Connect Global Resiliency

1. [Create a replica of your
   existing Amazon Connect instance](create-replica-connect-instance.md "create-replica-connect-instance.md"). Use the [ReplicateInstance](../APIReference/API_ReplicateInstance.md "../APIReference/API_ReplicateInstance.md") API.
2. [Create a
   traffic distribution group](setup-traffic-distribution-groups.md "setup-traffic-distribution-groups.md").
   1. Use the [CreateTrafficDistributionGroup](../APIReference/API_CreateTrafficDistributionGroup.md "../APIReference/API_CreateTrafficDistributionGroup.md") API.
   2. Use [DescribeTrafficDistributionGroup](../APIReference/API_DescribeTrafficDistributionGroup.md "../APIReference/API_DescribeTrafficDistributionGroup.md") API to determine
      whether the traffic distribution group has been created successfully (`Status`
      must be `ACTIVE`).

3. [Claim
   phone numbers to your traffic distribution group](claim-phone-numbers-traffic-distribution-groups.md "claim-phone-numbers-traffic-distribution-groups.md"). After your traffic distribution group has been created
   successfully (`Status` is `ACTIVE`), you can claim
   phone numbers to it using the [ClaimPhoneNumber](../APIReference/API_ClaimPhoneNumber.md "../APIReference/API_ClaimPhoneNumber.md") API.

###### Note

The default traffic distribution for these phone numbers is set to
100% - 0%. That is, 100% of inbound telephony traffic will go to the
source Amazon Connect instance that was used to create a replica.

In addition, after phone numbers are claimed to an instance, you can
assign them to multiple instances across AWS Regions. To
do this, use the [UpdatePhoneNumber](../APIReference/API_UpdatePhoneNumber.md "../APIReference/API_UpdatePhoneNumber.md") API to assign the numbers to a
traffic distribution group. 4. [Update your traffic
distribution](update-telephony-traffic-distribution.md "update-telephony-traffic-distribution.md"). Use the [UpdateTrafficDistribution](../APIReference/API_UpdateTrafficDistribution.md "../APIReference/API_UpdateTrafficDistribution.md") API to distribute traffic across the
linked instances in 10% increments.
