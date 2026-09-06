

**AWS Mainframe Modernization self-managed experience** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization self-managed experience, explore capabilities from vendor-direct offerings and from AWS Transform. Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

# Cancel batch jobs for AWS Mainframe Modernization applications
<a name="applications-m2-cancel-batch-job"></a>

In AWS Mainframe Modernization you can cancel batch jobs for your applications. You can review details about batch job executions. Each time that you submit a batch job, AWS Mainframe Modernization creates a separate batch job execution. You can monitor this job execution. You can search for batch jobs by name and supply JCL or script files to batch jobs.

**Important**  
If you cancel a batch job, this doesn't delete the job. It cancels a particular run of the batch job. The batch job records remain available for you to view in the details for the batch job run.

## Cancel a batch job
<a name="applications-m2-batch-job-cancel.console"></a>

When you cancel a batch job, it does not delete a batch job, but the running of tasks for that batch job. You can still view details of your batch job.

**To cancel a batch job**

1. Open the AWS Mainframe Modernization console at [https://console.aws.amazon.com/m2/](https://console.aws.amazon.com/m2/).

1. In the AWS Region selector, choose the Region with the application for your batch jobs.

1. From the batch job list find and select the batch job you want to cancel.

1. Choose **Actions**, and choose **Cancel job**.

1. Choose **Cancel batch job**.

This will cancel any batch job tasks you had scheduled for running. 