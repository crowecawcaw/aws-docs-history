

# Auto-tagging in MAP for AWS Transform

## What is auto-tagging?
<a name="auto-tagging-what-is"></a>

Auto-tagging is a feature of AWS Migration Acceleration Program (MAP) for AWS Transform that applies MAP tags to the AWS resources that AWS Transform agents create when you migrate or modernize workloads to AWS. The following agents support auto-tagging:
+ **AWS Transform migration agent** (previously called the VMware migration agent): server and VM rehosting, and source code containerization.
+ **AWS Transform Windows (SQL Server) modernization agent**: SQL Server to Amazon Aurora PostgreSQL.

These tags enable AWS to track your migration spend and apply your MAP credits.

## Why it matters
<a name="auto-tagging-why"></a>

MAP credits are applied only to tagged spend, and only from the moment a tag is correctly in place. There is no retroactive credit for untagged resources. In the past, you had to apply these tags yourself, which risked missed or incorrect tags. Auto-tagging applies the correct tag automatically, at the moment the resource is created, every time, so that no eligible spend is missed.

## How it works
<a name="auto-tagging-how"></a>

Once your engagement and workspace are configured, auto-tagging is fully managed. You do not need to manually apply tags to individual resources. The agent handles that automatically. The process works as follows:

1. **Your engagement is registered.** When your Express Migration qualifies for MAP, a unique attribution identity is generated for your migration. This identity consists of:
   + A **tag key**: `aws-apn-id`
   + A unique **tag value** tied to your engagement

1. **Agents receive tagging instructions automatically.** The agent knows which tag to apply as soon as your migration wave runs.

1. **Tags are applied at resource creation.** The agent applies the correct tag to every supported resource it creates.

## Supported use cases
<a name="auto-tagging-supported"></a>

The following table lists the migration types that support auto-tagging, the AWS Transform agent used, the resources each type tags, and example workloads.


| Migration type | AWS Transform agent | Resources tagged | Workload examples | 
| --- | --- | --- | --- | 
| Server or VM rehosting | Migration agent | Amazon EC2 instances and their Amazon EBS volumes; ENIs created at launch; Amazon FSx for NetApp ONTAP SVMs (when FSx storage is used); VPCs and security groups | VMware workloads migrated using the AWS Transform migration agent | 
| Source code containerization | Migration agent | Amazon ECR repositories (one per service); Amazon S3 bucket and AWS CodeBuild CloudWatch log group created for the migration (one per connector). Amazon ECS targets: resources created by the generated Terraform (ECS cluster, services, task definitions, ALB, target groups, listeners, log groups, Route 53 private hosted zone, AWS Cloud Map service, Amazon EFS, access-log bucket). Amazon EKS targets: the ALB (when the Helm chart includes an Ingress) | Application source code containerized and deployed to Amazon ECS or Amazon EKS | 
| Database modernization | Windows (SQL Server) modernization agent | Amazon Aurora clusters | SQL Server to Amazon Aurora PostgreSQL | 

## Resources not auto-tagged
<a name="auto-tagging-not-tagged"></a>

The following resources are not auto-tagged:
+ **Source code containerization:**
  + Temporary CodeBuild projects.
  + Amazon ECS tasks and ECS-managed Amazon EBS volumes.
  + On EKS: the ALB log bucket, hosted zone, EKS access entry, and EBS or EFS volumes created from PVCs.
+ **Database modernization:** Amazon RDS and Amazon DynamoDB.
+ **Customer-owned or pre-existing resources:** existing VPCs, IAM roles, ECS or EKS clusters, ECR repositories, S3 buckets, or log groups. Auto-tagging applies only to resources the agent creates.
+ **Migration of existing ECS or EKS clusters:** not supported.

**Note**  
Tagging the S3 bucket is best-effort. For resources that are not auto-tagged, apply the tag manually. For instructions, see [Tagging Resources](getting-started-step2.md).

## How auto-tagging is triggered
<a name="auto-tagging-triggered"></a>

Auto-tagging is not a setting you turn on. It activates automatically when the following conditions are met. You must first set up your workspace and migration job (see [What you need to do](#auto-tagging-what-you-do)).

1. The APN opportunity is **approved**.

1. The migration details are **submitted** (not just saved).

1. The engagement is in **review** status.

Once these conditions are true, the tag appears in your engagement. If the tag is missing, verify these three conditions before you proceed.

## What you need to do
<a name="auto-tagging-what-you-do"></a>

Complete the following steps to set up auto-tagging for your migration:

1. Create a **workspace** in AWS Transform.

1. Attach the workspace to your engagement.

1. Create a **migration job** in the workspace. For VMware migrations, select **Migration V3**.

1. Run migration planning and accept the plan.

1. When connecting to the AWS target account, **select the APN tag**. The migration agent uses this tag for all resources it creates.

1. Run the migration job for the servers in scope.

1. Apply the MAP tag to the server inventory, using one of the following options:

   **Option A – Update the inventory CSV**

   1. Download the inventory of the servers to be migrated from the **Artifacts** tab of your workspace.

   1. Update the tagging fields in the CSV:


<table>
<thead>
  <tr><th>Field</th><th>Value</th></tr>
</thead>
<tbody>
  <tr><td><code>map-tagging</code></td><td><code>TRUE</code></td></tr>
  <tr><td><code>map-tag-key</code></td><td><code>aws-apn-id</code></td></tr>
  <tr><td><code>map-tag-value</code></td><td>Your tag value (for example, <code>migra-abcdefg123456</code>)</td></tr>
</tbody>
</table>


   1. Import the updated CSV file back into the migration job.

   **Option B – Ask the migration agent in chat**

   In the job chat, ask the migration agent to apply the MAP tag to the servers in scope. For example:

   ```
   Apply the MAP tag aws-apn-id with value migra-abcdefg123456 to all servers in this wave.
   ```

## Validating the tag
<a name="auto-tagging-validating"></a>

### Before you proceed with the migration
<a name="auto-tagging-validating-before"></a>

Before you start the migration, confirm with the migration agent in the job chat which tag key and tag value it will apply to the migrated resources. This lets you catch an incorrect or missing tag before any resources are created, and before any untagged spend occurs.

For example, ask the agent:

```
Which MAP tag key and value will be applied to the migrated instances?
```

Confirm that the agent returns:


| Field | Expected value | 
| --- | --- | 
| Tag key | aws-apn-id | 
| Tag value | Your tag value (for example, migra-abcdefg123456) | 

If the tag key or value is incorrect or missing, update it (see step 7 in [What you need to do](#auto-tagging-what-you-do)) and confirm with the agent again before you proceed.

### After the migration completes
<a name="auto-tagging-validating-after"></a>

Verify that the tag was applied correctly to the migrated resources:

1. Copy the instance ID (or resource ID) from the migration job results.

1. Open the relevant AWS console (for example, Amazon EC2) in the target account.

1. Confirm that the tag `aws-apn-id` appears on the resource with the correct value.

If the tag is missing from a migrated resource:
+ Confirm that the APN tag was selected during the target account connection step.
+ Confirm that the tagging fields were applied to the inventory, either by re-importing the CSV with `map-tagging = TRUE` and the correct `map-tag-key` and `map-tag-value`, or by asking the migration agent in chat. You can download the inventory from the **Artifacts** tab of your workspace.
+ If the migration has already completed and the APN tag was not inherited or applied, you can apply the tag manually to the resource. This way you don't need to re-run the migration job. For instructions, see [Tagging Resources](getting-started-step2.md).

## Related resources
<a name="auto-tagging-resources"></a>
+ [AWS Transform VMware workshop: Create a workspace and job](https://catalog.workshops.aws/aws-transform-vmware/en-US/3-create-q-workspace-job)