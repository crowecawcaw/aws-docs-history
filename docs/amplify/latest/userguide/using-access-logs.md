# Retrieving and analyzing access logs for an Amplify application

Amplify stores access logs for all of the apps you host in Amplify. Access logs
contain information about requests that are made to your hosted apps. Amplify retains all
access logs for an app until you delete the app. All access logs for an app are available
in the Amplify console. However, each individual request for access logs is limited to a
two week time period that you specify.

###### Warning

Don’t include secrets, credentials, or sensitive data in URLs as path or query
parameters. These values are viewable in plain text in your Amplify application’s
access logs.

Amplify never reuses CloudFront distributions between customers. Amplify creates CloudFront
distributions in advance so that you don't have to wait for a CloudFront distribution to be
created when you deploy a new app. Before these distributions are assigned to an Amplify
app, they might receive traffic from bots. However, they're configured to always respond as
_Not found_ before they're assigned. If your app's access logs
contain entries for a time period before you created your app, these entries are related to
this activity.

###### Important

We recommend that you use the logs to understand the nature of the requests for your
content, not as a complete accounting of all requests. Amplify delivers access logs on
a best-effort basis. The log entry for a particular request might be delivered long
after the request was actually processed and, in rare cases, a log entry might not be
delivered at all. When a log entry is omitted from access logs, the number of entries in
the access logs won't match the usage that appears in the AWS billing and usage
reports.

## Retrieving an app's access logs

Use the following procedure to retrieve access logs for an Amplify app.

###### To view access logs

1. Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/ "https://console.aws.amazon.com/amplify/").
2. Choose the app that you want to view access logs for.
3. In the navigation pane, choose **Monitoring**, then choose
   **Access logs**.
4. Choose **Edit time range**.
5. In the **Edit time range** window do the following.
   1. For **Start date**, specify the first day of the two
      week interval to retrieve logs for.
   2. For **Start time**, choose the time on the first day to
      start the log retrieval.
   3. Choose **Confirm**.

6. The Amplify console displays the logs for your specified time range in the
   **Access logs** section. Choose **Download**
   to save the logs in a CSV format.

## Analyzing access logs

To analyze access logs you can store the CSV files in an Amazon S3 bucket. One way to
analyze your access logs is to use Athena. Athena is an interactive query service that can
help you analyze data for AWS services. You can follow the [step-by-step instructions here](../../../athena/latest/ug/cloudfront-logs.md#create-cloudfront-table "../../../athena/latest/ug/cloudfront-logs.md#create-cloudfront-table") to create a table. Once your table has been
created, you can query data as follows.

```
SELECT SUM(bytes) AS total_bytes
FROM logs
WHERE "date" BETWEEN DATE '2018-06-09' AND DATE '2018-06-11'
LIMIT 100;
```
