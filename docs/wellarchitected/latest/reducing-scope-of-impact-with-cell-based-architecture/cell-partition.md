# Cell partition

Cell partition is related to how you will divide your traffic between cells, since each
cell is an independent replica of your workload. This division is done using a partition
key, which can be simple or composite according to your workload requirements.

Partition keys must be chosen to match the _grain_ of the service, or
the natural ways that a service's workload can be subdivided with minimal cross-grain
interactions. A good partition key is one that is easily accessible in most API calls, either
as a direct parameter or a direct transformation of a parameter.

A key consideration in selecting a partition key is the maximum cell size requirements.
`CustomerID` might seem like a reasonable candidate partition key for many use
cases, but thought needs to go into how to handle really large customers. It is unlikely you
want to limit the degree to which a customer can adopt your service. For example, if you
choose the `CustomerID` for your partition key and a single customer of yours
becomes so big that it doesn't fit into a single cell anymore, but it needs to be allocated
across two cells. A good strategy is to define a second dimension more aligned with your type
of business to be part of the partition key along with the customerId of the customer in this
example.

Some service interactions might go against the grain of the partition key, or cause the
workload to span multiple cells (for example, scatter-gather). These are inevitable and need
to be accommodated, but should represent the minority of the service's workload. One approach
for this is that instead of letting the cells talk directly to each other, any cross-cell
calls have to go back through the normal cell router.

There are a variety of partitioning algorithms that can be used to map keys to cells.
Regardless of algorithm, there needs to be:

- A mechanism to serve or distribute state used by these algorithms,
- Accommodations for gracefully handling migration when cells are added and removed.
  The following is a non-exhaustive list of partitioning algorithms presented without
  specific recommendations.

###### Topics

- [Full mapping](full-mapping.md "full-mapping.md")
- [Prefix and range-based mapping](prefix-and-range-based-mapping.md "prefix-and-range-based-mapping.md")
- [Naïve modulo mapping or
  fixed partition number](naive-modulo-mapping-or-fixed-partition-number.md "naive-modulo-mapping-or-fixed-partition-number.md")
- [Consistent hashing](consistent-hashing.md "consistent-hashing.md")
- [A warning for all mapping
  approaches](a-warning-for-all-mapping-approaches.md "a-warning-for-all-mapping-approaches.md")
