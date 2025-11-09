# Amazon Q Business index metrics

The following table shows the [Index](concepts-terms.md#index "concepts-terms.md#index") metrics that
Amazon Q Business sends to CloudWatch in real time.

| Metric name                      | Unit  | Description                                                                                                                                               |
| -------------------------------- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DocumentCount`                  | Count | The number of documents. This metric is published every 15 minutes.<br>Valid dimensions: `ApplicationId`, `IndexId`                                       |
| `DocumentsIndexed`               | Count | The number of documents that were indexed.<br>Valid dimensions: `ApplicationId`, `IndexId`,<br>`DataSourceId`                                             |
| `DocumentsFailedToIndex`         | Count | The number of documents that failed to index.<br>Valid dimensions: `ApplicationId`, `IndexId`,<br>`DataSourceId`                                          |
| `DocumentsFailedToIndexDueToCDE` | Count | The number of documents that failed to index because of custom document<br>enrichment.<br>Valid dimensions: `ApplicationId`, `IndexId`,<br>`DataSourceId` |
| `ExtractedTextSize`              | MB    | Size of the extracted text<br>Valid dimensions: `ApplicationId`, `IndexId`                                                                                |
| `MonthlyDataSyncDuration`        | Count | Duration of data synchronization operations over a monthly period.<br>Valid dimensions: `ApplicationId`, `IndexId`,<br>`DataSourceId`                     |
