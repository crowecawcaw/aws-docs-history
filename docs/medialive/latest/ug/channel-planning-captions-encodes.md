

# Identify the captions encodes
<a name="channel-planning-captions-encodes"></a>

You must decide on the number of captions encodes. Follow this procedure for each output group. 

1. Determine the maximum number of captions encodes that are allowed in the output group. The following rules apply for each type of output group.



<table>
<thead>
  <tr><th>Type of output group</th><th>Rule for captions encodes</th></tr>
</thead>
<tbody>
  <tr><td>Archive</td><td>Zero or more captions encodes. The captions are either embedded or object-style captions.</td></tr>
  <tr><td>CMAF Ingest</td><td>Zero or more captions encodes. Typically, there are caption languages to match the audio languages. The captions are embedded or sidecar captions.</td></tr>
  <tr><td>Frame Capture</td><td>Zero captions encodes.</td></tr>
  <tr><td>HLS or MediaPackage</td><td>Zero or more captions encodes. Typically, there are caption languages to match the audio languages. The captions are either embedded or sidecar captions.</td></tr>
  <tr><td>Microsoft Smooth</td><td>Zero or more captions encodes. Typically, there are caption languages to match the audio languages. The captions are always sidecar captions.</td></tr>
  <tr><td>RTMP</td><td>Zero or one caption encodes. The captions are either embedded or object-style captions.</td></tr>
  <tr><td>SRT</td><td>Zero or more captions encodes. The captions are either embedded or object-style captions.</td></tr>
  <tr><td>UDP</td><td>One or more captions encodes. The captions are either embedded or object-style captions.</td></tr>
</tbody>
</table>


1. Identify the category that each caption format belongs to. See the list in [Captions categories](categories-captions.md). For example, WebVTT captions are sidecar captions.

1. Use this category to identify the number of captions encodes you need in the output group.
   + For embedded captions, you always create one captions encode.
   + For object-style captions and sidecar captions, you create one captions encode for each format and language that you want to include.