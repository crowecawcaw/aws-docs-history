

# Manage the associations for a VPC Lattice service network

When you associate a service or a resource configuration with the service network, it enables clients in VPCs connected to the service network, to make requests to the service and resource configuration. When you connect a VPC with the service network, it enables all the targets within that VPC to be clients and communicate with other services and resource configurations in the service network.

 The private DNS enabled property of the service network resource association overrides the private DNS enabled property of the service network endpoint and the service network VPC association. 

If a service network owner creates a service network resource association and doesn't enable private DNS, VPC Lattice won't provision private hosted zones for that resource configuration in any VPCs that the service network is connected to, even though private DNS is enabled on the service network endpoint or service network VPC associations. 

**Topics**
+ [Manage service network service associations](#service-network-service-associations)
+ [Manage service network resource associations](#service-network-resource-config-associations)
+ [Manage service network VPC associations](#service-network-vpc-associations)
+ [Manage service network VPC endpoint associations](#service-network-vpc-endpoint-associations)

## Manage service network service associations
<a name="service-network-service-associations"></a>

You can associate services that reside in your account or services that are shared with you from different accounts. This is an optional step while creating a service network. However, a service network is not fully functional until you associate a service. Service owners can associate their services to a service network if their account has the required access. For more information, see [Identity-based policy examples for VPC Lattice](security_iam_id-based-policies.md#security_iam_id-based-policy-examples).

When you delete a service association, the service can no longer connect to other services in the service network.

**To manage service associations using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, under **VPC Lattice**, choose **Service networks**.

1. Select the name of the service network to open its details page.

1. Choose the **Service associations** tab.

1. To create an association, do the following:

   1. Choose **Create associations**.

   1. Select a service from **Services**. To create a service, choose **Create an Amazon VPC Lattice service**.

   1. (Optional) To add a tag, expand **Service association tags**, choose **Add new tag**, and enter a tag key and tag value.

   1. Choose **Save changes**.

1. To delete an association, select the check box for the association and then choose **Actions**, **Delete service associations**. When prompted for confirmation, enter **confirm** and then choose **Delete**.

**To create a service association using the AWS CLI**  
Use the [create-service-network-service-association](https://docs.aws.amazon.com/cli/latest/reference/vpc-lattice/create-service-network-service-association.html) command.

**To delete a service association using the AWS CLI**  
Use the [delete-service-network-service-association](https://docs.aws.amazon.com/cli/latest/reference/vpc-lattice/delete-service-network-service-association.html) command.

## Manage service network resource associations
<a name="service-network-resource-config-associations"></a>

A resource configuration is a logical object that represents either a single resource or a group of resources. You can associate resource configurations that reside in your account or resource configurations that are shared with you from different accounts. This is an optional step while creating a service network. Resource configuration owners can associate their resource configurations to a service network if their account has the required access. For more information, see [Identity-based policy examples for VPC Lattice](https://docs.aws.amazon.com/vpc-lattice/latest/ug/security_iam_id-based-policies.html#security_iam_id-based-policy-examples).

### Manage associations between service networks and resource configurations
<a name="service-network-resource-config-association-manage"></a>

You can create or delete the association between the service network and resource configuration.

**To manage resource configuration associations using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, under **PrivateLink and Lattice**, choose **Service networks**.

1. Select the name of the service network to open its details page.

1. Choose the **Resource configuration associations** tab.

1. To create an association, do the following:

   1. Choose **Create associations**.

   1. For **Resource configurations**, select a resource configuration.

   1. For **DNS name**, select **Private DNS enabled** to allow VPC Lattice to provision a private hosted zone for your resource configuration associations based on the domain name of the resource configuration.

   1. (Optional) To add a tag, expand **Service association tags**, choose **Add new tag**, and enter a tag key and tag value.

   1. Choose **Save changes**.

1. To delete an association, select the check box for the association and then choose **Actions**, **Delete**. When prompted for confirmation, enter **confirm** and then choose **Delete**.

**To create a resource configuration association using the AWS CLI**  
Use the [create-service-network-resource-association](https://docs.aws.amazon.com/cli/latest/reference/vpc-lattice/create-service-network-resource-association.html) command.

**To delete a resource configuration association using the AWS CLI**  
Use the [delete-service-network-resource-association](https://docs.aws.amazon.com/cli/latest/reference/vpc-lattice/delete-service-network-resource-association.html) command.

### Monitor resource configuration associations
<a name="monitor-resource-config-associations"></a>

VPC Lattice publishes Amazon CloudWatch metrics for each service network resource association to the account that owns the resource gateway, using the `Service Network Resource Association Id` dimension. For more information, see [Resource gateway and resource configuration metrics](monitoring-cloudwatch.md#resource-gateway-resource-configuration-metrics).

## Manage service network VPC associations
<a name="service-network-vpc-associations"></a>

Clients can send requests to services and resources specified in resource configurations associated with a service network if the client is in VPCs associated with the service network. Client traffic that traverses a VPC peering connection or a transit gateway is only allowed through a service network using a VPC endpoint of type service network.

Associating a VPC is an optional step when you create a service network. Network owners can associate VPCs to a service network if their account has the required access. For more information, see [Identity-based policy examples for VPC Lattice](security_iam_id-based-policies.md#security_iam_id-based-policy-examples).

When you create or update a VPC association, you can specify the private DNS preference. This preference allows VPC Lattice to provision private hosted zones on the resource consumer's behalf. For more information, see [Custom domain names for resource consumers](resource-configuration.md#custom-domain-name-resource-consumers).

When you delete a VPC association, clients in the VPCs can no longer connect to services in the service network.

**To manage VPC associations using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, under **VPC Lattice**, choose **Service networks**.

1. Select the name of the service network to open its details page.

1. Choose the **VPC associations** tab.

1. To create a VPC association, do the following:

   1. Choose **Create VPC associations**.

   1. Choose **Add VPC association**.

   1. Select a VPC from **VPC** and select up to five security groups from **Security groups**. To create a security group, choose **Create new security group**.

   1. (Optional) To allow VPC Lattice to provision a private hosted zone based on the domain name of a resource configuration, for **DNS name**, select **Enable DNS name** and do the following:

      1. For **Private DNS preference**, select a preference.

         If you choose **All domains**, VPC Lattice provisions a private hosted zone for any custom domain name for a resource configuration.

      1. (Optional) If you choose **Verified and specified domains** or **Specified domains**, enter a comma separated list of domains that you want VPC Lattice to provision hosted zones for. VPC Lattice only provisions a hosted zone if it matches your private domains list. You can use wildcard matching.

   1. (Optional) To add a tag, expand **VPC association tags**, choose **Add new tag**, and enter a tag key and tag value.

   1. Choose **Save changes**.

1. To edit the security groups for an association, select the check box for the association and then choose **Actions**, **Edit security groups**. Add and remove security groups as needed.

1. To delete an association, select the check box for the association and then choose **Actions**, **Delete VPC associations**. When prompted for confirmation, enter **confirm** and then choose **Delete**.

**To create a VPC association using the AWS CLI**  
Use the [create-service-network-vpc-association](https://docs.aws.amazon.com/cli/latest/reference/vpc-lattice/create-service-network-vpc-association.html) command.

**To update the security groups or private DNS settings for a VPC association using the AWS CLI**  
Use the [update-service-network-vpc-association](https://docs.aws.amazon.com/cli/latest/reference/vpc-lattice/update-service-network-vpc-association.html) command.

The following example changes the private DNS preference so that VPC Lattice provisions private hosted zones only for domains that match `*.example.com`. When you specify `--dns-options`, also specify `--private-dns-enabled` and every DNS option that you want to keep. Options that you omit are reset to their defaults.

```
aws vpc-lattice update-service-network-vpc-association \
  --service-network-vpc-association-identifier snva-0123456789abcdef0 \
  --private-dns-enabled \
  --dns-options '{"privateDnsPreference":"SPECIFIED_DOMAINS_ONLY","privateDnsSpecifiedDomains":["*.example.com"]}'
```

The following example disables private DNS for a VPC association. Resource configurations connected after this change don't get private DNS records in the VPC. Existing records stay until the resource configuration is disconnected or the VPC association is deleted.

```
aws vpc-lattice update-service-network-vpc-association \
  --service-network-vpc-association-identifier snva-0123456789abcdef0 \
  --no-private-dns-enabled
```

**To delete a VPC association using the AWS CLI**  
Use the [delete-service-network-vpc-association](https://docs.aws.amazon.com/cli/latest/reference/vpc-lattice/delete-service-network-vpc-association.html) command.

For how resource VPC endpoints, service-network VPC endpoints, and service network VPC associations differ when you update them, see [Differences between connection types](resource-configuration.md#differences-between-connection-types).

### Monitor VPC associations
<a name="monitor-vpc-associations"></a>

VPC Lattice publishes Amazon CloudWatch metrics for traffic from a VPC association to resource configurations in the service network, using the `Service Network VPC Association Id` dimension. You can also view these metrics in the Amazon VPC console: under **VPC Lattice**, choose **Service networks**, select the service network, choose the **VPC associations** tab, and select the association. For more information, see [Resource consumer metrics](monitoring-cloudwatch.md#resource-consumer-metrics).

## Manage service network VPC endpoint associations
<a name="service-network-vpc-endpoint-associations"></a>

Clients can send requests to services and resources specified in resource configurations over a VPC endpoint (powered by AWS PrivateLink) in their VPC. A VPC endpoint of type *service network* connects a VPC to a service network. Client traffic that comes from outside the VPC over a VPC peering connection, Transit Gateway, Direct Connect, or VPN can use the VPC endpoint to reach services and resource configurations. With VPC endpoints, you can connect a VPC to multiple service networks. When you create a VPC endpoint in a VPC, IP addresses from the VPC (and not IP addresses from the [managed prefix list](security-groups.md#managed-prefix-list)) are used to establish connectivity to the service network.

When you create or update a service-network VPC endpoint, you can specify the private DNS preference. This preference allows VPC Lattice to provision private hosted zones on the resource consumer's behalf. To update an existing service-network VPC endpoint, use the `modify-vpc-endpoint` command. For more information, see [Custom domain names for resource consumers](resource-configuration.md#custom-domain-name-resource-consumers).

**To manage VPC endpoint associations using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, under **VPC Lattice**, choose **Service networks**.

1. Select the name of the service network to open its details page.

1. Choose the **Endpoint associations** tab to view the VPC endpoints connected to your service network.

1. Select the Endpoint ID of the VPC endpoint to open its details page. Then modify or delete the VPC endpoint association.

**To create a new VPC endpoint association using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, under **VPC Lattice**, choose **Endpoints**.

1. Choose **Create endpoints**.

1. For **Type**, choose **Service networks**.

1. Select the service network you want to connect to your VPC.

1. Select the VPC, subnets and security groups.

1. (Optional) To enable private DNS, choose **Enable private DNS**.

1. (Optional) To add a tag, expand **VPC association tags**, choose **Add new tag**, and enter a tag key and tag value.

1. Choose **Create endpoint**.

To learn more about how to use a VPC endpoint to connect to service networks, see [Access service networks](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-service-networks.html) in the *AWS PrivateLink user guide*.

For how resource VPC endpoints, service-network VPC endpoints, and service network VPC associations differ when you update them, see [Differences between connection types](resource-configuration.md#differences-between-connection-types).

### Monitor VPC endpoint associations
<a name="monitor-vpc-endpoint-associations"></a>

VPC Lattice publishes Amazon CloudWatch metrics for traffic from a service-network VPC endpoint to resource configurations in the service network, using the `VPC Endpoint Id` dimension. For more information, see [Resource consumer metrics](monitoring-cloudwatch.md#resource-consumer-metrics).