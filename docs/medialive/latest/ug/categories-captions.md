

# Captions categories
<a name="categories-captions"></a>

Captions are grouped into five categories, based on how the captions are included in the output. 


|  Captions format  |  Category of this format  | 
| --- | --- | 
| ARIB  | Object-style | 
| Burn-in | Burn-in | 
| DVB-Sub | Object-style | 
| EBU-TT-D | Sidecar | 
| Embedded | Embedded | 
| Embedded\+SCTE-20 | Embedded  | 
| RTMP CaptionInfo | Object-style | 
| SCTE-20\+Embedded | Embedded | 
| SCTE-27 | Object-style | 
| Smart Subtitles | Sidecar | 
| SMPTE-TT | Stream | 
| Teletext  | Object-style | 
| TTML | Sidecar | 
| WebVTT | Sidecar | 

## Embedded captions
<a name="embedded-in-video"></a>

The captions are carried inside the video encode, which is itself in an output in the output group. There is only ever one captions entity within that video encode, although that entity might contain captions for up to four languages. 

![Output container showing Video encode with Captions nested inside, and Audio encode below.](http://docs.aws.amazon.com/medialive/latest/ug/images/caption_categories_embedded.png)


## Object-style captions
<a name="captions-object"></a>

All the captions encodes for a specific output group are in the same output as the corresponding video and audio. 

![Output container showing video encode, audio encode, and two captions encode items.](http://docs.aws.amazon.com/medialive/latest/ug/images/caption_categories_object.png)


## Sidecar captions
<a name="captions-sidecar"></a>

Each captions encode for a specific output group is in its own "captions-only" output. The output group can contain more than one captions output, for example, one for each language. 

![Three output groups: one with video and audio encode, two with captions encode only.](http://docs.aws.amazon.com/medialive/latest/ug/images/caption_categories_sidecar.png)


Each captions-only output becomes a separate file in the packaged output.

## Stream
<a name="captions-stream"></a>

Each captions encode for a specific output group is in its own "captions-only" output. The output group can contain more than one captions output, for example, one for each language.

![Three output groups: one with video and audio encode, two with captions encode only.](http://docs.aws.amazon.com/medialive/latest/ug/images/caption_categories_stream.png)


Each captions-only output becomes a separate stream in the packaged output.

## Burn-in captions
<a name="burnin"></a>

The captions are converted into text and then overlaid on the picture directly in the video encode. Strictly speaking, once the overlay occurs, these are not really captions because they are indistinguishable from the video. 