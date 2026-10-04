

Amazon WorkSpaces Secure Browser will no longer be open to new customers starting October 29, 2026. If you would like to use Amazon WorkSpaces Secure Browser, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [Amazon WorkSpaces Secure Browser availability change](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/workspaces-secure-browser-maintenance-mode.html). 

# Restricted internet browsing architecture for Amazon WorkSpaces Secure Browser
<a name="restricted-architecture"></a>

The following is an example of a typical proxy setup in your VPC. The proxy Amazon EC2 instance is in public subnets and associated with Elastic IP, so they have access to internet. A network load balancer hosts an auto scaling group of proxy instances. This ensures that proxy instances can scale up automatically, and the network load balancer is the single proxy endpoint, which can be consumed by WorkSpaces Secure Browser sessions. 

![WorkSpaces Secure Browser architecture](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/images/restricted-internet-architecture.png)
