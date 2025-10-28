# Amazon Q Apps Analytics dashboard

metrics

The Amazon Q Apps dashboard provides a comprehensive view of key metrics to help admins
understand the performance and usage of Q Apps.

If the metrics are not populated in the dashboard, it is likely due to the absence of a
Q Apps service role or the role is not configured properly in the Amazon Q Business application environment.
Usually a banner will be displayed on the Amazon Q Business console to prompt creating and registering
the Q Apps service role.

Depending on how you set up the Amazon Q Business application environment prior to the introduction of
analytics dashboard feature, the banner might not always appear. To resolve the issue, go to
the **Admin controls and guardrails** page for the Amazon Q Business application environment,
choose **Edit Global Control** and re-save the configuration without changes.
The metrics should start populating in 10 minutes.

The following analytics are available in the Amazon Q Apps Analytics dashboard for the
specified time period.

- **Active users**

The average unique daily users creating, updating, or running Q Apps.

- **Active creators**

The average unique daily users creating or updating Q Apps.

- **Total Q Apps**

The average of the total Q Apps per day.

- **Active Q Apps**

The average number of daily Q Apps ran or updated.

- **Q App Participants trend**

A trend of the daily active users and the daily active creators.

- **Q App trend**

A trend of the total daily Q Apps created and the daily active Q Apps.

- **Total Q Apps Runs trend**

A trend of the total daily Q App runs.

- **Published Q App trend**

A trend of the total daily published Q Apps.
