

# Associate Resolver rules to a Route 53 Profile
<a name="profile-associate-resolver-rules"></a>

For instructions for how to create a Resolver rule, see [Creating forwarding rules](resolver-rules-managing.md#resolver-rules-managing-creating-rules), and then follow the steps in this procedure to associate Resolver rules to a Profile.<a name="profile-associate-resolver-rules-procedure"></a>

**To associate VPC Resolver rules**

1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

1. On the navigation bar, choose the Region where you created the Profile.

1. On the **<Profile name>** page, choose the **Resolver rules** tab, and then **Associate**.

1. On the **Associate Resolver rules** page, in the **Resolver rules** table you can select up to 10 Resolver rules you have previously created. If you want to associate more than 10 resolver rules, use the APIs. For more information, see [AssociateResourceToProfile](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_AssociateResourceToProfile.html).

   To create Resolver rules, see [Creating forwarding rules](resolver-rules-managing.md#resolver-rules-managing-creating-rules).

1. Choose **Associate**

1. The association progress is displayed in the **Status** column on the **Resolver rules** tab.