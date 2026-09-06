

# Organize encodes in an SRT output group
<a name="design-srt-package"></a>

An SRT output group can contain the following:
+ One or more outputs.

Each output contains the following:
+ One video encode.
+ One or more audio encodes.
+ Zero or more captions encodes. The captions are either embedded or object-style captions. 

Each output represents one SPTS. Each output (SPTS) has its own destination.

This diagram illustrates an SRT output group with one output. The captions are embedded in the video encode.

![Output group containing one output with embedded video and two audio outputs.](http://docs.aws.amazon.com/medialive/latest/ug/images/output3-nonABR-Ve-2A.png)


This diagram illustrates an SRT output group with one output. The captions are object-style captions.

![Output group labeled Output containing five elements: V, A, A, C, and C in oval shapes.](http://docs.aws.amazon.com/medialive/latest/ug/images/output4-nonABR-V-2A-2C.png)
