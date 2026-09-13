

# Setting Up Dynamic Multiview Outputs (Console)
<a name="dynamic-multiview-console"></a>

This section walks through creating a multiview output group in the AWS Elemental MediaLive console. Repeat it for each source feed — one MediaLive channel per feed.

**Before you start**
+ A MediaPackage V2 channel group containing one channel per source feed.
+ A decision about which layouts you want to support, which determines the renditions you need. See [How Dynamic Multiview works](dynamic-multiview-how-it-works.md).

**To create a multiview output group**

1. **Create or edit the channel.** Create the channel as you normally would, or open an existing channel for editing. Configure the input and input attachment first; nothing about the input is multiview-specific.

1. **Add a multiview output group.** Add an output group and choose the **MediaPackage Multiview** output group. This will create a MediaPackage output group. There isn't a new "multiview" output group variant in the API or SDK, but the **MediaPackage Multiview** option in the console is a shortcut to help expedite and simplify encode setup for multiview.

1. **Answer the wizard prompts.** The console asks for the properties it needs to generate a valid set of outputs:
   + **Codec** – H.264, H.265, or both.
   + **Frame rate** – Choose the default frame rate to configure. All properties are editable afterwards.
   + **Layout support** – Whether you want MediaLive to generate encodes that are suited for equal-size layouts, primary/secondary layouts, or both.

   The wizard uses these answers to generate a set of outputs with dimensions, encoder settings, and multiview usage roles already filled in so the channel has a tuned ABR stack and passes validation. All properties can be edited afterwards if changes are desired.

1. **Review the generated outputs.** The wizard creates an output group backed by a MediaPackage V2 destination with CMAF Ingest outputs. Enter the MediaPackage channel group name and the endpoint ID.

   Also, check the generated outputs before saving. For each one, confirm:
   + **Resolution** – that the ladder covers the range you want, and that primary/secondary pairs are in an exact 2:1 relationship.
   + **Bitrate** – the wizard's defaults are a starting point; tune them for your content.