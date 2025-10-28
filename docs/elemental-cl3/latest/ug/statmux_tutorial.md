# AWS Elemental Statmux tutorial

This tutorial describes how to create a statmuxed MPTS
workflow.

All the data in this tutorial is an example. You can adapt the workflow and create it
yourself if, you have one AWS Elemental Conductor Live node, one AWS Elemental Statmux node, and one AWS Elemental Live node, if
you have at least two sources that can be set up as inputs into Elemental Live, and if you have a
multicast address where you can send an MPTS output.

## Assumptions about

existing knowledge

We assume the following:

- We assume that you have some familiarity with the basic
  features of Conductor Live. You are familiar with setting up
  nodes in a cluster, and with creating redundancy groups to
  provide resiliency for CL3 outputs.
- We assume that you are very familiar with the structure
  and purpose of the events (channels) that you create using
  Elemental Live.
- We assume that you are familiar with the uses of statmux
  MPTS, and with multicast and unicast. You don't need to be
  familiar with how to create MPTSes using Conductor
  Live and Elemental Statmux.

## Step 1: Check

your cluster and redundant nodes

We're not going to show you how to create the cluster. Assume
you've already set up the following:

- Conductor Live is set up in a redundancy group as a high
  availability (HA) pair. This setup ensures that the MPTS
  workflow doesn't stop if one Conductor Live node
  fails.

Assume that the redundancy group is named CL_pair.

Assume that the two nodes are called CL_1 and CL_2.

- A pair of Elemental Statmux node in a 1-to-1 redundancy
  group. Both nodes actively process the same MPTS, which
  means they are both _hot_
  nodes. Conductor Live manages which output gets delivered.
  This setup ensures that there is no interruption if one node
  fails.

Assume that the redundancy group is named
SM_1-to-1_hot.

Assume that the nodes are called SM_X and SM_Y.

- Several Elemental Live nodes in an N-to-M redundancy group.
  Let's say there are three active nodes and one backup node
  serving those three active nodes. This setup ensures that
  encoding of the SPTS channels can quickly recover if the
  active Elemental Live node fails.

Assume that the redundancy group is named Live_NM.

Assume that the three active nodes are called EL_A, EL_B,
and EL_C.

Assume that the two backup nodes are called EL_D and
EL_E.

When you've read this tutorial, you can get more
information about [redundancy](cl3-resiliency.md "cl3-resiliency.md").

This is what you would see on the web interface for a cluster that
is set up in this way:

- When you chose **Cluster**, then
  **Nodes** on the Conductor Live main menu, you
  would see the following:
  - **CL_1**, with the following
    information:

  A key icon that indicates that it is currently the
  primary node.

  The redundancy type set as
  **HA**.
  - **CL_2**, with the same
    information, but without the key icon.
  - **SM_X** and
    **SM_Y** with the following
    information:

  The name of the redundancy group.

  Note that both nodes and in the same redundancy
  group, and that they are the only nodes in the
  group. From this you can infer that the nodes are
  set up as a 1-to-1 redundancy group.

  The number of MPTSes that exist on each
  node.

  Channels will always be 0 for an Elemental Statmux
  node.
  - The five Elemental Live nodes with the following
    information:

  The name of the redundancy group.

  Notice that all the nodes are in the same
  redundancy group, and that there are more than three
  nodes in the group. From this you can infer that the
  nodes are set up as an N-to-M redundancy group.

  The number of channels that exist on each
  node.

  MPTS will always be 0 for an Elemental Live
  node.

- When you chose **Cluster**, then
  **Redundancy** on the Conductor Live
  main menu, you would see the following:
  - In the **CL_pair** redundancy
    group, you would see **HA**.
  - In the **SM_1-to-1_hot**
    redundancy group, you would see two nodes in the
    **Active Nodes** tab, and no
    nodes in the **Backup Nodes** tab.
    This is a 1-to-1 redundancy group, so it doesn't
    have backup nodes.
  - In the **Live_NM** redundancy
    group, you would see three nodes in the
    **Active Nodes** tab, and two
    nodes in the **Backup Nodes**
    tab.

After you've read this tutorial, you can get more information
about [redundancy](cl3-resiliency.md "cl3-resiliency.md").

## Step 2: Create the

profiles

You must create the profiles that you require for the SPTS
channels that will produce the output from Elemental Live.

1. On the Conductor Live main menu, choose
   **Profiles**. On the
   **Profiles** page, choose **New
   Profile** (on the top right corner of the
   page).
2. Give the profile a name such as
   `SPTS-high-resolution`.
3. Create the profile in the usual way for everything except
   the output groups and outputs.
4. To set up the outputs on the profile, scroll down to
   **Output Groups** and choose the
   **UDP/TS** tab.
5. In the **New Output** section, choose the
   **Add Output** button.
6. For **MPTS membership**, choose
   **Remote**. This output section changes
   to display different fields. Leave the defaults for these
   fields.
7. In the **Streams** section, in the
   **Video** section, choose
   **Advanced** to display more fields.
   Set the following field:

**Rate Control Mode**: Set to
**Statmux**. This value indicates that
the muxer will control the rate control for the output.

Note that when you set this value, the
**Bitrate**, **Max
Bitrate**, and **Min Bitrate**
fields don't apply, so these fields become disabled. 8. Choose **Save**.

The profile that you created is listed on the
**Profiles** page. Conductor Live assigns a
unique numerical ID to the profile.

Under the **Channels** column, the profile
displays 0 0. This indicates that the profile is not yet being used
by any channels.

## Step 3: Create the SPTS

channels

You must create the SPTS channels that produce the SPTS outputs.
In the Conductor Live main menu, choose Channels to display the
Channels screen.

1. On the Conductor Live main menu, choose
   **Channels**. On the
   **Channel** page, choose **New
   Channel** (on the top right corner of the
   page).
2. Give the channel a name such as
   **Program_A**. Select the profile you
   just created.
3. In **Node**, choose the Elemental Live node where
   you want the channel to run. Note that the dropdown list
   shows only active Elemental Live nodes. It doesn't show backup Elemental Live
   nodes or any Elemental Statmux nodes.
4. Choose **Save**.
5. Repeat these steps to create the second channel. Name the
   channel **Program_B**. Choose the same
   profile as you did for the first channel. Choose the same
   Elemental Live node.

The channels that you created are listed on the
**Channels** page. Conductor Live assigns a unique
numerical ID to each channel. The row for each channel specifies its
profile and node.

Choose the **Profiles** page again. Note that the
profile that you created now displays **0 2**, to
indicate that the profile is being used by two channels but none of
the channels is active.

## Step 4: Create the

MPTS

You are now ready to create the MPTS. You set up this MPTS to
include the two channels that you created.

- On the Conductor Live main menu, choose **MPTS**.
  On the **MPTS** page, choose the
  **MPTS** button at the top right
  corner. The **Create a New MPTS** dialog
  appears.
- In the **Node** field, choose the arrow
  to show the dropdown list. The list shows both the Elemental Statmux
  nodes. In **1-to-1 redundancy** group, both
  nodes are active, so both nodes are listed in this dropdown.
  With a 1-to-1 redundancy group, there is no sense of one
  node being the leader and the other being the follower.

Therefore, you can choose either node.

- Choose one of the nodes where the MPTS will run.
- Complete the other fields. Pay particular attention to
  these fields:
  - **Name**. Give the node a name.
    For example, `MyMPTS`.

  For example, choose the node
  **SM_X**.
  - **Transport Stream Bitrate**.
    Enter a value here. This value is the total bitrate
    for the MPTS. All the SPTS channels in the MPTS will
    use a portion of this bitrate.
  - **URI**. This is the address to
    the destination on the downstream system. Conductor Live
    will deliver the MPTS to this address.
  - **Output listening**. Leave this
    field unchecked. This field applies if you want
    Elemental Statmux output listening resiliency. After
    you've finished this tutorial, you can get more
    information about [output
    listening](worker-nodes-other-resiliency.md "worker-nodes-other-resiliency.md").
  - **Add Destination**. Don't choose
    this button because we won't create another
    destination. You create a second destination for
    this MPTS only if you want statmux output
    redundancy. After you've finished this tutorial, you
    can get more information about [output
    redundancy](worker-nodes-other-resiliency.md "worker-nodes-other-resiliency.md").
  - Leave the default values for other fields.

- Choose the **Advanced** tab. This tab
  shows information for the SI/PSI tables. Remember that when
  you created the profiles, you ignored the fields for the
  SI/PSI tables. The tables on this tab let you create tables
  that apply to the entire MPTS. For now, leave the
  defaults.
- Choose **Save**.

The MPTS appears in the list of MPTSes. The node where you created
the MPTS (node `SM_X`) is part of a 1-to-1
redundancy group. Therefore, Conductor Live creates two instances of the
MPTS.

The two MPTSes have identical URLs in the
**Destinations** column, because the two MPTS
instances are exactly identical. One node is tagged as
**Primary**, the other as
**Secondary**.

Conductor Live assigns a unique numerical ID. The
**Channels** column displays **0 0
0**. The last 0 specifies that the MPTS doesn't have
any programs yet. We'll add those in the next step.

After you've finished this tutorial, you can get more information
about [Elemental Statmux node
redundancy](redundancy-worker.md "redundancy-worker.md").

## Step 5: Add programs

to the MPTS

After you create the MPTS, it has no programs in it. You must add
programs before you can run the MPTS.

1. Still on the **MPTS** page, choose the
   MPTS by its name (**MyMPTS**). Choose the
   primary instance of the MPTS. The
   **Details** page for the MPTS appear.
   The page has four tabs, and the
   **Channels** tab is currently
   selected.
2. On the upper right side of the page, look for the
   **Add Channel** field in the gray
   section.
3. Choose the down arrow and choose one of the channels that
   you added.

An empty row appears for the new channel. 4. In the **Basic** tab, complete the
**Service Name** and **Provider
Name**. Elemental Statmux uses this information
to create the SDT in the MPTS. 5. Leave the other fields blank. Note that you don’t need to
enter a minimum and maximum bitrate. 6. Choose **Save**. 7. Repeat to choose the other channel. 8. If you want to look at how these channels look in the
MPTS, choose **MPTS** on the Conductor Live main
menu.

On the **Basic** tab, note this
information:

    * **#**: A numerical ID for each
     program in this MPTS. The number is unique within
     this MPTS.
    * **ID**: A numerical ID for each
     program. This number is unique among all MPTSes in
     this Conductor Live cluster.
    * **Encoders**: Specifies the
     number of Elemental Live encoders that are currently providing
     programs (channels) to this MPTS.
    * **Program Number**: The PID for this
     program. When you added the channel to the MPTS, you
     had the option to specify this ID. In this tutorial,
     we didn't do that, so Conductor Live assigns a
     unique ID to each program in this field in the
     MPTs.
    * **Min and Max Bitrate**. Remember
     that when we added the program, we left these fields
     empty. Therefore, Conductor Live automatically
     assigns values.

The other tabs display information that Conductor Live
automatically assigns. Typically, there is no need to change these
values.

## Step 6: Start the

MPTS

There are two steps to starting the MPTS: start all the channels,
then start the MPTS. You should start processing in this order so
that when the MPTS starts, it immediately starts with its full
complement of programs (channels).

1. Start the channels: On the Conductor Live main menu, choose
   **Channels**.
2. Normally, you would identify the channels that belong to
   the MPTS you are starting. In our example, there is only one
   MPTS, so you don't need to do that.
3. In the row for each channel, choose the green arrow button
   on the far right.

Look at the **Status** column and make
sure that all the channels are running. 4. Start the MPTS: On the Conductor Live main menu, choose
**MPTS**. 5. In the row for the first instance of
**MyMPTS**, choose the
**Start** (green arrow) button on the
far right. 6. Repeat for the second instance of
**MyMPTS**. 7. The **Status** column shows both the
MPTSes as **Running**.

They are both running, because the Elemental Statmux node
is set up in a 1-to-1 redundancy group.

One instance of the MPTS is running on one node. The other
instance is running on the other node. 8. On the **MPTS** page, choose the MPTS by
its name. The **MPTS Details** page
appears. 9. On the left side of the page, choose the
**Performance** tab. The graphic
indicates the bandwidth allocation that Conductor Live is
continually applying to the entire MPTS and to each program
in the MPTS.

This tutorial has walked you through creating and starting an
MPTS.
