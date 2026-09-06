

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# Setting Up HDR Jobs Using the REST API
<a name="setting-up-hdr-jobs-using-the-rest-api"></a>

This section provides information for setting up your AWS Elemental Server job and profile XML for HDR. 

To use the information in this section, you should understand: 
+  The conceptual information provided in the main body of this document. 
+  How to create and modify jobs using XML.

## XML Reference Tables for HDR
<a name="xml-reference-tables-for-hdr"></a>




**Managing Overwrite of Source Metadata**  

<table>
<thead>
  <tr><th colspan="4">Element</th><th>Notes</th></tr>
</thead>
<tbody>
  <tr><td colspan="4">job</td><td>Top-level element</td></tr>
  <tr><td></td><td colspan="3">input</td><td></td></tr>
  <tr><td></td><td></td><td colspan="2">video_selector</td><td>Corresponds to the Video Selector section of the UI, under Input &gt; Advanced. One &lt;video_selector&gt; element exists per job, which applies to all outputs.</td></tr>
  <tr><td></td><td></td><td></td><td>force_color</td><td>Corresponds to the Force Color checkbox in the UI. Set to <code>true</code> to overwrite the source metadata with the values in &lt;color_space&gt; and, for HDR10, the children of &lt;hdr10_metadata&gt;. Set to <code>false</code> to retain metadata from the source.</td></tr>
  <tr><td></td><td></td><td></td><td>color_space</td><td>Corresponds to the Color Space dropdown in the Video Selector section of the UI.<br />Valid values are: follow, rec_601, rec_709, hdr10, hlg_2020</td></tr>
  <tr><td></td><td></td><td></td><td>hdr10_metadata</td><td>Contains children for specifying master display information for HDR10. See the table below.</td></tr>
</tbody>
</table>





**Metadata Specific to HDR10**  

| **Child of <hdr10\_metadata>** | **Valid Range** | 
| --- | --- | 
| red\_primary\_x | 0-50000 | 
| red\_primary\_y | 0-50000 | 
| green\_primary\_x | 0-50000 | 
| green\_primary\_y | 0-50000 | 
| blue\_primary\_x | 0-50000 | 
| blue\_primary\_y | 0-50000 | 
| white\_point\_x | 0-50000 | 
| white\_point\_y | 0-50000 | 
| min\_lumninance | 0-2147483647 | 
| max\_luminance | 0-2147483647 | 
| maxcll | 0- 65535  | 
| maxfall | 0- 65535 | 

For the following table, different outputs can have different values for `<insert_color_metadata>` because this setting is contained in the stream assembly.


**Including or Excluding Metadata from Outputs**  

<table>
<thead>
  <tr><th colspan="4">Element</th><th>Notes</th></tr>
</thead>
<tbody>
  <tr><td colspan="4">job</td><td>Top-level element</td></tr>
  <tr><td></td><td colspan="3">stream_assembly</td><td>Use one &lt;stream_assembly&gt; element for each set of encoding instructions you need.</td></tr>
  <tr><td></td><td></td><td colspan="2">name</td><td>Use the value of this element to map a stream assembly to an output.</td></tr>
  <tr><td></td><td></td><td colspan="2">video_description</td><td>Contains settings for how the video is encoded.</td></tr>
  <tr><td></td><td></td><td></td><td>insert_color_metadata</td><td>Set to <code>true</code> to include color metadata in the output; set to <code>false</code> to exclude it.</td></tr>
  <tr><td></td><td colspan="3">output group</td><td>Use one output group element for each video package type produced.<br />Different outputs within the group can have different sets of encoding instructions (different stream assemblies) applied to them.</td></tr>
  <tr><td></td><td></td><td colspan="2">output</td><td>Represents the actual set of elementary streams delivered to a single destination address.</td></tr>
  <tr><td></td><td></td><td></td><td>stream_assembly_name</td><td>Set the value of this element to match that of a &lt;stream_assembly&gt;/&lt;name&gt; element, which associates this output with the stream assembly.</td></tr>
</tbody>
</table>


For the following table, different outputs can have different settings for color correction because this setting is contained in the stream assembly.


**Color Correction**  

<table>
<thead>
  <tr><th colspan="6">Element</th><th>Notes</th></tr>
</thead>
<tbody>
  <tr><td colspan="6">job</td><td>Top-level element</td></tr>
  <tr><td></td><td colspan="5">stream_assembly</td><td>Use one &lt;stream_assembly&gt; element for each set of encoding instructions you need.</td></tr>
  <tr><td></td><td></td><td colspan="4">name</td><td>Use the value of this element to map a stream assembly to an output.</td></tr>
  <tr><td></td><td></td><td></td><td colspan="3">video_preprocessors</td><td></td></tr>
  <tr><td></td><td></td><td></td><td></td><td colspan="2">color_corrector</td><td>Include this element if you want color correction on your output.</td></tr>
  <tr><td></td><td></td><td></td><td></td><td></td><td>color_space_conversion</td><td>Use this element to specify the color space or format you want your video stream converted to. <br />Supported conversions are between HDR10 and HLG, from either rec. 601 or rec. 709 to either HDR10 or HLG, and between rec. 601 and rec. 709.<br />Valid values are: none, force_601, force_709, force_hdr10, force_hlg_2020</td></tr>
  <tr><td></td><td></td><td></td><td></td><td></td><td>brightness</td><td>Provide brightness correction value here.<br />Valid range is: 1 through 100</td></tr>
  <tr><td></td><td></td><td></td><td></td><td></td><td>contrast</td><td>Provide contrast correction value here.<br />Valid range is: 1 through 100</td></tr>
  <tr><td></td><td></td><td></td><td></td><td></td><td>hue</td><td>Provide hue correction value here.<br />Valid range is: -180 through 180</td></tr>
  <tr><td></td><td></td><td></td><td></td><td></td><td>saturation</td><td>Provide saturation correction value here.<br />Valid range is: 1 through 100</td></tr>
  <tr><td></td><td></td><td></td><td></td><td></td><td>hdr10_metadata</td><td>Contains children for specifying master display information for HDR10. See the table below.</td></tr>
  <tr><td></td><td colspan="5">output group</td><td>Use one output group element for each video package type produced.<br />Different outputs within the group can have different sets of encoding instructions (different stream assemblies) applied to them.</td></tr>
  <tr><td></td><td></td><td colspan="4">output</td><td>Represents the actual set of elementary streams delivered to a single destination address.</td></tr>
  <tr><td></td><td></td><td></td><td colspan="3">stream_assembly_name</td><td>Set the value of this element to match that of a &lt;stream_assembly&gt;/&lt;name&gt; element, which associates this output with the stream assembly.</td></tr>
</tbody>
</table>


The following table shows HDR10-specific metadata structures and ranges for which values for the elements must be supplied by your color grader or another upstream source along with information about your specific video asset.


**Metadata Specific to HDR10**  

| Child of <hdr10\_metadata> | Valid Range | 
| --- | --- | 
| red\_primary\_x | 0-50000 | 
| red\_primary\_y | 0-50000 | 
| green\_primary\_x | 0-50000 | 
| green\_primary\_y | 0-50000 | 
| blue\_primary\_x | 0-50000 | 
| blue\_primary\_y | 0-50000 | 
| white\_point\_x | 0-50000 | 
| white\_point\_y | 0-50000 | 
| min\_lumninance | 0-2147483647 | 
| max\_luminance | 0-2147483647 | 
| maxcll | 0- 65535  | 
| maxfall | 0- 65535 | 