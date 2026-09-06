

# Identifying content in a SMPTE 2110 source
<a name="extract-contents-s2110"></a>

The content in a SMPTE 2110 source is always a set of streams consisting of one video asset, zero or more audio assets, and zero or more captions (ancillary data) assets. Each asset is in its own stream. 

Obtain identifying information from the content provider.




- **Video**
  - **Details:** The video SDP typically contains only one video. / **Information to obtain:** None
  - **Details:** The video SDP might contain more than one video.  / **Information to obtain:** Obtain the media index of the video that you want to extract. 

- **Audio**
  - **Details:** The source might include multiple audio tracks, typically, one for each language. 
  - **Information to obtain:** Obtain the numbers and languages of the tracks. For example, "track 1 is French". 

- **Captions**
  - **Details:** ARIB / **Information to obtain:** You don't need any information. With ARIB captions, MediaLiveextracts all the languages.
  - **Details:** Embedded / **Information to obtain:** Obtain the languages in the channel numbers. For example, "channel 1 is French". 
  - **Details:** Teletext / **Information to obtain:** [If your plan for teletext captions](assess-uss-captions.md) is to convert the captions to a different format, you must obtain the page numbers for the languages that you want to convert. If you plan to pass through the captions as Teletext in the output, you don't need any identifiers.

