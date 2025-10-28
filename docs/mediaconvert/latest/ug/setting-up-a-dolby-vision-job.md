# Configuring Dolby Vision

Use the following steps to set up a Dolby Vision job. For more
information about jobs, see [Tutorial: Configuring job settings](setting-up-a-job.md "setting-up-a-job.md").

1. For your input file or files, choose from the following:
   - MXF file, with frame-interleaved Dolby Vision metadata or
     an XML file.
   - IMF package (IMP) with frame-interleaved
     Dolby Vision metadata or an XML file. Also, specify a
     composition playlist (CPL) file for
     your input. If your CPL is from an incomplete
     IMP, choose **Supplemental IMPs** to specify the
     location of your supplemental IMPs.
   - Apple ProRes QuickTime MOV, with a Dolby Vision studio
     metadata XML file.
   - Any input with an HDR10 color space.
   - Any input with an SDR color space.

2. For each output that you want to process with Dolby Vision, do
   the following:
   1. Make sure that your output settings conform to the limitations listed
      in [Requirements](dolby-vision-job-limitations-and-requirements.md "dolby-vision-job-limitations-and-requirements.md").
   2. Enable the **Dolby Vision** preprocessor.
   3. Specify a Dolby Vision **Profile** from one of the
      following choices:
      - **Profile 5**: Includes frame-interleaved
        Dolby Vision metadata in your output.
      - **Profile 8.1**: Includes both
        frame-interleaved Dolby Vision metadata and
        HDR10 metadata in your output.

3. Choose an on-demand queue. (Your default queue is on-demand.)
