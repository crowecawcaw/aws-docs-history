# Using SSML on the console

In the following example, you use an SSML tag to tell Amazon Polly to
substitute "World Wide Web Consortium" for "W3C" when it speaks a
short paragraph. You also use tags to introduce a pause and whisper
a word. Compare the results of this exercise with that of [Applying lexicons (Synthesizing Speech)](managing-lexicons-console-synthesize-speech.md "managing-lexicons-console-synthesize-speech.md")
.

For more information on SSML, with examples, see [Supported SSML tags](supportedtags.md "supportedtags.md").

###### To synthesize speech from SSML-enhanced text (console)

1. Sign in to the AWS Management Console and open the Amazon Polly console at [https://console.aws.amazon.com/polly/](https://console.aws.amazon.com/polly/ "https://console.aws.amazon.com/polly/").
2. If it isn't already displayed, choose the
   **Text-to-Speech** tab.
3. Turn on **SSML**.
4. Type or paste the following text in the text box:

```
<speak>
     He was caught up in the game.<break time="1s"/> In the middle of the
     10/3/2014 <sub alias="World Wide Web Consortium">W3C</sub> meeting,
     he shouted, "Nice job!" quite loudly. When his boss stared at him, he repeated
     <amazon:effect name="whispered">"Nice job,"</amazon:effect> in a
     whisper.
</speak>
```

The SSML tags tell Amazon Polly how to render the text:

    * `<break time="1s"/>` tells Amazon Polly
     to pause 1 second between the first two
     sentences.
    * `<sub alias="World Wide Web
     Consortium">W3C</sub>` tells
     Amazon Polly to substitute World Wide Web Consortium for
     the acronym W3C.
    * `<amazon:effect name="whispered">Nice
     job</amazon:effect>` tells Amazon Polly to
     whisper the second instance of "Nice job." .


    ###### Note

    When you use the AWS CLI, you enclose the input
     text in quotation marks to differentiate it from
     the surrounding code. The Amazon Polly console doesn't
     show you code, so you don't enclose input text
     in quotation marks when you use it.

5. For **Language**, choose
   **English, US**, then choose a
   voice.
6. To listen to the speech, choose
   **Listen**.
7. To save the speech file, choose
   **Download**. If you want to save it in
   a different format, expand **Additional
   settings**, turn on **Speech file
   format settings** and choose the format that
   you want, then choose **Download**.
