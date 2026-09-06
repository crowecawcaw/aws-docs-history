

**AWS Mainframe Modernization self-managed experience** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization self-managed experience, explore capabilities from vendor-direct offerings and from AWS Transform. Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

# Submit batch jobs for AWS Mainframe Modernization applications
<a name="applications-m2-batch-job"></a>

In AWS Mainframe Modernization you can submit batch jobs for your applications. You can submit or cancel batch jobs and review details about batch job executions. Each time that you submit a batch job, AWS Mainframe Modernization creates a separate batch job execution. You can monitor this job execution. You can search for batch jobs by name and supply JCL or script files to batch jobs.

**Important**  
If you cancel a batch job, this doesn't delete the job. It cancels a particular run of the batch job. The batch job records remain available for you to view in the details for the batch job run.

If your batch job requires access to one or more data sets, use the AWS Mainframe Modernization console to import the data sets. For more information, see [Import data sets for AWS Mainframe Modernization applications](applications-m2-dataset.md).

These instructions assume that you have completed the steps in [Set up for AWS Mainframe Modernization](setting-up.md) and in [Create an AWS Mainframe Modernization application](applications-m2-create.md).

**Topics**
+ [Submit a batch job](#applications-m2-batch-job-submit.console)
+ [Restart a batch job](#applications-m2-batch-job-restart.console)

## Submit a batch job
<a name="applications-m2-batch-job-submit.console"></a>

**To submit a batch job**

1. Open the AWS Mainframe Modernization console at [https://console.aws.amazon.com/m2/](https://console.aws.amazon.com/m2/).

1. In the AWS Region selector, choose the Region where the application that you want to submit a batch job for was created.

1. On the **Applications** page, choose the application that you want to submit a batch job for.
**Note**  
Before you can submit a batch job to an application, you must deploy the application successfully.

1. On the application details page, choose **Batch jobs**.

1. Choose **Submit job**.

1. In the **Select a script** section, choose a script. You can search for the script that you want by name.

1. Choose **Submit job**.

## Restart a batch job
<a name="applications-m2-batch-job-restart.console"></a>

**To restart a batch job**
**Important**  
A batch job restart is available on the following engine versions:  
Micro Focus (Rocket) environment engine versions 8.0.6 or greater. You also need to have an EFS or FSx file system attached to your environment.
AWS Transform for mainframe environment engine versions 4.3.0 or greater. You also need to have an EFS or FSx file system attached if it is HA environment.

1. Open the AWS Mainframe Modernization console at [https://console.aws.amazon.com/m2/](https://console.aws.amazon.com/m2/).

1. In the AWS Region selector, choose the Region where the application and your batch job was created.

1. On the **Applications** page, choose the application where you want to restart a batch job.

1. On the application details page, choose **Batch jobs**.

1. Select the batch job you want to restart from the generated list. Navigate to the **Actions** menu, and choose **Restart job**.

1. Specify how you want to restart the batch job. You can do the following for Micro Focus (Rocket) environment engine and AWS Transform for mainframe environment engine:
   + For Micro Focus (Rocket) environment engine, you can either choose to **Restart from the beginning** or **Restart using steps or procsteps**.
     + **Restart from the beginning** option allows you to restart all steps of a batch job from the beginning.
     + **Restart using steps or procsteps** option allows you to choose a specific step or procedure step you want to restart, and optionally a step or procedure step you want to end.
**Note**  
The end step or procstep must be greater than or equal to the start step or procstep number.
   + For AWS Transform for mainframe environment engine, you can either restart a batch job's most recent execution from a previously failed JCL/PROC step or perform a delayed restart by bypassing previously successful steps.
     + You can choose a specific **Step name** that you want to restart.
     + Optionally, you can use **Skip step** to bypass the selected step and restart from the next step in the wokflow.

1. Choose **Submit job**.