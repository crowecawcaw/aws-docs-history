# Release Notes

We recommend subscribing to the RSS feed so updates to these notes are delivered to your
Inbox. Choose the RSS link (under the topic title **Release notes**)
and then copy the URL (it ends with `doc-history.xml.rss`) into your RSS
reader. For example, you can subscribe to an RSS feed in Outlook.

## August 2026 Updates

### Amazon Connect Decisions introduces order rescheduling for Supply Intelligence

You can now auto-update order quantities without changing dates. When a date change
is needed, the system zeros out the existing order and creates a new planned order,
reducing manual coordination between planners and procurement.

### Amazon Connect Decisions now delivers faster, natural language responses

All natural language interactions are now fully streamed, delivering first responses
in under 3 seconds. The agent surfaces its thinking in real time so you can follow
along and redirect if needed.

### Amazon Connect Decisions adds guided setup through conversation

You can now configure metrics, rules, and thresholds through a guided conversation
with your Teammate. The Teammate analyzes your data, recommends optimal thresholds
and previews what would trigger.

### Amazon Connect Decisions adds support for customer managed keys

You can now use your own AWS KMS customer managed keys to encrypt data in
Amazon Connect Decisions. If you have data sovereignty or compliance requirements, this
gives you full control over key lifecycle, rotation, and access policies. To learn
more, see [Customer managed keys](../../../kms/latest/developerguide/concepts.md "../../../kms/latest/developerguide/concepts.md").

### Amazon Connect Decisions now supports custom permission roles

Amazon Connect Decisions now enables administrators to create custom permission roles with
granular control over what each user can access. Previously, access control was
limited to three fixed roles (Admin, Manager, Planner). With custom roles, you can
define permission sets that match your organizational structure by selecting Create,
Read, Update, and Delete operations across a visual permission matrix covering
Insights, Plans, and Management. You can create up to 100 custom roles per instance,
and permission changes take effect on the user's next action with no refresh or
re-login required. Default roles remain available and cannot be modified. For more
information, see [Overview of roles and permissions](overview-roles-permissions.md "overview-roles-permissions.md").
