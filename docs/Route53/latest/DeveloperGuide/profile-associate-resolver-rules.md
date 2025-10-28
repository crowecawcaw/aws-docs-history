# Associate Resolver rules to a Route 53 Profile

For instructions for how to create a Resolver rule, see [Creating forwarding rules](resolver-rules-managing.md#resolver-rules-managing-creating-rules "resolver-rules-managing.md#resolver-rules-managing-creating-rules"),
and then follow the steps in this procedure to associate Resolver rules to a Profile.

###### To associate Resolver rules

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. On the navigation bar, choose the Region where you created the Profile.
3. On the **<Profile name>** page, choose the **Resolver
   rules** tab, and then **Associate**.
4. On the **Associate Resolver rules** page, in the **Resolver
   rules** table you can select up to 10 Resolver rules you have
   previously created. If you want to associate more than 10 resolver rules,
   use the APIs. For more information, see [AssociateResourceToProfile](../APIReference/API_route53profiles_AssociateResourceToProfile.md "../APIReference/API_route53profiles_AssociateResourceToProfile.md").

To create Resolver rules, see [Creating forwarding rules](resolver-rules-managing.md#resolver-rules-managing-creating-rules "resolver-rules-managing.md#resolver-rules-managing-creating-rules"). 5. Choose **Associate** 6. The association progress is displayed in the **Status**
column on the **Resolver rules** tab.
