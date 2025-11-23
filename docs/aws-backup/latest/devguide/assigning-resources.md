# Select AWS services to backup

## Opt in to services, then assign resources

AWS Backup works with many [different AWS
services](backup-feature-availability.md#features-by-resource "backup-feature-availability.md#features-by-resource"). Before you decide which services to include in backup plan, use the [AWS Backup console](#backup-optin-console "#backup-optin-console") or [AWS CLI](#backup-optin-cli "#backup-optin-cli") to opt in to using AWS Backup to work with those services.

Then, in each backup plan, specify in the [console](assigning-resources-console.md "assigning-resources-console.md") or through [CLI](assigning-resources-json.md "assigning-resources-json.md") which
resource types to include in that plan.

For example, you can opt in to all services which AWS Backup supports, then include only Amazon S3
buckets and Aurora clusters in a backup plan.

###### Topics

- [AWS Backup service opt-in](#backup-service-optin "#backup-service-optin")
- [Backup plan resource assignment](#backup-resource-assignment "#backup-resource-assignment")
- [Assign resources using the AWS Backup
  console](assigning-resources-console.md "assigning-resources-console.md")
- [Assign resources with AWS CLI](assigning-resources-json.md "assigning-resources-json.md")
- [Assign AWS Backup resources through CloudFormation](assigning-resources-cfn.md "assigning-resources-cfn.md")
- [Backup plan resource assignments quotas](#assigning-resources-quotas "#assigning-resources-quotas")

## AWS Backup service opt-in

### Service opt-in through the AWS Backup console

###### To configure the AWS services to use with AWS Backup

1. Sign in to the AWS Management Console, and open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the navigation pane, choose **Settings**.
3. On the **Service opt-in** page, choose **Configure
   resources**.
4. On the **Configure resources** page, use the toggle switches to
   enable or disable the services that are used with AWS Backup. Choose
   **Confirm** when your services are configured. Make sure that the
   AWS service you're opting in is available in your AWS Region.

### Service opt-in through AWS CLI

Use the [`aws backup
 update-region-settings`](API_UpdateRegionSettings.md "API_UpdateRegionSettings.md") command to change the services (resource types)
your account or organization will use AWS Backup to orchestrate backup creation. Use the [`aws backup describe-region-settings`](API_DescribeRegionSettings.md "API_DescribeRegionSettings.md") command to determine which
services you have opted into in a specific Region.

## Backup plan resource assignment

Through the [AWS Backup console](assigning-resources-console.md "assigning-resources-console.md") or through
[AWS CLI](assigning-resources-json.md "assigning-resources-json.md"), the resource assignment in your
backup plan specifies which resources AWS Backup will include. AWS Backup provides both simple default
settings and fine-grained controls to assign resources.

You can assign resources in the following ways:

- Explicitly assign resource types to the backup plan
- Include all resources (AWS Backup will then scan for all supported resource types)
- Use tags to include or exclude resources

If you only use tags for resource assignment, then the service opt-in settings will
still apply.

You can further refine the resource assignment using conditions and tags. There are
some limits on the number of ARNs, conditions, and tags that can be used in a single
resource assignment.

Resource selection through CLI is based on service names and resource types. See [Assign resources with AWS CLI](assigning-resources-json.md "assigning-resources-json.md") for
considerations about resource election.

## Backup plan resource assignments quotas

The following quotas apply to a single resource assignment:

- 500 Amazon Resource Names (ARNs) without wildcards
- 30 ARNs with wildcard expressions
- 30 conditions
- 30 tags per resource assignment (and an unlimited number of resources per
  tag)
