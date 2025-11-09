# Create a Deadline Cloud farm

To create your developer farm and queue resources in AWS Deadline Cloud, use the AWS Command Line Interface (AWS CLI),
as shown in the following procedure. You will also create an AWS Identity and Access Management (IAM) role and a
customer-managed fleet (CMF) and associate the fleet with your queue. Then you can configure
the AWS CLI and confirm that your farm is set up and working as specified.

You can use this farm to explore the features of Deadline Cloud, then develop and test new
workloads, customizations, and pipeline integrations.

###### To create a farm

1. [Open an AWS CloudShell
   session](https://console.aws.amazon.com/cloudshell/home?region=us-west-2 "https://console.aws.amazon.com/cloudshell/home?region=us-west-2"). You'll use the CloudShell window to enter AWS Command Line Interface (AWS CLI)
   commands to run the examples in this tutorial. Keep the CloudShell window open as
   you proceed.
2. Create a name for your farm, and add that farm name to `~/.bashrc`.
   This will make it available for other terminal sessions.

```
`echo "DEV_FARM_NAME=DeveloperFarm" >> ~/.bashrc
source ~/.bashrc`

```

3. Create the farm resource, and add its farm ID to `~/.bashrc`.

```
`aws deadline create-farm \
 --display-name "$DEV_FARM_NAME"

echo "DEV_FARM_ID=\$(aws deadline list-farms \
 --query \"farms[?displayName=='\$DEV_FARM_NAME'].farmId \
 | [0]\" --output text)" >> ~/.bashrc
source ~/.bashrc`
```

4. Create the queue resource, and add its queue ID to `~/.bashrc.`

```
`aws deadline create-queue \
 --farm-id $DEV_FARM_ID \
 --display-name "$DEV_FARM_NAME Queue" \
 --job-run-as-user '{"posix": {"user": "job-user", "group": "job-group"}, "runAs":"QUEUE_CONFIGURED_USER"}'

echo "DEV_QUEUE_ID=\$(aws deadline list-queues \
 --farm-id \$DEV_FARM_ID \
 --query \"queues[?displayName=='\$DEV_FARM_NAME Queue'].queueId \
 | [0]\" --output text)" >> ~/.bashrc
source ~/.bashrc`
```

5. Create an IAM role for the fleet. This role provides worker hosts in your fleet
   with the necessary security credentials to run jobs from your queue.

```
`aws iam create-role \
 --role-name "${DEV_FARM_NAME}FleetRole" \
 --assume-role-policy-document \
 '{
 "Version": "2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "credentials.deadline.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
 }'
aws iam put-role-policy \
 --role-name "${DEV_FARM_NAME}FleetRole" \
 --policy-name WorkerPermissions \
 --policy-document \
 '{
 "Version": "2012-10-17",
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
 "Resource": "*",
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
 "Resource": "arn:aws:logs:*:*:*:/aws/deadline/*",
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
 }'`

```

6. Create the customer-managed fleet (CMF), and add its fleet ID to
   `~/.bashrc`.

```
`FLEET_ROLE_ARN="arn:aws:iam::$(aws sts get-caller-identity \
 --query "Account" --output text):role/${DEV_FARM_NAME}FleetRole"
aws deadline create-fleet \
 --farm-id $DEV_FARM_ID \
 --display-name "$DEV_FARM_NAME CMF" \
 --role-arn $FLEET_ROLE_ARN \
 --max-worker-count 5 \
 --configuration \
 '{
 "customerManaged": {
 "mode": "NO_SCALING",
 "workerCapabilities": {
 "vCpuCount": {"min": 1},
 "memoryMiB": {"min": 512},
 "osFamily": "linux",
 "cpuArchitectureType": "x86_64"
 }
 }
 }'

echo "DEV_CMF_ID=\$(aws deadline list-fleets \
 --farm-id \$DEV_FARM_ID \
 --query \"fleets[?displayName=='\$DEV_FARM_NAME CMF'].fleetId \
 | [0]\" --output text)" >> ~/.bashrc
source ~/.bashrc`
```

7. Associate the CMF with your queue.

```
`aws deadline create-queue-fleet-association \
 --farm-id $DEV_FARM_ID \
 --queue-id $DEV_QUEUE_ID \
 --fleet-id $DEV_CMF_ID`

```

8. Install the Deadline Cloud command-line interface.

```
`pip install deadline`
```

9. To set the default farm to the farm ID and the queue to the queue ID that you
   created earlier, use the following command.

```
`deadline config set defaults.farm_id $DEV_FARM_ID
deadline config set defaults.queue_id $DEV_QUEUE_ID`

```

10. (Optional) To confirm that your farm is set up according to your specifications,
    use the following commands:
    - List all farms – `deadline farm list`
    - List all queues in the default farm – `deadline queue
list`
    - List all fleets in the default farm – `deadline fleet
list`
    - Get the default farm – `deadline farm
get`
    - Get the default queue – `deadline queue
get`
    - Get all the fleets associated with the default queue –
      `deadline fleet get`

## Next steps

After you create your farm, you can run the Deadline Cloud worker agent on the hosts in your
fleet to process jobs. See [Run the Deadline Cloud worker agent](run-worker.md "run-worker.md").
