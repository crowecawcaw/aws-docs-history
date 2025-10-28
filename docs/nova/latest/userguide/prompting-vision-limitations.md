# Video understanding limitations

The following are key model limitations, where model accuracy and performance might not be
guaranteed.

- **One video per request:** currently the model
  supports only 1 video per request. Some frameworks and libraries use memory to keep
  track of previous interactions. There might be a video that was added in a previous
  context.
- **No audio support:** The models are currently
  trained to process and understand video content solely based on the visual
  information in the video. They do not possess the capability to analyze or
  comprehend any audio components that are present in the video.
- **Temporal causality:** The model has limited
  understanding of event causality across the progression of the video. Although it
  answers well to point in time questions, it does not perform as well on answers that
  depends on understanding a sequence of events
- **Multilingual image understanding:** The models have
  limited understanding of multilingual images and video frames. They might struggle
  or hallucinate on similar tasks.
- **People identification**: The Amazon Nova models do
  not support the capability to identify or name individuals in images, documents, or
  videos. The models will refuse to perform such tasks.
- **Spatial reasoning**: The Amazon Nova models have
  limited spatial reasoning capabilities. They may struggle with tasks that require
  precise localization or layout analysis.
- **Small text in images or videos**: If the text in
  the image or video is too small, consider increasing relative size of the text in
  the image by cropping to the relevant section while preserving necessary
  content.
- **Counting**: The Amazon Nova models can provide
  approximate counts of objects in an image, but might not always be precisely
  accurate, especially when dealing with large numbers of small objects.
- **Inappropriate content**: The Amazon Nova models will
  not process inappropriate or explicit images that violate the Acceptable Use
  Policy
- **Healthcare applications**: Due to the sensitive
  nature of these artifacts, even though Amazon Nova models can give general analysis on
  healthcare images or videos, we do not recommend that you interpret complex
  diagnostic scans. The response of Amazon Nova should never be considered a substitute
  for professional medical advice.
