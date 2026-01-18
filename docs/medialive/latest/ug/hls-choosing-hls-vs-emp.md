# Choosing between the HLS output group and

MediaPackage output group

If you want to deliver HLS output to AWS Elemental MediaPackage, you must decide if you want to create an
HLS output group or a MediaPackage output group.

## Delivering to MediaPackage v2

If you are delivering to a MediaPackage channel that uses MediaPackage v2, you must create an HLS
output group. The MediaPackage operator can tell you if the channel uses version 2 of the API. One
use case for using version 2 is to implement a glass-to-glass low latency workflow that
includes both MediaLive and MediaPackage.

## Delivering to standard MediaPackage (v1)

There are differences in the setup of each type of output group:

- The MediaPackage output requires less setup. AWS Elemental MediaLive is already set up with most
  of the information that it needs to package and deliver the output to the AWS Elemental MediaPackage
  channel that you specify. This easier setup has benefits, but it also has drawbacks
  because you can't control some configuration. For information about how MediaLive sets up a
  MediaPackage output group, see [Result of this
  procedure](mediapackage-create-result.md "mediapackage-create-result.md").
- For a MediaPackage output, the MediaLive channel and the AWS Elemental MediaPackage channel must be in
  the same AWS Region.
- In a MediaPackage output, there are some restrictions on setting up ID3 metadata.
  For details, see [Working with ID3 metadata](id3-metadata.md "id3-metadata.md").
