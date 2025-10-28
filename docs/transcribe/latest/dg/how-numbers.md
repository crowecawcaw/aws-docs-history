# Transcribing numbers and punctuation

Amazon Transcribe automatically adds punctuation to all supported languages, and capitalizes
words appropriately for languages that use case distinction in their writing systems.

For most languages, numbers are transcribed into their word forms. However, for languages with support for transcribing numbers,
Amazon Transcribe treats numbers differently depending on the context in which they're used.

For example, if a speaker says "Meet me at eight-thirty AM on June first at
one-hundred Main Street with three-dollars-and-fifty-cents and one-point-five chocolate
bars," this is transcribed as:

- Languages with number transcription support: Meet me at 8:30 a.m. on June 1st at 100 Main Street with
  $3.50 and 1.5 chocolate bars
- All other languages: Meet me at eight thirty a m on June first at one hundred
  Main Street with three dollars and fifty cents and one point five chocolate bars
  To view the languages with support for transcribing numbers, refer to
  [Supported languages and language-specific features](supported-languages.md "supported-languages.md").
