# Set up the HLS Manifest

(embedded captions)

This section applies when you set up the captions encode as described in [Step 1: Identify the
source captions that you want](identify-captions-in-the-input.md "identify-captions-in-the-input.md"), if the output group is HLS and the output
captions format is embedded. It describes how to include captions language information
in the manifest.

###### To specify language information in the manifest

1. In the HLS output group, go to the output. Click
   **Advanced**.
2. Complete **Caption Languages** as desired:
   - Omit: To omit any CLOSED-CAPTION lines in the manifest.
   - None: To include one CLOSED-CAPTION=None line in the manifest.
   - Insert: To insert one or more lines in the manifest.

3. If you chose **Insert**, more fields appear. Complete on more
   sets of fields.
   - You should complete as many fields as there are languages in this
     output.
   - The order in which you enter the languages must match the order of the
     captions in the source. For example, if the captions are in the order English,
     then French, then Spanish, then Portuguese, then set up CC1 as English, CC2 as
     French, and so on. If you do not order them correctly, the captions will be
     tagged with the wrong languages.
