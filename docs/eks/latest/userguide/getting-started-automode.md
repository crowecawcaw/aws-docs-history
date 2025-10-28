**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Get started with Amazon EKS – EKS Auto Mode

Like other EKS getting started experiences, creating your first cluster with EKS Auto Mode delegates the management of the cluster itself to AWS.
However, EKS Auto Mode extends EKS automation by handing responsibility of many essential services needed to set up workload infrastructure (nodes, networks, and various services), making it easier to manage nodes and scale up to meet workload demands.

Choose from one of the following ways to create a cluster with EKS Auto Mode:

- [Create an EKS Auto Mode Cluster with the AWS CLI](automode-get-started-cli.md "automode-get-started-cli.md"): Use the `aws` command line interface to create a cluster.
- [Create an EKS Auto Mode Cluster with the AWS Management Console](automode-get-started-console.md "automode-get-started-console.md"): Use the AWS Management Console to create a cluster.
- [Create an EKS Auto Mode Cluster with the eksctl CLI](automode-get-started-eksctl.md "automode-get-started-eksctl.md"): Use the `eksctl` command line interface to create a cluster.
  If you are comparing different approaches to creating your first EKS cluster,
  you should know that EKS Auto Mode has AWS take over additional cluster management responsibilities
  that include setting up components to:

- Start up and scale nodes as workload demand increases and decreases.
- Regularly upgrade the cluster itself (control plane), node operating systems, and services running on nodes.
- Choose default settings that determine things like the size and speed of node storage and Pod network configuration.
  For details on what you get with EKS Auto Mode clusters, see [Automate cluster infrastructure with EKS Auto Mode](automode.md "automode.md").
