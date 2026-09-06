

# Regions and Availability Zones for Lightsail
<a name="understanding-regions-and-availability-zones-in-amazon-lightsail"></a>

When creating resources in Amazon Lightsail, create them in an AWS Region that is closer to your users. You can also leverage multiple Availability Zones for fault tolerance and high availability with your applications. By provisioning resources closer to your users, your users can benefit from lower latency and increased performance. For example, if your blog traffic comes mostly from Switzerland, choose **Frankfurt** or **Paris**.

If your application would benefit from being created in an opt-in Region (Region that is disabled by default) that is supported for Lightsail, you can [enable the Region](https://docs.aws.amazon.com/lightsail/latest/userguide/opt-in-regions-for-lightsail-enable.html). If you later decide that you no longer want to operate resources in an opt-in Region, you can [disable the Region](https://docs.aws.amazon.com/lightsail/latest/userguide/opt-in-regions-for-lightsail-disable.html). For more information about opt-in Regions, see [Considerations before enabling and disabling Regions](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html#manage-acct-regions-considerations) and the [opt-in Region](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html?icmpid=docs_homepage_addtlrcs#optinregion) entry in the *AWS Glossary*.

**Note**  
Global resources such as DNS zones and Lightsail distributions are created only in the US East (N. Virginia) (us-east-1) Region, but they can reference any supported resource in any AWS Region.

**Topics**
+ [Regions for Lightsail](#regions-for-amazon-lightsail)
+ [SSH keys and Lightsail Regions](#ssh-keys-and-regions)
+ [Tips for working with Lightsail Regions](#tips-working-with-regions)
+ [Lightsail Availability Zones](#availability-zones)
+ [Availability Zones and your Lightsail application](#why-regions-and-availability-zones)
+ [Enable opt-in Regions for Lightsail](opt-in-regions-for-lightsail-enable.md)
+ [Disable opt-in Regions for Lightsail](opt-in-regions-for-lightsail-disable.md)

## Regions for Lightsail
<a name="regions-for-amazon-lightsail"></a>

Lightsail is available in the following Regions.
+ US East (N. Virginia) (us-east-1)
+ US East (Ohio) (us-east-2)
+ US West (Oregon) (us-west-2)
+ Asia Pacific (Hong Kong) (ap-east-1) \*
+ Asia Pacific (Jakarta) (ap-southeast-3) \*
+ Asia Pacific (Malaysia) (ap-southeast-5) \*
+ Asia Pacific (Mumbai) (ap-south-1)
+ Asia Pacific (Seoul) (ap-northeast-2)
+ Asia Pacific (Singapore) (ap-southeast-1)
+ Asia Pacific (Sydney) (ap-southeast-2)
+ Asia Pacific (Tokyo) (ap-northeast-1)
+ Canada (Central) (ca-central-1)
+ EU (Frankfurt) (eu-central-1)
+ EU (Ireland) (eu-west-1)
+ EU (London) (eu-west-2)
+ EU (Paris) (eu-west-3)
+ EU (Stockholm) (eu-north-1)
+ EU (Spain) (eu-south-2) \*
+ South America (São Paulo) (sa-east-1)

\* This Region is disabled by default. You must [enable the Region](https://docs.aws.amazon.com/lightsail/latest/userguide/opt-in-regions-for-lightsail-enable.html) before you can use it.

![Supported AWS Regions in Amazon Lightsail](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-regions_720.png)


## SSH keys and Lightsail Regions
<a name="ssh-keys-and-regions"></a>

In Lightsail, as soon as you create an instance in an AWS Region, we create a **Default** SSH key in that Region. This default key can be used to connect to instances only in that specific Region. For more information, see [SSH key pairs](understanding-ssh-in-amazon-lightsail.md).

## Tips for working with Lightsail Regions
<a name="tips-working-with-regions"></a>

Each AWS Region is designed to be completely isolated from other AWS Regions. This achieves the greatest possible fault tolerance and stability.

All communication between Regions occurs across the public internet. Therefore, you should use the appropriate encryption methods to protect your data. There is a charge for data transfer between Regions. For more information, see [Amazon EC2 Pricing - Data Transfer](https://aws.amazon.com/ec2/pricing/on-demand/#Data_Transfer).

When you work with a Lightsail instance using the AWS Command Line Interface (AWS CLI), we recommend that you specify the code for the Region using the `--region` option in your AWS CLI command. For example, you can specify **us-east-1** to return information about DNS zones and network resources in the US East (N. Virginia) (us-east-1) Region. For more information about using the AWS CLI `--region` option, see [General Options](http://docs.aws.amazon.com/cli/latest/topic/config-vars.html#general-options) in the *AWS CLI Reference*.

## Lightsail Availability Zones
<a name="availability-zones"></a>

Each AWS Region has multiple, isolated Availability Zones, which are indicated by a letter following the Region name (`us-east-2{{a}}`). Availability Zones are collections of data centers that run on physically distinct, independent infrastructure. Availability Zones are engineered to be highly reliable. Common points of failure such as generators and cooling equipment are not shared between Availability Zones. Availability Zones are also physically separate so that even an extreme disaster such as a fire, tornado, or flood will affect only the single Availability Zone where it occurred.

![How Availability Zones work in Amazon Lightsail](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-availability-zones-example.png)


You can create Lightsail instances in only one Availability Zone at a time. You might not see all Availability Zones at the time you create your instance. If you don't see the list of Availability Zones at all, be sure that you have selected a Region in the previous step.

## Availability Zones and your Lightsail application
<a name="why-regions-and-availability-zones"></a>

By launching your instances in separate Availability Zones, you can protect your applications from a failure in a single location. Before you proceed with such a configuration, review the general and application specific guidelines. For more information, see [Configure Lightsail instances for load balancing](https://docs.aws.amazon.com/lightsail/latest/userguide/configure-lightsail-instances-for-load-balancing.html).

To proceed with scaling an existing instance to make your application available in multiple Availability Zones, first [create a snapshot of your instance](understanding-snapshots-in-amazon-lightsail.md). Next, choose another Availability Zone when you [create a new instance from the snapshot you created](lightsail-how-to-create-instance-from-snapshot.md). With the new instance created from the snapshot, you can [distribute web traffic to the instances with a Lightsail load balancer](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-lightsail-load-balancers.html).