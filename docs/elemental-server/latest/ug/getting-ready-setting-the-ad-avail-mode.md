This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Getting Ready: Setting the Ad

Avail Mode

Read this section if you want to support any of these features:

- Manifest decoration for all outputs.
- Ad avail blanking for all outputs. (Note that this section does not apply to the
  blackout feature.)
  If you have several outputs and want to do manifest decoration or ad avail blanking on
  some outputs and not others, you have to set up two different profiles or
  jobs.

###### Note

You do not have to read this section if you _are_
doing Blackout image insertion but you are not doing ad avail blanking or manifest
decoration.

###### Set the Ad Avail Mode

You must set the Ad Avail mode. The Ad Avail mode applies to all outputs: it cannot
be set differently for individual outputs.

1. In the Profile or job screen, click Advanced Avail Controls (in the Input
   section towards the top of the screen):

![The file images/advanced-avail-controls.png.](images/advanced-avail-controls.png) 2. In Ad Avail Trigger, choose the desired mode. This mode identifies which of all
possible “ad avail” events are actually to be treated as “ad avails.” This
distinction comes into play in manifest decoration and ad avail blanking. For more
information, see [Manifest Decoration](manifest-decoration.md "manifest-decoration.md") and [Ad Avail Blanking and Blackout](ad-avail-blanking-and-blackout.md "ad-avail-blanking-and-blackout.md").

Typically, you select the mode to match the type ID that you already know the
input is using to indicate “ad avail” events.

    * **Splice Insert** mode. Select this mode if the input uses
     splice inserts to indicate ad avails. The input may also contain messages for
     other events, such as chapters or programs.
    * **Timesignal with APOS** mode. Select this mode if the
     input contains time signals of segmentation type Placement Opportunity. The
     input may also contain messages for other events, such as chapters or programs.

The following table specifies how a message (containing a specific combination of
message type and segmentation type) is treated, depending on the mode that is specified.
Each message is treated as either an ad avail, a non-ad avail, or as “other."

| Mode                   | Message Type ID        | Segmentation Type ID               | Ad Avail Event | Not an Ad Avail Event | Other Event               |
| ---------------------- | ---------------------- | ---------------------------------- | -------------- | --------------------- | ------------------------- | ------------------------- | --- | --- | --- |
| Splice Insert mode     | Splice Insert          | No segmentation descriptor present | X              |                       |                           |
| Provider advertisement | X                      |                                    |                |                       | Distributor advertisement | X                         |     |     |
| Placement opportunity  | X                      |                                    |                |                       | Other type                |                           |     | X   |
| Time signal            | Provider advertisement | X                                  |                |                       |                           | Distributor advertisement | X   |     |     |
| Placement opportunity  | X                      |                                    |                |                       | Other type                |                           |     | X   |
| Time signal APOS mode  | Splice insert          | Any                                |                | X                     |                           |
| Time signal            | Provider advertisement |                                    | X              |                       |                           | Distributor advertisement |     | X   |     |
| Placement opportunity  | X                      |                                    |                |                       | Other type                |                           |     | X   |
