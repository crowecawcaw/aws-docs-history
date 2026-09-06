

# Requirements for monitoring and incident management for Amazon EKS in AMS Accelerate
<a name="acc-requirements"></a>

These are the supported and/or required resources for monitoring and incident management for Amazon EKS for AMS Accelerate
+ **Supported Kubernetes versions:** See [Amazon EKS Kubernetes versions](https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html) in the **Amazon EKS User Guide**.
+ **Node types:** Amazon EKS managed nodes are supported. Windows nodes and containers aren't supported.
+ **Kubernetes cluster access:** AMS requires system:masters RBAC cluster role and cluster user.
+ **SSM Agent on Amazon EC2 nodes:** Both Bottle Rocket and Amazon EKS AMIs have SSM Agent pre-installed. Be sure that SSM Agent is installed on your custom AMIs and Amazon EC2 nodes.
+ **Service Quotas** For more information, see the service quotas for [Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP_quotas.html) and [Amazon Managed Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/AMG_quotas.html).
+ **Supported AWS Regions:**    
<a name="available-regions-table"></a>[See the AWS documentation website for more details](http://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-requirements.html)
**Note**  
Metrics for Amazon EKS clusters in af-south-1, Africa (Cape Town) and ap-east-1, Asia Pacific (Hong Kong) are exported to the AMS monitoring service in the same AWS Region, respectively. Metrics for these AWS Regions are then transported within the AMS monitoring service to different Regions where they are processed and stored. See the preceding table for Regions that the AMS monitoring service uses to store metrics.