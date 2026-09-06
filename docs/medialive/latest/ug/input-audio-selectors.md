

# Input settings—Audio selectors
<a name="input-audio-selectors"></a>

If you want to extract audio from the input, this section is required. You create one or more audio selectors to identify the audio asset to extract. Typically, you identify different languages from the input, but you could also extract different audio codecs (such as AAC and Dolby).

You can create a maximum of 20 audio selectors in one channel.

**To identify the audio to extract**

1. Decide if you need to create any audio selectors. When you planned the channel, you should have [identified the audio assets](channel-map-output-source.md) that you need to extract from this input. 

   The following table specifies whether you need to create an audio selector in order to extract that audio. In the table, find your input type and read across the row for guidance.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/medialive/latest/ug/input-audio-selectors.html)

   If the input contains more than one audio asset and you don't create a selector, MediaLive selects the first audio it encounters.

1. Choose **Add audio selector** once for each audio that you want to extract from the input.

   If you are creating a channel with multiple inputs, then you must extract the same audio languages from every input. For example, you must extract English and Spanish audio from every input. 

1. In **Audio selector name**, enter a name that describes the audio that you are extracting.

   If you are creating a channel with multiple inputs, then you must assign the identical name to the selector in every input. For example, create a selector called **audio-english** in every input, and a selector called **audio-spanish** in every input.

1. In **Selector Settings**, choose the appropriate type of selector, then complete the field that appears.
   + If you choose **Audio track selection**, then choose **Add tracks** to add a selector for each track you want to extract. 
   + If you choose **Audio pid selection**, enter the PID for the audio asset.
   + If you choose **Audio language selection**, enter the three-letter ISO code for the language of the audio asset to extract. Then complete **Language selection policy**. 