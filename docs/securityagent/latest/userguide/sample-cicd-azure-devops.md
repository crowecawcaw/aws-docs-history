

# Tutorial: Gate an Azure DevOps deployment with a scoped penetration test
<a name="sample-cicd-azure-devops"></a>

**Public preview**  
CI/CD pipeline integration is in preview and is subject to change.

This tutorial walks through a complete, reproducible setup that runs a continuous, scoped AWS Security Agent penetration test as a **post-deployment gate** in Azure DevOps Pipelines. You deploy an intentionally vulnerable sample application to a staging environment, then let AWS Security Agent test the deployed change and block promotion to production when it finds a vulnerability.

**Note**  
Running a penetration test job and hosting the sample application might result in charges to your AWS account. For pricing details, see [AWS Security Agent pricing](https://aws.amazon.com/continuum/pricing/).

For the concepts behind the integration — how the test is scoped to the deployed change, how OIDC authentication works, and how gating decisions are made — see [Run penetration tests from your CI/CD pipeline](cicd-pentest.md). This tutorial applies those concepts to a concrete Azure DevOps project.

**Intentional vulnerability**  
The sample application in this tutorial contains a deliberate SQL injection vulnerability so that the gate has a real finding to block on. Deploy it only to an isolated, non-production environment that you control, and remove it when you finish. Do not expose it to the public internet or connect it to production data.

## Prerequisites
<a name="_prerequisites"></a>

Before you start, make sure you have the following:
+ An AWS account, and permission in it to create an IAM OIDC identity provider, an IAM role, and AWS Security Agent resources.
+ An Azure DevOps organization and project that you own, in which you can create service connections, install extensions from the Visual Studio Marketplace, and edit pipelines.
+ The **AWS Toolkit for Azure DevOps** extension installed in your organization. This tutorial uses an AWS service connection from that extension for authentication.
+ The `RunPentest` task available in your organization. The task is not yet carried by a published release of the AWS Toolkit for Azure DevOps, so installing the extension alone does not provide it. Confirm the task appears in your pipeline task list before you start; if it does not, contact AWS Support for the current way to obtain it.
+ The build service identity granted permission to record the baseline. The gate stores the commit it last cleared using the pipeline’s own `System.AccessToken`, and the identity that token represents needs **Contribute** on the repository when your source is Azure Repos, or **Tag builds** when your source is GitHub, GitLab, or Bitbucket. Grant it under **Project settings**, **Repositories** or **Pipelines**, **Settings**.
**Important**  
Without that permission the gate still runs and still blocks correctly, but the baseline never advances: every run resolves its base from a fallback rung instead, testing a narrower range than you deployed, and nothing in the pipeline fails to tell you.  
You do not need to map the token into the task with `env: SYSTEM_ACCESSTOKEN: $(System.AccessToken)`. The task reads `System.AccessToken` directly, and the agent provides it without a mapping. That mapping is needed only for script steps, so adding it does no harm but fixes nothing — if the baseline is not advancing, the permission is the cause.
+ A staging environment that the sample application can deploy to, reachable from the network where your penetration test runs (the public internet, or a VPC in your AWS account for a private target). See [Connect agent to private VPC resources](connect-agent-vpc.md) for private targets.
+ An agent pool whose job timeout exceeds the gate’s own timeout. A free Microsoft-hosted agent is killed at 60 minutes, which is also the task’s default `timeoutMinutes`, so on that tier the agent is terminated before the gate can report a timeout of its own. This tutorial sets `timeoutMinutes: "45"`, which fits. If you raise it, use a paid or self-hosted pool.
+ The AWS Security Agent one-time setup described in [Run penetration tests from your CI/CD pipeline](cicd-pentest.md) under **Before you start**: a verified target domain, a CI/CD-enabled penetration test, your repository connected as a source control integration, and the Agent Space ID (`as-…​`) and penetration test ID (`pt-…​`) that identify them.

Throughout this tutorial, replace the following placeholders with your own values:


| Placeholder | Replace with | 
| --- | --- | 
|  `111122223333`  | Your 12-digit AWS account ID. | 
|  `AGENT_SPACE_ID` (`as-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`) | Your Agent Space ID. | 
|  `PENTEST_ID` (`pt-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`) | Your CI/CD-enabled penetration test ID. | 
|  `us-west-2`  | The AWS Region where your Agent Space and penetration test are located. | 

## Step 1: Create the vulnerable sample application
<a name="_step_1_create_the_vulnerable_sample_application"></a>

Create a small Flask application with one endpoint that builds a SQL query by string concatenation — a classic SQL injection. In your repository, add `app.py`:

```
import sqlite3
from flask import Flask, request

app = Flask(__name__)


@app.route("/products")
def products():
    # Intentionally vulnerable: user input is concatenated directly into SQL.
    category = request.args.get("category", "")
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    query = "SELECT name, price FROM products WHERE category = '" + category + "'"
    rows = cursor.execute(query).fetchall()
    conn.close()
    return {"products": rows}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
```

Add a `deploy.sh` script that deploys this application to your staging environment. The details depend on your infrastructure; the gate does not require any particular deployment mechanism, only that the application is running and reachable when the test runs.

## Step 2: Set up the IAM role for Azure DevOps OIDC
<a name="_step_2_set_up_the_iam_role_for_azure_devops_oidc"></a>

Azure DevOps authenticates to AWS through an AWS service connection that uses **workload identity federation** — no long-lived access keys. Azure DevOps issues a signed OIDC token for the pipeline, and AWS STS exchanges it for temporary credentials through an IAM role you create.

1. Create the IAM OIDC identity provider for Azure DevOps in your AWS account. The provider URL is your organization’s Azure DevOps issuer, and the audience is `api://AzureADTokenExchange`:

   ```
   aws iam create-open-id-connect-provider \
     --url https://vstoken.dev.azure.com/YOUR_ORGANIZATION_ID \
     --client-id-list api://AzureADTokenExchange
   ```

   Confirm your organization’s exact issuer URL and audience from the service connection setup dialog in Azure DevOps (you obtain the **Issuer** and **Subject identifier** there, and the service connection also gives you an **Issuer** and **Subject** to paste into the trust policy).

1. Create the IAM role with a trust policy scoped to your Azure DevOps organization, project, and pipeline through the token’s subject. Save the following as `trust-policy.json`, replacing the account ID, issuer host, and subject:

   ```
   {
     "Version": "2012-10-17",		 	 	 
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": {
           "Federated": "arn:aws:iam::111122223333:oidc-provider/vstoken.dev.azure.com/YOUR_ORGANIZATION_ID"
         },
         "Action": "sts:AssumeRoleWithWebIdentity",
         "Condition": {
           "StringEquals": {
             "vstoken.dev.azure.com/YOUR_ORGANIZATION_ID:aud": "api://AzureADTokenExchange",
             "vstoken.dev.azure.com/YOUR_ORGANIZATION_ID:sub": "sc://YOUR_ORGANIZATION/YOUR_PROJECT/YOUR_SERVICE_CONNECTION_NAME"
           }
         }
       }
     ]
   }
   ```

   The subject identifies the specific service connection, which scopes the role to your organization, project, and pipeline. Use the exact **Subject identifier** that the service connection dialog shows. For the reasoning behind scoping the subject rather than using a wildcard, see [Scope the trust policy to your pipeline](cicd-pentest.md#cicd-pentest-trust-policy).

1. Save the least-privilege permissions policy as `permissions.json`:

   ```
   {
     "Version": "2012-10-17",		 	 	 
     "Statement": [
       {
         "Effect": "Allow",
         "Action": [
           "securityagent:StartPentestJob",
           "securityagent:BatchGetPentestJobs",
           "securityagent:StopPentestJob",
           "securityagent:ListFindings",
           "securityagent:BatchGetFindings",
           "securityagent:ListIntegratedResources"
         ],
         "Resource": "*"
       }
     ]
   }
   ```

   For what each action does, see [Grant least-privilege permissions](cicd-pentest.md#cicd-pentest-permissions-policy).

1. Create the role and attach the policy. A penetration test job can run for tens of minutes, so create the role with a maximum session duration long enough to outlast the task:

   ```
   aws iam create-role --role-name my-pentest-gate-role \
     --assume-role-policy-document file://trust-policy.json \
     --max-session-duration 7200
   
   aws iam put-role-policy --role-name my-pentest-gate-role \
     --policy-name securityagent-run-pentest \
     --policy-document file://permissions.json
   ```

   The role ARN for the pipeline is `arn:aws:iam::111122223333:role/my-pentest-gate-role`.

## Step 3: Create the AWS service connection
<a name="_step_3_create_the_aws_service_connection"></a>

In Azure DevOps, go to **Project settings**, **Service connections**, and create a new **AWS** service connection provided by the AWS Toolkit. Choose **workload identity federation** (OIDC) rather than access keys, and set:
+  **Role to assume** – `arn:aws:iam::111122223333:role/my-pentest-gate-role`.
+  **AWS Region** – `us-west-2`.

Name the connection (for example, `aws-pentest-gate`). Azure DevOps generates the issuer and subject values that you used in the trust policy in Step 2; if you created the role before the connection, update the trust policy’s subject to match the value the connection shows.

## Step 4: Add the pipeline task
<a name="_step_4_add_the_pipeline_task"></a>

Edit your pipeline YAML. Run the deploy stage, then a gate stage that depends on it. In the gate stage, run the AWS Toolkit task for the integration, referencing your service connection.

```
trigger:
  branches:
    include: [main]

stages:
  - stage: DeployStaging
    jobs:
      - job: deploy
        pool:
          vmImage: ubuntu-latest
        steps:
          - checkout: self
            persistCredentials: false
          - script: ./deploy.sh staging
            displayName: Deploy to staging

  - stage: SecurityGate
    dependsOn: DeployStaging
    jobs:
      - job: pentest
        pool:
          vmImage: ubuntu-latest
        steps:
          - task: RunPentest@1
            inputs:
              awsCredentials: aws-pentest-gate
              regionName: us-west-2
              agentSpaceId: "as-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
              pentestId: "pt-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
              severityThreshold: HIGH
              onScopeConflict: block
              timeoutMinutes: "45"

  - stage: DeployProd
    dependsOn: SecurityGate
    jobs:
      - job: deploy_prod
        pool:
          vmImage: ubuntu-latest
        steps:
          - checkout: self
            persistCredentials: false
          - script: ./deploy.sh production
            displayName: Deploy to production
```

Because `DeployProd` declares `dependsOn: SecurityGate` and a failed task fails its stage, the production stage does not run when the gate fails. The `awsCredentials` input references the service connection you created in Step 3, which supplies temporary credentials through workload identity federation.

## Step 5: Validate your setup with a dry run
<a name="_step_5_validate_your_setup_with_a_dry_run"></a>

Before you rely on the gate, run it once in dry-run mode. Add the dry-run input to the task and run the pipeline:

```
          - task: RunPentest@1
            inputs:
              awsCredentials: aws-pentest-gate
              regionName: us-west-2
              agentSpaceId: "as-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
              pentestId: "pt-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
              dryRun: "true"
```

The dry run checks AWS authentication, the Region, and that your repository resolves to its integration — without starting a billable penetration test job. It surfaces the common setup mistakes (a bad OIDC trust policy, a Region mismatch, or a repository that is not connected) in seconds. When it passes, remove the dry-run input and continue. For more information, see [Validate your setup before you trust the gate](cicd-pentest.md#cicd-pentest-validate).

**A dry run can become the next run’s base commit**  
On Azure DevOps the gate falls back to the last successful build of this pipeline when it has no baseline to read, and a dry-run build succeeds. So on a pipeline with no baseline yet — which is the case the first time you run this tutorial — the commit you dry-ran on can become the base of the next real run. The gate then tests only what changed after it, rather than the range you meant to gate.  
Dry-run on the commit you intend to gate next, so that the range is the one you want either way. If you have already dry-run on an earlier commit, pin the base explicitly on your first real run.

## Step 6: Trigger the gate and read the result
<a name="_step_6_trigger_the_gate_and_read_the_result"></a>

Push a commit to `main` that changes the vulnerable endpoint. This triggers the pipeline: the `DeployStaging` stage deploys the change, then the `SecurityGate` stage starts a penetration test scoped to that change.

Open the pipeline run and watch the gate task:

1. The AWS Toolkit task uses the service connection to obtain temporary AWS credentials through workload identity federation. No stored AWS keys are involved.

1. The task resolves your repository, starts a scoped job, polls it to completion, and evaluates the findings against your severity threshold.

A scoped penetration test typically runs for tens of minutes, so the task runs for a while. That is expected, not a hang.

Because the deployed change introduced a SQL injection vulnerability, AWS Security Agent returns an **in scope** decision with a `HIGH` (or higher) finding. The gate task fails, the `SecurityGate` stage fails, and any later production stage that depends on it does not run.

The run’s **Extensions** tab records the verdict: the scope decision, the severity threshold the run was evaluated against, the finding counts, and whether the gate blocked.

![The Azure DevOps Extensions tab showing the gate blocked on one finding at or above HIGH](https://docs.aws.amazon.com/securityagent/latest/userguide/images/sample-cicd-azure-devops-blocked.png)


For the full gating behavior — including how authentication failures always block and how you choose fail-closed or fail-open for infrastructure errors — see [Choose how the pipeline responds](cicd-pentest.md#cicd-pentest-gating).

## Step 7: Fix the finding and confirm the gate passes
<a name="_step_7_fix_the_finding_and_confirm_the_gate_passes"></a>

Fix the vulnerability by using a parameterized query instead of string concatenation. In `app.py`, replace the query construction:

```
    category = request.args.get("category", "")
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    query = "SELECT name, price FROM products WHERE category = ?"
    rows = cursor.execute(query, (category,)).fetchall()
    conn.close()
    return {"products": rows}
```

Push the fix to `main`. The pipeline redeploys the change and runs the gate again against the new commit. With the injection removed, AWS Security Agent finds no findings at or above `HIGH`, the gate task passes, and the production stage proceeds.

The **Extensions** tab shows the same checks for the new commit, with no findings at or above the threshold and a passing verdict.

![The Azure DevOps Extensions tab showing the gate passed with no findings at or above HIGH](https://docs.aws.amazon.com/securityagent/latest/userguide/images/sample-cicd-azure-devops-passed.png)


## Clean up
<a name="_clean_up"></a>

To avoid ongoing cost and to remove the intentionally vulnerable application:

1. Tear down the sample application from your staging environment.

1. Remove the gate stage from your pipeline, or disable the pipeline, if you do not intend to keep the gate.

1. Delete the AWS service connection if it was created only for this tutorial.

1. If you created the IAM role and OIDC provider only for this tutorial, delete them:

   ```
   aws iam delete-role-policy --role-name my-pentest-gate-role \
     --policy-name securityagent-run-pentest
   aws iam delete-role --role-name my-pentest-gate-role
   aws iam delete-open-id-connect-provider \
     --open-id-connect-provider-arn arn:aws:iam::111122223333:oidc-provider/vstoken.dev.azure.com/YOUR_ORGANIZATION_ID
   ```

## Related topics
<a name="_related_topics"></a>
+  [Run penetration tests from your CI/CD pipeline](cicd-pentest.md) – concepts and reference for the CI/CD pipeline integration.
+  [Tutorial: Gate a GitHub Actions deployment with a scoped penetration test](sample-cicd-github.md), [Tutorial: Gate a GitLab CI/CD deployment with a scoped penetration test](sample-cicd-gitlab.md), [Tutorial: Gate a Bitbucket Pipelines deployment with a scoped penetration test](sample-cicd-bitbucket.md) – the same tutorial for other CI/CD platforms.
+  [Security best practices for AWS Security Agent](security-best-practices.md) – general best practices, including testing against non-production environments.