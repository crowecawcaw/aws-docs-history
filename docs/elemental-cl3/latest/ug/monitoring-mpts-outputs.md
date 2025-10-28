# Monitoring MPTS

outputs

###### Topics

- [Monitoring the progress of all MPTSes](#monitoring-the-progress-of-all-mpts-outputs "#monitoring-the-progress-of-all-mpts-outputs")
- [Monitoring the
  muxing performance of an MPTS](#monitoring-the-muxing-performance "#monitoring-the-muxing-performance")
- [Modifying the MPTS while it is running](#modifying-the-mpts-output-while-it-is-running "#modifying-the-mpts-output-while-it-is-running")

## Monitoring the progress of all MPTSes

You should monitor every MPTS constantly to ensure that none has
failed.

1. On the AWS Elemental Conductor Live main menu, choose **Status**, then choose
   **Overview**. Information about the MPTS appears.
2. If at least one MPTS is in error, go to the
   **MPTS** page.
3. Look for any MPTS that has an orange icon in the
   **Status** column.
4. Choose an orange icon to go to the **Status –
   Alerts & Messages** page. This page appears
   with the filter set to show only the information for this MPTS
   output.
5. Review the alerts and messages to determine why the MPTS
   failed.

## Monitoring the

muxing performance of an MPTS

To monitor the muxing of an individual MPTS, display the
**MPTS** page and choose
**Performance** (graph icon) beside the item.The
MPTS **Details** appears with the
**Performance** tab on top.

## Modifying the MPTS while it is running

You can modify the MPTS ouput even when it is running:

- You can modify its properties.
- To add or remove channels.

See [Modifying an MPTS](modifying-an-mpts.md "modifying-an-mpts.md").
