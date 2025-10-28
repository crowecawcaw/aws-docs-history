**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Monitor your cluster metrics with Prometheus

[Prometheus](https://prometheus.io/ "https://prometheus.io/") is a monitoring and time series database that scrapes endpoints. It provides the ability to query, aggregate, and store collected data. You can also use it for alerting and alert aggregation. This topic explains how to set up Prometheus as either a managed or open source option. Monitoring Amazon EKS control plane metrics is a common use case.

Amazon Managed Service for Prometheus is a Prometheus-compatible monitoring and alerting service that makes it easy to monitor containerized applications and infrastructure at scale. It is a fully-managed service that automatically scales the ingestion, storage, querying, and alerting of your metrics. It also integrates with AWS security services to enable fast and secure access to your data. You can use the open-source PromQL query language to query your metrics and alert on them. Also, you can use alert manager in Amazon Managed Service for Prometheus to set up alerting rules for critical alerts. You can then send these critical alerts as notifications to an Amazon SNS topic.

There are several different options for using Prometheus with Amazon EKS:

- You can turn on Prometheus metrics when first creating an Amazon EKS cluster or you can create your own Prometheus scraper for existing clusters. Both of these options are covered by this topic.
- You can deploy Prometheus using Helm. For more information, see [Deploy Prometheus using Helm](deploy-prometheus.md "deploy-prometheus.md").
- You can view control plane raw metrics in Prometheus format. For more information, see [Fetch control plane raw metrics in Prometheus format](view-raw-metrics.md "view-raw-metrics.md").

## Step 1: Turn on Prometheus metrics

###### Important

Amazon Managed Service for Prometheus resources are outside of the cluster lifecycle and need to be maintained independent of the cluster. When you delete your cluster, make sure to also delete any applicable scrapers to stop applicable costs. For more information, see [Find and delete scrapers](../../../prometheus/latest/userguide/AMP-collector-how-to.md#AMP-collector-list-delete "../../../prometheus/latest/userguide/AMP-collector-how-to.md#AMP-collector-list-delete") in the _Amazon Managed Service for Prometheus User Guide_.

Prometheus discovers and collects metrics from your cluster through a pull-based model called scraping. Scrapers are set up to gather data from your cluster infrastructure and containerized applications. When you turn on the option to send Prometheus metrics, Amazon Managed Service for Prometheus provides a fully managed agentless scraper.

If you haven’t created the cluster yet, you can turn on the option to send metrics to Prometheus when first creating the cluster. In the Amazon EKS console, this option is in the **Configure observability** step of creating a new cluster. For more information, see [Create an Amazon EKS cluster](create-cluster.md "create-cluster.md").

If you already have an existing cluster, you can create your own Prometheus scraper. To do this in the Amazon EKS console, navigate to your cluster’s **Observability** tab and choose the **Add scraper** button. If you would rather do so with the AWS API or AWS CLI, see [Create a scraper](../../../prometheus/latest/userguide/AMP-collector-how-to.md#AMP-collector-create "../../../prometheus/latest/userguide/AMP-collector-how-to.md#AMP-collector-create") in the _Amazon Managed Service for Prometheus User Guide_.

The following options are available when creating the scraper with the Amazon EKS console.

**Scraper alias**

(Optional) Enter a unique alias for the scraper.

**Destination**

Choose an Amazon Managed Service for Prometheus workspace. A workspace is a logical space dedicated to the storage and querying of Prometheus metrics. With this workspace, you will be able to view Prometheus metrics across the accounts that have access to it. The **Create new workspace** option tells Amazon EKS to create a workspace on your behalf using the **Workspace alias** you provide. With the **Select existing workspace** option, you can select an existing workspace from a dropdown list. For more information about workspaces, see [Managing workspaces](../../../prometheus/latest/userguide/AMP-manage-ingest-query.md "../../../prometheus/latest/userguide/AMP-manage-ingest-query.md") in the _Amazon Managed Service for Prometheus User Guide_.

**Service access**

This section summarizes the permissions you grant when sending Prometheus metrics:

- Allow Amazon Managed Service for Prometheus to describe the scraped Amazon EKS cluster
- Allow remote writing to the Amazon Managed Prometheus workspace

If the `AmazonManagedScraperRole` already exists, the scraper uses it. Choose the `AmazonManagedScraperRole` link to see the **Permission details**. If the `AmazonManagedScraperRole` doesn’t exist already, choose the **View permission details** link to see the specific permissions you are granting by sending Prometheus metrics.

**Subnets**

Modify the subnets that the scraper will inherit as needed. If you need to add a grayed out subnet option, go back to the create cluster **Specify networking** step.

**Scraper configuration**

Modify the scraper configuration in YAML format as needed. To do so, use the form or upload a replacement YAML file. For more information, see [Scraper configuration](../../../prometheus/latest/userguide/AMP-collector-how-to.md#AMP-collector-configuration "../../../prometheus/latest/userguide/AMP-collector-how-to.md#AMP-collector-configuration") in the _Amazon Managed Service for Prometheus User Guide_.

Amazon Managed Service for Prometheus refers to the agentless scraper that is created alongside the cluster as an AWS managed collector. For more information about AWS managed collectors, see [Ingest metrics with AWS managed collectors](../../../prometheus/latest/userguide/AMP-collector.md "../../../prometheus/latest/userguide/AMP-collector.md") in the _Amazon Managed Service for Prometheus User Guide_.

###### Important

- If you create a Prometheus scraper using the AWS CLI or AWS API, you need to adjust its configuration to give the scraper in-cluster permissions. For more information, see [Configuring your Amazon EKS cluster](../../../prometheus/latest/userguide/AMP-collector-how-to.md#AMP-collector-eks-setup "../../../prometheus/latest/userguide/AMP-collector-how-to.md#AMP-collector-eks-setup") in the _Amazon Managed Service for Prometheus User Guide_.
- If you have a Prometheus scraper created before November 11, 2024 that uses the `aws-auth`
  `ConfigMap` instead of access entries, you need to update it to access additional metrics from the Amazon EKS cluster control plane. For the updated configuration, see [Manually configuring Amazon EKS for scraper access](../../../prometheus/latest/userguide/AMP-collector-how-to.md#AMP-collector-eks-manual-setup "../../../prometheus/latest/userguide/AMP-collector-how-to.md#AMP-collector-eks-manual-setup") in the _Amazon Managed Service for Prometheus User Guide_.

## Step 2: Use the Prometheus metrics

For more information about how to use the Prometheus metrics after you turn them on for your cluster, see the [Amazon Managed Service for Prometheus User Guide](../../../prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.md "../../../prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.md").

## Step 3: Manage Prometheus scrapers

To manage scrapers, choose the **Observability** tab in the Amazon EKS console. A table shows a list of scrapers for the cluster, including information such as the scraper ID, alias, status, and creation date. You can add more scrapers, edit scrapers, delete scrapers, or view more information about the current scrapers.

To see more details about a scraper, choose the scraper ID link. For example, you can view the ARN, environment, workspace ID, IAM role, configuration, and networking information. You can use the scraper ID as input to Amazon Managed Service for Prometheus API operations like [`DescribeScraper`](../../../prometheus/latest/APIReference/API_DescribeScraper.md "../../../prometheus/latest/APIReference/API_DescribeScraper.md"), [`UpdateScraper`](../../../prometheus/latest/APIReference/API_UpdateScraper.md "../../../prometheus/latest/APIReference/API_UpdateScraper.md"), and [`DeleteScraper`](../../../prometheus/latest/APIReference/API_DeleteScraper.md "../../../prometheus/latest/APIReference/API_DeleteScraper.md"). For more information on using the Prometheus API, see the [Amazon Managed Service for Prometheus API Reference](../../../prometheus/latest/userguide/AMP-APIReference.md "../../../prometheus/latest/userguide/AMP-APIReference.md").
