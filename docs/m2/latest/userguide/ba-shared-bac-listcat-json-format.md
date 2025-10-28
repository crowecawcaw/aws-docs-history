AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see
[AWS Mainframe Modernization availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# LISTCAT JSON format

The LISTCAT JSON format is defined by the following attributes:

- optional "catalogId": identifier of the legacy catalog as a String, or "default" for the
  default catalog.
- "identifier": the data set name, as a String.
- "isIndexed": a boolean flag to indicate KSDS: true for KSDS, false otherwise.
- "isLinear": a boolean flag to indicate ESDS: true for ESDS, false otherwise.
- "isRelative": a boolean flag to indicate RRDS: true for RRDS, false otherwise
- **Note**: "isIndexed", "isLinear", and "isRelative" are
  mutually exclusive.
- "isFixedLengthRecord": a boolean flag: set to true if fixed length records data set, false
  otherwise.
- "avgRecordSize": Average record size in bytes, expressed as a positive integer.
- "maxRecordSize": Maximal Record size in bytes, expressed as an integer. Should be equal to
  avgRecordSize for fixed length record size.
- for KSDS only: Mandatory primary Key definition (as nested object)
  - labelled "primaryKey"
  - "offset": 0-based bytes offset for the primary key in the record.
  - "length": length in bytes of the primary key.
  - "unique": must be set to true for primary key.

- for KSDS/ESDS, collection of alternate keys (as collection of nested objects):
  - labelled "alternateKeys"
  - For each alternate key:
    - "offset": 0-based bytes offset for the alternate key in the record.
    - "length": length in bytes of the alternate key.
    - "unique": must be set to true for alternate key, if the key does not accept duplicate
      entries, false otherwise.

- if no alternate keys are present, provide an empty collection:

```
alternateKeys: []
```

The following is a sample KSDS LISTCAT JSON file.

```
{
  "catalogId": "default",
  "identifier": "AWS_M2_CARDDEMO_CARDXREF_VSAM_KSDS",
  "isIndexed": true,
  "isLinear": false,
  "isRelative": false,
  "isFixedLengthRecord": true,
  "avgRecordSize": 50,
  "maxRecordSize": 50,
  "primaryKey": {
    "offset": 0,
    "length": 16,
    "unique": true
  },
  "alternateKeys": [
    {
      "offset": 25,
      "length": 11,
      "unique": false
    }
  ]
}
```
