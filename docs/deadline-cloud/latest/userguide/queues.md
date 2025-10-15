# Deadline Cloud queues

A queue is a farm resource that manages and processes jobs.

To work with queues, you should already have a monitor and farm set up.

###### Topics

* [Create a queue](#create-queue "#create-queue")
* [Create a queue environment](create-queue-environment.md "create-queue-environment.md")
* [Associate a queue and fleet](associate-a-queue-and-fleet.md "associate-a-queue-and-fleet.md")

## Create a queue


1. From the [Deadline Cloud
 console](https://console.aws.amazon.com/deadlinecloud/home "https://console.aws.amazon.com/deadlinecloud/home") dashboard, select the farm that you want to create a queue
 for.


	1. Alternatively, in the left side panel choose **Farms and
	 other resources**, then select the farm you want to create
	 a queue for.
2. In the **Queues** tab, choose **Create
 queue**.
3. Enter a name for your queue.
4. For **Description**, enter the queue description. A
 description helps you identify your queue's purpose.
5. For **Job attachments**, you can either create a new Amazon S3
 bucket or choose an existing Amazon S3 bucket.


	1. To create a new Amazon S3 bucket
	
	
		1. Select **Create new job bucket**.
		2. Enter a name for the bucket. We recommend naming the bucket
		 `deadlinecloud-job-attachments-[MONITORNAME]`.
		3. Enter a **Root prefix** to define or change
		 your queue's root location.
	2. To choose an existing Amazon S3 bucket
	
	
		1. Select **Choose an existing S3 bucket** >
		 **Browse S3**.
		2. Select the S3 bucket for your queue from the list of available
		 buckets.
6. (Optional) To associate your queue with a customer-managed fleet, select
 **Enable association with customer-managed fleets**.
7. If you enable association with customer-managed fleets, you must complete the
 following steps. 


###### Important

We strongly recommend specifying users and groups for run-as
 functionality. If you don't, it will degrade your farm’s security posture
 because the jobs can then do everything the worker's agent can do. For more
 information about the potential security risks, see [Run jobs as users and groups](security-best-practices.md#job-run-as-user "security-best-practices.md#job-run-as-user").


	1. For Run as user:
	
	
	To provide credentials for the queue's jobs, select
	 **Queue-configured user**.
	
	
	Or, to opt out of setting your own credentials and run jobs as the
	 worker agent user, select **Worker agent user**.
	2. (Optional) For Run as user credentials, enter a user name and group
	 name to provide credentials for the queue's jobs.
	
	
	If you are using a Windows fleet, you must create an AWS Secrets Manager
	 secret that contains the password for the Run as user. If you don't have
	 an existing secret with the password, choose **Create
	 secret** to open the Secrets Manager console to create a secret. For
	 more information, see [Manage access to Windows job user secrets](../developerguide/manage-access-windows-secrets.md "../developerguide/manage-access-windows-secrets.md") in the
	 *Deadline Cloud Developer Guide*.
8. Requiring a budget helps manage costs for your queue. Select either
 **Don't require a budget** or **Require a
 budget**.
9. Your queue requires permission to access Amazon S3 on your behalf. You can create a
 new service role or use an existing service role. If you don't have an existing
 service role, create and use a new service role.


	1. To use an existing service role, select **Choose a service
	 role**, and then select a role from the dropdown.
	2. To create a new service role, select **Create and use a new
	 service role**, and then enter a role name and description.
10. (Optional) To add environment variables for the queue environment, choose
 **Add new environment variable**, and then enter a name and
 value for each variable you add.
11. (Optional) Choose **Add new tag** to add one or more tags to
 your queue.
12. To create a default Conda queue environment, keep the checkbox
 selected. To learn more about queue environments, see  [Create a queue environment](create-queue-environment.md "create-queue-environment.md"). If
 you are creating a queue for a customer-managed fleet, clear the
 checkbox.
13. Choose **Create queue**.
