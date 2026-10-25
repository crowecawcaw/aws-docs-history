

# Getting started with code vulnerabilities
<a name="cv-getting-started"></a>

AWS Continuum scans your code sources for security vulnerabilities.

To start using AWS Continuum for code vulnerabilities, use a GitHub or Amazon S3 integration. If you don't have an integration, create one. Then create an environment that uses the integration.

By default, you can add up to 10 code repositories to an environment across all of its integrations. Integrations and environments are subject to additional quotas. For more information about quotas and requesting an increase, see [Quotas for AWS Continuum](quotas.md).

## Connecting a code source
<a name="cv-getting-started-enable"></a>

If you already have an integration, continue to [Creating an environment](#cv-getting-started-s3-environment).

Otherwise, choose the procedure for your code source:
+ For GitHub, follow [Getting started through GitHub](#cv-getting-started-github).
+ For Amazon S3, follow [Getting started through Amazon S3](#cv-getting-started-s3).

## Getting started through GitHub
<a name="cv-getting-started-github"></a>

To scan code hosted in GitHub, connect a GitHub integration. Then create an environment that uses the integration.

Use a GitHub account that can install the GitHub app, or request approval from an organization owner.

To configure a GitHub integration, do the following:

1. Open the AWS Continuum console at [https://console.aws.amazon.com/continuum/](https://console.aws.amazon.com/continuum/).

1. Under **Code vulnerabilities**, choose **Integrations**.

1. Choose **Add integration**.

1. For **Source provider**, select **GitHub**.

1. For **Name**, enter an integration name.

1. For **GitHub account**, select **Personal account** or **Organization**.

1. If you selected **Organization**, enter the GitHub organization name for **Organization name**.

To install the GitHub app and authorize the integration, continue in the same form:

1. If the GitHub app is not installed, choose **Install GitHub app**. Install the app in the account that you selected.

1. If GitHub requires organization approval, wait for an owner to approve the installation.

1. If you opened the GitHub installation tab, close it and return to the AWS Continuum console.

1. Choose **Authorize with GitHub and create**.

1. Complete authorization in the GitHub window.

1. Return to the AWS Continuum console.

If the console still shows **Waiting for GitHub** after you authorize, choose **Cancel authorization**. Start authorization again.

After you create the integration, the console opens **Create environment**. Continue to [Creating an environment](#cv-getting-started-s3-environment).

## Getting started through Amazon S3
<a name="cv-getting-started-s3"></a>

To scan code stored in Amazon S3, prepare a bucket with your code. Create an AWS Identity and Access Management (IAM) role that grants AWS Continuum access to the bucket. Then connect an Amazon S3 integration and create an environment that uses it.

In the following example, replace {{amzn-s3-demo-bucket}} with your bucket name. Replace {{my-app.zip}} with your package file name.

The example source URI is `s3://{{amzn-s3-demo-bucket}}/code/{{my-app.zip}}`. Its object key is `code/{{my-app.zip}}`. The corresponding **Source code base path** value is `code/`.

To prepare an Amazon S3 source, do the following:

1. Create an Amazon S3 bucket in the same account and AWS Region where you enable AWS Continuum.

1. Choose a prefix in the bucket for your source code, such as `code/`. You configure this prefix when creating the environment.

1. Upload your code under the chosen prefix as a .zip package. For instructions on uploading objects, see [Uploading objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html) in the *Amazon S3 User Guide*.

1. In the Amazon S3 console, on **Upload: status**, confirm that the upload succeeded. If the upload fails, resolve the error before continuing.

### Granting access to the bucket
<a name="cv-getting-started-s3-role"></a>

As an administrator, create an IAM role in the same account as the bucket. The role path must be `/continuum/integrations/`. The role needs a permissions policy for the bucket and a trust policy so that AWS Continuum can assume the role.

In addition to the read permissions for the console, the IAM principal that creates the integration must have the following permissions:
+ `continuum:CreateIntegration` to create the integration
+ `iam:ListRoles` to select the integration role
+ `s3:ListAllMyBuckets` to browse Amazon S3 buckets
+ `iam:PassRole` to pass the integration role

Restrict `iam:PassRole` to the integration role. Use the `iam:PassedToService` condition key with the value `continuum.amazonaws.com`.

For information about permissions required to create an integration in the console, see [Using the AWS Continuum console](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-console).

Save the following JSON permissions policy as `integration-permissions.json`. Use it to let AWS Continuum list the bucket and read source objects and versions under your code and context prefixes. It also grants AWS Continuum permission to upload and read patches under `continuum-patches/`.

Grant `s3:ListBucket` without a condition. AWS Continuum uses this permission to validate access to the bucket when you create the integration.

Use each configured prefix exactly, including any trailing slash. If you omit these values, the defaults are `code/` and `context/`, respectively. Your source files can be stored under other prefixes, but the policy must grant access to those prefixes.

Replace {{bucket-name}} with the bucket used by your integration. Replace {{code-prefix}} with the **Source code base path** value. Replace {{context-prefix}} with the **Knowledge documents base path** value.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ListSourceBucket",
      "Effect": "Allow",
      "Action": [
        "s3:ListBucket"
      ],
      "Resource": "arn:aws:s3:::{{bucket-name}}"
    },
    {
      "Sid": "ReadSourcePrefixes",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:GetObjectVersion"
      ],
      "Resource": [
        "arn:aws:s3:::{{bucket-name}}/{{code-prefix}}*",
        "arn:aws:s3:::{{bucket-name}}/{{context-prefix}}*"
      ]
    },
    {
      "Sid": "DeliverContinuumPatches",
      "Effect": "Allow",
      "Action": [
        "s3:PutObject",
        "s3:GetObject",
        "s3:GetObjectVersion"
      ],
      "Resource": "arn:aws:s3:::{{bucket-name}}/continuum-patches/*"
    }
  ]
}
```

Use the following trust policy so that the AWS Continuum service principal, `continuum.amazonaws.com`, can assume the role with an external ID. Replace {{external-id}} with the external ID that you enter when creating the integration. Save the policy as `trust-policy.json`.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ContinuumAccess",
      "Effect": "Allow",
      "Principal": {
        "Service": "continuum.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "sts:ExternalId": "{{external-id}}"
        }
      }
    }
  ]
}
```

To create the role, configure the AWS CLI with a customer administrator principal that can create the role and attach an inline policy. Save both policy files in the current directory.

If a command fails, resolve the error before continuing. If `create-role` returns `EntityAlreadyExists`, choose an unused role name and use it consistently in these commands.

**To create the integration role (AWS CLI)**

1. Create the role with the required path.

   ```
   aws iam create-role \
       --role-name ContinuumIntegrationRole \
       --path /continuum/integrations/ \
       --assume-role-policy-document file://trust-policy.json
   ```

   The command returns details of the new role.

1. Attach the bucket permissions as an inline policy.

   ```
   aws iam put-role-policy \
       --role-name ContinuumIntegrationRole \
       --policy-name ContinuumIntegrationAccess \
       --policy-document file://integration-permissions.json
   ```

   This command produces no output on success.

1. Verify that the role's Amazon Resource Name (ARN) includes `role/continuum/integrations/`.

   ```
   aws iam get-role \
       --role-name ContinuumIntegrationRole \
       --query 'Role.Arn' \
       --output text
   ```

   The output has the following format, where {{account-id}} is your AWS account ID and {{role-name}} is the role name that you used in the commands:

   ```
   arn:aws:iam::{{account-id}}:role/continuum/integrations/{{role-name}}
   ```

If a command returns an access denied error, ask your administrator to check your permissions. These commands require `iam:CreateRole`, `iam:PutRolePolicy`, and `iam:GetRole`, respectively.

For information about diagnosing policies that deny access, see [Troubleshoot access denied error messages](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_access-denied.html) in the *IAM User Guide*.

Changes to IAM roles and policies can take time to become available. Before you use the role to create the integration, allow time for the changes to propagate. For more information, see [Changes that I make are not always immediately visible](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_general.html#troubleshoot_general_eventual-consistency) in the *IAM User Guide*.

Keep the role and its policies while an integration uses them. When you no longer need an integration, first update or delete every environment that references it, and then delete the integration. After deleting every integration that uses the role, delete the role and its policies if no other workload uses them. For information about deleting roles, see [Delete roles or instance profiles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_delete.html) in the *IAM User Guide*.

For more information about external IDs, see [Access to AWS accounts owned by third parties](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_third-party.html) in the *IAM User Guide*.

### Connecting an S3 integration
<a name="cv-getting-started-s3-integration"></a>

After you prepare the bucket and IAM role, create an Amazon S3 integration. The integration connects the bucket and role so that an environment can access your code.

1. Open the AWS Continuum console at [https://console.aws.amazon.com/continuum/](https://console.aws.amazon.com/continuum/).

1. Under **Code vulnerabilities**, choose **Integrations**.

1. Choose **Add integration**.

1. For **Source provider**, select Amazon S3.

1. For **Name**, enter an integration name.

1. For **S3 bucket**, use one of the following options:
   + To select a bucket, choose **Browse S3**. Select your bucket.
   + To enter an ARN, choose **Enter bucket ARN manually**. For **Bucket ARN**, enter the bucket ARN.

To grant access and create the integration, continue in the same form:

1. For **IAM role ARN**, select the role that you created.

1. For **External ID**, enter the value required by the role's `sts:ExternalId` condition. The integration value must match the trust policy value.

1. Choose **Create integration**.

After you create the integration, the console opens **Create environment**. Continue to [Creating an environment](#cv-getting-started-s3-environment).

If access validation fails, check the required role path. Verify the integration role trust policy and matching external ID. Check that the role's permissions allow access to the bucket and prefixes that you use.

## Creating an environment
<a name="cv-getting-started-s3-environment"></a>

An environment defines the code sources, scan frequency, and patch delivery settings that AWS Continuum uses to scan your code.

After you create a GitHub or Amazon S3 integration, the console opens **Create environment**.

If you already have an integration, use these steps to open **Create environment**:

1. Open the AWS Continuum console at [https://console.aws.amazon.com/continuum/](https://console.aws.amazon.com/continuum/).

1. In the navigation pane, choose **Environments**.

1. Choose **Create environment**.

Keep **Automatically deliver remediation patches** selected to deliver patches to your code source. AWS Continuum uploads patches to your Amazon S3 bucket or opens pull requests in your GitHub repositories.

To configure the environment, continue in the same form:

1. For **Environment name**, enter a name.

1. In **Code sources**, for **Integration**, select the integration that you want to use.

1. Configure the code source:

   1. If you selected a GitHub integration, for **Repositories**, enter the repositories that you want to scan. Enter each repository as `owner/repository`.

   1. If you selected an Amazon S3 integration, for **Source code base path**, enter the prefix where you uploaded your code. The default is `code/`.

   1. If you selected an Amazon S3 integration and uploaded custom context, enter its prefix in **Knowledge documents base path**. The default is `context/`.

To set the scan frequency and create the environment, continue in the same form:

1. Expand **Scan schedule**.

1. In **Scan schedule**, for **Scan frequency**, select one of the following options:
   + **Every day**
   + **Every 2 days**
   + **Every 7 days**
   + **Manual only**

1. (Optional) To change patch delivery or allowed dependency domains, expand **Advanced**.

1. (Optional) Under **Advanced**, select or clear **Automatically deliver remediation patches**.

1. (Optional) Under **Advanced**, for **Allowed dependency domains**, enter additional domains needed to build your code.

1. Choose **Create environment**.

## Following the first scan
<a name="cv-getting-started-first-scan"></a>

After you create the environment, the console opens **Environments**. Creating the environment starts the first build and scan. The selected scan frequency applies to subsequent scans.

To follow the first scan, do the following:

1. On the **Environments** page, find the **Created {{environment-name}}** notification. Choose **View environment details**.

1. Choose the **Scans** tab.

1. On the **Scans** tab, choose the refresh icon (**Refresh scans**) to update the results.

1. Review the **Status** column for the first scan. Refresh the results to check for updates.

When a scan completes successfully, its **Status** changes to **Succeeded**. AWS Continuum may continue processing findings into issues and generating patches after the scan completes.

To follow this processing, choose the **Findings** or **Issues** tab and refresh the results. Open an issue to review its processing status and any available patches.

To stop automatic scans, set **Scan frequency** to **Manual only**. For instructions on changing the scan frequency, see [Triggering a scan](cv-triggering-scan.md).