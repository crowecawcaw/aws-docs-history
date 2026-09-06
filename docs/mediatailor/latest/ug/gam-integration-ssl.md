

# Server-side AWS Elemental MediaTailor integration with Google's ad platforms
<a name="gam-integration-ssl"></a>

MediaTailor automatically authenticates server-to-server connections with Google Ad Manager (GAM), Google Campaign Manager (GCM), and Google Display & Video 360 (DV360) using SSL certificates issued by Google to AWS Elemental MediaTailor. When MediaTailor detects ad requests or tracking events destined for Google ad servers, it automatically establishes the required secure, authenticated connection—no additional SSL certificate setup or support ticket is required.

**Prerequisite:** You must have an active account with the relevant Google ad platform (Google Ad Manager, Google Campaign Manager, or Display & Video 360).

MediaTailor applies Google-issued SSL certificate authentication based on the following destination URI rules:

**Google Ad Manager (GAM): server-side ad requests**  
+ This rule triggers on ad requests to `serverside.doubleclick.net`, including when you configure the ADS Template URL with that domain or when a redirect ad request resolves to it.
+ MediaTailor adds the `ssss=mediatailor` query parameter if it is not present, then secures the connection using a Google-issued SSL certificate.
+ This provides access to Authorized Buyers—Google's real-time ad sales marketplace and ad exchange.

**Google Ad Manager (GAM): redirected ad requests inside VMAP**  
+ This rule triggers on `pubads.g.doubleclick.net` redirected ad requests when MediaTailor has previously seen VAST redirects to `serverside.doubleclick.net` in the current request and a previous ADS response was a VMAP response.
+ MediaTailor automatically changes the domain to `serverside.doubleclick.net` and establishes an authenticated connection using the Google-issued SSL certificate.
+ This enables access to Authorized Buyers for VMAP-based ad workflows.

**Google Campaign Manager (GCM): ad-serving and tracking requests**  
+ This rule triggers on `ad.doubleclick.net` ad-serving and tracking requests when the URI contains `/ddm/pfadx/` or `/ddm/trackimp/` (encoded or unencoded).
+ MediaTailor automatically changes the domain to `serverside.doubleclick.net` and establishes an authenticated connection using the Google-issued SSL certificate.
+ This supports advertisers running campaigns on these platforms with more accurate reporting and fewer rejected impressions.

**Display & Video 360 (DV360): ad requests**  
+ This rule triggers on `bid.g.doubleclick.net` or `pagead2.googlesyndication.com` ad requests when the URI contains `/dbm/vast/` (encoded or unencoded).
+ MediaTailor automatically changes the domain to `serverside.doubleclick.net` and establishes an authenticated connection using the Google-issued SSL certificate.
+ This enables authenticated ad serving for Display & Video 360 campaigns.

All other ad requests are processed without Google-issued SSL certificate authentication.

**Note**  
SSL certificate authentication is now automatic. If you previously submitted a support ticket to enable SSL certificates, no action is needed—your configurations continue to work.