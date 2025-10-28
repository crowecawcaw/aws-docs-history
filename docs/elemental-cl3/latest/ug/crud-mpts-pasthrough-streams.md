# Including passthrough

streams in an MPTS

Read this section if you want to include passthrough streams in the
MPTS. For guidelines and rules about the streams that you can pass
through, see [Passing through custom
streams](mpts-passthrough-high-pids.md "mpts-passthrough-high-pids.md") and [Passing through SI/PSI
tables](mpts-passthrough-PSI-pids.md "mpts-passthrough-PSI-pids.md")

To pass through a stream, you instruct Elemental Statmux to extract a specific
PID from a _source MPTS_ that is
provided by the upstream system. Elemental Statmux. The PID must identify a single
stream, not a program.

**Get ready**

To pass through one or more streams, you need the following
information:

- The source MPTS locations: The location where each upstream
  system source will push each source MPTS. The upstream system can
  decide on each location and provide it to you. Or you can let
  Elemental Statmux create a multicast address and then you can provide the
  upstream system with that location.

- The PID of each stream that you want to extract from each
  source MPTS.
  **The procedure**

You can add passthrough streams while you are creating the MPTS or
after you have created it.

Follow this procedure to extract one or more streams from the same
source MPTS:

1. On the **MPTS Details** page where you want
   to add the streams, display the **Passthrough
   Streams** tab.
2. Select the **Add Passthrough Stream** button.
   The **Add Passthrough Stream** dialog appears.
   Complete the fields:
   - **Name**: Give the program a nickname
     for your internal use. This name doesn't appear in the
     outputs MPTS.
   - **PID Controls – Incoming**: Identify
     the PID that you want to extract from the program. This PID
     must be discoverable — it must be included in a PMT that is
     included in the PAT for the source MPTS.
   - **PID Controls – Outgoing**: The PID to
     assign to the stream in the output MPTS.

   You must specify this PID, which means it must be unique
   among all the PIDs that you are manually specifying in the
   entire MPTS. You don't need to worry about it being unique
   among the PIDs that Elemental Statmux will assign because Elemental Statmux will
   always work around the PIDs you've assigned
   manually.

3. Select the **Add PID Mapping** button if you want
   to extract another stream from the same source MPTS.
4. Select the **Stream Endpoints** tab: Complete
   these fields if the upstream system has provided you with the
   location of the source MPTS.
5. Choose **Done**. One new entry appears in the
   list of passthrough streams in the MPTS.
6. Choose **Save**.
   Review the information:

- Select the **Stream Endpoints** tab. This tab
  shows the location of the source MPTS:
  - If you completed the location fields the dialog, this
    tab shows the information you entered.
  - If you left the location fields empty on the dialog,
    Elemental Statmux has automatically generated a primary and backup
    multicast address. Give this information to your contact at
    the upstream system so that they can push the source MPTS
    to that location.

- Select the **PID Controls** tab. All the PIDs
  that you entered on the dialog appear in the same entry.
