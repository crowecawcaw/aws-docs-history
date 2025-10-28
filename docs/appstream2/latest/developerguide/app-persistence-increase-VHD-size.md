# Increase the Size of the

Application Settings VHD

The default VHD maximum size is 1 GB for Elastic fleets and 5GB for Always-On and
On-Demand fleets. If a user requires additional space for application settings, you
can download the applicable application settings VHD to a Windows computer to expand
it. Then, replace the current VHD in the S3 bucket with the larger one. Do not do
this when the user has an active streaming session.

###### Note

To reduce the physical size of the virtual hard disk (VHD), clear the recycle
bin before ending a session. This also reduces upload and download times, and
improves the overall user experience.

###### To increase the size of the application settings VHD

###### Note

The full VHD must be downloaded before a user can stream applications.
Increasing the size of an application settings VHD can increase the time it
takes for users to start application streaming sessions.

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the **Bucket name** list, choose the S3 bucket that
   contains the application settings VHD to expand.
3. Locate and select the folder that contains the VHD. For information about
   how to navigate the S3 bucket folder structure, see _Amazon S3
   Bucket Storage_ earlier in this topic.

When you select the folder, the settings VHD and associated metadata file
display. 4. Download the Profile.vhdx file to a directory on your Windows computer. Do
not close your browser after the download completes, because you'll use the
browser again later to upload the expanded VHD. 5. To use Diskpart to increase the size of the VHD to 7 GB, open the command
prompt as an administrator, and type the following commands.

`diskpart`

`select vdisk
 file="C:\path\to\application\settings\profile.vhdx"`

`expand vdisk maximum=7000` 6. Then, type the following Diskpart commands to find and attach the VHD, and
display the list of volumes:

`select vdisk
 file="C:\path\to\application\settings\profile.vhdx"`

`attach vdisk`

`list volume`

In the output, make note of the volume number with the label
"AppStreamUsers". In the next step, you select this volume so that you can
enlarge it. 7. Type the following command:

`select volume ###`

where ### is the number in the list volume output. 8. Type the following command:

`extend` 9. Type the following commands to confirm that the size of the partition on
the VHD increased as expected (2 GB in this example):

`diskpart`

`select vdisk
 file="C:\path\to\application\settings\profile.vhdx"`

`list volume` 10. Type the following command to detach the VHD so that it can be
uploaded:

`detach vdisk` 11. Return to your browser with the Amazon S3 console, choose
**Upload**, **Add files**, and then
select the enlarged VHD. 12. Choose **Upload**.
After the VHD is uploaded, the next time the user streams from a fleet on which
application settings persistence is enabled with the applicable settings group, the
larger application settings VHD is available.
