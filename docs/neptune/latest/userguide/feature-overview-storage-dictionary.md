# Dictionary of user-facing values

Neptune does not store most user-facing values directly in the various indexes
it maintains. Instead, it stores them separately in a dictionary and replaces them
in the indexes with 8-byte identifiers.

- All user-facing values that would go in `S`, `P`,
  or `G` indexes are stored in the dictionary in this way.
- In the `O` index, numeric values are stored
  directly in the index (inlined). This includes `date` and
  `datetime` values (represented as milliseconds from the epoch).
- All other user-facing values that would go in the `O`
  index are stored in the dictionary and represented in the index by IDs.
  The dictionary contains a forward mapping of user-facing values to 8-byte
  IDs in a `value_to_id` index.

It stores the reverse mapping of 8-byte IDs to values in one of two indexes,
depending on the size of the values:

- An `id_to_value` index maps IDs to user-facing values
  that are smaller than 767 bytes after internal encoding.
- An `id_to_blob` index maps IDs to user-facing values
  that are larger.
