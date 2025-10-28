# Amazon DocumentDB Extended Support

Amazon DocumentDB Extended Support allows you to continue running an engine version past the end of the standard support date for an additional cost.
Your clusters are enrolled into Extended Support once past the end of the standard support date.
If you do not complete upgrades by the end of the engine version standard support date, your clusters are billed at the Extended Support rate.

###### Topics

- [Extended Support overview](#support-overview "#support-overview")
- [Extended Support charges](support-charges.md "support-charges.md")
- [Responsibilities](support-responsibilities.md "support-responsibilities.md")
  Amazon DocumentDB Extended Support provides the following updates and technical support:

- Security updates for [critical and high CVEs](https://nvd.nist.gov/vuln-metrics/cvss "https://nvd.nist.gov/vuln-metrics/cvss") for your instance or cluster
- Bug fixes and patches for critical issues
- The ability to open support cases and receive troubleshooting help within the standard Amazon DocumentDB service level agreement
  This paid offering gives you more time to upgrade to a supported engine version.
  For example, Amazon DocumentDB end of standard support date for version 3.6 is March 30, 2026, however you aren't ready to upgrade to version 5.0 before that date.
  In this case, Amazon DocumentDB enrolls your version 3.6 cluster in Extended Support so you can continue to use Amazon DocumentDB version 3.6.
  Starting March 31, 2026, AWS charges you an Extended Support premium for Amazon DocumentDB version 3.6 clusters.

Amazon DocumentDB Extended Support is available for up to 3 years past the engine version standard support date.
After this time, if you haven't upgraded your engine version to a supported version, then Amazon DocumentDB will upgrade your engine version.
We recommend that you upgrade to a supported engine version as soon as possible.

Amazon DocumentDB version 3.6 end of standard support date and Extended Support dates:

- **Release of version 3.6** — 9 January 2019
- **End of version 3.6 standard support** — 30 March 2026
- **Start of version 3.6 Extended Support year 1 pricing** — 31 March 2026
- **Start of version 3.6 Extended Support year 3 pricing** — 31 March 2028
- **End of version 3.6 Extended Support** — 30 March 2029

## Extended Support overview

Amazon DocumentDB upgrades your cluster to the last engine version released (before the end of the Extended Support date), if your cluster is not already on that version.
The upgrade period will not occur until after the standard support date for that engine version.

You can create new clusters with an engine version that has reached the end of standard support date, if you already have a cluster on that engine version.
Amazon DocumentDB enrolls these new clusters in Amazon DocumentDB Extended Support and charges you for this offering.
If you upgrade to an engine version that's still under Amazon DocumentDB standard support before version 3.6's end of standard support date, you will not be charged an Extended Support premium.

You can end enrollment in Amazon DocumentDB Extended Support at any time.
To end enrollment, upgrade each enrolled cluster to a newer engine version that is still under Amazon DocumentDB standard support.
The end of Amazon DocumentDB Extended Support enrollment will be effective the day that you complete an upgrade to a newer engine version that is still under Amazon DocumentDB standard support.

For more information about Amazon DocumentDB end of standard support dates and Amazon DocumentDB end of Extended Support dates, see [Amazon DocumentDB engine version support dates](docdb-version-support-dates.md "docdb-version-support-dates.md").
