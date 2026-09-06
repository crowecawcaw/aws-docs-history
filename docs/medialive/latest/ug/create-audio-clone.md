

# Creating an audio encode by cloning
<a name="create-audio-clone"></a>

You can create one audio encode and clone it among several outputs. The *source* encode could be an encode that you created from scratch, or it could be an encode that was itself created by cloning. For example, create *audio-1*, then clone it to *audio-2*, then clone *audio-2* to *audio-3*.

Note that the procedure for cloning an audio encode is nearly identical to the procedure for cloningg a video encode or captions encode.

1. On the **Create channel** page, find the output group that you [created](creating-a-channel-step4.md). 

1. Under that output group, find the output where you want to set up an audio encode.

1. The output might contain an audio encode that MediaLive has automatically added. If you don't plan to use this audio encode, remove it. Choose the audio encode and choose **Remove audio**.

1. Create a new audio. Choose **Add audio**. A menu appears that includes the option **Use an existing audio description**, followed by a list of the audios that currently exist in the entire channel. Choose the audio that you want to use.

1. Choose the audio encode that you want to use as the source for the new audio encode.

1. On the dialog that appears, choose **Clone the existing settings**. The fields for the encode appear, with the fields showing the values from the source encode.

1. Change any fields, as appropriate.

   Keep in mind that this cloned encode is a new encode instance. If you change fields, you don't affect the source encode.