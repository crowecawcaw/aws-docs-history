# Getting ready to use 3D LUTs files with

MediaLive

You can configure a channel to use a 3D LUTs color correct file for conversion, instead
of using the standard MediaLive color corrector file for conversion.

You provide a list of 3D LUTs files. Each 3D LUTs file contains color mapping
information for a specific source/output combination. For example, one file contains
information for converting Rec. 709 to HDR10.

## Using 3D LUTs files

These rules apply to using 3D LUTs files:

- **Sourcing of 3D LUTs files.** You must provide the
  3D LUTs files. MediaLive doesn't have built-in files.
- **One file for each combination.** You must provide a
  file for each source/output combination. For example, a file for converting Rec. 601
  to HDR10.
- **Maximum 8 files.** You can provide a maximum of 8
  files for each channel. This means that MediaLive supports up to 8 source/output
  conversion combinations.
- **Global application.** MediaLive uses a specific file in
  all the outputs where that file applies. For example, if there is a file to convert
  Rec. 601 to HDR10, MediaLive uses that file in every output that it applies to. You can't
  configure some outputs to use the standard mechanism for conversion.

## Contents of the 3D LUTs

files

The following rules apply to the contents of the files:

- **Format.** You must make sure that each 3D LUTs file
  follows the .cube 3D LUTs format.

- **Maximum one file per combination.** You can provide
  only one 3D LUTs file for each combination. You can't configure some outputs to use a
  different 3D LUTs file. When MediaLive reads the list of 3D LUTs files, it uses the first
  file that it finds for a source/output combination.
- **HDR10 luminance.** MediaLive supports conversion of
  HDR10 content with a maximum luminance of 1000 nits to 4000 nits, but it only supports
  one maximum luminance. When MediaLive reads the list of 3D LUTs files, it finds the first
  file for each conversion from HDR10. Even if you one file for 1000 nits and one for
  4000 nits (for example), MediaLive uses only the first file it encounters. Therefore the
  following guidelines apply:
  - You should make sure that all the HDR10 content in all the inputs in one
    channel have the same maximum luminance. If a source has a different maximum
    luminance, MediaLive will convert the content, but the outputs will have sub-optimal
    luminance.
  - In each 3D LUTs file for converting from HDR10, make sure that the luminance
    handling is appropriate for the luminance of the source.
