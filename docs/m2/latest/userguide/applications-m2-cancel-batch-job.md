AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see
[AWS Mainframe Modernization availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Cancel batch jobs for AWS Mainframe Modernization applications

In AWS Mainframe Modernization you can cancel batch jobs for your applications. You can review details about batch job executions. Each time that you submit a batch job, AWS Mainframe Modernization
creates a separate batch job execution. You can monitor this job execution. You can search for
batch jobs by name and supply JCL or script files to batch jobs.

###### Important

If you cancel a batch job, this doesn't delete the job. It cancels a particular run
of the batch job. The batch job records remain available for you to view in the details for the
batch job run.

## Cancel a batch job

When you cancel a batch job, it does not delete a batch job, but the running of
tasks for that batch job. You can still view details of your batch job.

###### To cancel a batch job

1. Open the AWS Mainframe Modernization console at [https://console.aws.amazon.com/m2/](https://console.aws.amazon.com/m2/ "https://console.aws.amazon.com/m2/").
2. In the AWS Region selector, choose the Region with the application for your batch jobs.
3. From the batch job list find and select the batch job you want to cancel.
4. Choose **Actions**, and choose **Cancel
   job**.
5. Choose **Cancel batch job**.

This will cancel any batch job tasks you had scheduled for running.
