This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Image Processing – Noise Reduction

## Description

In some applications, you can apply the Noise Reducer Preprocessor to improve output
quality. It works by reducing spatial noise, which makes images compress better. But it changes
the visual quality of the video.

- The **Filter** field has four options:
  - **Mean / Gaussian / Lanczos**: All of these algorithms allow
    for varying blur strengths. Mean is the strongest filter (it operates on a smaller group of
    pixels) while Lanczos is the mildest (it operates on a larger group of pixels).
  - **Sharpen**: This algorithm sharpens the edges instead
    of softening them.
  - **Conserve**: This algorithm limits the pixel values to
    within the minimum and maximum values of the neighboring pixel values. It is designed to
    reduce speckle noise. This filter does not seem to be very valuable with video.
  - **Bilateral**: This algorithm tends to preserve strong
    edges and is the best compromise between noise reduction and visual quality.

- **Strength**: The strength field of the filtering has its
  greatest effect at 3.

## Recommendations

In most cases, enabling the Noise Reducer is not required, but can help output quality if
the content will be compressed heavily. When enabled, the recommended algorithm is Bilateral,
but the other algorithms may produce better results in certain use cases. Testing the different
algorithms using the expected source content is the recommended method to determine the best
option.

## Location of Fields

| Location of Field on Web Interface                           | Location of Tag in XML                                                           |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------- |
| Streams > Advanced >Preprocessors > Noise Reducer > Filter   | stream_assembly/video_description/video_preprocessors/<br>noise_reducer/filter   |
| Streams > Advanced >Preprocessors > Noise Reducer > Strength | stream_assembly/video_description/video_preprocessors/<br>noise_reducer/strength |
