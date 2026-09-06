

# Create captions selectors in the inputs
<a name="identify-captions-in-the-input"></a>

This section describes the first step for setting up for captions in MediaLive. You must identify the captions that you want to use and assign each to a captions selector. If you don't create any captions selectors, you can't include captions in the output. All the captions will be removed from the media.

Then you must extract the captions that you want by adding a captions selector in the channel. Each extracted captions asset is contained in one captions selector. For example, one selector contains the Teletext captions in Czech.

**Topics**
+ [Identify the captions that you want](#identify-source-captions-step-a)
+ [Create captions selectors](#identify-source-captions-step-b)
+ [Information for DVB-Sub or SCTE-27](#dvb-sub-or-scte27)
+ [Information for embedded](#embedded)
+ [Information for Teletext](#teletext)

## Identify the captions that you want
<a name="identify-source-captions-step-a"></a>

1. Identify which captions are in the input (the provider of the input should provide you with this information). Identify the captions formats and, for each format, the languages. 

1. Identify which of those formats and languages that you want to use. 

1. If you are converting DVB-Sub or SCTE-27 captions to WebVTT, there are limits on the number of languages that MediaLive can ingest. For more information, see [Constraints for using OCR conversion](captions-languages-ocr.md).

1. Determine how many captions selectors to create in the input in the channel. For guidance, see the table that appears after this procedure.

You end up with a list of captions selectors to create. For example:
+ Captions Selector 1: Teletext captions in Czech
+ Captions Selector 2: Teletext captions in Polish


| Source captions | Output captions | Result | 
| --- | --- | --- | 
| ARIB  | ARIB | Create a single captions selector. All languages are passed through; there is no other option. | 
| Embedded | Embedded | Create a single captions selector. All languages are passed through; there is no other option. For details, see [Information for embedded](#embedded). | 
| Embedded | Another format | Specify the language to extract from the input and the language to include in an output. The specified language is extracted from the embedded captions and converted to the new format. | 
| DVB-Sub | WebVTT | Create one caption selector for each language, to a maximum of three caption selectors in the input. For more information about this limit, see [Constraints for using OCR conversion](captions-languages-ocr.md). | 
| DVB-Sub | SMPTE-TT | Create one caption selector for each language. The specified language is extracted from the DVB-Sub captions and converted to the new format.  | 
| DVB-Sub | DVB-Sub | Create a single captions selector. All languages are passed through. | 
| SCTE-27 | WebVTT | Create one caption selector for each language, to a maximum of three caption selectors in the input. For more information about this limit, see [Constraints for using OCR conversion](captions-languages-ocr.md). | 
| Teletext | Teletext | Create a single captions selector. All languages are passed through. All the pages in the teletext are passed through. For details, see [Information for Teletext](#teletext). | 
| Teletext | Another format | If you have Teletext source and want a different format in the output, create one captions selector for each language and format combination. | 
| Any other combination |  | Create one captions selector for each language and format combination. | 

## Create captions selectors
<a name="identify-source-captions-step-b"></a>

1. In the channel that you are creating, in the navigation pane, in **Input attachments**, choose the input. 

1. Got to **General input settings** and choose **Add captions selectors**.

1. In **Captions selector name**, enter a name that describes the captions in the source.. For example, **Teletext Czech**. 

1. In **Selector settings**, choose the format of the source captions. 

1. For most formats, more fields appear. For details about a field, choose the **Info** link next to the field. In addition, see [DVB-Sub or SCTE-27](#dvb-sub-or-scte27), [Embedded](#embedded), or [Teletext](#teletext).

1. Create more captions selectors, as required. 

## Information for DVB-Sub or SCTE-27
<a name="dvb-sub-or-scte27"></a>

1. You must specify the location of the captions.

   Complete the **PID** or **Language** code fields in one of the ways described in the following table. Each row in the table describes a valid way to complete these two fields.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/medialive/latest/ug/identify-captions-in-the-input.html)

1. If you plan to convert the captions to WebVTT, you must also specify the language of the captions.

   Complete the **OCR language** field to specify the language of the captions specified by this selector.

   MediaLive ignores any value in this field if you aren't converting the captions to WebVTT.

## Information for embedded
<a name="embedded"></a>

Read this section if the input captions are any of the following: embedded (EIA-608 or CEA-708), embedded\+SCTE-20, SCTE-20\+embedded, or SCTE-20.

**How many captions selectors?**
+ **Embedded passthrough** – Create only one captions selector. With this scenario, all languages are automatically extracted and are automatically included in the output.
+ **Embedded in, other out** – Create one captions selector for each language that you want to include in the output, to a maximum of four selectors.
+ **A combination of Embedded passthrough and Embedded conversion** – If you are setting up for embedded passthrough in some outputs and embedded-to-other in other outputs, create one captions selector for each language that you want to include in the output, to a maximum of four selectors. Don't worry about a selector for the embedded passthrough output. MediaLive extracts all the languages for that output, even though there is not a selector to explicitly specify this action. 

**Captions selector fields**
+ **Selector settings**: 
  + Choose embedded if the source captions are embedded (EIA-608 or CEA-708), embedded\+SCTE-20, or SCTE-20\+embedded.
  + Choose SCTE-20 if the source captions are SCTE-20 alone.
+ **EIA-608 track number** – This field specifies the language to extract. Complete as follows: 
  + If you are setting up for embedded passthrough only (you are creating only one captions selector for the input embedded captions), this field is ignored, so keep the default.
  + If you are converting embedded to another format (you are creating several captions selectors, one for each language), specify the number of the CC instance (from the input) that holds the language that you want.
+ **Convert 608 to 708**: The embedded source captions can be EIA-608 captions, CEA-708 captions, or both EIA-608 and CEA-708. You can specify how you want these captions to be handled when AWS Elemental MediaLive is ingesting content. The following table describes the behavior for various scenarios.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/medialive/latest/ug/identify-captions-in-the-input.html)
+ **SCTE-20 detection** – If the source captions combine embedded (EIA-608 or CEA-708) and SCTE-20, you might want to set this field to **Auto**. AWS Elemental MediaLive gives preference to the 608/708 embedded captions but switches to use the SCTE-20 captions when necessary. If you set this field to **Off**, AWS Elemental MediaLive never uses the SCTE-20 captions.

## Information for Teletext
<a name="teletext"></a>

Teletext is a form of data that can contain several types of information, not just captions. Teletext can be handled in one of the following ways:
+ If you want to include the entire Teletext input, you must set up for Teletext passthrough. The entire Teletext can never be converted to another format. 
+ Individual captions pages (the captions in a specific language) can be extracted and converted to another captions format.
+ Individual captions pages (the captions in a specific language) *cannot* be extracted and kept in Teletext. If you want to extract individual captions pages, you must convert them to another format.

**How many captions selectors?**
+ If you are setting up for Teletext passthrough captions, create only one captions selector, even if you want to include multiple languages in the output. With this scenario, all languages are automatically extracted and included in the output. 
+ If you are setting up for Teletext-to-other, create one captions selector for each language that you want to include in the output. For example, one selector to extract English Teletext, and one selector to extract Swedish Teletext.
+ If you are setting up for Teletext passthrough in some outputs and Teletext-to-other in other outputs, create one captions selector for each language that you want to include in the output. Don't worry about a selector for the passthrough output. MediaLive passes through all the data, even though there isn't a selector to explicitly specify this action. 

**Captions selector fields**
+ **Selector settings** – Choose **Teletext**.
+ **Page number** – This field specifies the page of the desired language. Complete as follows: 
  + If you are setting up for Teletext passthrough captions (you are creating only one captions selector for the input captions), keep the field blank. The value is ignored.
  + If you are converting Teletext to another format (you are creating several captions selectors, one for each language), complete the **Language code** field to specify the page for the language that you want. If you leave this field blank, you get a validation error when you save the channel. 

**Including a positioning rectangle**

If you plan to convert the source captions to EBU-TT-D, you can optionally define a rectangle that positions the captions on the video frame in the output. If you choose to use this feature, it will apply as follows:
+ It will apply to all your EBU-TT-D outputs that use this captions selector. 
+ It won't apply to any other formats of output captions that use this caption selector. The positioning information is simply omitted from these other captions formats.

You define the rectangle relative to the underlying video frame. For example, you specify the position of the left edge of the rectangle as a percentage of the entire width of the video frame. A value of 10 means "calculate a value X that is 10% of the frame width. Then find the left edge of the video frame and move X pixels into the frame and draw the left edge of the rectangle".

Specifying a percentage, rather than a fixed number, means that the rectangle works for different video renditions (different resolutions) in the same output.

To define a positioning rectangle, follow this procedure.

1. In the **Output rectangle** field, choose **Caption rectangle**.

1. Complete the fields for the four sides of the rectangle – **Left offset**, **Width**, **Top offset**, and **Height**.