

Amazon WorkSpaces Secure Browser will no longer be open to new customers starting October 29, 2026. If you would like to use Amazon WorkSpaces Secure Browser, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [Amazon WorkSpaces Secure Browser availability change](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/workspaces-secure-browser-maintenance-mode.html). 

# Restricted internet browsing prerequisites for Amazon WorkSpaces Secure Browser
<a name="restricted-prerequisites"></a>

Before you get started, make sure that you meet the following prerequisites:
+ You need an already deployed VPC, with public and private subnets spreading over several Availability Zones (AZs). For more information about how to set up your VPC environment, see [Default VPCs](https://docs.aws.amazon.com/vpc/latest/userguide/default-vpc.html).
+ You need one single proxy endpoint that is accessible from private subnets, where WorkSpaces Secure Browser sessions live (for example, the network load balancer DNS name). If you want to use your existing proxy, make sure it also has a single endpoint that is accessible from your private subnets.