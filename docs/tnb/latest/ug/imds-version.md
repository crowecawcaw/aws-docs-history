

# IMDS version
<a name="imds-version"></a>

AWS TNB supports instances that leverage Instance Metadata Service version 2 (IMDSv2), a session-oriented method. IMDSv2 includes higher security than IMDSV1. For more information, see [Add defense in depth against open firewalls, reverse proxies, and SSRF vulnerabilities with enhancements to the Amazon EC2 Instance Metadata Service](https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/).

When launching your instance, you must use IMDSv2. For more information on IMDSv2, see [Use IMDSv2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html) in the *Amazon EC2 User Guide*.