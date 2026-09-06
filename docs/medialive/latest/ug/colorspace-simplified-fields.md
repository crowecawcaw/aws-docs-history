

# Reference: Location of fields
<a name="colorspace-simplified-fields"></a>

Read this section if you know how to handle color space in MediaLive, and you only need a reminder of where the fields are located in the MediaLive Console. The information is sorted by the location of the fields on the **Channel** page, from top to bottom. 


<table>
<thead>
  <tr><th>Topic</th><th colspan="2">Location on the Channel page</th><th>Field</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">Input handling</td><td rowspan="2"><b>Input attachments</b></td><td rowspan="2"><b>Video Selector</b></td><td><b>Color space</b></td></tr>
  <tr><td><b>Color space usage</b></td></tr>
  <tr><td rowspan="2">Enter the display metadata for an input from a AWS Elemental Link device</td><td rowspan="2"><b>Input attachments</b></td><td rowspan="2"><b>Video Selector</b>, then <b>Color space settings</b></td><td><b>Max CLL</b></td></tr>
  <tr><td><b>Max Fall</b></td></tr>
  <tr><td>Configure the channel to use 3D LUTs files</td><td><b>General settings</b></td><td><b>Color correction settings</b></td><td><b>Url</b><b>Input color space</b><br /><b>Output color space</b></td></tr>
  <tr><td rowspan="4">Output, configure the video codec</td><td rowspan="4"><b>Output groups</b>, then <b>Outputs</b></td><td><b>Stream settings</b>, then <b>Video</b> </td><td><b>Codec settings</b></td></tr>
  <tr><td rowspan="3"><b>Stream settings</b>, then <b>Video</b>, then <b>Codec settings</b>, then <b>Codec details</b></td><td><b>Profile</b></td></tr>
  <tr><td><b>Tier</b></td></tr>
  <tr><td><b>Level</b></td></tr>
  <tr><td>Output, convert the color space</td><td><b>Output groups</b>, then <b>Outputs</b></td><td><b>Stream settings</b>, then <b>Video</b>, then <b>Color space</b></td><td> <b>Color space settings</b></td></tr>
  <tr><td>Output, include or omit color space metadata</td><td><b>Output groups</b>, then <b>Outputs</b></td><td><b>Stream settings</b>, then <b>Video</b>, then <b>Codec settings</b>, then <b>Codec details</b>, then <b>Additional settings</b></td><td><b>Color metadata</b></td></tr>
  <tr><td rowspan="2">Output, specify display metadata to include, only if you are converting to HDR10</td><td rowspan="2"><b>Output groups</b>, then <b>Outputs</b></td><td rowspan="2"><b>Stream settings</b>, then <b>Video</b>, then <b>Color space</b>, then <b>Color space settings</b></td><td><b>Max CLL</b></td></tr>
  <tr><td><b>Max Fall</b></td></tr>
  <tr><td rowspan="2">Output, set up enhanced VQ, only if the output codec is H.264</td><td rowspan="2"><b>Output groups</b>, then <b>Outputs</b></td><td rowspan="2"><b>Stream settings</b>, then <b>Video</b>, then <b>Codec settings</b>, then <b>Additional encoding settings</b></td><td><b>Quality level</b></td></tr>
  <tr><td><b>Filter settings</b></td></tr>
</tbody>
</table>
