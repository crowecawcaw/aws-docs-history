

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# Motion Image Inserter (Graphic Overlay) in AWS Elemental Server
<a name="motion-graphic-overlay"></a>

The following procedure walks you through how to set up motion graphic overlays. Motion graphic overlays are global, so they appear in all outputs. 

**To set up a motion graphic overlay**

1. Prepare your overlay asset. For more information, see [Requirements for Motion Overlay Files](requirements-for-the-motion-overlay-file.md). 
**Note**  
Motion graphic overlays are in the global processors. They appear on every output of the job and they scale with the video. Therefore, make your overlay size proportional to the size of your input video.

1. In the medium gray **Global Processors** section of the job, choose the **Motion Image Inserter** slider. The **Global Processors** section is just below the dark gray **Input** section.

1. Specify values for the motion image inserter settings. See the following table for information about each field. For information about **Action Time** and **Loop Input**, see [Setting Up When Your Motion Graphic Plays](when-your-motion-overlay-plays.md).    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-server/latest/ug/motion-graphic-overlay.html)