# Tracking overlay ads with client-side metadata

MediaTailor places the overlay ads in the `nonLinearAdsList` of the avail. The
MediaTailor client-side tracking API has two root objects, called `avails` and
`nonLinearAvails`. If the VAST response is a VMAP with
`breakType` of `nonlinear`, the avail metadata is inside the
`nonLinearAvails` root object. If the VAST response is a VMAP with a
`breakType` of `linear`, or is a plain VAST response without
VMAP, the avail metadata is inside the `avails` root object.

For more information about client-side tracking, see [Client-side ad tracking](ad-reporting-client-side.md "ad-reporting-client-side.md").

The following example shows a plain VAST response or VMAP response with a
`breakType` value of `linear`.

```
{
  "avails": [
    {
      "adBreakTrackingEvents": [
        {
          "beaconUrls": [
            "`https://adserver.com/beacon=breakstartimpression`"
          ],
          "eventType": "breakStart"
        },
        {
          "beaconUrls": [
            "`https://adserver.com/beacon=breakendimpression`"
          ],
          "eventType": "breakEnd"
        }
      ],
      "adMarkerDuration": null,
      "ads": [],
      "availId": "828",
      "availProgramDateTime": null,
      "duration": "PT0S",
      "durationInSeconds": 0,
      "meta": null,
      "nonLinearAdsList": [
        {
          "extensions": null,
          "nonLinearAdList": [
            {
              "adId": "",
              "adParameters": null,
              "adSystem": "2.0",
              "adTitle": "2",
              "apiFramework": null,
              "clickThrough": null,
              "clickTracking": null,
              "clickTrackingId": null,
              "creativeAdId": "",
              "creativeId": "18",
              "creativeSequence": "",
              "duration": null,
              "durationInSeconds": 0,
              "expandedHeight": null,
              "expandedWidth": null,
              "height": "360",
              "htmlResource": null,
              "iFrameResource": null,
              "maintainAspectRatio": false,
              "minSuggestedDuration": null,
              "scalable": false,
              "staticResource": "`https://client-side-ads.com/tags/static/ctv-generic/overlay001.json?iv_geo_country%3DUS%26`",
              "staticResourceCreativeType": "text/js_ref",
              "width": "640"
            }
          ],
          "trackingEvents": [
            {
              "beaconUrls": [
                "https://adserver.com/beacon=impression"
              ],
              "duration": null,
              "durationInSeconds": 0,
              "eventId": null,
              "eventProgramDateTime": null,
              "eventType": "impression",
              "startTime": null,
              "startTimeInSeconds": 0
            }
          ]
        }
      ],
      "startTime": "PT1M46.08S",
      "startTimeInSeconds": 106.08
    }
  ],
  "dashAvailabilityStartTime": null,
  "hlsAnchorMediaSequenceNumber": null,
  "nextToken": null,
  "nonLinearAvails": []
}
```

The following example shows a plain VMAP response with a `breakType` value
of `nonlinear`.

```
{
  "avails": [],
  "dashAvailabilityStartTime": null,
  "hlsAnchorMediaSequenceNumber": null,
  "nextToken": null,
  "nonLinearAvails": [
    {
      "adBreakTrackingEvents": [
        {
          "beaconUrls": [
            "`https://adserver.com/beacon=breakstartimpression`"
          ],
          "eventType": "breakStart"
        },
        {
          "beaconUrls": [
            "`https://adserver.com/beacon=breakendimpression`"
          ],
          "eventType": "breakEnd"
        }
      ],
      "adMarkerDuration": null,
      "ads": [],
      "availId": "828",
      "availProgramDateTime": null,
      "duration": "PT0S",
      "durationInSeconds": 0,
      "meta": null,
      "nonLinearAdsList": [
        {
          "extensions": null,
          "nonLinearAdList": [
            {
              "adId": "",
              "adParameters": null,
              "adSystem": "2.0",
              "adTitle": "2",
              "apiFramework": null,
              "clickThrough": null,
              "clickTracking": null,
              "clickTrackingId": null,
              "creativeAdId": "",
              "creativeId": "18",
              "creativeSequence": "",
              "duration": null,
              "durationInSeconds": 0,
              "expandedHeight": null,
              "expandedWidth": null,
              "height": "360",
              "htmlResource": null,
              "iFrameResource": null,
              "maintainAspectRatio": false,
              "minSuggestedDuration": null,
              "scalable": false,
              "staticResource": "`https://client-side-ads.com/tags/static/ctv-generic/overlay001.json?iv_geo_country%3DUS%26`",
              "staticResourceCreativeType": "text/js_ref",
              "width": "640"
            }
          ],
          "trackingEvents": [
            {
              "beaconUrls": [
                "`https://adserver.com/beacon=impression`"
              ],
              "duration": null,
              "durationInSeconds": 0,
              "eventId": null,
              "eventProgramDateTime": null,
              "eventType": "impression",
              "startTime": null,
              "startTimeInSeconds": 0
            }
          ]
        }
      ],
      "startTime": "PT1M46.08S",
      "startTimeInSeconds": 106.08
    }
  ]
}

```
