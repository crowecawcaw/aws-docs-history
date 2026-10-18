

# Source metadata field reference
<a name="source-metadata-field-reference"></a>

The fields returned by source metadata monitoring depend on the protocol of the incoming source. This section describes the fields for each supported protocol.

## Transport stream programs
<a name="source-metadata-fields-ts"></a>

Transport stream source metadata is available for both flows and router inputs.

The following fields describe the source's transport stream.

Transport stream ID  
The transport stream ID of the source, from the Program Association Table (PAT).

The **programs** section contains information about the individual programs contained in the transport stream. This section contains the following fields:


| Field | Details | 
| --- | --- | 
| Program number | The program number of the program. | 
| Program PID | The program Packet Identifier (PID). | 
| PCR PID | The Program Clock Reference (PCR) PID of the program. | 
| Program name | The name of the program. The program name is sourced from the service name value in the Service Description Table (SDT).  | 
| Streams | The nested sections contain info about the video, audio, and data stream types. | 

The **streams** section is nested within each individual transport stream program. This section contains the following fields:


| Field | Details | 
| --- | --- | 
| Stream type | The type of content that the stream contains. This value can be video, audio, data, or unknown. | 
| Codec | The codec of the stream. This value will vary depending on the type of stream. Example: a video stream type might display a value of H264 while an audio stream type displays AAC. | 
| PID | The Packet Identifier (PID) of the stream. | 
| Frame rate | The frame rate of the video stream, displayed in frames-per-second (fps). | 
| Frame resolution | The resolution of the video stream. In the console, this field will display the frame width followed by the frame height. Example: A frame width of 1920 and a frame height of 1080 is displayed in the console as `1920 x 1080`.<br />In the API/CLI response, the frame height and frame width are displayed as separate values.  | 
| Color | The color signaling of the video stream: colorimetry, transfer characteristics, and matrix coefficients. For information about the possible values, see [Video color information](#source-metadata-fields-color). | 
| Channels | The number of channels in the audio stream. | 
| Sample rate | The sample rate of the audio stream. In the API/CLI response, the sample rate is displayed in hertz (Hz). In the console, the sample rate is displayed in Hz, unless it exceeds 1000 Hz, then it is displayed in kilohertz (kHz). | 
| Sample size | The sample size of the audio stream. The sample size is displayed in bits. | 

## NDI® media streams
<a name="source-metadata-fields-ndi"></a>

NDI source metadata is available for flows only. The **streams** section contains information about the individual media streams that make up the Network Device Interface (NDI®) source. This section contains the following fields:


| Field | Details | 
| --- | --- | 
| Stream type | The type of content that the stream contains. This value can be video, audio, or data. | 
| Codec | The codec of the stream. | 
| Stream ID | A unique identifier for the media stream. | 
| Scan mode | The method used to display video frames, such as progressive or interlace. | 
| Frame rate | The frame rate of the video stream, in frames per second (fps). | 
| Frame resolution | The resolution of the video stream. In the console, this field displays the frame width followed by the frame height, such as 1920 x 1080. In the API/CLI response, the frame width and frame height are separate values. | 
| Color | The color signaling of the video stream: colorimetry, transfer characteristics, and matrix coefficients. For information about the possible values, see [Video color information](#source-metadata-fields-color). | 
| Channels | The number of channels in the audio stream. | 
| Sample rate | The sample rate of the audio stream, in hertz (Hz). | 

## Video color information
<a name="source-metadata-fields-color"></a>

Each video stream contains a nested color section, for both transport stream and NDI sources. Each value corresponds to a code point defined in [Recommendation ITU-T H.273](https://www.itu.int/rec/T-REC-H.273) on the International Telecommunication Union (ITU) website. Each field appears only when the stream signals one of the values listed for that field.


| Field | Details | 
| --- | --- | 
| Colorimetry | The color primaries of the video stream. This field can have one of the following values:+  `BT709` <br />+  `BT470M` <br />+  `BT470BG` <br />+  `BT601` <br />+  `SMPTE240M` <br />+  `GENERIC_FILM` <br />+  `BT2020` <br />+  `SMPTE428` <br />+  `SMPTE431` <br />+  `SMPTE432`  | 
| Transfer characteristics | The transfer function of the video stream. For example, `BT2100_PQ` and `BT2100_HLG` indicate high dynamic range (HDR) video. This field can have one of the following values:+  `BT709` <br />+  `BT470M` <br />+  `BT470BG` <br />+  `BT601` <br />+  `SMPTE240M` <br />+  `LINEAR` <br />+  `LOG100` <br />+  `LOG316` <br />+  `IEC61966_2_4` <br />+  `BT1361_ECG` <br />+  `IEC61966_2_1` <br />+  `BT2020_10` <br />+  `BT2020_12` <br />+  `BT2100_PQ` <br />+  `SMPTE428` <br />+  `BT2100_HLG`  | 
| Matrix coefficients | The matrix for deriving the luma and chroma signals from the RGB signals. This field can have one of the following values:+  `IDENTITY` <br />+  `BT709` <br />+  `FCC` <br />+  `BT470BG` <br />+  `BT601` <br />+  `SMPTE240M` <br />+  `YCGCO` <br />+  `BT2020_NCL` <br />+  `BT2020_CL` <br />+  `SMPTE2085` <br />+  `CHROMATICITY_DERIVED_NCL` <br />+  `CHROMATICITY_DERIVED_CL` <br />+  `BT2100_ICTCP` <br />+  `IPT_C2`  | 