

# Deploy a model in Studio
<a name="jumpstart-foundation-models-use-studio-updated-deploy"></a>

To deploy JumpStart foundation models, navigate to a model detail card in the Studio UI. For more information on how to open JumpStart in Studio, see [Open JumpStart in Studio](studio-jumpstart.md#jumpstart-open-studio). After navigating to the model detail page of your choice, choose **Deploy** in the upper right corner of the Studio UI. Then, follow the steps in [Deploy models with SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints-deploy-models.html#deploy-models-studio).

Amazon SageMaker JumpStart also offers optimized deployments, which provide pre-defined deployment configurations designed for specific use cases such as content generation, summarization, or chat-style interactions. When deploying a supported model, you can select your target use case and choose a constraint optimization — Cost optimized, Throughput optimized, Latency optimized, or Balanced — and Amazon SageMaker JumpStart automatically configures the endpoint for that scenario. This gives you visibility into key performance metrics like P50 latency, time-to-first-token (TTFT), and throughput, while ensuring the deployment is tuned for your workload. To get started, open a supported model's detail page in Studio, choose **Deploy**, and use the **Performance** panel to configure your optimized deployment.

**Important**  
Some foundation models require explicit acceptance of an end-user license agreement (EULA) before deployment. For more information, see [EULA acceptance in Amazon SageMaker Studio](jumpstart-foundation-models-choose.md#jumpstart-foundation-models-choose-eula-studio).