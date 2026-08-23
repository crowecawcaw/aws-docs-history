# Amazon CloudWatch metrics

| Metric name                            | Description                                                                       | Unit    |
| -------------------------------------- | --------------------------------------------------------------------------------- | ------- |
| `DeliveryToIceberg.DataFreshness`      | Age of the oldest record delivered; rising values indicate delivery lag or stall. | Seconds |
| `DeliveryToIceberg.BytesIn`            | Volume read into the delivery path.                                               | Bytes   |
| `DeliveryToIceberg.BytesProcessed`     | Volume processed.                                                                 | Bytes   |
| `DeliveryToIceberg.BytesOut`           | Volume written to the destination.                                                | Bytes   |
| `DeliveryToIceberg.TotalRowCount`      | Total rows seen.                                                                  | Count   |
| `DeliveryToIceberg.SuccessfulRowCount` | Rows delivered successfully.                                                      | Count   |
| `DeliveryToIceberg.FailedRowCount`     | Rows that failed delivery; non-zero is the key error signal.                      | Count   |
| `DeliveryToIceberg.CommitSuccess`      | Successful Iceberg commits.                                                       | Count   |
| `DeliveryToIceberg.DLQDeliverySuccess` | Records successfully routed to the dead-letter queue.                             | Count   |
