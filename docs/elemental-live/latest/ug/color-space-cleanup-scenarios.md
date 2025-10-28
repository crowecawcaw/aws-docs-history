# Step 2: Choose a clean-up

scenario

Read the following scenarios to decide if you need to clean up the
color space metadata in each input.

The following rules apply:

- If you are planning to convert the color space on the output side,
  keep in mind that the conversion will apply only to marked content. So if
  you use cleanup to insert missing metadata, you can increase the
  percentage of the content that gets converted in the output.
- The cleanup options don't convert the color space. Instead, cleanup
  options work on the metadata that is attached to the video.
- You should only clean up the color space if you are sure that all the
  unmarked portions use the color space that you choose. If the cleanup
  results in marking content as being in a specific color space when it
  isn't, then the video color quality will be degraded in the output.

###### Topics

- [Scenario A – Pass through accurate metadata](#color-space-scenario-pass "#color-space-scenario-pass")
- [Scenario B – Convert accurately marked color space](#color-space-scenario-convert "#color-space-scenario-convert")
- [Scenario C – Remove metadata](#color-space-scenario-remove "#color-space-scenario-remove")
- [Scenario D – Correct the metadata](#color-space-scenario-correct "#color-space-scenario-correct")
- [Scenario E – Correct the metadata in one color space](#color-space-scenario-correct-one "#color-space-scenario-correct-one")
- [Scenario F – Correct the metadata in multiple color spaces](#color-space-scenario-correct-multiple "#color-space-scenario-correct-multiple")

## Scenario A – Pass through accurate metadata

The details of this scenario are the following:

- Intended handling in the output – Pass through the color
  space.
- Status of the input – The video content is any combination of color
  spaces—SDR, HDR, or both.
- Status of the input color space metadata – The metadata is correct.

Recommendation:

- **Color Space** field – Set to
  **FOLLOW**
- **Force Color** field – Elemental Live ignores this
  field.

During ingest, Elemental Live will retain (pass through) the metadata.

## Scenario B – Convert accurately marked color space

The details of this scenario are the following:

- Intended handling in the output – Convert the color space and
  metadata.
- Status of the input color space – The video content is any
  combination of color spaces—SDR, HDR, or both.
- Status of the input color space metadata – The metadata is correct.

Recommendation:

- **Color Space** field – Set to
  **FOLLOW**.
- **Force Color** field – Elemental Live ignores this
  field.

During ingest, Elemental Live will retain (pass through) the metadata.

## Scenario C – Remove metadata

The details of this scenario are the following:

- Intended handling in the output – Remove the color space
  metadata.
- Status of the input – The video content is any combination of color
  spaces—SDR, HDR, or both.
- Status of the input color space metadata – The metadata can be of
  any quality.

Recommendation:

- **Color Space** field – Set to
  **FOLLOW**.
- **Force Color** field – Elemental Live ignores this
  field.

During ingest, Elemental Live will retain (pass through) the metadata.
You plan to remove the metadata, so you don't care about its
quality.

## Scenario D – Correct the metadata

The details of this scenario are the following:

- Intended handling in the output – Convert or pass through the color
  space.
- Status of the input – The video content is one color space. For
  example, the content is all REC_601.
- Status of the input color space metadata – Some of the metadata is
  missing, marked as _unknown_, or marked
  as a color space that Elemental Live doesn't support.

In addition, some of the metadata is wrong. For example, it is
marked as HDR10, but in fact, it is REC_601.

So in this scenario, the video content is all one color space, but the
color space metadata doesn't correctly indicate that fact.

Recommendation:

- **Color Space** field – Set to the color space that
  applies to the video content.
- **Force Color** field – Set to
  **FORCE**.

During ingest, Elemental Live will create metadata of the specified
color space for all missing, unmarked, and unknown metadata.

It will also force all existing metadata to match the specified color
space. Therefore, all the content in the input will be consistently marked
as belonging to one color space.

## Scenario E – Correct the metadata in one color space

The details of this scenario are the following:

- Intended handling in the output – Convert or pass through the color
  space.
- Status of the input – The video content is any combination of color
  spaces—REC_601, REC_709, HDR, and HLG.
- Status of the input color space metadata – The metadata for the
  video content of one color space is a mixture of acceptable and
  unacceptable. The metadata for that content is missing, marked as
  _unknown_, or marked as a color space
  that Elemental Live doesn't support. But in fact, all that content should
  be marked as one specific color space, for example, as REC_601.

The metadata for content for any other color space is correct. For
example, the metadata for REC_709 content and HDR10 content is
correct.

Recommendation:

- **Color Space** field – Set to the color space that
  has unacceptable metadata.
- **Force Color** field – Set to
  **FALLBACK**.

During ingest, Elemental Live will create metadata of the specific
color space for all missing, unmarked, and unknown video content. It will
retain existing metadata.

If you clean up the metadata in this way, Elemental Live might be able
to handle the color space appropriately in the output. However, if the
color map of the output is wrong in whole or in part, the video source was
probably in a color space that Elemental Live can't handle.

## Scenario F – Correct the metadata in multiple color spaces

The details of this scenario are the following:

- Intended handling in the output – Convert or pass through the color
  space.
- Status of the input – The video content is in _more than one_ color space. For example, the
  content is a mix of REC_601, REC_709, and HDR10.
- Status of the input color space metadata – The metadata for one
  color space is missing, wrong, marked as _unknown_, or marked as a color space that Elemental Live
  doesn't support. For example, the color space is REC_601, but its
  corresponding metadata is unreliable.

In addition, the metadata for one or more other color spaces is also
missing, wrong, unknown, or not supported. For example, the color space
of that content is HLG, but its corresponding metadata is
unreliable.

Recommendation:

There is no way to clean up this content because you can only mark all
the content as one type of color space. But in this scenario, the metadata
is incorrect in different types of color space.

If you force the color space, some of it will be forced to be correct,
but some of it will be forced to incorrect information. Inaccurate metadata
will result in an inaccurate conversion (if you convert in the output), or
in an inferior viewing experience (if you pass through in the
output).

The best recommendation we can provide is to remove the metadata on the
output side, as described in [scenario
C](#color-space-scenario-remove "#color-space-scenario-remove").

If you remove the metadata, Elemental Live might be able to handle the
color space appropriately in the output. However, if the color map of the
output is wrong in whole or in part, the video source was probably in a
color space that Elemental Live can't handle.
