# How does Network Firewall Proxy work?

###### Note

Network Firewall Proxy is in public preview release and is subject to change.

## Core components of each Proxy

A Network Firewall Proxy deployment consists of several key components that work together to provide application-layer filtering.

1. **Proxy Configuration** – A Proxy Configuration is a top level container that defines the monitoring and protection behavior for a Proxy. The details of the behavior are defined in the rule groups that you add to your configuration. Each proxy configuration has a unique identifier, You can use a single proxy configuration across multiple proxies.

While setting up a Proxy configuration, you need:

    * Configuration name and description
    * Associated rule groups
    * Default action for unmatched traffic

2. **Rule Group** – A collection of filtering rules organized in order of your desired priority. Your traffic is matched against these rules in the order of their priority. Depending on the match action, the proxy either stops the evaluation (if the action is terminal - allow or deny), or continues evaluation (if the action is alert) until it matches a rule with a terminal action. Each proxy configuration includes a default empty rule group, and individual rule groups support up to 1,000 rules maximum.
3. **Filtering Rules** - Filtering rules are the fundamental components of proxy configuration, controlling how traffic is processed and managed. Each rule operates as part of a systematic traffic evaluation process, combining specific match conditions with defined actions. You can configure your rule to evaluate the traffic in three different phases - pre-DNS, pre-request and post-response.

**Rule Processing Logic -** The proxy evaluates rules sequentially in order of priority. Rules are processed in order based on their insert position, with lower numbers receiving higher priority. Within each phase, evaluation continues until the first matching rule is found. When a rule matches, the outcome follows strict patterns: a deny action immediately blocks traffic and terminates all further rule processing; an allow action stops processing in the current phase but requires and continues evaluation in subsequent phases; and an alert action logs the event while allowing evaluation to continue.

For example, if a rule in the early phase matches and allows traffic, the proxy proceeds to evaluate rules in the next phase. However, a deny action at any point immediately blocks the traffic, regardless of any remaining rules.

**Proxy Endpoint** – It is a PrivateLink interface endpoint that carries traffic between the client and the Proxy.

## Traffic flow management and inspection

Network Firewall Proxy manages and inspects traffic through multiple phases, providing comprehensive filtering and security controls at each step.

When your client sends a CONNECT request to the proxy, the proxy evaluates the filtering rules in the pre-DNS phase of the associated Proxy Configuration, using the client identity and destination domain metadata available to it. This protects your workloads against any exfiltration via the DNS. If the request is allowed to proceed based on the filtering rules defined for this Proxy,the Proxy then performs a DNS query with the requested domain and resolves the destination IP address. The Proxy then establishes a TCP connection with the end destination and sends a response to the client acknowledging the request. When the client sends the TLS traffic to the proxy, the proxy then filters it based on IP address, or header attributes (only if TLS interception is enabled). Finally, the Proxy inspects the response from the destination and filters based on content type or length (only when TLS interception is enabled).

###### Note

Network Firewall proxy preview supports only HTTP/1.1 protocol. HTTP/2 (H2) and HTTP/3 (H3) traffic will not be supported – these connections may be dropped or result in timeouts. Ensure your applications use HTTP/1.1 when routing through the Network Firewall proxy during the public preview timeframe.

### Traffic Flow Phases

Understanding how traffic flows through the proxy helps you design effective filtering rules. The proxy intercepts egress traffic at multiple points in the connection lifecycle:

**Pre-DNS Phase**

Triggered when a request from an application would require the Proxy to resolve a domain name. At this stage, you can examine the requested domain, source IP address, source VPC, and source AWS account.These rules can allow or deny the connection request before the Proxy makes the DNS query.

Example PreDNS use cases:

- Block access to known malicious domains
- Implement domain allow-lists for approved external services
- Restrict DNS resolution based on source account or VPC

**Pre-request Phase**

Triggered after successful DNS resolution but before the HTTP request is is sent to the end server. At this stage, you can examine the resolved IP address, the destination ports and header attributes including HTTP method, URL path, etc. Rules can allow or deny the request based on these attributes.

###### Note

Without TLS decryption, you can only filter based on IP in the pre-request phase. Rules which match on HTTP fields will not match for HTTPS requests unless you have turned on TLS intercept.

Example Pre-request use cases:

- Block HTTP POST requests to prevent data uploads (Turn on TLS intercept)
- Require specific authentication headers (Turn on TLS intercept)
- Restrict access to specific IP ranges or ports

**Post-response Phase**

Triggered after receiving the HTTP response but before returning it to the client. At this stage, you can examine response headers, HTTP status codes, and response content types. Rules can allow or deny the response based on these attributes.

Example Post-response use cases:

- Block responses containing specific content types (images, executables)

Rules are evaluated in order within each phase. The first matching rule determines the action. If a rule denies traffic at any phase, the connection is terminated and subsequent phases are not evaluated. However, if the traffic is allowed or alerted in the pre-DNS phase, it will still be evaluated against pre-Request and post-response phase rules.
