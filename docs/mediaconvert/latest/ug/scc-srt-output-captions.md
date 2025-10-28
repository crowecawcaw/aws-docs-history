# SCC, SRT, and SMI (sidecar) output

captions

This section covers how to configure SCC, SRT, and SMI (sidecar) output captions in AWS Elemental MediaConvert. The main topics include:

- Where to specify the captions.
- How to specify multiple captions tracks.

## Where to specify the

captions

Put your captions in the same output group, but a different output from your video.

After you add captions to an output, delete the **Video** and
**Audio 1** groups of settings that the service automatically created with
the output.

###### To delete the Video and Audio 1 groups of settings

1. On the **Create job** page, in the **Job** pane on the left, under **Output groups**, choose the output that contains
   the groups of settings that you want to delete.
2. The **Video** group of settings is automatically displayed in the
   **Stream settings** section. Choose the **Remove video selector**
   button.
3. The **Audio 1** group of settings is automatically displayed in the
   **Stream settings** section. Choose the **Remove**
   button.

## How to specify multiple

captions tracks

For each SRT, SCC or SMI output you must have one output per caption
selector. In the caption output, choose the captions selector under
**Captions source** that is set up for the track that you
want to include. They will appear in the list of settings groups as
**Captions Selector 1**, **Captions Selector
2**, and so forth.
