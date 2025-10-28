# Viewing drift

You can view the drift status for your accounts and OUs through the console or APIs, and identify
when account and OU configurations are _drifted_, or out
of sync. Drift status also is communicated with SNS messages. For more information about receiving these SNS messages, see [Guidance on subscribing to SNS Topics](sns-guidance.md "sns-guidance.md").

To view OU and account drift status in the console, navigate to the **Organization** page, and then select the OUs or accounts that you wish to inspect.

To view drift status for OUs and accounts programmatically, call the
[`ListEnabledBaselines`](../APIReference/API_ListEnabledBaselines.md "../APIReference/API_ListEnabledBaselines.md") API to view statuses for your
enabled baselines. To view statuses for individual accounts programmatically with the
`ListEnabledBaselines` API, use the `includeChildren` flag.
You can filter by these statuses, and see only the accounts and OUs that require
your attention.

###### Note

AWS Control Tower generates a [lifecycle event](lifecycle-events.md "lifecycle-events.md") when each drift remediation operation is completed.
