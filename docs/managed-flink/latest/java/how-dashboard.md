Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Use the Apache Flink Dashboard with Managed Service for Apache Flink

You can use your application's Apache Flink Dashboard to monitor your Managed Service for Apache Flink application's health.
Your application's dashboard shows the following information:

- Resources in use, including Task Managers and Task Slots.
- Information about Jobs, including those that are running, completed, canceled, and failed.
  For information about Apache Flink Task Managers, Task Slots, and Jobs, see [Apache Flink Architecture](https://flink.apache.org/what-is-flink/flink-architecture/ "https://flink.apache.org/what-is-flink/flink-architecture/") on the Apache Flink website.

Note the following about using the Apache Flink Dashboard with Managed Service for Apache Flink applications:

- The Apache Flink Dashboard for Managed Service for Apache Flink applications is read-only. You can't make changes to your Managed Service for Apache Flink application using the
  Apache Flink Dashboard.
- The Apache Flink Dashboard is not compatible with Microsoft Internet Explorer.

## Access your application's Apache Flink Dashboard

You can access your application's Apache Flink Dashboard either through the Managed Service for Apache Flink
console, or by requesting a secure URL endpoint using the CLI.

### Access your application's Apache Flink Dashboard

using the Managed Service for Apache Flink console

To access your application's Apache Flink Dashboard from the console, choose
**Apache Flink Dashboard** on your application's page.

###### Note

When you open the dashboard from the Managed Service for Apache Flink console, the URL that the console generates will be
valid for 12 hours.

### Access your application's Apache Flink Dashboard using

the Managed Service for Apache Flink CLI

You can use the Managed Service for Apache Flink CLI to generate a URL to access your application dashboard. The URL that you generate is valid for a specified
amount of time.

###### Note

If you don't access the generated URL within three minutes, it will no longer be
valid.

You generate your dashboard URL using the [CreateApplicationPresignedUrl](../apiv2/API_CreateApplicationPresignedUrl.md "../apiv2/API_CreateApplicationPresignedUrl.md") action. You specify the following parameters for the action:

- The application name
- The time in seconds that the URL will be valid
- You specify `FLINK_DASHBOARD_URL` as the URL type.
