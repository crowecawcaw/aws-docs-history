# Configuring SDI video

routers

If your AWS Elemental Conductor Livecluster deployment includes a router for handling SDI inputs to Elemental Live
nodes, you must configure the router in the cluster.

If SDI video inputs connect directly to the Elemental Live node with a cable, see
[Adding SDI input
devices](conductor-live-config-sdi-dev.md "conductor-live-config-sdi-dev.md").

**Rules for routers**

- The cluster can include only one SDI router.
- That router can serve several Elemental Live nodes.
  If you try to set up a second SDI router, the configuration of the
  second router will fail in [Step D: Complete the Router Input
  Mappings](sdi-rou-input.md "sdi-rou-input.md").

**Where to perform the configuration**

Make sure you perform the configuration on the correct nodes.

| Node                          | Work on this node?                                                                |
| ----------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Primary Conductor Live node   | You _configure_ the router from the primary Conductor Live.                       |
| Secondary Conductor Live node | No.                                                                               |
| Worker node                   | You physically _connect_ the router to each Elemental Live node that will use it. | ###### Warning If you forget to configure the router, everything looks acceptable on the event or profile, but when you run the event, you receive a **`no input detected`** error. ###### Topics <br>• [Step A: Gather information](sdi-router-gather-info.md "sdi-router-gather-info.md") <br>• [Step B: Run cables from the router to each node](sdi-rou-ready.md "sdi-rou-ready.md") <br>• [Step C: Add the router](sdi-rou-create.md "sdi-rou-create.md") <br>• [Step D: Complete the Router Input Mappings](sdi-rou-input.md "sdi-rou-input.md") <br>• [Step E: Complete the Router Output Mappings](sdi-rou-output.md "sdi-rou-output.md") <br>• [Step F: Sync the Routers](sdi-rou-sync.md "sdi-rou-sync.md") <br>• [Step G: Use the Router Inputs](sdi-rou-using.md "sdi-rou-using.md") |
