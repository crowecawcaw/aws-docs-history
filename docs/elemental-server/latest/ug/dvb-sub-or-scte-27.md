This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# DVB-Sub or SCTE-27 Formats

AWS Elemental Server supports DVB-Sub and SCTE-27 formats only in TS inputs.

In most cases, create one captions selector per track. In each selector, specify which
track you want by providing the PID or language code.

###### Note

Don't specify the captions in both the **PID** field and the
**Language** dropdown list. Specify one or the other.

If you are doing DVB-sub-to-DVB-sub and you want to pass through all the captions tracks
from the input to the output, create one captions selector for all tracks. In this case, keep
the **PID** field blank and don't choose any language from the
**Language** dropdown list.
