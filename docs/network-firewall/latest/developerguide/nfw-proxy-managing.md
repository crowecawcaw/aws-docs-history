

# Managing a NAT/Proxy firewall

You manage most settings of a NAT/Proxy firewall the same way as for any firewall. For information about managing firewalls, see [Managing a firewall and firewall endpoints in AWS Network Firewall](firewall-managing.md). This section describes the tasks that are specific to NAT/Proxy firewalls.

## Viewing the firewall's status
<a name="nfw-proxy-viewing"></a>

In the console, on the firewall's details page:
+ **NAT gateway associations** lists the NAT gateways that Network Firewall created. While a NAT gateway is still being created, the console shows **NAT gateway provisioning**.
+ The **Firewall endpoints** table lists each Availability Zone's firewall endpoint, along with its NAT gateway and NAT gateway status.
+ The **Endpoints and identity** section shows the proxy listeners, the proxy hostname, the custom hostname and certificate (if you set them), and whether NAT on non-proxy traffic is enabled.

In the [DescribeFirewall](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DescribeFirewall.html) response, `FirewallStatus` includes the following for each Availability Zone, under `SyncStates`:
+ `Attachment` – The firewall endpoint's subnet, endpoint ID, status, status message, and `DnsName` (the proxy hostname).
+ `NatGatewayAttachments` – The ID, status, and status message of the NAT gateway that Network Firewall created for the Availability Zone.

The firewall status is `READY` only when every Availability Zone's firewall endpoint and NAT gateway are ready.

## Adding an Availability Zone
<a name="nfw-proxy-adding-az"></a>

To run the firewall in another Availability Zone, add a firewall endpoint subnet and a NAT gateway for that Availability Zone together. Network Firewall creates the NAT gateway and the firewall endpoint, and the existing proxy hostname starts resolving in the new Availability Zone. The firewall's other Availability Zones keep working, and the firewall shows `PROVISIONING` until the new Availability Zone is ready.

Use the [AssociateSubnets](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_AssociateSubnets.html) operation with `SubnetMappings` for the new firewall endpoint subnet and `NatGatewayCreateMappings` for the new NAT gateway. The same subnet and IP address requirements apply as when you create the firewall. You can't add an Availability Zone that the firewall already runs in. Subnet change protection must be turned off.

```bash
aws network-firewall associate-subnets \
    --firewall-name my-proxy-firewall \
    --update-token {{update-token}} \
    --subnet-mappings SubnetId=subnet-0endpointc1example,IPAddressType=IPV4 \
    --nat-gateway-create-mappings 'SubnetId=subnet-0natc1example,AllocationIds=eipalloc-0c1example,PrivateIps=10.0.30.10'
```

If Network Firewall can't create the new Availability Zone's NAT gateway, only that Availability Zone shows a failed status. The firewall itself doesn't fail. To recover, remove the Availability Zone, fix the cause, and add it again.

## Removing an Availability Zone
<a name="nfw-proxy-removing-az"></a>

Use the [DisassociateSubnets](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DisassociateSubnets.html) operation with the Availability Zone's firewall endpoint subnet. Network Firewall stops sending traffic through that Availability Zone, removes the firewall endpoint and its DNS record, and detaches the NAT gateway. The NAT gateway keeps working as a regular NAT gateway. If you don't need it, delete it in the Amazon VPC console.
+ You can't remove the firewall's last Availability Zone. To remove it, delete the firewall.
+ If a VPC endpoint association exists in the Availability Zone, the request fails. Delete the VPC endpoint associations in that Availability Zone first.
+ Subnet change protection must be turned off.

## Changing the proxy listeners
<a name="nfw-proxy-updating-listeners"></a>

You can change the proxy listener ports without recreating the firewall. The change applies regardless of the state of the NAT gateways.

In the console, on the firewall's details page, in the **Endpoints and identity** section, choose **Edit**.

In the API, use [UpdateProxySettings](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_UpdateProxySettings.html). The `ProxySettings` that you provide replace the firewall's existing proxy settings. If the firewall uses a custom hostname, include the same `CertificateArn` and `DomainName` in every request. If you leave them out, the request fails.

## Using the proxy from other VPCs
<a name="nfw-proxy-vpc-endpoint-associations"></a>

To let clients in other VPCs use the proxy, create VPC endpoint associations for the firewall. You can create them in your account or, if the firewall is shared with them, in other accounts. For information about creating VPC endpoint associations and sharing firewalls, see [Creating a VPC endpoint association](creating-vpc-endpoint-association.md) and [Sharing Network Firewall resources](sharing.md).

For a NAT/Proxy firewall:
+ The association's Availability Zone must be one that the firewall already runs in. To serve a new Availability Zone, add it to the firewall first.
+ Each VPC can have at most one firewall endpoint for the firewall in each Availability Zone, counting the firewall's own endpoints.
+ The proxy hostname resolves in the associated VPC to that VPC's firewall endpoint, and traffic leaves through the firewall's NAT gateway in the same Availability Zone.
+ Network Firewall associates a Route 53 private hosted zone with the associated VPC using your credentials, so you must have permission to associate a private hosted zone with that VPC.
+ If a VPC that you associate with the firewall already has a private hosted zone with the firewall's proxy DNS name, the operation fails with a `ConflictingDomain` exception. This applies to the default proxy hostname as well as a custom hostname.

## Deleting a NAT/Proxy firewall
<a name="nfw-proxy-deleting"></a>

Before you delete the firewall, remove any VPC route table routes that point to its firewall endpoints, and delete its VPC endpoint associations. In the console, when you delete the firewall, select **Also delete the NAT gateways this firewall created** to delete the NAT gateways along with the firewall. If you leave this option cleared, the NAT gateways keep working as regular NAT gateways, and you must delete them separately in the Amazon VPC console. In the API, set `DeleteAssociatedNatGateways` to `true` in the [DeleteFirewall](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DeleteFirewall.html) request.

For more information, see [NAT gateways that Network Firewall creates for a NAT/Proxy firewall](nfw-proxy-nat-gateways.md) and [Deleting a firewall in AWS Network Firewall](deleting-firewall.md).