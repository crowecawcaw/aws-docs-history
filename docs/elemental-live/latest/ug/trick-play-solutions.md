# Implementing a trick-play

track

Trick-play is used in digital video players to mimic some capabilities
of analog players, including fast-forward and rewind capabilities. These
capabilities often include a trick-play _track_—a visual cue for the person using the video
player. In AWS Elemental Live, you can include track assets in an HLS
output group. The downstream system for that output group can use these
assets to implement the visual cue in their trick-play
implementation.

Elemental Live provides two methods for including these assets:

- An I-frame-only manifest that conforms with the HLS
  specification.
- A trick-play track that conforms with the Image Media Playlist
  specification, version 0.4.

## Choosing an implementation of

trick-play track

You can follow one or both trick-play methods in the same output
group.

Before you follow either method, contact the downstream system for
the output group to find out how they implement trick-play. Find out
the following:

- Can the downstream system support a trick-play track? If
  so, which trick-play specification does it follow?
- Is the supported implementation required or optional? Both
  of these implementations introduce specific lines into the
  HLS manifest. If the lines are absent, will the downstream
  system fail to handle the output from Elemental Live?

It is likely that the downstream system considers both of
these implementations to be optional.

- If you choose the I-frame-only manifest method, confirm
  that the downstream system supports the method according to
  the HLS specification. If the downstream system has a
  variation, it's possible that the downstream system won't be
  able to handle the output from Elemental Live. Elemental Live
  doesn't support customizations of the method.
- If you choose the image media playlist method, confirm
  that the downstream system supports the method according to
  the Image Media Playlist specification. If the downstream
  system has a variation, it's possible that the downstream
  system won't be able to handle the output from
  Elemental Live. Elemental Live doesn't support customizations
  of the implementation.

###### Topics

- [Trick-play track via
  I-frames](trick-play-i-frames.md "trick-play-i-frames.md")
- [Trick-play track via the Image
  Media Playlist specification](trick-play-roku.md "trick-play-roku.md")
