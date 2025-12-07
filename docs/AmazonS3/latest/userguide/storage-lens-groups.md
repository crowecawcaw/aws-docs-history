# How S3 Storage Lens groups work

You can use Storage Lens groups to aggregate metrics using custom filters based on
object metadata. When you define a custom filter, you can use prefixes, suffixes, object
tags, object sizes, object age, or a combination of these custom filters. During Storage Lens group
creation, you can also include a single filter or multiple filter conditions. To specify
multiple filter conditions, you use `And` or `Or` logical
operators.

When you create and configure a Storage Lens group, the Storage Lens group itself acts as
a custom filter in the dashboard that you attach the group to. In your dashboard, you can
then use the Storage Lens group filter to obtain storage metrics based on the custom filter that
you defined in the group.

To view the data for your Storage Lens group in your S3 Storage Lens dashboard, you must attach
the group to the dashboard after you've created the group. After your Storage Lens group is
attached to your Storage Lens dashboard, your dashboard will collect storage usage metrics
within 48 hours. You can then visualize this data in the Storage Lens dashboard or export it
through a metrics export. If you forget to attach a Storage Lens group to a dashboard, your
Storage Lens group data won’t be captured or displayed anywhere.

###### Note

- When you create a S3 Storage Lens group, you're creating an AWS resource.
  Therefore, each Storage Lens group has its own Amazon Resource Name (ARN), which
  you can specify when [attaching it to or excluding it from a S3 Storage Lens dashboard](storage-lens-groups-dashboard-console.md "storage-lens-groups-dashboard-console.md").
- If your Storage Lens group isn't attached to a dashboard, you won't incur any
  additional charges for creating a Storage Lens group.
- S3 Storage Lens aggregates usage metrics for an object under all matching Storage
  Lens groups. Therefore, if an object matches the filter conditions for two or
  more Storage Lens groups, you will see repeated counts for the same object
  across your storage usage.
  You can create a Storage Lens group at the account level in a specified home Region (from
  the list of supported AWS Regions). Then, you can attach your Storage Lens group to
  multiple Storage Lens dashboards, as long as the dashboards are in the same AWS account
  and home Region. You can create up to 50 Storage Lens groups per home Region in each
  AWS account.

You can create and manage S3 Storage Lens groups by using the Amazon S3 console, AWS Command Line Interface (AWS CLI),
AWS SDKs, or the Amazon S3 REST API.

###### Topics

- [Viewing Storage Lens group aggregated
  metrics](#storage-lens-group-aggregation "#storage-lens-group-aggregation")
- [Storage Lens groups permissions](#storage-lens-group-permissions "#storage-lens-group-permissions")
- [Storage Lens groups
  configuration](#storage-lens-groups-configuration "#storage-lens-groups-configuration")
- [AWS resource tags](#storage-lens-group-resource-tags "#storage-lens-group-resource-tags")
- [Storage Lens groups metrics
  export](#storage-lens-groups-metrics-export "#storage-lens-groups-metrics-export")

## Viewing Storage Lens group aggregated

metrics

You can view the aggregated metrics for your Storage Lens groups by attaching the
groups to a dashboard. The Storage Lens groups that you want to attach must reside
within the designated home Region in the dashboard account.

To attach a Storage Lens group to a dashboard, you must specify the group in the
**Storage Lens group aggregation** section of your dashboard
configuration. If you have several Storage Lens groups, you can filter the
**Storage Lens group aggregation** results to include or exclude
only the groups that you want. For more information about attaching groups to your
dashboards, see [Attaching or removing S3 Storage Lens groups
to or from your dashboard](storage-lens-groups-dashboard-console.md "storage-lens-groups-dashboard-console.md").

After you've attached your groups, you will see the additional Storage Lens group
aggregation data in your dashboard within 48 hours.

###### Note

To view aggregated metrics for your Storage Lens group, you must attach the group
to an S3 Storage Lens dashboard.

## Storage Lens groups permissions

Storage Lens groups require certain permissions in AWS Identity and Access Management (IAM) to authorize
access to S3 Storage Lens group actions. To grant these permissions, you can use an
identity-based IAM policy. You can attach this policy to IAM users, groups, or roles
to grant them permissions. Such permissions can include the ability to create or delete
Storage Lens groups, view their configurations, or manage their tags.

The IAM user or role that you grant permissions to must belong to the account that
created or owns the Storage Lens group.

To use Storage Lens groups and to view your Storage Lens groups metrics, you must
first have the appropriate permissions to use S3 Storage Lens. For more information, see [Setting Amazon S3 Storage Lens permissions](storage_lens_iam_permissions.md "storage_lens_iam_permissions.md").

To create and manage S3 Storage Lens groups, you must have the following IAM
permissions, depending on which actions you want to perform:

| Action                                                                       | IAM permissions                                  |
| ---------------------------------------------------------------------------- | ------------------------------------------------ |
| Create a new Storage Lens group                                              | `s3:CreateStorageLensGroup`                      |
| Create a new Storage Lens group with tags                                    | `s3:CreateStorageLensGroup`,<br>`s3:TagResource` |
| Update an existing Storage Lens group                                        | `s3:UpdateStorageLensGroup`                      |
| Return the details of a Storage Lens group configuration                     | `s3:GetStorageLensGroup`                         |
| List all Storage Lens groups in your home Region                             | `s3:ListStorageLensGroups`                       |
| Delete a Storage Lens group                                                  | `s3:DeleteStorageLensGroup`                      |
| List the tags that were added to your Storage Lens group                     | `s3:ListTagsForResource`                         |
| Add or update a Storage Lens group tag for an existing Storage<br>Lens group | `s3:TagResource`                                 |
| Delete a tag from a Storage Lens group                                       | `s3:UntagResource`                               |

Here's an example of how to configure your IAM policy in the account that creates
the Storage Lens group. To use this policy, replace
`us-east-1` with the home Region that your
Storage Lens group is located in. Replace
`111122223333` with your
AWS account ID, and replace
`example-storage-lens-group` with the name
of your Storage Lens group. To apply these permissions to all Storage Lens groups,
replace `example-storage-lens-group` with an
`*`.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "EXAMPLE-Statement-ID",
            "Effect": "Allow",
            "Action": [
                "s3:CreateStorageLensGroup",
                "s3:UpdateStorageLensGroup",
                "s3:GetStorageLensGroup",
                "s3:ListStorageLensGroups",
                "s3:DeleteStorageLensGroup,
                "s3:TagResource",
                "s3:UntagResource",
                "s3:ListTagsForResource"
                ],
            "Resource": "arn:aws:s3:`us-east-1`:`111122223333`:storage-lens-group/``example-storage-lens-group``"
        }
    ]
}
```

For more information about S3 Storage Lens permissions, see [Setting Amazon S3 Storage Lens permissions](storage_lens_iam_permissions.md "storage_lens_iam_permissions.md"). For more information about IAM policy language, see [Policies and permissions in Amazon S3](access-policy-language-overview.md "access-policy-language-overview.md").

## Storage Lens groups

configuration

### S3 Storage Lens group name

We recommend giving your Storage Lens groups names that indicate their purpose so
that you can easily determine which groups you want to attach to your dashboards. To
[attach a Storage Lens group to a dashboard](storage-lens-groups-dashboard-console.md "storage-lens-groups-dashboard-console.md"), you must specify the group
in the **Storage Lens group aggregation** section of the dashboard
configuration.

Storage Lens group names must be unique within the account. They must not exceed
64 characters, and can contain only letters (a-z, A-Z), numbers (0-9), hyphens
(`-`), and underscores (`_`).

### Home Region

The home Region is the AWS Region where your Storage Lens group is created and
maintained. Your Storage Lens group is created in the same home Region as your
Amazon S3 Storage Lens dashboard. The Storage Lens group configuration and metrics are also
stored in this Region. You can create up to 50 Storage Lens groups in a home
Region.

After you create your Storage Lens group, you can’t edit the home Region.

### Scope

To include objects in your Storage Lens group, they must be in scope for your
Amazon S3 Storage Lens dashboard. The scope of your Storage Lens dashboard is determined by
the buckets that you included in the **Dashboard scope** of your
S3 Storage Lens dashboard configuration.

You can use different filters for your objects to define the scope of your Storage
Lens group. To view these Storage Lens group metrics in your S3 Storage Lens dashboard,
objects must match the filters that you include in your Storage Lens groups. For
example, suppose that your Storage Lens group includes objects with the prefix
`marketing` and the suffix `.png`, but no objects match
those criteria. In this case, metrics for this Storage Lens group won't be generated
in your daily metrics export, and no metrics for this group will be visible in your
dashboard.

### Filters

You can use the following filters in an S3 Storage Lens group:

- **Prefixes** – Specifies the [prefix](using-prefixes.md "using-prefixes.md") of included objects, which is a string of characters at
  the beginning of the object key name. For example, a value of
  `images` for the **Prefixes** filter
  includes objects with any of the following prefixes: `images/`,
  `images-marketing`, and `images/production`. The
  maximum length of a prefix is 1,024 bytes.
- **Suffixes** – Specifies the suffix of
  included objects (for example, `.png`, `.jpeg`, or
  `.csv`). The maximum length of a suffix is 1,024
  bytes.
- **Object tags** – Specifies the list
  of [object tags](object-tagging.md "object-tagging.md")
  that you want to filter on. A tag key can't exceed 128 Unicode characters,
  and a tag value can’t exceed 256 Unicode characters. Note that if the object tag value field is left empty, S3 Storage Lens groups only matches the object to
  other objects that also have empty tag values.
- **Age** – Specifies the object age
  range of included objects in days. Only integers are supported.
- **Size** – Specifies the object size range of
  included objects in bytes. Only integers are supported. The maximum
  allowable value is 50 TB.

### Storage Lens group object

tags

You can [create a Storage Lens group](storage-lens-groups-create.md "storage-lens-groups-create.md") that includes up to 10 object tag filters. The
following example includes two object tag key-value pairs as filters for a Storage
Lens group that's named
`Marketing-Department`. To use this example,
replace `Marketing-Department` with the name
of your group, and replace `object-tag-key-1`,
`object-tag-value-1`, and so on with
the object tag key-value pairs that you want to filter on.

```
{
    "Name": "`Marketing-Department`",
    "Filter": {
     "MatchAnyTag":[
                {
                    "Key": "`object-tag-key-1`",
                    "Value": "`object-tag-value-1`"
                },
                {
                    "Key": "`object-tag-key-2`",
                    "Value": "`object-tag-value-2`"
                }
            ]
    }
}
```

### Logical operators

(`And` or `Or`)

To include multiple filter conditions in your Storage Lens group, you can use
logical operators (either `And` or `Or`). In the following
example, the Storage Lens group that's named
`Marketing-Department` has an
`And` operator that contains `Prefix`,
`ObjectAge`, and `ObjectSize` filters. Because an
`And` operator is used, only objects that match **all** of these filter conditions will be included the Storage Lens
group's scope.

To use this example, replace the `user input
 placeholders` with the values that you want to filter
on.

```
{
    "Name": "`Marketing-Department`",
    "Filter": {
        "And": {
            "MatchAnyPrefix": [
                "`prefix-1`",
                "`prefix-2`",
                "`prefix-3/sub-prefix-1`"
            ],
             "MatchObjectAge": {
                "DaysGreaterThan": `10`,
                "DaysLessThan": `60`
            },
            "MatchObjectSize": {
                "BytesGreaterThan": `10`,
                "BytesLessThan": `60`
            }
        }
    }
}
```

###### Note

If you want to include objects that match **any**
of the conditions in the filters, replace the `And` logical operator
with the `Or` logical operator in this example.

## AWS resource tags

Each S3 Storage Lens group is counted as an AWS resource with its own Amazon Resource Name
(ARN). Therefore, when you configure your Storage Lens group, you can optionally add
AWS resource tags to the group. You can add up to 50 tags for each Storage Lens group.
To create a Storage Lens group with tags, you must have the
`s3:CreateStorageLensGroup` and `s3:TagResource`
permissions.

You can use AWS resource tags to categorize resources according to department, line
of business, or project. Doing so is useful when you have many resources of the same
type. By applying tags, you can quickly identify a specific Storage Lens group based on
the tags that you've assigned to it. You can also use tags to track and allocate
costs.

In addition, when you add an AWS resource tag to your Storage Lens group, you
activate [attribute-based access control (ABAC)](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md"). ABAC is an authorization strategy
that defines permissions based on attributes, in this case tags. You can also use
conditions that specify resource tags in your IAM policies to [control
access to AWS resources](../../../IAM/latest/UserGuide/access_tags.md#access_tags_control-resources "../../../IAM/latest/UserGuide/access_tags.md#access_tags_control-resources").

You can edit tag keys and values, and you can remove tags from a resource at any time.
Also, be aware of the following limitations:

- Tag keys and tag values are case sensitive.
- If you add a tag that has the same key as an existing tag on that resource,
  the new value overwrites the old value.
- If you delete a resource, any tags for the resource are also deleted.
- Don't include private or sensitive data in your AWS resource tags.
- System tags (or tags with tag keys that begin with `aws:`) aren't
  supported.
- The length of each tag key can't exceed 128 characters. The length of each tag
  value can't exceed 256 characters.

## Storage Lens groups metrics

export

S3 Storage Lens group metrics are included in the [Amazon S3 Storage Lens metrics export](storage_lens_understanding_metrics_export_schema.md "storage_lens_understanding_metrics_export_schema.md") for the dashboard that the Storage Lens group
is attached to. For general information about the Storage Lens metrics export feature,
see [Viewing Amazon S3 Storage Lens metrics using a data
export](storage_lens_view_metrics_export.md "storage_lens_view_metrics_export.md").

Your metrics export for Storage Lens groups includes any S3 Storage Lens metrics that are in
scope for the dashboard that you attached the Storage Lens group to. The export also
includes additional metrics data for Storage Lens groups.

After you create your Storage Lens group, your metrics export is sent daily to the
bucket that you selected when you configured the metrics export for the dashboard that
your group is attached to. It can take up to 48 hours for you to receive the first
metrics export.

To generate metrics in the daily export, objects must match the filters that you
include in your Storage Lens groups. If no objects match the filters that you included
in your Storage Lens group, then no metrics will be generated. However, if an object
matches two or more Storage Lens groups, the object is listed separately for each group
when it appears in the metrics export.

You can identify metrics for Storage Lens groups by looking for one of the following
values in the `record_type` column of the metrics export for your
dashboard:

- `STORAGE_LENS_GROUP_BUCKET`
- `STORAGE_LENS_GROUP_ACCOUNT`

The `record_value` column displays the resource ARN for the Storage Lens
group (for example,
`arn:aws:s3:`us-east-1`:`111122223333`:storage-lens-group/`Marketing-Department``).
