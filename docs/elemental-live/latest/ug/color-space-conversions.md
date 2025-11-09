# Support for conversion and

passthrough

## Handling of supported

color spaces

Elemental Live can read the color space information of any supported
color space. It can convert the color space or pass through the color space
as follows:

| Supported color space   | Pass through                       | Convert                                                                                                                                                                                                                                                                                                |
| ----------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 601                     | Yes                                | Yes, to any supported color space except Dolby Vision.                                                                                                                                                                                                                                                 |
| 709                     | Yes                                | Yes, to any supported color space except Dolby Vision.                                                                                                                                                                                                                                                 |
| SDR 2020                | Yes                                | Yes, to any supported color space except Dolby Vision.                                                                                                                                                                                                                                                 |
| HDR10                   | Yes                                | Yes, to any supported color space. If you want to convert to<br>Dolby Vision, see [Requirements for<br>inputs](color-space-inputs-requirements.md "color-space-inputs-requirements.md") and<br>[Requirements for<br>outputs](color-space-output-requirements.md "color-space-output-requirements.md"). |
| HLG                     | Yes                                | Yes, to any supported color space except Dolby Vision.                                                                                                                                                                                                                                                 |
| Dolby Vision 5.0        | No. See the note after this table. | No.                                                                                                                                                                                                                                                                                                    |
| Dolby Vision 8.1        | Yes                                | No.                                                                                                                                                                                                                                                                                                    |
| Unsupported color space | Yes                                | No.                                                                                                                                                                                                                                                                                                    |

### Ingesting Dolby Vision

5.0

Elemental Live can't ingest video in the Dolby Vision 5.0 color space.
An event with this type of input will fail immediately when ingest
starts.

## Handling of unsupported

color spaces

We can't make any promises about handling of video that uses an
unsupported color space. Any of the following might apply:

- Elemental Live might be able to ingest the input and pass through the
  color space and the color space metadata.
- Or it might ingest the input but produce unacceptable output.
- Or it might fail to ingest the input, so that the event follows the
  input loss behavior routine (for example, it might display a slate in the
  output).

Elemental Live is never able to convert an unsupported color space to
another color space.
