# Speech mark output

Amazon Polly returns speech mark objects in a line-delimited JSON stream. A speech mark object contains the
following fields:

- **time** – the timestamp in
  milliseconds from the beginning of the corresponding audio
  stream
- **type** – the type of
  speech mark (sentence, word, viseme, or ssml)
- **start** – the offset in bytes (not characters) of the start of the object in the input text (not including viseme marks)
- **end** – the offset in bytes (not characters) of the object's end in the input text (not including viseme marks)
- **value** – this varies depending on the
  type of speech mark

      + **SSML**: <mark> SSML tag
      + **viseme**: the viseme name
      + **word** or
       **sentence**: a substring of the
       input text, as delimited by the start and end fields

  For example, Amazon Polly generates the following `word` speech mark object
  from the text "Mary had a little lamb":

```
{"time":373,"type":"word","start":5,"end":8,"value":"had"}
```

The described word ("had") begins 373 milliseconds after the audio stream
begins, and starts at byte 5 and ends at byte 8 of the input text.

###### Note

This metadata is for the `Joanna` voice-id. If you use
another voice with the same input text, the metadata might
differ.
