

# Permissions for shared transformation definitions

Each share has exactly one permission. AWS Transform custom provides four AWS RAM managed permissions. `Execute` is the base. `ExecuteWithLearnings` adds the owner's lessons. The other two each add one thing to `ExecuteWithLearnings`: contribution or download. They don't include each other. In the AWS Transform CLI, the `--managed-policy` option and the **Managed Policy** column of `atx custom def share list` refer to these AWS RAM managed permissions. They aren't IAM policies.


| CLI `--managed-policy` value | AWS RAM managed permission | Actions allowed | What the consumer can do | 
| --- | --- | --- | --- | 
| Execute (default) | AWSRAMPermissionTransformCustomPackageExecute | transform-custom:ExecuteTransformation | Find the TD with atx custom def list and run it. Runs don't use the owner's lessons. The consumer can't download the TD with atx custom def get. | 
| ExecuteWithLearnings | AWSRAMPermissionTransformCustomPackageExecuteWithLearnings | The above, plus transform-custom:ListKnowledgeItems and transform-custom:GetKnowledgeItem | Run the TD with the owner's current and future lessons. The consumer can also list and read those lessons. | 
| ExecuteWithLearningsAndContribution | AWSRAMPermissionTransformCustomPackageExecuteWithLearningsAndContribution | ExecuteWithLearnings, plus transform-custom:ContributeKnowledgeItems | Run with the owner's lessons, and contribute lessons from the consumer's own runs to the owner's TD. The consumer opts in for each run. | 
| ExecuteWithLearningsAndPackageDownload | AWSRAMPermissionTransformCustomPackageExecuteWithLearningsAndPackageDownload | ExecuteWithLearnings, plus transform-custom:GetTransformationPackageUrl | Run with the owner's lessons, and download the TD with atx custom def get to adapt it and publish a separate TD in their own account. | 

The CLI accepts `--managed-policy` values in any letter case.

The AWS managed permission ARNs use the format `arn:aws:ram::aws:permission/{{name}}`, for example `arn:aws:ram::aws:permission/AWSRAMPermissionTransformCustomPackageExecute`. To list them, run the following command.

```bash
aws ram list-permissions --resource-type transform-custom:Package --region us-east-1
```

In `--resource-type`, the service prefix `transform-custom` is case sensitive and the resource name isn't. For example, `transform-custom:Package` and `transform-custom:package` work, and `Transform-Custom:package` doesn't.

**What a consumer can't do with any permission**
+ Change, delete, or publish a new version of the shared TD.
+ Reshare the TD with another account.
+ Tag the TD.
+ See the owner's other TDs, or any TD that isn't shared with the consumer.
+ See other consumers' repositories, runs, or identities.

**Things to know**
+ No AWS managed permission includes both download and contribution. An owner who needs both can use a customer managed permission.
+ **Customer managed permissions** – You can create customer managed permissions for `transform-custom:Package` in AWS RAM and attach them to a share in the AWS RAM console or with the AWS CLI. In this release, `atx custom def share` creates and updates shares only with the four AWS managed permissions. When a share uses a customer managed permission, `atx custom def share list` shows it as `{{name}} (custom)`. If you run `atx custom def share update` on that share, the AWS managed permission that you pass replaces it.
+ **IAM policies still apply in the consumer account** – The share's permission is the most that a consumer can do. A consumer's IAM principals also need identity-based policies that allow those actions on the shared TD's ARN. For more information, see [Identity-based policy examples for sharing](custom-sharing-policy-examples.md).
+ **Changing a permission takes effect for new requests** – If you reduce a share's permission, the consumer loses the removed actions for new requests. Content that the consumer already downloaded, and any TD that they published from it, can't be retracted. Runs that already started continue to completion.

**Note**  
A consumer can't use your lessons without also being able to read them. Any permission that includes lessons lets the consumer list and read them. If your lessons contain anything that you don't want the consumer to see, use `Execute`.