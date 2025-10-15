# Clean up your farm resources in Deadline Cloud

To develop and test new workloads and pipeline integrations, you can continue to use the
 Deadline Cloud developer farm that you created for this tutorial. If you no longer need your
 developer farm, you can delete its resources including farm, fleet, queue, AWS Identity and Access Management (IAM)
 roles, and logs in Amazon CloudWatch Logs. After you delete these resources, you will need to begin the
 tutorial again to use the resources. For more information, see [Getting started with Deadline Cloud resources](getting-started.md "getting-started.md").

###### To clean up developer farm resources

1. Choose your first CloudShell tab, then stop all the queue-fleet associations
 for your queue.



```
 `FLEETS=$(aws deadline list-queue-fleet-associations \
 --farm-id $DEV_FARM_ID \
 --queue-id $DEV_QUEUE_ID \
 --query "queueFleetAssociations[].fleetId" \
 --output text)
 for FLEET_ID in $FLEETS; do
 aws deadline update-queue-fleet-association \
 --farm-id $DEV_FARM_ID \
 --queue-id $DEV_QUEUE_ID \
 --fleet-id $FLEET_ID \
 --status STOP_SCHEDULING_AND_CANCEL_TASKS
 done`

```
2. List the queue fleet associations.



```
`aws deadline list-queue-fleet-associations \
 --farm-id $DEV_FARM_ID \
 --queue-id $DEV_QUEUE_ID`

```

You might need to rerun the command until the output reports `"status":
 "STOPPED"`, then you can proceed to the next step. This process can take
 several minutes to complete. 



```
{
    "queueFleetAssociations": [
        {
            "queueId": "queue-abcdefgh01234567890123456789012id",
            "fleetId": "fleet-abcdefgh01234567890123456789012id",
            "status": "STOPPED",
            "createdAt": "2023-11-21T20:49:19+00:00",
            "createdBy": "arn:aws:sts::123456789012:assumed-role/RoleToBeAssumed/MySessionName",
            "updatedAt": "2023-11-21T20:49:38+00:00",
            "updatedBy": "arn:aws:sts::123456789012:assumed-role/RoleToBeAssumed/MySessionName"
        },
        {
            "queueId": "queue-abcdefgh01234567890123456789012id",
            "fleetId": "fleet-abcdefgh01234567890123456789012id",
            "status": "STOPPED",
            "createdAt": "2023-11-21T20:32:06+00:00",
            "createdBy": "arn:aws:sts::123456789012:assumed-role/RoleToBeAssumed/MySessionName",
            "updatedAt": "2023-11-21T20:49:39+00:00",
            "updatedBy": "arn:aws:sts::123456789012:assumed-role/RoleToBeAssumed/MySessionName"
        }
    ]
}
```
3. Delete all of the queue-fleet associations for your queue.



```
`for FLEET_ID in $FLEETS; do
 aws deadline delete-queue-fleet-association \
 --farm-id $DEV_FARM_ID \
 --queue-id $DEV_QUEUE_ID \
 --fleet-id $FLEET_ID
 done`

```
4. Delete all of the fleets associated with your queue.



```
`for FLEET_ID in $FLEETS; do
 aws deadline delete-fleet \
 --farm-id $DEV_FARM_ID \
 --fleet-id $FLEET_ID
 done`

```
5. Delete the queue.



```
`aws deadline delete-queue \
 --farm-id $DEV_FARM_ID \
 --queue-id $DEV_QUEUE_ID`

```
6. Delete the farm.



```
`aws deadline delete-farm \
 --farm-id $DEV_FARM_ID`

```
7. Delete other AWS resources for your farm.


	1. Delete the fleet AWS Identity and Access Management (IAM) role.
	
	
	
	```
	`aws iam delete-role-policy \
	 --role-name "${DEV_FARM_NAME}FleetRole" \
	 --policy-name WorkerPermissions
	aws iam delete-role \
	 --role-name "${DEV_FARM_NAME}FleetRole"`
	
	```
	2. Delete the queue IAM role.
	
	
	
	```
	`aws iam delete-role-policy \
	 --role-name "${DEV_FARM_NAME}QueueRole" \
	 --policy-name S3BucketsAccess
	aws iam delete-role \
	 --role-name "${DEV_FARM_NAME}QueueRole"`
	
	```
	3. Delete the Amazon CloudWatch Logs log groups. Each queue and fleet has their own log
	 group.
	
	
	
	```
	`aws logs delete-log-group \
	 --log-group-name "/aws/deadline/$DEV_FARM_ID/$DEV_QUEUE_ID"
	aws logs delete-log-group \
	 --log-group-name "/aws/deadline/$DEV_FARM_ID/$DEV_CMF_ID"`
	`aws logs delete-log-group \
	 --log-group-name "/aws/deadline/$DEV_FARM_ID/$DEV_SMF_ID"`
	
	```
