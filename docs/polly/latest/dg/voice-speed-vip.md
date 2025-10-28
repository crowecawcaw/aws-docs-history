# Timing a voice speed

Because of the natural variation between voices, each available voice speaks at
slightly different speeds. For instance, with US English voices, Ivy and Joanna are
slightly faster than Matthew, and
considerably faster than Joey. Since there is so much variation between voices,
there is no standard speed (words per minute)
available for Amazon Polly voices. However, you can find how long it takes for your voice to
say the selected text using [Speech Marks](using-speechmarks.md "using-speechmarks.md").

###### To time the length of a spoken text passage

1. Open the AWS CLI.
2. Run the following code, filling in as needed.

```
     aws polly synthesize-speech \
          --language-code `optional language code if needed`
          --output-format json \
          --voice-id `[name of desired voice]` \
          --text '`[desired text]`' \
          --speech-mark-types='["viseme"]' \
          LengthOfText.txt
```

3. Open `LengthOfText.txt`.
   If the text were "Mary had a little lamb," the last few lines returned by Amazon Polly would
   be:

```
     {"time":882,"type":"viseme","value":"t"}
     {"time":964,"type":"viseme","value":"a"}
     {"time":1082,"type":"viseme","value":"p"}
```

The last viseme, essentially the sound for the final letters in "lamb" starts 1082
milliseconds after the beginning of the speech. While this is not exactly the length of
the audio, it's close and can serve as the basis for comparison between voices.
