# Server-side AWS Elemental MediaTailor integration with Google Ad

Manager

Server-side ad requests to Google Ad Manager (Ad Manager) must include the SSL
certificate that Ad Manager has issued to MediaTailor to authorize programmatic transactions.

###### To make server-side ad requests to Ad Manager

1.  [Submit an AWS
    Support ticket](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/") to request SSL certificates to be enabled. Include
    the following information in the Support ticket:

        * AWS Region
        * AWS account ID
        * MediaTailor playback configuration name

    If you don't enable SSL certificates, Ad Manager responds to MediaTailor ad requests
    with HTTP 401 error codes in the `ERROR_ADS_INVALID_RESPONSE` ADS
    interaction log event type.

2.  After SSL certificates are enabled, update the URL and parameters for your ADS
    and preroll ADS in the playback configuration. To update or create a playback
    configuration, see [MediaTailor playback configuration
    management](working-with-configurations.md "working-with-configurations.md").

For official guidance on VAST ad request URL parameters for Ad Manager, see
the Ad Manager [Server-side implementation guide.](https://support.google.com/admanager/answer/10668760 "https://support.google.com/admanager/answer/10668760") Updating includes the following
changes:

    * Change the base URL from `pubads.g.doubleclick.net` to
     `serverside.doubleclick.net`.
    * Add the parameter `ssss=mediatailor`. This indicates that
     MediaTailor is the server-side stitching source.
    * Remove the `IP` parameter. MediaTailor automatically passes in
     the end-user IP address using the `X-Forwarded-For`
     header.
    * Remove the `ss_req=1` parameter.

For updated and complete VAST URL guidance, see the [Server-side
implementation guide](https://support.google.com/admanager/answer/10668760 "https://support.google.com/admanager/answer/10668760") or contact your Google
account team.
