# Notifications

AWS Transform provides email notifications to keep you informed about workspace access changes, job status updates, and pending collaborator requests.

## Email notifications

Email notifications are enabled by default, and are sent to users who have read-only
or higher permissions on a job. Users can modify their notification preferences. There
are three categories of email notifications:

- **Workspace access updates**

You receive a notification when you are added to a new workspace, and when your role is changed within a workspace.

- **Daily digest emails**

You receive a daily digest email at 9:00 AM Pacific time summarizing your ongoing jobs if you have active jobs with one or more open required collaborator requests. The email
includes a table showing workspace name, job name, job status, collaborator request details, and required actions (limited to 10 rows)

###### Note

Daily digest emails are only sent for jobs that have required collaborator requests. Optional collaborator requests do not trigger digest emails.

- **Job status updates**

You receive an email when a job you have access to completes or fails.

### Managing email notifications

You can modify your email notification preferences in the web application by clicking the **Settings** cog in the top right corner of the application, and choosing **Notification settings**.

The notification settings page provides the following controls:

| Notification Type                 | Description                                                                               | Default Setting |
| --------------------------------- | ----------------------------------------------------------------------------------------- | --------------- |
| Workspace Access Updates          | Receive emails when added to a workspace, or when your role is changed within a workspace | Enabled         |
| Daily Collaborator Request Digest | Receive a daily digest of open collaborator requests for jobs in accessible workspaces    | Enabled         |
| Job Completion Updates            | Receive emails when a job is completed or fails                                           | Enabled         |

You can use a general setting to enable or disable all notifications, or configure individual notification types separately.
