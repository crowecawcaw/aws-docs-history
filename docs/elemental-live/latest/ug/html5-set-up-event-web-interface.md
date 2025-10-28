# Using the web interface

###### To configure the event using the web interface

1. Obtain the asset URL and user credentials (if required)
   from the administrator of the authoring system that is
   publishing the HTML5 asset.
2. In the **Global Processors** section,
   go to the **Image Inserter** field and
   choose **On**. More fields appear.
3. Complete these fields:
   - **Insertion Mode**: Choose
     **HTML**.
   - **Input**: Enter the location of
     the HTML5 asset.

   If access to your local or mounted directory
   requires authentication, enter the user name and
   password.

4. Set the following fields to match the control that
   you're using.

| Option for control       | Value for Active                                                                                     | Value for <enable_rest> | Value for <enable_scte35> |
| ------------------------ | ---------------------------------------------------------------------------------------------------- | ----------------------- | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Authoring system control | Unchecked                                                                                            | Unchecked               | Unchecked                 |
| REST API control         | Checked or unchecked, depending on whether you want the motion overlay to show when the event starts | Checked                 | Unchecked                 |
| SCTE 35 control          | Unchecked                                                                                            | Unchecked               | Checked                   | For detailed information about the fields, see [Fields for an HTML5 asset](html5-set-up-event-fields.md "html5-set-up-event-fields.md"). |
