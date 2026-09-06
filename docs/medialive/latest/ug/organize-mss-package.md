

# Organize encodes in a Microsoft Smooth output group
<a name="organize-mss-package"></a>

A Microsoft Smooth output group is typically set up as a video ABR stack. A video ABR stack is an output group that contains the following:
+ More than one outputs.

Each output can contain the following:
+ One video encode (rendition). Typically, each video encode is a different resolution.  
+ One or more audio encodes.
+ One or more captions encodes. The captions are always sidecar format.

There are two ways to organize the encodes, depending on whether the audio encodes must be bundled or each in their own rendition. You should have already [obtained this information](identify-dss-video-audio.md) from your downstream system.

**Downstream players that require bundled audio**

Plan for the output group to contain the following:
+ One output for each video encode. This output holds one video encode, all the audio encodes, and all the captions encodes (if the captions are embedded). 

  The same audio encodes will appear in each output. For example, the English and French encodes will appear in the high-resolution output, then the same English and French encodes will appear in the low-resolution output.
+ One output for each captions encode. Sidecar captions always go in their own output.

This diagram illustrates a Microsoft output group with bundled audio.

![Three output groups containing outputs labeled V, A, A, V, A, A, C, and C respectively.](http://docs.aws.amazon.com/medialive/latest/ug/images/output12-ABR-2V-2A-2C.png)


**Downstream players that require separate audio**

Plan for the output group to contain the following:
+ One output for each video encode. This output holds one video and all the captions encodes (if the captions are embedded). 
+ One output for each audio encode.

  The audio encodes might be for different languages, or they might be for different bitrates, or they might be for different languages and bitrates.
+ One output for each captions encode. Sidecar captions always go in their own output.

The arrangement of the audio encodes in this output group is called an *audio rendition group*.

This diagram illustrates a Microsoft Smooth output group with an audio rendition group.

![Output group containing six outputs: two V outputs, two A outputs, and two C outputs.](http://docs.aws.amazon.com/medialive/latest/ug/images/output14-ABR-2V-2Asep-2C.png)
