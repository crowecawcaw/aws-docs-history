This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Including SCTE-35 Markers with

AWS Elemental Server

You can use AWS Elemental Server to manipulate the SCTE-35 messages in MPEG-2 transport stream
(TS) inputs. These messages may or may not include segmentation descriptors. You can also use
AWS Elemental Server to remove or include the cueing information conveyed by SCTE messages in the
output streams (video, audio, closed captioning, data) and in any associated manifests. The
processing instructions are all set up in the AWS Elemental Server job.

Note that AWS Elemental encoders do not support processing of manifests that are present in the
input. The information in these manifests is not ingested by the AWS Elemental encoder and
is not included in the output or the output manifest.

###### About this topic

SCTE messages may convey DPI cueing information for ad avails and for other non-ad-avail
messages such as programs and chapters.

This topic covers both ESAM and non-ESAM processing of SCTE messages.

###### Assumptions

This topic assumes you are familiar with the following:

- SCTE-35 standards and how the input you are encoding implements these standards
- Profiles and with managing AWS Elemental Server jobs.
