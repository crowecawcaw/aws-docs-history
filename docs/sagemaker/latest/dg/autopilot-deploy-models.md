# Autopilot model deployment and prediction

This Amazon SageMaker Autopilot guide includes steps for model deployment, setting up real-time inference, and
running inference with batch jobs.

After you train your Autopilot models, you can deploy them to get predictions in one of
two ways:

1. Use [Deploy models for real-time inference](autopilot-deploy-models-realtime.md "autopilot-deploy-models-realtime.md") to set up an endpoint and obtain
   predictions interactively. Real-time inference is ideal for inference workloads where you
   have real-time, interactive, low latency requirements.
2. Use [Run batch inference jobs](autopilot-deploy-models-batch.md "autopilot-deploy-models-batch.md") to make predictions in parallel on
   batches of observations on an entire dataset. Batch inference is a good option for large
   datasets or if you don't need an immediate response to a model prediction request.

###### Note

To avoid incurring unnecessary charges: After the endpoints and resources that were
created from model deployment are no longer needed, you can delete them. For information about
pricing of instances by Region, see [Amazon SageMaker Pricing](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/").
