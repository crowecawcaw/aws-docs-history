# Using an Amazon EMR on EKS virtual cluster in Amazon SageMaker Unified Studio

After creating your Amazon EMR on EKS virtual cluster, you can begin using your compute.

###### Note

Amazon EMR on EKS in Amazon SageMaker Unified Studio is only available for SageMaker distributions >=2.10 and >=3.5.

1. From inside the project management view, select **Compute** from the navigation bar.
2. In the Compute panel, select the **Data processing** tab.
3. In the data processing panel, select your target Amazon EMR on EKS virtual cluster.
4. In the compute details panel, select **Actions** and **Open JupyterLab IDE**.
5. In the JupyterLab IDE, select a compatible **Connection type**
   and select the name of the **Compute**.

## Configuration for additional functionality in Amazon SageMaker Unified Studio

Some native Amazon EMR on EKS functionality requires additional configuration by your administrator
for your Amazon SageMaker Unified Studio projects. Contact your administrator to review documentation for additional functionality.

- [Configuring monitoring with Spark History Server for Amazon EMR on EKS](../adminguide/configuring-monitoring-with-spark-history-server-for-emr-on-eks.md "../adminguide/configuring-monitoring-with-spark-history-server-for-emr-on-eks.md")
- [Configuring fine-grained access controls for Amazon EMR on EKS](../adminguide/configuring-fine-grained-access-controls-for-emr-on-eks.md "../adminguide/configuring-fine-grained-access-controls-for-emr-on-eks.md")
- [Configuring trusted identity propagation for Amazon EMR on EKS](../adminguide/configuring-trusted-identity-propagation-for-emr-on-eks.md "../adminguide/configuring-trusted-identity-propagation-for-emr-on-eks.md")
- [Configuring user background sessions for Amazon EMR on EKS](../adminguide/configuring-user-background-sessions-for-emr-on-eks.md "../adminguide/configuring-user-background-sessions-for-emr-on-eks.md")
