**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Regex match rule

statement

This section explains what a regex match statement is and how it works.

A regex match statement instructs AWS WAF to match a request component against a
single regular expression (regex). A web request matches the statement if the
request component matches the regex that you specify.

This statement type is a good alternative to the [Regex pattern
set match rule statement](waf-rule-statement-type-regex-pattern-set-match.md "waf-rule-statement-type-regex-pattern-set-match.md") for
situations where you want to combine your matching criteria using mathematical
logic. For example, if you want a request component to match against some regex
patterns and to not match against others, you can combine the regex match
statements using the [AND rule
statement](waf-rule-statement-type-and.md "waf-rule-statement-type-and.md") and the [NOT rule
statement](waf-rule-statement-type-not.md "waf-rule-statement-type-not.md").

AWS WAF supports the pattern syntax used by the PCRE library `libpcre` with some exceptions. The library is documented at [PCRE - Perl Compatible Regular Expressions](http://www.pcre.org/ "http://www.pcre.org/"). For information about AWS WAF support, see [Supported regular expression syntax in AWS WAF](waf-regex-pattern-support.md "waf-regex-pattern-support.md").

## Rule statement

characteristics

**Nestable** – You can nest this statement
type.

**WCUs** – 3 WCUs, as a base cost.
If you use the request component **All query parameters**, add 10 WCUs.
If you use the request component **JSON body**, double the base cost WCUs. For each **Text transformation** that you apply, add 10 WCUs.

This statement type operates on a web request component, and requires the following request component settings:

- **Request component** – The part of the web request
  to inspect, for example, a query string or the body.

###### Warning

If you inspect the request components **Body**, **JSON body**, **Headers**, or **Cookies**, read about the limitations on how much content AWS WAF can inspect at
[Oversize web request components
in AWS WAF](waf-oversize-request-components.md "waf-oversize-request-components.md").

For information about web request components, see [Adjusting rule statement settings in AWS WAF](waf-rule-statement-fields.md "waf-rule-statement-fields.md").

- **Optional text transformations** –
  Transformations that you want AWS WAF to perform on the request component before
  inspecting it. For example, you could transform to lowercase or normalize
  white space. If you specify more than one transformation, AWS WAF processes them
  in the order listed. For information, see [Using text transformations in AWS WAF](waf-rule-statement-transformation.md "waf-rule-statement-transformation.md").

## Where to find this rule statement

- **Rule builder** on the console –
  For **Match type**, choose **Matches regular
  expression**.
- **API** –
  [RegexMatchStatement](../APIReference/API_RegexMatchStatement.md "../APIReference/API_RegexMatchStatement.md")
