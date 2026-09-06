

# Add egress-only internet access to a subnet
<a name="egress-only-internet-gateway-working-with"></a>

The following tasks describe how to create an egress-only (outbound) internet gateway for your private subnet and to configure routing for the subnet.

**Topics**
+ [1. Create an egress-only internet gateway](#egress-only-internet-gateway-create)
+ [2. Create a custom route table](#egress-only-internet-gateway-routing)
+ [3. Delete an egress-only internet gateway](#egress-only-internet-gateway-delete)
+ [Command line overview](#egress-only-internet-gateway-api-cli)

## 1. Create an egress-only internet gateway
<a name="egress-only-internet-gateway-create"></a>

You can create an egress-only internet gateway for your VPC using the Amazon VPC console.

**To create an egress-only internet gateway**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Egress Only Internet Gateways**.

1. Choose **Create Egress Only Internet Gateway**.

1. (Optional) Add or remove a tag.

   [Add a tag] Choose **Add new tag** and do the following:
   + For **Key**, enter the key name.
   + For **Value**, enter the key value.

   [Remove a tag] Choose **Remove** to the right of the tag's Key and Value.

1. Select the VPC in which to create the egress-only internet gateway. 

1. Choose **Create**.

## 2. Create a custom route table
<a name="egress-only-internet-gateway-routing"></a>

To send traffic destined outside the VPC to the egress-only internet gateway, you must create a custom route table, add a route that sends traffic to the gateway, and then associate it with your subnet. 

**To create a custom route table and add a route to the egress-only internet gateway**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Route Tables**, **Create route table**.

1. In the **Create route table** dialog box, optionally name your route table, then select your VPC and choose **Create route table**.

1. Select the custom route table that you just created. The details pane displays tabs for working with its routes, associations, and route propagation.

1. On the **Routes** tab, choose **Edit routes**, specify `::/0` in the **Destination** box, select the egress-only internet gateway ID in the **Target** list, and then choose **Save changes**. 

1. On the **Subnet associations** tab, choose **Edit subnet associations**, and select the check box for the subnet. Choose **Save**.

Alternatively, you can add a route to an existing route table that's associated with your subnet. Select your existing route table, and follow steps 5 and 6 above to add a route for the egress-only internet gateway.

For more information about route tables, see [Configure route tables](VPC_Route_Tables.md).

## 3. Delete an egress-only internet gateway
<a name="egress-only-internet-gateway-delete"></a>

If you no longer need an egress-only internet gateway, you can delete it. Any route in a route table that points to the deleted egress-only internet gateway remains in a `blackhole` status until you manually delete or update the route.

**To delete an egress-only internet gateway**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Egress Only Internet Gateways**, and select the egress-only internet gateway.

1. Choose **Delete**.

1. Choose **Delete Egress Only Internet Gateway** in the confirmation dialog box.

## Command line overview
<a name="egress-only-internet-gateway-api-cli"></a>

You can perform the tasks described on this page using the command line.

**Create an egress-only internet gateway**
+ [create-egress-only-internet-gateway](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-egress-only-internet-gateway.html) (AWS CLI)
+ [New-EC2EgressOnlyInternetGateway](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2EgressOnlyInternetGateway.html) (AWS Tools for Windows PowerShell)

**Describe an egress-only internet gateway**
+ [describe-egress-only-internet-gateways](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-egress-only-internet-gateways.html) (AWS CLI)
+ [Get-EC2EgressOnlyInternetGatewayList](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2EgressOnlyInternetGatewayList.html) (AWS Tools for Windows PowerShell)

**Delete an egress-only internet gateway**
+ [delete-egress-only-internet-gateway](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-egress-only-internet-gateway.html) (AWS CLI)
+ [Remove-EC2EgressOnlyInternetGateway](https://docs.aws.amazon.com/powershell/latest/reference/items/Remove-EC2EgressOnlyInternetGateway.html) (AWS Tools for Windows PowerShell)