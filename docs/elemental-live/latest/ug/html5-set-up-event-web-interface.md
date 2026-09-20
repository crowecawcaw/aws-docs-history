

# Using the web interface
<a name="html5-set-up-event-web-interface"></a>

**To configure the event using the web interface**

1. Obtain the asset URL and user credentials (if required) from the administrator of the authoring system that is publishing the HTML5 asset.

1. In the **Global Processors** section, go to the **Image Inserter** field and choose **On**. More fields appear.

1. Complete these fields:
   + **Insertion Mode**: Choose **HTML**.
   + **Input**: Enter the location of the HTML5 asset.

     If access to your local or mounted directory requires authentication, enter the user name and password.

1. Set the following fields to match the control that you're using.


<table>
<thead>
  <tr><th>Option for control</th><th>Value for Active</th><th>Value for &lt;enable_rest&gt;</th><th>Value for &lt;enable_scte35&gt;</th></tr>
</thead>
<tbody>
  <tr><td>Authoring system control</td><td>Unchecked</td><td>Unchecked</td><td>Unchecked</td></tr>
  <tr><td>REST API control</td><td>Checked or unchecked, depending on whether you want the motion overlay to show when the event starts</td><td>Checked</td><td>Unchecked</td></tr>
  <tr><td>SCTE 35 control</td><td>Unchecked</td><td>Unchecked</td><td>Checked</td></tr>
</tbody>
</table>


For detailed information about the fields, see [Fields for an HTML5 asset](html5-set-up-event-fields.md).