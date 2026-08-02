# Template variables

Variables use the `!{name}` syntax. The supported variables are:

| Variable             | Description                                         |
| -------------------- | --------------------------------------------------- |
| `!{channel-id}`      | The Channel ID.                                     |
| `!{topic-name}`      | The source Kafka topic name.                        |
| `!{partition-id}`    | The source Kafka partition ID.                      |
| `!{kafka-offset}`    | The Kafka offset of the first record in the object. |
| `!{sequence-number}` | A monotonic per-object (batch) sequence number.     |
| `!{yyyy}`            | Year (4-digit).                                     |
| `!{YY}`              | Year (2-digit).                                     |
| `!{MM}`              | Month.                                              |
| `!{dd}`              | Day.                                                |
| `!{HH}`              | Hour (24-hour).                                     |
| `!{mm}`              | Minute.                                             |
