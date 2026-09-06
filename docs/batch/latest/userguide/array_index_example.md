

# Use the array job index to control job differentiation
<a name="array_index_example"></a>

This tutorial describes how to use the `AWS_BATCH_JOB_ARRAY_INDEX` environment variable to differentiate the child jobs. Each child job is assigned to this variable. The example uses the child job's index number to read a specific line in a file. Then, it substitutes the parameter associated with that line number with a command inside the job's container. The result is that you can have multiple AWS Batch jobs that run the same Docker image and command arguments. However, the results are different because the array job index is used as a modifier.

In this tutorial, you create a text file that has all of the colors of the rainbow, each on its own line. Then, you create an entrypoint script for a Docker container that converts the index into a value that can be used for a line number in the color file. The index starts at zero, but line numbers start at one. Create a Dockerfile that copies the color and index files to the container image and sets `ENTRYPOINT` for the image to the entrypoint script. The Dockerfile and resources are built to a Docker image that's pushed to Amazon ECR. You then register a job definition that uses your new container image, submit an AWS Batch array job with that job definition, and view the results.

**Topics**
+ [Prerequisites](array-tutorial-prereqs.md)
+ [Build a container image](build-index-container.md)
+ [Push your image to Amazon ECR](push-array-image.md)
+ [Create and register a job definition](create-array-job-def.md)
+ [Submit an AWS Batch array job](submit-array-job.md)
+ [View your array job logs](#array-tutorial-logs)

## View your array job logs
<a name="array-tutorial-logs"></a>

After your job reaches the `SUCCEEDED` status, you can view the CloudWatch Logs from the job's container.

**To view your job's logs in CloudWatch Logs**

1. Open the AWS Batch console at [https://console.aws.amazon.com/batch/](https://console.aws.amazon.com/batch/).

1. In the left navigation pane, choose **Jobs**.

1. For **Job queue**, select a queue. 

1. In the **Status** section, choose **succeeded**.

1. To display all of the child jobs for your array job, select the job ID that was returned in the previous section.

1. To see the logs from the job's container, select one of the child jobs and choose **View logs**.  
![Array job container logs](http://docs.aws.amazon.com/batch/latest/userguide/images/array-logs.png)

1. View the other child job's logs. Each job returns a different color of the rainbow.