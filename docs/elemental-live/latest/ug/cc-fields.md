

# Completing the fields in the CC channel number
<a name="cc-fields"></a>
+ **CC Channel number**: This field specifies the language to extract. Complete as follows: 
  + If you are setting up embedded passthrough only (you are creating only one captions selector for the input embedded captions), this field is ignored, so keep the default.
  + If you are setting up embedded-to-another-format, (you are creating several captions selectors, one for each language), enter the number of the CC instance (from the input) that holds the desired language. For example, if this captions selector is intended to hold the French captions and the French captions are in event 2, enter 2 in this field.
+ **Force 608 to 708 Upconvert**: The embedded source captions can be EIA-608 captions, CEA-708 captions, or both EIA-608 and CEA-708. You can specify how you want these captions to be handled when Elemental Live is ingesting content. The following table describes the behavior for various scenarios.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-live/latest/ug/cc-fields.html)
+ **Use SCTE-20 if Embedded Unavailable**: This field appears only if you set the **Source** to **Embedded**. If the source captions combine embedded (EIA-608 or CEA-708) and SCTE-20, you might want to set this field to **Auto**. Elemental Live will give preference to the 608/708 embedded captions but will switch to use the SCTE-20 captions when necessary. If you set this field to Off, Elemental Live will never use the SCTE-20 captions.