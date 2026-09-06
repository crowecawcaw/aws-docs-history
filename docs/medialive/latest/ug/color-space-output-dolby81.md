

# Result when converting color space to Dolby Vision 8.1
<a name="color-space-output-dolby81"></a>

Read this section if you set up one or more MediaLive outputs to [convert the color space](colorspace-output-setup.md#colorspace-output-setup-convert) to Dolby Vision 8.1. The following table shows how MediaLive handles each type of color space that it encounters in the source.


<table>
<thead>
  <tr><th>Color space that MediaLive encounters</th><th>How MediaLive handles the color space</th></tr>
</thead>
<tbody>
  <tr><td>Content in HDR10</td><td>When you convert suitable content to Dolby Vision 8.1, MediaLive makes the following changes:<ul><li> It doesn't change the pixel values, because HDR10 and Dolby Vision 8.1 both use the same color space. </li><li> It changes the color space metadata to identify the new color space.  </li><li> It applies the new brightness function to the content. </li><li> It calculates the Dolby Vision 8.1 display metadata for the content.  </li></ul>After the conversion, the color space hasn't changed. However, the bright parts of the content are brighter, and the dark parts are darker.</td></tr>
  <tr><td>Content in any other supported color space</td><td>MediaLive passes through the color space and color space metadata for that portion,</td></tr>
  <tr><td>Content marked with an unknown or unsupported color space</td><td rowspan="2">Converting non-HDR10 content to Dolby Vision 8.1 doesn't comply with the usage intended by Dolby Vision 8.1. After conversion of the color space, the color map of the content will be completely wrong.</td></tr>
  <tr><td>Content with no color space metadata</td></tr>
</tbody>
</table>
