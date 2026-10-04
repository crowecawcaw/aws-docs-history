

Amazon WorkSpaces Secure Browser will no longer be open to new customers starting October 29, 2026. If you would like to use Amazon WorkSpaces Secure Browser, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [Amazon WorkSpaces Secure Browser availability change](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/workspaces-secure-browser-maintenance-mode.html). 

# Internet connectivity ports for Amazon WorkSpaces Secure Browser
<a name="vpc-connection"></a>

Each WorkSpaces Secure Browser streaming instance has a customer network interface that provides connectivity to the resources within your VPC, as well as to the internet if private subnets with NAT gateway are set up.

For internet connectivity, the following ports must be open to all destinations. If you are using a modified or custom security group, you'll need to add the required rules manually. For more information, see [Security group rules](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html#SecurityGroupRules.html).

**Note**  
This applies to egress traffic.
+ TCP 80 (HTTP)
+ TCP 443 (HTTPS)
+ UDP 8433