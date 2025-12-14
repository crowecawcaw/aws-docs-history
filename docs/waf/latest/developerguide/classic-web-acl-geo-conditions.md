**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Working with geographic match conditions

###### Warning

AWS WAF Classic is is going through a planned end-of-life process. Refer to your AWS Health dashboard for the milestones and dates specific to your Region.

###### Note

This is **AWS WAF Classic** documentation. You should only
use this version if you created AWS WAF
resources, like rules and web ACLs, in AWS WAF prior to November 2019, and you have not
migrated them over to the latest version yet. To migrate your web ACLs, see [Migrating your AWS WAF Classic resources to AWS WAF](waf-migrating-from-classic.md "waf-migrating-from-classic.md").

**For the latest version of AWS WAF**, see [AWS WAF](waf-chapter.md "waf-chapter.md").

If you want to allow or block web requests based on the country that the requests
originate from, create one or more geo match conditions. A geo match condition lists countries that your requests originate from. Later in
the process, when you create a web ACL, you specify whether to allow or block requests
from those countries.

You can use geo match conditions with other AWS WAF Classic conditions or rules to build sophisticated filtering. For example, if you want to block certain countries, but still allow specific IP addresses from that country, you could create a rule containing a geo match condition and an IP match condition. Configure the rule to block requests that originate from that country and do not match the approved IP addresses. As another example, if you want to prioritize resources for users in a particular country, you could include a geo match condition in two different rate-based rules. Set a higher rate limit for users in the preferred country and set a lower rate limit for all other users.

###### Note

If you are using the CloudFront geo restriction feature to block a country from accessing your
content, any request from that country is blocked and is not forwarded to AWS WAF Classic.
So if you want to allow or block requests based on geography plus other AWS WAF Classic
conditions, you should _not_ use the CloudFront geo restriction
feature. Instead, you should use an AWS WAF Classic geo match condition.

###### Topics

- [Creating a geo match condition](#classic-web-acl-geo-conditions-creating "#classic-web-acl-geo-conditions-creating")
- [Editing geo match conditions](#classic-web-acl-geo-conditions-editing "#classic-web-acl-geo-conditions-editing")
- [Deleting geo match conditions](#classic-web-acl-geo-conditions-deleting "#classic-web-acl-geo-conditions-deleting")

## Creating a geo match condition

If you want to allow some web requests and block others based on the countries that the
requests originate from, create a geo match condition for the countries that you
want to allow and another geo match condition for the countries that you want to
block.

###### Note

When you add a geo match condition to a rule, you also can configure AWS WAF Classic to allow or block
web requests that _do not_ originate from the country
that you specify in the condition.

###### To create a geo match condition

1. Sign in to the AWS Management Console and open the AWS WAF console at
   [https://console.aws.amazon.com/wafv2/](https://console.aws.amazon.com/wafv2/ "https://console.aws.amazon.com/wafv2/").

If you see **Switch to AWS WAF Classic** in the navigation pane, select it. 2. In the navigation pane, choose **Geo match**. 3. Choose **Create condition**. 4. Enter a name in the **Name** field.

The name can contain only
alphanumeric characters (A-Z, a-z, 0-9) or the following special characters: \_-!"#`+\*},./ . You can't change the name of a condition after you create it. 5. Choose a **Region**. 6. Choose a **Location type** and a country. **Location type** can currently only be **Country**. 7. Choose **Add location**. 8. Choose **Create**.

## Editing geo match conditions

You can add countries to or delete countries from your geo match condition.

###### To edit a geo match condition

1. Sign in to the AWS Management Console and open the AWS WAF console at
   [https://console.aws.amazon.com/wafv2/](https://console.aws.amazon.com/wafv2/ "https://console.aws.amazon.com/wafv2/").

If you see **Switch to AWS WAF Classic** in the navigation pane, select it. 2. In the navigation pane, choose **Geo match**. 3. In the **Geo match conditions** pane, choose the geo match condition that you want to edit. 4. To add a country:

    1. In the right pane, choose **Add filter**.
    2. Choose a **Location type** and a country. **Location type** can currently only be **Country**.
    3. Choose **Add**.

5. To delete a country:
   1. In the right pane, select the values that you want to delete.
   2. Choose **Delete filter**.

## Deleting geo match conditions

If you want to delete a geo match condition, you must first remove all countries in the condition and remove the condition from all the rules that are using
it, as described in the following procedure.

###### To delete a geo match condition

1. Sign in to the AWS Management Console and open the AWS WAF console at
   [https://console.aws.amazon.com/wafv2/](https://console.aws.amazon.com/wafv2/ "https://console.aws.amazon.com/wafv2/").

If you see **Switch to AWS WAF Classic** in the navigation pane, select it. 2. Remove the geo match condition from the rules that are using it:

    1. In the navigation pane, choose **Rules**.
    2. Choose the name of a rule that is using the geo match condition that you want to delete.
    3. In the right pane, choose **Edit rule**.
    4. Choose the **X** next to the condition you want to delete.
    5. Choose **Update**.
    6. Repeat for all the remaining rules that are using the geo match condition that
     you want to delete.

3. Remove the filters from the condition you want to delete:
   1. In the navigation pane, choose **Geo match**.
   2. Choose the name of the geo match condition that you want to delete.
   3. In the right pane, choose the check box next to **Filter** in order to select all of the filters.
   4. Choose the **Delete filter**.

4. In the navigation pane, choose **Geo match**.
5. In the **Geo match conditions** pane, choose the geo match condition that you want to delete.
6. Choose **Delete** to delete the selected condition.
