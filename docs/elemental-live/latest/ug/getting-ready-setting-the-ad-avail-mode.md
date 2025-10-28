# Getting

ready: Setting the ad avail mode

Read this section if you want to support any of the following
features:

- Manifest decoration for all outputs.
- Ad avail blanking for all outputs. (Note that this section
  does not apply to the blackout feature.)
  If you have several outputs and you want to do manifest decoration
  or ad avail blanking on some of the outputs and not on others, you have
  to set up two different profiles or events.

###### Note

You do not have to read this section if you _are_ doing Blackout image insertion but
you are not doing ad avail blanking or manifest decoration.

###### Set the ad avail mode

You must set the Ad Avail mode. The Ad Avail mode applies to all
outputs: it cannot be set uniquely for individual outputs. To set up
the Ad Avail Mode, do the following.

1. In the Profile or Event screen, click Ad Avail Controls (in
   the Input section towards the top of the screen):
2. In **Ad Avail Trigger**, choose the desired
   mode from the drop-down menu. This mode identifies which of all
   possible “ad avail” events are treated as “ad avails.” This
   distinction comes into play in manifest decoration and ad avail
   blanking. For more information, see [Manifest decoration](manifest-decoration.md "manifest-decoration.md") and [Ad avail blanking and
   blackout](ad-avail-blanking-and-blackout.md "ad-avail-blanking-and-blackout.md").

Typically, you select the mode to match the type ID that you
already know the input is using to indicate “ad avail” events.

    * **Splice Insert Mode** .
     Select this mode if the input uses splice inserts to
     indicate ad avails. The input
     might
     also contain messages for other events such as chapters or
     programs.
    * **Time Signal with APOS
     Mode**. Select this mode if the input contains
     time signals of segmentation type placement opportunity.
     The input
     might
     also contain messages for other events such as chapters or
     programs.

The following table specifies how a message (containing a specific
combination of message type and segmentation type) is treated depending
on the mode that is specified. Each message is treated as either an ad
avail, a non-ad avail, or as “other.”

Read across the first three columns to identify a combination of
mode, the message type and the segmentation type. Then in the last
three columns, identify how Elemental Live handles that
combination.

| Mode                   | Message type ID        | Segmentation type ID               | Handled as an ad avail event | Not handled as an ad avail event | Handled as another type of event |
| ---------------------- | ---------------------- | ---------------------------------- | ---------------------------- | -------------------------------- | -------------------------------- | ------------------------- | --- | --- | --- |
| Splice Insert Mode     | Splice Insert          | No segmentation descriptor present | X                            |                                  |                                  |
| Provider advertisement | X                      |                                    |                              |                                  | Distributor advertisement        | X                         |     |     |
| Placement opportunity  | X                      |                                    |                              |                                  | Other type                       |                           |     | X   |
| Time Signal            | Provider advertisement | X                                  |                              |                                  |                                  | Distributor advertisement | X   |     |     |
| Placement opportunity  | X                      |                                    |                              |                                  | Other type                       |                           |     | X   |
| Time Signal APOS Mode  | Splice Insert          | Any                                |                              | X                                |                                  |
| Time Signal            | Provider advertisement |                                    | X                            |                                  |                                  | Distributor advertisement |     | X   |     |
| Placement opportunity  | X                      |                                    |                              |                                  | Other type                       |                           |     | X   |
