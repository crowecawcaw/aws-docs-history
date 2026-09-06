

# Usage type components
<a name="billing-usage-type-components"></a>

The following table describes each component that can appear in an MediaLive usage type string.


| Component | Values | Description | 
| --- | --- | --- | 
| Tier | EML1, EML2, EMLA | EML1 = Single pipeline, EML2 = Standard (dual) pipeline, EMLA = MediaLive Anywhere | 
| Region | AWS Region code | Abbreviated region identifier. For example, USE1 = US East (N. Virginia), EUC1 = EU (Frankfurt), APN1 = Asia Pacific (Tokyo). | 
| Direction | IN, OUT | IN = Input processing, OUT = Output processing | 
| Codec | AVC, HEVC, MPEG2, AV1, CDI | AVC (H.264), HEVC (H.265), MPEG2, AV1, CDI (Cloud Digital Interface) | 
| Resolution | SD, HD, FHD, UHD | SD = Standard Definition, HD = High Definition, FHD = Full HD, UHD = Ultra HD | 
| Input bitrate level | L10, L20, L50 | L10 = less than 10 Mbps, L20 = 10–20 Mbps, L50 = 20–50 Mbps | 
| Output framerate | 30, 60 | 30 = up to 30 fps, 60 = 30–60 fps | 
| Video quality | S, E | S = Standard VQ, E = Enhanced VQ | 
| Reservation | -R suffix or no suffix | -R suffix = reserved capacity pricing, no suffix = on-demand | 