

# Setting up using the REST API
<a name="setting-up-via-the-rest-api"></a>

This topic lists the parameters found on the Elemental Live event or profile and specifies the location of those parameters in the XML for an event or profile. This topic does not cover control of SCTE-35 message via the REST API at runtime; that information is in [SCTE-35 message insertion into currently running events](scte-35-message-insertion.md). 


**Set the Ad Avail Mode**  

| Field | XML Tag | 
| --- | --- | 
| Advanced Avail Controls > Ad Avail Trigger | ad\_trigger | 


**Manifest Decoration**  

| Field | XML Tag | 
| --- | --- | 
| Output Group > Apple HLS > Advanced > Ad Markers | output\_group/apple\_live\_group\_settings/ad\_markers | 
| Output Group > MS Smooth > Enable Sparse Track | output\_group/ms\_smooth\_group\_settings/enable\_sparse\_track | 
| Output Group > MS Smooth > Acquisition Point ID | output\_group/ms\_smooth\_group\_settings/acquisition\_point\_id | 
| Output Group > RTMP> Ad Markers | output\_group/rtmp\_group\_settings/ad\_markers | 


**Ad Avail Blanking and Blackout**  

| Field | XML Tag | 
| --- | --- | 
| Advanced Avail Controls > Ignore no\_regional\_blackout\_flag | ignore\_no\_regional\_blackout\_flag | 
| Advanced Avail Controls > Ignore web\_delivery\_allowed\_flag | ignore\_web\_delivery\_allowed\_flag | 
| Processors > Global Processors > Ad Avail Blanking > On/Off | avail\_blanking/enabled/ | 
| Processors > Global Processors > Ad Avail Blanking > Browse | avail\_blanking/avail\_blanking\_image/certificate\_file | 
| Processors > Global Processors > Ad Avail Blanking > Browse | avail\_blanking/avail\_blanking\_image/interface | 
| Processors > Global Processors > Ad Avail Blanking > Credentials icon > Password | avail\_blanking/avail\_blanking\_image/password | 
| Processors > Global Processors > Ad Avail Blanking > Browse | avail\_blanking/avail\_blanking\_image/uri | 
| Processors > Global Processors > Ad Avail Blanking > > Credentials icon > Username | avail\_blanking/avail\_blanking\_image/username | 
| Processors > Global Processors > Blackout Image Insertion > On/Off | blackout\_slate/enabled/ | 
| Processors > Global Processors > Blackout Image Insertion > Enable Network End Blackout > Network ID | blackout\_slate/network\_id | 
| Processors > Global Processors > Blackout Image Insertion > Browse | blackout\_slate/blackout\_slate\_image/certificate\_file | 
| Processors > Global Processors > Blackout Image Insertion > Browse | blackout\_slate/blackout\_slate\_image/interface | 
| Processors > Global Processors > Blackout Image Insertion > Browse | blackout\_slate/blackout\_slate\_image/password | 
| Processors > Global Processors > Blackout Image Insertion > Browse | blackout\_slate/blackout\_slate\_image/uri | 
| Processors > Global Processors > Blackout Image Insertion > Browse | blackout\_slate/blackout\_slate\_image/username | 
| Processors > Global Processors > Blackout Image Insertion > Enable Network End Blackout > Network End Blackout Image > Browse | blackout\_slate/network\_end\_blackout\_image/certificate\_file | 
| Processors > Global Processors > Blackout Image Insertion > Enable Network End Blackout > Network End Blackout Image > Browse | blackout\_slate/network\_end\_blackout\_image/interface | 
| Processors > Global Processors > Blackout Image Insertion > Enable Network End Blackout > Network End Blackout Image > Credentials > Password | blackout\_slate/network\_end\_blackout\_image/password | 
| Processors > Global Processors > Blackout Image Insertion > Enable Network End Blackout > Network End Blackout Image > Browse | blackout\_slate/network\_end\_blackout\_image/uri | 
| Processors > Global Processors > Blackout Image Insertion > Enable Network End Blackout > Network End Blackout Image > Credentials > Username | blackout\_slate/network\_end\_blackout\_image/username | 


**Passthrough or Removal**  

| Field | XML Tag | 
| --- | --- | 
| Archive Output Group > Output > MPEG-2 TS > PID Control > SCTE-35 | output\_group/output/scte35\_passthrough | 
| Archive Output Group > Output > MPEG-2 TS > PID Control > SCTE-35 PID | output\_group/output/m2ts\_settings/scte35\_pid | 
| Apple HLS Output Group > Output > PID Control > SCTE-35 | output\_group/output/scte35\_passthrough | 
| Apple HLS Output Group > Output > PID Control > SCTE-35 PID | output\_group/output/m3u8\_settings/scte35\_pid | 
| UDP/TS Output Group > Output > SCTE-35 | output\_group/output/scte35\_passthrough | 
| UDP/TS Output Group > Output > SCTE-35 PID | output\_group/output/ts\_settings/scte35\_pid | 


**POIS conditioning**  

| Field | XML Tag | 
| --- | --- | 
| Advanced Avail Controls > Ad Avail Trigger > Acquisition Point Identifier | esam/acquisition\_point\_id/ | 
| Advanced Avail Controls > Ad Avail Trigger > Asset URI Identifier | esam/asset\_uri\_id/ | 
| Advanced Avail Controls > Ad Avail Trigger > Signal Conditioner Endpoint | esam/scc\_uri/certificate\_file | 
| Advanced Avail Controls > Ad Avail Trigger > Signal Conditioner Endpoint | esam/scc\_uri/interface | 
| Advanced Avail Controls > Ad Avail Trigger > Signal Conditioner Endpoint | esam/scc\_uri/password | 
| Advanced Avail Controls > Ad Avail Trigger > Signal Conditioner Endpoint | esam/scc\_uri/uri | 
| Advanced Avail Controls > Ad Avail Trigger > Signal Conditioner Endpoint | esam/scc\_uri/username | 
| Advanced Avail Controls > Ad Avail Trigger > Alternate Signal Conditioner Endpoint | esam/alternate\_scc\_uri/certificate\_file | 
| Advanced Avail Controls > Ad Avail Trigger > Alternate Signal Conditioner Endpoint | esam/alternate\_scc\_uri/interface | 
| Advanced Avail Controls > Ad Avail Trigger > Alternate Signal Conditioner Endpoint | esam/alternate\_scc\_uri/password | 
| Advanced Avail Controls > Ad Avail Trigger > Alternate Signal Conditioner Endpoint | esam/alternate\_scc\_uri/uri | 
| Advanced Avail Controls > Ad Avail Trigger > Alternate Signal Conditioner Endpoint | esam/alternate\_scc\_uri/username | 
| Advanced Avail Controls > Ad Avail Trigger > Manifest Conditioner Endpoint | esam/mcc\_uri/certificate\_file | 
| Advanced Avail Controls > Ad Avail Trigger > Manifest Conditioner Endpoint | esam/mcc\_uri/interface | 
| Advanced Avail Controls > Ad Avail Trigger > Manifest Conditioner Endpoint | esam/mcc\_uri/password | 
| Advanced Avail Controls > Ad Avail Trigger > Manifest Conditioner Endpoint | esam/mcc\_uri/uri | 
| Advanced Avail Controls > Ad Avail Trigger > Manifest Conditioner Endpoint | esam/mcc\_uri/username | 
| Advanced Avail Controls > Ad Avail Trigger > Alternate Manifest Conditioner Endpoint | esam/alternate\_mcc\_uri/certificate\_file | 
| Advanced Avail Controls > Ad Avail Trigger > Alternate Manifest Conditioner Endpoint | esam/alternate\_mcc\_uri/interface | 
| Advanced Avail Controls > Ad Avail Trigger > Alternate Manifest Conditioner Endpoint | esam/alternate\_mcc\_uri/password | 
| Advanced Avail Controls > Ad Avail Trigger > Alternate Manifest Conditioner Endpoint | esam/alternate\_mcc\_uri/uri | 
| Advanced Avail Controls > Ad Avail Trigger > Alternate Manifest Conditioner Endpoint | esam/alternate\_mcc\_uri/username | 
| Advanced Avail Controls > Ad Avail Trigger > Response Signal Preroll | esam/response\_signal\_preroll/ | 