**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Creating and managing a regex pattern set in AWS WAF

A regex pattern set provides a collection of regular expressions that you want to use together in a rule statement. Regex pattern sets are AWS resources.

To use a regex pattern set in a protection pack (web ACL) or rule group, you first create an AWS resource,
`RegexPatternSet` with your regex pattern specifications. Then you
reference the set when you add a regex pattern set rule statement to a protection pack (web ACL) or rule
group. A regex pattern set must contain at least one regex pattern.

If your regex pattern set contains more than one regex pattern, when it's used in a
rule, the pattern matching is combined with `OR` logic. That is, a web
request will match the pattern set rule statement if the request component matches any
of the patterns in the set.

AWS WAF supports the pattern syntax used by the PCRE library `libpcre` with some exceptions. The library is documented at [PCRE - Perl Compatible Regular Expressions](http://www.pcre.org/ "http://www.pcre.org/"). For information about AWS WAF support, see [Supported regular expression syntax in AWS WAF](waf-regex-pattern-support.md "waf-regex-pattern-support.md").

## Creating a regex pattern set

Follow the procedure in this section to create a new regex pattern set.

###### To create a regex pattern set

1. Sign in to the AWS Management Console and open the AWS WAF console at
   [https://console.aws.amazon.com/wafv2/homev2](https://console.aws.amazon.com/wafv2/homev2 "https://console.aws.amazon.com/wafv2/homev2").
2. In the navigation pane, choose **Regex pattern sets** and then
   **Create regex pattern set**.
3. Enter a name and description for the regex pattern set. You'll use these to identify it when you
   want to use the set.

###### Note

You can't change the name after you create the regex pattern set. 4. For **Region**, choose Global (CloudFront) or choose the Region where you want to store the regex pattern set.
You can use regional regex pattern sets only in protection packs (web ACLs) that protect regional resources. To use
a regex pattern set in protection packs (web ACLs) that protect Amazon CloudFront distributions, you must use Global (CloudFront). 5. In the **Regular expressions** text box, enter one regex pattern
per line.

For example, the regular expression `I[a@]mAB[a@]dRequest` matches the
following strings: `IamABadRequest`, `IamAB@dRequest`,
`I@mABadRequest`, and `I@mAB@dRequest`.

AWS WAF supports the pattern syntax used by the PCRE library `libpcre` with some exceptions. The library is documented at [PCRE - Perl Compatible Regular Expressions](http://www.pcre.org/ "http://www.pcre.org/"). For information about AWS WAF support, see [Supported regular expression syntax in AWS WAF](waf-regex-pattern-support.md "waf-regex-pattern-support.md"). 6. Review the settings for the regex pattern set, and choose **Create regex pattern set**.

## Deleting a regex pattern set

Follow the guidance in this section to delete a referenced set.

###### Deleting referenced sets and rule groups

When you delete an entity that you can use in a protection pack (web ACL), like an IP set, regex
pattern set, or rule group, AWS WAF checks to see if the entity is currently being
used in a protection pack (web ACL). If it finds that it is in use, AWS WAF warns you. AWS WAF is almost
always able to determine if an entity is being referenced by a protection pack (web ACL). However, in
rare cases it might not be able to do so. If you need to be sure that nothing is
currently using the entity, check for it in your protection packs (web ACLs) before deleting
it. If the entity is a referenced set, also check that no rule groups are using it.

###### To delete a regex pattern set

1. Sign in to the AWS Management Console and open the AWS WAF console at
   [https://console.aws.amazon.com/wafv2/homev2](https://console.aws.amazon.com/wafv2/homev2 "https://console.aws.amazon.com/wafv2/homev2").
2. In the navigation pane, choose **Regex pattern sets**.
3. Select the regex pattern set that you want to delete and choose **Delete**.
