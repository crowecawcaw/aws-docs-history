# Step F: Rebuild the cluster

## Step F1: Add and configure the worker

nodes

Follow these steps on each worker node:

1. Add the worker node to the cluster. Then add the node to its redundancy
   group. Finally, assign channels to the node, using the [list of channel
   assignments](migrate-std-prepare-node.md#migrate-std-capture-assignments "migrate-std-prepare-node.md#migrate-std-capture-assignments")) that you created. See [Adding worker nodes](migrate-topic-add-w.md "migrate-topic-add-w.md").
2. Set up worker features.

Configuration information about some features isn't included in the
database, so you must set them up again. The features are:

    * Enabling OCR conversion to handle captions
    * Disabling RTMP inputs in order to release processing
     resources
    * Setting the maximum for virtual input switching

See the section about features in the [AWS Elemental Live Configuration Guide](../../../elemental-live/latest/configguide.md "../../../elemental-live/latest/configguide.md").

###### Note

You might want to voluntarily change the configuration of one or more of the
worker nodes.

We strongly recommend that you don't make any voluntary changes to the
configuration until you have tested your workflows in the new setup.

## Step F2: Reconfigure

routers

This section applies if the cluster previously included nodes that connected to an
SDI input using a router. After you upgrade, the cluster still has information about
the SDI inputs and about the router, but it is missing the mapping from the inputs
to the router. You must reconfigure this information. You should have [made a note of the
configuration](migrate-std-prepare-node.md#migrate-std-capture-router "migrate-std-prepare-node.md#migrate-std-capture-router").

For more information see the information about configuring routers in the
_Reference: Configure connectivity_ section of
the [AWS Elemental Conductor Live Configuration Guide](../configguide.md "../configguide.md").

See the information about configuring routers in the _Reference: Configure connectivity_ section of the [AWS Elemental Conductor Live Configuration Guide](../configguide.md "../configguide.md").
Specifically, start at the _Complete the Router Output
Mappings_ step in that procedure.

## Step F3: Add Conductor node

If the cluster included a secondary Conductor, add it to the cluster and to the Conductor Live
redundancy group. See [Adding the secondary Conductor node to the
cluster](migrate-topic-add-conductor.md "migrate-topic-add-conductor.md").

## Step F4: Final steps

1. Start channels. You can start the channels that were previously running.
   See [Restarting channels](migrate-topic-channel-start.md "migrate-topic-channel-start.md").

If you have only one Conductor, the upgrade process is now complete. 2. If you have two Conductors, re-enable HA. The secondary Conductor synchs itself to
the primary Conductor. The upgrade process is now complete.
