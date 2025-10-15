# Download finished output in Deadline Cloud

After a job is finished, you can use the AWS Deadline Cloud monitor to download the results to
 your workstation. The output file is stored with the name and location that you
 specified when you created the job.

Output files are stored indefinitely. To reduce storage costs, consider creating an S3
 Lifecycle configuration for your queue's Amazon S3 bucket. For more information, see [Managing your storage lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html "https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html") in the *Amazon Simple Storage Service User
 Guide*.

###### To download the finished output of a job, step, or task

1. Follow the steps in [View and manage job details in Deadline Cloud](view-a-job.md "view-a-job.md") to
 view a list of jobs.
2. Select the job, step, or task that you want to download the output for.




	* If you select a job, you can download all of the output for all of the
	 tasks in all of the steps for that job.
	* If you select a step, you can download all of the output for all of
	 the tasks in that step.
	* If you select a task, you can download the output for that individual
	 task.
3. From the **Actions** menu, choose **Download
 output**.
4. The output will be downloaded to the location set when the job was
 submitted.
###### Note

Downloading output using the menu is currently only supported for
 Windows and Linux. If you have a
 Mac and you choose the **Download output** menu
 item, a window shows the AWS CLI command that you can use to download the rendered
 output.
