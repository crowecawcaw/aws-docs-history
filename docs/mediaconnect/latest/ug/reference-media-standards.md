

# Reference: Supported media standards
<a name="reference-media-standards"></a>

**Important**  
MediaConnect complies with and implements many media industry standards from different organizations. This reference is not intended to be a comprehensive list, but contains highlighted standards from specific organizations. 

## Video Services Forum: technical recommendations
<a name="reference-vsf-tr"></a>

AWS Elemental MediaConnect supports *technical recommendations (TR)* from the *Video Services Forum (VSF)* for some features. This reference guide can be used to identify which TRs are supported by MediaConnect. For more information about technical recommendations, visit the VSF website: [VSF technical recommendations](https://www.videoservicesforum.org/technical_recommendations.shtml)


**Supported VSF technical recommendations**  

| Technical recommendation | Description | 
| --- | --- | 
| TR-06-01: Reliable Internet Stream Transport (RIST) [Simple Profile] | This technical recommendation is for RIST Simple Profile support only. MediaConnect does not support Main, Enhanced, or Scalable Profiles when using RIST.  | 
| TR-07: Transport of JPEG XS Video in MPEG-2 Transport Stream (TS) over IP TR-07 is automatically invoked when you use a supported protocol and the maximum bitrate is greater than 200 Mbps.  | MediaConnect supports JPEG XS transport in MPEG-2 TS over IP with the following requirements and limitations:+  As a source:    Only a redundant RTP or RTP-FEC protocol is supported.   The maximum source bitrate is 500 Mbps.   TR-07 sources cannot be entitled.   <br />+  As an output:    The output protocol can be RTP or RTP-FEC.   Up to four total outputs can be used, but aggregate bandwidth must not exceed 1250 Mbps.    | 
| TR-08: Transport of JPEG XS Video in ST 2110-22 For JPEG XS passthrough flows where the video frames are not encoded by MediaConnect, the video frames are not decoded. As a result, no validation of TR-08 compliance is performed.  | MediaConnect supports JPEG XS transport over SMPTE ST 2110-22 with the following requirements and limitations:+  A High profile is required. Using the Main profile will not cause errors, but will be ignored by MediaConnect. <br />+  An interlace mode of 01 (top-field first) is required for interlaced signals. <br />+  A sublevel of either 3 bits-per-pixel or 4 bits-per-pixel is required. The sublevel depends on the level of compression and pixel bit depth you are using. <br />+  Video Description Boxes placed in the encoded video frames will reflect compliant values for profile, interlace mode, and sublevel. <br />+  Networked Media Open Specification (NMOS) registration is not supported. <br />+  Real-time Transport Protocol (RTP) sequential packet transmission mode only. <br />+  Codestream packetization mode only. Slice mode is not supported. Supported color space, bit depth, and chroma sampling configurations:+  YCbCr 10-bit 4:2:2 <br />+  RGB 10-bit 4:4:4 <br />+  RGB 12-bit 4:4:4  | 

## SMPTE-2022
<a name="reference-media-standards-smpte-2022"></a>

MediaConnect supports many SMPTE (Society of Motion Picture and Television Engineers) standards. The following table is specific to SMPTE-2022 and includes a selection of standards. It is not a comprehensive list of all supported SMPTE standards. 


**Supported SMPTE-2022 standards**  

| Standard | Description | 
| --- | --- | 
| SMPTE-2022-7: Seamless Protection Switching of RTP |  +  Sources: MediaConnect supports RTP sources that comply with this standard. For more information about source failover, see [Source failover](source-failover.md) <br />+  Outputs: RTP and RTP-FEC outputs are compliant with the SMPTE 2022-7 standard. If your downstream receiver supports 2022-7 source merging, RTP and RTP-FEC outputs will be compatible.   | 