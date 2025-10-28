# Previewing a manifest from AWS Elemental MediaPackage

Preview an endpoint's manifest to ensure that MediaPackage is receiving the content stream
and can package it. The preview is helpful for avoiding playback failures after the
endpoint is published and for troubleshooting later if there are any playback
issues.

You can use the MediaPackage console to preview playback from the endpoint.

###### To preview an endpoint's playback

1. Access the channel that the endpoint is associated with, as described in [Viewing channel details in AWS Elemental MediaPackage](channels-view.md "channels-view.md").
2. Under **Origin endpoints**, select the endpoint that you want to preview.
3. To preview playback, do one of the following:
   - Choose **Preview** to play content with the embedded player.
   - Choose **QR code** to view and scan the QR code for playback on a compatible device.
