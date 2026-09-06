

# Audio: Transcode support and passthrough support for Dolby audio codecs
<a name="codecs-containers-transcode-support"></a>

Three Dolby codecs are supported and can be transcoded or passed through as follows:
+ Dolby Digital (AC-3): Can be re-encoded as Dolby Digital or the original Dolby Digital can be passed through.
+ Dolby Digital Plus (E-AC-3): Can be re-encoded as Dolby Digital Plus or the original Dolby Digital Plus can be passed through.
+ Dolby E: Can be passed through as Dolby E. Cannot be re-encoded as Dolby E.

The following table specifies the fields on the input side and on the output side that control passthrough versus transcoding. 

<a name="codecs-containers-file-inputs-table"></a>
<table>
<thead>
  <tr><th colspan="2">Input</th><th colspan="2">Output &gt; Stream </th><th> Result</th></tr>
</thead>
<tbody>
  <tr><td>Codec Detected in Input</td><td>Value in Unwrap SMPTE 337 Field</td><td>Value in Output Codec Field</td><td>Value in Automatic Passthrough Field</td><td></td></tr>
  <tr><td>Dolby Digital</td><td>n/a</td><td>Dolby Digital</td><td>n/a</td><td>Re-encoded to Dolby Digital </td></tr>
  <tr><td>Dolby Digital</td><td>n/a</td><td>Dolby Digital Passthrough</td><td>n/a</td><td> Passthrough of Dolby Digital</td></tr>
  <tr><td>Dolby Digital Plus</td><td>n/a</td><td>Dolby Digital Plus</td><td>Checked</td><td> Passthrough of Dolby Digital Plus</td></tr>
  <tr><td>Dolby Digital Plus</td><td>n/a</td><td>Dolby Digital Plus</td><td>Unchecked</td><td>Re-encoded to Dolby Digital Plus</td></tr>
  <tr><td>Dolby Digital Plus</td><td>n/a</td><td>Dolby Digital Passthrough</td><td>n/a</td><td> Passthrough of Dolby Digital Plus</td></tr>
  <tr><td>Dolby Digital Plus and a non-Dolby Digital Plus codec</td><td>n/a</td><td>Dolby Digital Plus</td><td>Checked</td><td>The non-Dolby Digital Plus audio is transcoded to Dolby Digital Plus. The Dolby Digital Plus audio is passed through (it will not be re-encoded as Dolby Digital Plus).</td></tr>
  <tr><td>Dolby Digital Plus and a non-Dolby Digital Plus codec</td><td>n/a</td><td>Dolby Digital Plus</td><td>Unchecked</td><td>The non-Dolby Digital Plus audio is transcoded to Dolby Digital Plus. The Dolby Digital Plus audio is re-encoded to Dolby Digital Plus.</td></tr>
  <tr><td>Dolby Digital Plus and a non-Dolby Digital Plus codec</td><td>n/a</td><td>Dolby Digital Passthrough</td><td>n/a</td><td>Not valid: setting up like this causes a validation error.</td></tr>
  <tr><td>Dolby E in a PCM stream tagged with SMPTE 337</td><td>Unchecked</td><td>Uncompressed WAV</td><td>n/a</td><td>Passthrough of Dolby E. </td></tr>
  <tr><td>Dolby E in a PCM stream tagged with SMPTE 337</td><td>Unchecked</td><td>Uncompressed AIFF</td><td>n/a</td><td>Passthrough of Dolby E. </td></tr>
</tbody>
</table>
