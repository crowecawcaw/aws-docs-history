

# Update telephony traffic distribution across Connect Customer instances and AWS Regions
<a name="update-telephony-traffic-distribution"></a>

You use the [UpdateTrafficDistribution](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateTrafficDistribution.html) API to distribute telephony traffic and [shift agents](update-agents-across-regions.md) across Regions.

**Note**  
When you shift telephony traffic, also shift agents or agent sign-ins to make sure they can handle the calls in the other Region. If you don't shift the agents, voice calls will go to the shifted Region but there won't be any agents available to receive the calls.

After you have claimed phone numbers to your traffic distribution group, you can use the [UpdateTrafficDistribution](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateTrafficDistribution.html) API to distribute inbound voice contacts across linked instances in a given traffic distribution group in 10% increments.

If the following requirements are not met, your [UpdateTrafficDistribution](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateTrafficDistribution.html) API call will fail with an `InvalidRequestException`:
+ You must provide distribution for telephony traffic configuration.
+ You must specify the traffic distribution for both linked instances and the total distribution must add up to 100%.
+ You must specify traffic distribution in 10% increments.
+ The instance ARNs specified in the telephony configuration must match the ARNs of the linked instances.

When you call `UpdateTrafficDistribution` from the source AWS Region you can use either the traffic distribution group ID or Amazon Resource Name (ARN). When you call `UpdateTrafficDistribution` in the replica Region, you must use the traffic distribution group ARN.