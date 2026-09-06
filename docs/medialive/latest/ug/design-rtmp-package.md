

# Organize encodes in an RTMP output group
<a name="design-rtmp-package"></a>

An RTMP output group can contain the following:
+ One or more outputs.

Each output can contain the following:
+ One video encode.
+ Zero or one audio encodes.
+ Zero or one captions encodes.

This diagram illustrates an RTMP output group that contains one output where the captions are embedded in the video encode.

![Output group containing output with video embedded captions and audio.](http://docs.aws.amazon.com/medialive/latest/ug/images/output1-non-abr-Ve-A.png)


This diagram illustrates an RTMP output group that contains one output with object-style captions. 

![Output group containing three outputs labeled V, A, and C.](http://docs.aws.amazon.com/medialive/latest/ug/images/output2-non-abr-VAC.png)
