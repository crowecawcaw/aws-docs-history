

# Tutorial: Gate a Bitbucket Pipelines deployment with a scoped penetration test
<a name="sample-cicd-bitbucket"></a>

**Public preview**  
CI/CD pipeline integration is in preview and is subject to change.

This tutorial walks through a complete, reproducible setup that runs a continuous, scoped AWS Security Agent penetration test as a **post-deployment gate** in Bitbucket Pipelines. You deploy an intentionally vulnerable sample application to a staging environment, then let AWS Security Agent test the deployed change and block promotion to production when it finds a vulnerability.

**Note**  
Running a penetration test job and hosting the sample application might result in charges to your AWS account. For pricing details, see [AWS Security Agent pricing](https://aws.amazon.com/continuum/pricing/).

For the concepts behind the integration — how the test is scoped to the deployed change, how OIDC authentication works, and how gating decisions are made — see [Run penetration tests from your CI/CD pipeline](cicd-pentest.md). This tutorial applies those concepts to a concrete Bitbucket repository.

**Intentional vulnerability**  
The sample application in this tutorial contains a deliberate SQL injection vulnerability so that the gate has a real finding to block on. Deploy it only to an isolated, non-production environment that you control, and remove it when you finish. Do not expose it to the public internet or connect it to production data.

## Prerequisites
<a name="_prerequisites"></a>

Before you start, make sure you have the following:
+ An AWS account, and permission in it to create an IAM OIDC identity provider, an IAM role, and AWS Security Agent resources.
+ A Bitbucket Cloud repository that you own, in which you can edit `bitbucket-pipelines.yml` and repository settings. This tutorial uses the placeholder repository `my-workspace/my-app`; substitute your own workspace and repository throughout.
+ A staging environment that the sample application can deploy to, reachable from the network where your penetration test runs (the public internet, or a VPC in your AWS account for a private target). See [Connect agent to private VPC resources](connect-agent-vpc.md) for private targets.
+ The AWS Security Agent one-time setup described in [Run penetration tests from your CI/CD pipeline](cicd-pentest.md) under **Before you start**: a verified target domain, a CI/CD-enabled penetration test, your Bitbucket repository connected as a source control integration (see [Connect AWS Security Agent to Bitbucket repositories](connect-bitbucket.md)), and the Agent Space ID (`as-…​`) and penetration test ID (`pt-…​`) that identify them.
+ A Bitbucket access token with the **Pipelines variable** scope, for the baseline. On Bitbucket the gate cannot keep its baseline in git, because the REST API exposes only branches and tags, so it stores the commit it last cleared in a repository **pipelines variable** named `SECURITY_AGENT_BASELINE_` followed by a 40-character identifier derived from your Agent Space and penetration test IDs. Writing that variable needs a token.

  Create a repository, project, or workspace access token with the Pipelines variable scope, then add it under **Repository settings**, **Repository variables** as a secured variable named `SA_BITBUCKET_TOKEN`, and pass it to the Pipe as `BITBUCKET_ACCESS_TOKEN`.
**Important**  
Without that token the gate still runs and still passes or fails correctly, but it keeps no baseline: every run falls back to the parent of the commit being gated, so it tests a single commit instead of the range you deployed. Nothing fails, which is what makes the omission easy to miss — you get a narrower test than you asked for.

Throughout this tutorial, replace the following placeholders with your own values:


| Placeholder | Replace with | 
| --- | --- | 
|  `111122223333`  | Your 12-digit AWS account ID. | 
|  `AGENT_SPACE_ID` (`as-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`) | Your Agent Space ID. | 
|  `PENTEST_ID` (`pt-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`) | Your CI/CD-enabled penetration test ID. | 
|  `my-workspace/my-app`  | Your Bitbucket workspace and repository. | 
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

## Step 2: Set up Bitbucket OIDC and an IAM role
<a name="_step_2_set_up_bitbucket_oidc_and_an_iam_role"></a>

Bitbucket Pipelines authenticates to AWS with OIDC — no long-lived access keys. Bitbucket acts as a web identity provider: a step with `oidc: true` receives a signed OIDC token in the `$BITBUCKET_STEP_OIDC_TOKEN` variable, which you exchange for temporary AWS credentials.

1. In your repository, go to **Repository settings**, **OpenID Connect** (under **Pipelines**). Copy the **Identity provider URL** and the **Audience**. The provider URL has the form `https://api.bitbucket.org/2.0/workspaces/my-workspace/pipelines-config/identity/oidc`, and the audience is specific to your workspace.

1. Create the IAM OIDC identity provider in your AWS account using the identity provider URL and audience you copied:

   ```
   aws iam create-open-id-connect-provider \
     --url https://api.bitbucket.org/2.0/workspaces/my-workspace/pipelines-config/identity/oidc \
     --client-id-list ari:cloud:bitbucket::workspace/YOUR_WORKSPACE_UUID
   ```

   Use the exact audience value from the **OpenID Connect** settings page as the `--client-id-list` value.

1. Create the IAM role with a trust policy scoped to your repository. Bitbucket includes the repository UUID in the token’s `sub` claim, so scope the role to that UUID rather than to a wildcard. Save the following as `trust-policy.json`, replacing the account ID, the provider host portion, the audience, and the repository UUID:

   ```
   {
     "Version": "2012-10-17",		 	 	 
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": {
           "Federated": "arn:aws:iam::111122223333:oidc-provider/api.bitbucket.org/2.0/workspaces/my-workspace/pipelines-config/identity/oidc"
         },
         "Action": "sts:AssumeRoleWithWebIdentity",
         "Condition": {
           "StringEquals": {
             "api.bitbucket.org/2.0/workspaces/my-workspace/pipelines-config/identity/oidc:aud": "ari:cloud:bitbucket::workspace/YOUR_WORKSPACE_UUID"
           },
           "StringLike": {
             "api.bitbucket.org/2.0/workspaces/my-workspace/pipelines-config/identity/oidc:sub": "{YOUR_REPOSITORY_UUID}:*"
           }
         }
       }
     ]
   }
   ```

   For the reasoning behind scoping the `sub` claim to the repository (and not using a wildcard), see [Scope the trust policy to your pipeline](cicd-pentest.md#cicd-pentest-trust-policy). Confirm the exact `sub` format your workspace emits from the **OpenID Connect** settings page before you write the trust policy.

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

1. Create the role and attach the policy. A penetration test job can run for tens of minutes, so create the role with a maximum session duration long enough to outlast the step:

   ```
   aws iam create-role --role-name my-pentest-gate-role \
     --assume-role-policy-document file://trust-policy.json \
     --max-session-duration 7200
   
   aws iam put-role-policy --role-name my-pentest-gate-role \
     --policy-name securityagent-run-pentest \
     --policy-document file://permissions.json
   ```

   The role ARN for the pipeline is `arn:aws:iam::111122223333:role/my-pentest-gate-role`.

## Step 3: Add the pipeline
<a name="_step_3_add_the_pipeline"></a>

Edit `bitbucket-pipelines.yml`. Run the deploy step, then the gate step. Use a **Pipe** to run the integration, and enable OIDC on the gate step. Store the role ARN as a repository variable named `AWS_PENTEST_ROLE_ARN`, and the baseline token as `SA_BITBUCKET_TOKEN`.

```
image: atlassian/default-image:4

pipelines:
  branches:
    main:
      - step:
          name: Deploy to staging
          deployment: staging
          script:
            - ./deploy.sh staging
      - step:
          name: Security Agent pentest gate
          oidc: true
          script:
            - pipe: docker://public.ecr.aws/aws-continuum/run-pentest:1-bitbucket
              variables:
                AGENT_SPACE_ID: "as-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
                PENTEST_ID: "pt-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
                AWS_REGION: "us-west-2"
                AWS_ROLE_ARN: "$AWS_PENTEST_ROLE_ARN"
                BITBUCKET_ACCESS_TOKEN: "$SA_BITBUCKET_TOKEN"
                SEVERITY_THRESHOLD: "HIGH"
                ON_SCOPE_CONFLICT: "block"
                TIMEOUT_MINUTES: "45"
      - step:
          name: Deploy to production
          deployment: production
          script:
            - ./deploy.sh production
```

The `oidc: true` flag is required: it is what makes Bitbucket issue the OIDC token, and without it authentication to AWS cannot succeed.

Pass **every** value the Pipe reads through `variables:`, including `AWS_ROLE_ARN`. A Pipe runs in its own container, and a variable exported in the step’s `script` does not cross into it, so a role ARN exported in the shell is not reachable by the Pipe at all. The OIDC token is the one exception: Bitbucket places `$BITBUCKET_STEP_OIDC_TOKEN` inside the Pipe’s container directly, so the Pipe reads it there and exchanges it for temporary credentials. You do not need to write the token to a file.

Because Bitbucket Pipelines steps run in sequence and a failed step fails the pipeline, the gate step blocks the production step when it fails.

**Note**  
Pin the Pipe to an immutable image digest (for example, `docker://public.ecr.aws/aws-continuum/run-pentest@sha256:…​`) rather than a tag, so that a change to the upstream image cannot alter what runs in your pipeline without your review. The `1-bitbucket` tag above tracks the latest 1.x release, so it moves as patches are published. See [How the integration differs by provider](cicd-pentest.md#cicd-pentest-choose-provider).

## Step 4: Validate your setup with a dry run
<a name="_step_4_validate_your_setup_with_a_dry_run"></a>

Before you rely on the gate, run it once in dry-run mode. Add the dry-run variable to the Pipe and run the pipeline:

```
            - pipe: docker://public.ecr.aws/aws-continuum/run-pentest:1-bitbucket
              variables:
                AGENT_SPACE_ID: "as-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
                PENTEST_ID: "pt-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
                AWS_REGION: "us-west-2"
                AWS_ROLE_ARN: "$AWS_PENTEST_ROLE_ARN"
                DRY_RUN: "true"
```

The dry run checks AWS authentication, the Region, and that your repository resolves to its integration — without starting a billable penetration test job. It surfaces the common setup mistakes (a bad OIDC trust policy, a Region mismatch, or a repository that is not connected) in seconds. When it passes, remove the dry-run variable and continue. For more information, see [Validate your setup before you trust the gate](cicd-pentest.md#cicd-pentest-validate).

## Step 5: Trigger the gate and read the result
<a name="_step_5_trigger_the_gate_and_read_the_result"></a>

Push a commit to `main` that changes the vulnerable endpoint. This triggers the pipeline: the deploy step deploys the change to staging, then the gate step starts a penetration test scoped to that change.

Open the pipeline and watch the **Security Agent pentest gate** step:

1. Bitbucket issues the OIDC token, and the Pipe exchanges it for AWS credentials with `AssumeRoleWithWebIdentity`. No stored AWS keys are involved.

1. The Pipe resolves your repository, starts a scoped job, polls it to completion, and evaluates the findings against your severity threshold.

A scoped penetration test typically runs for tens of minutes, so the step runs for a while. That is expected, not a hang.

Because the deployed change introduced a SQL injection vulnerability, AWS Security Agent returns an **in scope** decision with a `HIGH` (or higher) finding. The gate step fails, and the pipeline stops before any later promotion step runs.

The step log records the verdict: the scope decision, the severity threshold the run was evaluated against, the finding counts, and whether the gate blocked.

![The Bitbucket step log showing the gate blocked on one finding at or above HIGH](https://docs.aws.amazon.com/securityagent/latest/userguide/images/sample-cicd-bitbucket-blocked.png)


For the full gating behavior — including how authentication failures always block and how you choose fail-closed or fail-open for infrastructure errors — see [Choose how the pipeline responds](cicd-pentest.md#cicd-pentest-gating).

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

Push the fix to `main`. The pipeline redeploys the change and runs the gate again against the new commit. With the injection removed, AWS Security Agent finds no findings at or above `HIGH`, the gate step passes, and the pipeline continues.

The step log shows the same checks for the new commit, with no findings at or above the threshold and a passing verdict.

![The Bitbucket step log showing the gate passed with no findings at or above HIGH](https://docs.aws.amazon.com/securityagent/latest/userguide/images/sample-cicd-bitbucket-passed.png)


## Clean up
<a name="_clean_up"></a>

To avoid ongoing cost and to remove the intentionally vulnerable application:

**Stopping the pipeline does not stop the penetration test**  
If you stop a running pipeline from the Bitbucket UI or API, the penetration test job keeps running server-side and keeps accruing cost. A Pipe has no post-step hook on Bitbucket, so the gate cannot reliably request a stop once the pipeline is being torn down — unlike its own timeout, which it handles itself.  
If you stop a pipeline while the gate is waiting, open the penetration test in the AWS Security Agent console and stop the job there. Check for a running job before you delete the IAM role, because the role is what the cleanup would have used.

1. Tear down the sample application from your staging environment.

1. Remove the gate step from `bitbucket-pipelines.yml`, or disable the pipeline, if you do not intend to keep the gate.

1. Delete the baseline repository variable, which is named `SECURITY_AGENT_BASELINE_` followed by a 40-character identifier, under **Repository settings**, **Repository variables**. Also delete the `SA_BITBUCKET_TOKEN` variable and revoke the token if you created it only for this tutorial.

1. If you created the IAM role and OIDC provider only for this tutorial, delete them:

   ```
   aws iam delete-role-policy --role-name my-pentest-gate-role \
     --policy-name securityagent-run-pentest
   aws iam delete-role --role-name my-pentest-gate-role
   aws iam delete-open-id-connect-provider \
     --open-id-connect-provider-arn arn:aws:iam::111122223333:oidc-provider/api.bitbucket.org/2.0/workspaces/my-workspace/pipelines-config/identity/oidc
   ```

## Related topics
<a name="_related_topics"></a>
+  [Run penetration tests from your CI/CD pipeline](cicd-pentest.md) – concepts and reference for the CI/CD pipeline integration.
+  [Tutorial: Gate a GitHub Actions deployment with a scoped penetration test](sample-cicd-github.md), [Tutorial: Gate a GitLab CI/CD deployment with a scoped penetration test](sample-cicd-gitlab.md), [Tutorial: Gate an Azure DevOps deployment with a scoped penetration test](sample-cicd-azure-devops.md) – the same tutorial for other CI/CD platforms.
+  [Security best practices for AWS Security Agent](security-best-practices.md) – general best practices, including testing against non-production environments.