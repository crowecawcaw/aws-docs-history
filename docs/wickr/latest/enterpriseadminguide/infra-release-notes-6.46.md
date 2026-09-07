

This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html).

# Infrastructure 6.46 release
<a name="infra-release-notes-6.46"></a>

The following release notes include information for infrastructure release 6.46. For information on the release timeline, see [Change log](#infra-release-notes-6.46-change-log).

**Platform version**


|  |  | 
| --- | --- | 
| Infrastructure | 6.46.1 <br />Replicated Native Scheduler (2080)<br />Replicated KOTS (1785) | 

**New features**:

Customers can now establish global federation with other Wickr Enterprise deployments and AWS Wickr networks using self-signed certificates.

**Improvements**: 
+ A new federated outbox has been introduced to provide a more reliable messaging send flow across global federation.
+ Added the ability to monitor the TLS certificate file change and automatically restart TCPProxy for the new certificate to take effect.

## Change log
<a name="infra-release-notes-6.46-change-log"></a>

**Change log for 6.46 release and release notes**


| Change | Description | Date | 
| --- | --- | --- | 
| Final release | Final notes with Replicated build number | October 16, 2024 | 
| Infrastructure update | Updates to address vulnerability scan results and improvements | October 16, 2024 | 