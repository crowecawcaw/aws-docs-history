

# Sequence manipulation functions
<a name="sequence-functions-syntax-support"></a>

This section describes functions for operating on sequence objects, also called sequence generators or just sequences. Sequence objects are special single-row tables created with [`CREATE SEQUENCE`](create-sequence-syntax-support.md). Sequence objects are commonly used to generate unique identifiers for rows of a table. The sequence functions provide simple, multiuser-safe methods for obtaining successive sequence values from sequence objects.

**Important**  
When using sequences, the cache value should be carefully considered. For more information, see the Important callout on the [`CREATE SEQUENCE`](create-sequence-syntax-support.md) page.  
For guidance on how best to use sequences based on workload patterns, see [Working with sequences and identity columns](sequences-identity-columns-working-with.md).


| Function | Description | 
| --- | --- | 
| nextval ( regclass ) → bigint | Advances the sequence object to its next value and returns that value. This is done atomically: even if multiple sessions run nextval concurrently, each will safely receive a distinct sequence value. If the sequence object has been created with default parameters, successive nextval calls will return increasing values beginning with 1. Other behaviors can be obtained by using appropriate parameters in the [`CREATE SEQUENCE`](create-sequence-syntax-support.md) command. This function requires USAGE or UPDATE privilege on the sequence. | 
| setval ( regclass, bigint [, boolean ] ) → bigint | Sets the sequence object's current value, and optionally its is\_called flag. The two-parameter form sets the sequence's last\_value field to the specified value and sets its is\_called field to true, meaning that the next nextval will advance the sequence before returning a value. The value that will be reported by currval is also set to the specified value. In the three-parameter form, is\_called can be set to either true or false. true has the same effect as the two-parameter form. If it's set to false, the next nextval will return exactly the specified value, and sequence advancement commences with the following nextval. Furthermore, the value reported by currval isn't changed here. For example: <pre>SELECT setval('myseq', 42);           -- Next nextval will return 43<br />SELECT setval('myseq', 42, true);     -- Same as above<br />SELECT setval('myseq', 42, false);    -- Next nextval will return 42</pre> The result returned by setval is just the value of its second argument. This function requires UPDATE privilege on the sequence. | 
| currval ( regclass ) → bigint | When called after nextval in the same transaction, returns the value most recently returned by nextval for this sequence. This function requires USAGE or SELECT privilege on the sequence. | 
| lastval () → bigint | When called after nextval in the same transaction, returns the value most recently returned by nextval. This function is identical to currval, except that instead of taking the sequence name as an argument it refers to whichever sequence nextval was most recently applied to. This function requires USAGE or SELECT privilege on the last used sequence. | 

**Warning**  
Call `currval` or `lastval` in the same transaction as `nextval`. Across transaction boundaries, their results are nondeterministic. Either function might return an error or a value from another transaction.  
If your application requires the exact value assigned by a sequence, use the value returned by `nextval` directly. For values generated during an `INSERT`, use `INSERT ... RETURNING`.

**Warning**  
The value obtained by `nextval` isn't reclaimed for re-use if the calling transaction later aborts. This can result in gaps in the sequence of assigned values. Gaps can also occur without a transaction abort. For example, an `INSERT` with an `ON CONFLICT` clause computes the row to insert, including any required `nextval` calls, before it detects a conflict. When the command follows the `ON CONFLICT` action, Aurora DSQL doesn't reclaim the sequence value.  
Likewise, sequence state changes made by `setval` are immediately visible to other transactions, and aren't undone if the calling transaction rolls back.

The sequence to be operated on by a sequence function is specified by a `regclass` argument, which is simply the OID of the sequence in the `pg_class` system catalog. You don't have to look up the OID by hand, however, because the `regclass` data type's input converter will do the work for you. See the PostgreSQL documentation on [Object Identifier Types](https://www.postgresql.org/docs/current/datatype-oid.html) for details.