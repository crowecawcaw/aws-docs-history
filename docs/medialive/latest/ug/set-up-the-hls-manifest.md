

# Language information in HLS manifests
<a name="set-up-the-hls-manifest"></a>

This section applies if you are [setting up captions in an HLS output group](output-embedded-and-more.md) in a MediaLive channel. You must include captions language information in the manifest.

For information about MediaPackage output groups with a MediaPackage v2 destination, see [MediaPackage v2 destinations](#set-up-the-hls-manifest-emp-v2).

If the captions are embedded captions and the output is HLS, you must include captions language information in the manifest. If you don't include this information, the downstream player won't have information about the embedded captions. To include language information in the manifest: 

1. In the HLS output group in Output groups, go to the **Captions** section. In **Captions language setting**, choose **Insert**. Choosing this option inserts lines in the manifest for each embedded captions language. It inserts as many lines as the mappings that you will add in the next step. 
**Note**  
This **Captions** section is in the output group. Don't confuse this section with the captions encode sections in the individual outputs.

1. Still in the HLS output group, for **HLS settings**, in **Captions language mappings**, choose **Add captions language mappings**.

1. Choose **Add captions language mappings** again to add more mapping groups, one for each embedded captions asset, to a maximum of four groups. For example, if the output embedded languages contain English, French, and Spanish, you need three mapping groups.

1. Complete each mapping group to identify the CC (caption channel) number and its language. Specify the language as a three-letter ISO language code, as per ISO 639-2. For example, if captions channel 1 is French, then set up the three fields with "1", "fre", and "French". 

   The order in which you enter the languages must match the order of the captions in the source. For example, if the captions are in the order French, then English, then Spanish, then Portuguese, then set up CC1 as French, CC2 as English, and so on. If you don't order them correctly, the captions in the manifest will be tagged with the wrong languages.

## MediaPackage v2 destinations
<a name="set-up-the-hls-manifest-emp-v2"></a>

In a MediaPackage output group with a MediaPackage v2 destination, **Caption Language Setting** controls the `CLOSED-CAPTIONS` signaling that MediaPackage v2 writes into the HLS manifest it delivers. This field applies only to EIA-608 embedded captions.

1. In the MediaPackage output group, in the **MediaPackage settings** section, expand **MediaPackage V2 settings**.

1. For **Caption Language Setting**, choose one of these values:
   + **Auto** – The default. If you set up **Caption Language Mappings**, the HLS manifest includes a `CLOSED-CAPTIONS` line for each mapped caption channel. If you don't, the manifest omits the `CLOSED-CAPTIONS` line.
   + **None** – The HLS manifest carries `CLOSED-CAPTIONS=NONE` on each `EXT-X-STREAM-INF` tag. This signals to players that the stream has no closed captions, so players stop offering a CC track. You can't choose **None** if you set up **Caption Language Mappings**.