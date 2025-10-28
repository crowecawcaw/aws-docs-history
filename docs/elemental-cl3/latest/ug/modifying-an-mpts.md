# Modifying an MPTS

1. On the Conductor Live main menu, choose **MPTS**.
2. Look for the MPTS you want. If the MPTS is listed twice, it
   has been set up for [output
   listening](worker-nodes-other-resiliency.md#es-resiliency-opl "worker-nodes-other-resiliency.md#es-resiliency-opl"). Find the MPTS that is marked as primary, and
   select it by ID or by name.

The **Details** page for the MPTS appear.
**Modify the properties of the
MPTS**

You can change any of the fields on this tab even if the MPTS is
running. For information on the fields, see [Creating a standard
MPTS](setting-up-mpts-outputs.md "setting-up-mpts-outputs.md"). The change takes effect
immediately. For example, if you change the transport stream bitrate,
the muxer starts using the new value immediately.

1. Choose the **Configuration** tab.
2. Change any fields and choose **Save**.
   **Add or delete channels**

You can add or delete channels, even if the MPTS has been started
and is running.

1.  Choose the **Channels** tab.
2.  Choose the action:

        * To add a channel, choose **Add a
         Channel**.


        * To delete a channel, select the
         **Delete** icon to the right of the
         channel.

    **Change the properties of one or more
    channels**

You can modify the properties of any channel, even if the MPTS has
been started and is running.

1. Choose the **Channels** tab.
2. Choose **Edit Channels**.
3. Select the tab, then change the fields for one or more
   channels.
4. Choose **Save**. The changes take effect
   immediately, on all affected channels in the MPTS.
