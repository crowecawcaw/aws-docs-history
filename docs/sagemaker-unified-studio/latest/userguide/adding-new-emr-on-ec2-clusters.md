# Adding a new Amazon EMR on EC2 cluster in Amazon SageMaker Unified Studio

As a data worker, you can make use of Amazon EMR on EC2 by adding existing or new Amazon EMR on EC2
clusters as compute instances to a project in the Amazon SageMaker Unified Studio Studio. Within a project, you can
use both existing and new Amazon EMR on EC2 clusters.

Before you can create a new Amazon EMR on EC2 cluster, your admin must enable blueprints.
On-demand creation isn't supported for Amazon EMR on EC2 in quick setup.

After your Admin has enabled blueprints:

1. From inside the project management view, select **Compute** from the
   navigation bar.
2. In the Compute panel, select the **Data processing** tab.
3. To create a new Amazon EMR on EC2 cluster, select the **Add compute**
   dropdown menu and then choose **New compute**.
4. In the **Add compute** modal, you can select the type of compute you
   would like to add to your project. Select **Create new compute
   resources**.
5. Select **Amazon EMR on EC2 cluster**.
6. The **Add compute** dialog box allows you to specify the name of the
   Amazon EMR on EC2 cluster, provide a description, and choose a release of EMR (such as EMR 7.5)
   that you want to install on your cluster.
7. After configuring these settings, select **Add compute**. After some
   time, your Amazon EMR on EC2 cluster will be added to your project.
