This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Bots 6.32 release

The following release notes include information for bots release 6.32. For information on
the release timeline, see [Change log](#bots-release-notes-6.32-change-log "#bots-release-notes-6.32-change-log").

**Platform versions**

|     |        |
| --- | ------ |
| Bot | 6.32.4 |

**Changes, enhancements, and resolved issues:**

- References to the default NPM registry were found in some code. Changes were made to
  ensure that the Airgap version does not reference any NPM registry.
- Fixed software not decoding read receipt API call responses correctly
- Fixed a race condition that was causing initial registrations to fail
- Changes were made to stop sending requests for read receipt status after one week for
  broadcasts.

## Change log

**Change log for 6.32 release and release notes**

| Change          | Description                             | Date              |
| --------------- | --------------------------------------- | ----------------- |
| Bots update     | Bug fix updates                         | February 26, 2024 |
| Initial release | Initial release of August release notes | February 21, 2024 |
