# ML lifecycle phase – Monitoring

The model monitoring system must capture data, compare that data
to the training set, define rules to detect issues, and send
alerts. This process repeats on a defined schedule, when initiated
by an event, or when initiated by human intervention. The issues
detected in the monitoring phase include: data quality, model
quality, bias drift, and feature attribution drift. 

![Figure 18 includes the key components of monitor phase. These components include: model explainability, detect drift, model update pipeline.](images/key-components-monitor-phase.png)

_Figure 18: Post deployment monitoring - main
components_

Figure 18 lists key components of monitoring, including:

- **Model explainability** -
  Monitoring system uses _explainability_ to
  evaluate the soundness of the model and if the predictions can
  be trusted.
- **Detect drift** - Monitoring
  system detects data and concept drifts, initiates an alert,
  and sends it to the alarm manager system. Data drift is
  significant changes to the data distribution compared to the
  data used for training. Concept drift is when the properties
  of the target variables change. Any kind of drift results in
  model performance degradation.
- **Model update pipeline** - If
  the alarm manager identifies any violations, it launches the
  model update pipeline for a re-train. This can be seen in
  Figure 19. The _Data prepare_,
  _CI/CD/CT_, and
  _Feature_ pipelines will also be active
  during this process.

![Figure 19 includes pipelines including online and offline feature pipeline, CI/CD/CT pipeline, Data prepare pipeline, real-time inference pipeline, and model update retrain pipeline. The pipelines are overlaid on the top of ML lifecycle architecture diagram](images/ml-lifecycle-model-update-inference-pipelines.png)

_Figure 19: ML lifecycle with model update re-train and
batch/real-time inference pipelines_

###### Best practices

- [Operational excellence pillar – Best practices](operational-excellence-pillar-best-practices-5.md "operational-excellence-pillar-best-practices-5.md")
- [Security pillar – Best practices](security-pillar-best-practices-5.md "security-pillar-best-practices-5.md")
- [Reliability pillar – Best practices](reliability-pillar-best-practices-5.md "reliability-pillar-best-practices-5.md")
- [Performance efficiency pillar – Best practices](performance-efficiency-pillar-best-practices-5.md "performance-efficiency-pillar-best-practices-5.md")
- [Cost optimization pillar – Best practices](cost-optimization-pillar-best-practices-5.md "cost-optimization-pillar-best-practices-5.md")
- [Sustainability pillar – Best practices](sustainability-pillar-best-practices-5.md "sustainability-pillar-best-practices-5.md")
