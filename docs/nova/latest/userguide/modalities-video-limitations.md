# Video understanding limitations

Understand the following limitations for Amazon Nova:

- **Multilingual Image Understanding:** The models
  have limited understanding of multilingual images and video frames and can
  struggle or hallucinate on similar tasks.
- **People identification**: The Amazon Nova models
  do not support the capability to identify or name individuals in images,
  documents or videos. The models will refuse to perform such tasks.
- **Spatial reasoning**: The Amazon Nova models have
  limited spatial reasoning capabilities. They may struggle with tasks that
  require precise localization or layout analysis.
- **Small Text in Images/Videos**: If the text in
  the image or video is too small, consider increasing relative size of the text
  in the image by cropping to relevant section while preserving necessary
  context.
- **Counting**: The Amazon Nova models can provide
  approximate counts of objects in an image, but may not always be precisely
  accurate, especially when dealing with large numbers of small objects.
- **Inappropriate content**: The Amazon Nova models
  will not process inappropriate or explicit images that violate the Acceptable
  Use Policy.
- **Healthcare applications**: Due to the sensitive
  nature of these artifacts, even though Amazon Nova models can give general
  analysis on healthcare images or videos, we do not recommend that you interpret
  complex diagnostic scans. Amazon Nova responses should never be considered a
  substitute for professional medical advice.
