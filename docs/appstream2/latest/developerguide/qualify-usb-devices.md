# Qualify USB Devices for Use with Streaming

Applications

There are two methods for specifying which USB devices your users can redirect
into their AppStream 2.0 streaming instances:

###### Note

USB redirection is currently only supported on Windows AppStream 2.0 streaming
instances. It is not supported on the macOS client.

- You can create the USB device filter strings within the configuration file
  saved on an image. This method can only be used with Always-On and On-Demand
  fleets.
- You can specify USB device filter strings when you create the fleet,
  either with the AWS Management Console or with the
  `CreateFleet` API. For detailed information about these
  strings, see the section below. This method can only be used with Elastic
  fleets.
  You can create a file on your AppStream 2.0 image that specifies which USB devices a user
  can make available for their streaming applications. To qualify your users' USB
  devices so that the devices can be used with streaming applications, perform these
  steps.

###### Note

For security reasons, only qualify USB devices from approved trusted sources.
Qualifying all generic devices or classes of devices might allow unapproved
devices to be used with your streaming applications.

1. If you haven't already done so, install the AppStream 2.0 client. For
   information, see [Install and Configure the AppStream 2.0 Client](install-configure-client.md "install-configure-client.md").
2. Connect the USB device that you want to qualify to your computer.
3. Navigate to
   **C:\Users\<logged-in-user>\AppData\Local\AppStreamClient**,
   and double-click **dcvusblist.exe**.
4. In the **DCV - USB devices** dialog box, the list of USB
   devices that are connected to your local computer displays. The
   **Filter** column displays the filter string for every
   USB device. Right-click the list entry for a USB device that you want to
   enable, and choose **Copy filter string**.
5. On your desktop, choose the Windows **Start** button, and
   search for Notepad. Double-click **Notepad** to open a new
   file, copy the filter string to the file, and save it. Later, you'll use the
   filter string to qualify the USB device.
6. Launch a new image builder. For more information, see [Launch an Image Builder to Install and Configure Streaming Applications](tutorial-image-builder-create.md "tutorial-image-builder-create.md").
7. After your image builder is in the **Running** state,
   perform the following steps to create a streaming URL and connect to the
   image builder by using the AppStream 2.0 client.
   1. With your image builder selected in the list, choose
      **Actions**, **Create streaming
      URL**.
   2. In the **Create streaming URL** dialog box,
      choose **Copy link**, and copy and paste the web
      address into a separate file for later use. You'll use this URL to
      reconnect to the image builder in step 12.
   3. Choose **Launch in Client**.
   4. If the **Launch Application** dialog box opens
      and prompts you to choose the application to use when opening the
      link, choose **Amazon AppStream**, **Open
      link**. To prevent this dialog box from displaying the
      next time you perform this step to connect to an image builder,
      select the **Remember my choice for amazonappstream
      links** check box.
   5. If the AppStream 2.0 client displays links to the AWS Customer
      Agreement, AWS Service Terms, and the AWS Privacy Notice, and
      third-party notices, review this information, and then choose
      **Finish**.
   6. If the client sign-in page is displayed, the web address field is
      prepopulated with the streaming URL. Choose
      **Connect**.
   7. If prompted, log in to the image builder as Administrator.

8. After you are connected to the image builder, if your USB device requires
   you to install drivers before you use it, download and install the drivers
   on the image builder. For example, if you use the Connexion 3D mouse, you
   must download and install the required Connexion drivers on the image
   builder.
9. On your image builder desktop, choose the Windows
   **Start** button, and search for Notepad. Right-click
   **Notepad**, and choose **Run as
   Administrator**.
10. Choose **File**, **Open**, and open the
    following file:
    `C:\ProgramData\Amazon\Photon\DCV\usb_device_allowlist.txt`.
    You can also allow an entire category of devices or all devices from a
    specific manufacturer by using wildcard expressions in the
    `usb_device_allowlist.txt` file.
11. Copy the filter string from your local computer to the image builder. The
    filter string for a specific USB device is a comma-separated string of the
    following fields: **Name**, **Base
    Class**, **SubClass**,
    **Protocol**, **ID Vendor**,
    **ID Product**, **Support Autoshare**,
    and **Skip Reset**. For detailed information about these
    strings, see [Working with USB Device Filter
    Strings](USB-device-filter-strings.md "USB-device-filter-strings.md").
12. Disconnect from your image builder, restart it, and reconnect to it by
    using the AppStream 2.0 client. To do so, open the AppStream 2.0 client and paste the
    streaming URL that you created in step 7 into the client sign-in web address
    field, and choose **Connect**.
13. On the image builder, test your USB device to confirm that it works as
    expected.
14. Before your users can use the USB device in an AppStream 2.0 session, they must
    first share the device with their session. For guidance that you can provide
    your users to help them perform this task, see [USB Devices](client-application-windows-how-to-share-usb-devices-user.md "client-application-windows-how-to-share-usb-devices-user.md").
15. If the USB device works with the image builder as expected, create an
    image. For more information, see [Tutorial: Create a Custom AppStream 2.0 Image by Using the
    AppStream 2.0 Console](tutorial-image-builder.md "tutorial-image-builder.md").
16. After you finish creating the image, update your AppStream 2.0 fleet to use the
    new image.
