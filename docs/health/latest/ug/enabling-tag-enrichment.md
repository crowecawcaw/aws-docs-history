

# Enabling tag enrichment

AWS Health doesn't access your tag information by default. To include tags in AWS Health events, you must turn on the feature and then configure the tag keys that you want.

**Note**  
When you turn on tag enrichment, AWS Health creates the AWSServiceRoleForTagsHealth service-linked role, which uses the TagsHealthServiceRolePolicy AWS managed policy. This managed policy and related role are used to enrich AWS Health events with tags. The policy allows the service-linked role to complete actions for you. You can't attach this policy to your AWS Identity and Access Management (IAM) entities. For more information about service-linked roles, see [Using service-linked roles for AWS Health](using-service-linked-roles.md). For more information about this policy, see [AWS managed policy: TagsHealthServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-TagsHealthServiceRolePolicy).  
This policy grants read-only permissions that allow AWS Health to read the tags on the resources in your account. AWS Health uses these tags so that you can view and filter your AWS Health events by resource tag. With this policy, AWS Health can't create, change, or remove tags, and it can't access the resources themselves.

## Requirements
<a name="tag-enrichment-requirements"></a>

Before you enable tag enrichment, review the following requirements:
+ **Account view:** You can turn on tags from any AWS account.
+ **Organizational view:** You must first turn on organizational view for AWS Health. For more information, see [Aggregating AWS Health events across accounts](aggregate-events.md). You must turn on and configure tags from the management account of your organization. Delegated administrator accounts can view tag information across the organization, but only the management account can change the configuration.
+ **Tag key limit:** You can configure up to **10 tag keys** for AWS Health to include in events.

## Using the AWS Health Dashboard to enable tag enrichment
<a name="enable-tags-health-dashboard"></a>

**To enable tag enrichment**

1. Open the AWS Health Dashboard at [https://health.aws.amazon.com/health/home](https://health.aws.amazon.com/health/home). For organizational view, sign in to the management account.

1. In the navigation pane, choose **Configurations**.

1. Choose **Enable tags**.
**Note**  
In organizational view, turning on tags can take up to 8 hours for large organizations. While AWS Health sets up access in your member accounts, the **Configurations** page shows a status of **Pending**, and the **Enable tags** button changes to **In progress**. You can't configure tag keys during this time. When setup is complete, the status changes to **Success** and the **Configure tags** button appears. You don't get a notification when this happens, so check the **Configurations** page again later.

1. Choose **Configure tags**.

1. Add up to 10 tag keys that you want AWS Health to include in events.

1. For each tag key, choose whether to include it in AWS Health events delivered through EventBridge.

1. Choose **Save**.

AWS Health then retrieves your tag information. This can take up to 24 hours. When processing is complete, tag information appears in the AWS Health Dashboard, the AWS Health API, and EventBridge (for tag keys that you enabled for EventBridge).

## Using the AWS Health API to enable tag enrichment
<a name="enable-tags-health-api"></a>

The following table lists the operations for each step in account view and organizational view. For more information about these operations, see the [AWS Health API Reference](https://docs.aws.amazon.com/health/latest/APIReference/Welcome.html).


| Step | Account view operation | Organizational view operation | 
| --- | --- | --- | 
| 1. Turn on tags | `EnableTags` | `EnableTagsForOrganization` | 
| 2. Confirm the feature is on | `DescribeTagsOnboardingStatus` | `DescribeTagsOnboardingStatusForOrganization` | 
| 3. Configure tag keys | `ConfigureTags` | `ConfigureTagsForOrganization` | 
| 4. Confirm the tag keys are active | `DescribeTagKeys` | `DescribeTagKeysForOrganization` | 

**To enable tag enrichment by using the API**

1. Call `EnableTags` (or `EnableTagsForOrganization`).

1. Call `DescribeTagsOnboardingStatus` (or `DescribeTagsOnboardingStatusForOrganization`) and confirm that the response is `{"status": "ENABLED"}`.
**Note**  
In organizational view, turning on tags can take up to 8 hours for large organizations. During this time, AWS Health creates the `AWSServiceRoleForTagsHealth` service-linked role in each member account, and the status is `PENDING`. Call `DescribeTagsOnboardingStatusForOrganization` about every 15 minutes until the status is `ENABLED`. Then configure your tag keys. If you call `ConfigureTagsForOrganization` while the status is `PENDING`, the request fails.

1. Call `ConfigureTags` (or `ConfigureTagsForOrganization`) with the tag keys that you want. To include a tag key in EventBridge events, set `enabledForEventBridge` to `true`.

1. Call `DescribeTagKeys` (or `DescribeTagKeysForOrganization`) and confirm that each key has a status of `ACTIVE`. This can take up to 24 hours. When all keys are active, setup is complete.

**Note**  
`ConfigureTags` and `ConfigureTagsForOrganization` calls replace your full list of tag keys. When you add a key, include all existing keys in the request. Any key that you leave out is removed from the configuration.

## AWS CLI examples
<a name="tags-cli-examples"></a>

The following AWS CLI commands show the full sequence.

To turn on tag enrichment for your account, run the following command. This command has no parameters.

```
aws health enable-tags --region us-east-1
```

Check the onboarding status every few minutes until it is `ENABLED`:

```
aws health describe-tags-onboarding-status --region us-east-1
```

To turn on tag enrichment for your organization, review the following notes and then run the command.

**Note**  
Before you run this command, note the following:  
**Organizational view:** It must already be turned on for AWS Health. You can do that with `aws health enable-health-service-access-for-organization`.
**`PENDING` status:** While AWS Health creates the service-linked role in each member account, the status shows `PENDING`. For large organizations this can take up to 8 hours. Don't run `configure-tags-for-organization` until the status is `ENABLED`, because it fails while the status is `PENDING`.
**Region:** `us-east-1` is the endpoint that the AWS Health organizational view APIs use in the `aws` partition.

In your organization's management account, run the following command:

```
aws health enable-tags-for-organization --region us-east-1
```

Check the status until it is `ENABLED`:

```
aws health describe-tags-onboarding-status-for-organization --region us-east-1
```

Configure the tag keys to include, and turn on each key for EventBridge:

```
aws health configure-tags --region us-east-1 \
--tag-keys '[{"key":"Dept","enabledForEventBridge":true},{"key":"Env","enabledForEventBridge":true},{"key":"awsApplication","enabledForEventBridge":true}]'
```

List registered keys (`key`, `status`, `enabledForEventBridge`):

```
aws health describe-tag-keys --region us-east-1
```

List the tag key and value pairs that AWS Health has retrieved. The default page size is 10:

```
aws health describe-tags --region us-east-1 --max-results 50
```

To list the affected resources of an event with their tags, run the following command. Replace `{{event-arn}}` with the ARN of the event.

```
aws health describe-affected-entities --region us-east-1 \
--filter eventArns={{event-arn}}
```

To turn off tag enrichment for your account, run the following command:

```
aws health disable-tags --region us-east-1
```