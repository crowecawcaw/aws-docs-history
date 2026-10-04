

# Tutorial: Gate a GitHub Actions deployment with a scoped penetration test
<a name="sample-cicd-github"></a>

**Public preview**  
CI/CD pipeline integration is in preview and is subject to change.

This tutorial walks through a complete, reproducible setup that runs a continuous, scoped AWS Security Agent penetration test as a **post-deployment gate** in GitHub Actions. You deploy an intentionally vulnerable sample application to a staging environment, then let AWS Security Agent test the deployed change and block promotion to production when it finds a vulnerability.

**Note**  
Running a penetration test job and hosting the sample application might result in charges to your AWS account. For pricing details, see [AWS Security Agent pricing](https://aws.amazon.com/continuum/pricing/).

For the concepts behind the integration — how the test is scoped to the deployed change, how OIDC authentication works, and how gating decisions are made — see [Run penetration tests from your CI/CD pipeline](cicd-pentest.md). This tutorial applies those concepts to a concrete GitHub repository.

**Intentional vulnerability**  
The sample application in this tutorial contains a deliberate SQL injection vulnerability so that the gate has a real finding to block on. Deploy it only to an isolated, non-production environment that you control, and remove it when you finish. Do not expose it to the public internet or connect it to production data.

## Prerequisites
<a name="_prerequisites"></a>

Before you start, make sure you have the following:
+ An AWS account, and permission in it to create an IAM OIDC identity provider, an IAM role, and AWS Security Agent resources.
+ A GitHub repository that you own, on `github.com`, in which you can add workflows and configure environments. This tutorial uses the placeholder repository `my-org/my-app`; substitute your own repository throughout.
+ A staging environment that the sample application can deploy to, reachable from the network where your penetration test runs (the public internet, or a VPC in your AWS account for a private target). See [Connect agent to private VPC resources](connect-agent-vpc.md) for private targets.
+ The AWS Security Agent one-time setup described in [Run penetration tests from your CI/CD pipeline](cicd-pentest.md) under **Before you start**: a verified target domain, a CI/CD-enabled penetration test, your GitHub repository connected as a source control integration, and the Agent Space ID (`as-…​`) and penetration test ID (`pt-…​`) that identify them.

Throughout this tutorial, replace the following placeholders with your own values:


| Placeholder | Replace with | 
| --- | --- | 
|  `111122223333`  | Your 12-digit AWS account ID. | 
|  `AGENT_SPACE_ID` (`as-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`) | Your Agent Space ID. | 
|  `PENTEST_ID` (`pt-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`) | Your CI/CD-enabled penetration test ID. | 
|  `my-org/my-app`  | Your GitHub organization and repository. | 
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

## Step 2: Set up GitHub OIDC and an IAM role
<a name="_step_2_set_up_github_oidc_and_an_iam_role"></a>

The workflow authenticates to AWS with GitHub OIDC — no long-lived access keys. Do this once in your AWS account.

1. If you do not already have one, create the GitHub OIDC identity provider:

   ```
   aws iam create-open-id-connect-provider \
     --url https://token.actions.githubusercontent.com \
     --client-id-list sts.amazonaws.com
   ```

1. Create the IAM role with a trust policy scoped to your repository and branch. Save the following as `trust-policy.json`, replacing the account ID and repository:

   ```
   {
     "Version": "2012-10-17",		 	 	 
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": {
           "Federated": "arn:aws:iam::111122223333:oidc-provider/token.actions.githubusercontent.com"
         },
         "Action": "sts:AssumeRoleWithWebIdentity",
         "Condition": {
           "StringEquals": {
             "token.actions.githubusercontent.com:aud": "sts.amazonaws.com"
           },
           "StringLike": {
             "token.actions.githubusercontent.com:sub": "repo:my-org/my-app:ref:refs/heads/main"
           }
         }
       }
     ]
   }
   ```

   For the reasoning behind scoping the `sub` claim and the immutable-subject caveat for newer repositories, see [Scope the trust policy to your pipeline](cicd-pentest.md#cicd-pentest-trust-policy).

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

1. Create the role and attach the policy. A penetration test job can run for tens of minutes, so create the role with a maximum session duration long enough to outlast the step’s timeout:

   ```
   aws iam create-role --role-name my-pentest-gate-role \
     --assume-role-policy-document file://trust-policy.json \
     --max-session-duration 7200
   
   aws iam put-role-policy --role-name my-pentest-gate-role \
     --policy-name securityagent-run-pentest \
     --policy-document file://permissions.json
   ```

   The role ARN for the workflow is `arn:aws:iam::111122223333:role/my-pentest-gate-role`.

## Step 3: Add the workflow
<a name="_step_3_add_the_workflow"></a>

Add `.github/workflows/deploy-and-pentest.yml` to your repository. The `deploy` job deploys the sample application to staging; the `security-pentest` job then runs the gate and, because production promotion depends on it, blocks production when the gate fails.

```
name: Deploy and pentest
on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: staging
    steps:
      - uses: actions/checkout@v4
        with:
          persist-credentials: false
      - run: ./deploy.sh staging

  security-pentest:
    needs: [deploy]
    runs-on: ubuntu-latest
    permissions:
      # Required for the OIDC credential exchange.
      id-token: write
      # Write rather than read: the gate records the commit it last cleared as a
      # ref in this repository and reads it back to test only what changed since.
      # With read access the marker never advances and every run tests full scope.
      contents: write
      # Lets the gate find the last successful run of this workflow to use as the
      # base commit. Without it that lookup is denied and the gate falls back to
      # the parent commit, testing a narrower range than intended.
      actions: read
      # Same, for deployment and deployment_status triggers, where the base is
      # the last successful deployment.
      deployments: read
    steps:
      - uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::111122223333:role/my-pentest-gate-role
          aws-region: us-west-2
          role-duration-seconds: 7200
      - uses: aws-actions/aws-continuum-run-pentest@v1
        with:
          agent-space-id: as-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
          pentest-id: pt-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
          severity-threshold: HIGH
          on-scope-conflict: block
          timeout-minutes: "45"

  deploy-prod:
    needs: [security-pentest]
    runs-on: ubuntu-latest
    environment: production
    steps:
      - uses: actions/checkout@v4
        with:
          persist-credentials: false
      - run: ./deploy.sh production
```

Because `deploy-prod` declares `needs: [security-pentest]`, GitHub skips it whenever the gate job fails, so a change with a `HIGH` (or higher) finding never reaches production.

The `security-pentest` job’s four workflow permissions each serve a specific part of the gate:
+  `id-token: write` mints the OIDC token for the credential exchange.
+  `contents: write` lets the gate read **and advance** the baseline marker it keeps as a ref in your repository. Read access is not enough: the marker would never advance, and every run would test a wider range than intended.
+  `actions: read` lets the gate use the last successful run of this workflow as the base commit when it has no marker to read.
+  `deployments: read` does the same for `deployment` and `deployment_status` triggers, where the base is the last successful deployment.

Grant the last two even though this tutorial’s first run has no marker yet. They are what the documented fallbacks need, and without them the lookup is denied and the gate silently falls back to the parent commit — testing one commit instead of the range you deployed.

This tutorial does not publish findings to GitHub’s Security tab, so it does not grant `security-events: write`. Add that permission only if you also set the `upload-sarif` input. The upload runs only on a change that was tested and produced findings, so enabling it on a scoped-out or findings-free run does nothing.

**Note**  
Pin `aws-actions/aws-continuum-run-pentest` to a specific commit SHA (for example, `aws-actions/aws-continuum-run-pentest@<commit-sha>`) rather than a moving tag, so that a change to the upstream action cannot alter what runs in your pipeline without your review. See [How the integration differs by provider](cicd-pentest.md#cicd-pentest-choose-provider).

## Step 4: Validate your setup with a dry run
<a name="_step_4_validate_your_setup_with_a_dry_run"></a>

Before you rely on the gate, run it once in dry-run mode. Add `dry-run: "true"` to the action inputs and trigger the workflow:

```
      - uses: aws-actions/aws-continuum-run-pentest@v1
        with:
          agent-space-id: as-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
          pentest-id: pt-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
          dry-run: "true"
```

The dry run checks AWS authentication, the Region, and that your repository resolves to its integration — without starting a billable penetration test job. If it fails, it surfaces the common setup mistakes (a bad OIDC trust policy, a Region mismatch, or a repository that is not connected) in seconds. When it passes, remove the `dry-run` input and continue. For more information, see [Validate your setup before you trust the gate](cicd-pentest.md#cicd-pentest-validate).

## Step 5: Trigger the gate and read the result
<a name="_step_5_trigger_the_gate_and_read_the_result"></a>

Push a commit to `main` that changes the vulnerable endpoint. This triggers the workflow: the `deploy` job deploys the change to staging, then the `security-pentest` job starts a penetration test scoped to that change.

Open the workflow run under the repository’s **Actions** tab and watch the `security-pentest` job:

1.  **Configure AWS credentials** – GitHub mints an OIDC token and the runner assumes your role. No stored secrets are involved.

1.  **Run AWS Security Agent pentest** – the action resolves your repository, starts a scoped job, polls it to completion, and evaluates the findings against your `severity-threshold`.

A scoped penetration test typically runs for tens of minutes, so the step sits **in progress** for a while. That is expected, not a hang. The step ends when the job reaches a terminal state or the `timeout-minutes` elapses.

Because the deployed change introduced a SQL injection vulnerability, AWS Security Agent returns an **in scope** decision with a `HIGH` (or higher) finding. The `security-pentest` job fails, and because the production job depends on it, promotion to production is blocked.

The job summary records the verdict: the scope decision, the severity threshold the run was evaluated against, the finding counts, and whether the gate blocked.

![The GitHub Actions job summary showing the gate blocked on one finding at or above HIGH](https://docs.aws.amazon.com/securityagent/latest/userguide/images/sample-cicd-github-blocked.png)


The action also sets outputs you can consume in later steps, including `scope-decision` (`IN_SCOPE`, `SCOPED_OUT`, or `SCOPE_CONFLICT`), `status`, `blocking-findings-count` (the findings at or above your threshold — the ones that fail the step), and `total-findings-count` (every finding the run inspected, at any severity). Both counts are absent on a run that never evaluated findings, such as a dry run, so read `status` and `scope-decision` to tell that apart from a run that genuinely found nothing. For the full gating behavior — including how authentication failures always block and how you choose fail-closed or fail-open for infrastructure errors — see [Choose how the pipeline responds](cicd-pentest.md#cicd-pentest-gating).

## Step 6: Fix the finding and confirm the gate passes
<a name="_step_6_fix_the_finding_and_confirm_the_gate_passes"></a>

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

Push the fix to `main`. The workflow redeploys the change and runs the gate again against the new commit. With the injection removed, AWS Security Agent finds no findings at or above `HIGH`, the `security-pentest` job passes, and promotion to production proceeds.

The job summary shows the same checks for the new commit, with no findings at or above the threshold and a passing verdict.

![The GitHub Actions job summary showing the gate passed with no findings at or above HIGH](https://docs.aws.amazon.com/securityagent/latest/userguide/images/sample-cicd-github-passed.png)


## Clean up
<a name="_clean_up"></a>

To avoid ongoing cost and to remove the intentionally vulnerable application:

1. Tear down the sample application from your staging environment.

1. Delete the workflow file, or disable it, if you do not intend to keep the gate.

1. If you created the IAM role and OIDC provider only for this tutorial, delete them:

   ```
   aws iam delete-role-policy --role-name my-pentest-gate-role \
     --policy-name securityagent-run-pentest
   aws iam delete-role --role-name my-pentest-gate-role
   aws iam delete-open-id-connect-provider \
     --open-id-connect-provider-arn arn:aws:iam::111122223333:oidc-provider/token.actions.githubusercontent.com
   ```

## Related topics
<a name="_related_topics"></a>
+  [Run penetration tests from your CI/CD pipeline](cicd-pentest.md) – concepts and reference for the CI/CD pipeline integration.
+  [Tutorial: Gate a GitLab CI/CD deployment with a scoped penetration test](sample-cicd-gitlab.md), [Tutorial: Gate a Bitbucket Pipelines deployment with a scoped penetration test](sample-cicd-bitbucket.md), [Tutorial: Gate an Azure DevOps deployment with a scoped penetration test](sample-cicd-azure-devops.md) – the same tutorial for other CI/CD platforms.
+  [Security best practices for AWS Security Agent](security-best-practices.md) – general best practices, including testing against non-production environments.