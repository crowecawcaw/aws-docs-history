# Deploy the Hub SDK

with a script

Deploy the managed integrations Hub SDK components manually using installation scripts, then validate the
deployment. This section describes the script execution steps and verification process.

###### Topics

- [Prepare your
  environment](#managedintegrations-sdk-v2-cookbook-runscript-prereq "#managedintegrations-sdk-v2-cookbook-runscript-prereq")
- [Run the Hub SDK script](#managedintegrations-sdk-v2-cookbook-runscript-run "#managedintegrations-sdk-v2-cookbook-runscript-run")
- [Verify hub
  provisioning](#managedintegrations-sdk-v2-cookbook-odm-validation-hub "#managedintegrations-sdk-v2-cookbook-odm-validation-hub")
- [Verify agent
  operation](#managedintegrations-sdk-v2-cookbook-odm-validation-agent "#managedintegrations-sdk-v2-cookbook-odm-validation-agent")
- [Verify
  LPW-Provisioner operation](#managedintegrations-sdk-v2-cookbook-odm-validation-provisioner "#managedintegrations-sdk-v2-cookbook-odm-validation-provisioner")

## Prepare your

environment

Complete these steps before running the SDK installation script:

1. Create a folder named `middleware` inside the `artifacts`
   folder.
2. Copy your hub middleware files to the `middleware` folder.
3. Run the initialization commands before starting the SDK.

###### Important

Repeat the initialization commands after each hub reboot.

```
#Get the current user
_user=$(whoami)

#Get the current group
_grp=$(id -gn)

#Display the user and group
echo "Current User: $_user"
echo "Current Group: $_grp"

sudo mkdir -p /dev/aipc/
sudo chown -R $_user:$_grp /dev/aipc
sudo mkdir -p /data/ace/kvstorage
sudo chown -R $_user:$_grp /data/ace/kvstorage
```

## Run the Hub SDK script

Navigate to the artifacts directory and run the `start_iotmi_sdk.sh`
script. This script launches the hub SDK components in the correct sequence. Review the
following example logs to verify successful startup:

###### Note

Logs for all the components running can be found inside the
`artifacts/logs` folder.

```
hub@hub-293ea release_Oct_17$ ./start_iotmi_sdk.sh
-------Stopping SDK running processes---
DeviceAgent: no process found
------Starting SDK-------
-------Creating logs directory----------
Logs directory created.
-------Verifying Middleware paths-------
All middleware libraries exist
-------Verifying Middleware pre reqs---
AIPC and KVstroage directories exist
-------Starting HubOnboarding-----------
-------Starting MQTT Proxy-----------
-------Starting Event Manager-----------
-------Starting Zigbee Service----------
-------Starting Zwave Service----------
/data/release_Oct_17/middleware/AceZwave/bin /data/release_Oct_17
/data/release_Oct_17
-------Starting CDMB--------------------
-------Starting Agent--------------------
-------Starting Provisioner--------------
-------Checking SDK status---------------
hub         6199  1.7  0.7 1004952 15568 pts/2   Sl+  21:41   0:00 ./iotmi_mqtt_proxy -C /data/aws/iotmi/config/iotmi_config.json
Process 'iotmi_mqtt_proxy' is running.
hub         6225  0.0  0.1 301576  2056 pts/2    Sl+  21:41   0:00 ./middleware/AceCommon/bin/ace_eventmgr
Process 'ace_eventmgr' is running.
hub         6234  104  0.2 238560  5036 pts/2    Sl+  21:41   0:38 ./middleware/AceZigbee/bin/ace_zigbee_service
Process 'ace_zigbee_service' is running.
hub         6242  0.4  0.7 1569372 14236 pts/2   Sl+  21:41   0:00 ./zwave_svc
Process 'zwave_svc' is running.
hub         6275  0.0  0.2 1212744 5380 pts/2    Sl+  21:41   0:00 ./DeviceCdmb
Process 'DeviceCdmb' is running.
hub         6308  0.6  0.9 1076108 18204 pts/2   Sl+  21:41   0:00 ./IoTManagedIntegrationsDeviceAgent
Process 'DeviceAgent' is running.
hub         6343  0.7  0.7 1388132 13812 pts/2   Sl+  21:42   0:00 ./iotmi_lpw_provisioner
Process 'iotmi_lpw_provisioner' is running.
------Successfully Started SDK----
```

## Verify hub

provisioning

Check that the `iot_provisioning_state` field in
`/data/aws/iotmi/config/iotmi_config.json` is set to `PROVISIONED`.
.

## Verify agent

operation

Check the logs file for agent startup messages and successful initialization.

```
tail -f -n 100 logs/agent_logs.txt
```

Example

```
[2024-09-06 02:31:54.413758906][Device_Agent][info] Successfully subscribed to topic: south/bF|gi_044F8821D0193608C8D5BF80858E20A56E3A8490/control
[2024-09-06 02:31:54.513956059][Device_Agent][info] Successfully subscribed to topic: south/bF|gi_044F8821D0193608C8D5BF80858E20A56E3A8490/setup
```

###### Note

Check that the `iotmi.db` database exists in your `artifacts`
directory.

## Verify

LPW-Provisioner operation

Check the logs file for `LPW-Provisioner` startup messages and successful
initialization.

```
tail -f -n 100 logs/provisioner_logs.txt
```

The following code shows an example.

```
[2024-09-06 02:33:22.068898877][LPWProvisionerCore][info] Successfully subscribed to topic: south/bF|gi_044F8821D0193608C8D5BF80858E20A56E3A8490/setup
```
