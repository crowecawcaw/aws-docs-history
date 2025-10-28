# Prerequisites for using overlay ads with MediaTailor

The following prerequisites apply when using overlay ads with MediaTailor:

- The workflow must be live, not video on demand (VOD).
- The Ad Decision Server (ADS) response must be configured to return only
  non-linear ads in the VAST response. MediaTailor ignores any linear ads for the
  purposes of ad stitching.
- The manifest must use a SCTE-35 time signal message with segmentation type
  `id=0x38` to invoke the overlay-ad feature.
- The streaming provider must have control of the client-device application and
  be integrated with the MediaTailor client-side tracking API.
