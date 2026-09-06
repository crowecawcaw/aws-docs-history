

# Step 3: Set up each input
<a name="color-space-event-input-setup"></a>

**To set up each input in the event**
**Note**  
This section assumes that you are familiar with creating or editing an event. 

1. On the **Event **page, in the **Input** section, open the **Advanced** section. More fields appear.

1. In the **Video selector** section, set the appropriate values for **Color Space** and **Force Color**.

   In the following table, each row shows a valid combination of the two fields and the result of that combination.     
[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-live/latest/ug/color-space-event-input-setup.html)

## Tips for HDR master display information
<a name="color-space-input-display-data"></a>

The HDR Master Display Information fields appear in the color space fields if you set the **Color Space** field to HDR10. Take the appropriate action:
+ Complete these fields only if your plan is to pass through this color space to the output, and only if the content provider has told you that the content currently doesn't include this metadata. For details about a field on the web interface, choose the question mark next to the field. 

  If the content provider has told you that the content already contains the metadata, leave these fields blank.

  Make sure to obtain values used in the color grading process for the input. You can't use the defaults or null values and expect to obtain valid color results. It's better to set the fields to null values, rather than to make up values.
+ Don't complete these fields if your plan is to convert from this HDR10 color space to another color space.

### Red, green, blue, white point x and y
<a name="hdr-input-RGB"></a>

Your content provider might provide numbers like this for X and Y points:
+ G (x=0.265, y=0.690)
+ B (x=0.150, y=0.060)
+ R (x=0.680, y=0.320)

You must convert these numbers to numbers like this: 
+ G (13250, 34500)
+ B (7500, 3000)
+ R (34000, 16000)

To convert between the two formats, divide each number by 0.00002 as per the HEVC specification.

For example, 0.265 divided by 0.00002 is 13250.

### Max luminance and min luminance
<a name="hdr-input-cll-fall"></a>

The maximum and minimum luminance are given in units of **0.0001 candelas per square meter**. Your content provider might provide this value in candelas per square meter instead. If so, then convert these numbers by multiplying by 10,000, then entering the result in the web interface.

For example, a value of 1000.0000 cd/m2 for max luminance would be converted to 10,000,000 and entered as that in the web interface.