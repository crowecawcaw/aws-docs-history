# Requirements for monitoring and incident management for Amazon EKS in AMS Accelerate

These are the supported and/or required resources for monitoring and incident management for Amazon EKS for AMS Accelerate

- **Supported Kubernetes versions:** See [Amazon EKS Kubernetes versions](../../../eks/latest/userguide/kubernetes-versions.md "../../../eks/latest/userguide/kubernetes-versions.md") in the **Amazon EKS User Guide**.
- **Node types:** Amazon EKS managed nodes are supported. Windows nodes and containers aren't supported.
- **Kubernetes cluster access:** AMS requires system:masters RBAC cluster role and cluster user.
- **SSM Agent on Amazon EC2 nodes:**
  Both Bottle Rocket and Amazon EKS AMIs have SSM Agent pre-installed. Be sure that SSM Agent is installed on your custom AMIs and Amazon EC2 nodes.
- **Service Quotas**
  For more information, see the service quotas for [Amazon Managed Service for Prometheus](../../../prometheus/latest/userguide/AMP_quotas.md "../../../prometheus/latest/userguide/AMP_quotas.md") and [Amazon Managed Grafana](../../../grafana/latest/userguide/AMG_quotas.md "../../../grafana/latest/userguide/AMG_quotas.md").
- **Supported AWS Regions:**

| Region name              | Region         | Metrics storage region           |
| ------------------------ | -------------- | -------------------------------- |
| US East (Ohio)           | us-east-2      | us-east-2                        |
| US East (N. Virginia)    | us-east-1      | us-east-1                        |
| US West (Oregon)         | us-west-2      | us-west-2                        |
| Asia Pacific (Tokyo)     | ap-northeast-1 | ap-northeast-1                   |
| Asia Pacific (Seoul)     | ap-northeast-2 | ap-northeast-2                   |
| Asia Pacific (Singapore) | ap-southeast-1 | ap-southeast-1                   |
| Asia Pacific (Sydney)    | ap-southeast-2 | ap-southeast-2                   |
| Europe (Frankfurt)       | eu-central-1   | eu-central-1                     |
| Europe (Ireland)         | eu-west-1      | eu-west-1                        |
| Europe (London)          | eu-west-2      | eu-west-2                        |
| Africa (Cape Town)       | af-south-1     | eu-west-1<br>eu-west-2           |
| Asia Pacific (Hong Kong) | ap-east-1      | ap-northeast-1<br>ap-northeast-2 |

###### Note

Metrics for Amazon EKS clusters in af-south-1, Africa (Cape Town) and ap-east-1, Asia Pacific (Hong Kong) are exported to the AMS monitoring service in the
same AWS Region, respectively. Metrics for these AWS Regions are then transported within the AMS monitoring service to different Regions where they are processed
and stored. See the preceding table for Regions that the AMS monitoring service uses to store metrics.
