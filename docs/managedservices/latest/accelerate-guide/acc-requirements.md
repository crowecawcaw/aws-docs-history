

# Requirements for monitoring and incident management for Amazon EKS in AMS Accelerate
<a name="acc-requirements"></a>

These are the supported and/or required resources for monitoring and incident management for Amazon EKS for AMS Accelerate
+ **Supported Kubernetes versions:** See [Amazon EKS Kubernetes versions](https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html) in the **Amazon EKS User Guide**.
+ **Node types:** Amazon EKS managed nodes are supported. Windows nodes and containers aren't supported.
+ **Kubernetes cluster access:** AMS requires system:masters RBAC cluster role and cluster user.
+ **SSM Agent on Amazon EC2 nodes:** Both Bottle Rocket and Amazon EKS AMIs have SSM Agent pre-installed. Be sure that SSM Agent is installed on your custom AMIs and Amazon EC2 nodes.
+ **Service Quotas** For more information, see the service quotas for [Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP_quotas.html) and [Amazon Managed Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/AMG_quotas.html).
+ **Supported AWS Regions:**

<a name="available-regions-table"></a>
<table>
<thead>
  <tr><th>Region name</th><th>Region</th><th>Metrics storage region</th></tr>
</thead>
<tbody>
  <tr><td>US East (Ohio)</td><td>us-east-2</td><td>us-east-2</td></tr>
  <tr><td>US East (N. Virginia)</td><td>us-east-1</td><td>us-east-1</td></tr>
  <tr><td>US West (Oregon)</td><td>us-west-2</td><td>us-west-2</td></tr>
  <tr><td>Asia Pacific (Tokyo)</td><td>ap-northeast-1</td><td>ap-northeast-1</td></tr>
  <tr><td>Asia Pacific (Seoul)</td><td>ap-northeast-2</td><td>ap-northeast-2</td></tr>
  <tr><td>Asia Pacific (Singapore)</td><td>ap-southeast-1</td><td>ap-southeast-1</td></tr>
  <tr><td>Asia Pacific (Sydney)</td><td>ap-southeast-2</td><td>ap-southeast-2</td></tr>
  <tr><td>Europe (Frankfurt)</td><td>eu-central-1</td><td>eu-central-1</td></tr>
  <tr><td>Europe (Ireland)</td><td>eu-west-1</td><td>eu-west-1</td></tr>
  <tr><td>Europe (London)</td><td>eu-west-2</td><td>eu-west-2</td></tr>
  <tr><td>Africa (Cape Town)</td><td>af-south-1</td><td>eu-west-1<br />eu-west-2</td></tr>
  <tr><td>Asia Pacific (Hong Kong)</td><td>ap-east-1</td><td>ap-northeast-1<br />ap-northeast-2</td></tr>
</tbody>
</table>

**Note**  
Metrics for Amazon EKS clusters in af-south-1, Africa (Cape Town) and ap-east-1, Asia Pacific (Hong Kong) are exported to the AMS monitoring service in the same AWS Region, respectively. Metrics for these AWS Regions are then transported within the AMS monitoring service to different Regions where they are processed and stored. See the preceding table for Regions that the AMS monitoring service uses to store metrics.