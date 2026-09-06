

# Managing prefix allocations for Direct Connect virtual interfaces
<a name="prefix-allocations"></a>

You can manage the number of inbound route prefixes allocated to each virtual interface on your Direct Connect connection. Use the AWS Management Console, AWS CLI, or AWS SDKs to view your connection's prefix pool, allocate prefixes to virtual interfaces, and adjust allocations as your routing needs change.

**Important**  
If the number of advertised prefixes on a virtual interface exceeds the allocated count, the BGP session on that virtual interface goes to an idle state (BGP DOWN). Ensure that your allocation is at least as large as the number of prefixes you plan to advertise.

## Prerequisites
<a name="prefix-allocations-prerequisites"></a>

Before you manage prefix allocations, ensure that you have the following:
+ An active Direct Connect dedicated connection or LAG.
+ At least one private or transit virtual interface.
+ Permissions to call Direct Connect APIs (`directconnect:DescribeConnections`, `directconnect:DescribeVirtualInterfaces`, `directconnect:DescribeDirectConnectGateways`, `directconnect:UpdateVirtualInterfaceAttributes`, `directconnect:CreatePrivateVirtualInterface`, `directconnect:CreateTransitVirtualInterface`).

## View your connection's prefix pool
<a name="prefix-allocations-view-pool"></a>

You can view the prefix pool for your connection to determine how many prefixes are available and how they are allocated across your virtual interfaces.

------
#### [ Console ]

**To view your connection's prefix pool**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Connections**.

1. Select your connection.

1. On the connection details page, locate the **Inbound prefixes** card.

1. Review the following values: **Pool size**, **Unallocated**, and **Allocated**. IPv4 and IPv6 values are shown separately.

------
#### [ Command line ]

Use the [describe-connections](https://docs.aws.amazon.com/cli/latest/reference/directconnect/describe-connections.html) command.

```
aws directconnect describe-connections \
    --connection-id {{dxcon-abc12345}}
```

In the response, check the following fields:
+ `prefixPoolSizeIpv4` and `prefixPoolSizeIpv6` — The total number of prefixes in the pool.
+ `prefixPoolUnallocatedCountIpv4` and `prefixPoolUnallocatedCountIpv6` — The number of prefixes that are not allocated to a virtual interface.

------

## Set the prefix allocation when creating a virtual interface
<a name="prefix-allocations-create-vif"></a>

You can set the prefix allocation for a virtual interface when you create it. This reserves a portion of the connection's prefix pool for the new virtual interface.

------
#### [ Console ]

**To set the prefix allocation when creating a virtual interface**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Virtual Interfaces**.

1. Choose **Create virtual interface**.

1. Configure the virtual interface settings, including the type, VLAN, and BGP ASN.

1. In the **Inbound prefix allocation** section, enter the number of IPv4 and IPv6 prefixes to allocate.

1. Choose **Create virtual interface**.

------
#### [ Command line ]

Use the [create-private-virtual-interface](https://docs.aws.amazon.com/cli/latest/reference/directconnect/create-private-virtual-interface.html) command. The following example creates a private virtual interface with prefix allocations.

```
aws directconnect create-private-virtual-interface \
    --connection-id {{dxcon-abc12345}} \
    --new-private-virtual-interface '{
        "virtualInterfaceName": "{{my-private-vif}}",
        "vlan": {{101}},
        "asn": {{65000}},
        "directConnectGatewayId": "{{d2113d06-a0d8-476b-91a7-8555d9973d12}}",
        "prefixPoolAllocatedCountIpv4": {{500}},
        "prefixPoolAllocatedCountIpv6": {{100}}
    }'
```

------

## Update the prefix allocation on an existing virtual interface
<a name="prefix-allocations-update"></a>

You can update the prefix allocation on an existing virtual interface to increase or decrease the number of prefixes reserved for that interface.

------
#### [ Console ]

**To update the prefix allocation on a virtual interface**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Virtual Interfaces**.

1. Select the virtual interface that you want to update.

1. Choose **Edit**.

1. Update the **IPv4 prefix allocation** value, the **IPv6 prefix allocation** value, or both.

1. Choose **Update virtual interface**.

------
#### [ Command line ]

Use the [update-virtual-interface-attributes](https://docs.aws.amazon.com/cli/latest/reference/directconnect/update-virtual-interface-attributes.html) command.

```
aws directconnect update-virtual-interface-attributes \
    --virtual-interface-id {{dxvif-abc12345}} \
    --prefix-pool-allocated-count-ipv4 {{500}} \
    --prefix-pool-allocated-count-ipv6 {{100}}
```

------

## View the Direct Connect gateway total prefix allocations
<a name="prefix-allocations-view-dxgw"></a>

You can view the total prefix allocations across all virtual interfaces attached to a Direct Connect gateway.

------
#### [ Console ]

**To view the Direct Connect gateway total prefix allocations**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Direct Connect Gateways**.

1. Select your gateway.

1. On the gateway details page, review the **Total prefix pool allocations** value.

------
#### [ Command line ]

Use the [describe-direct-connect-gateways](https://docs.aws.amazon.com/cli/latest/reference/directconnect/describe-direct-connect-gateways.html) command.

```
aws directconnect describe-direct-connect-gateways \
    --direct-connect-gateway-id {{d2113d06-a0d8-476b-91a7-8555d9973d12}}
```

In the response, check the `totalPrefixPoolAllocations` field.

------

## Verify the allocation change
<a name="prefix-allocations-expected-results"></a>

After you update a prefix allocation, the new value takes effect immediately. The BGP session remains up as long as the number of advertised prefixes does not exceed the new allocation. The API rejects requests to reduce an allocation below the number of prefixes currently in use on the VIF.

## Troubleshooting
<a name="prefix-allocations-troubleshooting"></a>

The following are common issues that you might encounter when managing prefix allocations.

BGP session goes down after adding prefixes  
The number of advertised prefixes exceeded the allocated count. Increase the allocation by using the `UpdateVirtualInterfaceAttributes` API or the console.

Cannot decrease allocation  
You cannot reduce a VIF's allocated value below the number of prefixes currently in use. First reduce the number of prefixes advertised by your on-premises device, then reduce the allocation.

Cannot increase allocation  
The connection's prefix pool might be fully allocated. Check the `prefixPoolUnallocatedCountIpv4` and `prefixPoolUnallocatedCountIpv6` values on the connection. You might need to reduce allocations on other virtual interfaces first.

Direct Connect gateway total exceeds 10,000  
The sum of all combined IPv4 and IPv6 allocations across virtual interfaces attached to a single Direct Connect gateway cannot exceed 10,000. Reduce allocations on other virtual interfaces or use a second gateway.