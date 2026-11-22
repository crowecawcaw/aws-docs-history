

# Share a transformation definition

You can share a TD with the AWS Transform CLI, the AWS RAM console, or the AWS CLI. The AWS Transform CLI is the simplest. It finds the TD's ARN, creates the AWS RAM resource share, and attaches the managed permission for you.

## Share with the AWS Transform CLI
<a name="custom-sharing-share-cli"></a>

```bash
atx custom def share create -n {{td-name}} --target {{target}} [--managed-policy {{name}}]
```

The following table describes the options for `share create`.


| Option | Description | 
| --- | --- | 
| -n, --transformation-name | The name of a published TD in your account. | 
| --target | One target: a 12-digit AWS account ID, an organization ARN (arn:aws:organizations::{{management-account-id}}:organization/o-{{id}}), or an OU ARN (arn:aws:organizations::{{management-account-id}}:ou/o-{{id}}/ou-{{id}}). To share with several targets, run share create once for each. | 
| --managed-policy | Execute (default), ExecuteWithLearnings, ExecuteWithLearningsAndContribution, or ExecuteWithLearningsAndPackageDownload. | 
| --json | Print the result as JSON. | 

All share commands accept `--json`. None of them takes `--region`.

**Example – Share with an account outside your organization**

The following example shares a TD with an account outside your organization:

```bash
atx custom def share create -n java17-upgrade --target 444455556666
```

```
Share 6f1c2e8a-... created; waiting for AWS RAM...
Shared 'java17-upgrade' with account 444455556666.
  Share ID: 6f1c2e8a-...
  Status: Pending — waiting for 444455556666 to accept the invitation.
```

The consumer has 12 hours to accept. After that, the invitation expires. To invite the account again, run `share create` again.

**Example – Share with an OU and let runs use your lessons**

The following example shares a TD with an OU, with a permission that lets runs use your lessons:

```bash
atx custom def share create -n java17-upgrade \
  --target arn:aws:organizations::111122223333:ou/o-a1b2c3d4e5/ou-ab12-34cd56ef \
  --managed-policy ExecuteWithLearnings
```

Accounts in the OU get access right away, with no invitation.

```
Share {{share-id}} created; waiting for AWS RAM...
Shared 'java17-upgrade' with organizational unit ou-ab12-34cd56ef.
   Share ID: {{share-id}}
   Status: Active — accounts in ou-ab12-34cd56ef can use it now.
Note: ou-ab12-34cd56ef can also read this transformation definition's learnings.
```

**What the CLI does in special cases**

The following table shows what `share create` does in special cases.


| Case | Result | 
| --- | --- | 
| The TD is already shared with the target | '{{td-name}}' is already shared with {{target}} (share {{id}}, {{status}}). Nothing new is created. | 
| The target declined an earlier share | share create invites the account again into the same share, with the same share ID. | 
| The TD doesn't exist or isn't published | No published transformation definition named '{{td-name}}' in this account ({{Region}}). Drafts can't be shared — … | 
| The target is your own account | You can't share with your own account. | 
| The target isn't valid | --target must be a 12-digit account ID, an organization ARN, or an OU ARN. | 
| The permission isn't valid | --managed-policy must be one of: Execute, ExecuteWithLearnings, ExecuteWithLearningsAndContribution, ExecuteWithLearningsAndPackageDownload. | 

## Share with the AWS RAM console
<a name="custom-sharing-share-console"></a>

1. Open the [AWS RAM console](https://console.aws.amazon.com/ram/), and choose the Region where the TD is published.

1. Choose **Create resource share**.

1. Enter a name for the share.

1. For **Resource type**, choose **Transformation definitions**, and then choose the TD.

1. For the managed permission, choose one of the four `AWSRAMPermissionTransformCustomPackage…` permissions, or a customer managed permission.

1. Add principals: your organization, OUs, or account IDs. To share with accounts outside your organization, keep **Allow sharing with anyone** selected.

1. Review, and then choose **Create resource share**.

In the AWS RAM console, shared TDs appear with the resource type `transform-custom:Package` and the TD's ARN.

## Share with the AWS CLI
<a name="custom-sharing-share-aws-cli"></a>

The following AWS CLI command shares a TD with one account, with the `Execute` permission:

```bash
aws ram create-resource-share \
  --region us-east-1 \
  --name java17-upgrade-share \
  --resource-arns arn:aws:transform-custom:us-east-1:111122223333:package/java17-upgrade \
  --principals 444455556666 \
  --permission-arns arn:aws:ram::aws:permission/AWSRAMPermissionTransformCustomPackageExecute
```

`atx custom def share list --outgoing` lists every share that you own that contains a TD, however it was created. It also lists shares whose revoke didn't finish. Shares that you revoked aren't listed.