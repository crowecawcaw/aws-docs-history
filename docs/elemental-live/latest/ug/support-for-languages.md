# Support for multiple

languages

If the source includes captions in multiple languages, you can
include multiple languages in the output as follows:

- **Embedded Passthrough**. For any
  of the embedded source formats, if you specify embedded as the
  output format, then all languages that are in the input are included
  in the output. You can't remove any of the languages.
- **Embedded In, Other Out**. For any
  of the embedded source formats, if you are doing “embedded in, other
  out,” you can specify which languages to extract from the
  input.
- **Teletext Passthrough**. For
  teletext sources, if you specify teletext as the output, then all
  languages (pages) are included in the output. You can't strip out
  any languages. In fact, the entire teletext content is included in
  the output; you can't strip out any of the pages. Furthermore,
  teletext passthrough is supported only in TS outputs.
- **Teletext In, Other Out**. For
  teletext source, if you are doing “teletext in, other out,” you can
  specify which languages (teletext pages) to extract and which
  languages to include in an output.
- **Any Other Combination**. For all
  other sources, you always specify the language to extract from the
  input and the language to include in an output, regardless of the
  source format and output format.
