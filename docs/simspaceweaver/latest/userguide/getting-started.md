End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Getting started with SimSpace Weaver

This section provides tutorials to help you get started with SimSpace Weaver. These tutorials
introduce you to the general workflow for building simulations with SimSpace Weaver. These tutorials demonstrate how to create, deploy, and run simulations in SimSpace Weaver. We
recommend that you begin with the quick start tutorial to get a simulation running in
minutes. Go through the other tutorials after that to learn more.

These tutorials use a sample application (`PathfindingSample`)
included in the SimSpace Weaver app SDK .zip file that you downloaded during the [setup procedures](setting-up_local.md "setting-up_local.md"). The sample application demonstrates
the concepts that all SimSpace Weaver simulations share, including spatial partitioning,
cross-partition entity handoff, apps, and subscriptions.

In the tutorials, you will create a simulation with four spatial partitions. A separate
instance of the `PathfindingSample` spatial app manages each
individual partition. The spatial apps create entities in their own partitions. The entities
move to a particular position in the simulation world, avoiding obstacles as they move. You
can use a separate client application (included in the SimSpace Weaver app SDK) to view the
simulation.

###### Topics

- [Quick start tutorial for SimSpace Weaver](getting-started_quickstart.md "getting-started_quickstart.md")
- [Detailed tutorial: Learn the details while
  building the sample application](getting-started_detailed.md "getting-started_detailed.md")
