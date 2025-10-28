# Client-side AWS Elemental MediaTailor integration with Google Ad

Manager

A MediaTailor client-side integration is required to use the Google Ad Manager Programmatic
Access Libraries (PAL) SDKs. This integration is required if you want to use Ad
Manager's open auction transaction type.

The PAL SDKs provide information about the content, device, and user data for a
playback session. Through the PAL SDK, you can provide this information to Google Ad
Manager, which can then make better determinations of what targeted ads to show. SDKs
are available for Android, iOS, HTML5, and Cast. For information about using the PAL
SDKs, see [Google Ad Manager
PAL SDK](https://developers.google.com/ad-manager/pal "https://developers.google.com/ad-manager/pal").

###### To create client-side integration with Ad Manager

1. Use the PAL SDK to generate a nonce.

The nonce is an encrypted string that PAL generates for stream requests. Each
request must have a unique nonce. For information about setting up a nonce,
choose your SDK from [Google Ad Manager
PAL SDK](https://developers.google.com/ad-manager/pal "https://developers.google.com/ad-manager/pal"). 2. Use the `givn` parameter in your ADS request to pass through the
nonce value. To do this, update your ADS URL to include
`&givn=`[player_params.givn]``.
For instructions, see [Enabling client-side
tracking](ad-reporting-client-side.md#ad-reporting-client-side-enabling "ad-reporting-client-side.md#ad-reporting-client-side-enabling").

###### Datazoom player SDKs

MediaTailor has partnered with Datazoom to provide free player SDKs to ease integrations
with SDKs such as those offered in the Ad Manager PAL. For information about the
Datazoom and MediaTailor partnership, see [Datazoom free
player SDKs](ad-reporting-client-side-ad-tracking-integrations.md#ad-reporting-client-side-ad-tracking-integrations-dz "ad-reporting-client-side-ad-tracking-integrations.md#ad-reporting-client-side-ad-tracking-integrations-dz").

To access the Datazoom player SDKs, use the contact information on the [Datazoom with
AWS](https://www.datazoom.io/partner-aws "https://www.datazoom.io/partner-aws") site.
