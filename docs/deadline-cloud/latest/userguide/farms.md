# Deadline Cloud farms

With a Deadline Cloud farm, you can manage users and project resources. A 
 *farm* is a where your project resources are located.
 Your farm consists of queues and fleets. A *queue* is 
 where submitted jobs are located and scheduled to be rendered. A *fleet* is a group of worker nodes that run tasks to complete jobs. After you 
 create a farm, you can create queues and fleets to meet your project's needs.


## Create a farm


1. From the [Deadline Cloud 
 console](https://console.aws.amazon.com/deadlinecloud/home "https://console.aws.amazon.com/deadlinecloud/home"), choose **Go to Dashboard**.
2. In the Farms section of the Deadline Cloud dashboard, choose 
 **Actions** â **Create farm**.


	1. Alternatively, in the left side panel choose 
	 **Farms and other resources**, then choose 
	 **Create Farm**.
3. Add a **Name** for your farm.
4. For **Description**, enter the farm description. 
 A clear description can help you quickly identify your farm's purpose.
5. (Optional) By default, your data is
 encrypted with a key that AWS owns and manages for your security. You can
 choose **Customize encryption settings (advanced)** to use
 an existing key or to create a new one that you manage.


If you choose to customize encryption settings using the checkbox, enter a
 AWS KMS ARN, or create a new AWS KMS by choosing **Create new KMS
 key**.
6. (Optional) Choose **Add new
 tag** to add one or more tags to your farm.
7. Choose **Create farm**. After creation, your farm 
 displays.
