

# DASH bandwidth reporting
<a name="dash-bandwidth-reporting"></a>

In a DASH manifest, each video `Representation` element carries a `bandwidth` attribute. The `bandwidth` value tells the player how much network throughput the representation requires. Players use this value to choose which representation to request as network conditions change. With bandwidth reporting mode, you can control how AWS Elemental MediaPackage calculates this value for regular (non-iFrame) video representations.

The bandwidth reporting mode applies to the `bandwidth` attribute of regular video representations only. Audio, subtitle, image (thumbnail), and iFrame-only (trick-play) representations are not affected. The setting also doesn't change HLS, Low-Latency HLS, or MSS manifests.

**How each mode chooses the value**  
Choose between the two `BandwidthReportingMode` values based on how you want players to interpret each video representation:
+ `AVERAGE` – The `bandwidth` attribute is the average bitrate of the source video track. This is the default setting, and it matches the behavior of MediaPackage when you don't set a bandwidth reporting mode.
+ `MAX` – The `bandwidth` attribute is the peak bitrate of the video stream alone. The peak value doesn't include audio. MediaPackage derives the peak value differently depending on the ingest type of the channel:
  + For CMAF ingest (including MultiView), MediaPackage uses the maximum bitrate that the encoder signals in the CMAF `btrt` (BitRateBox) of the initialization segment.
  + For HLS (TS) ingest, MediaPackage calculates the peak from three values: the coded picture buffer (CPB) size, the average bitrate, and the endpoint segment duration. The encoder signals the CPB size in the H.264 or H.265 hypothetical reference decoder (HRD) parameters. Shorter segments produce a higher peak. MediaPackage uses the same calculation that it uses for the HLS `BANDWIDTH` attribute.

MediaPackage never reports a `MAX` value that is lower than the `AVERAGE` value. If no peak is available, MediaPackage typically reports the average bitrate instead. This can happen if the CMAF `btrt` box doesn't signal a maximum, the encoder omits HRD parameters, or the computed peak is lower than the average.

The DASH specification (ISO/IEC 23009-1) defines `bandwidth` in relation to `minBufferTime`. It describes the bandwidth that a client needs for continuous playback, which is a peak-oriented definition. When you report `MAX` values, players might choose a lower-quality representation at startup, or switch representations more conservatively, because the reported bandwidth is higher.

**Requirements and limitations**  
Keep the following in mind when you use bandwidth reporting mode:
+ Encoders that run in constant bitrate (CBR) mode often signal a CMAF `btrt` maximum bitrate that equals the average bitrate. In that case, the `MAX` value equals the `AVERAGE` value.
+ For HLS (TS) ingest, `MAX` requires the encoder to signal hypothetical reference decoder (HRD) parameters. AWS Elemental MediaLive and AWS Elemental Live signal these parameters. If the encoder omits them, MediaPackage typically reports the average bitrate.
+ A change to the bandwidth reporting mode takes effect after the cached manifests refresh.

**Example Video representation reported as AVERAGE**  
In this example, a video representation ingested over HLS (TS) has an average bitrate of 1,000,000 bps, a 2,000,000-bit buffer, and 2-second segments. With the `AVERAGE` mode, MediaPackage reports the average bitrate in the `bandwidth` attribute:  

```
<Representation id="h264_video" bandwidth="1000000" codecs="avc1.640029" frameRate="30/1" width="1280" height="720"/>
```

**Example Video representation reported as MAX**  
The following example shows the same video representation with the `MAX` mode. MediaPackage calculates the peak bitrate from the 2,000,000-bit CPB size, the 1,000,000 bps average bitrate, and the 2-second segment duration, and reports it in the `bandwidth` attribute:  

```
<Representation id="h264_video" bandwidth="1520000" codecs="avc1.640029" frameRate="30/1" width="1280" height="720"/>
```

To configure the bandwidth reporting mode for a DASH endpoint, set the `BandwidthReportingMode` field in the DASH manifest configuration. For the console steps, see [Create a DASH manifest](endpoints-create.md#dash-manifest).