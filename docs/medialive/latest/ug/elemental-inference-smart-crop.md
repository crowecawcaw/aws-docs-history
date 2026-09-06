

# Smart cropping video using Elemental Inference
<a name="elemental-inference-smart-crop"></a>

In an AWS Elemental MediaLive channel, you can enable the smart crop feature in order to set up one or more outputs with an aspect ratio that is different from the source aspect ratio. A typical use case is to create vertical video from a landscape video. 

MediaLive uses AWS Elemental Inference to crop the video frames to an aspect ratio that you specify. 

Elemental Inference analyzes the source content to detect the region of interest. For example, consider the source video of a soccer game. Elemental Inference infers the location of the region of interest when the ball is moving. Elemental Inference will typically infer that the soccer ball and the players around the ball are that region of interest. 

MediaLive obtains information about the region of interest from Elemental Inference and crops and scales the video. 

**Topics**
+ [Get ready](smart-crop-get-ready.md)
+ [Setting up with the MediaLive console](smart-crop-console-create.md)
+ [Viewing the smart crop setup](smart-crop-view.md)
+ [Modifying smart crop using the MediaLive console](smart-crop-modify-console.md)
+ [Disabling smart crop](smart-crop-disable-console.md)
+ [Monitoring smart crop activity](smart-crop-monitor.md)