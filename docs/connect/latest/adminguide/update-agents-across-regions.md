# Update agent distribution in your

Amazon Connect agent workspace across AWS Regions

Just as you can use the `UpdateTrafficDistribution` API to [distribute telephony traffic
across Regions](update-telephony-traffic-distribution.md "update-telephony-traffic-distribution.md"), you can also use it to distribute agents across AWS
Regions, either fully or gradually as part of regular operational readiness
testing. For example, you might keep 40% of agents in one AWS Region to
complete active contacts and shift the remaining agents to the replica
Region.

###### Note

When you shift telephony traffic, also shift agents and/or agent sign-ins
to ensure they can handle the calls in the other Region. If you don't shift
the agents, voice calls will go to the shifted Region but there won't be any
agents available to receive the calls.

After you have added agents to your traffic distribution group, use the [UpdateTrafficDistribution](../APIReference/API_UpdateTrafficDistribution.md "../APIReference/API_UpdateTrafficDistribution.md") API to distribute agents across linked
instances in a given traffic distribution group in 10% increments. Your agents
will be able to complete active voice contacts before shifting Regions.

###### Note

If an agent gets an error when they try to end a contact before shifting
Regions, they need to refresh the agent workspace page. For more
information, see [Set up Amazon Connect Agent Workspace
to support agents shifting across AWS Regions](setup-agentworkspace-switchover.md "setup-agentworkspace-switchover.md").

###### Contents

- [Requirements](#update-agent-traffic-distribution-requirements "#update-agent-traffic-distribution-requirements")
- [Enable both Regions
  during regular operations](#change-signin-weights "#change-signin-weights")
- [How to shift all telephony
  traffic and agents across AWS Regions](#shift-all-traffic "#shift-all-traffic")

## Requirements

If the following requirements are not met, your [UpdateTrafficDistribution](../APIReference/API_UpdateTrafficDistribution.md "../APIReference/API_UpdateTrafficDistribution.md") API call will fail with an
`InvalidRequestException`:

1. The specified traffic distribution group must exist.
2. The status of the traffic distribution group must be
   `ACTIVE`.
3. If you are changing the `SignInConfig` distribution,
   you can only do so for the default traffic distribution group. The default traffic distribution group is
   created when the replica Amazon Connect instance is created. See the
   `IsDefault` parameter in the [TrafficDistributionGroup](../APIReference/API_TrafficDistributionGroup.md "../APIReference/API_TrafficDistributionGroup.md") data type.

When you call `UpdateTrafficDistribution` from the source AWS
Region you can use either the traffic distribution group ID or Amazon Resource Name (ARN). When you call
`UpdateTrafficDistribution` in the replica Region, you must use the
traffic distribution group ARN.

## Enable both AWS Regions during

regular operations

The `UpdateTrafficDistribution` API includes a distribution
called `SignInConfig`. It allows you to choose which backend
sign-in servers are used to facilitate the agent signing in to their
instance group. Regardless of the `SignInConfig` set in your
traffic distribution group, agents will be signed in to both instances in
the traffic distribution group.

For the best experience, we recommend having both AWS Regions enabled
during regular operations. To achieve this pass `true` to both
`SignInConfig` distributions. If you need to shift your
entire telephony traffic and agents across to one AWS Region, we recommend
changing the `SignInConfig` to `false` for the Region
you are shifting traffic away from.

For example, the following call results in agents having a 50% chance of
using the us-west-2 sign-in server and a 50% of using the us-east-1 sign-in
server for a given login call from the identity provider.

```
aws connect update-traffic-distribution \
--id traffic distribution group ID or ARN \
--cli-input-json \
'{
   "SignInConfig":{
      "Distributions":[
         {
            "Region":"us-west-2",
            "Enabled":true
         },
         {
            "Region":"us-east-1",
            "Enabled":true
         }
      ]
   }
}'
```

Conversely, the following sign-in distribution routes 100% of traffic on
the sign-in endpoint to use the us-east-1 sign-in server.

```
aws connect update-traffic-distribution \
--id traffic distribution group ID or ARN \
--cli-input-json \
'{
   "SignInConfig":{
      "Distributions":[
         {
            "Region":"us-west-2",
            "Enabled":false
         },
         {
            "Region":"us-east-1",
            "Enabled":true
         }
      ]
   }
}'
```

This distribution controls only which Region of the sign-in server is used
to facilitate logging in the agent to both instances in their instance
group. It doesn't affect the distribution of agents controlled by the
`AgentConfig` part of the
`UpdateTrafficDistribution` API.

###### Important

If the sign-in endpoint is not responsive during agent sign-in and
your `SignInConfig` distribution is split across Regions,
then you can resolve the errors by changing distribution to a single
AWS Region. Or, if your `SignInConfig` is weighted on one
Region and it isn't responsive, you can try shifting the
`SignInConfig` to the disabled Region. Regardless of how
your `SignInConfig` is configured, agents will still benefit
from having a session active in both the source and replica Regions
because they will attempt to sign into their Amazon Connect instance in both
Regions.

## How to shift all telephony traffic and

agents across AWS Regions

To shift all new inbound voice contacts, agent sign-in distribution, and
agent distribution from us-west-2 to us-east-1, use the following code
snippet.

```
aws connect update-traffic-distribution \
--id traffic distribution group ID or ARN \
--cli-input-json \
'{
   "SignInConfig":{
      "Distributions":[
         {
            "Region":"us-west-2",
            "Enabled":false
         },
         {
            "Region":"us-east-1",
            "Enabled":true
         }
      ]
   },
   "AgentConfig":{
      "Distributions":[
         {
            "Region":"us-west-2",
            "Percentage":0
         },
         {
            "Region":"us-east-1",
            "Percentage":100
         }
      ]
   },
   "TelephonyConfig":{
      "Distributions":[
         {
            "Region":"us-west-2",
            "Percentage":0
         },
         {
            "Region":"us-east-1",
            "Percentage":100
         }
      ]
   }
}
'
```

When you call `UpdateTrafficDistribution` from the source AWS
Region you can use either the traffic distribution group ID or Amazon
Resource Name (ARN). When you call `UpdateTrafficDistribution` in
the replica Region, you must use the traffic distribution group ARN.
