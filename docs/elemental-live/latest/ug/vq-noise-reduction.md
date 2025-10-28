# Noise reduction

## Description

You can apply the noise reducer preprocessor to improve output video
quality.

- The **Filter** parameter has four
  options:
  - **Mean / Gaussian / Lanczos**: All of these
    algorithms allow for varying blur strengths. **Mean**
    is the strongest filter; it operates on a smaller group of pixels.
    **Lanczos** is the mildest filter; it operates on a
    larger group of pixels.
  - **Sharpen**: This algorithm sharpens
    the edges instead of softening them.
  - **Conserve**: This algorithm limits
    the pixel values to within the minimum and maximum values of the
    neighboring pixel values. It is designed to reduce speckle noise. This
    filter does not seem to be very valuable with video.
  - **Bilateral**: This algorithm tends to
    preserve strong edges; it's the best compromise between noise reduction
    and visual quality.

- **Strength**: The strength parameter of the
  filtering has its greatest effect at **3**.

## Recommendations

In most cases, the noise reducer is not required. The reducer can help
output quality if the content is being heavily compressed. However, it
changes the visual quality of the video.

The recommended algorithm is bilateral, but the other algorithms might
produce better results in certain use cases. We recommend that you run tests
on a video sample, to determine the best option for your application.

## Location of parameters

This table shows where the parameters mentioned in this section are
located. The first column shows the location on the web interface. The
second column shows the location in the event XML.

| Location of parameter on web interface                           | Location of tag in XML                                                        |
| ---------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **Streams > Advanced >Preprocessors > Noise Reducer > Filter**   | stream_assembly/video_description/video_preprocessors/ noise_reducer/filter   |
| **Streams > Advanced >Preprocessors > Noise Reducer > Strength** | stream_assembly/video_description/video_preprocessors/ noise_reducer/strength |
