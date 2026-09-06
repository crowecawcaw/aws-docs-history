

# Using a webcam on Windows, Linux and macOS clients
<a name="using-webcam-native"></a>

The steps for selecting the camera to use are similar across the Windows, Linux and macOS clients.

**To select the webcam to use**

1. Launch the client and connect to the Amazon DCV session.

1. Do one of the following depending on your client.
   + Windows and Linux clients

     1. Choose the **Settings** icon.

     1. Select **Camera**.

     1. Select the camera from the drop-down list  
![Webcam menu option](http://docs.aws.amazon.com/dcv/latest/userguide/images/menu.png)
   + macOS client

     1. Choose the **DCV Viewer** icon.

     1. Select the **General** tab.

     1. Select the arrow down arrow in the **Select Camera:** field to open a drop-down list of cameras.

     1. Select the camera from the drop-down list  
![Webcam menu option](http://docs.aws.amazon.com/dcv/latest/userguide/images/mac-preferences-general-camera.png)

**Note**  
The camera menu items appears only if you're authorized to use a webcam in the session. If you don't see the camera menu items, you might not be authorized to use a webcam.
You can't change the webcam selection while the webcam is in use, or while another client enabled a webcam in the session.

**To start using your webcam in a session**  
You must first enable it. Use the webcam icon on the toolbar to enable or disable your webcam for use in the session. You can also use the icon to determine its current state. The webcam icon appears on the toolbar only if the following is the case:
+ You're authorized to use a webcam.
+ You have at least one webcam connected to your local computer.
+ No other users enabled a webcam for use in the session.


| Toolbar icon | Description | 
| --- | --- | 
|  ![Webcam disabled](http://docs.aws.amazon.com/dcv/latest/userguide/images/disabled.png)  | Your webcam is disabled in the session. Other clients can enable a webcam for use in the session.<br />Click the icon to enable your webcam in the session. If you didn't previously select the webcam to use, the default webcam is used. | 
|  ![Webcam enabled](http://docs.aws.amazon.com/dcv/latest/userguide/images/enabled.png)  | Your webcam is enabled in the session, but it isn't in use. While your webcam is enabled, no other clients that are connected to the session can use a webcam.<br />Click the icon to disable your webcam in the session. | 
|  ![Webcam in use](http://docs.aws.amazon.com/dcv/latest/userguide/images/inuse.png)  | Your webcam is in use by a remote application in the Amazon DCV session. No other clients can enable a webcam while your webcam is in use.<br />Click the icon to disable your webcam in the session. | 

## Troubleshooting
<a name="troubleshoot"></a>

**Topics**
+ [Webcam doesn't work on Windows 10](#win-10)
+ [Client application says that the webcam is in use](#close-app)

### Webcam doesn't work on Windows 10
<a name="win-10"></a>

Windows 10 provides built-in privacy settings that manage access to the device camera. If you're running Windows 10 on your client computer, these privacy settings might prevent use of the webcam.

**Note**  
If you're connecting to a Windows 2019 Amazon DCV server, you might need to perform these steps on the Amazon DCV server as well.

To modify the privacy settings on your computer, do the following:

1. Choose the search icon on the toolbar.

1. Enter `Settings` and press **Enter**.

1. In the left-hand panel, choose **Camera**.

1. For **Allow apps to access your camera**, switch the toggle to the **On** position.

1. You might need to restart your computer for the changes to take effect.

### Client application says that the webcam is in use
<a name="close-app"></a>

Only one application can use the webcam at a time. If you're using the webcam in multiple applications, first close the applications where it's no longer needed.