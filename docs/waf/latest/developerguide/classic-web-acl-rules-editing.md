**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Adding and removing conditions in a rule

###### Warning

AWS WAF Classic is is going through a planned end-of-life process. Refer to your AWS Health dashboard for the milestones and dates specific to your Region.

###### Note

This is **AWS WAF Classic** documentation. You should only
use this version if you created AWS WAF
resources, like rules and web ACLs, in AWS WAF prior to November 2019, and you have not
migrated them over to the latest version yet. To migrate your web ACLs, see [Migrating your AWS WAF Classic resources to AWS WAF](waf-migrating-from-classic.md "waf-migrating-from-classic.md").

**For the latest version of AWS WAF**, see [AWS WAF](waf-chapter.md "waf-chapter.md").

You can change a rule by adding or removing conditions.

###### To add or remove conditions in a rule

1. Sign in to the AWS Management Console and open the AWS WAF console at
   [https://console.aws.amazon.com/wafv2/](https://console.aws.amazon.com/wafv2/ "https://console.aws.amazon.com/wafv2/").

If you see **Switch to AWS WAF Classic** in the navigation pane, select it. 2. In the navigation pane, choose **Rules**. 3. Choose the name of the rule in which you want to add or remove conditions. 4. Choose **Add rule**. 5. To add a condition, choose **Add condition** and specify the following values:

**When a request does/does not**
If you want AWS WAF Classic to allow or block requests based on the filters in a condition, for example,
web requests that originate from the range of IP addresses 192.0.2.0/24, choose **does**.

If you want AWS WAF Classic to allow or block requests based on the inverse of the filters in a condition,
choose **does not**. For example, if an IP match condition includes the IP address range
192.0.2.0/24 and you want AWS WAF Classic to allow or block requests that _do not_ come from
those IP addresses, choose **does not**.

**match/originate from**
Choose the type of condition that you want to add to the rule:

    * Cross-site scripting match conditions – choose **match at least one of the
     filters in the cross-site scripting match condition**
    * IP match conditions – choose **originate from an IP address in**
    * Geo match conditions – choose **originate from a geographic location
     in**
    * Size constraint conditions – choose **match at least one of the filters in the
     size constraint condition**
    * SQL injection match conditions – choose **match at least one of the filters in the
     SQL injection match condition**
    * String match conditions – choose **match at least one of the filters
     in the string match condition**
    * Regular expression match conditions – choose **match at least one of the filters
     in the regex match condition**

**_condition name_**
Choose the condition that you want to add to the rule. The list displays only conditions
of the type that you chose in the preceding step. 6. To remove a condition, select the **X** to the right of the condition name 7. Choose **Update**.
