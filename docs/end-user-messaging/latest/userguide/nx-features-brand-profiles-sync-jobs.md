

# Track brand profile jobs
<a name="nx-features-brand-profiles-sync-jobs"></a>

The registration sync operations run asynchronously and each returns a job ID. Track a job to see whether it is `PROCESSING`, `SUCCESS`, or `FAILED`, along with the resources it created or updated and any error details. List jobs to see all jobs for a brand profile.

------
#### [ AWS Management Console ]

**To track a brand profile job using the console**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. Open the brand profile detail page and choose the **Jobs** tab.

1. The **Jobs** table lists each job with its operation type, status, and creation time. Choose a job to see the resources it affected and any error details.

------
#### [ AWS CLI ]

**To track a brand profile job using the AWS CLI**

1. At the command line, enter the following command:

   ```
   $ aws endusermessaging get-job \
   > --job-id {{job-abc123}}
   ```

   Replace {{job-abc123}} with the job ID returned by a sync operation. The response includes the `status` (`PROCESSING`, `SUCCESS`, or `FAILED`), the affected resources, and any error code and message.

1. To list all jobs for a brand profile, use the following command:

   ```
   $ aws endusermessaging list-jobs \
   > --brand-profile-id {{bp-gkma20fagojtpys0e}}
   ```

   You can filter with **--status** and **--operation-type**.

------