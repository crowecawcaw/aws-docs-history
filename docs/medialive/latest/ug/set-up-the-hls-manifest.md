# Language information in HLS manifests

This section applies if you are [setting up
captions in an HLS output group](output-embedded-and-more.md "output-embedded-and-more.md") in a MediaLive channel. You must include captions
language information in the manifest.

If the captions are embedded captions and the output is HLS, you must include captions
language information in the manifest. If you don't include this information, the
downstream player won't have information about the embedded captions. To include language
information in the manifest:

1. In the HLS output group in Output groups, go to the
   **Captions** section. In **Captions language
   setting**, choose **Insert**. Choosing this option inserts
   lines in the manifest for each embedded captions language. It inserts as many lines as
   the mappings that you will add in the next step.

###### Note

This **Captions** section is in the output group. Don't confuse
this section with the the captions encode sections in the individual outputs. 2. Still in the HLS output group, for **HLS settings**, in
**Captions language mappings**, choose **Add captions
language mappings**. 3. Choose **Add captions language mappings** again to add more
mapping groups, one for each embedded captions asset, to a maximum of four groups. For
example, if the output embedded languages contain English, French, and Spanish, you
need three mapping groups. 4. Complete each mapping group to identify the CC (caption channel) number and its
language. Specify the language as a three-letter ISO language code, as per ISO 639-2.
For example, if captions channel 1 is French, then set up the three fields with "1",
"fre", and "French".

The order in which you enter the languages must match the order of the captions in
the source. For example, if the captions are in the order French, then English, then
Spanish, then Portuguese, then set up CC1 as French, CC2 as English, and so on. If you
don't order them correctly, the captions in the manifest will be tagged with the wrong
languages.
