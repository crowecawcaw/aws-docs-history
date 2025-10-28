# Viewing logs for AWS Glue jobs

You can view real-time logs using the AWS Glue console or the Amazon CloudWatch console.

###### To view real-time logs using the AWS Glue console dashboard

1. Sign in to the AWS Management Console and open the AWS Glue console at
   [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/ "https://console.aws.amazon.com/glue/").
2. In the navigation pane, choose **Jobs**.
3. Add or start an existing job. Choose **Action**, **Run
   job**.

When you start running a job, you navigate to a page that contains information about the
running job:

    * The **Logs** tab shows the older aggregated application
     logs.
    * The **Logs** tab shows a real-time progress bar when
     the job is running with `glueContext` initialized.
    * The **Logs** tab also contains the **Driver
     logs**, which capture real-time Apache Spark driver logs, and application
     logs from the script logged using the AWS Glue application logger when the job is
     running.

4. For older jobs, you can also view the real-time logs under the **Job
   History** view by choosing **Logs**. This action takes you to
   the CloudWatch console that shows all Spark driver, executor, and progress bar log streams for
   that job run.

###### To view real-time logs using the CloudWatch console dashboard

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Log**.
3. Choose the **/aws-glue/jobs/error/** log group.
4. In the **Filter** box, paste the job run ID.

You can view the driver logs, executor logs, and progress bar (if using the
**Standard filter**).
