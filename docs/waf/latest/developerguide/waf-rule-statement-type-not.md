**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# NOT rule

statement

The NOT rule statement logically negates the results of a single
nested statement, so the nested statements must not match for the
NOT statement to match, and vice versa. This requires one
nested statement.

For example, if you want to block requests that don't originate in a specific
country, create a NOT statement with action set to block, and nest
a geographic match statement that specifies the country.

## Rule statement characteristics

**Nestable** – You can nest this statement
type.

**WCUs** – Depends on the nested
statement.

## Where to find this rule statement

- **Rule builder** on the console –
  For **If a request**, choose **doesn't match
  the statement (NOT)**, and then fill in the nested
  statement.
- **API** –
  [NotStatement](../APIReference/API_NotStatement.md "../APIReference/API_NotStatement.md")
