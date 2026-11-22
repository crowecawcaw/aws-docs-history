

# Replicating image deletions in Amazon ECR

By default, Amazon ECR replication copies images to your replication destinations but does not replicate deletions. You can enable replication of deletes on a replication rule. When you enable replication of deletes, Amazon ECR replicates image deletions and image tag removals from the source registry to the replication destinations for that rule. This keeps your destination repositories consistent with the source without requiring you to delete images in each Region or account separately.

## How replication of deletes works
<a name="replication-delete-how"></a>

Replication of deletes applies to the same repositories and destinations as the replication rule that you enable it on. When you enable replication of deletes, Amazon ECR replicates the following actions from the source registry to each replication destination.
+ When you remove a tag from an image that has other tags, Amazon ECR removes the same tag from the image in each destination repository.
+ When you remove the last tag from an image, Amazon ECR deletes the untagged image. Amazon ECR also deletes the corresponding digest and all related tags in each destination repository.
+ When you delete an image by digest, Amazon ECR deletes the image and all of its tags in each destination repository.
+ When a lifecycle policy expires an image in the source registry, Amazon ECR replicates the deletion to each destination repository.

## Enabling replication of deletes
<a name="replication-delete-enable"></a>

Amazon ECR doesn't replicate image deletions or image tag removals by default. You enable replication of deletes per replication rule by setting the `deleteReplication` parameter on the rule. If you don't set this parameter, Amazon ECR doesn't replicate image deletions or image tag removals for the replication rule. Amazon ECR replicates only the image deletions and image tag removals that occur after you enable replication of deletes. Amazon ECR doesn't replicate deletions that occurred before you enabled it.

To enable replication of deletes with the AWS CLI, update your replication configuration with the `deleteReplication` parameter set on the rule. For more information, see [Configuring private image replication in Amazon ECR](registry-settings-configure.md). In the following example, replace {{us-west-2}} with your destination Region and replace the registry ID with your destination AWS account ID.

```JSON
{
    "rules": [
        {
            "destinations": [
                {
                    "region": "{{us-west-2}}",
                    "registryId": "{{111122223333}}"
                }
            ],
            "deleteReplication": {
                "enabled": true
            }
        }
    ]
}
```

## Ordering and consistency
<a name="replication-delete-ordering"></a>

Replication is asynchronous and eventually consistent. Image pushes and replicated deletions can arrive at a destination in a different order than they occurred in the source registry. Amazon ECR applies a replicated deletion only when the destination content still matches the source action. If the image or tag doesn't exist in the destination repository, or was changed by a more recent action, the replicated deletion has no effect. A replicated deletion occurs once. For example, if you configured replication from `us-west-2` to `us-east-1` and from `us-east-1` to `us-east-2`, a deletion in `us-west-2` is replicated only to `us-east-1`; it isn't replicated again to `us-east-2`.

## Required permissions for replication of deletes
<a name="replication-delete-permissions"></a>

Amazon ECR uses the `AWSServiceRoleForECRReplication` service-linked role to replicate on your behalf. The role's `ECRReplicationServiceRolePolicy` policy includes the permissions Amazon ECR needs to replicate image deletions and image tag removals. For more information, see [Using service-linked roles for Amazon ECR](using-service-linked-roles.md).

For cross-account replication, the destination registry must grant the source account the `ecr:ReplicateImageDelete` permission in its registry permissions policy, in addition to the `ecr:ReplicateImage` and `ecr:CreateRepository` permissions. For more information, see [Private registry permissions in Amazon ECR](registry-permissions.md).

## Monitoring replication of deletes
<a name="replication-delete-monitoring"></a>

Amazon ECR emits an Amazon EventBridge event with the detail type `ECR Replication Action` and an `action-type` of `REPLICATE_DELETE` in the destination Region when a replicated deletion completes. For more information, see [Amazon ECR events and EventBridge](ecr-eventbridge.md).

Replicated deletions are recorded in the destination account's CloudTrail logs as `ReplicateImageDelete` events. For more information, see [Logging Amazon ECR actions with AWS CloudTrail](logging-using-cloudtrail.md).

## Considerations for replication of deletes
<a name="replication-delete-considerations"></a>
+ Amazon ECR does not replicate repository deletions.
+ Amazon ECR replicates deletions only at the image level. Deleting a repository in the source Region doesn't delete the corresponding images in the destination repositories.
+ Amazon ECR replicates only the deletions that occur after you enable replication of deletes. There is no retroactive replication.