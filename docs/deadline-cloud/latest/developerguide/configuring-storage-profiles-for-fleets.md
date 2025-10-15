# Configure storage profiles for
 fleets

You can configure a fleet to include a storage profile that models
 the file system locations on all workers in the fleet. The host file system configuration of
 all workers in a fleet must match their fleet's storage profile. Workers with different file
 system configurations must be in separate fleets. 

To set your fleet's configuration to use the `WorkerConfig` storage profile
 use the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html "https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html") in [AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html "https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html"): 


```
# Change the value of FARM_ID to your farm's identifier
FARM_ID=farm-`00112233445566778899aabbccddeeff`
# Change the value of FLEET_ID to your fleet's identifier
FLEET_ID=fleet-`00112233445566778899aabbccddeeff`
# Change the value of WORKER_CFG_ID to your storage profile named WorkerConfig
WORKER_CFG_ID=sp-`00112233445566778899aabbccddeeff`

FLEET_WORKER_MODE=$( \
  aws deadline get-fleet --farm-id $FARM_ID --fleet-id $FLEET_ID \
   --query '.configuration.customerManaged.mode' \
)
FLEET_WORKER_CAPABILITIES=$( \
  aws deadline get-fleet --farm-id $FARM_ID --fleet-id $FLEET_ID \
   --query '.configuration.customerManaged.workerCapabilities' \
)

aws deadline update-fleet --farm-id $FARM_ID --fleet-id $FLEET_ID \
  --configuration \
  "{
    \"customerManaged\": {
      \"storageProfileId\": \"$WORKER_CFG_ID\",
      \"mode\": $FLEET_WORKER_MODE,
      \"workerCapabilities\": $FLEET_WORKER_CAPABILITIES
    }
  }"
```
