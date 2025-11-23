# Establish performance evaluation processes

| GENPERF01: How do you capture and improve the performance of your generative AI models in production? |
| ----------------------------------------------------------------------------------------------------- |
|                                                                                                       |

Foundation models are built to perform sufficiently well on a wide variety of tasks. Their task-specific performance is tracked using leaderboards and other public metric tracking solutions. Strong performance in one task (for example, summarization) does not indicate strong performance in another task (such as question answering).

Task performance is evaluated using benchmarks built from ground truth data, and model performance against these test suites help when selecting a model for a workload. These new performance metrics expand classic performance considerations such as latency and throughput. Efficient model selection and customization requires careful consideration of the various performance requirements of a generative AI workload, which is informed by the business case.

###### Best practices

- [GENPERF01-BP01 Define a ground truth data set of prompts and
  responses](genperf01-bp01.md "genperf01-bp01.md")
- [GENPERF01-BP02 Collect performance metrics from generative AI
  workloads](genperf01-bp02.md "genperf01-bp02.md")
