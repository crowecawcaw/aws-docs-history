# `AWSSupport-TroubleshootLambdaInternetAccess`

**Description**

The `AWSSupport-TroubleshootLambdaInternetAccess` runbook helps you
troubleshoot internet access issues for a AWS Lambda function that was launched into
Amazon Virtual Private Cloud (Amazon VPC). Resources such as subnet routes, security groups rules, and
network access control list (ACL) rules are reviewed to confirm outbound internet
access is allowed.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootLambdaInternetAccess "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootLambdaInternetAccess")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**

- AutomationAssumeRole

Type: String

Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
(IAM) role that allows Systems Manager Automation to perform the actions on your
behalf. If no role is specified, Systems Manager Automation uses the permissions of
the user that starts this runbook.

- FunctionName

Type: String

Description: (Required) The name of the Lambda function you want to
troubleshoot internet access for.

- destinationIp

Type: String

Description: (Required) The destination IP address you want to establish
an outbound connection to.

- destinationPort

Type: String

Default: 443

Description: (Optional) The destination port you want to establish an
outbound connection on.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `lambda:GetFunction`
- `ec2:DescribeRouteTables`
- `ec2:DescribeNatGateways`
- `ec2:DescribeSecurityGroups`
- `ec2:DescribeNetworkAcls`

**Document Steps**

- `aws:executeScript` - Verifies the configuration of various
  resources in your VPC where the Lambda function was launched.
- `aws:branch` - Branches based on whether the Lambda function
  specified is in a VPC or not.
- `aws:executeScript` - Reviews the route table routes for the
  subnet where the Lambda function was launched, and verifies that routes to a
  network address translation (NAT) gateway, and internet gateway are present.
  Confirms the Lambda function is not in a public subnet.
- `aws:executeScript` - Verifies the security group associated with
  the Lambda function allows outbound internet access based on the values
  specified for the `destinationIp` and
  `destinationPort` parameters.
- `aws:executeScript` - Verifies the ACL rules associated with the
  subnets of the Lambda function and the NAT gateway allow outbound internet
  access based on the values specified for the `destinationIp` and
  `destinationPort` parameters.

**Outputs**

checkVpc.vpc - The ID of the VPC where your Lambda function was launched.

checkVpc.subnet - The IDs of the subnets where your Lambda function was
launched.

checkVpc.securityGroups - Security groups associated with the Lambda
function.

checkNACL.NACL - Analysis message with resource names. `LambdaIp`
refers to the private IP address of the elastic network interface for your Lambda
function. The `LambdaIpRules` object is only generated for subnets that
have a route to a NAT gateway. The following content is an example of the output.

```
{
   "subnet-1234567890":{
      "NACL":"acl-1234567890",
      "destinationIp_Egress":"Allowed",
      "destinationIp_Ingress":"notAllowed",
      "Analysis":"This NACL has an allow rule for Egress traffic but there is no Ingress rule. Please allow the destination IP / destionation port in Ingress rule",
      "LambdaIpRules":{
         "{LambdaIp}":{
            "Egress":"notAllowed",
            "Ingress":"notAllowed",
            "Analysis":"This is a NAT subnet NACL. It does not have ingress or egress rule allowed in it for Lambda's corresponding private ip {LambdaIp} Please allow this IP in your egress and ingress NACL rules"
         }
      }
   },
   "subnet-0987654321":{
      "NACL":"acl-0987654321",
      "destinationIp_Egress":"Allowed",
      "destinationIp_Ingress":"notAllowed",
      "Analysis":"This NACL has an allow rule for Egress traffic but there is no Ingress rule. Please allow the destination IP / destionation port in Ingress rule"
   }
}
```

checkSecurityGroups.secgrps - Analysis for the security group associated with your
Lambda function. The following content is an example of the output.

```
{
   "sg-123456789":{
      "Status":"Allowed",
      "Analysis":"This security group has allowed destintion IP and port in its outbuond rule."
   }
}
```

checkSubnet.subnets - Analysis for the subnets in your VPC associated with your
Lambda function. The following content is an example of the output.

```
{
   "subnet-0c4ee6cdexample15":{
      "Route":{
         "DestinationCidrBlock":"8.8.8.0/26",
         "NatGatewayId":"nat-00f0example69fdec",
         "Origin":"CreateRoute",
         "State":"active"
      },
      "Analysis":"This Route Table has an active NAT gateway path. Also, The NAT gateway is launched in public subnet",
      "RouteTable":"rtb-0b1fexample16961b"
   }
}
```
