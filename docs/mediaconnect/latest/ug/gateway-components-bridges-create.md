# Creating a MediaConnect Gateway bridge

After you have registered at least one instance to your gateway, you can create a
bridge. The process for creating a bridge will vary depending on the bridge type you
select.

###### Contents

- [Prerequisites](gateway-components-bridges-create.md#gateway-components-bridges-create-prerequisites "gateway-components-bridges-create.md#gateway-components-bridges-create-prerequisites")
- [Procedure](gateway-components-bridges-create.md#gateway-components-bridges-create-procedure "gateway-components-bridges-create.md#gateway-components-bridges-create-procedure")
- [Next
  steps](gateway-components-bridges-create.md#gateway-components-bridges-create-next-steps "gateway-components-bridges-create.md#gateway-components-bridges-create-next-steps")
  - [Starting a bridge](gateway-components-bridges-create.md#gateway-components-bridges-create-next-steps-start-bridge "gateway-components-bridges-create.md#gateway-components-bridges-create-next-steps-start-bridge")
  - [Updating a bridge](gateway-components-bridges-create.md#gateway-components-bridges-create-next-steps-update-bridge "gateway-components-bridges-create.md#gateway-components-bridges-create-next-steps-update-bridge")

## Prerequisites

- The following procedure assumes that you have previously created a
  gateway and registered an instance to it.
- Before creating a bridge, you will need to collect the details of the
  bridge you want to create.
- If you're creating an ingress bridge and you want to use
  source-specific multicast (SSM), verify your network capability and
  ensure that your network infrastructure (routers and switches) supports
  SSM. The multicast source IP that you use must be a valid IPv4 address.

## Procedure

After you have registered at least one instance to your gateway,
you can create a bridge. The process for creating a bridge will vary
depending on the bridge type you select. There are two bridge types:
ingress (a ground-to-cloud bridge) or egress (a cloud-to-ground
bridge).

Console

###### To create an ingress bridge

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").
2. From the navigation pane, select
   **Gateways**.
3. In the **Gateways** section, select the
   gateway you want to create the bridge on.
4. On the gateway **Details** page, select
   the **Bridges** tab.
5. Select **Create bridge**.
6. On the **Create bridge** page, complete
   the following steps in the **Details**
   section:
   1. Enter a **Name** for the bridge.
   2. For **Bridge type**, select
      **Ingress bridge**.
   3. Enter the **Maximum bitrate** for
      the content you will transport over the
      bridge.
   4. Enter the **Maximum outputs** for
      the bridge.

7. Next, complete the following steps in the
   **Sources** section. The source of an
   ingress bridge is multicast content that originates at your
   premises:
   1. Enter a **Name** for the bridge
      source.
   2. Select a **Network**. This is a
      network you created during the gateway setup
      process.
   3. Select the **Protocol** for this
      source.
   4. Enter the **Multicast IP**
      address.
   5. (Optional) If you want to use source-specific
      multicast (SSM), enter the **Multicast
      Source IP** address. The multicast source
      IP that you enter must be a valid IPv4 address. If
      you don't enter a value here, the bridge source will
      use Any-Source Multicast (ASM) mode.
   6. Enter the **Port** of the
      source.

8. If you add more than one source, you can set up failover
   using the **Failover configuration**
   section.
   1. Select the **Failover mode**:
      **Failover** or
      **Merge**.
   2. (Optional) If you select
      **Failover** as the mode, you can
      select one of the sources you previously configured
      to be the **Primary source**. If
      you don't select a **Primary
      source**, MediaConnect will select one at
      random.

9. Choose **Create bridge**.
10. After the bridge is created, you can start the bridge by
    selecting **Start** on the bridge's
    **Details** page.

###### To create an egress bridge

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").
2. From the navigation pane, select
   **Gateways**.
3. In the **Gateways** section, select the
   gateway you want to create the bridge on.
4. On the gateway's **Details** page, select
   the **Bridges** tab.
5. Choose **Create bridge**.
6. On the **Create bridge** page, complete
   the following steps in the **Details**
   section:
   1. Enter a **Name** for the bridge.
   2. Select a **Bridge type** of
      **Egress bridge**.
   3. Enter the **Maximum bitrate** for
      the content you will transport over the
      bridge.

7. Complete the following steps in the
   **Sources** section:
   1. Enter a **Name** for the bridge
      source. For an Egress bridge, the source is the
      content coming from a MediaConnect flow and delivered to
      your premises.
   2. Select a **Network**. This is a
      network you created during the gateway setup
      process.
   3. Select the **Flow ARN**. This is
      the ARN of the MediaConnect flow that you will use as a
      source.
   4. If this flow uses a **VPC
      interface**, select it.

8. If you add more than one source, you can set up failover
   using the **Failover configuration**
   section.
   1. When you select an egress bridge, the only
      available **Failover mode** is
      **Failover**.
      **Merge** cannot be
      selected.
   2. (Optional) Select one of the sources that you
      previously created to be the **Primary
      source**. If you don't select a
      **Primary source**, MediaConnect will
      select one at random.

9. Under **Outputs**, complete the following
   steps.
   1. Enter a **Name** for the bridge
      output.
   2. Select a **Network**. This is a
      network that you created during the MediaConnect Gateway setup
      process.
   3. Select a transport **Protocol**
      for the output.
   4. Enter an **IP address** for the
      output. This must be an IP that is compatible with
      your local network.
   5. Enter the **Port** for the
      output. This must be a port that is compatible with
      your local network.
   6. Enter a **TTL** (time-to-live)
      for the output.

10. Select **Create bridge**.
11. After the bridge is created, you can start the bridge by
    selecting **Start** on the bridge details
    page.

AWS CLI

###### To create a bridge using the AWS CLI

1. Find the details of the bridge you want to create. These
   details will be stored in a JSON file on the computer
   running the AWS CLI. The JSON file should be named
   `bridge.json`. The following examples show
   the correct sections and formatting for the JSON file.

Here is an example for creating an egress bridge:

```
{
    "Name": "bridge",
    "PlacementArn": "`arn:aws:mediaconnect:us-west-2:111122223333:gateway:1-23aBC45dEF67hiJ8-12AbC34DE5fG:gateway`",
    "EgressGatewayBridge": {
        "MaxBitrate": `100000000`
    },
    "SourceFailoverConfig": {
        "FailoverMode": "`FAILOVER`",
        "State": "`ACTIVE`"
    },
    "Sources": [
        {
            "FlowSource": {
                "Name": "`Source0`",
                "FlowArn": "`arn:aws:mediaconnect:us-west-2:111122223333:flow:1-UAECXlABCQJeVwMB-95ec11ac6059:gatewayFlow`",
                "NetworkName": "`blue`"
            }
        },
        {
            "FlowSource": {
                "Name": "`Source1`",
                "FlowArn": "`arn:aws:mediaconnect:us-west-2:111122223333:flow:1-ECRZVGADYMGtPGTM-c1iPQ5FNL7Qn:gatewayFlow`",
                "NetworkName": "`blue`",
                "FlowVpcInterfaceAttachment": {
                    "VpcInterfaceName": "`VPCIF`"
                }
            }
        }
    ],
    "Outputs": [
        {
            "NetworkOutput": {
                "Name": "`Output0`",
                "NetworkName": "`blue`",
                "IpAddress": "`225.1.2.3`",
                "Port": `5010`,
                "Protocol": "`rtp-fec`",
                "Ttl": `8`
            }
        },
        {
            "NetworkOutput": {
                "Name": "`Output1`",
                "NetworkName": "`blue`",
                "IpAddress": "`225.1.2.4`",
                "Port": `6010`,
                "Protocol": "`rtp`",
                "Ttl": `250`
            }
        }
    ]
}
```

Here is an example for creating an ingress bridge that
supports SSM (`MulticastSourceSettings` and
`MulticastSourceIp` are defined in the
source):

```
{
      "Name": "bridge",
      "PlacementArn": "`arn:aws:mediaconnect:us-west-2:111122223333:gateway:1-23aBC45dEF67hiJ8-12AbC34DE5fG:gateway`",
      "IngressGatewayBridge": {
          "MaxBitrate": 80000000,
          "MaxOutputs": 1
      },
      "SourceFailoverConfig": {
          "FailoverMode": "FAILOVER",
          "SourcePriority": {
              "PrimarySource": "`network-source1`"
          },
          "State": "ENABLED"
      },
      "Sources": [
          {
              "NetworkSource": {
                  "MulticastIp": "`224.0.0.1`",
                  "MulticastSourceSettings": {
                    "MulticastSourceIp": "`1.2.3.4`"
                  },
                  "Name": "`network-source1`",
                  "NetworkName": "`network-1`",
                  "Port": `5001`,
                  "Protocol": "`rtp`"
              }
          },
          {
              "NetworkSource": {
                  "MulticastIp": "`224.0.0.2`",
                  "MulticastSourceSettings": {
                    "MulticastSourceIp": "`4.3.2.1`"
                  },
                  "Name": "`network-source2`",
                  "NetworkName": "`network-1`",
                  "Port": `5001`,
                  "Protocol": "`rtp`"
              }
          }
      ]
  }
```

2. Enter the following command into the AWS CLI interface.
   Replace the `<yourprofile>` and
   `<region>` values with your
   desired profile and AWS Region.

```
aws --profile `<yourprofile>` --region `<region>` mediaconnect create-bridge
      --cli-input-json file://bridge.json
```

3. The AWS CLI will return a response like the following
   example.

```
{
    "Bridge": {
        "BridgeArn": "arn:aws:mediaconnect:us-west-2:111122223333:bridge:1-GLxlBRLrHzzvpwyb-1dd82066b207:bridge",
        "BridgeMessages": [],
        "BridgeState": "STANDBY",
        "EgressGatewayBridge": {
            "MaxBitrate": 100000000
        },
        "Name": "bridge",
        "Outputs": [
            {
                "NetworkOutput": {
                    "IpAddress": "225.1.2.3",
                    "Name": "Output0",
                    "NetworkName": "blue",
                    "Port": 5010,
                    "Protocol": "rtp-fec",
                    "Ttl": 8
                }
            },
            {
                "NetworkOutput": {
                    "IpAddress": "225.1.2.4",
                    "Name": "Output1",
                    "NetworkName": "blue",
                    "Port": 6010,
                    "Protocol": "rtp",
                    "Ttl": 250
                }
            }
        ],
        "PlacementArn": "arn:aws:mediaconnect:us-west-2:111122223333:gateway:1-23aBC45dEF67hiJ8-12AbC34DE5fG:gateway",
        "SourceFailoverConfig": {
            "FailoverMode": "FAILOVER",
            "State": "ENABLED"
        },
        "Sources": [
            {
                "FlowSource": {
                    "FlowArn": "arn:aws:mediaconnect:us-west-2:111122223333:flow:1-UAECXlABCQJeVwMB-95ec11ac6059:gatewayFlow",
                    "Name": "Source0",
                    "NetworkName": "blue"
                }
            },
            {
                "FlowSource": {
                    "FlowArn": "arn:aws:mediaconnect:us-west-2:111122223333:flow:1-ECRZVGADYMGtPGTM-c1iPQ5FNL7Qn:gatewayFlow",
                    "Name": "Source1",
                    "NetworkName": "blue",
                    "FlowVpcInterfaceAttachment": {
                        "VpcInterfaceName": "VPCIF"
                    }
                }
            }
        ]
    }
}
```

## Next

steps

### Starting a bridge

After the bridge is created, you can start the bridge by choosing
`Start` on the bridge's details page.

### Updating a bridge

When updating an existing bridge source to use SSM, keep these key points in
mind:

1. **Bridge state requirements**: The bridge
   must be in `STANDBY` state before you make any changes.
2. **Enabling SSM**: To enable SSM, add a
   multicast source IP to the ingress bridge configuration. After you start
   the bridge, it will use the new SSM configuration and only accept
   multicast traffic from the specified source IP.
3. **Reverting to ASM**: To switch back to
   Any-Source Multicast (ASM) mode, remove the multicast source IP from the
   ingress bridge configuration. Remember, this can only be done when the
   bridge is in `STANDBY` state.
4. **Applying changes**: After you make your
   changes, you must start the bridge for the new configuration to take
   effect.
5. **Verifying bridge source information**:
   You can view the current state of your bridge sources (including the
   multicast source IP) by using the [DescribeBridge](../api/v1-bridges-bridgearn.md "../api/v1-bridges-bridgearn.md") API or checking the bridge details in the
   console.

By following these guidelines, you can successfully manage your bridge's
multicast settings, switching between SSM and ASM modes as needed.
