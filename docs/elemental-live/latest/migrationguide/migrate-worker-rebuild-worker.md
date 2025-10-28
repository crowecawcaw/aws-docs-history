# Step I: Configure the Elemental Live node after

migration

**Install new licenses**

Install new licenses.

If a specific node handles SMPTE 2110 inputs or outputs, you should have obtained a
new license that includes the SMPTE 2110 add-on package. (The procedure for obtaining a
new license is described in the essential notes in the [current Release Notes](../../../elemental-live.md "../../../elemental-live.md").) To deploy the
license, see the section about configuring licenses in the [AWS Elemental Live Configuration Guide](../configguide.md "../configguide.md").

**Set up worker features**

Configuration information about some features isn't included in the database, so you
must set them up again. The features are:

- Enabling OCR conversion to handle captions
- Disabling RTMP inputs in order to release processing resources
- Setting the maximum for virtual input switching
  See the section about features in the [AWS Elemental Live Configuration Guide](../configguide.md "../configguide.md").

###### Note

You might want to voluntarily change the configuration of the appliance.

We strongly recommend that you don't make any voluntary changes to the
configuration until you have tested your workflows in the new setup.

**Reconfigure routers**

This section applies if the node was connected to an SDI input using a router. After
you upgrade, the node still has information about the SDI inputs and about the router,
but it is missing the mapping from the inputs to the router. You must reconfigure this
information. You should have [made a note
of the configuration](migrate-worker-prepare-node.md#migrate-worker-capture-router "migrate-worker-prepare-node.md#migrate-worker-capture-router").

For more information see the section about configuring routers in the
[AWS Elemental Live Configuration Guide](../configguide.md "../configguide.md").
