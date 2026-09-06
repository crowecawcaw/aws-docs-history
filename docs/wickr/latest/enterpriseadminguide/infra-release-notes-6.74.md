This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Infrastructure 6.74 release

The following release notes include information for infrastructure release 6.74. For
information on the release timeline, see [Change log](#infra-release-notes-6.74-change-log "#infra-release-notes-6.74-change-log").

**Platform version**

| Platform       | Version |
| -------------- | ------- |
| Infrastructure | 6.74    |

**Changes, enhancements, and resolved issues:**

- **Storage backend migration** — For deployments that use
  internal S3 storage, this release migrates the storage backend from MinIO to SeaweedFS to
  improve file transfer reliability and performance. The migration runs automatically in the
  background after upgrade with zero downtime and no manual steps. Your existing data remains
  accessible throughout the migration and is preserved until you choose to remove the legacy
  storage. Deployments that use external S3 storage are not affected.
- **Embedded cluster** — Updated to Kubernetes 1.33.
- **Valkey** — Replaced Redis with Valkey for in-memory
  session storage. The migration runs automatically during upgrade with zero downtime, and users
  are not required to sign in again.
- General enhancements and bug fixes.
  **Required update**: Deployments that use internal S3 storage require
  approximately twice the normal storage capacity temporarily during the automatic migration.
  Ensure sufficient disk space is available, and do not apply configuration changes while the
  migration is in progress. After you have verified that file uploads and downloads work correctly,
  you can remove the legacy MinIO storage to reclaim the additional capacity.

## Change log

**Change log for 6.74 release and release notes**

| Change                | Description                             | Date            |
| --------------------- | --------------------------------------- | --------------- |
| Infrastructure update | Initial release of August release notes | August 27, 2026 |
