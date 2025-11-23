# Supporting Unified Search in the

AWS Management Console

The AWS Management Console has a search bar at the top of every console page. This provides a
[Unified Search](../../../awsconsolehelpdocs/latest/gsg/using-search.md "../../../awsconsolehelpdocs/latest/gsg/using-search.md") experience across all AWS services. Unified Search results can
include such things as:

- AWS service and feature console pages.
- AWS documentation pages.
- AWS blog and Knowledge Base articles
- Resources in your accounts — if have at minimum read-only access.
  The account resources you can view in your Unified Search results depend on the
  permissions assigned to you.

- Partial Regional results: With, at minimum, the permissions in the
  `AWSResourceExplorerReadOnlyAccess` managed policy, you can can
  immediately search all tagged resources and supported untagged resources created
  after the immediate resource discovery release in a Region.
- Full Regional results: With at minimum, the permissions in the
  `AWSResourceExplorerReadOnlyAccess` managed policy and the
  `iam:CreateServiceLinkedRole` permission, you can search full
  results, including all tagged and untagged resources with ongoing automatic updates
  and historical backfill, in a Region.
- Full cross-Region results: If you create an aggregator index, cross-Region results
  are available in Unified Search.
  Unified Search always uses the default view in the AWS Region that contains the
  aggregator index to perform all searches when present.

For more information about resourcer views, see [Permission tiers and user
experiences](manage-immediate-resource-discovery-experience.md#immediate-permission-tiers "manage-immediate-resource-discovery-experience.md#immediate-permission-tiers").
