#

List and update routing controls and states with the AWS CLI

After you create your Amazon Application Recovery Controller (ARC) resources, such as cluster, routing controls, and control panels, you can
interact with the cluster to list and update routing control states for failover.

For each cluster that you create, ARC provides you with a set of cluster endpoints, one in each of five AWS Regions.
You must specify one of these Regional endpoints (the AWS Region and the endpoint URL) when you make calls to the
cluster to retrieve or set routing control states to `On` or `Off`. When you use the AWS CLI, to get
or update routing control states, in addition to the Regional endpoint, you must also specify the
`--region` of the Regional endpoint, as shown in the examples in this section.

You can use any of the Regional cluster endpoints. We recommend that your systems rotate through the regional
endpoints, and be prepared to retry with each of the available endpoints. For code samples that illustrate trying cluster endpoints in sequence,
see [Actions for Application Recovery Controller using AWS SDKs](service_code_examples_actions.md "service_code_examples_actions.md") .

For more information about using the AWS CLI, see the AWS CLI Command Reference. For a list of routing control API actions and
links to more information, see [Routing control API operations](actions.md "actions.md").

###### Important

Although you can update a routing control state on the Amazon Route 53 console, we recommend
that you [update routing control states](routing-control.update.md "routing-control.update.md") by using the AWS CLI or an AWS SDK. ARC offers
extreme reliability with the ARC routing control data plane for rerouting traffic and failing over across cells.
For more recommendations about using ARC for failover, see [Best practices for routing control in ARC](route53-arc-best-practices.md "route53-arc-best-practices.md").

When you create a routing control, the state is set to `Off`. This means that traffic is not routed to the target
cell for that routing control. You can verify the state of the routing control by running the command
`get-routing-control-state`.

To determine the Region and the endpoint to specify, run the `describe-clusters` command to view
the `ClusterEndpoints`. Each `ClusterEndpoint` includes a Region and corresponding
endpoint that you can use to get or update routing control states. _[DescribeCluster](../../../recovery-cluster/latest/api/cluster-clusterarn.md "../../../recovery-cluster/latest/api/cluster-clusterarn.md") is a
recovery control configuration API operation. We recommend that you keep a local copy of your ARC
Regional cluster endpoints, in bookmarks or hardcoded in automation code that you use to retry your endpoints._

##

1.  List routing controls

You can view your routing controls and routing control states using the highly reliable ARC data plane endpoints.

1. List routing controls for a specific control panel. If you don't specify a control panel, `list-routing-controls`
   returns all the routing controls in the cluster.

```
aws route53-recovery-cluster list-routing-controls --control-panel-arn \
        arn:aws:route53-recovery-control::111122223333:controlpanel/0123456bbbbbbb0123456bbbbbb0123456 \
        --region us-west-2 \
        --endpoint-url https://host-dddddd.us-west-2.example.com/v1
```

```
{
    "RoutingControls": [{
        "ControlPanelArn": "arn:aws:route53-recovery-control::111122223333:controlpanel/0123456bbbbbbb0123456bbbbbb0123456",
        "ControlPanelName": "ExampleControlPanel",
        "RoutingControlArn": "arn:aws:route53-recovery-control::111122223333:controlpanel/0123456bbbbbbb0123456bbbbbb0123456/routingcontrol/abcdefg1234567",
        "RoutingControlName": "RCOne",
        "RoutingControlState": "On"
    },
    {
        "ControlPanelArn": "arn:aws:route53-recovery-control::023759465626:controlpanel/0123456bbbbbbb0123456bbbbbb0123456",
        "ControlPanelName": "ExampleControlPanel",
        "RoutingControlArn": "arn:aws:route53-recovery-control::023759465626:controlpanel/0123456bbbbbbb0123456bbbbbb0123456/routingcontrol/zzzzxxxxyyyy123456",
        "RoutingControlName": "RCTwo",
        "RoutingControlState": "Off"
    }
]
```

##

2. Get routing controls

3. Get a routing control state.

```
aws route53-recovery-cluster get-routing-control-state --routing-control-arn \
        arn:aws:route53-recovery-control::111122223333:controlpanel/0123456bbbbbbb0123456bbbbbb0123456/routingcontrol/abcdefg1234567 \
        --region us-west-2 \
        --endpoint-url https://host-dddddd.us-west-2.example.com/v1
```

```
{"RoutingControlArn": "arn:aws:route53-recovery-control::111122223333:controlpanel/0123456bbbbbbb0123456bbbbbb0123456/routingcontrol/abcdefg1234567",
    "RoutingControlName": "RCOne",
    "RoutingControlState": "On"
}
```

##

2.  Update routing controls

To route traffic to the target endpoint controlled by the routing control, you update the routing control state to `On`.
Update the routing control state by running the command `update-routing-control-state`.
(When the request is successful, the response is empty.)

2a. Update a routing control state.

```
aws route53-recovery-cluster update-routing-control-state \
        --routing-control-arn \
        arn:aws:route53-recovery-control::111122223333:controlpanel/0123456bbbbbbb0123456bbbbbb0123456/routingcontrol/abcdefg1234567 \
        --routing-control-state On \
        --region us-west-2 \
        --endpoint-url https://host-dddddd.us-west-2.example.com/v1
```

```
{}
```

You can update several routing controls at the same time with one API call: `update-routing-control-states`.
(When the request is successful, the response is empty.)

2b. Update several routing control states at once (batch updates).

```
aws route53-recovery-cluster update-routing-control-states \
        --update-routing-control-state-entries \
        '[{"RoutingControlArn": "arn:aws:route53-recovery-control::111122223333:controlpanel/0123456bbbbbbb0123456bbbbbb0123456/routingcontrol/abcdefg1234567",
        "RoutingControlState": "Off"}, \
        {"RoutingControlArn": "arn:aws:route53-recovery-control::111122223333:controlpanel/0123456bbbbbbb0123456bbbbbb0123456/routingcontrol/hijklmnop987654321",
        "RoutingControlState": "On"}]' \
        --region us-west-2 \
        --endpoint-url https://host-dddddd.us-west-2.example.com/v1
```

```
{}
```
