# Inference options in Amazon SageMaker AI

SageMaker AI provides multiple inference options so that you can pick the option that best
suits your workload:

- [Real-Time Inference](realtime-endpoints.md "realtime-endpoints.md"): _Real-time
  inference_ is ideal for online inferences that have low latency or
  high throughput requirements. Use real-time inference for a persistent and fully
  managed endpoint (REST API) that can handle sustained traffic, backed by the
  instance type of your choice. Real-time inference can support payload sizes up
  to 25 MB and processing times of 60 seconds for regular responses and 8 min for streaming responses.
- [Serverless Inference](serverless-endpoints.md "serverless-endpoints.md"): _Serverless inference_ is ideal when you have
  intermittent or unpredictable traffic patterns. SageMaker AI manages all of the
  underlying infrastructure, so there’s no need to manage instances or scaling
  policies. You pay only for what you use and not for idle time. It can support
  payload sizes up to 4 MB and processing times up to 60 seconds.
- [Batch Transform](batch-transform.md "batch-transform.md"): _Batch transform_
  is suitable for offline processing when large amounts of data are available
  upfront and you don’t need a persistent endpoint. You can also use batch
  transform for pre-processing datasets. It can support large datasets that are
  GBs in size and processing times of days.
- [Asynchronous Inference](async-inference.md "async-inference.md"): _Asynchronous inference_ is
  ideal when you want to queue requests and have large payloads with long
  processing times. Asynchronous Inference can support payloads up to 1 GB and long processing
  times up to one hour. You can also scale down your endpoint to 0 when there are
  no requests to process.
