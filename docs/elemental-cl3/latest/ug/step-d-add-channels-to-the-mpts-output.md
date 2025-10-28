# Step 2. Add

channels to the MPTS

After you create the MPTS, you must add channels. The [channels must already
exist](resource_channel.md "resource_channel.md").

1. On the Conductor Live main menu, choose **MPTS**.
2. Select the MPTS by ID or by name. If the MPTS is listed
   twice, it has been set up for [output
   listening](worker-nodes-other-resiliency.md "worker-nodes-other-resiliency.md"). Select the MPTS that is marked as
   **Primary**.

The **Details** page for the MPTS appear.
The page has four tabs, and the **Channels**
tab is currently selected. 3. On the **MPTS Details** page, select the
**Channels** tab. Note that the area at
the bottom of the page lists the channels in the MPTS. This
list is currently empty. 4. Choose **Add a Channel** and choose from
the list of channels that appears. To appear in this list, a
channel must have these characteristics:

    * It must be set up as an SPTS channel with MPTS
     membership set to **Remote**.
    * It can't already be in another MPTS.
    * It can't already be assigned to an MPTS unless using
     CBR rate control.


    When a channel is using CBR for the Rate Control
     Mode, it can be used in unlimited MPTSes.

5. When you select the channel, it is added to the list of
   channels for this MPTS. The list has several tabs.
6. Complete the fields in the tabs as appropriate. For more
   information about the significant fields, see the sections
   after this procedure.
7. Choose **Save**.
   The MPTS is now ready to start. See [Starting or stopping an
   MPTS](starting-an-mpts-output.md "starting-an-mpts-output.md").

###### Topics

- [Basic tab](mpts-channel-tab-basic.md "mpts-channel-tab-basic.md")
- [PID Controls tab](mpts-channel-tab-pid.md "mpts-channel-tab-pid.md")
- [TS Endpoints tab](mpts-channel-tab-ts.md "mpts-channel-tab-ts.md")
- [Complexity
  Endpoints tab](mpts-channel-tab-complexity.md "mpts-channel-tab-complexity.md")
- [RateAllocation
  Endpoints tab](mpts-channel-tab-allocation.md "mpts-channel-tab-allocation.md")
