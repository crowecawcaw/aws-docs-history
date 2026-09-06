

# Connect your Studio JupyterLab notebooks to EMR Serverless with trusted identity propagation enabled
<a name="trustedidentitypropagation-emr-serverless"></a>

Amazon EMR Serverless provides a serverless option for running Apache Spark and Apache Hive applications without managing clusters. When integrated with trusted identity propagation, EMR Serverless automatically scales compute resources while maintaining your identity context for access control and auditing. This approach eliminates the operational overhead of cluster management while preserving the security benefits of identity-based access control. The following section provides information on how to connect your trusted identity propagation enabled Studio with the EMR Serverless.

To connect Studio to Amazon EMR Serverless with trusted identity propagation enabled, ensure you have completed the following setups:
+  [Setting up trusted identity propagation for Studio](trustedidentitypropagation-setup.md) 
+  [Trusted identity propagation with EMR Serverless](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/security-iam-service-trusted-prop.html) 
+  [Enable communications between Studio and EMR Serverless](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-notebooks-emr-serverless.html) 

 **Connect to the EMR Serverless application** 

For a full list of options on how to connect your JupyterLab notebook to EMR Serverless, see [Connect to an EMR Serverless application](https://docs.aws.amazon.com/sagemaker/latest/dg/connect-emr-serverless-application.html).