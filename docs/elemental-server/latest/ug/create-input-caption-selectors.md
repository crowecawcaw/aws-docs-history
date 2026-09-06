

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# Creating Input Captions Selectors
<a name="create-input-caption-selectors"></a>

When you set up captions, you begin by creating input captions selectors. Captions selectors identify a particular captions asset on the input and associate a label with it. The captions asset is either a single track or the set of all tracks contained in the input file, depending on your input captions format. For example, you might add **Captions selector 1** and associate the French captions with it. When you [set up an output to include captions](including-captions-in-outputs.md), you do so by specifying these input captions selectors in the streams in your outputs. 

**To create input captions selectors**

1. On the **Create New Job** page, In the **Input** section, under **Input 1**, choose **Advanced** to display more settings.

1. Choose the **Add Caption Selector**, below the **Video Selector** and **Audio Selector** sections. 

1. Under **Source**, choose the input captions format. 

1. For most formats, more fields appear. Specify the values for these fields as described in the topic that relates to your input captions format. For more information about these fields, choose the appropriate topic from the list following this procedure.

1. Create more captions selectors as necessary. The number of captions selectors you need depends on your input captions format. For information on the number of captions selectors you should set up, see the topic from the list following this procedure that corresponds to your input captions format.

**Topics**
+ [Ancillary (QuickTime Captions Track or Captions in MXF VANC Data)](ancillary.md)
+ [ARIB](arib-input.md)
+ [Embedded (CEA/EIA-608, CEA/EIA-708), SCTE-20, and Embedded\+SCTE-20, and SCTE-20\+Embedded](embedded.md)
+ [DVB-Sub or SCTE-27 Formats](dvb-sub-or-scte-27.md)
+ [Teletext](dvb-teletext.md)
+ [SCC, SMI, SRT, STL, TTML (Sidecar)](scc.md)
+ [Setting Up Input Captions With 608 XDS Data](setting-up-for-608-xds-data.md)
+ [Extracting VBI Data Included in Embedded Input Captions](embedded-captions-in-vbi-data.md)