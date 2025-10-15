# Configure storage profiles for queues

 A queue's configuration includes a list of case-sensitive names of the shared file
 system locations that jobs submitted to the queue require access to. for example, jobs
 submitted to queue `Q1` require file system locations `FSCommon` and
 `FS1`. Jobs submitted to queue `Q2` require file system locations
 `FSCommon` and `FS2`. 

To set the queue's configurations to require these file system locations, use the
 following script: 


```

# Change the value of FARM_ID to your farm's identifier
FARM_ID=farm-`00112233445566778899aabbccddeeff`
# Change the value of QUEUE1_ID to queue Q1's identifier
QUEUE1_ID=queue-`00112233445566778899aabbccddeeff`
# Change the value of QUEUE2_ID to queue Q2's identifier
QUEUE2_ID=queue-`00112233445566778899aabbccddeeff`

aws deadline update-queue --farm-id $FARM_ID --queue-id $QUEUE1_ID \
  --required-file-system-location-names-to-add FSComm FS1

aws deadline update-queue --farm-id $FARM_ID --queue-id $QUEUE2_ID \
  --required-file-system-location-names-to-add FSComm FS2
```
 A queue's configuration also includes a list of allowed storage profiles that applies
 to jobs submitted to and fleets associated with that queue. Only storage profiles that
 define file system locations for all of the required file system locations for the queue are
 allowed in the queue's list of allowed storage profiles. 

A job fails if you submit it with a storage profile that isn't in the list of allowed
 storage profiles for the queue. You can always submit a job with no storage profile to a
 queue. The workstation configurations labeled `WSAll` and `WS1` both
 have the required file system locations (`FSCommon` and `FS1`) for
 queue `Q1`. They need to be allowed to submit jobs to the queue. Similarly,
 workstation configurations `WSAll` and `WS2` meet the requirements for
 queue `Q2`. They need to be allowed to submit jobs to that queue. Update both
 queue configurations to allow jobs to be submitted with these storage profiles using the
 following script: 


```
# Change the value of WSALL_ID to the identifier of the WSAll storage profile
WSALL_ID=sp-`00112233445566778899aabbccddeeff`
# Change the value of WS1 to the identifier of the WS1 storage profile
WS1_ID=sp-`00112233445566778899aabbccddeeff`
# Change the value of WS2 to the identifier of the WS2 storage profile
WS2_ID=sp-`00112233445566778899aabbccddeeff`

aws deadline update-queue --farm-id $FARM_ID --queue-id $QUEUE1_ID \
  --allowed-storage-profile-ids-to-add $WSALL_ID $WS1_ID

aws deadline update-queue --farm-id $FARM_ID --queue-id $QUEUE2_ID \
  --allowed-storage-profile-ids-to-add $WSALL_ID $WS2_ID
```
 If you add the `WS2` storage profile to the list of allowed storage profiles
 for queue `Q1` it fails: 


```
$ aws deadline update-queue --farm-id $FARM_ID --queue-id $QUEUE1_ID \
  --allowed-storage-profile-ids-to-add $WS2_ID

An error occurred (ValidationException) when calling the UpdateQueue operation: Storage profile id: sp-`00112233445566778899aabbccddeeff` does not have required file system location: FS1
```
 This is because the `WS2` storage profile doesn't contain a definition for
 the file system location named `FS1` that queue `Q1` requires. 

 Associating a fleet that is configured with a storage profile that is not in the
 queue's list of allowed storage profiles also fails. For example: 


```
$ aws deadline create-queue-fleet-association --farm-id $FARM_ID \
   --fleet-id $FLEET_ID \
   --queue-id $QUEUE1_ID

An error occurred (ValidationException) when calling the CreateQueueFleetAssociation operation: Mismatch between storage profile ids.
```
To fix the error, add the storage profile named `WorkerConfig` to the list of
 allowed storage profiles for both queue `Q1` and queue `Q2`. Then,
 associate the fleet with these queues so that workers in the fleet can run jobs from both
 queues. 


```
# Change the value of FLEET_ID to your fleet's identifier
FLEET_ID=fleet-`00112233445566778899aabbccddeeff`
# Change the value of WORKER_CFG_ID to your storage profile named WorkerCfg
WORKER_CFG_ID=sp-`00112233445566778899aabbccddeeff`

aws deadline update-queue --farm-id $FARM_ID --queue-id $QUEUE1_ID \
  --allowed-storage-profile-ids-to-add $WORKER_CFG_ID

aws deadline update-queue --farm-id $FARM_ID --queue-id $QUEUE2_ID \
  --allowed-storage-profile-ids-to-add $WORKER_CFG_ID

aws deadline create-queue-fleet-association --farm-id $FARM_ID \
  --fleet-id $FLEET_ID \
  --queue-id $QUEUE1_ID

aws deadline create-queue-fleet-association --farm-id $FARM_ID \
  --fleet-id $FLEET_ID \
  --queue-id $QUEUE2_ID
```
