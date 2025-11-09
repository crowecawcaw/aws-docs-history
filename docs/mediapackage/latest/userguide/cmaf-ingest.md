# CMAF ingest in AWS Elemental MediaPackage

AWS Elemental MediaPackage Version 2 (v2) supports CMAF ingest. CMAF ingest delivers content to viewers in
multiple streaming formats from a single ingest workflow. CMAF ingest provides flexibility
and features to optimize your streaming experience.

The topics in this section cover CMAF ingest.

## Choosing a MediaLive output group for

MediaPackage CMAF ingest

When configuring AWS Elemental MediaLive to send content to MediaPackage, you can choose between two output
group types for CMAF ingest. Your choice affects which capabilities are available for
stream control and presentation in your streaming workflow.

### When to use each output

group

Use this guidance to determine the output group that best fits your streaming
requirements:

When to use CMAF Ingest output group

- You have a simpler workflow that doesn't require custom stream
  ordering or naming
- You want to configure the system simply with minimal
  setup
- Stream order and custom properties are not critical for your
  use case

When to use MediaPackage output group

- You need additional passthrough capabilities for stream
  metadata
- You want to preserve the exact order of streams as configured
  in MediaLive
- You need enhanced control over stream presentation and
  properties

### How each output group works

CMAF Ingest output group

The CMAF Ingest output group provides straightforward CMAF ingest with
minimal configuration. MediaPackage extracts metadata from the initialization
segments and uses MP4 segments to generate manifests. This output group
requires simpler setup but provides standard stream handling.

MediaPackage output group

The MediaPackage output group enables additional passthrough
capabilities and desired stream ordering when customers choose this
output group instead of the CMAF Ingest output group. This provides
enhanced control over how streams are presented in output
manifests.

The following table compares the capabilities available with each MediaLive output
group:

| Capability comparison between MediaLive output groups | Capability                                       | CMAF Ingest Output Group                       | MediaPackage Output Group |
| ----------------------------------------------------- | ------------------------------------------------ | ---------------------------------------------- | ------------------------- |
| Stream order preservation                             | Standard (alphabetical order in output manifest) | Enhanced (preserves desired stream ordering)   |
| Stream metadata passthrough                           | Standard                                         | Enhanced (additional passthrough capabilities) |
| Setup complexity                                      | Simple                                           | More configuration options                     |

## Enhanced CMAF capabilities with

MediaPackage output groups

When using the MediaPackage output group in MediaLive, AWS Elemental MediaPackage provides additional
passthrough capabilities and desired stream ordering. These enhanced capabilities give
you greater control over how streams are presented to viewers in your streaming
applications.

### Stream ordering preservation

When you choose the MediaPackage output group in MediaLive, the desired stream
ordering configured in MediaLive is preserved in the output manifests. This allows you
to control how different video, audio, and subtitle streams appear to
viewers.

Stream ordering preservation helps you:

- Ensure viewers start with your intended default streams
- Present quality choices in your preferred order
- Organize streams logically for better viewer navigation

### Additional passthrough

capabilities

The MediaPackage output group provides additional passthrough capabilities that
enable enhanced stream metadata to be preserved from MediaLive to the output
manifests.

These capabilities support:

- Enhanced stream identification and presentation
- Improved viewer experience through better stream organization
- More control over how streams appear in player interfaces
