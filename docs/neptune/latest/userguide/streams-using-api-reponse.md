# Neptune Streams API Response Format

A response to a Neptune Streams REST API request has the following fields:

- `lastEventId`   –  
  Sequence identifier of the last change in
  the stream response. An event ID is composed of two fields: A `commitNum`
  identifies a transaction that changed the graph, and an `opNum` identifies a
  specific operation within that transaction. This is shown in the following example.

```
  "eventId": {
    "commitNum": 12,
    "opNum": 1
  }
```

- `lastTrxTimestamp`   –  
  The time at which the commit for the transaction was requested, in milliseconds
  from the Unix epoch.
- `format`   –  
  Serialization format for the change records being returned. The possible values are
  `PG_JSON` for Gremlin or openCypher change records, and `NQUADS` for
  SPARQL change records.
- `records`   –  
  An array of serialized change-log stream records included in the response.
  Each record in the `records` array contains these fields:
  - `commitTimestamp`   –  
    The time at which the commit for the transaction was requested,
    in milliseconds from the Unix epoch.
  - `eventId`   –  
    The sequence identifier of the stream change record.
  - `data`   –  
    The serialized Gremlin, SPARQL, or OpenCypher change record.
    The serialization formats of each record are described in more
    detail in the next section, [Serialization Formats in Neptune Streams](streams-change-formats.md "streams-change-formats.md").
  - `op`   –  
    The operation that created the change.
  - `isLastOp`   –  
    Only present if this operation is the last one in its transaction.
    When present, it is set to `true`. Useful for ensuring that
    an entire transaction is consumed.

- `totalRecords`   –  
  The total number of records in the response.
  For example, the following response returns Gremlin change data,
  for a transaction that contains more than one operation:

```
{
  "lastEventId": {
    "commitNum": 12,
    "opNum": 1
  },
  "lastTrxTimestamp": 1560011610678,
  "format": "PG_JSON",
  "records": [
    {
      "commitTimestamp": 1560011610678,
      "eventId": {
        "commitNum": 1,
        "opNum": 1
      },
      "data": {
        "id": "d2b59bf8-0d0f-218b-f68b-2aa7b0b1904a",
        "type": "vl",
        "key": "label",
        "value": {
          "value": "vertex",
          "dataType": "String"
        }
      },
      "op": "ADD"
    }
  ],
  "totalRecords": 1
}
```

The following response returns SPARQL change data for the last operation in
a transaction (the operation identified by `EventId(97, 1)` in transaction
number 97).

```
{
  "lastEventId": {
    "commitNum": 97,
    "opNum": 1
  },
  "lastTrxTimestamp": 1561489355102,
  "format": "NQUADS",
  "records": [
    {
      "commitTimestamp": 1561489355102,
      "eventId": {
        "commitNum": 97,
        "opNum": 1
      },
      "data": {
        "stmt": "<https://test.com/s> <https://test.com/p> <https://test.com/o> .\n"
      },
      "op": "ADD",
      "isLastOp": true
    }
  ],
  "totalRecords": 1
}
```
