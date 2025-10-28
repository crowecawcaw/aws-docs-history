This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Teletext

You can use Teletext captions in one of the following ways:

- Teletext can include more data than just captions. If you want to include the entire
  Teletext input, your input and output captions format must be Teletext. You can't convert the
  entire set of Teletext data to another captions format.

AWS Elemental Server supports Teletext-to-Teletext only in MPEG-2 outputs.

- You can extract and convert individual captions pages (for example, the captions in a
  specific language) to another captions format. You can't extract individual captions pages and
  keep them in Teletext format. If you want to extract individual captions pages, you must
  convert them to another format.

## Number of Captions Selectors for

Teletext

- If you are doing Teletext-to-Teletext captions, create only one captions selector, even
  if you want to include multiple tracks in the output. In this case, AWS Elemental Server
  automatically extracts all tracks and includes them in the output.
- If you are doing Teletext-to-other, create one captions selector for each track that you
  want to include in the output.
- If you are doing Teletext-to-Teletext in some outputs and Teletext-to-other in other
  outputs, create one captions selector for the Teletext-to-Teletext, and then create
  individual selectors for the Teletext-to-other, one for each track that AWS Elemental Server
  converts.

## Captions Selector Fields for Teletext

Captions

- **Source**: Choose **Teletext**.
- **Page**: This field specifies the captions page you want. A captions
  page usually corresponds to a language. Complete as follows:
  - If you are doing Teletext-to-Teletext captions (that is, you create only one captions
    selector for the input embedded captions), keep this field blank. AWS Elemental Server ignores any
    value that you provide.
  - If you are converting Teletext to another format (that is, you create several captions
    selectors, one for each language), then specify the page for the language that you want. If
    you keep this field blank, you will get a validation error when you submit the job.
