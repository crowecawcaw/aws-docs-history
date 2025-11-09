# Example use cases for evidence

finder

Evidence finder can help you with several use cases. This page provides some examples and
suggests the search filters that you can use in each scenario.

###### Topics

- [Use case 1: Find non-compliant evidence and organize
  delegations](#use-case-find-non-compliant-evidence "#use-case-find-non-compliant-evidence")
- [Use case 2: Identify compliant evidence](#use-case-find-compliant-evidence "#use-case-find-compliant-evidence")
- [Use case 3: Perform a quick preview of evidence resources](#use-case-evidence-preview "#use-case-evidence-preview")

## Use case 1: Find non-compliant evidence and organize

delegations

This use case is ideal if you’re a compliance officer, a data protection officer, or a GRC
professional who oversees audit preparation.

As you monitor the compliance posture for your organization, you might rely on partner
teams to help you remediate issues. You can use evidence finder to help you organize your work
for your partner teams.

By applying filters, you can focus on evidence for one area at a time. Moreover, you can
also stay aligned with the responsibilities and scope of each partner team that you work with.
By performing a targeted search in this way, you can use the search results to identify what
exactly needs remediating in each subject area. You can then delegate that non-compliant
evidence to the corresponding partner team for remediation.

For this workflow, follow the steps to [search for
evidence](search-for-evidence-in-evidence-finder.md "search-for-evidence-in-evidence-finder.md"). Use the following filters to find non-compliant evidence.

```
Assessment | `<assessment name>`
Date range | `<date range>`
Resource compliance | `Non-compliant`
```

Next, apply additional filters for the area that you're focusing on. For example, use the
**Service category** filter to find non-compliant resources that are related
to IAM. Then, share those results with the team that owns IAM resources for your
organization. Or, if you're querying an assessment that was created from a standard framework,
you can use the **Control domain** filter to find non-compliant evidence that's
related to the identity and access management domain.

```
Control domain | `<domain that you're focusing on>`
or
Service category | `<AWS service category that you're focusing on>`
```

After you find the evidence that you need, follow the steps to generate an assessment
report from your search results. For instructions, see [Generating an assessment report
from your search results](exporting-search-results-from-evidence-finder.md#generate-one-time-report-from-search-results "exporting-search-results-from-evidence-finder.md#generate-one-time-report-from-search-results"). You can share this report with
your partner team, who can use it as a remediation checklist.

## Use case 2: Identify compliant evidence

This use case is ideal if you work in SecOps, IT/DevOps, or another role that owns and
remediates cloud assets.

As part of an audit, you might be asked to remediate issues with the resources that you
own. After you do this work, you can use evidence finder to validate that your resources are
compliant.

For this workflow, follow the steps to [search for
evidence](search-for-evidence-in-evidence-finder.md "search-for-evidence-in-evidence-finder.md"). Use the following filters to find compliant evidence.

```
Assessment | `<assessment name>`
Date range | `<date range>`
Resource compliance | `Compliant`
```

Next, apply additional filters to show only the evidence that you’re responsible for.
Depending on your ownership scope, make the search as targeted as needed. The following filter
examples are ordered from broadest to most precise. Choose the appropriate options for you, and
replace the `<placeholder text>` with your own values.

```
Control domain | `<a subject area that you're responsible for>`
Service category | `<a category of AWS services that you own>`
Service | `<a specific AWS service that you own>`
Resource type | `<a collection of resources that you own>`
Resource ARN | `<a specific resource that you own>`
```

If you’re responsible for multiple instances of the same criteria (for example, you own
multiple AWS services), you can [group your
results](evidence-finder-filters-and-groups.md#groups "evidence-finder-filters-and-groups.md#groups") by that value. This provides you with the total evidence matches for each
AWS service. You can then get the results for the services that you own.

## Use case 3: Perform a quick preview of evidence resources

This use case is ideal for all Audit Manager customers.

Previously, it was time consuming to review individual evidence details. If you wanted to
preview evidence, you had to go directly to that assessment, then navigate through deeply nested
evidence folders. Now, evidence finder provides a convenient way to preview this information.
For each evidence item that matches your search query, you can preview the individual resources
for that evidence.

To get started, follow the steps to [search for
evidence](search-for-evidence-in-evidence-finder.md "search-for-evidence-in-evidence-finder.md"). Then, select the radio button next to a result to see a resource summary in
the current page. You can preview each individual resource that relates to an evidence item. To
see the full evidence details for any resource, choose the evidence name. For more information,
see [Previewing resource summaries](viewing-search-results-in-evidence-finder.md#preview-evidence "viewing-search-results-in-evidence-finder.md#preview-evidence").

![An example of a search result and the on-screen resource summary for that result.](images/evidence-finder-preview-console.png)
