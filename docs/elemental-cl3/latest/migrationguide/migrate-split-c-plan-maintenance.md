# Plan maintenance windows

You should plan to perform the cluster migration in several phases.

**First phase**

You can perform the tasks in [Step A: Get ready](migrate-split-c-get-ready.md "migrate-split-c-get-ready.md") outside of a
maintenance window.

**Second phase**

Perform the following tasks in one or more maintenance windows. The number of windows
depends on the number of nodes you can complete in one maintenance window.

- [Step B: Prepare each node](migrate-split-c-prepare-node.md "migrate-split-c-prepare-node.md")
  **Remaining phases**

Perform all the following tasks on several maintenance windows.

- [Step C: Split the cluster](migrate-split-c-split.md "migrate-split-c-split.md")
- [Step D: Upgrade node X](migrate-split-c-upgrade-primary.md "migrate-split-c-upgrade-primary.md")
- [Step E: Upgrade the worker
  nodes](migrate-split-c-upgrade-w-nodes.md "migrate-split-c-upgrade-w-nodes.md")
- [Step F: Upgrade node Y](migrate-split-c-upgrade-secondary.md "migrate-split-c-upgrade-secondary.md")
- [Step G: Add node Y to cluster](migrate-split-c-add-secondary.md "migrate-split-c-add-secondary.md")
  Follow these rules:

- Perform step C in one window, and perform step D in the next window. Or
  combine steps C and D in one window.

You could also perform step D outside of a maintenance window (but before you
perform step E). You can do this because node X is no longer active — it's not
part of the working cluster.

- Perform step E on as many nodes as you can in one maintenance window. In each
  window, you remove one or more workers nodes from the original cluster and put
  them in the new cluster. Eventually, all the worker nodes will be in the new
  cluster.

A consideration when you decide which worker nodes to migrate at the same time
is whether you have routers in the cluster. Identify all worker nodes that use
the SDI inputs attached to the router. Then plan to migrate those worker nodes
together. After you've migrated all those nodes, you will be able to reconfigure
the new cluster for that router.

- Then perform step F in one window, and step G in the next window. Or combine
  steps F and G in one window.

You could also perform step F outside of a maintenance window (but before you
perform step G). You can do this because node Y is no longer active — it's not
part of the working cluster.
