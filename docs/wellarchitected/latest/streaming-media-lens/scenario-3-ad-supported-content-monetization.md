

# Ad-supported content monetization
<a name="scenario-3-ad-supported-content-monetization"></a>

Advertising supported monetization is achieved by either inserting or replacing advertisements in the content. Targeted and personalized advertisements lead to higher engagement and maximize the return on investment for advertisers. With a well-designed ad insertion service, you can deliver a streaming media experience to millions of concurrent viewers across a range of multiscreen devices with personalized ad content, creating a smooth, broadcast-like experience.

Tracking ad impressions is an important part of ad insertion and is accomplished through the client beaconing of quartile views as it plays ad segments. Capturing beaconing data directly from the players in this way reduces the effects of ad blocking software and adheres to established advertising open standards. Accurately measuring ad impressions and viewing behavior across web, iOS, Android, and other connected viewing devices, helps more effectively measure the revenue impact of every ad delivered.

Ad insertions can be achieved either at the client-side or server-side. Traditional client-side ad insertion requires working with various player SDKs across multiple platforms to maintain ad logic for different ad formats and content variations. In addition, ad blockers (software that blocks online advertising from being displayed) are able to detect client-side ad insertion and can limit the impressions.

By contrast, server-side video ad insertion (SSAI) is a method in which video ads are integrated into the stream at the origin. With SSAI, there is no need for the client to switch between content and the advertisement. Buffering and session initialization delay before and after the insertion of the ad are removed, providing a higher quality viewing experience. Compared to client-side ad insertion, SSAI typically improves the ad experience, impressions, and provides an opportunity to personalize advertisements. Potential challenges for SSAI implementation include linear scalability challenges for the ad insertion and decision services. Server Guided Ad Insertion (SGAI) is a related approach that uses the ad decisioning process from SSAI but has the client perform the actual ad retrieval. It can help with some of the challenges around large scale usage of SSAI.

A common approach to SSAI is shown in the following figure. In this architecture, we depict cloud services for the origin server, ad insertion service, and the content delivery network. These cloud-based services are highly available, natively redundant, and verify that the customer experience isn't degraded in the event of host-level failure.

## Reference architecture
<a name="scenario-3-reference-architecture"></a>

![Server-side ad insertion architecture showing the numbered flow between player devices, a CloudFront CDN for delivery, a MediaTailor ad insertion service, a MediaPackage origin service for origination, and an ad decision service. The CDN forwards manifest requests to MediaTailor, which retrieves the content manifest from the origin, queries the ad decision service for personalized ads, and returns a personalized manifest through the CDN to the player.](https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/images/image3.png)


1. Device requests content manifest to begin playback session.

1. The CDN forwards the request for a personalized manifest to the ad insertion service (AIS).

1. The AIS coalesces requests for the manifest from all players and forwards requests to the origin.

1. The origin responds back to the AIS with the content manifest, including any ad markers.

1. If the manifest has ad markers, the ad insertion service makes a call to the ad decision server (ADS) to get a list of personalized ads to insert for the playback session.

1. The ADS returns a Video Ad Serving Template (VAST) response with a list of personalized ads.

1. The AIS personalizes the manifest by inserting the desired ad segments at the ad marker locations, and delivers the personalized manifest to the CDN.

1. The CDN returns the personalized manifest to the player.

1. The personalized manifest points the player to content segments and ad segments.

   1. If the segment is a main content segment, the CDN passes that request to the origin.

   1. If the segment is an ad segment, the request for the segment is routed to the AIS.

   1. The origin returns the content segment.

   1. The AIS returns the ad segment.

1. CDN serves the segment to the player.

## Configuration notes
<a name="scenario-3-configuration-notes"></a>
+ Use the same AWS Region for both the ad insertion service and the origin server.
+ Use one or more CDNs to cache content and ad segments. However, personalized manifest responses must not be cached or shared between viewers (in contrast, the original content manifest might benefit from being cached to reduce the request rate against the origin from the AIS). For more information, refer to [Using a CDN to optimize MediaTailor ad personalization and content delivery](https://docs.aws.amazon.com/mediatailor/latest/ug/integrating-cdn.html).
+ Select the ad insertion service that supports inserting ads into all the desired streaming protocols, such as HLS or DASH. AWS Elemental MediaTailor supports ad insertions to HLS and DASH streaming formats for Live and VOD content.
+ Target an ad insertion latency that's less than the segment length to minimize playback rebuffering.
+ Design your client to handle a mix of encrypted and unencrypted content during playback. Content is usually encrypted while ad segments aren't.
+ To maintain consistent video quality and reliable playback when switching between main content and ad segments, verify that the ad insertion service processes advertisements to match the bit rate, frame rate, and resolution of the main content.
+ Refer to [This is My Architecture video](https://aws.amazon.com/blogs/media/this-is-my-architecture-advertising-analytics-at-scale-for-live-events-featuring-amazon-prime-video/) to learn how Amazon Prime Video scales ad measurement and tracking at scale on AWS.