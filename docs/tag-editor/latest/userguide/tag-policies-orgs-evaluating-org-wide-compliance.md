# Evaluating

organization-wide compliance

You can evaluate your organization's compliance with its effective tag policy. You can
generate a report that lists all tagged resources in accounts across your organization and
whether each resource is compliant with the effective tag policy.

###### Important

Untagged resources don't appear as noncompliant in results.

To find untagged resources in your account, use AWS Resource Explorer with a query that uses
`tag:none`. For more information, see [Search for untagged resources](../../../resource-explorer/latest/userguide/using-search-query-examples.md#example-1 "../../../resource-explorer/latest/userguide/using-search-query-examples.md#example-1") in the _AWS Resource Explorer
User Guide_.

You can generate the report from your organization's management account in the
`us-east-1` AWS Region only. The account generating the report must have
access to an Amazon S3 bucket in the US East (N. Virginia) Region. The bucket must have an attached
bucket policy as shown in [Amazon S3
bucket policy for storing report](tag-policies-orgs.md#bucket-policy "tag-policies-orgs.md#bucket-policy").

To generate an organization-wide compliance report, you must have the following
permissions:

- `organizations:DescribeEffectivePolicy`
- `tag:GetComplianceSummary`
- `tag:StartReportCreation`
- `tag:DescribeReportCreation`
- `s3:ListAllMyBuckets`
- `s3:GetBucketAcl`
- `s3:GetObject`
- `s3:PutObject`
  For an example IAM policy displaying these permissions, review [Permissions for evaluating organization-wide compliance](tag-policies-orgs.md#tag-policies-permissions-org "tag-policies-orgs.md#tag-policies-permissions-org").

###### To generate an organization-wide compliance report (console)

1. Open the [Tag Policies
   console](https://console.aws.amazon.com/resource-groups/tag-policies/ "https://console.aws.amazon.com/resource-groups/tag-policies/").
2. Choose the **This organization root** tab, and near the bottom of
   the page, choose **Generate report**.
3. On the **Generate report** screen, specify where to store the
   report.
4. Choose **Start exporting**.
   When the report is complete, you can download it from the **Noncompliance
   report** section on the **Organization root** tab.

###### Notes

Organization-wide compliance is evaluated every 48 hours. This results in the
following:

- It can take up to 48 hours for changes to a tag policy or resources to be
  shown in the organization-wide compliance report. For example, assume that you
  have a tag policy that defines a new standardized tag for a resource type.
  Resources of that type that don't have this tag can show as compliant in the
  report for up to 48 hours.
- Although you can generate the report at any time, report results aren't
  updated until the next evaluation is complete.
- The **NoncompliantKeys** column lists tag keys on the
  resource that are noncompliant with the effective tag policy.
- The **KeysWithNonCompliantValues** column lists keys defined
  in the effective policy that are on the resource with either incorrect case
  treatment or noncompliant values.
- If you close an AWS account that was a member of the organization, it can
  continue to appear in the tag compliance report for up to 90 days.

###### To generate an organization-wide compliance report (AWS CLI, AWS API)

Use the following commands and operations to generate an organization-wide compliance
report, check on its status, and view the report:

- AWS Command Line Interface AWS CLI):

      + [aws resourcegroupstaggingapi
       start-report-creation](../../../cli/latest/reference/resourcegroupstaggingapi/start-report-creation.md "../../../cli/latest/reference/resourcegroupstaggingapi/start-report-creation.md")
      + [aws resourcegroupstaggingapi
       describe-report-creation](../../../cli/latest/reference/resourcegroupstaggingapi/describe-report-creation.md "../../../cli/latest/reference/resourcegroupstaggingapi/describe-report-creation.md")
      + [aws resourcegroupstaggingapi
       get-compliance-summary](../../../cli/latest/reference/resourcegroupstaggingapi/get-compliance-summary.md "../../../cli/latest/reference/resourcegroupstaggingapi/get-compliance-summary.md")

  For the complete procedure for using tag policies in the AWS CLI, see [Using tag policies
  in the AWS CLI](../../../organizations/latest/userguide/tag-policy-cli.md "../../../organizations/latest/userguide/tag-policy-cli.md") in the _AWS Organizations User Guide_.

- AWS API:
  - [StartReportCreation](../../../resourcegroupstagging/latest/APIReference/API_StartReportCreation.md "../../../resourcegroupstagging/latest/APIReference/API_StartReportCreation.md")
  - [DescribeReportCreation](../../../resourcegroupstagging/latest/APIReference/API_DescribeReportCreation.md "../../../resourcegroupstagging/latest/APIReference/API_DescribeReportCreation.md")
  - [GetComplianceSummary](../../../resourcegroupstagging/latest/APIReference/API_GetComplianceSummary.md "../../../resourcegroupstagging/latest/APIReference/API_GetComplianceSummary.md")
