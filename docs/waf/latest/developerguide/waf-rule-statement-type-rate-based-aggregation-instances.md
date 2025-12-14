**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Rate-based rule aggregation

instances and counts

This section explains how a rate-based rule evaluates web requests.

When a rate-based rule evaluates web requests using your aggregation criteria, each
unique set of values that the rule finds for the specified aggregation keys defines
a unique _aggregation instance_.

- **Multiple keys** – If you've defined multiple custom
  keys, the value for each key contributes to the aggregation instance
  definition. Each unique combination of values defines an aggregation
  instance.
- **Single key** – If you've chosen a single key,
  either in the custom keys or by selecting one of the singleton IP address
  choices, then each unique value for the key defines an aggregation instance.
- **Count all - no keys** – If you've selected the
  aggregation option **Count all**, then all requests that
  the rule evaluates belong to a single aggregation instance for the rule.
  This choice requires a scope-down statement.

A rate-based rule counts web requests separately for each aggregation instance that it
identifies.

For example, assume a rate-based rule evaluates web requests with the following IP address and HTTP method values:

- IP address 10.1.1.1, HTTP method POST
- IP address 10.1.1.1, HTTP method GET
- IP address 127.0.0.0, HTTP method POST
- IP address 10.1.1.1, HTTP method GET
  The rule creates different aggregation instances according to your aggregation criteria.

- If the aggregation criteria is just the IP address, then each individual IP address is an aggregation instance, and AWS WAF counts requests separately for each. The aggregation instances and request counts for our example would be the following:
  - IP address 10.1.1.1: count 3
  - IP address 127.0.0.0: count 1

- If the aggregation criteria is HTTP method, then each individual HTTP method is an aggregation instance. The aggregation instances and request counts for our example would be the following:
  - HTTP method POST: count 2
  - HTTP method GET: count 2

- If the aggregation criteria is IP address and HTTP method, then each IP address and each HTTP method would contribute to the combined aggregation instance. The aggregation instances and request counts for our example would be the following:
  - IP address 10.1.1.1, HTTP method POST: count 1
  - IP address 10.1.1.1, HTTP method GET: count 2
  - IP address 127.0.0.0, HTTP method POST: count 1
