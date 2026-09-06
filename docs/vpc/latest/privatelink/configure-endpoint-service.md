

# Configure an endpoint service
<a name="configure-endpoint-service"></a>

After you create an endpoint service, you can update its configuration.

**Topics**
+ [Manage permissions](#add-remove-permissions)
+ [Accept or reject connection requests](#accept-reject-connection-requests)
+ [Manage load balancers](#associate-load-balancer)
+ [Associate a private DNS name](#associate-private-dns-name)
+ [Modify the supported Regions](#manage-supported-regions)
+ [Modify the supported IP address types](#supported-ip-address-types)
+ [Manage tags](#add-remove-endpoint-service-tags)

## Manage permissions
<a name="add-remove-permissions"></a>

The combination of permissions and acceptance settings help you control which service consumers (AWS principals) can access your endpoint service. For example, you can grant permissions to specific principals that you trust and automatically accept all connection requests, or you can grant permissions to a wider group of principals and manually accept specific connection requests that you trust.

By default, your endpoint service is not available to service consumers. You must add permissions that allow specific AWS principals to create an interface VPC endpoint to connect to your endpoint service. To add permissions for an AWS principal, you need its Amazon Resource Name (ARN). The following list includes example ARNs for supported AWS principals.ARNs for AWS principals

AWS account (includes all principals in the account)  
arn:aws:iam::{{account\_id}}:root

Role  
 arn:aws:iam::{{account\_id}}:role/{{role\_name}}

User  
arn:aws:iam::{{account\_id}}:user/{{user\_name}}

All principals in all AWS accounts  
\*

**Considerations**
+ If you grant everyone permission to access the endpoint service and configure the endpoint service to accept all requests, your load balancer will be public even if it has no public IP address.
+ If you remove permissions, it does not affect existing connections between the endpoint and the service that were previously accepted.

**To manage permissions for your endpoint service using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Endpoint services**.

1. Select the endpoint service and choose the **Allow principals** tab.

1. To add permissions, choose **Allow principals**. For **Principals to add**, enter the ARN of the principal. To add another principal, choose **Add principal**. When you are finished adding principals, choose **Allow principals**.

1. To remove permissions, select the principal and choose **Actions**, **Delete**. When prompted for confirmation, enter **delete** and then choose **Delete**.

**To add permissions for your endpoint service using the command line**
+ [modify-vpc-endpoint-service-permissions](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-vpc-endpoint-service-permissions.html) (AWS CLI)
+ [Edit-EC2EndpointServicePermission](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-EC2EndpointServicePermission.html) (Tools for Windows PowerShell)

## Accept or reject connection requests
<a name="accept-reject-connection-requests"></a>

The combination of permissions and acceptance settings help you control which service consumers (AWS principals) can access your endpoint service. For example, you can grant permissions to specific principals that you trust and automatically accept all connection requests, or you can grant permissions to a wider group of principals and manually accept specific connection requests that you trust.

You can configure your endpoint service to accept connection requests automatically. Otherwise, you must accept or reject them manually. If you do not accept a connection request, the service consumer can't access your endpoint service.

If you grant everyone permission to access the endpoint service and configure the endpoint service to accept all requests, your load balancer will be public even if it has no public IP address.

You can receive a notification when a connection request is accepted or rejected. For more information, see [Receive alerts for endpoint service events](create-notification-endpoint-service.md).

**To modify the acceptance setting using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Endpoint services**.

1. Select the endpoint service.

1. Choose **Actions**, **Modify endpoint acceptance setting**.

1. Select or clear **Acceptance required**.

1. Choose **Save changes**

**To modify the acceptance setting using the command line**
+ [modify-vpc-endpoint-service-configuration](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-vpc-endpoint-service-configuration.html) (AWS CLI)
+ [Edit-EC2VpcEndpointServiceConfiguration](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-EC2VpcEndpointServiceConfiguration.html) (Tools for Windows PowerShell)

**To accept or reject a connection request using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Endpoint services**.

1. Select the endpoint service.

1. From the **Endpoint connections** tab, select the endpoint connection.

1. To accept the connection request, choose **Actions**, **Accept endpoint connection request**. When prompted for confirmation, enter **accept** and then choose **Accept**.

1. To reject the connection request, choose **Actions**, **Reject endpoint connection request**. When prompted for confirmation, enter **reject** and then choose **Reject**.

**To accept or reject a connection request using the command line**
+ [accept-vpc-endpoint-connections](https://docs.aws.amazon.com/cli/latest/reference/ec2/accept-vpc-endpoint-connections.html) or [reject-vpc-endpoint-connections](https://docs.aws.amazon.com/cli/latest/reference/ec2/reject-vpc-endpoint-connections.html) (AWS CLI)
+ [Approve-EC2EndpointConnection](https://docs.aws.amazon.com/powershell/latest/reference/items/Approve-EC2EndpointConnection.html) or [Deny-EC2EndpointConnection](https://docs.aws.amazon.com/powershell/latest/reference/items/Deny-EC2EndpointConnection.html) (Tools for Windows PowerShell)

## Manage load balancers
<a name="associate-load-balancer"></a>

You can manage the load balancers that are associated with your endpoint service. You can't disassociate a load balancer if there are endpoints connected to your endpoint service.

If you enable another Availability Zone for your load balancers, the Availability Zone will appear under the **Load Balancers** tab on the **Endpoint services** page. However, it won't be enabled for the endpoint service or listed in the **Details** tab of your endpoint service on the AWS Management Console. You need to enable the endpoint service for the new Availability Zone.

It might take a few minutes for the load balancer’s Availability Zone to be ready for your endpoint service. If you are using an automation, we recommend that you add a wait in your automation process before you enable the endpoint service for the new Availability Zone.

**To manage the load balancers for your endpoint service using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Endpoint services**.

1. Select the endpoint service.

1. Choose **Actions**, **Associate or disassociate load balancers**.

1. Change the endpoint service configuration as needed. For example:
   + Select the check box for a load balancer to associate it with the endpoint service.
   + Clear the check box for a load balancer to disassociate it from the endpoint service. You must keep at least one load balancer selected.

1. Choose **Save changes**

   The endpoint service will be enabled for any new Availability Zones you added to your load balancer. The new Availability Zone is listed under the **Load Balancers** tab and the **Details** tab of the endpoint service.

 After you enable an Availability Zone for the endpoint service, service consumers can add a subnet from that Availability Zone to their interface VPC endpoints.

**To manage the load balancers for your endpoint service using the command line**
+ [modify-vpc-endpoint-service-configuration](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-vpc-endpoint-service-configuration.html) (AWS CLI)
+ [Edit-EC2VpcEndpointServiceConfiguration](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-EC2VpcEndpointServiceConfiguration.html) (Tools for Windows PowerShell)

To enable the endpoint service in an Availability Zone that was recently enabled for the load balancer, simply call the command with the ID of the endpoint service.

## Associate a private DNS name
<a name="associate-private-dns-name"></a>

You can associate a private DNS name with your endpoint service. After you associate a private DNS name, you must update the entry for the domain on your DNS server. Before service consumers can use the private DNS name, the service provider must verify that they own the domain. For more information, see [Manage DNS names](manage-dns-names.md).

**To modify an endpoint service private DNS name using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Endpoint services**.

1. Select the endpoint service.

1. Choose **Actions**, **Modify private DNS name**.

1. Select **Associate a private DNS name with the service** and enter the private DNS name.
   + Domain names must use lowercase.
   + You can use wildcards in domain names (for example, **\*.myexampleservice.com**).

1. Choose **Save changes**.

1. The private DNS name is ready for use by service consumers when the verification status is **verified**. If the verification status changes, new connection requests are denied but existing connections are not affected.

**To modify an endpoint service private DNS name using the command line**
+ [modify-vpc-endpoint-service-configuration](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-vpc-endpoint-service-configuration.html) (AWS CLI)
+ [Edit-EC2VpcEndpointServiceConfiguration](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-EC2VpcEndpointServiceConfiguration.html) (Tools for Windows PowerShell)

**To initiate the domain verification process using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Endpoint services**.

1. Select the endpoint service.

1. Choose **Actions**, **Verify domain ownership for private DNS name**. 

1. When prompted for confirmation, enter **verify** and then choose **Verify**.

**To initiate the domain verification process using the command line**
+ [start-vpc-endpoint-service-private-dns-verification](https://docs.aws.amazon.com/cli/latest/reference/ec2/start-vpc-endpoint-service-private-dns-verification.html) (AWS CLI)
+ [Start-EC2VpcEndpointServicePrivateDnsVerification](https://docs.aws.amazon.com/powershell/latest/reference/items/Start-EC2VpcEndpointServicePrivateDnsVerification.html) (Tools for Windows PowerShell)

## Modify the supported Regions
<a name="manage-supported-regions"></a>

You can modify the set of supported Regions for your endpoint service. Before you can add an opt-in Region, you must opt in. You can't remove the Region that hosts your endpoint service.

After you remove a Region, service consumers can't create new endpoints that specify it as the service Region. Removing a Region doesn't affect existing endpoints that specify it as the service Region. When you remove a Region, we recommend that you reject any existing endpoint connections from that Region.

**To modify the supported Regions for your endpoint service**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Endpoint services**.

1. Select the endpoint service.

1. Choose **Actions**, **Modify supported Regions**.

1. Select and deselect Regions as needed.

1. Choose **Save changes**.

## Modify the supported IP address types
<a name="supported-ip-address-types"></a>

You can change the IP address types that are supported by your endpoint service.

**Consideration**  
To enable your endpoint service to accept IPv6 requests, its Network Load Balancers must use the dualstack IP address type. The targets do not need to support IPv6 traffic. For more information, see [IP address type](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancers.html#ip-address-type) in the *User Guide for Network Load Balancers*.

**To modify the supported IP address types using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Endpoint services**.

1. Select the VPC endpoint service.

1. Choose **Actions**, **Modify supported IP address types**.

1. For **Supported IP address types**, do one of the following:
   + Select **IPv4** – Enable the endpoint service to accept IPv4 requests.
   + Select **IPv6** – Enable the endpoint service to accept IPv6 requests.
   + Select **IPv4** and **IPv6** – Enable the endpoint service to accept both IPv4 and IPv6 requests.

1. Choose **Save changes**.

**To modify the supported IP address types using the command line**
+ [modify-vpc-endpoint-service-configuration](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-vpc-endpoint-service-configuration.html) (AWS CLI)
+ [Edit-EC2VpcEndpointServiceConfiguration](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-EC2VpcEndpointServiceConfiguration.html) (Tools for Windows PowerShell)

## Manage tags
<a name="add-remove-endpoint-service-tags"></a>

You can tag your resources to help you identify them or categorize them according to your organization's needs.

**To manage tags for your endpoint service using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Endpoint services**.

1. Select the VPC endpoint service.

1. Choose **Actions**, **Manage tags**.

1. For each tag to add, choose **Add new tag** and enter the tag key and tag value.

1. To remove a tag, choose **Remove** to the right of the tag key and value.

1. Choose **Save**.

**To manage tags for your endpoint connections using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Endpoint services**.

1. Select the VPC endpoint service and then choose the **Endpoint connections** tab.

1. Select the endpoint connection and then choose **Actions**, **Manage tags**.

1. For each tag to add, choose **Add new tag** and enter the tag key and tag value.

1. To remove a tag, choose **Remove** to the right of the tag key and value.

1. Choose **Save**.

**To manage tags for your endpoint service permissions using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Endpoint services**.

1. Select the VPC endpoint service and then choose the **Allow principals** tab.

1. Select the principal and then choose **Actions**, **Manage tags**.

1. For each tag to add, choose **Add new tag** and enter the tag key and tag value.

1. To remove a tag, choose **Remove** to the right of the tag key and value.

1. Choose **Save**.

**To add and remove tags using the command line**
+ [create-tags](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-tags.html) and [delete-tags](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-tags.html) (AWS CLI)
+ [New-EC2Tag](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2Tag.html) and [Remove-EC2Tag](https://docs.aws.amazon.com/powershell/latest/reference/items/Remove-EC2Tag.html) (Tools for Windows PowerShell)