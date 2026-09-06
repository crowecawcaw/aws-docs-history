

# Gateway endpoints for Amazon DynamoDB
<a name="vpc-endpoints-ddb"></a>

You can access Amazon DynamoDB from your VPC using gateway VPC endpoints. After you create the gateway endpoint, you can add it as a target in your route table for traffic destined from your VPC to DynamoDB.

There is no additional charge for using gateway endpoints.

DynamoDB supports both gateway endpoints and interface endpoints. With a gateway endpoint, you can access DynamoDB from your VPC, without requiring an internet gateway or NAT device for your VPC, and with no additional cost. However, gateway endpoints do not allow access from on-premises networks, from peered VPCs in other AWS Regions, or through a transit gateway. For those scenarios, you must use an interface endpoint, which is available for an additional cost. For more information, see [Types of VPC endpoints for DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/privatelink-interface-endpoints.html#types-of-vpc-endpoints-for-ddb) in the *Amazon DynamoDB Developer Guide*.

**Topics**
+ [Considerations](#gateway-endpoint-considerations-ddb)
+ [Create a gateway endpoint](#create-gateway-endpoint-ddb)
+ [Control access using IAM policies](#iam-policies-ddb)
+ [Associate route tables](#associate-route-tables-ddb)
+ [Edit the VPC endpoint policy](#edit-vpc-endpoint-policy-ddb)
+ [Delete a gateway endpoint](#delete-gateway-endpoint-ddb)

## Considerations
<a name="gateway-endpoint-considerations-ddb"></a>
+ A gateway endpoint is available only in the Region where you created it. Be sure to create your gateway endpoint in the same Region as your DynamoDB tables.
+ If you're using the Amazon DNS servers, you must enable both [DNS hostnames and DNS resolution](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html#vpc-dns-updating) for your VPC. If you're using your own DNS server, ensure that requests to DynamoDB resolve correctly to the IP addresses maintained by AWS.
+ The rules for the security groups for your instances that access DynamoDB through a gateway endpoint must allow traffic to and from DynamoDB. You can reference the ID of the [prefix list](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-aws-managed-prefix-lists.html) for DynamoDB in security group rules.
+ The network ACL for the subnet for your instances that access DynamoDB through a gateway endpoint must allow traffic to and from DynamoDB. You can't reference prefix lists in network ACL rules, but you can get the IP address range for DynamoDB from the [prefix list](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-aws-managed-prefix-lists.html) for DynamoDB.
+ If you use AWS CloudTrail to log DynamoDB operations, the log files contain the private IP addresses of the EC2 instances in the service consumer VPC and the ID of the gateway endpoint for any requests performed through the endpoint.
+ Gateway endpoints support only IPv4 traffic.
+ The source IPv4 addresses from instances in your affected subnets change from public IPv4 addresses to private IPv4 addresses from your VPC. An endpoint switches network routes and disconnects open TCP connections. The previous connections that used public IPv4 addresses are not resumed. We recommend that you do not have any critical tasks running when you create or modify a gateway endpoint. Alternatively, test to ensure that your software can automatically reconnect to DynamoDB if a connection breaks.
+ Endpoint connections cannot be extended out of a VPC. Resources on the other side of a VPN connection, VPC peering connection, transit gateway, or Direct Connect connection in your VPC cannot use a gateway endpoint to communicate with DynamoDB.
+ Your account has a default quota of 20 gateway endpoints per Region, which is adjustable. There is also a limit of 255 gateway endpoints per VPC.

## Create a gateway endpoint
<a name="create-gateway-endpoint-ddb"></a>

Use the following procedure to create a gateway endpoint that connects to DynamoDB.

**To create a gateway endpoint using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Endpoints**.

1. Choose **Create endpoint**.

1. For **Service category**, choose **AWS services**.

1. For **Services**, add the filter **Type = Gateway** and select **com.amazonaws.**{{region}}**.dynamodb**.

1. For **VPC**, select the VPC in which to create the endpoint.

1. For **Route tables**, select the route tables to be used by the endpoint. We automatically add a route that points traffic destined for the service to the endpoint network interface.

1. For **Policy**, select **Full access** to allow all operations by all principals on all resources over the VPC endpoint. Otherwise, select **Custom** to attach a VPC endpoint policy that controls the permissions that principals have to perform actions on resources over the VPC endpoint.

1. (Optional) To add a tag, choose **Add new tag** and enter the tag key and the tag value.

1. Choose **Create endpoint**.

**To create a gateway endpoint using the command line**
+ [create-vpc-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-vpc-endpoint.html) (AWS CLI)
+ [New-EC2VpcEndpoint](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2VpcEndpoint.html) (Tools for Windows PowerShell)

## Control access using IAM policies
<a name="iam-policies-ddb"></a>

You can create IAM policies to control which IAM principals can access DynamoDB tables using a specific VPC endpoint.

**Example: Restrict access to a specific endpoint**  
You can create a policy that restricts access to a specific VPC endpoint by using the [aws:sourceVpce](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourcevpce) condition key. The following policy denies access to DynamoDB tables in the account unless the specified VPC endpoint is used. This example assumes that there is also a policy statement that allows the access required for your use cases.    
****  

```
{
   "Version":"2012-10-17",		 	 	 
   "Statement": [
      {
         "Sid": "Allow-access-from-specific-endpoint",
         "Effect": "Deny",
         "Principal": "*",
         "Action": "dynamodb:*",
         "Resource": "arn:aws:dynamodb:{{us-east-1}}:{{111111111111}}:table/*",
         "Condition": { 
            "StringNotEquals" : { 
               "aws:sourceVpce": "vpce-11aa22bb" 
            } 
         }
      }
   ]
}
```

**Example: Allow access from a specific IAM role**  
You can create a policy that allows access using a specific IAM role. The following policy grants access to the specified IAM role.    
****  

```
{
   "Version":"2012-10-17",		 	 	 
   "Statement": [
      {
         "Sid": "Allow-access-from-specific-IAM-role",
         "Effect": "Allow",
         "Principal": "*",
         "Action": "*",
         "Resource": "*",
         "Condition": {
            "ArnEquals": {
               "aws:PrincipalArn": "arn:aws:iam::{{111122223333}}:role/{{role_name}}"
            }
         }
      }
   ]
}
```

**Example: Allows access from a specific account**  
You can create a policy that allows access from a specific account only. The following policy grants access to users in the specified account.    
****  

```
{
   "Version":"2012-10-17",		 	 	 
   "Statement": [
      {
         "Sid": "Allow-access-from-account",
         "Effect": "Allow",
         "Principal": "*",
         "Action": "*",
         "Resource": "*",
         "Condition": {
            "StringEquals": {
               "aws:PrincipalAccount": "{{111122223333}}"
            }
         }
      }
   ]        
}
```

## Associate route tables
<a name="associate-route-tables-ddb"></a>

You can change the route tables that are associated with the gateway endpoint. When you associate a route table, we automatically add a route that points traffic destined for the service to the endpoint network interface. When you disassociate a route table, we automatically remove the endpoint route from the route table.

**To associate route tables using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Endpoints**.

1. Select the gateway endpoint.

1. Choose **Actions**, **Manage route tables**.

1. Select or deselect route tables as needed.

1. Choose **Modify route tables**.

**To associate route tables using the command line**
+ [modify-vpc-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-vpc-endpoint.html) (AWS CLI)
+ [Edit-EC2VpcEndpoint](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-EC2VpcEndpoint.html) (Tools for Windows PowerShell)

## Edit the VPC endpoint policy
<a name="edit-vpc-endpoint-policy-ddb"></a>

You can edit the endpoint policy for a gateway endpoint, which controls access to DynamoDB from the VPC through the endpoint. After you update an endpoint policy, it can take a few minutes for the changes to take effect. The default policy allows full access. For more information, see [Endpoint policies](vpc-endpoints-access.md).

**To change the endpoint policy using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Endpoints**.

1. Select the gateway endpoint.

1. Choose **Actions**, **Manage policy**.

1. Choose **Full Access** to allow full access to the service, or choose **Custom** and attach a custom policy.

1. Choose **Save**.

**To modify a gateway endpoint using the command line**
+ [modify-vpc-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-vpc-endpoint.html) (AWS CLI)
+ [Edit-EC2VpcEndpoint](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-EC2VpcEndpoint.html) (Tools for Windows PowerShell)

The following are example endpoint policies for accessing DynamoDB.

**Example: Allow read-only access**  
You can create a policy that restricts access to read-only access. The following policy grants permission to list and describe DynamoDB tables.  

```
{
  "Statement": [
    {
      "Sid": "ReadOnlyAccess",
      "Effect": "Allow",
      "Principal": "*",
      "Action": [
        "dynamodb:DescribeTable",
        "dynamodb:ListTables"
      ],
      "Resource": "*"
    }
  ]
}
```

**Example: Restrict access to a specific table**  
You can create a policy that restricts access to a specific DynamoDB table. The following policy allows access to the specified DynamoDB table.  

```
{
  "Statement": [
    {
      "Sid": "Allow-access-to-specific-table",
      "Effect": "Allow",
      "Principal": "*",
      "Action": [
        "dynamodb:Batch*",
        "dynamodb:Delete*",
        "dynamodb:DescribeTable",
        "dynamodb:GetItem",
        "dynamodb:PutItem",
        "dynamodb:Update*"
      ],
      "Resource": "arn:aws:dynamodb:{{region}}:{{123456789012}}:table/{{table_name}}"
    }
  ]
}
```

## Delete a gateway endpoint
<a name="delete-gateway-endpoint-ddb"></a>

When you are finished with a gateway endpoint, you can delete it. When you delete a gateway endpoint, we remove the endpoint route from the subnet route tables.

**To delete a gateway endpoint using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Endpoints**.

1. Select the gateway endpoint.

1. Choose **Actions**, **Delete VPC endpoints**. 

1. When prompted for confirmation, enter **delete**.

1. Choose **Delete**.

**To delete a gateway endpoint using the command line**
+ [delete-vpc-endpoints](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-vpc-endpoints.html) (AWS CLI)
+ [Remove-EC2VpcEndpoint](https://docs.aws.amazon.com/powershell/latest/reference/items/Remove-EC2VpcEndpoint.html) (Tools for Windows PowerShell)