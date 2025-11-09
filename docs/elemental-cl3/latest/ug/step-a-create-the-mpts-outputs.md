# Step 1: Create the

MPTS

###### To create an MPTS

1. On the Conductor Live main menu, choose **MPTS**.
   Then choose **New MPTS**. The
   **Create a New MPTS** dialog
   appears.
2. Complete the fields in the top section of the dialog. For information about a field, hover on the upper-right corner of the field and choose the **?** icon. Pay particular
   attention to the following fields.

| Field                    | Description                                                                                                                              |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Name                     | Any name.                                                                                                                                |
| Transport Stream ID      | The PID for the transport stream in the<br>MPTS.                                                                                         |
| Node                     | The node where you want the MPTS to run. The<br>list shows all active nodes. It doesn't<br>include backup nodes in a redundancy<br>group |
| Transport Stream Bitrate | The total bitrate for the MPTS.<br>All the SPTS channels in the MPTS will use a<br>portion of this bitrate.                              |

3. Complete the fields in the **Output** tab
   and the **Advanced** tab. For more
   information about the significant fields, see the sections
   after this procedure.
4. Choose **Save**.

The MPTS appears in the list of MPTSes.

If the node you selected is part of a 1-to-1 or 1-to-1 Plus
redundancy group, Conductor Live automatically creates two instance of
the MPTS. One instance is on the primary Elemental Statmux node, the
other is on the secondary node. Both MPTS instances have the
same downstream system destination or destinations.

The next step in creating the MPTS is to [add
channels](step-d-add-channels-to-the-mpts-output.md "step-d-add-channels-to-the-mpts-output.md") (programs).

Other optional steps are [adding passthrough
streams](crud-mpts-pasthrough-streams.md "crud-mpts-pasthrough-streams.md"), and [adding passthrough
programs](crud-mpts-passthrough-programs.md "crud-mpts-passthrough-programs.md").

###### Topics

- [Output tab](step-create-mpts-tab-output.md "step-create-mpts-tab-output.md")
