# Deploy Hub SDK with systemd

###### Important

Follow the `readme.md` in the `hubSystemdSetup` directory of the release.tgz file
for the latest updates.

This section describes the scripts and processes for deploying and configuring services on a Linux-based hub device.

## Overview

The deployment process consists of two main scripts:

- `copy_to_hub.sh`: Runs on the host machine to copy necessary files to the hub
- `setup_hub.sh`: Runs on the hub to configure the environment and deploy services

Additionally, `systemd/deploy_iotshd_services_on_hub.sh` handles process bootstrap sequence and process permission management, and is automatically triggered by `setup_hub.sh`.

## Prerequisites

The listed prerequistes are required for successful deployment.

- systemd service is available on the hub
- SSH access to the hub device
- Sudo privileges on the hub device
- `scp` utility installed on host machine
- `sed` utility installed on host machine
- unzip utility installed on host machine

## File structure

The file structure is designed to facilitate the organization and management of its
various components, enabling efficient access and navigation of the content.

```
hubSystemdSetup/
├── README.md
├── copy_to_hub.sh
├── setup_hub.sh
├── iotshd_config.json  # Sample configuration file
├── local_certs/  # Directory for DHA certificates
└── systemd/
    ├── *.service.template  # Systemd service templates
    └── deploy_iotshd_services_on_hub.sh
```

In the SDK release tgz file, the overall file structure is:

```
IoT-managed-integrations-Hub-SDK-aarch64-v1.0.0.tgz
├──package/
    ├──greengrass/
        ├──artifacts/
        ├──recipes/
    ├──hubSystemdSetup/
        ├── REAME.md
        ├── copy_to_hub.sh
        ├── setup_hub.sh
        ├── iotshd_config.json  # Sample configuration file
        ├── local_certs/  # Directory for DHA certificates
        └── systemd/
            ├── *.service.template  # Systemd service templates
            └── deploy_iotshd_services_on_hub.sh
```

## Initial setup

### Extract the SDK package

```
tar -xzf managed-integrations-Hub-SDK-vVersion-linux-aarch64-timestamp.tgz
```

Navigate to the extracted directory and prepare the package:

```
# Create package.zip containing required artifacts
zip -r package.zip package/greengrass/artifacts
# Move package.zip to the hubSystemdSetup directory
mv package.zip ../hubSystemdSetup/
```

### Add device configuration files

Follow the two steps listed to create the device configuration files, and copy them to the hub.

1. [Add device configuration files](managedintegrations-sdk-v2-cookbook-hubsetup.md#managedintegrations-sdk-v2-cookbook-genconfig "managedintegrations-sdk-v2-cookbook-hubsetup.md#managedintegrations-sdk-v2-cookbook-genconfig") to create the device configuration files
   needed. The SDK uses this file for its function.
2. [Copy the configuration files](managedintegrations-sdk-v2-cookbook-hubsetup.md#managedintegrations-sdk-v2-cookbook-config-contents "managedintegrations-sdk-v2-cookbook-hubsetup.md#managedintegrations-sdk-v2-cookbook-config-contents") to copy the created configuration files to
   the hub.

## Copy files to the hub

Run the deployment script from your host machine:

```
chmod +x copy_to_hub.sh
./copy_to_hub.sh hub_ip_address package_file
```

###### Example

```
./copy_to_hub.sh 192.168.50.223 ~/Downloads/EAR3-package.zip
```

This copies:

- The package file (renamed to package.zip on the hub)
- Configuration files
- Certificates
- Systemd service files

## Set up hub

After the files are copied, SSH into the hub and run the setup script:

```
ssh hub@hub_ip
chmod +x setup_hub.sh
sudo ./setup_hub.sh
```

### User and group configurations

By default, we use the user **hub** and group **hub** for the SDK components.
There are multiple ways to configure them:

- Use a custom user/group:

```
sudo ./setup_hub.sh --user=USERNAME --group=GROUPNAME
```

- Create them manually before running the setup script:

```
sudo groupadd -f GROUPNAME
sudo useradd -r -g GROUPNAME USERNAME
```

- Add the commands in `setup_hub.sh`.

## Manage services

To restart all the services, run the following script from hub:

```
sudo /usr/local/bin/deploy_iotshd_services_on_hub.sh
```

The setup script will create necessary directories, set appropriate permissions, and deploy services automatically.
If you're not using SSH/SCP, you must modify `copy_to_hub.sh` for your specific deployment method.
Ensure all certificate files and configurations are properly set up before deployment.
