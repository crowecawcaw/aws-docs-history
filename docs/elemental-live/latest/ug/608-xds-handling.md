# Setting up for 608 XDS data

If your source content includes 608 XDS data, you can set up the event to include it
or strip it from the output.

The Extended Data Services (XDS or EDS) standard is part of EIA-608 and allows for the
delivery of ancillary data.

###### Note

You set up handling of this source data for the entire event, so you set up to
either include it in every output and stream, or you set up to exclude it from every
output and stream.

###### To configure handling of this data

1. In the Input section of the event, click **Advanced**.
2. Click the **Add Caption Selector** button.
3. Set the source to **Null**.

You only need to create one Caption Selector for 608 XDS data, regardless of the
number of outputs you are creating. 4. If you also want to extract regular captions, create more Caption Selectors
according to the regular procedure. 5. In the **Global Processors** section, turn on **608
Extended Data Services** and complete the fields as desired.

###### Note

No setup is required in the captions section of the output or the streams.
