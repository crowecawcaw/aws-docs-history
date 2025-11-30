# Limits of the proxy service for the public preview in US East (Ohio) region only

###### Note

Network Firewall Proxy is in public preview release and is subject to change.

###### Service resource limits

- Number of Proxies per account - 1
- Number of Proxy configuration per account - 50
- Number of Proxy rule groups per account - 500
- Number of proxy configuration shared with proxies - 5
- Maximum size of condition-key:condition-value map per rule group - 30 MB
- Maximum size per condition-key:condition-value map per rule - 30 KB
- Maximum condition value - 1 KB
- Number of EgressProxyRules per rule group - 1000
- Number of EgressProxyRuleGroups per Proxy Configuration - 10
- Network Firewall proxy preview supports only HTTP/1.1 protocol. HTTP/2 (H2) and HTTP/3 (H3) traffic will not be supported – these connections may be dropped or result in timeouts. Ensure your applications use HTTP/1.1 when routing through the Network Firewall proxy.
