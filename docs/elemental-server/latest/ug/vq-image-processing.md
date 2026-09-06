

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# Image Processing Controls
<a name="vq-image-processing"></a>

**Topics**
+ [Image Processing – Scaling Content](#vq-scaling-content)
+ [Image Processing – Color Correction](#vq-color-correction)
+ [Image Processing – Scan Type – Key Controls](vq-scan-type-key.md)
+ [Image Processing – Scan Type – Secondary Fields](vq-scan-type-secondary.md)
+ [Image Processing – Noise Reduction](vq-noise-reduction.md)
+ [Image Processing – framerate Conversion](vq-framerate-conversion.md)

## Image Processing – Scaling Content
<a name="vq-scaling-content"></a>

### Description
<a name="description-scaling-content"></a>

Scaling content is typically applied to adjust source content to better match the intended output device screen size or to optimize the resolution of a video output for a particular bitrate. Typically, the lower the bitrate, the smaller the resolution. These settings relate to scaling.
+  **Resolution** (width, height): Controls the number of pixels encoded (e.g. 1280x720, 640x480) 
+ **Stretch to Output**: Controls the aspect ratio of video content itself. For example, if Stretch to Output is enabled and source content with a resolution of 1280x720 (16:9) is transcoded to 640x480 (4:3), the resulting output video appears skewed as the aspect ratio of the video content is modified. 
+ **Anti-alias**: Choose Bilinear Interpolation or the variable-tap Lanczos filter. In almost all cases, the Lanczos filter provides much better quality when scaling video content, with a small impact on performance. 

### Recommendations
<a name="recommendation-scaling-content"></a>

Enable **Anti-alias** unless speed is of utmost importance and video quality is not. 

### Location of Fields
<a name="api-scaling-content"></a>


| Stream – Video > Resolution | stream\_assembly/video\_description/resolution | 
| --- | --- | 
| Stream – Video > Stretch to output | stream\_assembly/video\_description/stretch\_to\_output | 
| Stream – Video > Anti-alias | stream\_assembly/video\_description/anti\_alias | 

## Image Processing – Color Correction
<a name="vq-color-correction"></a>

### Description
<a name="description-vq-color-correction"></a>

In some situations, color correction can be used to adjust the visual color representation of content:
+  **Brightness / Contrast / Hue / Saturation**: Provide basic pixel luma and chroma adjustment. 
+ **Video Range**: Expands the pixel value range from 16-235 vs 0-255 (full-swing encoding). Set to true to set to full-swing encoding or set to false to pass through the encoding. 

  Set to "true" only if you are sure the range of the input is not full-swing. If it is full-swing and you choose "true", the blacks and whites in the output are clipped. 
+ **Color Space Conversion**: Adjusts pixel values from input to output color space (e.g. REC-601). 
  + Set to "None" to perform no conversion. 
  + Set to "Force 601" or "Force 709" to convert inputs with differing colorspaces. When choosing either of these options, either the metadata must specify the colorspace of the input or you must manually specify that colorspace via the Color Space field in the Video Selector section. If the input colorspace is not specified in one of these ways, the encoder ignores the selected value and does not do any conversion. 

### Recommendations
<a name="vq-color-correction-recommendations"></a>

Color adjustment does not affect output quality so there are no specific recommendations. 

### Location of Fields
<a name="vq-color-correction-api"></a>

The following table lists each field by its location on the web interface and shows the location of the corresponding tag in the XML. 


| Location of Field on Web Interface | Location of Tag in XML | 
| --- | --- | 
| Input > Video Selector > Color Space | input/video\_selector/color\_space | 
| Stream – Video > Advanced > Preprocessors > Color Corrector > Brightness | stream\_assembly/video\_description/video\_preprocessor/<br /> color\_corrector/brightness | 
| Stream – Video > Advanced > Preprocessors > Color Corrector > Contrast | stream\_assembly/video\_description/video\_preprocessor/<br /> color\_corrector/contrast | 
| Stream – Video > Advanced > Preprocessors > Color Corrector > Hue | stream\_assembly/video\_description/video\_preprocessor/<br /> color\_corrector/hue | 
| Stream – Video > Advanced > Preprocessors > Color Corrector > Saturation | stream\_assembly/video\_description/video\_preprocessor/<br /> color\_corrector/saturation | 
| Stream – Video > Advanced > Preprocessors > Color Corrector > Video Range | stream\_assembly/video\_description/video\_preprocessor/<br /> color\_corrector/full\_swing | 
| Stream – Video > Advanced > Preprocessors > Color Corrector > Color Space Conversion | stream\_assembly/video\_description/video\_preprocessor/<br /> color\_corrector/color\_space\_conversion | 