# MediaTailor server-side ad tracking and

reporting

AWS Elemental MediaTailor defaults to server-side reporting for comprehensive ad tracking and measurement.
With server-side reporting, when the player requests an ad URL from the manifest, the
service reports ad consumption directly to the ad tracking URL. After the player initializes
a playback session with MediaTailor, no further input is required from you or the player
to perform server-side reporting. As each ad is played back, MediaTailor sends beacons to
the ad server to report how much of the ad has been viewed. MediaTailor sends beacons for
the start of the ad and for the ad progression in quartiles: the first quartile, midpoint,
third quartile, and ad completion.

###### To perform server-side ad reporting

- From the player, initialize a new MediaTailor playback session using a request
  in one of the following formats, according to your protocol:

      + Example: HLS format



      ```
      GET `<mediatailorURL>`/v1/master/`<hashed-account-id>`/`<origin-id>`/`<asset-id>`?ads.`<key-value-pairs-for-ads>`&`<key-value-pairs-for-origin-server>`
      ```
      + Example: DASH format



      ```
      GET `<mediatailorURL>`/v1/dash/`<hashed-account-id>`/`<origin-id>`/`<asset-id>`?ads.`<key-value-pairs-for-ads>`&`<key-value-pairs-for-origin-server>`
      ```

  The key-value pairs are the dynamic targeting parameters for ad tracking. For
  information about adding parameters to the request, see [MediaTailor dynamic ad variables for ADS requests](variables.md "variables.md").
  AWS Elemental MediaTailor responds to the request with the manifest URL. The manifest contains
  URLs for the media manifests. The media manifests contain embedded links for ad segment
  requests.

###### Note

When MediaTailor encounters a double-slash (//) in a tracking URL, it collapses the slashes
to one (/).

When the player requests playback from an ad segment URL (`/v1/segment` path),
AWS Elemental MediaTailor sends the appropriate beacon to the ad server through the ad tracking
URLs. At the same time, the service issues a redirect to the actual `*.ts` ad
segment. The ad segment is either in the Amazon CloudFront distribution where MediaTailor stores
transcoded ads, or in the content delivery network (CDN) where you have cached the ad.

The following sections provide more information about working with server-side ad tracking
from MediaTailor.

###### Topics

- [Beacon
  glossary](ad-reporting-server-side-beacon-glossary.md "ad-reporting-server-side-beacon-glossary.md")
- [Timing and
  caching behavior](ad-reporting-server-side-timing-behavior.md "ad-reporting-server-side-timing-behavior.md")
- [Tracking
  features](ad-reporting-server-side-features.md "ad-reporting-server-side-features.md")
