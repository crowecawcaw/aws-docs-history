# Enrich security logs and findings

## Enrichment with threat intelligence

and organizational context

During the course of analysis, observables of interest require enrichment for
enhanced contextualization of the alert. As stated in the Preparation section, integrating
and leveraging cyber threat intelligence can be helpful to understand more about a
security finding. Threat intelligence services are used to assign reputation and attribute
ownership to public IP addresses, domain names, and file hashes. These tools are available
as paid and no charge services.

Customers adopting Amazon Athena as a log querying tool gain the advantage of AWS
Glue jobs to load threat intelligence information as tables. The threat intelligence
tables can be used in SQL queries to correlate log elements such as IP addresses and
domain names, providing an enriched view of the data to be analyzed.

AWS does not provide threat intelligence directly to customers, but services such as
Amazon GuardDuty makes use of threat intelligence for enrichment and finding generation.
You can also upload custom threat lists to GuardDuty based on your own threat
intelligence.

## Enrichment with automation

Automation is an integral part of AWS Cloud governance. It can be used throughout
the various phases of the incident response lifecycle.

For the detection phase, rule-based automation matches patterns of interest from the
threat model in logs and takes appropriate action, such as sending notifications. The
analysis phase can leverage the detection mechanism and forward the alert body to an
engine capable of querying logs and enriching observables for contextualization of the
event.

The alert body, in its fundamental form, is comprised of a _resource_ and an _identity_. As an example,
you could implement an automation to query CloudTrail for AWS API activity performed by the
alert body’s identity or resource around the time of the alert, providing additional
insights including `eventSource`, `eventName`,
`SourceIPAddress`, and `userAgent` of identified API activity. By
performing these queries in an automated way, responders can save time during triage and
get additional context to help make better informed decisions.

Refer to the [How to enrich AWS Security Hub findings with account metadata](https://aws.amazon.com/blogs/security/how-to-enrich-aws-security-hub-findings-with-account-metadata/ "https://aws.amazon.com/blogs/security/how-to-enrich-aws-security-hub-findings-with-account-metadata/") blog post for an
example on how to use automation to enrich security findings and simplify analysis.
