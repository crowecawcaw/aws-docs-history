# Configuring Nielsen non-linear watermarking

To use this feature, you must first establish a relationship with Nielsen and set up a
Nielsen SID/TIC server in the AWS Cloud. Contact Nielsen to download their SID/TIC
server software, generate a WRR license file, and receive installation and setup
instructions. For an overview of how the infrastructure works, see [Nielsen SID/TIC server requirements in the AWS
Cloud](how-mediaconvert-interacts-with-your-nielsen-sid-tic-server-in-the-aws-cloud.md "how-mediaconvert-interacts-with-your-nielsen-sid-tic-server-in-the-aws-cloud.md").

###### To set up Nielsen non-linear watermarking (console)

1. Set up a Nielsen SID/TIC server system in the AWS Cloud. For more
   information, contact Nielsen.
2. Set up an Amazon S3 bucket to hold your Nielsen metadata .zip file. MediaConvert
   writes the metadata to this bucket.
3. Set up your job inputs and outputs as described in [Tutorial: Configuring job settings](setting-up-a-job.md "setting-up-a-job.md").
4. On the **Create job** page, in the **Job** pane on the left, under **Job settings** choose
   **Settings**.
5. In the **Partner integrations** section on the right, choose
   **Nielsen non-linear watermarking**.
6. Provide values for the settings that become visible when you enable
   **Nielsen non-linear watermarking**. For instructions and
   guidance about each of these settings, choose the **Info** link
   next to the setting label.
7. Choose **Create**, at the bottom of the page, to run your
   job.
8. Transfer the data in your metadata Amazon S3 bucket to Nielsen, according to their
   instructions.

###### To set up Nielsen non-linear watermarking (API, CLI, and SDK)

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

- **Nielsen non-linear watermarking** (`nielsenNonLinearWatermark`)
- **Source watermark status** (`sourceWatermarkStatus`)
- **Watermark types** (`activeWatermarkProcess`)
- **SID** (`sourceId`)
- **CSID** (`cbetSourceId`)
- **Asset ID** (`assetId`)
- **Asset name** (`assetName`)
- **Episode ID** (`episodeId`)
- **TIC server REST endpoint** (`ticServerUrl`)
- **ADI file** (`adiFilename`)
- **Metadata destination** (`metadataDestination`)
- **Share TICs across tracks** (`uniqueTicPerAudioTrack`)
