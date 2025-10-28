# Create an Amazon EC2 job queue

Complete the following steps to create a job queue for Amazon Elastic Compute Cloud (Amazon EC2).

###### To create an Amazon EC2 job queue

1. Open the AWS Batch console at [https://console.aws.amazon.com/batch/](https://console.aws.amazon.com/batch/ "https://console.aws.amazon.com/batch/").
2. From the navigation bar, select the AWS Region to use.
3. In the navigation pane, choose **Job queues**.
4. Choose **Create**.
5. For **Orchestration type**, choose **Amazon Elastic Compute Cloud
   (Amazon EC2)**.
6. For **Name**, enter a unique name for your job queue. The name can be up
   to 128 characters long, and can contain uppercase and lowercase letters, numbers, and
   underscores (\_).
7. For **Priority**, enter an whole number value for the job queue's
   priority. Job queues with a higher priority are run before lower priority job queues that are
   associated with the same compute environment. Priority is determined in descending order. For
   example, a job queue with a priority value of 10 is given scheduling preference over a job
   queue with a priority value of 1.
8. (Optional) For **Scheduling policy Amazon Resource Name (ARN)**, choose an existing
   scheduling policy.
9. For **Connected compute environments**, select one or more compute
   environments from the list to associate with the job queue. Select compute environments in the
   order that you want the queue to attempt job queue placement. The job scheduler uses the order
   that you select compute environments in to determine which compute environment starts a given
   job. Before you can associate them with a job queue, compute environments must be in the
   `VALID` state. You can associate up to three compute environments with a job queue.
   If you don't have an existing compute environment, choose **Create compute
   environment**

###### Note

All compute environments that are associated with a job queue must share the same
provisioning model. AWS Batch doesn't support mixing provisioning models in a single job
queue. 10. For **Compute environment order**, choose the up and down arrows to configure
order that you want. 11. Choose **Create job queue** to finish and create your job queue.
