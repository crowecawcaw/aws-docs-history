

# Readiness check API operations
<a name="actions.readiness"></a>

**Note**  
The readiness check feature in Amazon Application Recovery Controller (ARC) is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Amazon Application Recovery Controller (ARC) readiness check availability change](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-readiness-availability-change.html).

The following table lists ARC operations that you can use for recovery readiness (readiness check), with links to relevant documentation.

For examples of how to use common recovery readiness API operations with the AWS Command Line Interface, see [Examples of using ARC readiness check API operations with the AWS CLI](getting-started-cli-readiness.md).


| Action | Using the ARC console | Using the ARC API | 
| --- | --- | --- | 
| Create a cell | See [Creating, updating, and deleting recovery groups in ARC](recovery-readiness.recovery-groups.md) | See [CreateCell](https://docs.aws.amazon.com/recovery-readiness/latest/api/cells.html) | 
| Get a cell | See [Creating, updating, and deleting recovery groups in ARC](recovery-readiness.recovery-groups.md) | See [GetCell](https://docs.aws.amazon.com/recovery-readiness/latest/api/cells-cellname.html) | 
| Delete a cell | See [Creating, updating, and deleting recovery groups in ARC](recovery-readiness.recovery-groups.md) | See [DeleteCell](https://docs.aws.amazon.com/recovery-readiness/latest/api/cells-cellname.html) | 
| Update a cell | N/A | See [UpdateCell](https://docs.aws.amazon.com/recovery-readiness/latest/api/cells-cellname.html) | 
| List cells for an account | See [Creating, updating, and deleting recovery groups in ARC](recovery-readiness.recovery-groups.md) | See [ListCells](https://docs.aws.amazon.com/recovery-readiness/latest/api/cells.html) | 
| Create a recovery group | See [Creating, updating, and deleting recovery groups in ARC](recovery-readiness.recovery-groups.md) | See [CreateRecoveryGroup](https://docs.aws.amazon.com/recovery-readiness/latest/api/recoverygroups.html) | 
| Get a recovery group | See [Creating, updating, and deleting recovery groups in ARC](recovery-readiness.recovery-groups.md) | See [GetRecoveryGroup](https://docs.aws.amazon.com/recovery-readiness/latest/api/recoverygroups-recoverygroupname.html) | 
| Update a recovery group | See [Creating, updating, and deleting recovery groups in ARC](recovery-readiness.recovery-groups.md) | See [UpdateRecoveryGroup](https://docs.aws.amazon.com/recovery-readiness/latest/api/recoverygroups-recoverygroupname.html) | 
| Delete a recovery group | See [Creating, updating, and deleting recovery groups in ARC](recovery-readiness.recovery-groups.md) | See [DeleteRecoveryGroup](https://docs.aws.amazon.com/recovery-readiness/latest/api/recoverygroups-recoverygroupname.html) | 
| List recovery groups | See [Creating, updating, and deleting recovery groups in ARC](recovery-readiness.recovery-groups.md) | See [ListRecoveryGroups](https://docs.aws.amazon.com/recovery-readiness/latest/api/recoverygroups.html) | 
| Create a resource set | See [Creating and updating readiness checks in ARC](recovery-readiness.create-readiness-check-or-set.md) | See [CreateResourceSet](https://docs.aws.amazon.com/recovery-readiness/latest/api/resourcesets.html) | 
| Get a resource set | See [Creating and updating readiness checks in ARC](recovery-readiness.create-readiness-check-or-set.md) | See [GetResourceSet](https://docs.aws.amazon.com/recovery-readiness/latest/api/resourcesets-resourcesetname.html) | 
| Update a resource set | See [Creating and updating readiness checks in ARC](recovery-readiness.create-readiness-check-or-set.md) | See [UpdateResourceSet](https://docs.aws.amazon.com/recovery-readiness/latest/api/resourcesets-resourcesetname.html) | 
| Delete a resource set | See [Creating and updating readiness checks in ARC](recovery-readiness.create-readiness-check-or-set.md) | See [DeleteResourceSet](https://docs.aws.amazon.com/recovery-readiness/latest/api/resourcesets-resourcesetname.html) | 
| List resource sets | See [Creating and updating readiness checks in ARC](recovery-readiness.create-readiness-check-or-set.md) | See [ListResourceSets](https://docs.aws.amazon.com/recovery-readiness/latest/api/resourcesets.html) | 
| Create a readiness check | See [Creating and updating readiness checks in ARC](recovery-readiness.create-readiness-check-or-set.md) | See [CreateReadinessCheck](https://docs.aws.amazon.com/recovery-readiness/latest/api/readinesschecks.html) | 
| Get a readiness check | See [Creating and updating readiness checks in ARC](recovery-readiness.create-readiness-check-or-set.md) | See [GetReadinessCheck](https://docs.aws.amazon.com/recovery-readiness/latest/api/readinesschecks-readinesscheckname.html) | 
| Update a readiness check | See [Creating and updating readiness checks in ARC](recovery-readiness.create-readiness-check-or-set.md) | See [UpdateReadinessCheck](https://docs.aws.amazon.com/recovery-readiness/latest/api/readinesschecks-readinesscheckname.html) | 
| Delete a readiness check | See [Creating and updating readiness checks in ARC](recovery-readiness.create-readiness-check-or-set.md) | See [DeleteReadinessCheck](https://docs.aws.amazon.com/recovery-readiness/latest/api/readinesschecks-readinesscheckname.html) | 
| List readiness checks | See [Creating and updating readiness checks in ARC](recovery-readiness.create-readiness-check-or-set.md) | See [ListReadinessChecks](https://docs.aws.amazon.com/recovery-readiness/latest/api/readinesschecks.html) | 
| List readiness rules | See [Readiness rules descriptions in ARC](recovery-readiness.rules-resources.md) | See [ListRules](https://docs.aws.amazon.com/recovery-readiness/latest/api/rules.html) | 
| Check status of an entire readiness check | See [Monitoring readiness status in ARC](recovery-readiness.status.md) | See [GetReadinessCheckStatus](https://docs.aws.amazon.com/recovery-readiness/latest/api/readinesschecks-readinesscheckname-status.html) | 
| Check status of a resource | See [Monitoring readiness status in ARC](recovery-readiness.status.md) | See [GetReadinessCheckResourceStatus](https://docs.aws.amazon.com/recovery-readiness/latest/api/readinesschecks-readinesscheckname-resource-resourceidentifier-status.html) | 
| Check status of a cell | See [Monitoring readiness status in ARC](recovery-readiness.status.md) | See [GetCellReadinessSummary](https://docs.aws.amazon.com/recovery-readiness/latest/api/cellreadiness-cellname.html) | 
| Check status of a recovery group | See [Monitoring readiness status in ARC](recovery-readiness.status.md) | See [GetRecoveryGroupReadinessSummary](https://docs.aws.amazon.com/recovery-readiness/latest/api/recoverygroupreadiness-recoverygroupname.html) | 