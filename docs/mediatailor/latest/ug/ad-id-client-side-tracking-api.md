# Client-side tracking API

The following example shows how a player SDK links the ad metadata in
the manifest with the full tracking event data in the client-side tracking response
payload with `creativeId` and `adId`.

###### Example JSON message:

```
{
  "avails": [
    {
      "adBreakTrackingEvents": [],
      "ads": [
        {
          "adId": "5",
          "adParameters": "",
          "adProgramDateTime": null,
          "adSystem": "2.0",
          "adTitle": "AD-caribbean2-15",
          "adVerifications": [],
          "companionAds": [],
          "creativeId": "1234",
          "creativeSequence": "2",
          "duration": "PT15S",
          "durationInSeconds": 15,
          "extensions": [],
          "mediaFiles": {
            "mediaFilesList": [],
            "mezzanine": ""
          },
          "skipOffset": null,
          "startTime": "PT30S",
          "startTimeInSeconds": 30,
          "trackingEvents": [
            {
              "beaconUrls": [
                "https://`myServer`/impression"
              ],
              "duration": "PT15S",
              "durationInSeconds": 15,
              "eventId": "5",
              "eventProgramDateTime": null,
              "eventType": "impression",
              "startTime": "PT30S",
              "startTimeInSeconds": 30
            }
          ],
          "vastAdId": ""
        }
      ],
      "availId": "5",
      "availProgramDateTime": null,
      "duration": "PT15S",
      "durationInSeconds": 15,
      "meta": null,
      "nonLinearAdsList": [],
      "startTime": "PT30S",
      "startTimeInSeconds": 30
    }
  ],
  "nextToken": "UFQ1TTM0Ljk2N1NfMjAyMi0xMS0xOFQwNDozMzo1Mi4yNDUxOTdaXzE%3D",
  "nonLinearAvails": []
}
```
