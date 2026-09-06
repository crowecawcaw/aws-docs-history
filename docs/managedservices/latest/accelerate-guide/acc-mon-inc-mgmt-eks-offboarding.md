

# Offboard from Monitoring and Incident Management for Amazon EKS in AMS Accelerate
<a name="acc-mon-inc-mgmt-eks-offboarding"></a>

Notify your cloud service delivery manager (CSDM) with account IDs and cluster names to start the offboarding process. After you offboard, alert processing, metric storage, and metric querying are suspended and metrics are deleted in accordance with the default [ Amazon Managed Service for Prometheus data retention policies](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP_quotas.html).

AMS performs the following offboarding steps:



1. AMS disables alerts that are sent to you and AMS Operations.

1. AMS removes the Prometheus instance from your Amazon EKS cluster.

1. AMS removes other AWS resources that are installed in your account, such as IAM roles and AWS Config rules.

After these steps are completed, you must complete the following offboarding steps: 

1. Use `eksctl` to remove the Kubernetes RBAC permissions from the `aws-auth` `ConfigMap`. 

1. If you previously installed it, remove the Amazon Managed Grafana instance that you configured to connect to AMS.