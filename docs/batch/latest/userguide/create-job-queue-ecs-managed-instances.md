

# Create an Amazon ECS Managed Instances job queue
<a name="create-job-queue-ecs-managed-instances"></a>

Complete the following steps to create a job queue for Amazon ECS Managed Instances compute environments.

**To create an Amazon ECS Managed Instances job queue**

1. Open the AWS Batch console at [https://console.aws.amazon.com/batch/](https://console.aws.amazon.com/batch/).

1. From the navigation bar, choose the AWS Region to use.

1. In the navigation pane, choose **Job queues**.

1. Choose **Create**.

1. For **Name**, enter a unique name for your job queue. The name can be up to 128 characters long, and can contain uppercase and lowercase letters, numbers, and underscores (\_).

1. For **Priority**, enter a whole number value for the job queue's priority. The scheduler runs job queues with a higher priority before lower-priority job queues that are associated with the same compute environment. Priority is determined in descending order. For example, a job queue with a priority value of 10 is given scheduling preference over a job queue with a priority value of 1.

1. (Optional) For **Scheduling policy Amazon Resource Name (ARN)**, choose an existing scheduling policy.

1. For **Connected compute environments**, choose one or more Amazon ECS Managed Instances compute environments from the list to associate with the job queue. Choose compute environments in the order that you want the queue to attempt job placement. The job scheduler uses the order that you specify to determine which compute environment starts a given job. Before you can associate them with a job queue, compute environments must be in the `VALID` state. You can associate up to three compute environments with a job queue.
**Important**  
If your job queue includes both On-Demand and Spot compute environments, all On-Demand compute environments must be ordered before any Spot compute environments.

1. For **Compute environment order**, choose the up and down arrows to configure the order that you want.

1. Choose **Create job queue** to finish and create your job queue.