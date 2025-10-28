# Step 4: Download and post the SDP file

If your organization doesn't use NMOS, you must make sure that the downstream system
(the SMPTE 2110 receiver) can access them:

- If the location is accessible and doesn't need user credentials, provide the
  downstream system operator with the full path so that they can download the SDP
  files.
- If the location where the files are stored isn't accessible from the public
  internet, you must download the files and put them on a location that is
  accessible.
  If your organization uses NMOS, skip this step.

**Location and syntax of the files**

Elemental Live puts the SDP files on the HTTP root folder:

`/opt/elemental_se/web/public/`

The files are named as follows:

`SmpteSt2110Output.LiveEvent_<event ID>.OutputGroup_<output
 group>_2110-<ID>_<media>_<unique number on node>.sdp`

For example:

`SmpteSt2110Output.LiveEvent_123.OutputGroup_curling_smpte_2110.2110-20_video_473.sdp`

The key pieces of information are:

- `123` – The number for this event, unique on this Elemental Live node.
- `curling` – The name you assigned to this output group.
- `2110-20_video` – Identifies this file type. In this example, it's an
  SDP file for uncompressed video.
- `473` – A number that is unique for this Elemental Live node.

###### To locate and download the SMPTE 2110 SDP file

1. From your output, select **View Logs**.
2. Select the eme log to view its contents.
3. Within the eme log, search for `Writing SDP file to`. You will find a
   line for the video, and a line for the audio. Copy the portions that follow
   `/opt/elemental_se/web/public/` for each line. These are your SDP
   files. For example:

`SmpteSt2110Output.LiveEvent_123.OutputGroup_curling_smpte_2110.2110-20_video_473.sdp` 4. If you don't know the IP address of your Elemental Live appliance, find it now. In the
Elemental Live web interface, choose **Settings**. (Don't choose
**Input Devices** or **Routers** from the
submenu).

On the **Settings** page, choose the **Network**
tab, then choose the **Current Settings** tab. Make a note of the IP
addresses in the **Domain Name Servers** section. 5. Download the file using a suitable tool to connect from a computer that is on your
network to the Elemental Live appliance. For example:

    * On a PC, use Windows Share protocol. Connect to:


    `\\<IP address>\opt\elemental_se\web\public\`
    * On a Mac, use Samba. Connect to:


    `smb://<IP address>/opt/elemental_se/web/public/`

6. Download the files. Then put the files on an HTTP server that you know the
   receiver can access.
