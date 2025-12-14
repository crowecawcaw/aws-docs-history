**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Key concepts in network security director

###### Note

AWS Shield network security director is in public preview release and is subject to change.

**Resources**

The compute, networking, and security resources that handle your application traffic:

- _Compute_ – Amazon Elastic Compute Cloud instances
- _Networking_ – Application Load Balancers, Amazon API Gateways, Amazon CloudFront distributions, VPC subnets, and VPC elastic network interfaces (ENIs)
- _Security_ – AWS WAF web ACLs, VPC security groups, and VPC network access control lists (NACLs)

**Findings**

Alerts about missing or misconfigured network security services, with severity levels of NONE, INFORMATIONAL, LOW, MEDIUM, HIGH, or CRITICAL. network security director generates findings by evaluating configuration settings and threat intelligence for each resource.

**Severity**

A measure of a resource's vulnerability to potential security events, based on AWS best practices and threat intelligence. Severity assessment considers both potential vulnerabilities and existing protections. A resource's severity level matches its most severe finding, or shows as none if there are no findings.

**Network topology**

A visual representation of your network that shows resource connections, internet exposure, and tag-based relationships. Use the topology view to investigate resources and their findings.

## Understanding network security director findings

###### Note

AWS Shield network security director is in public preview release and is subject to change.

Network security director generates specific findings for each type of resource it analyzes. These findings help you identify security issues and take appropriate action. The following table lists all possible findings by resource type.

| network security director findings by resource type | Resource type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Finding description |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| Application Load Balancer                           | • CloudFront origin is also Internet accessible without CloudFront protections<br>• AWS WAF missing bot and scraper rules<br>• DDoS activity detected<br>• Resource has no firewall attached for protection<br>• AWS WAF missing all rules - no protection, possible misconfiguration<br>• AWS WAF missing key AWS Managed Rules (IP Reputation, Common Rules, or Bad Inputs)                                                                                                                                                                                                                                                                                                      |
| Amazon API Gateway                                  | • AWS WAF missing bot and scraper rules<br>• Resource has no firewall attached for protection<br>• AWS WAF missing all rules - no protection, possible misconfiguration<br>• AWS WAF missing key AWS Managed Rules (IP Reputation, Common Rules, or Bad Inputs)                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Amazon CloudFront                                   | • AWS WAF missing bot and scraper rules<br>• DDoS activity detected<br>• Resource has no firewall attached for protection<br>• AWS WAF missing all rules - no protection, possible misconfiguration<br>• AWS WAF missing key AWS Managed Rules (IP Reputation, Common Rules, or Bad Inputs)                                                                                                                                                                                                                                                                                                                                                                                        |
| Amazon Elastic Compute Cloud (EC2) instance         | • Allows unrestricted inbound access (0.0.0.0/0) on all ports<br>• Allows unrestricted inbound access (0.0.0.0/0) to RDP port 3389<br>• Allows unrestricted inbound access (0.0.0.0/0) to SSH port 22<br>• Allows unrestricted outbound access (0.0.0.0/0) on all ports<br>• Resource has no firewall attached for protection<br>• CloudFront origin is also Internet accessible without CloudFront protections<br>• Resource has no firewall attached for protection<br>• AWS WAF missing bot and scraper rules<br>• AWS WAF missing all rules - no protection, possible misconfiguration<br>• AWS WAF missing key AWS Managed Rules (IP Reputation, Common Rules, or Bad Inputs) |
| VPC security group                                  | • Allows unrestricted inbound access (0.0.0.0/0) on all ports<br>• Allows unrestricted inbound access (0.0.0.0/0) to RDP port 3389<br>• Allows unrestricted inbound access (0.0.0.0/0) to SSH port 22<br>• Allows unrestricted outbound access (0.0.0.0/0) on all ports                                                                                                                                                                                                                                                                                                                                                                                                            |
| VPC network access control list (NACL)              | • Allows unrestricted inbound access (0.0.0.0/0) on all ports<br>• Allows unrestricted inbound access (0.0.0.0/0) to RDP port 3389<br>• Allows unrestricted inbound access (0.0.0.0/0) to SSH port 22<br>• Allows unrestricted outbound access (0.0.0.0/0) on all ports                                                                                                                                                                                                                                                                                                                                                                                                            |
| AWS WAF web ACL                                     | • Bot activity detected<br>• AWS WAF missing bot and scraper rules<br>• AWS WAF WebACL is not associated with any resources<br>• AWS WAF missing all rules - no protection, possible misconfiguration<br>• AWS WAF missing key AWS Managed Rules (IP Reputation, Common Rules, or Bad Inputs)                                                                                                                                                                                                                                                                                                                                                                                      |
