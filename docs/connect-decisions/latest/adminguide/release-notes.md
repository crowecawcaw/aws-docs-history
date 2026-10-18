

# Release Notes
<a name="release-notes"></a>

 We recommend subscribing to the RSS feed so updates to these notes are delivered to you automatically. Choose the RSS button at the top of this page and copy the feed URL into your RSS reader. For example, you can subscribe to an RSS feed in Outlook. 

## October 2026 Updates
<a name="release-notes-october-2026"></a>

### Amazon Connect Decisions adds bulk assignment of data access
<a name="release-notes-bulk-assignment-of-data-access"></a>

 Administrators can now assign roles and grant or revoke product and site access for many users at once. Upload a CSV to create new users, change roles, and add or remove product and site access across your instance in a single run, instead of editing one user at a time. Before anything is applied, a review step shows every proposed change — new users, access added, access removed, no change, and any errors — so you can confirm the full set first. After applying, you can download a report of exactly what changed for each user, and download an error report if a file is rejected. This capability is available to administrators only. 

## September 2026 Updates
<a name="release-notes-september-2026"></a>

### Amazon Connect Decisions improves insights filtering performance and scoping
<a name="release-notes-insights-filtering-performance"></a>

 The insights listing page now opens pre-scoped to the records each user has access to, so planners see only their own insights on arrival. 

### Amazon Connect Decisions adds a daily adoption view in natural language
<a name="release-notes-daily-adoption-view"></a>

 You can now ask for a daily breakdown of insights by status and by the person who acted on each one. This gives team leads visibility into how insights are being reviewed and resolved day to day, supporting adoption tracking and change management across planning teams. 

## August 2026 Updates
<a name="release-notes-august-2026"></a>

### Amazon Connect Decisions introduces order rescheduling for Supply Intelligence
<a name="release-notes-order-rescheduling"></a>

 You can now auto-update order quantities without changing dates. When a date change is needed, the system zeros out the existing order and creates a new planned order, reducing manual coordination between planners and procurement. 

### Amazon Connect Decisions now delivers faster, natural language responses
<a name="release-notes-faster-natural-language-responses"></a>

 All natural language interactions are now fully streamed, delivering first responses in under 3 seconds. The agent surfaces its thinking in real time so you can follow along and redirect if needed. 

### Amazon Connect Decisions adds guided setup through conversation
<a name="release-notes-guided-setup-through-conversation"></a>

 You can now configure metrics, rules, and thresholds through a guided conversation with your Teammate. The Teammate analyzes your data, recommends optimal thresholds and previews what would trigger. 

### Amazon Connect Decisions adds support for customer managed keys
<a name="release-notes-customer-managed-keys"></a>

 You can now use your own AWS KMS customer managed keys to encrypt data in Amazon Connect Decisions. If you have data sovereignty or compliance requirements, this gives you full control over key lifecycle, rotation, and access policies. To learn more, see [Customer managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html). 

### Amazon Connect Decisions now supports custom permission roles
<a name="release-notes-custom-permission-roles"></a>

 Amazon Connect Decisions now enables administrators to create custom permission roles with granular control over what each user can access. Previously, access control was limited to three fixed roles (Admin, Manager, Planner). With custom roles, you can define permission sets that match your organizational structure by selecting Create, Read, Update, and Delete operations across a visual permission matrix covering Insights, Plans, and Management. You can create up to 100 custom roles per instance, and permission changes take effect on the user's next action with no refresh or re-login required. Default roles remain available and cannot be modified. For more information, see [Overview of roles and permissions](https://docs.aws.amazon.com/connect-decisions/latest/adminguide/overview-roles-permissions.html). 