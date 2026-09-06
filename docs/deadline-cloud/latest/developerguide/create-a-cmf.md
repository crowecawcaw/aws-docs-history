

# Create a customer-managed fleet
<a name="create-a-cmf"></a>

To create a customer-managed fleet (CMF), complete the following steps.

------
#### [ Deadline Cloud console ]

**To use the Deadline Cloud console to create a customer-managed fleet** 

1. Open the Deadline Cloud [ console](https://console.aws.amazon.com/deadlinecloud/home).

1. Select **Farms**. A list of available farms displays.

1. Select the name of the **Farm** you want to work in.

1. Select the **Fleets** tab, and then choose **Create fleet**.

1. Enter a **Name** for your fleet.

1. (Optional) Enter a **Description** for your fleet.

1. Select **Customer managed** for **Fleet type**.

1. Select your fleet's service access.

   1. We recommend using the **Create and use a new service role** option for each fleet for more granular permissions control. This option is selected by default.

   1. You can also use an existing service role by selecting **Choose a service role**.

1. Review your selections, then choose **Next**.

1. Select an **operating system** for your fleet. All of a fleet's workers must have a common operating system.

1. Select the **host CPU architecture**.

1. Select the minimum and maximum vCPU and memory **Hardware capabilities** to meet the workload demands of your fleets.

1. Select an Auto Scaling type. For more information, see [Use EventBridge to handle Auto Scaling events](https://docs.aws.amazon.com/autoscaling/ec2/userguide/automating-ec2-auto-scaling-with-eventbridge.html).
   + **No scaling**: You are creating an on-premises fleet and want opt out of Deadline Cloud Auto Scaling.
   + **Scaling recommendations**: You are creating an Amazon Elastic Compute Cloud (Amazon EC2) fleet.

1. (Optional) Select the arrow to expand the Add capabilities section.

1. (Optional) Select the checkbox for **Add GPU capability - Optional**, then enter the minimum and maximum GPUs and memory.

1. Review your selections, then choose **Next**.

1. (Optional) Define custom worker capabilities, then choose **Next**.

1. Using the dropdown, select one or more **queues** to associate with the fleet.
**Note**  
We recommend associating a fleet only with queues that are all in the same trust boundary. This recommendation ensures a strong security boundary between running jobs on the same worker.

1. Review the queue associations, then choose **Next**.

1. (Optional) For Default conda queue environment, we'll create an environment for your queue that will install conda packages requested by jobs.
**Note**  
The conda queue environment is used to install conda packages requested by jobs. Typically, you should uncheck the conda queue environment on queues associated with CMFs because CMFs won't have the required conda commands installed by default.

1. (Optional) Add tags to your CMF. For more information, see [Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html).

1. Review your fleet configuration and make any changes, then choose **Create fleet**.

1. Select the **Fleets** tab, then note the **Fleet ID**.

------
#### [ AWS CLI ]

**To use the AWS CLI to create a customer-managed fleet**

1. Open a terminal.

1. Create `fleet-trust-policy.json` in a new editor.

   1. Add the following IAM policy, replacing the {{ITALICIZED}} text with your AWS account ID and Deadline Cloud farm ID.

------
#### [ JSON ]

****  

      ```
      {
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
                          "aws:SourceAccount": "{{111122223333}}"
                      },
                      "ArnEquals": {
                          "aws:SourceArn": "arn:aws:deadline:*:{{111122223333}}:farm/{{FARM_ID}}"
                      }
                  }
              }
          ]
      }
      ```

------

   1. Save your changes.

1. Create `fleet-policy.json`.

   1. Add the following IAM policy.

------
#### [ JSON ]

****  

      ```
      {
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
                  "Resource": "arn:aws:deadline:*:{{111122223333}}:*",
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
      }
      ```

------

   1. Save your changes.

1. Add an IAM role for the workers in your fleet to use.

   ```
   aws iam create-role --role-name FleetWorkerRoleName --assume-role-policy-document file://fleet-trust-policy.json
   aws iam put-role-policy --role-name FleetWorkerRoleName --policy-name FleetWorkerPolicy --policy-document file://fleet-policy.json
   ```

1. Create `create-fleet-request.json`.

   1. Add the following IAM policy, replacing the ITALICIZED text with your CMF's values.
**Note**  
You can find the {{ROLE\_ARN}} in the `create-cmf-fleet.json`.  
For the {{OS\_FAMILY}}, you must choose one of `linux`, `macos` or `windows`.

      ```
      {
          "farmId": "{{FARM_ID}}",
          "displayName": "{{FLEET_NAME}}",
          "description": "{{FLEET_DESCRIPTION}}",
          "roleArn": "{{ROLE_ARN}}",
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
                      "osFamily": "{{OS_FAMILY}}",
                      "cpuArchitectureType": "x86_64"
                  }
              }
          }
      }
      ```

   1. Save your changes.

1. Create your fleet.

   ```
   aws deadline create-fleet --cli-input-json file://create-fleet-request.json
   ```

------