

# AWS Elemental MediaPackage manifest filtering error conditions
<a name="error-conditions-and-handling"></a>

Common error conditions for manifest filtering with MediaPackage are listed in the following table. 



| Error condition | Example | HTTP status code | 
| --- | --- | --- | 
| A list parameter is not found and is not part of a constrained list | ?aws.manifestfilter=audio\_language:dahlia | 200 | 
| Only subtitle streams are present in the stream | ?aws.manifestfilter=audio\_sample\_rate:0-1;video\_bitrate=0-1 | 200 | 
| Duplicate filter parameter | ?aws.manifestfilter=audio\_sample\_rate:0-48000;aws.manifestfilter=audio\_sample\_rate:0-48000 | 400 | 
| Invalid parameter | ?aws.manifestfilter=donut\_type:rhododendron | 400 | 
| Invalid range parameter | ?aws.manifestfilter=audio\_sample\_rate:300-0 | 400 | 
| Invalid range value (more than INT\_MAX) | ?aws.manifestfilter=audio\_sample\_rate:0-2147483648 | 400 | 
| Malformed query string | ?aws.manifestfilter=audio\_sample\_rate:is:0-44100 | 400 | 
| Parameter string is greater than 1024 characters | ?aws.manifestfilter=audio\_language:abcdef.... | 400 | 
| Query parameters on an TS or CMAF bitrate manifest | index\_1.m3u8?aws.manifestfilter=video\_codec:h264 | 400 | 
| Query parameters on a segment request | ...\_1.[ts\|mp4\|vtt..]?aws.manifestfilter=video\_codec:h264 | 400 | 
| Repeated query parameter | ?aws.manifestfilter=audio\_sample\_rate:0-48000;aws.manifestfilter=video\_bitrate:0-1 | 400 | 
| Application of the filter results in an empty manifest (content has no streams that meet the conditions defined in the query string) | ?aws.manifestfilter=audio\_sample\_rate:0-1;video\_bitrate=0-1 | 400 | 