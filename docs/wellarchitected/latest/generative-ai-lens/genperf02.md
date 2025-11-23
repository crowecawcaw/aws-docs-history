# Maintaining model performance

| GENPERF02: How do you verify your generative AI workload maintains acceptable performance levels? |
| ------------------------------------------------------------------------------------------------- |
|                                                                                                   |

Foundation models are inherently non-deterministic. They introduce an element of randomness into systems. This randomness can be difficult to account for, especially when traditional performance evaluation techniques rely on a determinism. Furthermore, while they are flexible, broadly applicable, and capable performing multiple tasks, foundation models are compute-intensive resources that may require tuning and customization to meet your organization AI requirements.

Developing a methodology for maintaining consistent model performance in a rapidly evolving environment of available models requires well-understood minimum performance thresholds, clear requirements for each model task, and a suite of remediation actions in the case of performance degradation or new model availability.

###### Best practices

- [GENPERF02-BP01 Load test model endpoints](genperf02-bp01.md "genperf02-bp01.md")
- [GENPERF02-BP02 Optimize inference parameters to improve
  response quality](genperf02-bp02.md "genperf02-bp02.md")
- [GENPERF02-BP03 Select and customize the appropriate model for
  your use case](genperf02-bp03.md "genperf02-bp03.md")
