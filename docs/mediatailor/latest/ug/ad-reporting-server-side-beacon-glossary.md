

# Server-side tracking beacon glossary
<a name="ad-reporting-server-side-beacon-glossary"></a>

MediaTailor server-side tracking uses a standardized set of beacons to report ad viewing progress to ad servers and verification services. These beacons align with Interactive Advertising Bureau (IAB) standards for video ad measurement and provide accurate reporting of ad impressions and completion rates.


**Server-side tracking beacon types**  

| Beacon Type | When Fired | Purpose | Timing Details | 
| --- | --- | --- | --- | 
| Impression | When the player requests the first ad segment | Indicates that ad content has begun loading and is about to be displayed to the viewer | Fired on the first /v1/segment request for an ad. Aligns with IAB guidelines requiring ad content to begin loading before counting an impression. See [Server-side tracking workflow](ad-reporting-server-side-timing-behavior.md#ad-reporting-server-side-timing-behavior-workflow) for the complete sequence. | 
| Start | When the player begins rendering the ad content | Confirms that ad playback has actually started | Typically fired simultaneously with the impression beacon on the first segment request, but represents the actual start of ad rendering. This distinction is important for verification services that track both impression and start events separately. | 
| First Quartile | When the player reaches 25% of the ad duration | Measures continued ad viewing through the first quarter of the ad | Fired when the player requests the segment that contains the 25% point of the ad duration. For example, in a 20-second ad with 2-second segments, this would typically fire on the request for the 3rd segment (at approximately 4-6 seconds into the ad). | 
| Midpoint | When the player reaches 50% of the ad duration | Measures continued ad viewing through half of the ad | Fired when the player requests the segment that contains the 50% point of the ad duration. For example, in a 20-second ad with 2-second segments, this would typically fire on the request for the 5th segment (at approximately 8-10 seconds into the ad). | 
| Third Quartile | When the player reaches 75% of the ad duration | Measures continued ad viewing through three-quarters of the ad | Fired when the player requests the segment that contains the 75% point of the ad duration. For example, in a 20-second ad with 2-second segments, this would typically fire on the request for the 8th segment (at approximately 14-16 seconds into the ad). | 
| Complete | When the player reaches the end of the ad | Confirms that the entire ad was delivered to the viewer | Fired when the player requests the final segment of the ad. This indicates that the viewer has potentially seen the entire ad content. For example, in a 20-second ad with 2-second segments, this would typically fire on the request for the 10th segment (at approximately 18-20 seconds into the ad). | 

**Note**  
The exact timing of beacon firing depends on the segment duration and ad length. MediaTailor calculates the appropriate segment request that corresponds to each quartile position based on the specific ad duration and segment structure.