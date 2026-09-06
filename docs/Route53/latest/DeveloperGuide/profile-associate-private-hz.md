

# Associate private hosted zones to a Route 53 Profile
<a name="profile-associate-private-hz"></a>

For intructions for how to create a private hosted zone, see [Creating a private hosted zone](hosted-zone-private-creating.md), and then follow the steps in this procedure to associate a private hosted zone to a Profile.<a name="profile-associate-private-hz-procedure"></a>

**To associate private hosted zones**

1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

1. On the navigation bar, choose the Region where you created the Profile.

1. In the navigation pane, choose **Profiles** and on the **Profiles** table, choose the linked name of the Profile you want to work with.

1. On the **<Profile name>** page, choose the **Private hosted zones** tab, and then **Associate**.

1. On the **Associate private hosted zones** page you can select up to 10 private hosted zones you have previously created. If you want to associate more than 10 private hosted zones, use the APIs. For more information, see [AssociateResourceToProfile](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_AssociateResourceToProfile.html).

   To create private hosted zones, see [Creating a private hosted zone](hosted-zone-private-creating.md).

1. Choose **Associate**

1. The association progress is displayed in the **Status** column on the **Private hosted zones** tab.