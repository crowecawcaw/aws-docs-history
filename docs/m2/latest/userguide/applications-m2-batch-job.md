AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see
[AWS Mainframe Modernization availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Submit batch jobs for AWS Mainframe Modernization applications

In AWS Mainframe Modernization you can submit batch jobs for your applications. You can submit or cancel batch jobs
and review details about batch job executions. Each time that you submit a batch job, AWS Mainframe Modernization
creates a separate batch job execution. You can monitor this job execution. You can search for
batch jobs by name and supply JCL or script files to batch jobs.

###### Important

If you cancel a batch job, this doesn't delete the job. It cancels a particular run
of the batch job. The batch job records remain available for you to view in the details for the
batch job run.

If your batch job requires access to one or more data sets, use the AWS Mainframe Modernization console to
import the data sets. For more information, see [Import data sets for AWS Mainframe Modernization applications](applications-m2-dataset.md "applications-m2-dataset.md").

These instructions assume that you have completed the steps in [Set up for AWS Mainframe Modernization](setting-up.md "setting-up.md") and in [Create an AWS Mainframe Modernization application](applications-m2-create.md "applications-m2-create.md").

###### Topics

- [Submit a batch job](#applications-m2-batch-job-submit.console "#applications-m2-batch-job-submit.console")
- [Restart a batch job](#applications-m2-batch-job-restart.console "#applications-m2-batch-job-restart.console")

## Submit a batch job

###### To submit a batch job

1. Open the AWS Mainframe Modernization console at [https://console.aws.amazon.com/m2/](https://console.aws.amazon.com/m2/ "https://console.aws.amazon.com/m2/").
2. In the AWS Region selector, choose the Region where the application that you want to
   submit a batch job for was created.
3. On the **Applications** page, choose the application that you want to
   submit a batch job for.

###### Note

Before you can submit a batch job to an application, you must deploy the application
successfully. 4. On the application details page, choose **Batch jobs**. 5. Choose **Submit job**. 6. In the **Select a script** section, choose a script. You can search for
the script that you want by name. 7. Choose **Submit job**.

## Restart a batch job

###### To restart a batch job

###### Important

A batch job restart is available on the following engine versions:

- Micro Focus (Rocket) environment engine versions 8.0.6 or greater. You also need to have an
  EFS or FSx file system attached to your environment.
- AWS Blu Age environment engine versions 4.3.0 or greater. You also need to have an EFS or FSx
  file system attached if it is HA environment.

1. Open the AWS Mainframe Modernization console at [https://console.aws.amazon.com/m2/](https://console.aws.amazon.com/m2/ "https://console.aws.amazon.com/m2/").
2. In the AWS Region selector, choose the Region where the application and your batch job was created.
3. On the **Applications** page, choose the application where you want to
   restart a batch job.
4. On the application details page, choose **Batch jobs**.
5. Select the batch job you want to restart from the generated list. Navigate to the **Actions** menu, and choose **Restart job**.
6. Specify how you want to restart the batch job. You can do the following for Micro Focus (Rocket)
   environment engine and AWS Blu Age environment engine:
   - For Micro Focus (Rocket) environment engine, you can either choose to **Restart from
     the beginning** or **Restart using steps or procsteps**.
     - **Restart from the beginning** option allows you to restart all
       steps of a batch job from the beginning.
     - **Restart using steps or procsteps** option allows you to choose a
       specific step or procedure step you want to restart, and optionally a step or procedure
       step you want to end.

###### Note

The end step or procstep must be greater than or equal to the start step or procstep
number.

    * For AWS Blu Age environment engine, you can either restart a batch job's most recent execution
     from a previously failed JCL/PROC step or perform a delayed restart by bypassing previously
     successful steps.




    	+ You can choose a specific **Step name** that you want to
    	 restart.
    	+ Optionally, you can use **Skip step** to bypass the selected step
    	 and restart from the next step in the wokflow.

7. Choose **Submit job**.
