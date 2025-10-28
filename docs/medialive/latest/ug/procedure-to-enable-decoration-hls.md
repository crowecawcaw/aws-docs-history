# Enabling decoration –

HLS

In an HLS output group, manifest decoration is enabled at the output group level,
which means that the manifests for all outputs in that group include instructions
based on the SCTE 35 content.

###### To enable decoration

1. In the channel that you are creating, make sure that you have set the ad
   avail mode. See [Getting ready: Set
   the ad avail mode](getting-ready-set-the-ad-avail-mode.md "getting-ready-set-the-ad-avail-mode.md").
2. In the navigation pane, find the desired HLS output group.
3. In **Ad Marker**, choose **Add ad
   markers**.
4. For **HLS ad markers**, select the type of ad marker. For
   information about the different types of markers, see [Sample manifests - HLS](sample-manifests-hls.md "sample-manifests-hls.md").
5. Repeat to add more types of markers, as desired.
   The manifest for each output will include a separate set of tags for each type
   that you select.
