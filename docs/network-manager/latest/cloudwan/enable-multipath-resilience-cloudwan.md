

# Enable multipath resilience in a core network policy

Multipath resilience is a cross-Region feature for an AWS Cloud WAN core network. When you enable it in the core network policy, we replicate each packet across multiple paths on the AWS global network between the covered edge locations and de-duplicate the copies at the destination edge. Multipath resilience provides Daily Uptime of at least 99.999%, measured in Unavailable Seconds. For more information about the SLA, see [Multipath Resilience SLA](https://aws.amazon.com/vpc/features/vpc-multipath-resilience/sla) on the AWS website.

Multipath resilience has the following characteristics:
+ **Declarative, no bilateral handshake.** Multipath resilience is configured in the core network policy. Unlike VPC and transit gateway peering, there is no second-side consent step because a core network is a single-account construct.
+ **Cross-Region only.** Multipath resilience applies to traffic between two edge locations in different AWS Regions. At launch, the supported Regions are US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), and Europe (Ireland).
+ **Scoped to edge sets or the whole network.** Multipath resilience covers the bidirectional edge sets you specify, or all eligible pairs when you leave the list empty.

## Multipath resilience concepts
<a name="cloudwan-multipath-resilience-concepts"></a>

The following table describes the concepts that apply to multipath resilience in an AWS Cloud WAN core network.


| Concept | Description | 
| --- | --- | 
| Enabled / Disabled | In the console, multipath resilience is shown as simply **enabled** or **disabled**. When enabled, packet replication covers all eligible edge sets by default; if `edge-sets` is set in the policy JSON, replication covers only those pairs. | 
| Edge set | A bidirectional pair of core network edge locations. Specifying edge sets scopes coverage and billing to just those routes. The order of the two locations in a pair does not matter; `[us-east-1, us-east-2]` covers both directions. Each Region in a pair must already be an edge location in the core network's policy and must be in one of the multipath resilience supported Regions (US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), and Europe (Ireland)); unsupported pairs are rejected at policy validation time. | 

The following JSON block enables multipath resilience for all eligible edge sets in the core network:

```json
"core-network-configuration": {
  "multipath-resilience": {
    "mode": "best-effort"
  }
}
```

The following JSON block enables multipath resilience and scopes coverage to specific edge sets:

```json
"core-network-configuration": {
  "multipath-resilience": {
    "mode": "best-effort",
    "edge-sets": [
      {
        "edge-locations": [
          "us-east-1", 
          "us-east-2"
        ]
      },
      {
        "edge-locations": [
          "us-west-2", 
          "eu-west-1"
        ]
      }
    ]
  }
}
```

## View the multipath resilience configuration for a policy version
<a name="cloudwan-view-multipath-resilience"></a>

You can view the multipath resilience status and the covered edge sets for any core network policy version.

**To view the multipath resilience configuration for a policy version using the console**

1. Open the [AWS Network Manager console](https://console.aws.amazon.com/networkmanager/home).

1. In the navigation pane, choose **Global networks**, and then choose the global network.

1. Choose **Core network**, and then choose **Policy versions**.

1. Choose the policy version ID to open its detail page.

1. On the **Policy details** tab, under **Network configuration**, choose the **Multipath resilience** sub-tab.

1. Review the multipath resilience status and edge sets.
   + **Status**: **Enabled** or **Disabled**.
   + **Edge sets**: a bordered table of each bidirectional pair, displayed as **Location 1** and **Location 2**. The table is empty when the policy covers all eligible pairs.

1. To view the raw policy document and the `multipath-resilience` block, choose the **JSON** tab.

To monitor the replicated traffic between covered edge locations, use the multipath resilience CloudWatch metrics. For more information, see [Cloud WAN multipath resilience metrics](cloudwan-metrics.md#cloudwan-metrics-multipath-resilience).

## Enable multipath resilience in a new core network policy version
<a name="cloudwan-enable-multipath-resilience"></a>

A core network policy is immutable. To enable multipath resilience, create a new policy version from scratch or copy from an existing version, add the configuration, and apply the new version to the core network.

The core network must already have edge locations configured in supported AWS Regions.

**To enable multipath resilience in a new policy version using the visual editor**

1. Start a new core network policy version using the visual editor. For instructions on creating a policy version, see [Create an AWS Cloud WAN core network policy version using the console](cloudwan-create-policy-console.md).

1. In the visual editor, choose the **Multipath resilience** tab.

1. Select **Enable multipath resilience**.

1. (Optional) Under **Edge sets - optional**, add pairs to scope coverage and reduce replication charges. Choose the **Info** link to open the help panel.

   1. Choose **Add edge set**.

   1. In the row, select **Location 1** and **Location 2**. The pair is bidirectional; the order of the two locations does not matter.

   1. Repeat for additional pairs. To delete a row, choose **Remove**.

   Leaving the list empty applies multipath resilience to all eligible edge sets in the core network.

1. Switch to the **JSON** tab if you want to confirm the generated `multipath-resilience` block in the raw policy document.

1. Choose **Create policy**. The new version is saved to the core network as a non-LIVE version with **Change set state** **Pending generation**.

1. After the change set finishes generating, apply the new version to the core network to make it **LIVE**. Multipath resilience activates only after the new version is live. For the steps to deploy a policy change set, see [Deploy an AWS Cloud WAN core network policy version](cloudwan-policy-version-deploy.md).

To enable multipath resilience directly in a JSON policy, add the `multipath-resilience` block as shown in [Multipath resilience concepts](#cloudwan-multipath-resilience-concepts), and then create the policy version using the JSON editor. For general guidance on creating policy versions, see [Create an AWS Cloud WAN core network policy version using JSON](cloudwan-create-policy-json.md).

**Note**  
All Regions you choose for a pair must already be edge locations in the core network's configuration and must be in the multipath resilience supported Regions (US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), and Europe (Ireland)). Unsupported pairs are rejected at policy validation time.