# Connect your Studio

JupyterLab notebooks to EMR Serverless with trusted identity propagation
enabled

Amazon EMR Serverless provides a serverless option for running Apache Spark and Apache
Hive applications without managing clusters. When integrated with trusted identity
propagation, EMR Serverless automatically scales compute resources while maintaining your
identity context for access control and auditing. This approach eliminates the operational
overhead of cluster management while preserving the security benefits of identity-based
access control. The following section provides information on how to connect your trusted
identity propagation enabled Studio with the EMR Serverless.

To connect Studio to Amazon EMR Serverless with trusted identity propagation enabled,
ensure you have completed the following setups:

- [Setting up trusted identity propagation for
  Studio](trustedidentitypropagation-setup.md "trustedidentitypropagation-setup.md")
- [Trusted identity propagation with EMR Serverless](../../../emr/latest/EMR-Serverless-UserGuide/security-iam-service-trusted-prop.md "../../../emr/latest/EMR-Serverless-UserGuide/security-iam-service-trusted-prop.md")
- [Enable communications
  between Studio and EMR Serverless](studio-notebooks-emr-serverless.md "studio-notebooks-emr-serverless.md")

**Connect to the EMR Serverless application**

For a full list of options on how to connect your JupyterLab notebook to
EMR Serverless, see [Connect to an
EMR Serverless application](connect-emr-serverless-application.md "connect-emr-serverless-application.md").
