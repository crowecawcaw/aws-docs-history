**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# AWS WAF rules

This section explains what an AWS WAF rule is and how it works.

An AWS WAF rule defines how to inspect HTTP(S) web requests and the action to take on a
request when it matches the inspection criteria. You define rules only in the context of a
rule group or protection pack (web ACL).

Rules don't exist in AWS WAF on their own. They aren't AWS resources, and they don't have
Amazon Resource Names (ARNs). You can access a rule by name in the rule group or protection pack (web ACL)
where it's defined. You can manage rules and copy them to other protection packs (web ACLs) by using the JSON
view of the rule group or protection pack (web ACL) that contains the rule. You can also manage them through
the AWS WAF console rule builder, which is available for protection packs (web ACLs) and
rule groups.

###### Rule name

Each rule requires a name. Avoid names that start with `AWS` and names that are
used for rule groups or rules that are managed for you by other services. See [Recognizing rule groups provided by other services](waf-service-owned-rule-groups.md "waf-service-owned-rule-groups.md").

###### Note

If you change the name of a rule and you want the rule's metric name to reflect the change, you
must update the metric name as well. AWS WAF doesn't automatically update the metric name for a rule when you change the rule name.
You can change the metric name when you edit the
rule in the console, by using the rule JSON editor. You can also change both names through the APIs and in any JSON listing that you
use to define your protection pack (web ACL) or rule group.

###### Rule statement

Each rule also requires a rule statement that defines how the rule inspects web requests. The rule statement might contain other, nested statements at any depth, depending on the rule and statement type. Some rule statements take sets of criteria. For example, you can specify up to 10,000 IP addresses or IP address ranges for an IP set match rule.

You can define rules that inspect for criteria like the following:

- Scripts that are likely to be malicious. Attackers embed scripts that can exploit
  vulnerabilities in web applications. This is known as cross-site scripting
  (XSS).
- IP addresses or address ranges that requests originate from.
- Country or geographical location that requests originate from.
- Length of a specified part of the request, such as the query string.
- SQL code that is likely to be malicious. Attackers try to extract data from your
  database by embedding malicious SQL code in a web request. This is known as SQL
  injection.
- Strings that appear in the request, for example, values that appear in the
  `User-Agent` header or text strings that appear in the query string.
  You can also use regular expressions (regex) to specify these strings.
- Labels that prior rules in the protection pack (web ACL) have added to the request.
  In addition to statements with web request inspection criteria, like the ones in the
  preceding list, AWS WAF supports logical statements for `AND`, `OR`, and
  `NOT` that you use to combine statements in a rule.

For example, based on recent requests that you've seen from an attacker, you might create
a rule with a logical `AND` statement that combines the following nested
statements:

- The requests come from 192.0.2.44.
- They contain the value `BadBot` in the `User-Agent`
  header.
- They appear to include SQL-like code in the query string.
  In this case, the web request needs to match all of the statements to result in a match
  for the top-level `AND`.

###### Topics

- [Using rule actions in AWS WAF](waf-rule-action.md "waf-rule-action.md")
- [Using rule statements in AWS WAF](waf-rule-statements.md "waf-rule-statements.md")
- [Using match rule statements in AWS WAF](waf-rule-statements-match.md "waf-rule-statements-match.md")
- [Using logical rule statements in AWS WAF](waf-rule-statements-logical.md "waf-rule-statements-logical.md")
- [Using rate-based rule statements in AWS WAF](waf-rule-statement-type-rate-based.md "waf-rule-statement-type-rate-based.md")
- [Using rule group rule statements in AWS WAF](waf-rule-statements-rule-group.md "waf-rule-statements-rule-group.md")
