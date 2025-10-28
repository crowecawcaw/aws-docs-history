# Receiving CloudTrail log files from multiple Regions

When you create a multi-Region trail, CloudTrail logs events from all Regions enabled in your account. CloudTrail delivers log files to the same S3 bucket and
CloudWatch Logs log group. As long as CloudTrail has permissions to write to an S3 bucket, the bucket for a
multi-Region trail does not have to be in the trail's home Region.

Although most AWS Regions are enabled by default for your AWS account, you must
manually enable certain Regions (also referred to as _opt-in Regions_).
For information about which Regions are enabled by default, see [Considerations before enabling and disabling Regions](../../../accounts/latest/reference/manage-acct-regions.md#manage-acct-regions-considerations "../../../accounts/latest/reference/manage-acct-regions.md#manage-acct-regions-considerations") in the
_AWS Account Management Reference Guide_. For the list of Regions CloudTrail supports,
see [CloudTrail supported Regions](cloudtrail-supported-regions.md "cloudtrail-supported-regions.md").

After you enable an opt-in Region, CloudTrail creates an identical copy of each multi-Region
trail in the opt-in Region that you enabled. For more information, see [What happens when you enable an
opt-in Region?](cloudtrail-multi-region-trails.md#cloudtrail-multi-region-trails-optin "cloudtrail-multi-region-trails.md#cloudtrail-multi-region-trails-optin").

If you later disable an opt-in Region, the copy of the multi-Region trail in that Region will remain.
Because your account may have activity in the Region you disabled, such as actions by
AWS services to remove resources, CloudTrail will continue to capture activity and attempt
to deliver events to the S3 bucket for any trails that are not deleted before the Region
is disabled.

To convert an existing single-Region trail to a multi-Region trail,
you must use the AWS CLI.

To change an existing trail so that it applies to all enabled Regions, add the
`--is-multi-region-trail` option to the [update-trail](cloudtrail-create-and-update-a-trail-by-using-the-aws-cli-update-trail.md "cloudtrail-create-and-update-a-trail-by-using-the-aws-cli-update-trail.md") command.

```
aws cloudtrail update-trail --name `my-trail` --is-multi-region-trail
```

To confirm that the trail is now a multi-Region trail, verify that the `IsMultiRegionTrail`
element in the output shows `true`.

```
{
    "IncludeGlobalServiceEvents": true,
    "Name": "`my-trail`",
    "TrailARN": "arn:aws:cloudtrail:`us-east-2`:`123456789012`:trail/`my-trail`",
    "LogFileValidationEnabled": false,
    **"IsMultiRegionTrail": true**,
    "IsOrganizationTrail": false,
    "S3BucketName": "`amzn-s3-demo-bucket`"
}
```

For more information, see the following resources:

- [Understanding multi-Region trails and
  opt-in Regions](cloudtrail-multi-region-trails.md "cloudtrail-multi-region-trails.md")
- [Creating a trail for your AWS account](cloudtrail-create-and-update-a-trail.md "cloudtrail-create-and-update-a-trail.md")
- [CloudTrail FAQs](https://aws.amazon.com/cloudtrail/faqs/ "https://aws.amazon.com/cloudtrail/faqs/")
