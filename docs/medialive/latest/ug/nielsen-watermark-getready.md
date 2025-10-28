# Getting

ready

To prepare to insert Nielsen watermarks in a MediaLive output, you must obtain some information
about the watermarks data for each channel.

###### To get ready for watermarks

1.  Determine if you should insert NAES II (N2), NAES VI (NW) watermarks,
    or CBET watermarks. NAES II are used in the United States. CBET are used in
    Canada. You can insert one or both types in the same audio encode.
2.  Obtain the following information from your contact at The Nielsen
    Company:

        * For NAES II or NAES VI watermarks:




        	+ Source Identification Code (SID).
        	+ NAES check digit code.
        * For CBET watermarks:




        	+ CBET Source Identification (CSID) code.
        	+ CBET check digit code.

    You must obtain separate sets of values for each channel.

3.  If you are setting up CBET watermarks, decide how you want to handle
    watermarks that are already in the source audio. The options are the
    following:
    - Remove all the existing watermarks and replace them with new
      ones.
    - Keep the existing watermarks. MediaLive will insert new watermarks only
      in portions of the audio stream where there are no watermarks.
