

# Onboarding your transit gateway to a context store

You configure context sharing in AWS Network Manager, on the network side, not on the network firewall. It's a one-time setup for each transit gateway. A global network can have one context store, and you associate the store with transit gateways only. The following steps summarize the setup; for the full procedures, see [Context sharing with security services](https://docs.aws.amazon.com/network-manager/latest/tgwnm/context-stores.html) in the *AWS Global Networks for Transit Gateways User Guide*.

**To create a context store and associate it with your transit gateway**

1. Open the AWS Network Manager console at [https://console.aws.amazon.com/networkmanager/home#/networks](https://console.aws.amazon.com/networkmanager/home#/networks).

1. Choose a global network, or choose **Create global network** to create one. The **Context store** column of the global networks list shows whether a global network already has a store. For more information, see [Global networks](https://docs.aws.amazon.com/network-manager/latest/tgwnm/global-networks.html) in the *AWS Global Networks for Transit Gateways User Guide*.

1. Register the transit gateway that your network firewall is attached to with the global network, and wait for the registration to become **Available**. For instructions, see [Transit gateway registrations](https://docs.aws.amazon.com/network-manager/latest/tgwnm/tgw-registrations.html) in the *AWS Global Networks for Transit Gateways User Guide*.

1. In the navigation pane for the global network, choose **Context store**, choose **Create context store**, and under **Create associations** select the registered transit gateways to share context for. The store's **Status** shows **Pending** and then **Available**. For the full procedure, see [Create a context store](https://docs.aws.amazon.com/network-manager/latest/tgwnm/create-context-store.html) in the *AWS Global Networks for Transit Gateways User Guide*.

1. To associate another transit gateway later, use the store's **Associations** tab. The **Association state** shows **Associating** and then **Associated**, which typically takes minutes. For the full procedure, see [Associate a transit gateway with a context store](https://docs.aws.amazon.com/network-manager/latest/tgwnm/associate-context-store.html) in the *AWS Global Networks for Transit Gateways User Guide*.

After the association, the context store tracks the resources behind the transit gateway, and traffic that flows through the transit gateway carries the context of its source.

After the AWS Network Manager steps are complete, in the account that owns the context store, create an IAM role that grants Network Firewall read access to the store. Network Firewall assumes a role with a fixed name and a fixed set of permissions: the role must be named exactly `NetworkFirewallContextStoreReadOnly`. You create it once per store owner account. It covers every context store in the account.

**Important**  
Without this role, the network firewall can't sync with the context store, and context-aware rules match no traffic.

Create the role with the following trust policy, which allows the Network Firewall service principal to assume it:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "network-firewall.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

Attach the following permissions policy to the role:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "networkmanager:GetContextStoreAssociation",
                "networkmanager:GetContextVersion",
                "networkmanager:ListContexts",
                "networkmanager:ListContextChanges"
            ],
            "Resource": "*"
        }
    ]
}
```

On the network firewall side, there's nothing to configure: Network Firewall automatically discovers the context store associated with your firewall's transit gateway, typically within minutes of the association. To confirm the discovery, open the firewall's details page in the Network Firewall console and check the **Context store sync state** section. It shows the context store ID and owner account. Or call `DescribeFirewall` and check that the `ContextStoreId` and `ContextStoreOwnerAccountId` fields in the `Firewall` object are populated:

```sh
aws network-firewall describe-firewall --firewall-name example-firewall
```