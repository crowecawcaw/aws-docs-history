# Troubleshooting customer

segments in Amazon Connect

## The Customer segments option doesn't appear in the left navigation

panel

If a **Customer segments** option does not exist in Amazon Connect admin website
left navigation panel, check if the user's security profiles has the
**Customer segment - View** permission. For more
information, see [Assign security
profile permissions to manage customer segments](security-profile-customer-profile-segmentation.md "security-profile-customer-profile-segmentation.md"). After the
permission is updated, refresh the Amazon Connect admin website page to reflect the change.

## Export

CSV button not available, or export job timed out

Exporting a segment that contains more than 350,000 profiles is not supported
in the Amazon Connect admin website. Alternatively, we recommend exporting this type of segment to an
Amazon S3 bucket using the `CreateSegmentSnapshot` API through the command
line reference (CLI) or SDK.

## Error: You

reached the limit of 60 unique attributes

This error occurs when the number of unique attributes in the segment
definition exceeds the quota. The number of unique attributes are counted
including the starting audiences recursively.

###### Solutions

- Reduce the number of unique attributes by removing audience filters
  in the segment definition, or removing starting audiences that contains
  audience filters.
- [Request a quota
  increase](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md") for the service quotas - Maximum number of unique
  attributes in segment

For more about default service quota, see [Amazon Connect Customer Profiles service quotas](../../../general/latest/gr/connect_region.md#limits_customer_profiles "../../../general/latest/gr/connect_region.md#limits_customer_profiles").

## Error: You reached the limit of 10 unique calculated attributes

This error occurs when the number of unique calculated attributes in the
segment definition exceeds the quota. The number of unique calculated attributes
are counted including the starting audiences recursively.

###### Solutions

- Reduce the number of unique calculated attributes by removing
  audience filters on calculated attributes in the segment definition, or
  removing starting audiences that contains audience filters on calculated
  attributes.
- [Request a quota
  increase](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md") for the service quotas - Maximum number of unique
  calculated attributes in segment.

For more about default service quota, see [Amazon Connect Customer Profiles service quotas](../../../general/latest/gr/connect_region.md#limits_customer_profiles "../../../general/latest/gr/connect_region.md#limits_customer_profiles").

## Error: You reached the limit of 5 depth of starting audiences

This error occurs when the depth of starting audiences exceeds the quota. The
depth is counted recursively for all of the starting audiences in your audience
group. For example, if you select a segment "Eligible rental upgrade" as a
starting audience, and the segment "Eligible rental upgrade" has another segment
as a starting audience, the depth will be 2.

###### Solution

- Remove one or more starting audiences in your audience group that
  contains deeply nested starting audiences.

For more about default service quotas, see [Amazon Connect Customer Profiles service quotas](../../../general/latest/gr/connect_region.md#limits_customer_profiles "../../../general/latest/gr/connect_region.md#limits_customer_profiles").
