# Supported SSML tags

All tags except for `<amazon:domain name="news">` are supported for Standard voices. Tag availability for other voices is provided in the following table.

Amazon Polly supports the following SSML tags:

| Action                                                                                          | SSML tag                           | Neural voice availability | Long-form voice availability | Generative voice availability |
| ----------------------------------------------------------------------------------------------- | ---------------------------------- | ------------------------- | ---------------------------- | ----------------------------- |
| [Adding a pause](break-tag.md "break-tag.md")                                                   | <break>                            | Full availability         | Full availability            | Full availability             |
| [Emphasizing words](emphasis-tag.md "emphasis-tag.md")                                          | <emphasis>                         | Not available             | Not available                | Not available                 |
| [Specifying another language for<br>specific words](lang-tag.md "lang-tag.md")                  | <lang>                             | Full availability         | Full availability            | Full availability             |
| [Placing a custom tag in your text](custom-tag.md "custom-tag.md")                              | <mark>                             | Full availability         | Full availability            | Partial availability          |
| [Adding a pause between paragraphs](p-tag.md "p-tag.md")                                        | <p>                                | Full availability         | Full availability            | Full availability             |
| [Using phonetic pronunciation](phoneme-tag.md "phoneme-tag.md")                                 | <phoneme>                          | Full availability         | Full availability            | Partial availability          |
| [Controlling volume, speaking rate,<br>and pitch](prosody-tag.md "prosody-tag.md")              | <prosody>                          | Partial availability      | Partial availability         | Partial availiability         |
| [Setting a maximum duration for<br>synthesized speech](maxduration-tag.md "maxduration-tag.md") | <prosody amazon:max-duration>      | Not available             | Not available                | Not available                 |
| [Adding a pause between sentences](s-tag.md "s-tag.md")                                         | <s>                                | Full availability         | Full availability            | Full availability             |
| [Controlling how special types of<br>words are spoken](say-as-tag.md "say-as-tag.md")           | <say-as>                           | Partial availability      | Full availability            | Full availability             |
| [Identifying SSML-enhanced text](speak-tag.md "speak-tag.md")                                   | <speak>                            | Full availability         | Full availability            | Full availability             |
| [Pronouncing acronyms and abbreviations](sub-tag.md "sub-tag.md")                               | <sub>                              | Full availability         | Full availability            | Full availability             |
| [Improving pronunciation by specifying<br>parts of speech](w-tag.md "w-tag.md")                 | <w>                                | Full availability         | Full availability            | Full availability             |
| [Adding the sound of breathing](breath-tag.md "breath-tag.md")                                  | <amazon:auto-breaths>              | Not available             | Not available                | Not available                 |
| [Newscaster speaking style](newscaster-tag.md "newscaster-tag.md")                              | <amazon:domain name="news">        | Select neural voices only | Not available                | Not available                 |
| [Adding dynamic range compression](drc-tag.md "drc-tag.md")                                     | <amazon:effect name="drc">         | Full availability         | Full availability            | Not available                 |
| [Speaking softly](phonation-tag.md "phonation-tag.md")                                          | <amazon:effect phonation="soft">   | Not available             | Not available                | Not available                 |
| [Controlling timbre](vocaltractlength-tag.md "vocaltractlength-tag.md")                         | <amazon:effect vocal-tract-length> | Not available             | Not available                | Not available                 |
| [Whispering](whispered-tag.md "whispered-tag.md")                                               | <amazon:effect name="whispered">   | Not available             | Not available                | Not available                 |

###### Note

If you use unsupported SSML tags in standard, neural, or long-form
format, you will get an error.
