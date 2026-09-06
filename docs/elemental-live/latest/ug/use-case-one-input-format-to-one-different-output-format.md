

# Use case 2: One input format converted to one different output format
<a name="use-case-one-input-format-to-one-different-output-format"></a>

This example shows how to implement [the second use case](typical-scenarios.md#use-case-one-input-format-to-different-output-formats) from the typical scenarios. The input includes two captions languages, and the single output will convert those captions. For example, the input has embedded captions in German and French. You want to produce a UDP output with both captions converted to DVB-Sub, plus one video and one audio. 

![Diagram showing input captions in German and French converted to DVB-Sub output formats.](http://docs.aws.amazon.com/elemental-live/latest/ug/images/captions_INembed_OUTdvb_udp_result.png)


## Event setup
<a name="procedure3"></a>

**To convert the input format to another on output**

1. On the web interface, on the **Event** screen, for **Input Settings**, choose **Add captions selector** twice, to create Captions selector 1 (for German) and Captions selector 2 (for French). In both cases, set **Selector settings** to **Embedded source**.

1. Create a UDP output group. 

1. Create one output and set up the video and audio.

1. In this output, choose **Add captions** to create a captions encode. 
   + **Captions selector name**: Captions selector 1. 
   + **Captions settings**: DVB-Sub. 
   + **Language code** and **Language description**: German.
   + Other fields: Keep the defaults or complete as desired. 

1. Choose **Add captions** again to create another captions encode. Set up this encode for the French captions. Make sure that you set up the font fields for German and French in exactly the same way. 

1. Finish setting up the event and save it.