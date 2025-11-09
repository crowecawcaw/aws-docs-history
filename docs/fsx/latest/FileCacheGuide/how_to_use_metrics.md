# How to use Amazon File Cache metrics

The metrics reported by Amazon File Cache provide information that you can analyze in
different ways. The following list shows some common uses for the metrics. These are
suggestions to get you started, not a comprehensive list.

| How Do I Determine...  | Relevant Metrics                                                                                       |
| ---------------------- | ------------------------------------------------------------------------------------------------------ |
| My cache's throughput? | SUM(DataReadBytes + DataWriteBytes)/Period (in seconds)                                                |
| My cache's IOPS?       | Total IOPS = SUM(DataReadOperations + DataWriteOperations + MetadataOperations)/Period (in<br>seconds) |
