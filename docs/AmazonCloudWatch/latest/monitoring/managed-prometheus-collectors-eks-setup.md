

# Integrate Amazon EKS
<a name="managed-prometheus-collectors-eks-setup"></a>

An Amazon CloudWatch managed Prometheus collector scrapes metrics that are Prometheus-compatible. For more information about Prometheus-compatible metrics, see [What are Prometheus-compatible metrics?](https://docs.aws.amazon.com/prometheus/latest/userguide/what-is-prometheus-compatible-metrics.html). Amazon EKS clusters expose metrics for the API server. Amazon EKS clusters that are Kubernetes version 1.28 or above also expose metrics for the kube-scheduler and kube-controller-manager. For more information, see [Fetch control plane raw metrics in Prometheus format](https://docs.aws.amazon.com/eks/latest/userguide/prometheus.html) in the *Amazon EKS User Guide*.

The *Amazon Managed Service for Prometheus User Guide* provides detailed setup instructions. For instructions on configuring Amazon EKS clusters, access entries, and ConfigMap setup, see [Set up managed collectors for Amazon EKS](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html).

**Note**  
The collector enriches each Amazon EKS metric with attributes that identify its origin — the instrumentation scope, the AWS account and Region, an inferred unit, and the cluster name and cluster ARN. You can filter and group on these attributes when you query your metrics with PromQL.

## Create a scraper with CloudWatch destination
<a name="managed-prometheus-collectors-eks-create-scraper"></a>

You can use [GetDefaultScraperConfiguration](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_GetDefaultScraperConfiguration.html) to retrieve a general-purpose scraper configuration, or provide your own.

------
#### [ AWS API ]

Use the `CreateScraper` API operation to create a scraper with a CloudWatch destination. Replace the AWS account, security group, subnet, Amazon EKS cluster, and dataset information with your own values.

```
POST /scrapers HTTP/1.1

{
  "alias": "eks-metrics-scraper",
  "source": {
    "eksConfiguration": {
      "clusterArn": "arn:aws:eks:{{us-west-2}}:{{123456789012}}:cluster/{{my-cluster}}",
      "securityGroupIds": ["{{sg-security-group-id}}"],
      "subnetIds": ["{{subnet-subnet-id-1}}", "{{subnet-subnet-id-2}}"]
    }
  },
  "destination": {
    "cloudWatchConfiguration": {
      "datasetArn": "arn:aws:cloudwatch:{{us-west-2}}:{{123456789012}}:dataset/default"
    }
  },
  "scrapeConfiguration": {
    "configurationBlob": "{{base64-encoded-blob}}"
  }
}
```

------
#### [ AWS CLI ]

Use the `create-scraper` command to create a scraper with a CloudWatch destination. Replace the AWS account, security group, subnet, Amazon EKS cluster, and dataset information with your own values.

```
aws amp create-scraper \
  --alias "eks-metrics-scraper" \
  --source eksConfiguration="{clusterArn='arn:aws:eks:{{us-west-2}}:{{123456789012}}:cluster/{{my-cluster}}', \
    securityGroupIds=['{{sg-security-group-id}}'], \
    subnetIds=['{{subnet-subnet-id-1}}','{{subnet-subnet-id-2}}']}" \
  --scrape-configuration configurationBlob=$(cat {{eks-config.yaml}} | base64 -w 0) \
  --destination cloudWatchConfiguration="{datasetArn='arn:aws:cloudwatch:{{us-west-2}}:{{123456789012}}:dataset/default'}"
```

------

## View the automatic dashboard
<a name="managed-prometheus-collectors-eks-dashboards"></a>

After the collector begins delivering your Amazon EKS metrics to CloudWatch, the CloudWatch console provides an automatic dashboard named **EKS OTel**. To open it, see [EKS OTel](https://console.aws.amazon.com/cloudwatch/home?#dashboards/templates/eks-otel), or sign in to the AWS Management Console, open the CloudWatch console, choose **Dashboards** in the navigation pane, choose **Automatic dashboards**, and then choose **EKS OTel**. You can start monitoring your clusters without building any widgets or dashboards yourself.

If the automatic dashboard meets your needs, you can use it as is. To build a tailored monitoring experience, you can add any of its widgets to a custom dashboard. For more information about custom dashboards, see [Using CloudWatch dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html).

## Cross-account observability
<a name="managed-prometheus-collectors-eks-cross-account"></a>

For cross-account Amazon EKS monitoring, we recommend using Amazon CloudWatch metric centralization. For more information, see [CloudWatch metrics centralization](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html).

For alternative cross-account scraper configurations, see [Cross-account scrapers](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-cross-account.html) in the *Amazon Managed Service for Prometheus User Guide*.