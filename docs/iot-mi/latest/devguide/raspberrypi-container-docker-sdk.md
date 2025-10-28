# Managed integrations Hub SDK Docker container on Raspberry Pi

###### Note

This implementation of AWS IoT Hub SDK on Raspberry Pi is a demonstration project
intended for learning and testing purposes only and is not intended to be used in production environments.
For the purposes of this demo, set the following configurations for development ease:

**AWS credentials storage**: For demo purposes only, credentials and certificates are
stored in an accessible location for easier testing and development.
Production environments must use secure storage solutions like AWS Secrets Manager, or
Systems Manager Parameter Store. They must implement encryption at rest, and follow AWS IoT security guidelines.

**Container privileges**: The demo runs with elevated privileges to allow unrestricted access to host resources
and simplify development workflows. In production, containers should operate with minimal required privileges.

**Network bridge configuration**: The demo uses a network bridge configuration that exposes internal network traffic
for easier debugging and monitoring. In production environments, implement proper network isolation and segmentation to
prevent unauthorized access to internal network traffic.

**USB device permissions**: Unrestricted USB device access is enabled to facilitate easy
connection of development peripherals and testing devices. For production, implement strict USB device controls and validation to prevent device spoofing attacks.

These configurations enable straightforward testing and must notcbe used in production environments. When deploying to production,
please follow security best practices to prevent host system compromise and unauthorized access to credentials.

## Prerequisites

The following prerequisites are required to for the docker container.

- Download and install [Raspberry Pi imager](https://www.raspberrypi.com/software/ "https://www.raspberrypi.com/software/").
- Obtain an [SD Card](https://www.amazon.com/dp/B0CWPPDS3D?ref=ppx_yo2ov_dt_b_fed_asin_title "https://www.amazon.com/dp/B0CWPPDS3D?ref=ppx_yo2ov_dt_b_fed_asin_title").
- Set up a [Raspberry Pi 5 with 2.4Ghz 64-bit quad-core CPU (8GB RAM)](https://www.amazon.com/CanaKit-Raspberry-Starter-Kit-PRO/dp/B0CRSNCJ6Y/ "https://www.amazon.com/CanaKit-Raspberry-Starter-Kit-PRO/dp/B0CRSNCJ6Y/").
- Connect a [Sonoff Zigbee USB Dongle](https://www.amazon.com/Plus-ZBDongle-Interface-Pre-Installed-Coordinated-Zigbee2MQTT/dp/B0B6P22YJC/ "https://www.amazon.com/Plus-ZBDongle-Interface-Pre-Installed-Coordinated-Zigbee2MQTT/dp/B0B6P22YJC/").
- [Flash firmware to Sonoff Zigbee USB dongle](supported-raspberry.md#sonoff-zigbee-firmware-flashing "supported-raspberry.md#sonoff-zigbee-firmware-flashing").
- Connect a [Silicon Labs SLUSB001A Dongle](https://www.digikey.com/en/products/detail/silicon-labs/SLUSB001A/9867108 "https://www.digikey.com/en/products/detail/silicon-labs/SLUSB001A/9867108").
- [Sign up for an AWS account](setting-up.md#sign-up-for-aws "setting-up.md#sign-up-for-aws").
- Install the latest version of [AWS CLI from the
  Managed integrations AWS CLI Command Reference](../../../cli/latest/reference/iot-managed-integrations.md "../../../cli/latest/reference/iot-managed-integrations.md").
- SSH access to the Raspberry Pi with IP address or hostname.

## Use Managed integrations Hub SDK Docker container on Raspberry Pi

1. Download [Managed integrations Raspberry Pi Hub SDK Docker](https://d2no7dt1utuyzo.cloudfront.net/IotMI-HubSDK-RaspberryPi/1.0.0/IotMI-HubSDK-Docker-v1.0.0.tar.gz "https://d2no7dt1utuyzo.cloudfront.net/IotMI-HubSDK-RaspberryPi/1.0.0/IotMI-HubSDK-Docker-v1.0.0.tar.gz").
2. Copy the file to the Raspberry Pi using SCP:

```
scp ~/path/to/IotMI-HubSDK-Docker-v1.0.0.tar.gz [username]@raspberrypi.local:~
```

3. Connect to the Raspberry Pi via SSH:

```
ssh hub123456@raspberrypi.local
```

4. Install Docker if not present:

```
# Install Docker
cd
curl -fsSL https://get.docker.com | sudo sh

# Add your user to docker group
sudo usermod -aG docker $USER
exit # exit ssh

# Log in again
```

5. Install Docker Compose if not present:

```
# Install Docker Compose
sudo apt-get update
sudo apt-get install -y docker-compose-plugin
```

6. Extract the Hub SDK files:

```
# Navigate to the home directory
cd

# Extract the hub-docker.tar.gz file
tar -xzf IotMI-HubSDK-Docker-v1.0.0.tar.gz
```

7. Navigate to the hub-docker directory:

```
cd IotMI-HubSDK-Docker
```

8. Complete [Hub onboarding setup](managedintegrations-sdk-v2-cookbook-hubsetup.md "managedintegrations-sdk-v2-cookbook-hubsetup.md") to configure authentication and settings.

###### Note

You must be on `YUL` or `DUB` region to do this step. 9. Start the Docker container:

```
# The first time it's called, it will build the container
docker compose up -d
docker compose logs -f
```

**Expected output:**

```
[+] Running 1/1
 ✔ Container iotmi-hubsdk-docker-hubsdk-1  Started
hubsdk-1  | -\-\-\-\-\-\-Checking USB dongles-\-\-\-\-\-\-\-\-\-\-\-\-
hubsdk-1  | -\-\-\-\-\-\-Stopping SDK running processes-\-\-
hubsdk-1  | iotmi_mqtt_proxy: no process found
hubsdk-1  | ace_eventmgr: no process found
hubsdk-1  | ace_zigbee_service: no process found
hubsdk-1  | zwave_svc: no process found
hubsdk-1  | iotmi_cdmb: no process found
hubsdk-1  | iotmi_device_agent: no process found
hubsdk-1  | iotmi_lpw_provisioner: no process found
hubsdk-1  | iotmi_log_daemon: no process found
hubsdk-1  | -\-\-\-\-\-\-Starting Hub SDK-\-\-\-\-\-\-\-\-\-\-\-\-
hubsdk-1  | -\-\-\-\-\-\-Creating logs directory-\-\-\-\-\-\-\-\-\-
hubsdk-1  | Logs directory created.
hubsdk-1  | -\-\-\-\-\-\-Verifying Middleware paths-\-\-\-\-\-\-
hubsdk-1  | All middleware libraries exist
hubsdk-1  | -\-\-\-\-\-\-Verifying Middleware pre reqs-\-\-
hubsdk-1  | AIPC and KVstroage directories exist
hubsdk-1  | -\-\-\-\-\-\-Starting HubOnboarding-\-\-\-\-\-\-\-\-\-\-
hubsdk-1  | -\-\-\-\-\-\-Starting MQTT Proxy-\-\-\-\-\-\-\-\-\-\-
hubsdk-1  | -\-\-\-\-\-\-Staring Log Daemon-\-\-
hubsdk-1  | -\-\-\-\-\-\-Starting Event Manager-\-\-\-\-\-\-\-\-\-\-
hubsdk-1  | -\-\-\-\-\-\-Starting Zigbee Service-\-\-\-\-\-\-\-\-\-
hubsdk-1  | -\-\-\-\-\-\-Starting Zwave Service-\-\-\-\-\-\-\-\-\-
hubsdk-1  | /data/aws/iotmi/middleware/AceZwave/bin /data/aws/iotmi
hubsdk-1  | /data/aws/iotmi
hubsdk-1  | -\-\-\-\-\-\-Starting CDMB-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-
hubsdk-1  | -\-\-\-\-\-\-Starting Agent-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-
hubsdk-1  | -\-\-\-\-\-\-Starting Provisioner-\-\-\-\-\-\-\-\-\-\-\-\-\-
hubsdk-1  | -\-\-\-\-\-\-Checking SDK status-\-\-\-\-\-\-\-\-\-\-\-\-\-\-
hubsdk-1  | root         105  0.2  0.2 1093488 16608 ?       Sl   20:51   0:00 ./iotmi_mqtt_proxy -C /data/aws/iotmi/config/iotmi_config.json
hubsdk-1  | Process 'iotmi_mqtt_proxy' is running.
hubsdk-1  | root         183  0.0  0.0 236272  3152 ?        Sl   20:51   0:00 ./middleware/AceCommon/bin/ace_eventmgr
hubsdk-1  | Process 'ace_eventmgr' is running.
hubsdk-1  | root         190 12.0  0.1 319264  8352 ?        Sl   20:51   0:04 ./middleware/AceZigbee/bin/ace_zigbee_service
hubsdk-1  | Process 'ace_zigbee_service' is running.
hubsdk-1  | root         200  0.0  0.1 1365792 12480 ?       Sl   20:51   0:00 ./zwave_svc
hubsdk-1  | Process 'zwave_svc' is running.
hubsdk-1  | root         233  0.0  0.0 1198704 5760 ?        Sl   20:51   0:00 ./iotmi_cdmb
hubsdk-1  | Process 'iotmi_cdmb' is running.
hubsdk-1  | root         268  0.2  0.2 2017424 21968 ?       Sl   20:51   0:00 ./iotmi_device_agent
hubsdk-1  | Process 'iotmi_device_agent' is running.
hubsdk-1  | root         311  0.1  0.1 1523072 13008 ?       Sl   20:51   0:00 ./iotmi_lpw_provisioner
hubsdk-1  | Process 'iotmi_lpw_provisioner' is running.
hubsdk-1  | root         132  0.0  0.0 875024  7232 ?        Sl   20:51   0:00 ./iotmi_log_daemon
hubsdk-1  | Process 'iotmi_log_daemon' is running.
hubsdk-1  | -\-\-\-\-\-Successfully Started Hub SDK-\-\-\-
```

After successfully starting the Hub SDK, proceed with device onboarding and management at
[User guided setup to onboard and operate
devices](managedintegrations-sdk-v2-cookbook-ugs.md "managedintegrations-sdk-v2-cookbook-ugs.md").

###### Note

- To access the Docker container bash shell, run the following command:

```
docker compose exec hubsdk bash
```

- To restart the container after reboot, run the following command:

```
docker compose up -d
```

- To update the Hub SDK, replace binaries in the following folder:

```
hub-docker/iotmi
```

- To safely restart the container while preserving data, do:

```
docker compose down
docker compose up -d
docker compose logs -f
```
