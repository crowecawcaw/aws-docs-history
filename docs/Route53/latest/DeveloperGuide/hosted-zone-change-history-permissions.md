

# Permissions for Change History

The following table lists each Change History API operation and the IAM actions that you must allow in the `Action` element of a policy statement to call it. A resource type marked with an asterisk (\*) is required. The `hostedzone` resource type has the ARN `arn:aws:route53:::hostedzone/{{Id}}`. These actions don't support service-specific condition keys.


**IAM actions for Change History**  

| API operation | Description | IAM actions | Access level | Resource types (\*required) | 
| --- | --- | --- | --- | --- | 
| [ListHostedZoneChangeBatches](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListHostedZoneChangeBatches.html) | Grants permission to get a list of the change batches in a specified hosted zone's change history | `route53:ListHostedZoneChangeBatches` | List | `hostedzone*` | 
| [GetHostedZoneChangeBatch](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetHostedZoneChangeBatch.html) | Grants permission to get the records that a specified change batch created, updated, or deleted in a hosted zone | `route53:GetHostedZoneChangeBatch`<br />`route53:ListResourceRecordSets` | List | `hostedzone*` | 
| [ListResourceRecordSetChanges](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListResourceRecordSetChanges.html) | Grants permission to list the changes to a specified record in a hosted zone's change history | `route53:GetHostedZoneChangeBatch`<br />`route53:ListResourceRecordSets` | List | `hostedzone*` | 

`ListResourceRecordSetChanges` doesn't have an IAM action of its own.

Change History shows the ARN of the principal that submitted each change, including role session names. Grant these actions only to principals that can see that information. For an example policy, see [Example 6: Allow reading the change history of a hosted zone](access-control-managing-permissions.md#access-policy-example-allow-read-change-history).