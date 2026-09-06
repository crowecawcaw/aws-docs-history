

# Scope of processing depending on outputs
<a name="scope-of-processing-depending-on-outputs"></a>

The following table summarizes which options apply to which kind of output. Following the table are details for each output type.


| Output | Passthrough in TS outputs | Manifest decoration | Blanking | 
| --- | --- | --- | --- | 
| Archive outputs with MPEG-2 as the container | Include all the original SCTE-35 messages. <br />Convert any SCTE-104 messages to SCTE-35 messages (of the same message type) and include in the TS output. | Not applicable | Applicable | 
| Archive outputs with other containers | Not applicable | Not applicable | Applicable | 
| HLS | Include all the original SCTE-35 messages. <br />Convert any SCTE-104 messages to SCTE-35 messages (of the same message type) and include in the TS output.<br />Note that, with HLS, you either implement both manifest decoration and passthrough or you implement neither. | Decorate the HLS manifest with one or more of the following types of ad markers:+  Adobe <br />+  Elemental <br />+  SCTE-35 enhanced.  | Applicable | 
| DASH | Not applicable | Not applicable | Applicable | 
| MS Smooth | Not applicable | Include information about the SCTE-35 event in the sparse track. | Applicable | 
| SMPTE 2110 |  |  |  | 
| RTMP | Not applicable | Include one or more of the following types of ad markers in the RTMP datastream:+  OnAkamaiAdPod <br />+  OnCuePoint <br />+  OnCuePoint SCTE-35 <br />+  OnUserDataEvent  | Applicable | 
| UDP/TS | Include all the original SCTE-35 messages. <br />Convert any SCTE-104 messages to SCTE-35 messages (of the same message type) and include in the TS output. | Not applicable | Applicable | 

**Topics**
+ [Archive output with MPEG-2 container](archive-output-with-mpeg-2-container.md)
+ [Archive output with other containers](archive-output-with-other-containers.md)
+ [Apple HLS output](apple-hls-output.md)
+ [DASH output](dash-output.md)
+ [MS Smooth output](ms-smooth-output.md)
+ [Adobe RTMP output](adobe-rtmp-output.md)
+ [SMPTE 2110 output](s35-scope-s2110.md)
+ [UDP/TS output](udp-ts-output.md)