

# Control traffic entering your VPC using a gateway route table
<a name="associate-route-table-gateway"></a>

To control traffic entering your VPC with a gateway route table, you can associate or disassociate an internet gateway or a virtual private gateway with a route table. For more information, see [Gateway route tables](gateway-route-tables.md).

**To associate or disassociate a gateway with a route table using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Route tables**, and then select the route table.

1. From the **Edge associations** tab, choose **Edit edge associations**.

1. Select or deselect the checkbox for the gateway.

1. Choose **Save changes**.

**To associate a gateway with a route table using the AWS CLI**  
Use the [associate-route-table](https://docs.aws.amazon.com/cli/latest/reference/ec2/associate-route-table.html) command. The following example associates the specified route table with the specified internet gateway.

```
aws ec2 associate-route-table
    --route-table-id {{rtb-01234567890123456}} \
    --gateway-id {{igw-11aa22bb33cc44dd1}}
```

**To disassociate a gateway from a route table using the AWS CLI**  
Use the [disassociate-route-table](https://docs.aws.amazon.com/cli/latest/reference/ec2/disassociate-route-table.html)command. Specify the ID of the association between the route table and the gateway.

```
aws ec2 disassociate-route-table \
    --association-id {{rtbassoc-0abcdef1234567890}}
```