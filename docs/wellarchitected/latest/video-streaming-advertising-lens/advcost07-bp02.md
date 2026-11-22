

# ADVCOST07-BP02 Replace dedicated forecasting infrastructure with serverless ML-based inventory prediction

 Separate persistent forecasting infrastructure for linear and digital duplicates training compute, model serving endpoints, and data science operational overhead. A single serverless ML forecasting pipeline reduces idle compute costs during off-peak periods. 

 **Desired outcome:** 
+  A single ML forecasting pipeline predicts available inventory across linear, digital, and CTV using serverless inference endpoints. 
+  The need for persistent forecasting compute is removed. Serverless endpoints scale to zero between forecast runs. 
+  Unified models capture cross-system viewership shifts that siloed models miss. 

 **Common anti-patterns:** 
+  Operating separate persistent ML infrastructure for linear TV forecasting (proprietary models against Nielsen panel data) and digital forecasting (real-time impression-based systems), so training compute, model serving endpoints, and data science operational overhead are duplicated for predictions that could share a single pipeline. 
+  Running forecasting inference endpoints around the clock on provisioned compute when predictions are consumed in scheduled batches (daily or weekly planning cycles), which pays for idle capacity between forecast runs rather than using serverless endpoints that scale to zero. 
+  Training linear and digital forecasting models on siloed datasets that can't capture cross-system audience migration (cord-cutting and streaming shifts), so predictions miss viewership trends visible only when linear and digital data are combined. 
+  Maintaining separate data science teams and operational processes for linear and digital forecasting, which duplicates model monitoring, retraining workflows, and incident response for systems that could be unified under a single pipeline with shared governance. 
+  Retraining forecasting models on fixed schedules regardless of whether new viewership data has arrived or audience patterns have shifted, so training compute is wasted on redundant runs while stale predictions still occur when significant changes fall between scheduled retraining windows. 

 **Benefits of establishing this best practice:** 
+  Reduce persistent forecasting compute by using serverless inference (pay per prediction) 
+  Remove duplicate model training pipelines for linear and digital forecasting 
+  Unified models capture cross-system viewership shifts (cord-cutting trends) that siloed models miss 
+  Reduce data science headcount needed to maintain two separate forecasting systems 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Training runs are expensive but infrequent, and inference (generating predictions) happens in scheduled batches aligned to planning cycles. Daily or weekly planning teams consume forecast outputs in bulk, then the system is idle until the next cycle. Persistent infrastructure for this workload pattern means paying around-the-clock compute costs for a system active only during batch windows. 

 Separate forecasting systems for linear and digital compounds wasted spend. Linear models trained on Nielsen panel data and digital models trained on impression logs often run on independent infrastructure with separate model registries, training pipelines, and monitoring. The operational overhead doubles, as you now require two sets of model retraining jobs, two deployment pipelines, or two on-call rotations. 

 Beyond cost, siloed models produce worse predictions. Cross-system audience migration (cord-cutting, streaming adoption shifts) is visible only when linear viewership decline and digital viewership growth are analyzed together. A model trained on both datasets captures these trends. 

 Whether you can release idle capacity depends on who consumes the output and how quickly they need it. Capacity that releases when idle must be re-acquired on the next request, so the first call after a quiet period is slower. That slower first call rules out anything on an auction path. It does not matter here, because a person reads a forecast during a planning cycle. Confirm the latency tolerance before you rely on the saving. Repeat the check before you extend the same pattern to a consumer with tighter latency expectations. 

 The same question applies to retraining. A fixed schedule retrains when the data has not moved and waits when the data has moved sharply. Trigger retraining on the condition that makes it necessary. This avoids both problems and usually detects drift sooner than a calendar would. In exchange, you have a trigger to maintain, and a miscalibrated trigger goes unnoticed because a stale model keeps returning confident forecasts. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Consolidate forecasting training data:** Combine linear viewership data (set-top box, ACR, and panel) with digital impression data in the S3 data lakehouse. Create a unified feature store in SageMaker AI Feature Store for cross-system viewership signals. 

1.  **Deploy serverless inference endpoints:** Replace persistent forecasting compute with SageMaker AI Serverless Inference endpoints. Configure endpoints to scale to zero between prediction runs. Forecasting is typically consumed in scheduled batches (daily planning cycles) rather than continuously. 

1.  **Automate retraining with SageMaker AI Pipelines:** Configure SageMaker AI Pipelines to trigger automated retraining only when new viewership data arrives or model accuracy drops below threshold. This avoids wasteful fixed-schedule retraining when data hasn't changed. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Amazon SageMaker AI Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html) 

 **Related services:** 
+  [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) 
+  [Amazon S3](https://aws.amazon.com/s3/) 