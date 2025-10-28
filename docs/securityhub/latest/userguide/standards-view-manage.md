# Understanding security standards in Security Hub CSPM

In AWS Security Hub CSPM, a _security standard_ is a set of
requirements that's based on regulatory frameworks, industry best practices, or company
policies. For details about the standards that Security Hub CSPM currently supports, including the
security controls that apply to each one, see the [Standards reference for Security Hub CSPM](standards-reference.md "standards-reference.md").

When you enable a standard, Security Hub CSPM automatically enables all the controls that apply to the
standard. Security Hub CSPM then runs security checks on the controls, which generates Security Hub CSPM findings.
You can disable and later re-enable individual controls as necessary. You can also disable a
standard completely. If you disable a standard, Security Hub CSPM stops running security checks on
controls that apply to the standard. Findings are no longer generated for the
controls.

In addition to findings, Security Hub CSPM generates a security score for each standard that you
enable. The score is based on the status of the controls that apply to the standard. If you
set an aggregation Region, the security score for a standard reflects the status of the
controls across all linked Regions. If you're the Security Hub CSPM administrator for an organization,
the score reflects the status of the controls for all the accounts in your organization. For
more information, see [Calculating security scores](standards-security-score.md "standards-security-score.md").

To review and manage standards, you can use the Security Hub CSPM console or the Security Hub CSPM API. On the
console, the **Security standards** page shows all the security standards
that Security Hub CSPM currently supports. This includes a description of each standard and the current
status of the standard. If you enable a standard, you can also use this page to access
additional details for the standard. For example, you can review:

- The current security score for the standard.
- Aggregated statistics for controls that apply to the standard.
- A list of controls that apply to the standard and are currently enabled, including
  the compliance status of each one.
- A list of controls that apply to the standard but are currently disabled.
  For deeper analysis, you can filter and sort the data, and drill down to review the
  details of individual controls that apply to the standard.

You can enable standards individually for a single account and AWS Region. However, to
save time and reduce configuration drift in multi-account and multi-Region environments, we
recommend using [central configuration](central-configuration-intro.md "central-configuration-intro.md") to
enable and manage standards. With central configuration, the delegated Security Hub CSPM administrator
can create policies that specify how to configure a standard across multiple accounts and
Regions.

###### Topics

- [Standards reference](standards-reference.md "standards-reference.md")
- [Enabling a standard](enable-standards.md "enable-standards.md")
- [Reviewing the details of a standard](securityhub-standards-view-controls.md "securityhub-standards-view-controls.md")
- [Turning off auto-enabled standards](securityhub-auto-enabled-standards.md "securityhub-auto-enabled-standards.md")
- [Disabling a standard](disable-standards.md "disable-standards.md")
