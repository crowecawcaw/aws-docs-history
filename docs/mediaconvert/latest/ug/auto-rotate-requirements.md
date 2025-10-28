# Input file requirements for video rotation

You can use rotation for inputs that have the following video characteristics:

- Progressive video
- Chroma subsampling scheme 4:2:2 or 4:2:0
  In addition to the general input restrictions for the rotate feature, to use
  _automatic_ rotation your input file must conform to these limitations:

- Input container: .mov or .mp4
- Rotation metadata specifying 90, 180, or 270-degree rotation

If your rotation metadata is within one degree less or more than the values
listed here, the service will round to a supported value.

###### Note

If your input file has rotation metadata that specifies a rotation other than
those listed here, the service defaults to no rotation.
