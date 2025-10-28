# Connect Studio JupyterLab

notebooks to Amazon EMR with trusted identity propagation enabled

Connecting Amazon SageMaker Studio JupyterLab notebooks to Amazon EMR clusters enables you
to leverage the distributed computing power of Amazon EMR for large-scale data processing and
analytics workloads. With trusted identity propagation enabled, your identity context is
propagated to Amazon EMR, allowing for fine-grained access control and comprehensive audit
trails. The following page provides instructions on how to connect your Studio notebook
to Amazon EMR clusters. Once set up, you can use the `Connect to Cluster` option in
your Studio notebook.

To connect Studio to Amazon EMR with trusted identity propagation enabled, ensure
you have completed the following setups:

- [Setting up trusted identity propagation for
  Studio](trustedidentitypropagation-setup.md "trustedidentitypropagation-setup.md")
- [Getting
  started with AWS IAM Identity Center integration for Amazon EMR](../../../emr/latest/ManagementGuide/emr-idc-start.md "../../../emr/latest/ManagementGuide/emr-idc-start.md")
- [Enable communications between Studio and Amazon EMR clusters](studio-notebooks-emr-cluster.md "studio-notebooks-emr-cluster.md")

**Connect to the Amazon EMR cluster**

For a full list of options on how to connect your JupyterLab notebook to Amazon EMR, see
[Connect to
an Amazon EMR cluster](connect-emr-clusters.md "connect-emr-clusters.md").
