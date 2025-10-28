# AOSPERF04-BP03 Use the flat object type for nested

objects

Improve efficiency by using flat object types for indexing and
querying complex data structures, reducing storage and retrieval
overhead.

**Level of risk exposed if this best practice
is not established:** Medium

**Desired outcome**: You use flat
object types for indexing and querying complex data structures,
which improves the efficiency of your storage and retrieval of
nested objects.

**Benefits of establishing this best
practice:**

- **Efficient reads:** Fetching
  performance is similar to that of a keyword field.
- **Memory efficiency:** Storing
  the entire complex JSON object in one field without indexing all
  of its subfields reduces the number of fields in an index.
- **Space efficiency:** OpenSearch
  does not create an inverted index for subfields in flat objects,
  which saves space.
- **Compatibility for migration:**
  You can migrate your data from systems that support similar flat
  types to OpenSearch.

## Implementation guidance

The flat object field type treats the JSON object as a string,
allowing subfield access without indexing for faster lookup and
addressing performance concerns.

Flat objects are defined in the mapping of an index, either at
creation time or by adding a new field that is flat object type.
You cannot change an existing field to use flat object.

### Implementation steps

- Create a mapping for your index where issue is of type
  `flat_object`:

```
PUT /test-index/
        {
        "mappings": {
        "properties": {
        "issue": {
        "type": "flat_object"
        }
        }
        }
        }
```

## Resources

- [Flat
  object field type](https://opensearch.org/docs/latest/field-types/supported-field-types/flat-object/ "https://opensearch.org/docs/latest/field-types/supported-field-types/flat-object/")
