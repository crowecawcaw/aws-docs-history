

# Including accessibility data in captions in MediaLive
<a name="captions-accessibility"></a>

In the captions in CMAF Ingest, HLS, MediaPackage, or Microsoft Smooth output groups, you can include accessibility data. This data describes the type of accessibility that the encode represents. For example, a captions track might provide a written translation (into another language) of the speech in the content. Accessibility data is also known as accessibility signaling.

**Topics**
+ [Supported accessibility data standards](#captions-accessibility-standards)
+ [Specifying data in a CMAF Ingest or Microsoft Smooth output](#captions-accessibility-cmaf-mss)
+ [Specifying data in an HLS or MediaPackage output](#captions-accessibility-hls-emp)

## Supported accessibility data standards
<a name="captions-accessibility-standards"></a>

MediaLive supports the following styles of accessibility data. 


| Accessibility data style | Specification | CMAF Ingest | HLS or MediaPackage | Microsoft Smooth | 
| --- | --- | --- | --- | --- | 
| DASH role captions | DASH role scheme (ISO/IEC 23009-1:2022(E)) | Yes |  | Yes | 
| DVB DASH accessibility | * ETSI TS 103 285 Technical Specification, V1.3.1 (2020-02)* | Yes |  | Yes | 
| Accessibility | Signaled in tags that are inserted in the HLS manifest. |  | Yes |  | 

## Specifying data in a CMAF Ingest or Microsoft Smooth output
<a name="captions-accessibility-cmaf-mss"></a>

You can set up the captions encode to include accessibility data when you create the encode, as described in [Create embedded or object captions encodes](output-embedded-and-more.md) and [Create sidecar or SMPTE-TT captions encodes](output-sidecar-and-smptett-mss.md).

In the output that has the captions encode that you want to set up, follow these steps:
+ To include DASH Roles, choose **Add dash role**s as many times as you want. Choose the style in each role.
+ To include DVB DASH accessibility style, in **DVB DASH accessibility**, choose the applicable description. You can add only one instance of this accessibility style.

You can add more than one style of accessibility data to each encode. For example, you can add Dash Roles and DVB DASH accessibility style. You might want to do this because different downstream systems for these outputs implement different styles.

### Handling of accessibility data in CMAF Ingest or Microsoft Smooth
<a name="captions-accessibility-cmaf-mss-result"></a>

The fields for accessibility data appear for all output group types, including types that don't support this data. 

**Note**  
When you set up audio encodes and you plan to include accessibility data, proceed as follows. First create the audio encodes in the CMAF Ingest and/or Microsoft Smooth output groups, and set up the accessibility data. Then create the audio encodes in the other output groups.

**Handling in supported output groups**

If you aren't implementing shared captions encodes, MediaLive includes the data only in the captions outputs of the CMAF Ingest and Microsoft Smooth output groups that you set up for captions accessibility data. 

**Handling in shared encodes**

You might plan to share captions encodes among several output groups. For example, you might share a captions encode among one CMAF Ingest output group and other output groups. 

If you set up accessibility data in a shared audio encode, MediaLive will handle the data as follows:
+ It will include the data in the CMAF Ingest and Microsoft Smooth output groups that share the encode.
+ It won't include the data in other output groups, because those output groups don't support this data. Even though the output group is sharing the encode, MediaLive won't include the data. 

**Handling in other output groups**

You might try to set up accessibility fields in an output that doesn't support accessibility data. If you're not implementing encode sharing with a CMAF Ingest or Microsoft Smooth output group, you will get an error message when you save the channel. 

## Specifying data in an HLS or MediaPackage output
<a name="captions-accessibility-hls-emp"></a>

You can set up the captions encode to include accessibility data when you create the encode, as described in [Create embedded or object captions encodes](output-embedded-and-more.md).

In the output that has the captions encode that you want to set up, in **Accessibility**, choose **IMPLEMENTS\_ACCESSIBILITY\_FEATURES**.

MediaLive assigns accessibility captions a unique attribute in the EXT-X-MEDIA tag of the HLS manifest:

`CHARACTERISTICS="public.accessibility.describes-spoken-dialog,public.accessibility.describes-music-and-sound"`

Here is an example of the EXT-X-MEDIA tag with the accessibility caption attribute:

`#EXT-X-MEDIA:TYPE=SUBTITLES,GROUP-ID="captions-group",NAME="accessibility-captions1",LANGUAGE="eng", CHARACTERISTICS="public.accessibility.describes-spoken-dialog,public.accessibility.describes-music-and-sound",AUTOSELECT=YES,DEFAULT=YES,URI="caption-accessibility-eng.m3u8"`

### Handling of accessibility data in HLS or MediaPackage output groups
<a name="captions-accessibility-hls-emp-results"></a>

The **Accessibility** field appears for all output group types, including types that don't support this data. 

**Note**  
When you set up audio encodes and you plan to include accessibility data, proceed as follows. First create the audio encodes in the HLS and/or MediaPackage output groups, and set up the accessibility data. Then create the audio encodes in the other output groups.

**Handling in supported output groups**

If you aren't implementing shared audio encodes, MediaLive includes the data only in the audio outputs of the HLS and MediaPackage output groups that you set up for audio accessibility data. 

**Handling in shared encodes**

You might plan to share captions encodes among several output groups. For example, you might share a captions codec among one HLS output group and other output groups. 

If you set up accessibility data in a shared captions encode, MediaLive will handle the data as follows:
+ It will include the data in the HLS and MediaPackage output groups that share the encode.
+ It won't include the data in other output groups, because those output groups don't support this data. Even though the output group is sharing the encode, MediaLive won't include the data. 

**Handling in other output groups**

You might try to set up **Accessibility** in an output that doesn't support accessibility data. If you're not implementing encode sharing with an HLS or MediaPackage output group, you will get an error message when you save the channel. 