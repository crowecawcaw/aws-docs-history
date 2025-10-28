# Associate interface VPC endpoints to a Route 53 Profile

For instructions on how to create a interface VPC endpoint, see
[Create a VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws") in the _VPC User Guide._
and then follow the steps in this procedure to associate a VPC endpoint to a Profile.

###### To associate VPC endpoints

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. On the navigation bar, choose the Region where you created the Profile.
3. On the **<Profile name>** page, choose the **VPC endpoints** tab, and then **Associate**.
4. On the **Associate VPC endpoints** page, in the **VPC endpoints** table you can select up to 10 endpoints you have
   previously created. If you want to associate more than 10 endpoints,
   use the APIs. For more information, see [AssociateResourceToProfile](../APIReference/API_route53profiles_AssociateResourceToProfile.md "../APIReference/API_route53profiles_AssociateResourceToProfile.md").

To create Resolver rules, see [Creating forwarding rules](resolver-rules-managing.md#resolver-rules-managing-creating-rules "resolver-rules-managing.md#resolver-rules-managing-creating-rules"). 5. Choose **Associate** 6. The association progress is displayed in the **Status**
column on the **VPC endpoints** tab.
