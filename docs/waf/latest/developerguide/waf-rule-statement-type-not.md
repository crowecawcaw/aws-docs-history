

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# NOT rule statement
<a name="waf-rule-statement-type-not"></a>

The NOT rule statement logically negates the results of a single nested statement, so the nested statements must not match for the NOT statement to match, and vice versa. This requires one nested statement. 

For example, if you want to block requests that don't originate in a specific country, create a NOT statement with action set to block, and nest a geographic match statement that specifies the country. 

## Rule statement characteristics
<a name="not-rule-statement-characteristics"></a>

**Nestable** – You can nest this statement type. 

**WCUs** – Depends on the nested statement.

## Where to find this rule statement
<a name="not-rule-statement-where-to-find"></a>
+ **Rule builder** on the console – For **If a request**, choose **doesn't match the statement (NOT)**, and then fill in the nested statement.
+ **API** – [NotStatement](https://docs.aws.amazon.com/waf/latest/APIReference/API_NotStatement.html)