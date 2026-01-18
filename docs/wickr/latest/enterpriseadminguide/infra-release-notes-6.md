This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Infrastructure 6.34 release

The following release notes include information for infrastructure release 6.34. For
information on the release timeline, see [Change log](#infra-release-notes-6.34-change-log "#infra-release-notes-6.34-change-log").

**Platform version**

|                |                                                                        |
| -------------- | ---------------------------------------------------------------------- |
| Infrastructure | 6.34.1<br>Replicated Native Scheduler (1928)<br>Replicated KOTS (1377) |

**New features**:

- Global Federation is now available between AWS WickrGov networks and Wickr Enterprise
  deployments.
- New Wickr Enterprise infrastructure is now available for non-AWS cloud deployments and
  on-premises deployments. This new architecture, based on Kubernetes, improves scalability and
  fault tolerance. The deployment is tested on RKE2.
- Network administrators can now view and manipulate usage dashboards.
  **Changes and resolved issues**:

Fixed a return error code before doLogin when device details are not found in the database,
preventing suspended users on iOS from viewing content.

**Improvements**:

- Removed reference to Wickr Me in admin Global Federation options.
- Allow a superadmin to configure password policy.

## Change log

**Change log for 6.34 release and release notes**

| Change                | Description                                                                             | Date           |
| --------------------- | --------------------------------------------------------------------------------------- | -------------- |
| Final release         | Final notes with Replicated build number                                                | March 28, 2024 |
| Infrastructure update | Updates to address vulnerability scan results, new features, fixes, and<br>improvements | March 26, 2024 |
| Initial release       | Initial release of March release notes                                                  | March 20, 2024 |
