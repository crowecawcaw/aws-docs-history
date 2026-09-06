

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# Setting up the HLS Manifest
<a name="set-up-the-hls-manifest"></a>

If the captions are embedded captions and the output is HLS, you can choose to include caption language information in the manifest.

1. In the HLS output group, go to the output. Click **Advanced**.

1. Complete Caption Languages as desired:
   + **Omit**: To omit any CLOSED-CAPTION lines in the manifest.
   + **None**: To include one CLOSED-CAPTION=None line in the manifest.
   + **Insert**: To insert one or more lines in the manifest.

1. If you chose **Insert**, more fields appear. Complete on more sets of fields. 
+ You should complete as many fields as there are languages in this output. 
+ The order in which you enter the languages must match the order of the captions in the source. For example, if the captions are in the order English, then French, then Spanish, then Portuguese, then set up CC1 as English, CC2 as French, and so on. If you do not order them correctly, the captions will be tagged with the wrong languages.