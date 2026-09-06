

# Get started with Connect Customer Global Resiliency
<a name="get-started-connect-global-resiliency"></a>

**Important**  
Connect Customer instances created before March 31, 2021, were assigned a domain with the following format:  

```
                https://{{your-instance-alias}}.awsapps.com/connect/
```
If your domain uses the older format, you won’t be able to properly configure the Connect Customer Global Resiliency feature. To enable this feature, you’ll need to [update your domain](update-your-connect-domain.md) to the newer format:  

```
                https://{{your-instance-alias}}.my.connect.aws/
```

**Note**  
**New user?** Check out the [Connect Customer Global Resiliency Workshop](https://catalog.workshops.aws/amazon-connect-global-resiliency/en-US). This online course guides you through the process of onboarding and testing phone number and agent failover using new APIs through the AWS CLI.  
Global Resiliency is available only for Connect Customer instances created in the following AWS Regions: US East (N. Virginia), US West (Oregon), Asia Pacific (Osaka), Asia Pacific (Tokyo), Europe (Frankfurt), and Europe (London).  
You can only create a replica in the US East (N. Virginia) Region if your source is US West (Oregon), or the other way around. 
You can only create a replica in the Europe (Frankfurt) Region if your source is Europe (London), or the other way around.
You can only create a replica in Asia Pacific (Osaka) Region if your source is Asia Pacific (Tokyo).
To obtain access to this feature, contact your Connect Customer Solutions Architect or Technical Account Manager.

You get started with Connect Customer Global Resiliency by creating a replica of your existing Connect Customer instance in another AWS Region, and by creating a traffic distribution group. 

A *traffic distribution group* is a Connect Customer resource that you can use to link Connect Customer instances that are in different AWS Regions. Phone numbers can be attached to the traffic distribution group. Traffic to these numbers can be distributed between the instances in the traffic distribution group. 

## How to set up Connect Customer Global Resiliency
<a name="howto-setup-gr"></a>

1. [Create a replica of your existing Connect Customer instance](create-replica-connect-instance.md). Use the [ReplicateInstance](https://docs.aws.amazon.com/connect/latest/APIReference/API_ReplicateInstance.html) API.

1. [Create a traffic distribution group](setup-traffic-distribution-groups.md).

   1. Use the [CreateTrafficDistributionGroup](https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateTrafficDistributionGroup.html) API.

   1. Use [DescribeTrafficDistributionGroup](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeTrafficDistributionGroup.html) API to determine whether the traffic distribution group has been created successfully (`Status` must be `ACTIVE`).

1. [Claim phone numbers to your traffic distribution group](claim-phone-numbers-traffic-distribution-groups.md). After your traffic distribution group has been created successfully (`Status` is `ACTIVE`), you can claim phone numbers to it using the [ClaimPhoneNumber](https://docs.aws.amazon.com/connect/latest/APIReference/API_ClaimPhoneNumber.html) API. 
**Note**  
The default traffic distribution for these phone numbers is set to 100% - 0%. That is, 100% of inbound telephony traffic will go to the source Connect Customer instance that was used to create a replica.   
In addition, after phone numbers are claimed to an instance, you can assign them to multiple instances across AWS Regions. To do this, use the [UpdatePhoneNumber](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdatePhoneNumber.html) API to assign the numbers to a traffic distribution group.

1. [Update your traffic distribution](update-telephony-traffic-distribution.md). Use the [UpdateTrafficDistribution](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateTrafficDistribution.html) API to distribute traffic across the linked instances in 10% increments. 

**Perform monthly failover testing**  
Perform monthly testing to validate your failover procedure and confirm your runbook is current.  
If a full failover test is not feasible, create a test traffic distribution group pointed to the replica Region. Use it to test critical flows monthly without impacting production traffic.