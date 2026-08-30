**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Configure advanced Kubernetes control plane parameters

This guide walks you through setting and viewing advanced Kubernetes control plane parameters using the AWS CLI and AWS Management Console. For an explanation of each parameter and its effect on your cluster, see [Advanced Kubernetes control plane configuration](control-plane-configuration.md "control-plane-configuration.md").

## Prerequisites

Before you begin, make sure that you have:

- **An Amazon EKS cluster running Kubernetes version 1.31 or later** – Advanced Kubernetes control plane configuration is supported on new and existing clusters running Kubernetes version 1.31 or later. All parameters in this topic share this minimum version.
- **AWS CLI** – A command line tool for working with AWS services, including Amazon EKS. For more information, see [Installing](../../../cli/latest/userguide/cli-chap-install.md "../../../cli/latest/userguide/cli-chap-install.md") in the _AWS Command Line Interface User Guide_. After installing the AWS CLI, we recommend that you also configure it. For more information, see [Quick configuration with aws configure](../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-config "../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-config") in the _AWS Command Line Interface User Guide_.
- **Required IAM permissions** – The IAM principal that you’re using must have permissions to describe and update Amazon EKS clusters. To check the current principal, run the following command:

```
aws sts get-caller-identity
```

###### Note

We recommend that you complete the steps in this topic in a Bash shell. If you aren’t using a Bash shell, some script commands such as line continuation characters and the way variables are set and used require adjustment for your shell. Additionally, the quoting and escaping rules for your shell might be different. For more information, see [Using quotation marks with strings in the AWS CLI](../../../cli/latest/userguide/cli-usage-parameters-quoting-strings.md "../../../cli/latest/userguide/cli-usage-parameters-quoting-strings.md") in the _AWS Command Line Interface User Guide_.

Set your preferred cluster name and region before running the commands in this topic:

```
export CLUSTER=my-eks-cluster
export AWS_REGION=us-west-2
```

## Supported values

Amazon EKS validates each parameter against the following ranges and rejects a request outside them.

| Component parameter                                                                                     | Supported values                  | Default               |
| ------------------------------------------------------------------------------------------------------- | --------------------------------- | --------------------- |
| `kubeSchedulerConfig.nodeResourcesFit.scoringStrategy.type`                                             | `LeastAllocated`, `MostAllocated` | `LeastAllocated`      |
| `kubeSchedulerConfig.nodeResourcesFit.scoringStrategy.resources[].weight`                               | `1` to `100`                      | `cpu: 1`, `memory: 1` |
| `kubeControllerManagerConfig.horizontalPodAutoscalerControllerConfig.horizontalPodAutoscalerSyncPeriod` | `10s` to `15s`                    | `15s`                 |
| `kubeControllerManagerConfig.podGcControllerConfig.terminatedPodGcThreshold`                            | `10000` to `12500`                | `12500`               |
| `kubeApiServerConfig.eventTtl`                                                                          | `10m` to `60m`                    | `60m`                 |
| `kubeApiServerConfig.serviceNodePortRange.minPort`                                                      | `10260` to `32767`                | `30000`               |
| `kubeApiServerConfig.serviceNodePortRange.maxPort`                                                      | `10260` to `32767`                | `32767`               |

These values apply to the Kubernetes versions available at publication and can change in later versions. To retrieve the current values for a specific version, see the following section.

## Find the defaults and supported values for a Kubernetes version

The `DescribeClusterVersions` operation reports the default value and the supported values for every control plane parameter, for each Kubernetes version. Read the values from this operation rather than hardcoding them, particularly if you automate cluster configuration or manage clusters across several Kubernetes versions.

```
aws eks describe-cluster-versions --cluster-versions 1.35
```

The response includes a `controlPlaneComponentConfig` object, organized by control plane component. Each parameter reports a `defaultValue` and a `constraints` object:

```
{
    "clusterVersions": [
        {
            "clusterVersion": "1.35",
            "clusterType": "eks",
            "defaultVersion": false,
            "releaseDate": "2026-01-23T00:00:00+00:00",
            "endOfStandardSupportDate": "2027-03-23T00:00:00+00:00",
            "endOfExtendedSupportDate": "2028-03-23T00:00:00+00:00",
            "status": "STANDARD_SUPPORT",
            "controlPlaneScalingTiers": [
                {
                    "tierName": "tier-xl",
                    "apiRequestConcurrency": 2000,
                    "podSchedulingRatePerSecond": 167,
                    "clusterDatabaseSizeGb": 16
                },
                {
                    "tierName": "tier-2xl",
                    "apiRequestConcurrency": 4000,
                    "podSchedulingRatePerSecond": 283,
                    "clusterDatabaseSizeGb": 16
                },
                {
                    "tierName": "tier-4xl",
                    "apiRequestConcurrency": 8000,
                    "podSchedulingRatePerSecond": 400,
                    "clusterDatabaseSizeGb": 16
                },
                {
                    "tierName": "tier-8xl",
                    "apiRequestConcurrency": 16000,
                    "podSchedulingRatePerSecond": 400,
                    "clusterDatabaseSizeGb": 16
                }
            ],
            "controlPlaneComponentConfig": {
                "kubeApiServerConfig": {
                    "eventTtl": {
                        "defaultValue": "60m",
                        "constraints": {
                            "min": "10m",
                            "max": "60m"
                        }
                    },
                    "serviceNodePortRange": {
                        "defaultValue": {
                            "minPort": 30000,
                            "maxPort": 32767
                        },
                        "constraints": {
                            "minPort": {"min": 10260, "max": 32767},
                            "maxPort": {"min": 10260, "max": 32767}
                        }
                    }
                },
                "kubeSchedulerConfig": {
                    "nodeResourcesFit": {
                        "scoringStrategy": {
                            "defaultValue": {
                                "type": "LeastAllocated",
                                "resources": [
                                    {"name": "cpu", "weight": 1},
                                    {"name": "memory", "weight": 1}
                                ]
                            },
                            "constraints": {
                                "scoringStrategy": {
                                    "allowedValues": ["LeastAllocated", "MostAllocated"]
                                },
                                "resources": {
                                    "name": {
                                        "allowedValues": [
                                            "cpu",
                                            "memory",
                                            "nvidia.com/gpu",
                                            "aws.amazon.com/neuron",
                                            "aws.amazon.com/neuroncore"
                                        ]
                                    },
                                    "weight": {"min": 1, "max": 100}
                                }
                            }
                        }
                    }
                },
                "kubeControllerManagerConfig": {
                    "horizontalPodAutoscalerControllerConfig": {
                        "horizontalPodAutoscalerSyncPeriod": {
                            "defaultValue": "15s",
                            "constraints": {
                                "min": "10s",
                                "max": "15s"
                            }
                        }
                    },
                    "podGcControllerConfig": {
                        "terminatedPodGcThreshold": {
                            "defaultValue": 12500,
                            "constraints": {
                                "min": 10000,
                                "max": 12500
                            }
                        }
                    }
                }
            }
        }
    ]
}
```

The preceding response shows the version support dates, Provisioned Control Plane scaling tiers, and the control plane configuration fields. For more information, see [DescribeClusterVersions](../APIReference/API_DescribeClusterVersions.md "../APIReference/API_DescribeClusterVersions.md") in the _Amazon EKS API Reference_.

To return only the configuration fields, use the `--query` option:

```
aws eks describe-cluster-versions --cluster-versions 1.35 \
--query 'clusterVersions[0].controlPlaneComponentConfig'
```

## Control plane configuration — AWS CLI

Each control plane component has its own parameter: `--kube-scheduler-config`, `--kube-controller-manager-config`, and `--kube-api-server-config`. You only specify the components you want to customize. Each parameter accepts inline JSON.

### Create a cluster with control plane parameters

The following command creates a cluster that retains new Kubernetes events for 10 minutes instead of the default 60 minutes. Parameters you don’t specify use their default values.

```
aws eks create-cluster \
--name "$CLUSTER" \
--kubernetes-version 1.35 \
--role-arn arn:aws:iam::111122223333:role/eks-service-role \
--resources-vpc-config subnetIds=subnet-abc123,subnet-def456,securityGroupIds=sg-xyz789 \
--kube-api-server-config '{
  "eventTtl": "10m"
}'
```

Response:

```
{
    "cluster": {
        "name": "my-eks-cluster",
        "arn": "arn:aws:eks:us-west-2:111122223333:cluster/my-eks-cluster",
        "createdAt": 1709640000.0,
        "version": "1.35",
        "roleArn": "arn:aws:iam::111122223333:role/eks-service-role",
        "status": "CREATING",
        "kubeSchedulerConfig": {
            "nodeResourcesFit": {
                "scoringStrategy": {
                    "type": "LeastAllocated"
                }
            }
        },
        "kubeControllerManagerConfig": {
            "horizontalPodAutoscalerControllerConfig": {
                "horizontalPodAutoscalerSyncPeriod": "15s"
            }
        },
        "kubeApiServerConfig": {
            "eventTtl": "10m",
            "serviceNodePortRange": {
                "minPort": 30000,
                "maxPort": 32767
            }
        }
    }
}
```

### View the control plane configuration for a cluster

```
aws eks describe-cluster --name "$CLUSTER"
```

The response includes `kubeSchedulerConfig`, `kubeControllerManagerConfig`, and `kubeApiServerConfig` as top-level fields. These fields are always present and show the complete configuration running on your control plane, including parameters you haven’t customized and their default values.

To return the configuration for a single component, use the `--query` option:

```
aws eks describe-cluster --name "$CLUSTER" \
--query 'cluster.kubeSchedulerConfig'
```

Response:

```
{
    "nodeResourcesFit": {
        "scoringStrategy": {
            "type": "LeastAllocated"
        }
    }
}
```

### Configure the scheduler scoring strategy

By default, the scheduler uses the `LeastAllocated` strategy, which spreads pods across nodes. The following command changes it to `MostAllocated`, which prefers nodes that already have higher resource allocation and packs pods onto fewer nodes.

```
aws eks update-cluster-config \
--name "$CLUSTER" \
--kube-scheduler-config '{
  "nodeResourcesFit": {
    "scoringStrategy": {
      "type": "MostAllocated"
    }
  }
}'
```

Response:

```
{
    "update": {
        "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "status": "InProgress",
        "type": "ControlPlaneComponentConfigUpdate",
        "params": [
            {
                "type": "kubeSchedulerConfig",
                "value": "{\"nodeResourcesFit\":{\"scoringStrategy\":{\"type\":\"MostAllocated\"}}}"
            }
        ],
        "createdAt": 1709643600.0,
        "errors": []
    }
}
```

You can also specify a `resources` array to weight individual resources in the scoring calculation, which is useful when a specific resource is the constraint in your cluster. For more information, see [Advanced Kubernetes control plane configuration](control-plane-configuration.md "control-plane-configuration.md").

The other control plane parameters follow the same pattern, each with its own component flag: `--kube-api-server-config` for `eventTtl` and `serviceNodePortRange`, and `--kube-controller-manager-config` for the Horizontal Pod Autoscaler sync period. For what each parameter does and what to consider before changing it, see [Advanced Kubernetes control plane configuration](control-plane-configuration.md "control-plane-configuration.md").

### Update more than one component at a time

You can specify multiple component parameters in a single call:

```
aws eks update-cluster-config \
--name "$CLUSTER" \
--kube-scheduler-config '{"nodeResourcesFit":{"scoringStrategy":{"type":"MostAllocated"}}}' \
--kube-api-server-config '{"eventTtl":"30m"}'
```

Updates merge with your existing configuration. Only the fields you specify change, and fields you omit keep their current values. The preceding command leaves your controller manager configuration unchanged.

### Monitor a control plane configuration update

A configuration change isn’t in effect when `update-cluster-config` returns. Amazon EKS applies the new configuration through a rolling update of your control plane, which takes several minutes. To block until the change completes:

```
aws eks wait cluster-active --name "$CLUSTER"
```

This command returns when the cluster reaches `ACTIVE` status, typically within several minutes.

To list updates for your cluster:

```
aws eks list-updates --name "$CLUSTER"
```

Response:

```
{
    "updateIds": [
        "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
    ]
}
```

To view the status of a specific update:

```
aws eks describe-update --name "$CLUSTER" \
--update-id a1b2c3d4-5678-90ab-cdef-EXAMPLE11111
```

The status changes from `InProgress` to `Successful` when the update completes, or to `Failed` if an error occurs. The `errors` field indicates the reason for a failure.

## Control plane configuration — AWS Management Console

To configure advanced Kubernetes control plane parameters when you create a cluster:

1. Open the [Amazon EKS console](https://console.aws.amazon.com/eks/home#/clusters "https://console.aws.amazon.com/eks/home#/clusters").
2. Choose **Create cluster**.
3. Under _Configuration options_, select **Custom configuration**.
4. Scroll down to **Control plane configuration**.
5. Choose **Enable control plane configuration**.
6. Set the parameters you want to configure. Parameters you leave unchanged use their default values.
7. Select other cluster configuration options as needed. On the final step, choose **Create cluster**. It might take several minutes for cluster creation to complete.

To configure advanced Kubernetes control plane parameters on an existing cluster:

1. Open the [Amazon EKS console](https://console.aws.amazon.com/eks/home#/clusters "https://console.aws.amazon.com/eks/home#/clusters").
2. Choose the cluster you want to update.
3. Choose the **Overview** tab, then scroll down to **Control plane configuration**.
4. Choose **Manage**, and then select **Enable control plane configuration** to set the parameters you want to change. Then choose **Save changes**.
