# Update telephony traffic

distribution across Amazon Connect instances and AWS Regions

You use the [UpdateTrafficDistribution](../APIReference/API_UpdateTrafficDistribution.md "../APIReference/API_UpdateTrafficDistribution.md") API to distribute telephony traffic and [shift agents](update-agents-across-regions.md "update-agents-across-regions.md") across
Regions.

###### Note

When you shift telephony traffic, also shift agents and/or agent sign-ins to
ensure they can handle the calls in the other Region. If you don't shift the
agents, voice calls will go to the shifted Region but there won't be any agents
available to receive the calls.

After you have claimed phone numbers to your traffic distribution group, you can
use the [UpdateTrafficDistribution](../APIReference/API_UpdateTrafficDistribution.md "../APIReference/API_UpdateTrafficDistribution.md") API to distribute inbound voice contacts
across linked instances in a given traffic distribution group in 10%
increments.

If the following requirements are not met, your [UpdateTrafficDistribution](../APIReference/API_UpdateTrafficDistribution.md "../APIReference/API_UpdateTrafficDistribution.md") API call will fail with an
`InvalidRequestException`:

- You must provide distribution for telephony traffic configuration.
- You must specify the traffic distribution for both linked instances and
  the total distribution must add up to 100%.
- You must specify traffic distribution in 10% increments.
- The instance ARNs specified in the telephony configuration must match the
  ARNs of the linked instances.
  When you call `UpdateTrafficDistribution` from the source AWS
  Region you can use either the traffic distribution group ID or Amazon Resource Name (ARN). When you call
  `UpdateTrafficDistribution` in the replica Region, you must use the
  traffic distribution group ARN.
