# Create a customer-managed fleet

To create a customer-managed fleet (CMF), complete the following steps.


Deadline Cloud console
**To use the Deadline Cloud console to create a customer-managed
 fleet**



1. Open the Deadline Cloud [console](https://console.aws.amazon.com/deadlinecloud/home "https://console.aws.amazon.com/deadlinecloud/home").
2. Select **Farms**. A list of available 
 farms displays.
3. Select the name of the **Farm** you want to 
 work in.
4. Select the **Fleets** tab, and then choose 
 **Create fleet**.
5. Enter a **Name** for your fleet.
6. (Optional) Enter a
 **Description** for your fleet.
7. Select **Customer managed** for **Fleet
 type**.
8. Select your fleet's service access.


	1. We recommend using the **Create and use a new service role** option for each 
	 fleet for more granular permissions control. This option is selected by default.
	2. You can also use an existing service role by selecting **Choose a service role**.
9. Review your selections, then choose **Next**.
10. Select an **operating system** for your fleet. All of 
 a fleet’s workers must have a common operating system.
11. Select the **host CPU architecture**.
12. Select the minimum and maximum vCPU and memory **Hardware 
 capabilities** to meet the workload demands of your fleets.
13. Select an Auto Scaling type. For more information, see [Use EventBridge to handle Auto Scaling events](https://docs.aws.amazon.com/autoscaling/ec2/userguide/automating-ec2-auto-scaling-with-eventbridge.html "https://docs.aws.amazon.com/autoscaling/ec2/userguide/automating-ec2-auto-scaling-with-eventbridge.html").




	* **No scaling**: You are creating an
	 on-premises fleet and want opt out of Deadline Cloud Auto Scaling.
	* **Scaling recommendations**: You are creating
	 an Amazon Elastic Compute Cloud (Amazon EC2) fleet.
14. (Optional) Select the arrow to expand the Add capabilities section.
15. (Optional) Select the checkbox for **Add GPU capability - 
 Optional**, then enter the minimum and maximum GPUs and memory.
16. Review your selections, then choose **Next**.
17. (Optional) Define custom worker capabilities, then choose **Next**.
18. Using the dropdown, select one or more **queues** to associate with the
 fleet.


###### Note

We recommend associating a fleet only with queues that are all in
 the same trust boundary. This ensures a strong security boundary
 between running jobs on the same worker.
19. Review the queue associations, then choose **Next**.
20. (Optional) For Default Conda queue environment, 
 we'll create an environment for your queue that will install Conda packages 
 requested by jobs.


###### Note

The Conda queue environment is used to install Conda packages requested by jobs. Typically, 
 you should uncheck the Conda queue environment on queues associated with CMFs because 
 CMFs won't have the required Conda commands installed by default.
21. (Optional) Add tags to your CMF. For more information, see [Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html "https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html").
22. Review your fleet configuration and make any changes, then choose 
 **Create fleet**.
23. Select the **Fleets** tab, then note the
 **Fleet ID**.


AWS CLI
**To use the AWS CLI to create a customer-managed
 fleet**


1. Open a terminal.
2. Create `fleet-trust-policy.json` in a new editor.


	1. Add the following IAM policy, replacing the
	 `ITALICIZED` text with your AWS
	 account ID and Deadline Cloud farm ID.
	
	
	JSONJSON
	
	
	
	
	```
	`{
	 "Version":"2012-10-17", 
	 "Statement": [
	 {
	 "Effect": "Allow",
	 "Principal": {
	 "Service": "credentials.deadline.amazonaws.com"
	 },
	 "Action": "sts:AssumeRole",
	 "Condition": {
	 "StringEquals": {
	 "aws:SourceAccount": "`111122223333`"
	 },
	 "ArnEquals": {
	 "aws:SourceArn": "arn:aws:deadline:*:`111122223333`:farm/`FARM_ID`"
	 }
	 }
	 }
	 ]
	}`
	
	```
	2. Save your changes.
3. Create `fleet-policy.json`.


	1. Add the following IAM policy.
	
	
	JSONJSON
	
	
	
	
	```
	`{
	 "Version":"2012-10-17", 
	 "Statement": [
	 {
	 "Effect": "Allow",
	 "Action": [
	 "deadline:AssumeFleetRoleForWorker",
	 "deadline:UpdateWorker",
	 "deadline:DeleteWorker",
	 "deadline:UpdateWorkerSchedule",
	 "deadline:BatchGetJobEntity",
	 "deadline:AssumeQueueRoleForWorker"
	 ],
	 "Resource": "arn:aws:deadline:*:`111122223333`:*",
	 "Condition": {
	 "StringEquals": {
	 "aws:PrincipalAccount": "${aws:ResourceAccount}"
	 }
	 }
	 },
	 {
	 "Effect": "Allow",
	 "Action": [
	 "logs:CreateLogStream"
	 ],
	 "Resource": "arn:aws:logs:*:*:*://deadline/*",
	 "Condition": {
	 "StringEquals": {
	 "aws:PrincipalAccount": "${aws:ResourceAccount}"
	 }
	 }
	 },
	 {
	 "Effect": "Allow",
	 "Action": [
	 "logs:PutLogEvents",
	 "logs:GetLogEvents"
	 ],
	 "Resource": "arn:aws:logs:*:*:*:/aws/deadline/*",
	 "Condition": {
	 "StringEquals": {
	 "aws:PrincipalAccount": "${aws:ResourceAccount}"
	 }
	 }
	 }
	 ]
	}`
	
	```
	2. Save your changes.
4. Add an IAM role for the workers in your fleet to use.



```
aws iam create-role --role-name FleetWorkerRoleName --assume-role-policy-document file://fleet-trust-policy.json
aws iam put-role-policy --role-name FleetWorkerRoleName --policy-name FleetWorkerPolicy --policy-document file://fleet-policy.json
```
5. Create `create-fleet-request.json`.


	1. Add the following IAM policy, replacing the ITALICIZED text
	 with your CMF's values.
	
	
	###### Note
	
	You can find the `ROLE_ARN` in
	 the `create-cmf-fleet.json`.
	
	For the `OS_FAMILY`, you must choose one of `linux`, 
	 `macos` or `windows`.
	
	
	
	```
	{
	    "farmId": "`FARM_ID`",
	    "displayName": "`FLEET_NAME`",
	    "description": "`FLEET_DESCRIPTION`",
	    "roleArn": "`ROLE_ARN`",
	    "minWorkerCount": 0,
	    "maxWorkerCount": 10,
	    "configuration": {
	        "customerManaged": {
	            "mode": "NO_SCALING",
	            "workerCapabilities": {
	                "vCpuCount": {
	                    "min": 1,
	                    "max": 4
	                },
	                "memoryMiB": {
	                    "min": 1024,
	                    "max": 4096
	                },
	                "osFamily": "`OS_FAMILY`",
	                "cpuArchitectureType": "x86_64",
	            },
	        },
	    }
	}
	```
	2. Save your changes.
6. Create your fleet.



```
`aws deadline create-fleet --cli-input-json file://create-fleet-request.json`
```
