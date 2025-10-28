# Client-side ad-tracking

integrations

This section describes integrations between MediaTailor and various client-side ad-tracking
servers.

###### Topics

- [Open Measurement SDK](#ad-reporting-client-side-ad-tracking-integrations-open-measurement-sdk "#ad-reporting-client-side-ad-tracking-integrations-open-measurement-sdk")
- [Datazoom free
  player SDKs](#ad-reporting-client-side-ad-tracking-integrations-dz "#ad-reporting-client-side-ad-tracking-integrations-dz")
- [Roku Advertising
  Framework (RAF)](#ad-reporting-client-side-ad-tracking-integrations-raf "#ad-reporting-client-side-ad-tracking-integrations-raf")
- [TheoPlayer](#ad-reporting-client-side-ad-tracking-integrations-theoplayer "#ad-reporting-client-side-ad-tracking-integrations-theoplayer")
- [MediaTailor SDK](#ad-reporting-client-side-ad-tracking-integrations-mediatailor-sdk "#ad-reporting-client-side-ad-tracking-integrations-mediatailor-sdk")

## Open Measurement SDK

The Interactive Advertising Bureau (IAB) Open Measurement SDK (OM SDK) facilitates
third-party viewability and verification measurement for ads served to web-video and
native-app environments.

For older VAST version 3 documents, verification code should be loaded with the
Extension node, with extension type `AdVerifications`. The root of the
extension node is an `AdVerifications` node with the same schema as the VAST
4.1 element.

To facilitate easier adoption of the OM SDK, MediaTailor has partnered with Datazoom to
provide free player SDKs that are configured and verified for Open Measurement. For more
information, see [Datazoom free
player SDKs](#ad-reporting-client-side-ad-tracking-integrations-dz "#ad-reporting-client-side-ad-tracking-integrations-dz").

###### Note

MediaTailor currently supports VAST version 3 only.

###### Example : Verification node in VAST 3, prior to Version 4.1

```
...
<Extensions>
    <Extension type="AdVerifications">
        <AdVerifications>
            <Verification vendor="company.com-omid">
                <JavaScriptResource apiFramework="omid" browserOptional="true">
                    <![CDATA[https://verification.com/omid_verification.js]]>
                </JavaScriptResource>
                <TrackingEvents>
                    <Tracking event="verificationNotExecuted">
                        <![CDATA[https://verification.com/trackingurl]]>
                    </Tracking>
                </TrackingEvents>
                <VerificationParameters>
                    <![CDATA[verification params key/value pairs]]>
                </VerificationParameters>
            </Verification>
        </AdVerifications>
    </Extension>
</Extensions>
```

MediaTailor extracts the `AdVerifications` data from the
`<Extensions>` node and places it into the
`adVerifications` array in the client-side tracking response.

###### Example : adVerifications array in client-side tracking response

```
{
  "avails": [
    {
      "adBreakTrackingEvents": [],
      "adMarkerDuration": null,
      "ads": [
        {
          "adId": "3062770",
          "adParameters": "",
          "adProgramDateTime": "2023-08-23T16:25:40.914Z",
          "adSystem": "2.0",
          "adTitle": "AD-polarbear-15",
          "adVerifications": [
            {
              "executableResource": [],
              "javaScriptResource": [
                {
                  "apiFramework": "omid",
                  "browserOptional": "true",
                  "uri": "https://verification.com/omid_verification.js"
                }
              ],
              "trackingEvents": [
                {
                  "event": "verificationNotExecuted",
                  "uri": "https://verification.com/trackingurl"
                }
              ],
              "vendor": "company.com-omid",
              "verificationParameters": "verification params key value pairs"
            }
          ],
          "companionAds": [],
          "creativeId": "00006",
          "creativeSequence": "1",
          "duration": "PT14.982S",
          "durationInSeconds": 14.982,
          "extensions": [
            {
              "content": "<AdVerifications>\n\t\t\t\t\t\t<Verification vendor=\"`company.com-omid`\">\n\t\t\t\t\t\t\t<JavaScriptResource apiFramework=\"`omid`\" browserOptional=\"true\"><![CDATA[`https://verification.com/omid_verification.js`;]]></JavaScriptResource>\n\t\t\t\t\t\t\t<TrackingEvents>\n\t\t\t\t\t\t\t\t<Tracking event=\"verificationNotExecuted\"><![CDATA[`;https://verification.com/trackingurl`;]]></Tracking>\n\t\t\t\t\t\t\t</TrackingEvents>\n\t\t\t\t\t\t\t<VerificationParameters><![CDATA[`verification params key/value pairs`;]]></VerificationParameters>\n\t\t\t\t\t\t</Verification>\n\t\t\t\t\t</AdVerifications>",
              "type": "AdVerifications"
            }
          ],
          "mediaFiles": {
            "mediaFilesList": [],
            "mezzanine": ""
          },
          "skipOffset": null,
          "startTime": "PT10.11S",
          "startTimeInSeconds": 10.11,
          "trackingEvents": [
            {
              "beaconUrls": [
                "https://n8ljfs0h09.execute-api.us-west-2.amazonaws.com/v1/impression"
              ],
              "duration": "PT14.982S",
              "durationInSeconds": 14.982,
              "eventId": "3062770",
              "eventProgramDateTime": null,
              "eventType": "impression",
              "startTime": "PT10.11S",
              "startTimeInSeconds": 10.11
            }
          ],
          "vastAdId": ""
        }
      ],
      "availId": "3062770",
      "availProgramDateTime": "2023-08-23T16:25:40.914Z",
      "duration": "PT14.982S",
      "durationInSeconds": 14.982,
      "meta": null,
      "nonLinearAdsList": [],
      "startTime": "PT10.11S",
      "startTimeInSeconds": 10.11
    }
  ],
  "dashAvailabilityStartTime": null,
  "hlsAnchorMediaSequenceNumber": null,
  "nextToken": "UFQxMC4xMVNfMjAyMy0wOC0yM1QxNjoyNjoyNC4yNDYxMDIxOTBaXzE%3D",
  "nonLinearAvails": []
}
```

###### Note

Engage with the IAB Tech Lab to ensure that applications are certified annually to
ensure compliance.

For more information about the OM SDK, see [Open Measurement SDK](https://iabtechlab.com/standards/open-measurement-sdk/ "https://iabtechlab.com/standards/open-measurement-sdk/") on the IAB Tech Lab website.

## Datazoom free

player SDKs

To facilitate easier adoption of the player SDKs, MediaTailor has partnered with Datazoom to
provide free player SDKs that are configured and tested with the [Client-side AWS Elemental MediaTailor integration with Google Ad
Manager](gam-integration-pal.md "gam-integration-pal.md") and the
IAB Tech [Open Measurement SDK](#ad-reporting-client-side-ad-tracking-integrations-open-measurement-sdk "#ad-reporting-client-side-ad-tracking-integrations-open-measurement-sdk").

The Datazoom player SDK supports these features:

- Live and VOD playlists
- DASH and HLS specifications
- Player vendor support for Bitmovin, exoplayer, Android media player, Apple
  AVPlayer, Brightcove, Chromecast Receiver, Dash.js, hls.js, JWPlayer, Shaka
  player, THEO player, Video.js, Roku and more
- IAB Tech Lab Open Measurement certification, where available on selected
  devices
- Click-through event handling
- Ad-event dispatchers, such as ad count down timers, ad overlay and non-linear
  events, ad-break start, ad-break end
- Client-side ad beaconing
- Google Programmatic Access Library (PAL) SDK, as an optional configuration
  setting

Datazoom also offers a paid analytics and telemetry service that the player SDKs
support. Customers can opt into and control player SDK telemetry from the Datazoom
management console. To access the Datazoom player SDKs and to learn more about the
value-added telemetry and analytics service, use the contact information on the [Datazoom site](https://www.datazoom.io/partner-aws "https://www.datazoom.io/partner-aws").

## Roku Advertising

Framework (RAF)

The Roku Ad Framework (RAF) maintains a consistent ad experience across the Roku
platform. All channels, including video advertisements, must meet Roku's certification
requirements for RAF. Notably, the app must always use client-side event firing through RAF.
MediaTailor, as a server-side ad insertion (SSAI) provider, supports client-side event firing. The
RAFX SSAI Adapters provide interfaces to both SSAI manifest servers, or stitchers, and
RAF. These interfaces include:

- Parsing the `masterURL` response and extracting
  `playURL`, `AdURL`, and ad metadata.
- Transforming MediaTailor SSAI ad metadata into RAF-usable ad metadata, and
  configuring RAF for playback.
- Observing stream events and timed metadata.
- Matching the stream events, ad metadata, and firing-event pixels on
  time.
- Pinging/polling the `AdURL`, as required by the MediaTailor SSAI manifest
  server, then parsing and re-configuring RAF.

For more information about SSAI adapters for RAF, see [Implementing Server-Side Ad Insertion Using Roku Adapters](https://developer.roku.com/docs/developer-program/advertising/ssai-adapters.md "https://developer.roku.com/docs/developer-program/advertising/ssai-adapters.md") on the Roku
website.

## TheoPlayer

TheoPlayer integration with MediaTailor does the following:

- Provides functionality to support MediaTailor client-side event tracking
  for HLS and DASH for both VOD and live workflows.
- Supports sending tracking beacons only for linear ads.
- Disables seeking during an ad. However, no logic is in place for playing an ad when the user seeks
  past the ad break.

For more information about SSAI in TheoPlayer, and to review the web, Android, iOS,
and tvOS SDKs for MediaTailor, see [MediaTailor](https://docs.theoplayer.com/how-to-guides/01-ads/12-mediatailor.md "https://docs.theoplayer.com/how-to-guides/01-ads/12-mediatailor.md") on the TheoPlayer website.

## MediaTailor SDK

AWS Elemental maintains a JavaScript-based software-development kit
(SDK). AWS Elemental provides the SDK as-is, with no
implied warranty. Use the SDK as a reference demonstration to streamline your onboarding
to using MediaTailor. The SDK shows how to interact with the MediaTailor client-side tracking API.
The SDK implements client-side ad tracking and reporting for HTML5-based players. The
SDK initializes a MediaTailor client-side reporting session, then periodically requests
ad-tracking information. During playback, the SDK emits ad tracking events when new
ad events are detected.

The MediaTailor SDK supports these features:

- Live and VOD playlists
- DASH and HLS specifications
- Click-through event handling
- Ad-event dispatchers
- Custom event hooks
- Client-side ad beaconing. For more information about sending ad beacons,
  see [Client-side beaconing](ad-reporting-client-side-beaconing.md "ad-reporting-client-side-beaconing.md").

###### Note

Submit an AWS Support ticket to receive a sample JavaScript SDK for MediaTailor.
You'll receive a download link for the package and its files.
