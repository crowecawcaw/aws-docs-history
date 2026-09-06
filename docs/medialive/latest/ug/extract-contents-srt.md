

# Identifying content in an SRT source
<a name="extract-contents-srt"></a>

The content in an SRT input is always a transport stream (TS). The TS is made up of one program (SPTS) or multiple programs (MPTS). Each program contains a combination of video, a combination of audio, and optional captions. 

Obtain identifying information from the content provider.




- **Video**
  - **Details:** The source content might contain more than one video rendition.If two video renditions are identical, look at the audios and captions in each program. Those might be different, in which case you should choose the video rendition that contains the audio or captions formats that you want.
  - **Information to obtain:** Obtain the PID of the video rendition that you want.

- **Audio**
  - **Details:** You must work with the audio that is in the same rendition as the video that you chose.
  - **Information to obtain:** Obtain the PIDs or three-character language codes of the audio languages that you want.We recommend that you obtain the PIDs for the audio assets. They are a more reliable way of identifying an audio asset. 

- **Captions**
  - **Details:** Embedded / **Information to obtain:** Obtain the languages in the channel numbers. For example, "channel 1 is French". 
  - **Details:** Object-style captions, for example, DVB-Sub / **Information to obtain:** Obtain the PIDs of the captions languages that you want. 

