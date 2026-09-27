

# Source metadata field reference
<a name="source-metadata-field-reference"></a>

The fields returned by source metadata monitoring depend on the protocol of the incoming source. This section describes the fields for each supported protocol.

## Transport stream programs
<a name="source-metadata-fields-ts"></a>

Transport stream source metadata is available for both flows and router inputs.

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
| Channels | The number of channels in the audio stream. | 
| Sample rate | The sample rate of the audio stream, in hertz (Hz). | 