**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Size constraint

rule statement

This section explains what a size constraint statement is and how it works.

A size constraint statement compares the number of bytes that AWS WAF receives for a web
request component to a number that you provide, and matches according to your comparison criteria.

The comparison criteria is an operator such as greater than (>) or
less than (<). For example, you can match on requests that have a query string with a size that's greater
than 100 bytes.

If you inspect the URI path, any `/` in the path counts as one character. For example, the URI path `/logo.jpg` is nine characters long.

###### Note

This statement only inspects the size of the web request component. It doesn't inspect the contents of the component.

## Rule statement

characteristics

**Nestable** – You can nest this statement
type.

**WCUs** – 1 WCU, as a base cost.
If you use the request component **All query parameters**, add 10 WCUs.
If you use the request component **JSON body**, double the base cost WCUs. For each **Text transformation** that you apply, add 10 WCUs.

This statement type operates on a web request component, and requires the following request component settings:

- **Request component** – The part of the web request
  to inspect, for example, a query string or the body. For information about web request components, see [Adjusting rule statement settings in AWS WAF](waf-rule-statement-fields.md "waf-rule-statement-fields.md").

A size constraint statement inspects only the size of the component after
any transformations have been applied. It does not inspect the contents of the component.

- **Optional text transformations** –
  Transformations that you want AWS WAF to perform on the request component before
  inspecting its size. For example, you could compress white space or decode HTML entities.
  If you specify more than one transformation, AWS WAF processes them
  in the order listed. For information, see [Using text transformations in AWS WAF](waf-rule-statement-transformation.md "waf-rule-statement-transformation.md").

Additionally, this statement requires the following settings:

- **Size match condition** – This
  indicates the numerical comparison operator to use to compare the size
  that you provide with the request component that you've chosen. Choose
  the operator from the list.
- **Size** – The size setting, in bytes, to use in the comparison.

## Where to find this rule statement

- **Rule builder** on the console –
  For **Match type**, under **Size match
  condition**, choose the condition that you want to
  use.
- **API** –
  [SizeConstraintStatement](../APIReference/API_SizeConstraintStatement.md "../APIReference/API_SizeConstraintStatement.md")
