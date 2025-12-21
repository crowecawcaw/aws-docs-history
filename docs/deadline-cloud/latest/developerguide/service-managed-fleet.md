# Add a service-managed fleet to your developer farm

in Deadline Cloud

AWS CloudShell does not provide enough compute capacity to test larger workloads. It's also not
configured to work with jobs that distribute tasks on multiple worker hosts.

Instead of using CloudShell, you can add an Auto Scaling service-managed fleet (SMF) to your
developer farm. An SMF provides sufficient compute capacity for larger workloads and can
handle jobs that need to distribute job tasks across multiple worker hosts.

Before you add an SMF, you must set up a Deadline Cloud farm, queue, and fleet. See [Create a Deadline Cloud farm](create-a-farm.md "create-a-farm.md").

###### To add a service-managed fleet to your developer farm

1. Choose your first AWS CloudShell tab, then create the service-managed fleet and add its
   fleet ID to `.bashrc`. This action makes it available for other terminal
   sessions.

```
`FLEET_ROLE_ARN="arn:aws:iam::$(aws sts get-caller-identity \
 --query "Account" --output text):role/${DEV_FARM_NAME}FleetRole"
 aws deadline create-fleet \
 --farm-id $DEV_FARM_ID \
 --display-name "$DEV_FARM_NAME SMF" \
 --role-arn $FLEET_ROLE_ARN \
 --max-worker-count 5 \
 --configuration \
 '{
 "serviceManagedEc2": {
 "instanceCapabilities": {
 "vCpuCount": {
 "min": 2,
 "max": 4
 },
 "memoryMiB": {
 "min": 512
 },
 "osFamily": "linux",
 "cpuArchitectureType": "x86_64"
 },
 "instanceMarketOptions": {
 "type": "spot"
 }
 }
 }'

 echo "DEV_SMF_ID=$(aws deadline list-fleets \
 --farm-id $DEV_FARM_ID \
 --query "fleets[?displayName=='$DEV_FARM_NAME SMF'].fleetId \
 | [0]" --output text)" >> ~/.bashrc
 source ~/.bashrc`

```

2. Associate the SMF with your queue.

```
`aws deadline create-queue-fleet-association \
 --farm-id $DEV_FARM_ID \
 --queue-id $DEV_QUEUE_ID \
 --fleet-id $DEV_SMF_ID`

```

3. Submit simple_file_job to the queue. When prompted to confirm the
   upload, enter `y`.

```
deadline bundle submit simple_file_job \
    -p InFile=simple_job/template.yaml \
    -p OutFile=hash-jobattachments.txt

```

4. Confirm the SMF is working correctly.

```
`deadline fleet get`

```

    * The worker may take a few minutes to start. Repeat the `deadline
     fleet get` command until you can see that the fleet is
     running.
    * The `queueFleetAssociationsStatus` for
     service-managed fleet will be
     `ACTIVE`.
    * The SMF `autoScalingStatus` will change from
     `GROWING` to `STEADY`.

Your status will look similar to the following:

```
fleetId: fleet-2cc78e0dd3f04d1db427e7dc1d51ea44
farmId: farm-63ee8d77cdab4a578b685be8c5561c4a
displayName: DeveloperFarm SMF
description: ''
status: ACTIVE
autoScalingStatus: STEADY
targetWorkerCount: 0
workerCount: 0
minWorkerCount: 0
maxWorkerCount: 5

```

5. View the log for the job that you submitted. This log is stored in a log in
   Amazon CloudWatch Logs, not the CloudShell file system.

```
 JOB_ID=$(deadline config get defaults.job_id)
 SESSION_ID=$(aws deadline list-sessions \
         --farm-id $DEV_FARM_ID \
         --queue-id $DEV_QUEUE_ID \
         --job-id $JOB_ID \
         --query "sessions[0].sessionId" \
         --output text)
 aws logs tail /aws/deadline/$DEV_FARM_ID/$DEV_QUEUE_ID \
     --log-stream-names $SESSION_ID

```

## Next steps

After creating and testing a service-managed fleet, you should remove the resources
that you created to avoid unnecessary charges.

- [Clean up your farm resources in Deadline Cloud](cleaning-up.md "cleaning-up.md") to shut down the
  resources that you used for this tutorial.
