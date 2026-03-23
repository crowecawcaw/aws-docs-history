This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Infrastructure 6.26 release

The following release notes include information for infrastructure release 6.26. For
information on the release timeline, see [Change log](#infra-release-notes-6.26-change-log "#infra-release-notes-6.26-change-log").

**Platform version**

|                |               |
| -------------- | ------------- |
| Infrastructure | 6.26.1 (1799) |

**New features**:

- General availability of guest user access: Wickr Enterprise licensed users can
  communicate with guest users that do not require an AWS account. Each licensed user receives
  five guest users for free. Documentation for this feature is provided in the 6.26 Enterprise
  administrator guide.
- Multitenant domain visibility: In a Wickr Enterprise installation, a superadmin can now
  hide local domains from lower-level admins using a new toggle located in **Local
  Domains for Federation** under the **Global Federation** section of
  the superadmin dashboard. Turning off the toggle hides the **Learn More**
  prompt in the team directory, which prevents the viewing of other local domains associated with
  other networks in the Enterprise deployment.
- Bulk delete and suspend users: Admins can now delete and suspend users by uploading a CSV
  file in the admin dashboard. Wickr provides default templates for this feature.
- SSO token grace period: Admins may now set a grace period for SSO token expiration. The
  options are no grace period, 30 minutes, and 60 minutes. The default setting is for no grace
  period.
  **Changes, enhancements, and resolved issues**:

- Updates to security group authorization logic to no longer authorize on values that are
  not changing.
- Deleting a bot should no longer throw an error.
  **Improvements**:

- Routine service container OS updates to address CVEs.
- Upgrade Expirer and PushDevice to Node18
- Set minimum Docker version to v20.10.10 for Wickr Enterprise.

## Change log

**Change log for 6.26 release and release notes**

| Change                | Description                               | Date              |
| --------------------- | ----------------------------------------- | ----------------- |
| Final release         | Final notes with Replicated build number  | November 14, 2023 |
| Infrastructure update | General availability of guest user access | November 14, 2023 |
| Initial release       | Initial release of November release notes | November 8, 2023  |
