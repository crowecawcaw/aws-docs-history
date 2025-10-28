Defect Detection App is in preview release and is subject to change.

# Managing station health

The Defect Detection Station App provides information on the health of a station. Use the information
on this page to understand the health of your station and to takes steps towards
solving issues that you encounter.

###### Note

The Station App updates the health information every two seconds.

###### Topics

- [Usage information](#da-managing-system-health-usage "#da-managing-system-health-usage")
- [Getting the log files](#dda-managing-system-health-logs "#dda-managing-system-health-logs")
- [Restarting the Defect Detection Station App](#dda-managing-system-health-restart "#dda-managing-system-health-restart")

## Usage information

The application health provides usage information for the disk volume, CPU, and
memory.

### Disk space

Station App shows the disk space shown for the disk volume where the
`/aws_dda/` folder is mounted. If disk space is low, we recommend the
following:

- Backup and remove images that you have captured in the
  `/aws_dda/image-capture/` folder. These are images that you have
  previously captured for use in a dataset. Each sub folder in
  `/aws_dda/image-capture/` is associated with an image source.
  You can backup the images to a different disk volume, physical drive, or network
  location (if the station is connected to a network). If you still need the
  images to create a dataset, access them from the backup location in the Defect Detection App.
  For more information, see [Creating your datasets](dda-create-dataset.md "dda-create-dataset.md")
- Remove files you have installed that are unrelated to the station
  software. The files must be outside of the `/aws_dda/` folder (if you
  have unrelated files in `/aws_dda/`, move them to a different location). If
  removing these files isn't possible, consider adding another hard drive to the edge device.

### CPU

Station App shows the percentage CPU usage for the edge device that hosts the station. If necessary contact
your provider for further help.

### Memory

Station App shows the percentage memory usage for the edge device that hosts the station.
If high memory usage degrades the performance of the station, consider adding more memory to the device. If necessary
contact your provider for further help.

## Getting the log files

If you are having problems with Defect Detection Station App, your supplier might ask you to provide
the application log files. The log files are a snapshot of the edge device and contain
AWS IoT Greengrass logs, local server logs, and system information (memory, CPU, I/O, processes,
disk).

###### To download the log files

1. Open the Station App on your edge device by opening a browser and navigating to
   `x.x.x.x`:3000. Change `x.x.x.x` to the IP address of
   your edge device.
2. On the left of the application, choose **Application health** and then **Application health overview**.
3. In the **Application logs and restart** section, choose **Download full logs**.
4. Download to the logs to your edge device. Contact your supplier for information about how to use the logs.

## Restarting the Defect Detection Station App

If the Defect Detection Station App isn't working correctly, restarting the Defect Detection Station App might solve the issue. We recommend
checking with your provider first before restarting the Defect Detection Station App.
Restarting the Defect Detection Station App only restarts the Station App software and doesn't reboot the edge device that hosts the station.

###### To restart the Defect Detection Station App

1. Open the Station App on your edge device by opening a browser and navigating to
   `x.x.x.x`:3000. Change `x.x.x.x` to the IP address of
   your edge device.
2. On the left of the application, choose **Application health** and then **Application health overview**.
3. In the **Application logs and restart** section, choose **Restart application**.
4. Wait for the Station App to restart. Restarting the Defect Detection Station App might take a few minutes to complete. During this time, the Defect Detection Station App web page is unavailable.
5. When the Defect Detection Station App is again available, check the alert at the top of the page. If the restart failed, contact your reseller.
