

This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html).

# Infrastructure 6.62 release
<a name="infra-release-notes-6.62"></a>

The following release notes include information for infrastructure release 6.62. For information on the release timeline, see [Change log](#infra-release-notes-6.62-change-log).

**Platform version**


|  |  | 
| --- | --- | 
| Infrastructure | 6.62<br />Replicated KOTS (2756) | 

**Changes, enhancements, and resolved issues:**
+ MySQL 8 upgrade
+ General enhancements and bug fixes.

**Required Update**: MySQL 8 upgrade is required for all future releases. Version 6.58 must be installed before updating to this release.

## Infrastructure 6.62 (Hotfix) release
<a name="infra-release-notes-6.62-hotfix"></a>

**Platform version**


|  |  | 
| --- | --- | 
| Infrastructure | 6.62.1<br />Replicated KOTS (2778) | 

Changes, enhancements, and resolved issues:

 A race condition occurring during new installations with the Embedded Cluster and Internal MySQL Database option has been resolved. This issue previously caused enterprise-init to run unsuccessfully during initial setup.

## Change log
<a name="infra-release-notes-6.62-change-log"></a>

**Change log for 6.62 release and release notes**


| Change | Description | Date | 
| --- | --- | --- | 
| Infrastructure version 6.62 > Infrastructure version 6.62.1 | Bug fix | December 8, 2025 | 
| Infrastructure update | Initial release of November release notes | November 4, 2025 | 