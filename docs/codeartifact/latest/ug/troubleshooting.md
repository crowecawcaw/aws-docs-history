# Troubleshooting AWS CodeArtifact

The following information might help you troubleshoot common issues with CodeArtifact.

For information about troubleshooting format-specific issues, see the following topics:

- [Maven troubleshooting](maven-troubleshooting.md "maven-troubleshooting.md")
- [Swift troubleshooting](swift-troubleshooting.md "swift-troubleshooting.md")

## I cannot view notifications

**Problem:** When you are in the Developer Tools console and choose
**Notifications** under **Settings**, you see a
permissions error.

**Possible fixes:** While notifications are a feature of the Developer Tools console, CodeArtifact does not currently support notifications.
None of the managed policies for CodeArtifact include permissions
that allow users to view or manage notifications. If you use other services in the Developer Tools console, and those services support notifications, the managed policies
for those services include the permissions required to view and manage notifications for those services.
