# MediaTailor dynamic ad variables for ADS requests

AWS Elemental MediaTailor uses dynamic ad variables to pass information from your viewing session to the
ad decision server (ADS). This information helps the ADS select the most relevant ads for
your viewers.

This section provides an overview of dynamic ad variables and links to specific
implementation guides. For step-by-step configuration instructions, see the individual
topics below.

###### Dynamic variable types

MediaTailor supports four types of dynamic variables:

- **Session variables** – Automatically
  generated values like session ID and SCTE-35 data. See [MediaTailor session variables for ADS requests](variables-session.md "variables-session.md").
- **Player variables** – Custom parameters sent
  by your video player. See [MediaTailor player variables for ADS requests](variables-player.md "variables-player.md").
- **Domain variables** with **Configuration aliases** – Dynamic URL domains for multi-origin
  configurations.
- **Configuration aliases** – Predefined
  mappings for dynamic variable replacement. See [Configuration
  aliases](configuration-aliases-overview.md "configuration-aliases-overview.md").

###### Common use cases

Use dynamic ad variables to:

- Pass viewer demographics and preferences to your ADS
- Route requests to different origins based on geographic location
- Enable time-shifted viewing with MediaPackage integration
- Implement A/B testing and failover scenarios
  The following sections provide additional detail about using dynamic ad variables with
  MediaTailor.

###### Topics

- [Session variables](variables-session.md "variables-session.md")
- [Player variables](variables-player.md "variables-player.md")
- [Domain variables](variables-domains.md "variables-domains.md")
- [Configuration
  aliases](configuration-aliases-overview.md "configuration-aliases-overview.md")
- [Passing ADS
  parameters](passing-paramters-to-the-ads.md "passing-paramters-to-the-ads.md")
- [Parameter routing](parameter-routing-behavior.md "parameter-routing-behavior.md")
- [MediaPackage
  integration](mediapackage-integration-param.md "mediapackage-integration-param.md")
- [Session behavior](parameter-session-behavior.md "parameter-session-behavior.md")
- [Parameter
  reference](parameter-comprehensive-reference.md "parameter-comprehensive-reference.md")
- [Parameter
  troubleshooting](parameter-troubleshooting.md "parameter-troubleshooting.md")
- [Alias
  troubleshooting](configuration-aliases-troubleshooting.md "configuration-aliases-troubleshooting.md")
  For parameter formatting requirements and troubleshooting, see [MediaTailor parameter reference and
  limitations](parameter-comprehensive-reference.md "parameter-comprehensive-reference.md") and [MediaTailor parameter troubleshooting
  guide](parameter-troubleshooting.md "parameter-troubleshooting.md").
