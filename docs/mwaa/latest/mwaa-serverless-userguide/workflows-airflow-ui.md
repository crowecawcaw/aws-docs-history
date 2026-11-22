

# Access the Airflow UI

Amazon MWAA Serverless provides the native Apache Airflow UI for your workflows. Use it to browse your workflows, inspect workflow runs and task instances, read task logs, view a workflow's source and versions, and start a workflow run. You don't run or manage a web server. Amazon MWAA Serverless hosts the UI and opens it in a new browser tab.

The UI runs with the permissions of the IAM identity that opens it. It shows only the workflows, runs, and logs that the identity can read, and it starts a run only if the identity is allowed to start one. You don't pass a role to the UI.

**Topics**
+ [Prerequisites](#workflows-airflow-ui-prereqs)
+ [Open the Airflow UI](#workflows-airflow-ui-open)
+ [Sessions](#workflows-airflow-ui-sessions)
+ [Limitations](#workflows-airflow-ui-limitations)

## Prerequisites
<a name="workflows-airflow-ui-prereqs"></a>
+ **A workflow.** The UI shows the Amazon MWAA Serverless workflows in your account in the current AWS Region. For instructions, refer to [Manage your Amazon MWAA Serverless workflows](workflows.md#workflows-manage).
+ **Permission to create the UI URL.** The IAM identity that opens the UI must be allowed `airflow-serverless:CreateAirflowUiUrl`.
+ **A browser that accepts cookies.** The UI keeps your session in a cookie on the UI's domain.
+ **Permissions for what you do in the UI.** What you can see and do in the UI depends on the IAM permissions of the identity that opens it. The following table lists the actions needed for each task in the UI. For example, an identity without `airflow-serverless:StartWorkflowRun` can view workflows but can't start a run.



| To do this in the UI | Allow these actions | 
| --- | --- | 
| List and view workflows | airflow-serverless:ListWorkflows, airflow-serverless:GetWorkflow | 
| View workflow versions | airflow-serverless:ListWorkflowVersions | 
| View workflow runs | airflow-serverless:ListWorkflowRuns, airflow-serverless:GetWorkflowRun | 
| View task instances | airflow-serverless:ListTaskInstances, airflow-serverless:GetTaskInstance | 
| Start a workflow run | airflow-serverless:StartWorkflowRun | 
| Read task logs | logs:FilterLogEvents on the workflow's CloudWatch Logs log group. If the log group is encrypted with a customer managed KMS key, the key policy must also allow the identity to use the key. | 

The following example JSON policy grants read access to all workflows in the account and lets the identity start runs. `CreateAirflowUiUrl` and `ListWorkflows` don't act on a specific workflow, so they use `"Resource": "*"`. The other actions are scoped to the account's workflows. Replace the Region, account ID, and log group with your own.

```json
{
  "Version": "2012-10-17", 		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "airflow-serverless:CreateAirflowUiUrl",
        "airflow-serverless:ListWorkflows"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "airflow-serverless:GetWorkflow",
        "airflow-serverless:ListWorkflowVersions",
        "airflow-serverless:ListWorkflowRuns",
        "airflow-serverless:GetWorkflowRun",
        "airflow-serverless:ListTaskInstances",
        "airflow-serverless:GetTaskInstance",
        "airflow-serverless:StartWorkflowRun"
      ],
      "Resource": "arn:aws:airflow-serverless:{{us-east-1}}:{{111122223333}}:workflow/*"
    },
    {
      "Effect": "Allow",
      "Action": "logs:FilterLogEvents",
      "Resource": "arn:aws:logs:{{us-east-1}}:{{111122223333}}:log-group:{{my-workflow-log-group}}:*"
    }
  ]
}
```

To give an identity read-only access to the UI, omit `airflow-serverless:StartWorkflowRun`.

## Open the Airflow UI
<a name="workflows-airflow-ui-open"></a>

You can open the UI from the console, or create a launch URL with the AWS CLI or the API and open it in a browser.

------
#### [ Console ]

1. Open the [Amazon MWAA console](https://console.aws.amazon.com/mwaa/).

1. In the navigation pane, choose **Serverless workflows**.

1. On the **Serverless workflows** page, choose **Open Airflow UI**. The UI opens in a new browser tab.

------
#### [ CLI ]

Run `create-airflow-ui-url`, then open the `AuthorizedUrl` from the output in a browser before `UrlExpiresAt`.

```bash
aws mwaa-serverless create-airflow-ui-url --region {{us-east-1}}
```

Example output:

```json
{
    "AuthorizedUrl": "https://a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4.airflowserverless.us-east-1.on.aws/launch?token=...",
    "SessionId": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
    "UrlExpiresAt": "2026-11-02T18:05:00+00:00",
    "SessionExpiresAt": "2026-11-03T06:00:00+00:00"
}
```

You can set two optional parameters:
+ `--expires-in-seconds`: how long the launch URL stays valid, from 5 to 300 seconds. The default is 300.
+ `--session-duration-in-seconds`: how long the UI session lasts, from 1 to 43,200 seconds (12 hours). The default is 43,200.

```bash
aws mwaa-serverless create-airflow-ui-url --expires-in-seconds 60 --session-duration-in-seconds 3600 --region {{us-east-1}}
```

------
#### [ API ]

Call `CreateAirflowUiUrl`, then open the `AuthorizedUrl` from the response in a browser before `UrlExpiresAt`. Both request fields are optional:
+ `ExpiresInSeconds`: how long the launch URL stays valid, from 5 to 300 seconds. The default is 300.
+ `SessionDurationInSeconds`: how long the UI session lasts, from 1 to 43,200 seconds (12 hours). The default is 43,200.

The following example calls `CreateAirflowUiUrl` with curl, which signs the request with Signature Version 4 using the credentials in your environment. The `--aws-sigv4` option requires curl 7.75.0 or later. If you use long-term credentials, omit the `x-amz-security-token` header.

```bash
curl --aws-sigv4 "aws:amz:{{us-east-1}}:airflow-serverless" \
  --user "$AWS_ACCESS_KEY_ID:$AWS_SECRET_ACCESS_KEY" \
  -H "x-amz-security-token: $AWS_SESSION_TOKEN" \
  -H "Content-Type: application/x-amz-json-1.0" \
  -H "X-Amz-Target: AmazonMWAAServerless.CreateAirflowUiUrl" \
  -d '{"ExpiresInSeconds": 60, "SessionDurationInSeconds": 3600}' \
  https://airflow-serverless.{{us-east-1}}.api.aws/
```

Example response:

```json
{
    "AuthorizedUrl": "https://a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4.airflowserverless.us-east-1.on.aws/launch?token=...",
    "SessionId": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
    "UrlExpiresAt": "2026-11-02T18:01:00Z",
    "SessionExpiresAt": "2026-11-02T19:00:00Z"
}
```

For more information, refer to the [Amazon MWAA Serverless API Reference](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_CreateAirflowUiUrl.html).

------

## Sessions
<a name="workflows-airflow-ui-sessions"></a>

When you open the launch URL, Amazon MWAA Serverless starts a UI session for you in that browser.
+ **The launch URL works once.** The first browser that opens it starts the session, and the URL can't be used again. Treat the URL like a password until it is used or expires. The first person to open it gets a session with your permissions. Don't share it. To open the UI again, create a new URL.
+ **The session lasts up to 12 hours.** By default, the session ends 12 hours after you create the URL. To end it sooner, set `--session-duration-in-seconds`. `SessionExpiresAt` in the output shows when the session ends. After that, create a new URL.
+ **The session is tied to your network address.** The session works only from the IP address that opened the launch URL.
+ **Sign out** from the user menu in the UI to end the session early.

AWS CloudTrail records each launch URL as a `CreateAirflowUiUrl` event. It records the calls that the UI makes on your behalf, such as `ListWorkflowRuns` or `StartWorkflowRun`, under your identity.

## Limitations
<a name="workflows-airflow-ui-limitations"></a>
+ **Workflow and run changes.** You can't pause or unpause a workflow, or stop, clear, or mark the state of a run or task instance from the UI. To change a workflow's schedule, use `UpdateWorkflow`. To stop a run, use `StopWorkflowRun`.
+ **Admin features.** Connections, variables, pools, providers, configuration, plugins, backfills, assets, and the audit log aren't available.
+ **Access through a VPC endpoint (AWS PrivateLink).** The UI is served over public HTTPS and isn't reachable through a VPC endpoint, so the browser that opens the launch URL needs internet access. You can still call `CreateAirflowUiUrl` through an Amazon MWAA Serverless interface VPC endpoint.