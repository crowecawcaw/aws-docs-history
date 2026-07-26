# Integrating AWS Elemental MediaTailor with Google's ad platforms

MediaTailor automatically authenticates server-to-server connections with Google Ad Manager
(GAM), Google Campaign Manager (GCM), and Google Display & Video 360 (DV360). When
MediaTailor detects that an ad request or tracking event is destined for a Google ad server, it
automatically establishes the required secure, authenticated connection.

You must have an account set up with the relevant Google ad platform. MediaTailor supports the
following integration types:

- **Server-side integration**: MediaTailor automatically
  secures server-side ad requests and impression tracking requests to Google's ad
  platforms. This includes:

  - **Google Ad Manager (GAM)**: Ad requests to
    Google's ad server for publishers are automatically secured, which is
    required for access to Authorized Buyers—Google's real-time ad sales
    marketplace and ad exchange.
  - **Google Campaign Manager (GCM)**:
    Ad-serving and tracking requests are automatically routed through Google's
    authenticated endpoint and secured, supporting advertisers who run campaigns
    on these platforms with more accurate reporting and fewer rejected
    impressions.
  - **Display & Video 360 (DV360)**:
    Ad requests are automatically routed through Google's authenticated endpoint
    and secured, supporting advertisers who run campaigns on these platforms
    with more accurate reporting and fewer rejected impressions.

- **Client-side integration**: A player integration
  using the Google Programmatic Access Libraries (PAL) SDK. This integration is
  required if you want to use the open auction transaction type in Google Ad
  Manager.
  All other ad requests continue to operate without modification.

Ad Manager support for programmatic transaction types varies based on the type of
integration that you're using. For a list of available options, see [Transaction
types](https://support.google.com/admanager/answer/2805834?hl=en "https://support.google.com/admanager/answer/2805834?hl=en") or contact your Google account team.

###### Topics

- [Server-side integration](gam-integration-ssl.md "gam-integration-ssl.md")
- [Client-side integration](gam-integration-pal.md "gam-integration-pal.md")
- [Optimizing ad fill rate](gam-integration-fill-rate.md "gam-integration-fill-rate.md")
