# Full mapping

A highly flexible yet expensive approach is to explicitly map every key to a cell. This
comes with the downsides of a critical read and write dependency on the mapping table, a
read-your-writes consistency requirement, and a large amount of state.

![Diagram showing a full mapping.](images/full-mapping.jpg)

_Full mapping_

Advantages:

- Simple to implement.
- More control over distribution to control hot cells and to perform a cell
  migration.
  Disadvantages:

- Higher performance cost when cardinality is too high.
- If the map is kept in memory, it might have a longer cell router bootstrap
  time.
