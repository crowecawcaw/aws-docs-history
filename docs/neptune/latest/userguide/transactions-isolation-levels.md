# Definition of Isolation Levels

The "I" in `ACID` stands for _isolation_. The degree of
isolation of a transaction determines how much or little other concurrent transactions can
affect the data that it operates on.

The [SQL:1992
Standard](http://www.contrib.andrew.cmu.edu/~shadow/sql/sql1992.txt "http://www.contrib.andrew.cmu.edu/~shadow/sql/sql1992.txt") created a vocabulary for describing isolation levels. It defines three types
of interactions (that it calls _phenomena_) that can occur between two
concurrent transactions, `Tx1` and `Tx2`:

- `Dirty read` – This occurs when `Tx1` modifies an item,
  and then `Tx2` reads that item before `Tx1` has committed the change.
  Then, if `Tx1` never succeeds in committing the change, or rolls it back,
  `Tx2` has read a value that never made it into the database.
- `Non-repeatable read` – This happens when `Tx1` reads an
  item, then `Tx2` modifies or deletes that item and commits the change, and then
  `Tx1` tries to reread the item. `Tx1` now reads a different value
  than before, or finds that the item no longer exists.
- `Phantom read` – This happens when `Tx1` reads a set of
  items that satisfy a search criterion, and then `Tx2` adds a new item that
  satisfies the search criterion, and then `Tx1` repeats the search.
  `Tx1` now obtains a different set of items than it did before.
  Each of these three types of interaction can cause inconsistencies in the
  resulting data in a database.

The SQL:1992 standard defined four isolation levels that have different guarantees in terms
of the three types of interaction and the inconsistencies that they can produce. At all four
levels, a transaction can be guaranteed to execute completely or not at all:

- `READ UNCOMMITTED` – Allows all three kinds of interaction (that
  is, dirty reads, non-repeatable reads, and phantom reads).
- `READ COMMITTED` – Dirty reads are not possible, but nonrepeatable
  and phantom reads are.
- `REPEATABLE READ` – Neither dirty reads nor nonrepeatable reads are
  possible, but phantom reads still are.
- `SERIALIZABLE` – None of the three types of interaction phenomena
  can occur.
  Multiversion concurrency control (MVCC) allows one other kind of isolation, namely
  _SNAPSHOT_ isolation. This guarantees that a transaction operates
  on a snapshot of data as it exists when the transaction begins, and that no other
  transaction can change that snapshot.
