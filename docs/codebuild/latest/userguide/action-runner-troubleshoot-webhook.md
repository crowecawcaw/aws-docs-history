

# Troubleshoot the webhook
<a name="action-runner-troubleshoot-webhook"></a>

**Issue: **The webhook you set up in [Tutorial: Configure a CodeBuild-hosted GitHub Actions runner](action-runner.md) isn't working or your workflow job is hanging on GitHub.

**Possible causes: **
+ Your webhook **Workflow jobs** event might be failing to trigger a build. Review the **Response** logs to view the response or error message.
+ Your jobs are being assigned to the incorrect runner agent due to their label configuration. This issue can occur when one of your jobs within a single workflow run has fewer labels than another job. For example, if you have two jobs with the following labels in the same workflow run:
  + **Job 1**: `codebuild-myProject-${{ github.run_id }}-${{ github.run_attempt }}`
  + **Job 2**: `codebuild-myProject-${{ github.run_id }}-${{ github.run_attempt }}`, `instance-size:medium`

  When routing a self-hosted GitHub Actions job, GitHub will route the job to any runner with all the job's specified labels. This behavior means that **Job 1** can be picked up by either the runner created for **Job 1** or **Job 2**, but **Job 2** can only be picked up by the runner created for **Job 2** since it has an additional label. If **Job 1** is picked up by the runner created for **Job 2**, then **Job 2** will become stuck since the **Job 1** runner doesn't have the `instance-size:medium` label.

**Recommended solutions: **

When creating multiple jobs within the same workflow run, use the same number of label overrides for each job or assign each job a custom label, such as `job1` or `job2`.

Assigning each job its own unique custom label is the most reliable option. It ensures that no job's set of labels is a subset of another job's. When every job carries a label that no other job has, GitHub matches each job only to the runner created for it, regardless of how many other overrides each job uses. In the following workflow, each job has a unique label (`job1` and `job2`). Although **Job 2** has an extra `instance-size:medium` override, **Job 1** can no longer be matched to the runner created for **Job 2**, so neither job becomes stuck:

```
name: Hello World
on: [push]
jobs:
  job1:
    runs-on:
      - codebuild-myProject-${{ github.run_id }}-${{ github.run_attempt }}
      - job1
    steps:
      - run: echo "Hello from Job 1!"
  job2:
    runs-on:
      - codebuild-myProject-${{ github.run_id }}-${{ github.run_attempt }}
      - instance-size:medium
      - job2
    steps:
      - run: echo "Hello from Job 2!"
```

If the error persists, use the following instructions to debug the issue.

1. Open the GitHub console at `https://github.com/{{user-name}}/{{repository-name}}/settings/hooks` to view your repository's webhook settings. On this page, you'll see a webhook that was created for your repository.

1. Choose **Edit** and confirm that the webhook is enabled to deliver **Workflow jobs** events.  
![Workflow job events are enabled in your webhook.](http://docs.aws.amazon.com/codebuild/latest/userguide/images/github-actions-workflow-jobs.png)

1.  Navigate to the **Recent Deliveries** tab, find the corresponding `workflow_job.queued` event, and expand the event. 

1.  Review the **labels** field in the **Payload** and make sure it's as expected. 

1.  Finally, review the **Response** tab, as this contains the response or error message returned from CodeBuild.   
![The response or error message returned from CodeBuild.](http://docs.aws.amazon.com/codebuild/latest/userguide/images/github-actions-workflow-jobs-response.png)

1.  Alternatively, you can debug webhook failures using GitHub's APIs. You can view recent deliveries for a webhook using the [ List deliveries for a repository webhook](https://docs.github.com/en/rest/repos/webhooks?apiVersion=2022-11-28#list-deliveries-for-a-repository-webhook) API: 

   ```
   gh api \
     -H "Accept: application/vnd.github+json" \
     -H "X-GitHub-Api-Version: 2022-11-28" \
     /repos/{{owner}}/{{repo}}/hooks/{{hook-id}}/deliveries
   ```

    After finding the webhook delivery you're looking to debug and noting the delivery ID, you can use the [ Get a delivery for a repository webhook](https://docs.github.com/en/rest/repos/webhooks?apiVersion=2022-11-28#get-a-delivery-for-a-repository-webhook) API. CodeBuild's response to the webhook's delivery payload can be found in the `response` section: 

   ```
   gh api \
     -H "Accept: application/vnd.github+json" \
     -H "X-GitHub-Api-Version: 2022-11-28" \
     /repos/{{owner}}/{{repo}}/hooks/{{hook-id}}/deliveries/{{delivery-id}}
   ```

**Issue:** Your GitHub Actions with [deployment protection](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/reviewing-deployments) rules enabled triggers builds within CodeBuild before the deployment has been approved.

**Possible causes:** CodeBuild fetches the deployment and environment associated with the GitHub Actions job if they exist to verify if the deployment is approved. If CodeBuild fails to fetch either the deployment or environment, the CodeBuild build may be triggered prematurely.

**Recommended solutions:** Verify that the credentials associated with your CodeBuild projects have read permissions for deployments and actions within GitHub.