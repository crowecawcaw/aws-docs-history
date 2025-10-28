# Cell migration

Cells should not share state or components between cells. Depending on the workload, a
cell migration strategy might be needed to migrate data/customers from one cell to another. A
possible scenario when a cell migration may be needed is if a particular customer or resource
in your workload becomes too big and requires it to have a dedicated cell.

Stateful cell-based architectures will almost certainly require online cell migration to
adjust placement when cells are added or removed. One consideration of online cell migration
is handling mapping decisions during the transitionary period. This may involve cross-cell
redirects, performing multiple iterations of the mapping algorithm when necessary, or both,
against different versions of the mapping algorithm state.

Another consideration is how to safely migrate the state. This will be system-dependent
but at a high-level will likely consist of the following phases:

- **Clone** the data from the current location into the new
  location, as a non-authoritative copy.
- **Flip** the new location copy to be
  _authoritative_.
- **Redirect** from old location to new location.
- **Forget** the data from the old location.
  Another approach is to use careful coordination between the router and the cells, for
  example using the control plane to migrate clients from one cell to another and ensuring this
  state transition before the cell is ready to receive traffic. In this case, dependencies
  between cells are avoided or kept to a minimum, as these dependencies have been influenced
  across cells and therefore decrease fault isolation.
