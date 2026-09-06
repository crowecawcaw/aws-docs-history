

# Deleting a VPC endpoint association in AWS Network Firewall
<a name="deleting-vpc-endpoint-association"></a>

Before you delete a Network Firewall VPC endpoint association, remove its firewall endpoint from any VPC route tables that use it. For information about managing route tables for your VPC, see [Route tables](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html) in the *Amazon Virtual Private Cloud User Guide*.

**To delete a VPC endpoint association**

1. Sign in to the AWS Management Console and open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, under **Network Firewall**, choose **VPC endpoint associations**.

1. In the **VPC endpoint associations** page, select the VPC endpoint association that you want to delete.

1. Choose **Delete**, and then confirm your request.

Your VPC endpoint association is removed from the list in the **VPC endpoint association** page. The removal can take a few minutes to complete.