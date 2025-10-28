# Using an AWS managed collector

To use an Amazon Managed Service for Prometheus collector, you must create a scraper that discovers and pulls
metrics in your Amazon EKS cluster.

- You can create a scraper as part of your Amazon EKS cluster creation. For more
  information about creating an Amazon EKS cluster, including creating a scraper, see
  [Creating an Amazon EKS cluster](../../../eks/latest/userguide/create-cluster.md "../../../eks/latest/userguide/create-cluster.md") in the _Amazon EKS User
  Guide_.
- You can create your own scraper, programmatically with the AWS API or by
  using the AWS CLI.
  An Amazon Managed Service for Prometheus collector scrapes metrics that are Prometheus-compatible. For more
  information about Prometheus compatible metrics, see [What are Prometheus-compatible
  metrics?](prom-compatible-metrics.md "prom-compatible-metrics.md"). Amazon EKS
  clusters expose metrics for the API server. Amazon EKS clusters that are Kubernetes version
  `1.28` or above also expose metrics for the `kube-scheduler`
  and `kube-controller-manager`. For more information, see [Fetch
  control plane raw metrics in Prometheus format](../../../eks/latest/userguide/view-raw-metrics.md#scheduler-controller-metrics "../../../eks/latest/userguide/view-raw-metrics.md#scheduler-controller-metrics") in the _Amazon EKS User
  Guide_.

###### Note

Scraping metrics from a cluster may incur charges for network usage. One way to
optimize these costs is to configure your `/metrics` endpoint to compress
the provided metrics (for example, with gzip), reducing the data that must be moved
across the network. How to do this depends on the application or library providing
the metrics. Some libraries gzip by default.

The following topics describe how to create, manage, and configure scrapers.

###### Topics

- [Create a scraper](#AMP-collector-create "#AMP-collector-create")
- [Configuring your Amazon EKS cluster](#AMP-collector-eks-setup "#AMP-collector-eks-setup")
- [Find and delete scrapers](#AMP-collector-list-delete "#AMP-collector-list-delete")
- [Scraper configuration](#AMP-collector-configuration "#AMP-collector-configuration")
- [Troubleshooting scraper
  configuration](#AMP-collector-troubleshoot "#AMP-collector-troubleshoot")
- [Scraper limitations](#AMP-collector-limits "#AMP-collector-limits")

## Create a scraper

An Amazon Managed Service for Prometheus collector consists of a scraper that discovers and collects metrics
from an Amazon EKS cluster. Amazon Managed Service for Prometheus manages the scraper for you, giving you the
scalability, security, and reliability that you need, without having to manage any
instances, agents, or scrapers yourself.

There are three ways to create a scraper:

- A scraper is automatically created for you when you [create an Amazon EKS cluster through the Amazon EKS console](../../../eks/latest/userguide/create-cluster.md "../../../eks/latest/userguide/create-cluster.md") and choose to
  turn on Prometheus metrics.
- You can create a scraper from the Amazon EKS console for an existing cluster.
  Open the cluster in the [Amazon EKS
  console](https://console.aws.amazon.com/eks/home#/clusters "https://console.aws.amazon.com/eks/home#/clusters"), then, on the **Observability** tab,
  choose **Add scraper**.

For more details on the available settings, see [Turn on Prometheus metrics](../../../eks/latest/userguide/prometheus.md#turn-on-prometheus-metrics "../../../eks/latest/userguide/prometheus.md#turn-on-prometheus-metrics") in the
_Amazon EKS User Guide_.

- You can create a scraper using either the AWS API or the AWS CLI.

These options are described in the following procedure.

There are a few prerequisites for creating your own scraper:

- You must have an Amazon EKS cluster created.
- Your Amazon EKS cluster must have [cluster endpoint access
  control](../../../eks/latest/userguide/cluster-endpoint.md "../../../eks/latest/userguide/cluster-endpoint.md") set to include private access. It can include private
  and public, but must include private.
- The Amazon VPC in which the Amazon EKS cluster resides must have [DNS enabled](../../../vpc/latest/userguide/AmazonDNS-concepts.md "../../../vpc/latest/userguide/AmazonDNS-concepts.md").

###### Note

The cluster will be associated with the scraper by its Amazon resource name
(ARN). If you delete a cluster, and then create a new one with the same name,
the ARN will be reused for the new cluster. Because of this, the scraper will
attempt to collect metrics for the new cluster. You [delete scrapers](#AMP-collector-list-delete "#AMP-collector-list-delete") separately from
deleting the cluster.

AWS API
**To create a scraper using the AWS
API**

Use the `CreateScraper` API operation to create a scraper
with the AWS API. The following example creates a scraper in the
`us-west-2` Region. You need to replace the
AWS account, workspace, security, and Amazon EKS cluster information with
your own IDs, and provide the configuration to use for your
scraper.

###### Note

The security group and subnets should be set to the security group
and subnets for the cluster to which you are connecting.

You must include at least two subnets, in at least two
availability zones.

The `scrapeConfiguration` is a Prometheus configuration
YAML file that is base64 encoded. You can download a general purpose
configuration with the `GetDefaultScraperConfiguration` API
operation. For more information about the format of the
`scrapeConfiguration`, see [Scraper configuration](#AMP-collector-configuration "#AMP-collector-configuration").

```
POST /scrapers HTTP/1.1
Content-Length: 415
Authorization: AUTHPARAMS
X-Amz-Date: 20201201T193725Z
User-Agent: aws-cli/1.18.147 Python/2.7.18 Linux/5.4.58-37.125.amzn2int.x86_64 botocore/1.18.6

{
    "alias": "myScraper",
    "destination":  {
        "ampConfiguration": {
            "workspaceArn": "arn:aws:aps:us-west-2:`account-id`:workspace/ws-`workspace-id`"
        }
    },
    "source": {
        "eksConfiguration": {
            "clusterArn": "arn:aws:eks:us-west-2:`account-id`:cluster/`cluster-name`",
            "securityGroupIds": ["sg-`security-group-id`"],
            "subnetIds": ["subnet-`subnet-id-1`", "subnet-`subnet-id-2`"]
        }
    },
    "scrapeConfiguration": {
        "configurationBlob": `<base64-encoded-blob>`
    }
}
```

AWS CLI
**To create a scraper using the
AWS CLI**

Use the `create-scraper` command to create a scraper with
the the AWS CLI. The following example creates a scraper in the
`us-west-2` Region. You need to replace the
AWS account, workspace, security, and Amazon EKS cluster information with
your own IDs, and provide the configuration to use for your
scraper.

###### Note

The security group and subnets should be set to the security group
and subnets for the cluster to which you are connecting.

You must include at least two subnets, in at least two
availability zones.

The `scrape-configuration` is a Prometheus configuration
YAML file that is base64 encoded. You can download a general purpose
configuration with the `get-default-scraper-configuration`
command. For more information about the format of the
`scrape-configuration`, see [Scraper configuration](#AMP-collector-configuration "#AMP-collector-configuration").

```
aws amp create-scraper \
  --source eksConfiguration="{clusterArn='arn:aws:eks:us-west-2:`account-id`:cluster/`cluster-name`', securityGroupIds=['sg-`security-group-id`'],subnetIds=['subnet-`subnet-id-1`', 'subnet-`subnet-id-2`']}" \
  --scrape-configuration configurationBlob=`<base64-encoded-blob>` \
  --destination ampConfiguration="{workspaceArn='arn:aws:aps:us-west-2:`account-id`:workspace/ws-`workspace-id`'}"
```

The following is a full list of the scraper operations that you can use with the
AWS API:

- Create a scraper with the [CreateScraper](../APIReference/API_CreateScraper.md "../APIReference/API_CreateScraper.md") API operation.
- List your existing scrapers with the [ListScrapers](../APIReference/API_ListScrapers.md "../APIReference/API_ListScrapers.md") API operation.
- Update the alias, configuration, or destination of a scraper with the
  [UpdateScraper](../APIReference/API_UpdateScraper.md "../APIReference/API_UpdateScraper.md") API operation.
- Delete a scraper with the [DeleteScraper](../APIReference/API_DeleteScraper.md "../APIReference/API_DeleteScraper.md") API operation.
- Get more details about a scraper with the [DescribeScraper](../APIReference/API_DescribeScraper.md "../APIReference/API_DescribeScraper.md") API operation.
- Get a general purpose configuration for scrapers with the [GetDefaultScraperConfiguration](../APIReference/API_GetDefaultScraperConfiguration.md "../APIReference/API_GetDefaultScraperConfiguration.md") API operation.

###### Note

The Amazon EKS cluster that you are scraping must be configured to allow Amazon Managed Service for Prometheus
to access the metrics. The next topic describes how to configure your
cluster.

### Cross-account setup

To create a cross-account scraper when your Amazon EKS cluster and Amazon Managed Service for Prometheus workspace
are in different accounts, use the following procedure. For example, you have a
source account `account_id_source` containing the Amazon EKS cluster and a
target account `account_id_target` containing the Amazon Managed Service for Prometheus
workspace.

###### To create a scraper in a cross-account setup

1. In the source account, create a role
   `arn:aws:iam::`account_id`_source:role/Source`
   and add the following trust policy.

```
{
    "Effect": "Allow",
    "Principal": {
    "Service": [
        "scraper.aps.amazonaws.com"
     ]
    },
    "Action": "sts:AssumeRole",
    "Condition": {
        "ArnEquals": {
            "aws:SourceArn": "scraper_ARN"
        },
        "StringEquals": {
            "AWS:SourceAccount": "account_id"
        }
    }
}


```

2. On every combination of source (Amazon EKS cluster) and target (Amazon Managed Service for Prometheus
   workspace), you need to create a role
   `arn:aws:iam::`account_id`_target:role/Target`
   and add the following trust policy with permissions for [AmazonPrometheusRemoteWriteAccess](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

```
{
  "Effect": "Allow",
  "Principal": {
     "AWS": "arn:aws:iam::account_id_source:role/Source"
  },
  "Action": "sts:AssumeRole",
  "Condition": {
     "StringEquals": {
        "sts:ExternalId": "scraper_ARN"
      }
  }
}


```

3. Create a scraper with the `--role-configuration`
   option.

```
aws amp create-scraper \
  --source eksConfiguration="{clusterArn='arn:aws:eks:us-west-2:`account-id`_source:cluster/xarw,subnetIds=[subnet-`subnet-id`]}" \
  --scrape-configuration configurationBlob=`<base64-encoded-blob>` \
  --destination ampConfiguration="{workspaceArn='arn:aws:aps:us-west-2:`account-id`_target:workspace/ws-`workspace-id`'}"\
  --role-configuration '{"sourceRoleArn":"arn:aws:iam::`account-id`_source:role/Source", "targetRoleArn":"arn:aws:iam::`account-id`_target:role/Target"}'
```

4. Validate the scraper creation.

```
aws amp list-scrapers
{
    "scrapers": [
        {
            "scraperId": "`scraper-id`",
            "arn": "arn:aws:aps:us-west-2:`account_id`_source:scraper/`scraper-id`",
            "roleArn": "arn:aws:iam::`account_id`_source:role/aws-service-role/scraper.aps.amazonaws.com/AWSServiceRoleForAmazonPrometheusScraperInternal_cc319052-41a3-4",
            "status": {
                "statusCode": "ACTIVE"
            },
            "createdAt": "2024-10-29T16:37:58.789000+00:00",
            "lastModifiedAt": "2024-10-29T16:55:17.085000+00:00",
            "tags": {},
            "source": {
                "eksConfiguration": {
                    "clusterArn": "arn:aws:eks:us-west-2:`account_id`_source:cluster/xarw",
                    "securityGroupIds": [
                        "sg-`security-group-id`",
                        "sg-`security-group-id`"
                    ],
                    "subnetIds": [
                        "subnet-`subnet_id`"
                    ]
                }
            },
            "destination": {
                "ampConfiguration": {
                    "workspaceArn": "arn:aws:aps:us-west-2:`account_id`_target:workspace/ws-`workspace-id`"
                }
            }
        }
    ]
}



```

### Changing between RoleConfiguration and

service-linked role

When you want to switch back to a service-linked role instead of the
`RoleConfiguration` to write to an Amazon Managed Service for Prometheus workspace, you must
update the `UpdateScraper` and provide a workspace in the same
account as the scraper without the `RoleConfiguration`. The
`RoleConfiguration` will be removed from the scraper and the
service-linked role will be used.

When you are changing workspaces in the same account as the scraper and you
want to continue using the `RoleConfiguration`, you must again
provide the `RoleConfiguration` on `UpdateScraper`.

### Creating scraper for workspaces

enabled with customer managed keys

To create a scraper for ingesting metrics into a Amazon Managed Service for Prometheus workspace with
[customer managed
keys](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk"), use the `--role-configuration` with both the source
and target set to the same account.

```
aws amp create-scraper \
  --source eksConfiguration="{clusterArn='arn:aws:eks:us-west-2:`account-id`:cluster/xarw,subnetIds=[subnet-`subnet_id`]}" \
  --scrape-configuration configurationBlob=`<base64-encoded-blob>` \
  --destination ampConfiguration="{workspaceArn='arn:aws:aps:us-west-2:`account-id`:workspace/ws-`workspace-id`'}"\
  --role-configuration '{"sourceRoleArn":"arn:aws:iam::`account_id`:role/Source", "targetRoleArn":"arn:aws:iam::`account_id`:role/Target"}'

```

### Common errors when creating

scrapers

The following are the most common issues when attempting to create a new
scraper.

- Required AWS resources don't exist. The _security
  group_, _subnets_, and _Amazon EKS
  cluster_ specified must exist.
- Insufficient IP address space. You must have at least one IP address
  available in each subnet that you pass into the
  `CreateScraper` API.

## Configuring your Amazon EKS cluster

Your Amazon EKS cluster must be configured to allow the scraper to access metrics.
There are two options for this configuration:

- Use Amazon EKS _access entries_ to automatically provide
  Amazon Managed Service for Prometheus collectors access to your cluster.
- Manually configure your Amazon EKS cluster for managed metric scraping.

The following topics describe each of these in more detail.

### Configure Amazon EKS for

scraper access with access entries

Using access entries for Amazon EKS is the easiest way to give Amazon Managed Service for Prometheus access to
scrape metrics from your cluster.

The Amazon EKS cluster that you are scraping must be configured to allow API
authentication. The cluster authentication mode must be set to either
`API` or `API_AND_CONFIG_MAP`. This is viewable in the
Amazon EKS console on the **Access configuration** tab of the
cluster details. For more information, see [Allowing IAM roles or users
access to Kubernetes object on your Amazon EKS cluster](../../../eks/latest/userguide/access-entries.md "../../../eks/latest/userguide/access-entries.md") in the _Amazon EKS User Guide_.

You can create the scraper when creating the cluster, or after creating the
cluster:

- **When creating a cluster** – You
  can configure this access when you [create an Amazon EKS
  cluster through the Amazon EKS console](../../../eks/latest/userguide/create-cluster.md "../../../eks/latest/userguide/create-cluster.md") (follow the instructions
  to create a scraper as part of the cluster), and an access entry policy
  will automatically be created, giving Amazon Managed Service for Prometheus access to the cluster
  metrics.
- **Adding after a cluster is created**
  – if your Amazon EKS cluster already exists, then set the
  authentication mode to either `API` or
  `API_AND_CONFIG_MAP`, and any scrapers you create [through the Amazon Managed Service for Prometheus API or
  CLI](#AMP-collector-create "#AMP-collector-create") or through the Amazon EKS console will automatically have the
  correct access entry policy created for you, and the scrapers will have
  access to your cluster.

**Access entry policy created**

When you create a scraper and let Amazon Managed Service for Prometheus generate an access entry policy
for you, it generates the following policy. For more information about access
entries, see [Allowing IAM roles or users access to
Kubernetes](../../../eks/latest/userguide/access-entries.md "../../../eks/latest/userguide/access-entries.md") in the _Amazon EKS User Guide_.

```
{
    "rules": [
        {
            "effect": "allow",
            "apiGroups": [
                ""
            ],
            "resources": [
                "nodes",
                "nodes/proxy",
                "nodes/metrics",
                "services",
                "endpoints",
                "pods",
                "ingresses",
                "configmaps"
            ],
            "verbs": [
                "get",
                "list",
                "watch"
            ]
        },
        {
            "effect": "allow",
            "apiGroups": [
                "extensions",
                "networking.k8s.io"
            ],
            "resources": [
                "ingresses/status",
                "ingresses"
            ],
            "verbs": [
                "get",
                "list",
                "watch"
            ]
        },
        {
            "effect": "allow",
            "apiGroups": [
                "metrics.eks.amazonaws.com"
            ],
            "resources": [
                "kcm/metrics",
                "ksh/metrics"
            ],
            "verbs": [
                "get"
            ]
        },
        {
            "effect": "allow",
            "nonResourceURLs": [
                "/metrics"
            ],
            "verbs": [
                "get"
            ]
        }
    ]
}
```

### Manually configuring Amazon EKS for

scraper access

If you prefer to use the `aws-auth ConfigMap` to control access to
your kubernetes cluster, you can still give Amazon Managed Service for Prometheus scrapers access to your
metrics. The following steps will give Amazon Managed Service for Prometheus access to scrape metrics from
your Amazon EKS cluster.

###### Note

For more information about `ConfigMap` and access entries, see
[Allowing IAM roles or users access to
Kubernetes](../../../eks/latest/userguide/access-entries.md "../../../eks/latest/userguide/access-entries.md") in the _Amazon EKS User Guide_.

This procedure uses `kubectl` and the AWS CLI. For information
about installing `kubectl`, see [Installing kubectl](../../../eks/latest/userguide/install-kubectl.md "../../../eks/latest/userguide/install-kubectl.md")
in the _Amazon EKS User Guide_.

###### To manually configure your Amazon EKS cluster for managed metric

scraping

1. Create a file, called `clusterrole-binding.yml`, with the
   following text:

```
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: aps-collector-role
rules:
  - apiGroups: [""]
    resources: ["nodes", "nodes/proxy", "nodes/metrics", "services", "endpoints", "pods", "ingresses", "configmaps"]
    verbs: ["describe", "get", "list", "watch"]
  - apiGroups: ["extensions", "networking.k8s.io"]
    resources: ["ingresses/status", "ingresses"]
    verbs: ["describe", "get", "list", "watch"]
  - nonResourceURLs: ["/metrics"]
    verbs: ["get"]
  - apiGroups: ["metrics.eks.amazonaws.com"]
    resources: ["kcm/metrics", "ksh/metrics"]
    verbs: ["get"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: aps-collector-user-role-binding
subjects:
- kind: User
  name: aps-collector-user
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: aps-collector-role
  apiGroup: rbac.authorization.k8s.io
```

2. Run the following command in your cluster:

```
kubectl apply -f clusterrole-binding.yml
```

This will create the cluster role binding and rule. This example uses
`aps-collector-role` as the role name, and
`aps-collector-user` as the user name. 3. The following command gives you information about the scraper with the
ID `scraper-id`. This is the scraper that you
created using the command in the previous section.

```
aws amp describe-scraper --scraper-id `scraper-id`
```

4. From the results of the `describe-scraper`, find the
   `roleArn`.This will have the following format:

```
arn:aws:iam::`account-id`:role/aws-service-role/scraper.aps.amazonaws.com/AWSServiceRoleForAmazonPrometheusScraper_`unique-id`
```

Amazon EKS requires a different format for this ARN. You must adjust the
format of the returned ARN to be used in the next step. Edit it to match
this format:

```
arn:aws:iam::`account-id`:role/AWSServiceRoleForAmazonPrometheusScraper_`unique-id`
```

For example, this ARN:

```
arn:aws:iam::111122223333:role/aws-service-role/scraper.aps.amazonaws.com/AWSServiceRoleForAmazonPrometheusScraper_1234abcd-56ef-7
```

Must be rewritten as:

```
arn:aws:iam::111122223333:role/AWSServiceRoleForAmazonPrometheusScraper_1234abcd-56ef-7
```

5. Run the following command in your cluster, using the modified
   `roleArn` from the previous step, as well as your cluster
   name and region.:

```
eksctl create iamidentitymapping --cluster `cluster-name` --region `region-id` --arn `roleArn` --username aps-collector-user
```

This allows the scraper to access the cluster using the role and user
you created in the `clusterrole-binding.yml` file.

## Find and delete scrapers

You can use the AWS API or the AWS CLI to list the scrapers in your account or to
delete them.

###### Note

Make sure that you are using the latest version of the AWS CLI or SDK. The
latest version provides you with the latest features and functionality, as well
as security updates. Alternatively, use [AWS Cloudshell](../../../cloudshell/latest/userguide/welcome.md "../../../cloudshell/latest/userguide/welcome.md"),
which provides an always up-to-date command line experience,
automatically.

To list all the scrapers in your account, use the [ListScrapers](../APIReference/API_ListScrapers.md "../APIReference/API_ListScrapers.md")
API operation.

Alternatively, with the AWS CLI, call:

```
aws amp list-scrapers
```

`ListScrapers` returns all of the scrapers in your account, for
example:

```
{
    "scrapers": [
        {
            "scraperId": "s-1234abcd-56ef-7890-abcd-1234ef567890",
            "arn": "arn:aws:aps:us-west-2:123456789012:scraper/s-1234abcd-56ef-7890-abcd-1234ef567890",
            "roleArn": "arn:aws:iam::123456789012:role/aws-service-role/AWSServiceRoleForAmazonPrometheusScraper_1234abcd-2931",
            "status": {
                "statusCode": "DELETING"
            },
            "createdAt": "2023-10-12T15:22:19.014000-07:00",
            "lastModifiedAt": "2023-10-12T15:55:43.487000-07:00",
            "tags": {},
            "source": {
                "eksConfiguration": {
                    "clusterArn": "arn:aws:eks:us-west-2:123456789012:cluster/my-cluster",
                    "securityGroupIds": [
                        "sg-1234abcd5678ef90"
                    ],
                    "subnetIds": [
                        "subnet-abcd1234ef567890",
                        "subnet-1234abcd5678ab90"
                    ]
                }
            },
            "destination": {
                "ampConfiguration": {
                    "workspaceArn": "arn:aws:aps:us-west-2:123456789012:workspace/ws-1234abcd-5678-ef90-ab12-cdef3456a78"
                }
            }
        }
    ]
}
```

To delete a scraper, find the `scraperId` for the scraper that you want
to delete, using the `ListScrapers` operation, and then use the [DeleteScraper](../APIReference/API_DeleteScraper.md "../APIReference/API_DeleteScraper.md") operation to delete it.

Alternatively, with the AWS CLI, call:

```
aws amp delete-scraper --scraper-id `scraperId`
```

## Scraper configuration

You can control how your scraper discovers and collects metrics with a
Prometheus-compatible scraper configuration. For example, you can change the
interval that metrics are sent to the workspace. You can also use relabeling to
dynamically rewrite the labels of a metric. The scraper configuration is a YAML file
that is part of the definition of the scraper.

When a new scraper is created, you specify a configuration by providing a base64
encoded YAML file in the API call. You can download a general purpose configuration
file with the `GetDefaultScraperConfiguration` operation in the Amazon Managed Service for Prometheus
API.

To modify the configuration of a scraper, you can use the
`UpdateScraper` operation. If you need to update the source of the
metrics (for example, to a different Amazon EKS cluster), you must delete the scraper and
recreate it with the new source.

**Supported configuration**

For information about the scraper configuration format, including a detailed
breakdown of the possible values, see [Configuration](https://prometheus.io/docs/prometheus/latest/configuration/configuration/ "https://prometheus.io/docs/prometheus/latest/configuration/configuration/") in the Prometheus documentation. The global configuration
options, and `<scrape_config>` options describe the most commonly
needed options.

Because Amazon EKS is the only supported service, the only service discovery config
(`<*_sd_config>`) supported is the
`<kubernetes_sd_config>`.

The complete list of config sections allowed:

- `<global>`
- `<scrape_config>`
- `<static_config>`
- `<relabel_config>`
- `<metric_relabel_configs>`
- `<kubernetes_sd_config>`

Limitations within these sections are listed after the sample configuration
file.

**Sample configuration file**

The following is a sample YAML configuration file with a 30 second scrape
interval. This sample includes support for the kube API server metrics, as well as
kube-controller-manager and kube-scheduler metrics. For more information, see [Fetch control plane raw metrics in Prometheus format](../../../eks/latest/userguide/view-raw-metrics.md#scheduler-controller-metrics "../../../eks/latest/userguide/view-raw-metrics.md#scheduler-controller-metrics") in the
_Amazon EKS User Guide_.

```
global:
   scrape_interval: 30s
   external_labels:
     clusterArn: apiserver-test-2
scrape_configs:
  - job_name: pod_exporter
    kubernetes_sd_configs:
      - role: pod
  - job_name: cadvisor
    scheme: https
    authorization:
      type: Bearer
      credentials_file: /var/run/secrets/kubernetes.io/serviceaccount/token
    kubernetes_sd_configs:
      - role: node
    relabel_configs:
      - action: labelmap
        regex: __meta_kubernetes_node_label_(.+)
      - replacement: kubernetes.default.svc:443
        target_label: __address__
      - source_labels: [__meta_kubernetes_node_name]
        regex: (.+)
        target_label: __metrics_path__
        replacement: /api/v1/nodes/$1/proxy/metrics/cadvisor
  # apiserver metrics
  - scheme: https
    authorization:
      type: Bearer
      credentials_file: /var/run/secrets/kubernetes.io/serviceaccount/token
    job_name: kubernetes-apiservers
    kubernetes_sd_configs:
    - role: endpoints
    relabel_configs:
    - action: keep
      regex: default;kubernetes;https
      source_labels:
      - __meta_kubernetes_namespace
      - __meta_kubernetes_service_name
      - __meta_kubernetes_endpoint_port_name
  # kube proxy metrics
  - job_name: kube-proxy
    honor_labels: true
    kubernetes_sd_configs:
    - role: pod
    relabel_configs:
    - action: keep
      source_labels:
      - __meta_kubernetes_namespace
      - __meta_kubernetes_pod_name
      separator: '/'
      regex: 'kube-system/kube-proxy.+'
    - source_labels:
      - __address__
      action: replace
      target_label: __address__
      regex: (.+?)(\\:\\d+)?
      replacement: $1:10249
  # Scheduler metrics
  - job_name: 'ksh-metrics'
    kubernetes_sd_configs:
    - role: endpoints
    metrics_path: /apis/metrics.eks.amazonaws.com/v1/ksh/container/metrics
    scheme: https
    bearer_token_file: /var/run/secrets/kubernetes.io/serviceaccount/token
    relabel_configs:
    - source_labels:
      - __meta_kubernetes_namespace
      - __meta_kubernetes_service_name
      - __meta_kubernetes_endpoint_port_name
      action: keep
      regex: default;kubernetes;https
  # Controller Manager metrics
  - job_name: 'kcm-metrics'
    kubernetes_sd_configs:
    - role: endpoints
    metrics_path: /apis/metrics.eks.amazonaws.com/v1/kcm/container/metrics
    scheme: https
    bearer_token_file: /var/run/secrets/kubernetes.io/serviceaccount/token
    relabel_configs:
    - source_labels:
      - __meta_kubernetes_namespace
      - __meta_kubernetes_service_name
      - __meta_kubernetes_endpoint_port_name
      action: keep
      regex: default;kubernetes;https
```

The following are limitations specific to AWS managed collectors:

- **Scrape interval** – The scraper
  config can't specify a scrape interval of less than 30 seconds.
- **Targets** – Targets in the
  `static_config` must be specified as IP addresses.
- **DNS resolution** – Related to the
  target name, the only server name that is recognized in this config is the
  Kubernetes api server, `kubernetes.default.svc`. All other
  machines names must be specified by IP address.
- **Authorization** – Omit if no
  authorization is needed. If it is needed, the authorization must be
  `Bearer`, and must point to the file
  `/var/run/secrets/kubernetes.io/serviceaccount/token`. In
  other words, if used, the authorization section must look like the
  following:

```
    authorization:
      type: Bearer
      credentials_file: /var/run/secrets/kubernetes.io/serviceaccount/token
```

###### Note

`type: Bearer` is the default, so can be omitted.

## Troubleshooting scraper

configuration

Amazon Managed Service for Prometheus collectors automatically discover and scrape metrics. But how can you
troubleshoot when you don't see a metric you expect to see in your Amazon Managed Service for Prometheus
workspace?

###### Important

Verify that private access for your Amazon EKS cluster is enabled. For more
information, see [Cluster private endpoint](../../../eks/latest/userguide/cluster-endpoint.md#cluster-endpoint-private "../../../eks/latest/userguide/cluster-endpoint.md#cluster-endpoint-private") in the _Amazon EKS User Guide_.

The `up` metric is a helpful tool. For each endpoint that an Amazon Managed Service for Prometheus
collector discovers, it automatically vends this metric. There are three states of
this metric that can help you to troubleshoot what is happening within the
collector.

- `up` is not present – If there is no `up`
  metric present for an endpoint, then that means that the collector was not
  able to find the endpoint.

If you are sure that the endpoint exists, there are several reasons why
the collector might not be able to find it.

    + You might need to adjust the scrape configuration. The discovery
     `relabel_config` might need to be adjusted.
    + There could be a problem with the `role` used for
     discovery.
    + The Amazon VPC used by the Amazon EKS cluster might not have [DNS enabled](../../../vpc/latest/userguide/AmazonDNS-concepts.md "../../../vpc/latest/userguide/AmazonDNS-concepts.md"), which would keep the
     collector from finding the endpoint.

- `up` is present, but is always 0 – If `up` is
  present, but 0, then the collector is able to discover the endpoint, but
  can't find any Prometheus-compatible metrics.

In this case, you might try using a `curl` command against the
endpoint directly. You can validate that you have the details correct, for
example, the protocol (`http` or `https`), the
endpoint, or port that you are using. You can also check that the endpoint
is responding with a valid `200` response, and follows the
Prometheus format. Finally, the body of the response can't be larger than
the maximum allowed size. (For limits on AWS managed collectors, see the
following section.)

- `up` is present and greater than 0 – If `up`
  is present, and is greater than 0, then metrics are being sent to
  Amazon Managed Service for Prometheus.

Validate that you are looking for the correct metrics in Amazon Managed Service for Prometheus (or
your alternate dashboard, such as Amazon Managed Grafana). You can use curl again to
check for expected data in your `/metrics` endpoint. Also check
that you haven't exceeded other limits, such as the number of endpoints per
scraper. You can check the number of metrics endpoints being scraped by
checking the count of `up` metrics, using
`count(up)`.

## Scraper limitations

There are few limitations to the fully managed scrapers provided by
Amazon Managed Service for Prometheus.

- **Region** – Your EKS cluster, managed
  scraper, and Amazon Managed Service for Prometheus workspace must all be in the same AWS
  Region.
- **Collectors** – You can have a
  maximum of 10 Amazon Managed Service for Prometheus scrapers per region per account.

###### Note

You can request an increase to this limit by [requesting a quota increase](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase "https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase").

- **Metrics response** – The body of a
  response from any one `/metrics` endpoint request cannot be more
  than 50 megabytes (MB).
- **Endpoints per scraper** – A scraper
  can scrape a maximum of 30,000 `/metrics` endpoints.
- **Scrape interval** – The scraper
  config can't specify a scrape interval of less than 30 seconds.
