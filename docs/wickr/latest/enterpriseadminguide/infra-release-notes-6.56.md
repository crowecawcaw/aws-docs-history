

This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html).

# Infrastructure 6.56 release
<a name="infra-release-notes-6.56"></a>

The following release notes include information for infrastructure release 6.56. For information on the release timeline, see [Change log](#infra-release-notes-6.56-change-log).

**Platform version**


|  |  | 
| --- | --- | 
| Infrastructure | 6.56.1<br />Replicated KOTS (2279) | 

**New features:**

This release initiates a phased upgrade process to support future features related to security group management. To ensure a smooth transition, existing data will be replicated automatically to new infrastructure components on upgrade. This transition will not impact current Wickr functionality.

**Changes, enhancements, and resolved issues:**

General enhancements and bug fixes.

**Required update**: Database schema changes in this version enable future security group management capabilities.

## Change log
<a name="infra-release-notes-6.56-change-log"></a>

**Change log for 6.56 release and release notes**


| Change | Description | Date | 
| --- | --- | --- | 
| Infrastructure update | Initial release of July release notes | July 21, 2025 | 