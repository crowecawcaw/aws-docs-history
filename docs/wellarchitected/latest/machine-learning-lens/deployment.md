# Deployment

After you have trained, tuned, and evaluated your model, you can deploy it into production
and make predictions against this deployed model. Amazon SageMaker AI Studio can convert notebook code
to production-ready jobs without the need to manage the underlying infrastructure. Be sure to
use a governance process. Controlling deployments through automation combined with manual or
automated quality gates facilitates that changes can be effectively validated with dependent
systems prior to deployment to production. 

![Deployment architecture diagram](images/deployment-architecture-diagram.png)
_Figure 14: Deployment architecture diagram_

Figure 14 illustrates the deployment phase of the ML lifecycle in production. An
application sends request payloads to a production endpoint to make inference against the model.
Model artifacts are fetched from the model registry, features are retrieved from the feature
store, and the inference code container is obtained from the container repository. 

![Deployment main components](images/deployment-main-components.png)
_Figure 15: Deployment main components_

Figure 15 lists key components of production deployment including:

- **Blue/green, canary, A/B, shadow deployment/testing:**
  Deployment and testing strategies that reduce downtime and risks when releasing a new or
  updated version.
- The _blue/green_ deployment technique provides two identical
  production environments (initially _blue_ is the existing infrastructure
  and _green_ is an identical infrastructure for testing). Once testing is
  done on the _green_ environment, live application traffic is directed to
  it from the _blue_ environment. Then the roles of the blue/green
  environments are switched.
- With a _canary_ deployment, a new release is deployed to a small
  group of users while other users continue to use the previous version. Once you're satisfied
  with the new release, you can gradually roll it out to the users.
- _A/B_ testing strategy enables deploying changes to a model. Direct a
  defined portion of traffic to the new model. Direct the remaining traffic to the old model.
  A/B testing is similar to canary testing, but has larger user groups and a longer time
  scale, typically days or even weeks.
- With a _shadow_ deployment strategy, the new version is available
  alongside the old version. The input data is run through both versions. The older version is
  used for servicing the production application and the new one is used for testing and
  analysis.
- **Inference pipeline:** Figure 16 shows the inference pipeline
  that automates capturing of the prepared data, performing predictions and post-processing
  for real-time or batch inferences.
- **Scheduler pipeline:** Deployed model is representative of the
  latest data patterns. When configured as shown in Figure 16, re-training at intervals can
  minimize the risk of data and concept drifts. A scheduler can initiate a re-training at
  business defined intervals. Data preparation, CI/CD/CT, and feature pipelines will also be
  active during this process.

![ML lifecycle with scheduler retrain and batch or real-time inference pipelines](images/ml-lifecycle-scheduler-inference-pipelines.png)
_Figure 16: ML lifecycle with scheduler retrain and batch or real-time inference pipelines_
