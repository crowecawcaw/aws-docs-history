# Collection types

Collection types provide a way to organize and structure data for efficient retrieval and
analysis. They are used in ML databases to define the schema of a dataset and its elements. In
Amazon SageMaker Feature Store, the supported collection types include list, set, and vector.

Collections are a grouping of elements in which each element within the collection must have
the same feature type (`String`, `Integral`, or `Fractional`).
For example, a collection can contain elements with all of the element feature types as
`Fractional`, but a collection cannot contain elements with some feature types as
`Fractional` and some feature types as `String`.

Only `InMemory` online store feature groups currently support collection types.
The following list describes the collection type options.

**List**: An ordered collection of elements.

- The length of the list is determined by how many elements are in the collection.
- Example: You can have a list such as [‘a’, ‘b’, ‘a’], because the list preserves the order
  and can have repeat elements.
  **Set**: An unordered collection of unique elements.

- The length of the set is determined by how many unique elements are in the
  collection.
- Example: You cannot have a set such as [‘a’, 'b', 'a'], because it contains a repeat
  element. The set will instead have the elements [‘a’, ‘b’], because the set only contains unique
  elements.
  **Vector**: A specialized list that represents a fixed-size
  array of elements. The order of the elements hold significance, such that the positions of the
  elements represent certain properties of the data.

- The elements in the vector collection type _must_ have the
  `Fractional` feature type.
- You may only have one vector collection type per online store `InMemory` tier
  feature group.
- The dimension (number of elements in the vector) of the vector is predetermined by you and
  is specified using `VectorDimension`. The max dimension limit is 8192.
- Example: You can have a vector such as [4.2, -6.3, 4.2], where the first, second, and third
  elements can represent the x, y, and z positions in physical space.
  There are no limits on the length of the collections, as long as they don't exceed the
  maximum size of a record. For the maximum size of a record, see [Quotas, naming rules and data types](feature-store-quotas.md "feature-store-quotas.md").
