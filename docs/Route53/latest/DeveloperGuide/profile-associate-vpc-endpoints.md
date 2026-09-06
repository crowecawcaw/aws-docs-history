

# Associate interface VPC endpoints to a Route 53 Profile
<a name="profile-associate-vpc-endpoints"></a>

For instructions on how to create a interface VPC endpoint, see [Create a VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint-aws) in the *VPC User Guide.* and then follow the steps in this procedure to associate a VPC endpoint to a Profile.<a name="profile-associate-vpc-endpoints-procedure"></a>

**To associate VPC endpoints**

1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

1. On the navigation bar, choose the Region where you created the Profile.

1. On the **<Profile name>** page, choose the **VPC endpoints** tab, and then **Associate**.

1. On the **Associate VPC endpoints** page, in the **VPC endpoints** table you can select up to 10 endpoints you have previously created. If you want to associate more than 10 endpoints, use the APIs. For more information, see [AssociateResourceToProfile](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_AssociateResourceToProfile.html).

   To create Resolver rules, see [Creating forwarding rules](resolver-rules-managing.md#resolver-rules-managing-creating-rules).

1. Choose **Associate**

1. The association progress is displayed in the **Status** column on the **VPC endpoints** tab.