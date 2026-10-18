

# Using a webcam on Windows, Linux and macOS clients
<a name="using-webcam-native"></a>

**Note**  
The webcam option is available only if the following conditions are met:  
You're authorized to use a webcam in the session.
You have at least one webcam connected to your local computer.
No other users enabled a webcam for use in the session.

## Selecting a webcam
<a name="webcam-select"></a>

Launch the client, connect to the Amazon DCV session, and do one of the following depending on your client.

**Important**  
You can't change the webcam selection while the webcam is in use, or while another client enabled a webcam in the session.

------
#### [ Windows ]

1. Choose the **Settings** icon.

1. Select **Camera**.

1. Select the camera from the drop-down list.  
![Webcam menu option](https://docs.aws.amazon.com/dcv/latest/userguide/images/menu.png)

------
#### [ macOS ]

1. Choose the **Devices** toolbar button.

1. Select the webcam from the **Camera** menu.
**Tip**  
A live preview shows the camera feed when a webcam is selected.  
![Devices toolbar showing the Camera selection menu with live preview.](https://docs.aws.amazon.com/dcv/latest/userguide/images/mac-webcam.png)

**Tip**  
You can also select the webcam from the menu bar. Choose the **Connection** menu, then select **Devices**, **Camera**, and choose the desired device.

------
#### [ Linux ]

1. Click on the **Devices** menu icon from the toolbar at the top.

1. Select the camera from the drop-down list below the **Camera** toggle.  
![Devices menu showing the Camera toggle and a camera selection drop-down.](https://docs.aws.amazon.com/dcv/latest/userguide/images/linux-webcam.png)

------

## Enabling the webcam
<a name="webcam-enable"></a>

After selecting a webcam, enable it. The steps depend on the client used.

------
#### [ Windows ]

Choose the webcam icon on the toolbar.

**Tip**  
You can also use the webcam icon to determine its current state.  


| Toolbar icon | Description | 
| --- | --- | 
|  ![Webcam disabled](https://docs.aws.amazon.com/dcv/latest/userguide/images/disabled.png)  | Your webcam is disabled in the session. Other clients can enable a webcam for use in the session.<br />Click the icon to enable your webcam in the session. If you didn't previously select the webcam to use, the default webcam is used. | 
|  ![Webcam enabled](https://docs.aws.amazon.com/dcv/latest/userguide/images/enabled.png)  | Your webcam is enabled in the session, but it isn't in use. While your webcam is enabled, no other clients that are connected to the session can use a webcam.<br />Click the icon to disable your webcam in the session. | 
|  ![Webcam in use](https://docs.aws.amazon.com/dcv/latest/userguide/images/inuse.png)  | Your webcam is in use by a remote application in the Amazon DCV session. No other clients can enable a webcam while your webcam is in use.<br />Click the icon to disable your webcam in the session. | 

------
#### [ macOS ]

The webcam is enabled automatically when you select a camera.

------
#### [ Linux ]

Turn on the **Camera** toggle.

**Tip**  
When you turn on the **Camera** toggle, a preview of the selected camera appears.

------

## Disabling the webcam
<a name="webcam-disable"></a>

Do one of the following depending on your client.

------
#### [ Windows ]

Choose the webcam icon on the toolbar.

------
#### [ macOS ]

1. Choose the **Devices** toolbar button.

1. Set the **Camera** selection back to **None**.

------
#### [ Linux ]

Turn off the **Camera** toggle.

------

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