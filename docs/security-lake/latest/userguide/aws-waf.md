# AWS WAF logs in Security Lake

When you add AWS WAF as a log source in Security Lake, Security Lake immediately starts collecting the
logs. AWS WAF is a web application firewall that you can use to monitor web requests
that your end users send to your applications and to control access to your content.
Logged information includes the time that AWS WAF received a web request from your AWS
resource, detailed information about the request, and details about the rules that the
request matched.

Security Lake consumes AWS WAF logs directly from AWS WAF through an independent and duplicate
stream of logs. This process is designed to not require
additional setup or affect existing AWS WAF configurations.
Security Lake logs only retrieve data that's permitted by the AWS WAF
[web access
control list (web ACL)](../../../waf/latest/developerguide/web-acl.md "../../../waf/latest/developerguide/web-acl.md") configuration. If [Data protection](../../../waf/latest/developerguide/waf-data-protection-and-logging.md "../../../waf/latest/developerguide/waf-data-protection-and-logging.md")
is enabled for the web ACL in Security Lake accounts, the generated data will be redacted or hashed based on
your web ACL settings. For information about using AWS WAF to protect your application resources, see
[How AWS WAF works](../../../waf/latest/developerguide/how-aws-waf-works.md "../../../waf/latest/developerguide/how-aws-waf-works.md") in the _AWS WAF Developer Guide_.

###### Important

If you are using Amazon CloudFront distribution as the resource type in AWS WAF, you must
select US East (N. Virginia) to ingest the global logs in Security Lake.

AWS WAF logs is supported only in OCSF v1.1.0. For information about how Security Lake
normalizes AWS WAF log events to OCSF, see the mapping reference in the [GitHub OCSF repository for AWS WAF logs (v1.1.0)](https://github.com/ocsf/examples/tree/main/mappings/markdown/AWS/v1.1.0/WAF "https://github.com/ocsf/examples/tree/main/mappings/markdown/AWS/v1.1.0/WAF").
