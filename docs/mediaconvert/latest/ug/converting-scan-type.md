# Converting the scan type of your

video

After you know how you want to specify the relevant settings, use one of the following procedures to set up your job. For conceptual information and guidance about choosing the right values for these settings, see

[Settings for scan
type conversion](working-with-scan-type.md#settings-for-scan-type-conversion "working-with-scan-type.md#settings-for-scan-type-conversion").

###### To set up your transcoding job to convert scan type and telecine

(console)

1. Consult the topic [Settings for scan
   type conversion](working-with-scan-type.md#settings-for-scan-type-conversion "working-with-scan-type.md#settings-for-scan-type-conversion") to determine
   the values that you want to set for interlacing or deinterlacing.
2. Set up your job inputs and outputs as described in [Tutorial: Configuring job settings](setting-up-a-job.md "setting-up-a-job.md").
3. On the **Create job** page, in the **Job** pane on the left, choose the output that you want to work with.
4. Find the settings you need in the **Encoding settings**
   section as follows:
   - **Deinterlacer** preprocessor: Choose
     **Deinterlacer** from the list of preprocessors
     at the bottom of the **Encoding settings**
     section.
   - **Deinterlace Control**: Find this setting in the
     **Deinterlacer** section after you enable the
     deinterlacer.
   - **Deinterlace algorithm**: Find this setting in
     the **Deinterlacer** section after you enable the
     deinterlacer.
   - **Deinterlace mode**: Find this setting in the
     **Deinterlacer** section after you enable the
     deinterlacer.
   - **Interlace mode**: Find this setting directly
     under **Encoding settings**. You might want to use
     your web browser's search function to find this setting.
   - **Telecine**: This setting is only visible in the
     MediaConvert console when you set **Frame rate** to
     **29.970**. Find **Frame
     rate** directly under **Encoding
     settings**. You might want to use your web browser's
     search function to find this setting.

   The default value for **Telecine** is **None**.
   Therefore, you only need to make this setting visible in the MediaConvert console
   when you are creating a telecine output.

###### To set up your transcoding job to convert scan type and telecine (API, CLI,

or SDK)

If you use the API, CLI, or an SDK, specify the relevant settings in your JSON
job specification and then submit it programmatically with your job. For more
information about submitting your job programmatically, see one of the
introductory topics of the _AWS Elemental MediaConvert API
Reference_:

- [Getting started with AWS Elemental MediaConvert using the AWS SDKs or the AWS
  CLI](../apireference/custom-endpoints.md "../apireference/custom-endpoints.md")
- [Getting started with AWS Elemental MediaConvert
  using the API](../apireference/getting-started.md "../apireference/getting-started.md")

1. Consult the topic [Settings for scan
   type conversion](working-with-scan-type.md#settings-for-scan-type-conversion "working-with-scan-type.md#settings-for-scan-type-conversion") to determine
   the values that you want to set for interlacing or deinterlacing.
2. Use the MediaConvert console to generate your JSON job specification.
   We recommend this approach, because the console functions as an
   interactive validator against the MediaConvert job schema. Follow these
   steps to generate your JSON job specification using the console:
   1. Follow the previous procedure for the console.
   2. In the **Job** pane on the left, under **Job
      settings**, choose **Show job
      JSON**.Find additional information, including where each setting belongs in the job
      settings structure, in the _AWS Elemental MediaConvert API
      Reference_. Links in this list go to information about the setting
      in that document:
   - **Deinterlacer** preprocessor: `Deinterlacer`
   - **Deinterlace Control**: `DeinterlacerControl`
   - **Deinterlace algorithm**: `DeinterlaceAlgorithm`
   - **Deinterlace mode**: `DeinterlacerMode`
   - **Interlace mode**
     (`interlaceMode`)
     - AVC (H.264): `interlaceMode`
     - HEVC (H.265): `interlaceMode`
     - MPEG-2: `interlaceMode`
     - Apple ProRes: `interlaceMode`

   - **Telecine** (`telecine`)
     - AVC (H.264): `telecine`
     - HEVC (H.265): `telecine`
     - MPEG-2: `telecine`
     - Apple ProRes: `telecine`

   - **Scan type** (`InputScanType`)
