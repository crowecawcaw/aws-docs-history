

# Set up basic MediaTailor channel assembly with a CDN
<a name="ca-cdn-setup-basic"></a>

AWS Elemental MediaTailor channel assembly enables you to configure a basic integration with your content delivery network (CDN) for efficient delivery of linear streaming channels to your viewers. Follow these steps to set up the integration between channel assembly and your CDN.

1. Configure your CDN to accept manifests from viewers and forward them to MediaTailor channel assembly.

1. Set up MediaTailor channel assembly to access your channel schedule and determine the current programming.

1. Configure MediaTailor channel assembly to request content segments from your origin server based on the schedule.

1. Ensure your content origin can deliver the requested segments to MediaTailor channel assembly.

1. Set up MediaTailor channel assembly to generate dynamic manifests based on the current schedule.

1. Configure your CDN to deliver the assembled multivariant playlists, media playlists, and MPDs to viewers.

1. Set up your CDN to handle segment requests from viewers, with appropriate cache settings.

1. Configure your CDN to forward cache misses to MediaTailor channel assembly.

1. Set up MediaTailor channel assembly to retrieve requested segments from your content origin.

1. Configure your CDN to deliver content segments to viewers for playback.