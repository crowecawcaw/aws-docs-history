# Getting started with Amazon Detective

This tutorial provides an introduction to Amazon Detective. You'll learn how to enable Detective for your AWS account.
You'll also learn how to verify that Detective has begun to ingest and extract data from your AWS account into your behavior graph.

When you enable Amazon Detective, Detective creates a Region-specific behavior graph that has your
account as its administrator account. This is initially the only account in the behavior graph.
The administrator account can then invite other AWS accounts to contribute their data to the
behavior graph. See [Managing accounts in Detective](accounts.md "accounts.md").

Enabling Detective in a Region for the first time also begins a 30-day free trial for the
behavior graph. If the account disables Detective and then enables it again, no free trial is
available. See [About the free trial for behavior graphs](free-trial-overview.md "free-trial-overview.md").

After the free trial, each account in the behavior graph is billed for the data they
contribute to it. The administrator account can track the usage and see the total projected cost
for a typical 30-day period for their entire behavior graph. For more information, see [Monitoring usage for a Detective administrator account](usage-tracking-admin.md "usage-tracking-admin.md"). Member accounts can track the usage and projected cost for
the behavior graphs that they belong to. For more information, see [Monitoring usage for a Detective member account](member-usage-tracking.md "member-usage-tracking.md").

###### Topics

- [Setting up your AWS account](detective-before-you-begin.md "detective-before-you-begin.md")
- [Prerequisites to enable Detective](detective-prerequisites.md "detective-prerequisites.md")
- [Recommendations to enable Detective](detective-recommendations.md "detective-recommendations.md")
- [Enabling Detective](detective-enabling.md "detective-enabling.md")
