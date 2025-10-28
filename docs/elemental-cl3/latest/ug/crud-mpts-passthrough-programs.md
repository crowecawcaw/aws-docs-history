# Including passthrough

programs in an MPTS

Read this section if you want to include passthrough programs in the
MPTS. For guidelines and rules about including these programs in an
MPTS, see [Including passthrough
programs](mpts-passthrough-program.md "mpts-passthrough-program.md").

To pass through a program, you instruct Elemental Statmux to extract a specific
program from a _source MPTS_ that is
provided by the upstream system.

**Get ready**

To pass through one or more programs, you need the following
information:

- The source MPTS locations: The location where each upstream
  system source will push each source MPTS. The upstream system can
  decide on each location and provide it to you. Or you can let
  Elemental Statmux create a multicast address and then you can provide the
  upstream system with that location.

- The PID of each program that you want to extract from each
  source MPTS.
  **The procedure**

You can add passthrough programs while you are creating the MPTS or
after you have created it.

Follow this procedure to extract one or more programs from the same
source MPTS:

1. On the **MPTS Details** page where you want
   to add
2. Select the **Add Program Selector** button if you
   want to extract another program from the same source MPTS.
3. the programs, display the **Passthrough
   Programs** tab.
4. Select the **Add Passthrough Program**
   button. The **Add Passthrough Program** dialog
   appears. Complete the fields:
   - **Name**: Give the program a nickname
     for your internal use. This name doesn't appear in the
     outputs MPTS.
   - **Stream Endpoints** tab: Complete
     these fields if the upstream system has provided you with
     the location of the source MPTS.

5. Choose **Done**. One new entry appears in the
   list of passthrough programs in the MPTS. The entry has
   information over three tabs.
6. Select the **Basic** tab. On this tab, you
   must identify the following:
   - The program that you want to extract from the source
     MPTS. Complete the Incoming Program Number.
   - The PID for this program in the output MPTS. Complete
     the Outgoing Program Number.
   - The optional data to extract from the program: Complete
     Provider Name, Service Name, or Service Descriptor
     Passthrough for this program in the output MPTS. Or leave
     these three fields empty, to omit this information from the
     output MPTS.

7. Still on the **Basic** tab, if you want to
   extract another program from the same MPTS, select the Add
   Program Selector button on the far right. Complete the fields.
8. Select the **Stream Endpoints** tab. This tab
   shows the location of the source MPTS:
   - If you completed the location fields the dialog, this
     tab shows the information you entered. You can change any
     of the fields.
   - If you want Elemental Statmux to generate a primary and backup
     multicast address, leave these fields empty.

9. Select the **PID Controls** tab. All the
   programs that you entered in the **Basic** tab
   appear. This tab lets you remap the stream PIDs that are in the
   source program, so that the streams have different PIDs in the
   output program.

A field appears for every stream type that Elemental Statmux supports.

If you leave a field empty, 10. Select the **Add Program Selector** button if you
want to extract another program from the same source MPTS. 11. When you've added all the programs, choose
**Save**.
Review the information:

- Select the **Stream Endpoints** tab. This tab
  shows the location of the source MPTS:
  - If you completed the location fields the dialog, this
    tab shows the information you entered.
  - If you left those fields empty, Elemental Statmux has automatically
    generated a primary and backup multicast address. Give this
    information to your contact at the upstream system so that
    they can push the source MPTS to that location.
