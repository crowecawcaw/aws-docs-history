# Viewing job details

If you want more information about an Amazon S3 Batch Operations job than you can retrieve
 by listing jobs, you can view all of the details for a single job. You can view details
 for jobs that haven't yet finished or jobs that finished within the last 90 days. In
 addition to the information returned in a job list, a single job's details include other
 items, such as: 


* The operation parameters
* Details about the manifest
* Information about the completion report (if you configured one when you
 created the job)
* The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) user role that you
 assigned to run the job
By viewing an individual job's details, you can access a job's entire configuration. To view a job’s details, you can use the Amazon S3 console or the AWS Command Line Interface (AWS CLI).


## Get an S3 Batch Operations job description in the Amazon S3 console


###### To view a Batch Operations job description by using the console

1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Batch Operations**.
3. Choose the job ID of the specific job to view its details.

## Get an
 S3 Batch Operations job description in the AWS CLI


The following example gets the description of an S3 Batch Operations job by using the AWS CLI. To use the following example command, replace the ``user input placeholders`` with your own information.



```
aws s3control describe-job \
--region `us-west-2` \
--account-id `account-id` \
--job-id `00e123a4-c0d8-41f4-a0eb-b46f9ba5b07c`
```
For more information and examples, see [describe-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/describe-job.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/describe-job.html") in the *AWS CLI Command Reference*.
