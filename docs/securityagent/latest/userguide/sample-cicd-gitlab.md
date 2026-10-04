

# Tutorial: Gate a GitLab CI/CD deployment with a scoped penetration test
<a name="sample-cicd-gitlab"></a>

**Public preview**  
CI/CD pipeline integration is in preview and is subject to change.

This tutorial walks through a complete, reproducible setup that runs a continuous, scoped AWS Security Agent penetration test as a **post-deployment gate** in GitLab CI/CD. You deploy an intentionally vulnerable sample application to a pre-production environment, then let AWS Security Agent test the deployed change and block promotion to production when it finds a vulnerability.

**Note**  
Running a penetration test job and hosting the sample application might result in charges to your AWS account. For pricing details, see [AWS Security Agent pricing](https://aws.amazon.com/continuum/pricing/).

For the concepts behind the integration — how the test is scoped to the deployed change, how OIDC authentication works, and how gating decisions are made — see [Run penetration tests from your CI/CD pipeline](cicd-pentest.md). This tutorial applies those concepts to a concrete GitLab project.

**Intentional vulnerability**  
The sample application in this tutorial contains a deliberate SQL injection vulnerability so that the gate has a real finding to block on. Deploy it only to an isolated, non-production environment that you control, and remove it when you finish. Do not expose it to the public internet or connect it to production data.

## Prerequisites
<a name="_prerequisites"></a>

Before you start, make sure you have the following:
+ An AWS account, and permission in it to create an IAM OIDC identity provider, an IAM role, and AWS Security Agent resources.
+ A GitLab project that you own, on `gitlab.com`, in which you can edit `.gitlab-ci.yml` and set CI/CD variables. This tutorial uses the placeholder project `my-group/my-app`; substitute your own group and project throughout.
+ A GitLab access token (a Project or Group Access Token, or a personal access token) with the `read_api` and `write_repository` scopes and at least the Developer role. The integration uses it to maintain the diff baseline tag in your project.
+ A pre-production environment that the sample application can deploy to, reachable from the network where your penetration test runs (the public internet, or a VPC in your AWS account for a private target). See [Connect agent to private VPC resources](connect-agent-vpc.md) for private targets.
+ The AWS Security Agent one-time setup described in [Run penetration tests from your CI/CD pipeline](cicd-pentest.md) under **Before you start**: a verified target domain, a CI/CD-enabled penetration test, your GitLab project connected as a source control integration, and the Agent Space ID (`as-…​`) and penetration test ID (`pt-…​`) that identify them.
+ A project **maximum job timeout** higher than the gate job’s own timeout. The gate needs a long-running job, and GitLab’s runner enforces whichever limit is lower. This tutorial’s gate job runs for up to 55 minutes, so raise the project maximum above that under **Settings**, **CI/CD**, **General pipelines** before your first run.

**A pipeline variable can override the gate’s settings**  
On GitLab a pipeline variable takes precedence over the values a job sets itself, and the component’s settings are passed that way. If you can run a pipeline, you can therefore supply a variable that lowers the severity threshold, turns on dry-run mode, or relaxes error handling, and the gate will honor it over your `.gitlab-ci.yml`.  
Before you rely on this gate to hold a release, restrict who may override variables: under **Settings**, **CI/CD**, **Variables**, set the minimum role required to override variables on a pipeline. See [On GitLab, the committed settings are not the gate’s contract](cicd-pentest.md#cicd-pentest-gitlab-variable-override).

Throughout this tutorial, replace the following placeholders with your own values:


| Placeholder | Replace with | 
| --- | --- | 
|  `111122223333`  | Your 12-digit AWS account ID. | 
|  `AGENT_SPACE_ID` (`as-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`) | Your Agent Space ID. | 
|  `PENTEST_ID` (`pt-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`) | Your CI/CD-enabled penetration test ID. | 
|  `my-group/my-app`  | Your GitLab group and project path. | 
|  `us-west-2`  | The AWS Region where your Agent Space and penetration test are located. | 

## Step 1: Create the vulnerable sample application
<a name="_step_1_create_the_vulnerable_sample_application"></a>

Create a small Flask application with one endpoint that builds a SQL query by string concatenation — a classic SQL injection. In your project, add `app.py`:

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

Add a `deploy.sh` script that deploys this application to your pre-production environment. The details depend on your infrastructure; the gate does not require any particular deployment mechanism, only that the application is running and reachable when the test runs.

## Step 2: Set up GitLab OIDC and an IAM role
<a name="_step_2_set_up_gitlab_oidc_and_an_iam_role"></a>

The component authenticates to AWS with GitLab OIDC ID tokens — no long-lived access keys. Do this once in your AWS account.

1. If you do not already have one, create the GitLab OIDC identity provider. The client ID is the audience (`aud`) that the component sets on the ID token, which defaults to `https://gitlab.com`:

   ```
   aws iam create-open-id-connect-provider \
     --url https://gitlab.com \
     --client-id-list https://gitlab.com
   ```

1. Create the IAM role with a trust policy scoped to your project. Save the following as `trust-policy.json`, replacing the account ID and project path:

   ```
   {
     "Version": "2012-10-17",		 	 	 
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": {
           "Federated": "arn:aws:iam::111122223333:oidc-provider/gitlab.com"
         },
         "Action": "sts:AssumeRoleWithWebIdentity",
         "Condition": {
           "StringEquals": {
             "gitlab.com:aud": "https://gitlab.com"
           },
           "StringLike": {
             "gitlab.com:sub": "project_path:my-group/my-app:ref_type:branch:ref:main"
           }
         }
       }
     ]
   }
   ```

   The GitLab OIDC `sub` claim has the form `project_path:GROUP/PROJECT:ref_type:branch:ref:BRANCH`. Keep it as specific as your workflow allows. For the reasoning behind scoping the `sub` claim, see [Scope the trust policy to your pipeline](cicd-pentest.md#cicd-pentest-trust-policy).

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

1. Create the role and attach the policy. The component asks AWS STS for a credential lifetime derived from the gate timeout, so the role’s maximum session duration has to cover it. Size it as `(timeout-minutes + 10) * 60` seconds — the extra ten minutes cover findings collection and cleanup. IAM’s own minimum for a role’s maximum session duration is 3,600 seconds, so that formula asks for more than IAM’s floor only once your timeout passes 50 minutes. This tutorial’s `timeout-minutes: "45"` is already covered by 3,600; the example sets 4,200 so that raising the timeout to the 60-minute default needs no change to the role:

   ```
   aws iam create-role --role-name my-pentest-gate-role \
     --assume-role-policy-document file://trust-policy.json \
     --max-session-duration 4200
   
   aws iam put-role-policy --role-name my-pentest-gate-role \
     --policy-name securityagent-run-pentest \
     --policy-document file://permissions.json
   ```
**Important**  
AWS STS **rejects** a request for a longer session than the role allows rather than shortening it, so a role whose maximum is too low fails the credential exchange outright — before any penetration test starts. Recompute the maximum whenever you change `timeout-minutes`.  
This is also why you cannot reuse a role built for GitHub Actions here without checking it. A role left at IAM’s 3,600-second default works on GitHub, because `configure-aws-credentials` asks for less, but it fails on GitLab as soon as the timeout needs more.

   The role ARN for the component is `arn:aws:iam::111122223333:role/my-pentest-gate-role`.

## Step 3: Store the GitLab access token
<a name="_step_3_store_the_gitlab_access_token"></a>

The component keeps the baseline — the record of the commit it last cleared — as a tag in your project, and it needs a token to read and write one. `CI_JOB_TOKEN` cannot create tags or read a merge base, so it is not sufficient.

Create a Project or Group Access Token (or a personal access token) with the `read_api` and `write_repository` scopes and the **Developer** role. In your project, go to **Settings**, **CI/CD**, **Variables** and add it as a masked variable named `SA_GITLAB_TOKEN`.

Keep the `continuum/pentest/cicd/baseline/*` tag namespace unprotected, which is the default, so that the Developer-role token can create the baseline tags. If you protect that namespace, add the token’s identity to its \*Allowed to create\* list instead.

**Important**  
Without the token the gate still runs, but it has no persistent baseline: each run falls back to the parent of the commit being gated, so it tests one commit rather than the range you deployed. That is a narrower test than you asked for, not a wider one.

## Step 4: Add the component to your pipeline
<a name="_step_4_add_the_component_to_your_pipeline"></a>

Edit `.gitlab-ci.yml`. Place the gate in a stage **after** your deploy stage, and gate the production job on it with `needs`. Because a failed job fails the pipeline, the production job does not run when the gate fails.

```
stages: [build, deploy-preprod, security-gate, deploy-prod]

# The baseline is a tag in your own project, and creating a tag starts a
# pipeline, so without this rule the gate re-triggers itself on every pass —
# and each passing run writes another tag. Exclude the baseline namespace.
workflow:
  rules:
    - if: '$CI_COMMIT_TAG =~ /^continuum\/pentest\/cicd\/baseline\//'
      when: never
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
      when: never
    - if: '$CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH'

include:
  - component: $CI_SERVER_FQDN/aws/continuum/pentest/run-pentest@1
    inputs:
      agent-space-id: "as-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
      pentest-id: "pt-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
      stage: security-gate
      aws-role-arn: "arn:aws:iam::111122223333:role/my-pentest-gate-role"
      aws-region: "us-west-2"
      gitlab-token: "$SA_GITLAB_TOKEN"
      severity-threshold: "HIGH"
      on-scope-conflict: "block"
      timeout-minutes: "45"
      job-timeout: "55 minutes"

deploy-preprod:
  stage: deploy-preprod
  environment: preprod
  script: ./deploy.sh preprod

deploy-prod:
  stage: deploy-prod
  needs: ["aws-continuum-pentest"]
  when: manual
  environment: production
  script: ./deploy.sh prod
```

The component defines a job named `aws-continuum-pentest`. The `stage` input must name a stage that runs after your deploy stage, and the `deploy-prod` job’s `needs` must reference that job name so that promotion is gated on the result.

**Exclude the baseline tag namespace, or the gate re-triggers itself**  
Each time the gate passes it creates a tag under `continuum/pentest/cicd/baseline/`, and on GitLab creating a tag is a pipeline trigger. If any job in your pipeline is tag-driven — the common `rules: if: $CI_COMMIT_TAG` idiom, `only: tags`, or release automation — the gate fires again on its own tag, passes, writes another tag, and repeats. Each of those runs is a billable penetration test.  
The `workflow: rules` block above prevents that for the whole pipeline. If you cannot use a `workflow` rule, exclude the namespace on each tag-driven job instead, with `rules: if: '$CI_COMMIT_TAG !~ /^continuum\/pentest\/cicd\/baseline\//'`.

**Note**  
Pin the component to a released version rather than a moving reference, so that a change to the upstream component cannot alter what runs in your pipeline without your review. `@1` tracks the latest 1.x release; pin the exact version, such as `@v1.0.4`, to hold it still. Note that GitLab looks up an exact version as a literal ref, so the `v` prefix is required for one — `@1.0.4` resolves to nothing, while `@v1.0.4`, `@1`, and `@1.0` all resolve. See [How the integration differs by provider](cicd-pentest.md#cicd-pentest-choose-provider).

## Step 5: Validate your setup with a dry run
<a name="_step_5_validate_your_setup_with_a_dry_run"></a>

Before you rely on the gate, run it once in dry-run mode. Add `dry-run: "true"` to the component inputs and run the pipeline:

```
  - component: $CI_SERVER_FQDN/aws/continuum/pentest/run-pentest@1
    inputs:
      agent-space-id: "as-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
      pentest-id: "pt-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
      stage: security-gate
      aws-role-arn: "arn:aws:iam::111122223333:role/my-pentest-gate-role"
      aws-region: "us-west-2"
      dry-run: "true"
```

The dry run checks AWS authentication, the Region, and that your project resolves to its integration — without starting a billable penetration test job. It surfaces the common setup mistakes (a bad OIDC trust policy, a Region mismatch, or a project that is not connected) in seconds. When it passes, remove the `dry-run` input and continue. For more information, see [Validate your setup before you trust the gate](cicd-pentest.md#cicd-pentest-validate).

## Step 6: Trigger the gate and read the result
<a name="_step_6_trigger_the_gate_and_read_the_result"></a>

Push a commit to your deploy branch that changes the vulnerable endpoint. This triggers the deploy pipeline: the `deploy-preprod` job deploys the change, then the `aws-continuum-pentest` job starts a penetration test scoped to that change.

Open the pipeline and watch the `aws-continuum-pentest` job:

1. In `before_script`, GitLab mints an ID token and the job exchanges it for AWS credentials with `AssumeRoleWithWebIdentity`. No stored AWS keys are involved.

1. In `script`, the component resolves your project, starts a scoped job, polls it to completion, evaluates findings against your `severity-threshold`, and exits non-zero to fail the pipeline if the gate blocks.

A scoped penetration test typically runs for tens of minutes, so the job runs for a while. That is expected, not a hang.

Because the deployed change introduced a SQL injection vulnerability, AWS Security Agent returns an **in scope** decision with a `HIGH` (or higher) finding. The `aws-continuum-pentest` job fails, and because `deploy-prod` needs it, promotion to production is blocked.

The job log records the verdict: the scope decision, the severity threshold the run was evaluated against, the finding counts, and whether the gate blocked.

![The GitLab job log showing the gate blocked on one finding at or above HIGH](https://docs.aws.amazon.com/securityagent/latest/userguide/images/sample-cicd-gitlab-blocked.png)


The job writes its outputs as a dotenv report artifact that downstream jobs can read as variables, including `SCOPE_DECISION` (`IN_SCOPE`, `SCOPED_OUT`, or `SCOPE_CONFLICT`), `FINDINGS_COUNT`, and `STATUS`. If you set `sast-report: "true"`, the job also emits `gl-sast-report.json` so the findings appear in the merge request security widget. For the full gating behavior, see [Choose how the pipeline responds](cicd-pentest.md#cicd-pentest-gating).

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

Push the fix to your deploy branch. The pipeline redeploys the change and runs the gate again against the new commit. With the injection removed, AWS Security Agent finds no findings at or above `HIGH`, the gate job passes, and the manual `deploy-prod` job becomes available to promote.

The job log shows the same checks for the new commit, with no findings at or above the threshold and a passing verdict.

![The GitLab job log showing the gate passed with no findings at or above HIGH](https://docs.aws.amazon.com/securityagent/latest/userguide/images/sample-cicd-gitlab-passed.png)


## Clean up
<a name="_clean_up"></a>

To avoid ongoing cost and to remove the intentionally vulnerable application:

1. Tear down the sample application from your pre-production environment.

1. Remove the component include from `.gitlab-ci.yml`, or disable the pipeline, if you do not intend to keep the gate.

1. Delete the `SA_GITLAB_TOKEN` CI/CD variable if it was created only for this tutorial.

1. If you created the IAM role and OIDC provider only for this tutorial, delete them:

   ```
   aws iam delete-role-policy --role-name my-pentest-gate-role \
     --policy-name securityagent-run-pentest
   aws iam delete-role --role-name my-pentest-gate-role
   aws iam delete-open-id-connect-provider \
     --open-id-connect-provider-arn arn:aws:iam::111122223333:oidc-provider/gitlab.com
   ```

## Related topics
<a name="_related_topics"></a>
+  [Run penetration tests from your CI/CD pipeline](cicd-pentest.md) – concepts and reference for the CI/CD pipeline integration.
+  [Tutorial: Gate a GitHub Actions deployment with a scoped penetration test](sample-cicd-github.md), [Tutorial: Gate a Bitbucket Pipelines deployment with a scoped penetration test](sample-cicd-bitbucket.md), [Tutorial: Gate an Azure DevOps deployment with a scoped penetration test](sample-cicd-azure-devops.md) – the same tutorial for other CI/CD platforms.
+  [Security best practices for AWS Security Agent](security-best-practices.md) – general best practices, including testing against non-production environments.