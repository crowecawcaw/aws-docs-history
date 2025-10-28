# Disassociating a resource from an Amazon Route 53 Profile

Before you delete a Profile, you miust dissociate all resources from it.

###### To disassociate a resource

associated to a Route 53 Profile

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **Profiles**.
3. On the navigation bar, choose the Region where the Profile from which you want to disassociate a resource was created.
4. Select the button next to the name of the Profile from which you want to disassociate a resource.
5. On the **<Profile name>** page choose the tab for the resource you want to delete,
   either , **DNS Firewall rule groups**, **Private hosted zones**,
   **Resolver rules** or **VPC endpoints**.
6. On the tab page for the resource, choose the resource you want to disassociate and then **Disassociate**.
7. In the **Disassociate resources** dialog, type in `confirm`, and then choose
   **Disassociate**.
