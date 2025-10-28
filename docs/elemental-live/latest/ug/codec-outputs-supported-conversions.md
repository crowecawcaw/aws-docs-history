# Audio

codecs and supported conversions

Generally, Elemental Live can convert any audio codec that is
supported as a source to any audio codec that is supported as an
output. However, there are some constraints, as follows.

- Constraint when Dolby Digital with Atmos is the source.
  Conversion to another codec isn't supported. You can only pass
  through this source codec.
- Constraint when converting to another codec (other than
  Dolby Digital with Atmos) and changing the coding mode. The
  following rules apply:

      + The source must contain at least as many channels as
       the output. For example, to produce Dolby 5.1 (6
       channels), the source must contain 6 channels.
      + The source can contain fewer channels. For example,
       you can convert Dolby 5.1 to AAC 2.0.

  In both cases, you might need to remix the channels in the
  output.
