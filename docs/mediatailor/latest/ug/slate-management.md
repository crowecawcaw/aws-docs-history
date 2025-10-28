# MediaTailor slate ad insertion

###### Note

Slate is only available for live and live-to-VOD workflows.

With AWS Elemental MediaTailor, you can designate a _slate ad_ for ad breaks. A
slate is a default MP4 asset that is inserted into a stream, such as a still image or
looped video, that plays instead of the live content.

AWS Elemental MediaTailor shows slate during ad breaks in the following specific situations:

- To fill in time remaining in a break that has not been replaced by
  personalized ads
- If the Ad Decision Server (ADS) responds with an empty VAST or VMAP
  response
- For error conditions, such as ADS timeout or HTTP 500 error from the
  ADS
- If an ad isn't available for insertion by MediaTailor (such as when it hasn't
  finished transcoding)
  If you don't configure a slate, MediaTailor defaults to the underlying content
  stream when one of the above conditions is met.

## Configuring the slate

You designate the slate in the **additional configuration** pane
in the [MediaTailor console](https://console.aws.amazon.com/console/home?nc2=h_ct&src=header-signin "https://console.aws.amazon.com/console/home?nc2=h_ct&src=header-signin"). MediaTailor downloads the slate from the URL
that you specify, and transcodes it to the same renditions as your content. You can
control the maximum amount of time that a slate will be shown through the optional
**personalization threshold** configuration in the MediaTailor
console. For more information, see [How personalization threshold
works](#personalization-threshold-scenarios "#personalization-threshold-scenarios").

The slate must be a high-quality MP4 asset that contains both audio and video.
Configuring the slate is optional for non-VPAID configurations but mandatory for
VPAID workflows.

###### Note

If the server that hosts your slate uses HTTPS, its certificate must be from a
well-known certificate authority. It can't be a self-signed certificate. If you
use a self-signed certificate, then AWS Elemental MediaTailor can't retrieve and stitch
the slate into the manifests from the content origin.

## How personalization threshold

works

The personalization threshold defines the maximum duration of underfilled ad time (in seconds) allowed in an ad break. This feature applies specifically to ad replacement in Live and VOD streams, rather than ad insertion, because it relies on an underlying content stream.

The behavior varies based on three scenarios:

1. **When personalization is disabled:**
   1. Slate will be inserted for the full duration of unfilled time
   2. Start/End bumpers will be inserted when configured (for more information, see [MediaTailor bumper ad insertion](bumpers.md "bumpers.md"))
   3. Ads will be inserted as normal

2. **When personalization is enabled and threshold less
   than break duration:**
   1. If the unfilled time exceeds the personalization threshold:
      1. MediaTailor abandons personalization of the ad break
      2. The underlying content is shown
      3. No ads, slate, or bumpers are inserted

   2. If the unfilled time is less than the personalization threshold:
      1. Ads and slate are inserted
      2. Bumpers are inserted if configured

3. **When personalization is enabled and threshold
   greater than break duration:**
   1. Ads will be inserted
   2. Slate will be inserted for any remaining time in the ad break
   3. Bumpers will be inserted if configured

The following table provides detailed behaviors for specific scenarios across both HLS and DASH protocols:

| Detailed behavior matrix                                        | Scenario                                     | Personalization disabled                                                                                                      | Personalization enabled less than break duration | Personalization enabled greater than break duration                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------------------------------------------------------- | -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Empty VAST or VMAP                                              | Slate inserted                               | No slates inserted                                                                                                            | Slate inserted                                   |
| ADS timeout                                                     | Slate inserted                               | No slates inserted                                                                                                            | Slate inserted                                   |
| Ad isn't available (Vast 404)                                   | Slate inserted                               | No slates inserted                                                                                                            | Slate inserted                                   |
| Duration of ads is longer than ad break                         | Ads inserted                                 | No ads inserted                                                                                                               | Ads inserted                                     |
| Fill in time that's not fully used by an ad replacement         | Slate inserted                               | If personalization threshold greater than unfilled time: No ads/slates inserted, else: Ads and slates inserted                | Slate inserted                                   |
| Preroll with empty VAST                                         | Slate inserted, no preroll inserted          | No slates inserted, no preroll inserted                                                                                       | Slate inserted, no preroll inserted              |
| Preroll with ADS timeout                                        | Slate inserted, no preroll inserted          | No slates inserted, no preroll inserted                                                                                       | Slate inserted, no preroll inserted              |
| Preroll when ad isn't available (Vast 404)                      | Slate inserted, no preroll inserted          | No slates inserted, no preroll inserted                                                                                       | Slate inserted, no preroll inserted              |
| Bumpers with empty VAST                                         | Slate inserted, bumper inserted              | No slates inserted, no bumpers inserted                                                                                       | Slate inserted, bumper inserted                  |
| Bumpers with ADS timeout                                        | Slate inserted, bumper inserted              | No slates inserted, no bumpers inserted                                                                                       | Slate inserted, bumper inserted                  |
| Bumpers when ad isn't available (Vast 404)                      | Slate inserted, bumper inserted              | No slates inserted, no bumpers inserted                                                                                       | Slate inserted, bumper inserted                  |
| Bumpers to fill in time that's not fully used by ad replacement | Slate inserted, bumper inserted, ad inserted | If personalization threshold greater than unfilled time: No bumpers/ads/slates inserted, else: No bumpers/ads/slates inserted | Slate inserted, bumper inserted, ad inserted     | ###### Important considerations Remember the following when you're working with slate and personalization threshold. <br>• This behavior is consistent across both HLS and DASH protocols <br>• The personalization threshold feature only applies when slate is configured <br>• When slate is configured and personalization threshold is not configured, slate will play for either the full origin avail duration or whatever time remains after filling in the ads <br>• For VPAID ads, MediaTailor inserts slate for the duration of the VPAID ad to hold space for ads that the video player will insert ## Slate configuration and VPAID ###### Important Slate configuration is mandatory when using VPAID ads. MediaTailor inserts slate to hold space for VPAID ads that the video player will insert. The slate duration might be slightly longer than the VPAID ad duration to accommodate user interactivity. The video player then handles the VPAID ad based on the client-side reporting metadata that MediaTailor returns, as described in [VPAID requirements](vast.md#vpaid "vast.md#vpaid"). For information about client-side reporting, see [Client-side ad tracking](ad-reporting-client-side.md "ad-reporting-client-side.md"). |
