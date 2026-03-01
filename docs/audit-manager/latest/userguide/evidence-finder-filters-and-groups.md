# Filter and grouping options for evidence finder

On this page, you can see a list of the filter and grouping options that are available for
you to use in evidence finder.

## Filter reference

You can use the following filters to find evidence that matches specific criteria, such as
an assessment, control, or AWS service.

###### Topics

- [Required filters](#required-filters "#required-filters")
- [Additional filters (optional)](#additional-filters "#additional-filters")
- [Combining filters](#combining-filters "#combining-filters")

### Required filters

Use these filters to get started with a high-level overview of the evidence in an
assessment.

| Filter name             | Description                                                    | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ----------------------- | -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Assessment**          | Returns evidence for a specific assessment.                    | You can filter by one assessment only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Date range**          | Returns evidence for a specific time period.                   | Either, you can use a *Relative range<br>• to define a<br>range that’s relative to today’s date (for example, `Last 30 days`).<br>Or, you can use an *Absolute range<br>• to specify a<br>specific date range (for example, `June 27th – July<br>4th`).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Resource compliance** | Returns resources with a specific compliance check evaluation. | Audit Manager collects [compliance check<br>evidence](concepts.md#evidence "concepts.md#evidence") for controls that use AWS Config and Security Hub CSPM as a data source type. Multiple<br>resources might be assessed during evidence collection. As a result, a single piece of<br>compliance check evidence can include one or more resources. You can use this filter to<br>explore compliance status at the resource level.<br>You can choose one or more of the following options:<br>• **Non-compliant** – This filter finds resources with<br>compliance check issues. This happens if Security Hub reports a *Fail<br>• result, or if AWS Config reports a *Non-compliant<br>• result.<br>• **Compliant** – This filter finds resources that don’t have<br>compliance check issues. This happens if Security Hub CSPM reports a *Pass<br>• result, or if AWS Config reports a *Compliant<br>• result.<br>• **Inconclusive** – This filter finds resources for which a<br>compliance check isn’t available or applicable. This happens if a resource uses AWS Config<br>or Security Hub CSPM as the underlying data source type, but those services aren't enabled. This<br>also happens if the resource uses an underlying data source type that doesn't support<br>compliance checks (such as manual evidence, AWS API calls, or CloudTrail). |

### Additional filters (optional)

Use these filters to narrow the scope of your search query. For example, use
**Service** to see all evidence that's related to Amazon S3. Use
**Resource type** to focus just on S3 buckets. Or, use **Resource
ARN** to target a specific S3 bucket.

You can create additional filters using one or more of the following criteria.

| Criteria name        | Description                               | When to use this criteria                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| -------------------- | ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Account ID**       | Drill down by AWS account.                | Use this criteria to find evidence that's related to a specific<br>AWS account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Control**          | Drill down by control name.               | Use this criteria to find evidence that's related to a specific control.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Control domain**   | Drill down by control domain.             | Use this criteria to focus on a specific subject area as you prepare for an audit.<br>You can filter by control domain if you're querying an assessment that was created from a<br>standard framework.<br>Examples of control domains include network security, identity and access management,<br>and data protection.<br>Some control domains might be marked as **Outdated**<br>following Audit Manager's transition to a new set of control domains provided by AWS Control<br>Catalog. For more information, see [I see that a control domain is marked as “outdated”. What does this mean?](evidence-finder-issues.md#outdated-control-domains "evidence-finder-issues.md#outdated-control-domains"). |
| **Data source type** | Drill down by the type of data source.    | Use this criteria to focus on a specific data source.<br>Set the value to `Manual` to find evidence that you uploaded manually.<br>Otherwise, you can filter automated evidence based on where it came from (for example,<br>`AWS Config`, `CloudTrail`, `Security Hub CSPM`, or `AWS API<br>calls`).                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Event name**       | Drill down by event name.                 | Use this criteria to focus on a specific event that the evidence is related to. An<br>event is a record of an activity in an AWS account.<br>For example, you can search for the name of an API call, such as the IAM<br>`AttachRolePolicy` operation that's used to configure permissions. Or, search<br>for a CloudTrail keyword, such as the `ConsoleLogin` event that's logged by CloudTrail when<br>a user signs in to your account.                                                                                                                                                                                                                                                                   |
| **Resource ARN**     | Drill down by Amazon Resource Name (ARN). | Use this criteria to find evidence that's related to a specific AWS<br>resource.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Resource type**    | Drill down by resource type.              | Use this criteria to focus on the type of resource that's being assessed, such as an<br>Amazon EC2 instance or an S3 bucket.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Service**          | Drill down by AWS service name.           | Use this criteria to find evidence that's related to a specific AWS service, such<br>as Amazon EC2, Amazon S3, or AWS Config.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Service category** | Drill down by AWS service category.       | Use this criteria to focus on a specific category of AWS service. Examples<br>include security, identity and compliance, database, and storage.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

### Combining filters

#### Criteria behavior

When you specify more than one criteria, Audit Manager applies the `AND` operator to
your selections. This means that all of the criteria are grouped into a single query, and the
results must match all of the combined criteria.

###### Example

In the following filter setup, evidence finder returns non-compliant resources from
the last 7 days for the assessment that’s called `MySOC2Assessment`.
Additionally, the results relate to both an IAM policy and the specified control.

![A selection of applied filters, with the AND operator highlighted.](images/evidence-finder-filter_description-console.png)

#### Criteria value behavior

When you specify more than one criteria value, the values are linked with an
`OR` operator. Evidence finder returns results that match any of these criteria
values.

###### Example

In the following filter setup, evidence finder returns search results that come from
either AWS CloudTrail, AWS Config, or AWS Security Hub CSPM.

![An example filter setup that shows multiple values defined for a single criteria.](images/evidence-finder-filter_description-multiple_values-console.png)

## Grouping reference

You can group your search results for quicker navigation. Grouping shows you the breadth of
your search results, and how they're distributed across a specific dimension.

You can use any of the following group by values.

| Group by             | Description                                                            |
| -------------------- | ---------------------------------------------------------------------- |
| **Account ID**       | Group results by AWS account.                                          |
| **Control**          | Group results by control name.                                         |
| **Data source type** | Group results by the type of data source where the evidence came from. |
| **Event name**       | Group results by an event name.                                        |
| **Resource ARN**     | Group results by Amazon Resource Name (ARN).                           |
| **Resource type**    | Group results by resource type.                                        |
| **Service**          | Group results by AWS service name.                                     |
| **Service category** | Group results by AWS service category.                                 |
