# Complete prerequisites to use

Debezium source connector

Your connector must be able to access the internet so that it can interact with services such as AWS Secrets Manager that are
outside of your Amazon Virtual Private Cloud. The steps in this section help you complete the following tasks to enable internet access.

- Set up a public subnet that hosts a NAT gateway and routes traffic to an internet gateway in your VPC.
- Create a default route that directs your private subnet traffic to your NAT gateway.
  For more information, see [Enable internet access for Amazon MSK
  Connect](msk-connect-internet-access.md "msk-connect-internet-access.md").

**Prerequisites**

Before you can enable internet access, you need the following items:

- The ID of the Amazon Virtual Private Cloud (VPC) associated with your cluster. For example, _vpc-123456ab_.
- The IDs of the private subnets in your VPC. For example, _subnet-a1b2c3de_, _subnet-f4g5h6ij_, etc. You must configure your connector with private subnets.

###### To enable internet access for your connector

1.  Open the Amazon Virtual Private Cloud console at
    [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2.  Create a public subnet for your NAT gateway with a descriptive name, and note the
    subnet ID. For detailed instructions, see [Create a subnet in your
    VPC](../../../vpc/latest/userguide/working-with-vpcs.md#AddaSubnet "../../../vpc/latest/userguide/working-with-vpcs.md#AddaSubnet").
3.  Create an internet gateway so that your VPC can communicate with the internet, and
    note the gateway ID. Attach the internet gateway to your VPC. For instructions, see
    [Create
    and attach an internet gateway](../../../vpc/latest/userguide/VPC_Internet_Gateway.md#Add_IGW_Attach_Gateway "../../../vpc/latest/userguide/VPC_Internet_Gateway.md#Add_IGW_Attach_Gateway").
4.  Provision a public NAT gateway so that hosts in your private subnets can reach
    your public subnet. When you create the NAT gateway, select the public subnet that you
    created earlier. For instructions, see [Create a NAT gateway](../../../vpc/latest/userguide/vpc-nat-gateway.md#nat-gateway-creating "../../../vpc/latest/userguide/vpc-nat-gateway.md#nat-gateway-creating").
5.  Configure your route tables. You must have two route tables in total to complete this
    setup. You should already have a main route table that was automatically created at the
    same time as your VPC. In this step you create an additional route table for your public
    subnet.

        1. Use the following settings to modify your VPC's main route table so that your
         private subnets route traffic to your NAT gateway. For instructions, see
         [Work with route tables](../../../vpc/latest/userguide/WorkWithRouteTables.md "../../../vpc/latest/userguide/WorkWithRouteTables.md") in the *Amazon Virtual Private Cloud*
        *User Guide*.




        Private MSKC route table| Property | Value |

    | --- | --- |
    | Name tag | We recommend that you give this route table a descriptive name tag to help you identify it. For example, **Private MSKC**. |
    | Associated subnets | Your private subnets |
    | A route to enable internet access for MSK Connect | <br>• **Destination**: 0.0.0.0/0 <br>• **Target**: Your NAT gateway ID. For example, _nat-12a345bc6789efg1h_. |
    | A local route for internal traffic | <br>• **Destination**: 10.0.0.0/16. This value may differ depending on your VPC's CIDR block. <br>• **Target**: Local | 2. Follow the instructions in [Create a custom route table](../../../vpc/latest/userguide/VPC_Internet_Gateway.md#Add_IGW_Routing "../../../vpc/latest/userguide/VPC_Internet_Gateway.md#Add_IGW_Routing") to create a route table for your public subnet. When you create the table, enter a descriptive name in the **Name tag** field to help you identify which subnet the table is associated with. For example, **Public MSKC**. 3. Configure your **Public MSKC** route table using the following settings.
    | Property | Value |
    | --- | --- |
    | Name tag | **Public MSKC** or a different descriptive name that you choose |
    | Associated subnets | Your public subnet with NAT gateway |
    | A route to enable internet access for MSK Connect | <br>• **Destination**: 0.0.0.0/0 <br>• **Target**: Your internet gateway ID. For example, _igw-1a234bc5_. |
    | A local route for internal traffic | <br>• **Destination**: 10.0.0.0/16. This value may differ depending on your VPC's CIDR block. <br>• **Target**: Local | Now that you have enabled internet access for Amazon MSK Connect you are ready to create a connector.
