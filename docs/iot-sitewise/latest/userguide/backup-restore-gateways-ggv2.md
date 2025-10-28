# Back up and restore SiteWise Edge gateways

This topic covers how to restore SiteWise Edge gateways and backup your metric data. If you are
experiencing issues with a broken SiteWise Edge gateway on the same machine and need to
troubleshoot the issue, please read the AWS IoT SiteWise documentation [Troubleshooting SiteWise Edge gateway issues](troubleshooting-gateway.md#troubleshoot-gateway-issues "troubleshooting-gateway.md#troubleshoot-gateway-issues").

###### Note

The guidance covered in this topic is for SiteWise Edge gateways installed on AWS IoT Greengrass V2 version
2.1.0 or higher.

## Daily backups of metric

data

Creating a back up is important, if you would like to transfer or restore the data on
a new machine. Backing up your data greatly reduces the risk of loss of operating data
during a transfer or restoration process.

This section applies to gateways that use the data processing pack. For more
information on the data processing pack, see [Configure an asset model for data
processing on SiteWise Edge](edge-processing.md#process-gateway-data-edge "edge-processing.md#process-gateway-data-edge").

The **influxdb** folder path is as follows:

Linux
``/greengrass/v2`/work/aws.iot.SiteWiseEdgeProcessor/influxdb`

Windows
``C:\greengrass\v2`\work\aws.iot.SiteWiseEdgeProcessor\influxdb`

We recommend that you backup the whole folder with everything underneath it.

We recommend that you periodically backup your metric data from the 1.0 SiteWise Edge to
either an external hard drive or to the AWS cloud.

## Restore a SiteWise Edge gateway

Before attempting to restore a SiteWise Edge gateway, ensure that all edge devices connected
to the gateway are stopped or disconnected.

Use the following procedure to a restore a SiteWise Edge gateway:

1. Use the installation script downloaded when you create SiteWise Edge gateway to
   restore the SiteWise Edge gateway on the new machine. Read the [Installing the SiteWise Edge gateway software on your local device](install-gateway-software-on-local-device.md "install-gateway-software-on-local-device.md")
   procedure to setup the SiteWise Edge gateway.

If you lose or cannot find the installation script, please contact [AWS Customer
Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/"). 2. Once the SiteWise Edge gateway has been installed, log into the [AWS IoT Greengrass console](https://console.aws.amazon.com/greengrass "https://console.aws.amazon.com/greengrass"). 3. To redeploy the components, navigate to **Manage** then under
**AWS IoT Greengrass devices** select **Core
devices**. 4. In the **AWS IoT Greengrass core devices** table select the core device
corresponding to your SiteWise Edge gateway. 5. Once on the device page, open the **Deployments** tab and select your
**Deployment ID**, this will open the **Deployments** page
with your selected ID. 6. Once you are on the **Deployments** page, in the top right
press the **Actions** button, and select the
**Revise** option. to initiate a new deployment. Configure
the deployment. If you would like to keep the deployment as it is, skip to
**Review** and **Deploy**. 7. Wait for the **Deployment Status** to become
`Completed`.

###### Note

It will also take a few minutes for all components on the SiteWise Edge to fully
setup and running.

## Restore AWS IoT SiteWise data

Use the following procedure to restore data on a new machine.

1. Copy the `influxdb` folder to the new machine.
2. Stop the SiteWise EdgeProcessor component, by running the following command in your
   terminal:

Linux
sudo
``/greengrass/v2`/bin/greengrass-cli
component stop -n aws.iot.SiteWiseEdgeProcessor`

Windows
``C:\greengrass\v2`\bin\greengrass-cli
component stop -n aws.iot.SiteWiseEdgeProcesso` 3. Locate the path where you backed up your data, and run the following
command:

Linux
`sudo yes | sudo cp -rf
 <`influxdb_backup_path`>
 `/greengrass/v2/`work/aws.iot.SiteWiseEdgeProcessor/influxdb`

PowerShell
`Copy-Item -Recurse -Force
 <`influxdb_backup_path`>\*
 `C:\greengrass\v2`\work\aws.iot.SiteWiseEdgeProcessor\`

Windows
`robocopy
 <`influxdb_backup_path`>
 `C:\greengrass\v2`\work\aws.iot.SiteWiseEdgeProcessor\
 /E` 4. Restart the SiteWiseEdgeProcessor component:

Linux
`sudo
 `/greengrass/v2`/bin/greengrass-cli
 component restart -n aws.iot.SiteWiseEdgeProcessor`

Windows
``C:\greengrass\v2`\bin\greengrass-cli
component restart -n aws.iot.SiteWiseEdgeProcessor`

## Validate successful backups and

restorations

Use this procedure validate your backed-up data and SiteWise Edge gateway
restorations.

###### Note

This procedure requires that you have installed AWS OpsHub for AWS IoT SiteWise. For more
information see, [Managing SiteWise Edge
gateways using AWS OpsHub for AWS IoT SiteWise](manage-gateways-ggv2.md "manage-gateways-ggv2.md").

1. Open AWS OpsHub for AWS IoT SiteWise.
2. On the SiteWise Edge Gateway **Settings** page, check the status of
   each component listed in the **Components** table. Verify that
   the status color is green and the readout displays **RUNNING**.
3. Validate your past data on the portal dashboard to check that the past data
   and the new data are both properly setup. There will be a downtime between past
   and new data. You should except to see a duration where no data points are
   collected.

If you run into issues with backing up or restoring a SiteWise Edge gateway see the following
troubleshooting topics [Troubleshooting an
AWS IoT SiteWise Edge gateway](troubleshooting-gateway.md "troubleshooting-gateway.md").
