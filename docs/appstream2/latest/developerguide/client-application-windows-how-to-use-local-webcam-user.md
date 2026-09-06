

# Video and Audio Conferencing
<a name="client-application-windows-how-to-use-local-webcam-user"></a>

WorkSpaces Applications real-time audio-video (AV) redirects your local webcam video input to WorkSpaces Applications streaming sessions. That way, you can use your local devices for video and audio conferencing within your WorkSpaces Applications streaming session.



**To use a local webcam and microphone within an WorkSpaces Applications streaming session**

1. Open the WorkSpaces Applications client and connect to a streaming session.

1. In the WorkSpaces Applications toolbar in the top left of your session window, do either of the following: 
   + If the video icon has a diagonal line through it (as shown in the following screenshot), this indicates that the WorkSpaces Applications real-time AV feature is available for use but no webcams are attached to your streaming session. Choose the video icon to attach one or more webcams.   
![Amazon AppStream 2.0 toolbar with video icon showing diagonal line indicating detached webcams.](http://docs.aws.amazon.com/appstream2/latest/developerguide/images/Webcam-available-1.png)
   + If the video icon does not have a diagonal line through it (as shown in the following screenshot), one or more webcams are already attached to your streaming session. Skip this step and proceed to the next step.   
![Amazon AppStream 2.0 toolbar with video icon highlighted.](http://docs.aws.amazon.com/appstream2/latest/developerguide/images/Webcam-attached-2.png)
**Note**  
If the video icon doesn't display in the WorkSpaces Applications toolbar, contact your WorkSpaces Applications administrator. Your administrator might need to perform additional configuration tasks, as described in [Real-Time Audio-Video](feature-support-real-time-av.md).

1. To display the names of the webcams that are attached to your streaming session, choose the downward arrow next to the video icon. If you have more than one webcam (for example, if you have a USB webcam that is connected to your laptop and a built-in webcam), a check mark appears next to the name of the webcam that is selected for use for video conferencing within your streaming session.  
![Dropdown menu showing Webcam 1 selected with a check mark and Webcam 2 as an option.](http://docs.aws.amazon.com/appstream2/latest/developerguide/images/Webcam1-selected-3.png)

1. To use the selected webcam for video conferencing within your WorkSpaces Applications streaming session, start the video conferencing application that you want to use. When the webcam is active (being used for video conferencing within your streaming session), the video icon is red.  
![Amazon AppStream 2.0 toolbar with red video icon and dropdown menu showing Webcam 1 selected.](http://docs.aws.amazon.com/appstream2/latest/developerguide/images/Webcam1-selected-cameras-streaming-4.png)

1. To enable the microphone, choose the microphone icon.

**Note**  
If you have more than one webcam and want to change the one that you use for streaming within an WorkSpaces Applications session, you must first detach your webcams from the session. For more information, see the next procedure.

**To change the local webcam to use within an WorkSpaces Applications streaming session**

1. Within your WorkSpaces Applications streaming session, in the WorkSpaces Applications toolbar in the top left of your session window, do either of the following: 
   + If the video icon does not have a diagonal line through it (as shown in the following screenshot), this indicates that the WorkSpaces Applications real-time AV feature is available for use and that webcams are still attached to your streaming session. Choose the video icon to detach the webcams.  
![Amazon AppStream 2.0 toolbar with video icon highlighted.](http://docs.aws.amazon.com/appstream2/latest/developerguide/images/Webcam-attached-2.png)
   + If the video icon has a diagonal line through it (as shown in the following screenshot), your webcams are already detached from your streaming session. Skip this step and proceed to the next step.  
![Amazon AppStream 2.0 toolbar with video icon showing diagonal line indicating detached webcams.](http://docs.aws.amazon.com/appstream2/latest/developerguide/images/Webcam-available-1.png)

1. Display the names of your webcams by choosing the downward arrow next to the video icon, then select the name of the webcam that you want to use.
**Note**  
You must select the name of the webcam you want to use. If you select the check mark next to the name of the webcam you want to use, the webcam won't change.  
![Amazon AppStream 2.0 toolbar with Webcam 2 selected from webcam dropdown menu.](http://docs.aws.amazon.com/appstream2/latest/developerguide/images/Webcam2-selected-5.png)

1. Choose the video icon to reattach the webcams to your WorkSpaces Applications streaming session.   
![Video icon highlighted in the Amazon AppStream 2.0 toolbar with Webcam 2 selected in dropdown.](http://docs.aws.amazon.com/appstream2/latest/developerguide/images/Webcam-2-selected-cameras-reattached-6.png)