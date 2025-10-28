# Organizing redundancy

groups in the cluster

These rules and guidelines apply to organizing multiple redundancy
groups in the cluster.

- You can create as many redundancy groups as you want. For
  example, you can create several Elemental Live redundancy groups, and
  these groups can be different types.
- You can mix and match different types of redundancy
  groups. For example, you can organize all your Elemental
  Live nodes in one or more N-to-M redundancy groups, but
  organize your Elemental Statmux nodes in a 1-to-1 redundancy
  group.
- You should think about how you want to associate
  redundancy groups of Elemental Live nodes with redundancy groups of
  Elemental Statmux nodes.

There is no rule in Conductor Live that forces you set have all
the channels in one Elemental Live redundancy group serve only the
MPTSes in a single Elemental Statmux redundancy group. But you might
find it is easier to manage failures, and to track what has
happened, if you do enforce associations yourself.
