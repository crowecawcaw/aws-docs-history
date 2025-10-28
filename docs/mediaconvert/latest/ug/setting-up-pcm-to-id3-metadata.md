# Configuring

PCM to ID3 metadata

To use this feature, your input must have PCM audio that contains Nielsen watermarks.
You provide your Nielsen distributor ID to MediaConvert and then, during the transcode,
MediaConvert inserts the watermark information into the ID3 metadata of your
output.

You can put Nielsen watermarking information into the ID3 metadata of outputs in
the following output groups only:

- Apple HLS
- File group, when your output container is MPEG-2 Transport Stream

###### To enable PCM to ID3 metadata (console)

1. Set up your job inputs and outputs as described in [Tutorial: Configuring job settings](setting-up-a-job.md "setting-up-a-job.md").
2. Enable PCM to ID3 metadata in the job-wide settings.
   1. On the **Create job** page, in the **Job** pane on the left, under **Job settings** choose
      **Settings**.
   2. In the **Partner integrations** section on the right,
      choose **Nielsen PCM to ID3 metadata**.
   3. For **Distributor ID**, provide the ID that Nielsen
      assigned to your organization.

3. Enable PCM to ID3 metadata in the outputs where you want it. Do these steps
   for each **Apple HLS** output that you want to have ID3
   metadata.
   1. In the **Job** pane on the left, choose the
      output.
   2. In the **Output settings** section on the right,
      expand the section **Transport stream
      settings**.
   3. For **Nielsen ID3**, choose
      **Insert**.

4. Do these steps for each **File group** output that you want
   to have ID3 metadata.
   1. In the **Job** pane on the left, choose the
      output.
   2. In the **Output settings** section on the right,
      expand the section **Container settings**.
   3. Scroll to the section **PID controls**.
   4. For **Nielsen ID3**, choose
      **Insert**.

###### To enable PCM to ID3 metadata (API, CLI, and SDK)

If you use the API, CLI, or an SDK, specify the relevant settings in your JSON
job specification and then submit it programmatically with your job. For more
information about submitting your job programmatically, see one of the
introductory topics of the _AWS Elemental MediaConvert API
Reference_:

- [Getting started with AWS Elemental MediaConvert using the AWS SDKs or the AWS
  CLI](../apireference/custom-endpoints.md "../apireference/custom-endpoints.md")
- [Getting started with AWS Elemental MediaConvert
  using the API](../apireference/getting-started.md "../apireference/getting-started.md")
- Use the MediaConvert console to generate your JSON job specification.
  We recommend this approach, because the console functions as an
  interactive validator against the MediaConvert job schema. Follow these
  steps to generate your JSON job specification using the console:

      1. Follow the previous procedure for the console.
      2. In the **Job** pane on the left, under **Job
       settings**, choose **Show job
       JSON**.

  Find additional information, including where each setting belongs in the job
  settings structure, in the _AWS Elemental MediaConvert API
  Reference_. Links in this list go to information about the setting
  in that document:

- **Nielsen PCM to ID3 metadata** (`nielsenConfiguration`)
- **Distributor ID** (`distributorId`)
- **Nielsen ID3**, for outputs in an **Apple
  HLS** output group (`nielsenId3`, child of `m3u8Settings`)
- **Nielsen ID3**, for outputs in a **File
  group** output group (`nielsenId3`, child of `m2tsSettings`)
