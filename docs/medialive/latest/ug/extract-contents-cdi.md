

# Identifying content in a CDI source
<a name="extract-contents-cdi"></a>

The content in a CDI source always consists of uncompressed video, uncompressed audio, and captions. 

Obtain identifying information from the content provider.




- **Video**
  - **Description:** You don't need identifying information. MediaLive always extracts the first video that it encounters.
  - **Information to obtain:** None

- **Audio**
  - **Description:** The source might include multiple audio tracks, typically one for each language. 
  - **Information to obtain:** Obtain the numbers and languages of the tracks. For example, "track 1 is French". 

- **Captions**
  - **Description:** ARIB / **Information to obtain:** You don't need any information. With ARIB captions, MediaLiveextracts all the languages.
  - **Description:** Embedded / **Information to obtain:** Obtain the languages in the channel numbers. For example, "channel 1 is French".
  - **Description:** Teletext / **Information to obtain:** [If your plan for teletext captions](assess-uss-captions.md) is to convert the captions to a different format, you must obtain the page numbers for the languages that you want to convert. If you plan to pass through the captions as Teletext in the output, you don't need any identifiers.

