# Deleting Conformance Packs for AWS Config

You can use the AWS Config console or the AWS CLI to delete conformance packs.

## Considerations

**Recommendation: Consider excluding the `AWS::Config::ResourceCompliance` resource type from recording before deleting rules**

Deleting rules creates configuration items (CIs) for `AWS::Config::ResourceCompliance`
that can affect your costs for the configuration recorder. If you are deleting rules which evaluate a large number of resource types,
this can lead to a spike in the number of CIs recorded.

To avoid the associated costs, you can opt to disable recording
for the `AWS::Config::ResourceCompliance` resource type before deleting rules, and re-enable recording after the rules have been deleted.

However, since deleting rules is an asynchronous process, it might take an hour or more to complete. During the time
when recording is disabled for `AWS::Config::ResourceCompliance`, rule evaluations will not be recorded in the associated resource’s history.

## To delete a conformance pack

Deleting Conformance Packs (Console)

1. To delete a conformance pack, select the conformance pack from the
   table.
2. Choose **Actions** and then choose
   **Delete**.
3. On the delete `conformance pack` dialog box, confirm
   if you would like to permanently delete this conformance pack.

###### Important

You cannot revert this action. When you delete a conformance pack, you
delete all of the AWS Config rules and remediation actions in that conformance
pack. 4. Enter **Delete** and choose
**Delete**.

On the **Conformance packs** page, you can see the deployment
status as **Deleting** until the conformance pack is completely
deleted.

Deleting Conformance Packs (AWS CLI)
Enter the following command.

```
aws configservice delete-conformance-pack --conformance-pack-name MyConformancePack1
```

If successful, the command runs with no additional output.

###### Important

You cannot revert this action. When you delete a conformance pack, you
delete all of the AWS Config rules and remediation actions in that conformance
pack.
