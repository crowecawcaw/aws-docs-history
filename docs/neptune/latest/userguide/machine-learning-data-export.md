# Using the neptune-export

tool or Neptune-Export service to export data from Neptune for Neptune ML

Neptune ML requires that you provide training data for the [Deep Graph Library (DGL)](https://www.dgl.ai/ "https://www.dgl.ai/") to create and evaluate
models.

You can export data from Neptune using either the [Neptune-Export service](export-service.md "export-service.md"), or [neptune-export utility](export-utility.md "export-utility.md"). Both the
service and the command line tool publish data to Amazon Simple Storage Service (Amazon S3) in a CSV format,
encrypted using Amazon S3 server-side encryption (`SSE-S3`).
See [Files exported by Neptune-Export
and neptune-export](exported-files.md "exported-files.md").

In addition, when you configure an export of training data for Neptune ML
the export job creates and publishes an encrypted model-training configuration
file along with the exported data. By default, this file is named
`training-data-configuration.json`.
