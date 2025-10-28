# Associate private hosted zones to a Route 53 Profile

For intructions for how to create a private hosted zone, see [Creating a private hosted zone](hosted-zone-private-creating.md "hosted-zone-private-creating.md"), and then
follow the steps in this procedure to associate a private hosted zone to a Profile.

###### To associate private hosted zones

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. On the navigation bar, choose the Region where you created the Profile.
3. In the navigation pane, choose
   **Profiles** and on the **Profiles** table, choose the linked name of the Profile you
   want to work with.
4. On the **<Profile name>** page, choose the **Private hosted
   zones** tab, and then **Associate**.
5. On the **Associate private hosted zones** page you can select up to 10
   private hosted zones you have previously created. If you want to associate
   more than 10 private hosted zones, use the APIs. For more information, see
   [AssociateResourceToProfile](../APIReference/API_route53profiles_AssociateResourceToProfile.md "../APIReference/API_route53profiles_AssociateResourceToProfile.md").

To create private hosted zones, see [Creating a private hosted zone](hosted-zone-private-creating.md "hosted-zone-private-creating.md"). 6. Choose **Associate** 7. The association progress is displayed in the **Status**
column on the **Private hosted zones** tab.
