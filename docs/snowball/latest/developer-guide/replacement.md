AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Replacing a node in a cluster

To replace a node, you first need to order a replacement. You can order a
replacement node from the console, the AWS CLI, or one of the AWS
SDKs. If you're ordering a replacement node from the console, you can order
replacements for any job that hasn't been canceled or completed. Then, you diassociate the unhealthy node from the cluster, connect the replacement node to your network and unlock the cluster including the replacement node, associate the replacement node with the cluster, and restart the Amazon S3 compatible storage on Snowball Edge service.

###### To order a replacement node from the console

1. Sign in to the [AWS Snow Family Management Console](https://console.aws.amazon.com/snowfamily/home "https://console.aws.amazon.com/snowfamily/home").
2. Find and choose a job for a node that belongs to the cluster that you
   created from the Job dashboard.
3. For **Actions**, choose **Replace
   node**.

Doing this opens the final step of the job creation wizard, with all
settings identical to how the cluster was originally created. 4. Choose **Create job**.
Your replacement Snowball Edge is now on its way to you. Use the following
procedure to remove the unhealthy node from the cluster.

###### To remove a node from a cluster

1. Power off the node to be removed. For more information, see [Powering off
   the Snowball Edge](turnitoff.md "turnitoff.md").
2. Use the `describe-cluster` command to ensure the unhealthy
   node unreachable. This is indicated by the value of
   `UNREACHABLE` for the `State` name of the
   `NetworkReachability` object.

```

snowballEdge describe-cluster --manifest-file `path/to/manifest/file.bin` --unlock-code `unlock-code` --endpoint https://`ip-address-of-device-in-cluster`

```

###### Example of `describe-cluster` output

```

{
    "ClusterId": "CID12345678-1234-1234-1234-123456789012",
    "Devices": [
        {
            "DeviceId": "JID12345678-1234-1234-1234-123456789012",
            "UnlockStatus": {
                "State": "UNLOCKED"
            },
            "ActiveNetworkInterface": {
                "IpAddress": "10.0.0.0"
            },
            "ClusterAssociation": {
                "ClusterId": "CID12345678-1234-1234-1234-123456789012",
                "State": "ASSOCIATED"
            },
            "NetworkReachability": {
                "State": "REACHABLE"
            },
            "Tags": []
        },
        {
            "DeviceId": "JID12345678-1234-1234-1234-123456789013",
            "UnlockStatus": {
                "State": "UNLOCKED"
            },
            "ActiveNetworkInterface": {
                "IpAddress": "10.0.0.1"
            },
            "ClusterAssociation": {
                "ClusterId": "CID12345678-1234-1234-1234-123456789012",
                "State": "ASSOCIATED"
            },
            "NetworkReachability": {
                "State": "REACHABLE"
            },
            "Tags": []
        },
        {
            "DeviceId": "JID12345678-1234-1234-1234-123456789014",
            "ClusterAssociation": {
                "ClusterId": "CID12345678-1234-1234-1234-123456789012",
                "State": "ASSOCIATED"
            },
            "NetworkReachability": {
                "State": "UNREACHABLE"
            }
        }
    ]
}

```

3. Use the `describe-service` command to ensure the status of
   the `s3-snow` service is `DEGRADED`.

```

snowballEdge describe-service --service-id s3-snow --device-ip-addresses `snow-device-1-address snow-device-2-address` --manifest-file `path/to/manifest/file.bin` --unlock-code `unlock-code` --endpoint https://`snow-device-ip-address`

```

###### Example of output of `describe-service` command

```

{
    "ServiceId": "s3-snow",
    "Autostart": true,
    "Status": {
        "State": "DEGRADED"
    },
    "ServiceCapacities": [
        {
            "Name": "S3 Storage",
            "Unit": "Byte",
            "Used": 38768180432,
            "Available": 82961231819568
        }
    ],
    "Endpoints": [
        {
            "Protocol": "https",
            "Port": 443,
            "Host": "10.0.0.10",
            "CertificateAssociation": {
                "CertificateArn": "arn:aws:snowball-device:::certificate/7Rg2lP9tQaHnW4sC6xUzF1vGyD3jB5kN8MwEiYpT"
            },
            "Description" : "s3-snow bucket API endpoint (for s3control SDK)",
            "DeviceId": "JID-beta-207012320001-24-02-05-17-17-26",
            "Status": {
                "State": "ACTIVE"
            }
        },
        {
            "Protocol": "https",
            "Port": 443,
            "Host": "10.0.0.11",
            "CertificateAssociation": {
                "CertificateArn": "arn:aws:snowball-device:::certificate/7Rg2lP9tQaHnW4sC6xUzF1vGyD3jB5kN8MwEiYpT"
            },
            "Description": "Description" : "s3-snow object & bucket API endpoint (for s3api SDK)",
            "DeviceId": "JID-beta-207012320001-24-02-05-17-17-26",
            "Status": {
                "State": "ACTIVE"
            }
        },
        {
            "Protocol": "https",
            "Port": 443,
            "Host": "10.0.0.12",
            "CertificateAssociation": {
                "CertificateArn": "arn:aws:snowball-device:::certificate/7Rg2lP9tQaHnW4sC6xUzF1vGyD3jB5kN8MwEiYpT"
            },
            "Description": "Description" : "s3-snow bucket API endpoint (for s3control SDK)",
            "DeviceId": "JID-beta-207012240003-24-02-05-17-17-27",
            "Status": {
                "State": "ACTIVE"
            }
        },
        {
            "Protocol": "https",
            "Port": 443,
            "Host": "10.0.0.13",
            "CertificateAssociation": {
                "CertificateArn": "arn:aws:snowball-device:::certificate/7Rg2lP9tQaHnW4sC6xUzF1vGyD3jB5kN8MwEiYpT"
            },
            "Description": "Description" : "s3-snow object & bucket API endpoint (for s3api SDK)",
            "DeviceId": "JID-beta-207012320001-24-02-05-17-17-27",
            "Status": {
                "State": "ACTIVE"
            }
        }
    ]
}

```

4. Use the `disassociate-device` command to disassociate and
   remove the unhealthy node from the cluster.

```

snowballEdge disassociate-device --device-id `device-id` --manifest-file `path/to/manifest/file.bin` --unlock-code `unlock-code` --endpoint https://`ip-address-of-unhealthy-device`

```

###### Example output of `disassociate-device` command

```

Disassociating your Snowball Edge device from the cluster. Your Snowball Edge device will be disassociated from the cluster when it is in the "DISASSOCIATED" state. You can use the describe-cluster command to determine the state of your cluster.

```

5. Use the `describe-cluster` command again to ensure the
   unhealthy node is disassociated from the cluster.

```

snowballEdge describe-cluster --manifest-file `path/to/manifest/file.bin` --unlock-code `unlock-code` --endpoint https:`ip-address-of-healthy-device`

```

###### Example of `describe-cluster` command showing node is

disassociated

```

{
    "ClusterId": "CID12345678-1234-1234-1234-123456789012",
    "Devices": [
        {
            "DeviceId": "JID12345678-1234-1234-1234-123456789012",
            "UnlockStatus": {
                "State": "UNLOCKED"
            },
            "ActiveNetworkInterface": {
                "IpAddress": "10.0.0.0"
            },
            "ClusterAssociation": {
                "ClusterId": "CID12345678-1234-1234-1234-123456789012",
                "State": "ASSOCIATED"
            },
            "NetworkReachability": {
                "State": "REACHABLE"
            },
            "Tags": []
        },
        {
            "DeviceId": "JID12345678-1234-1234-1234-123456789013",
            "UnlockStatus": {
                "State": "UNLOCKED"
            },
            "ActiveNetworkInterface": {
                "IpAddress": "10.0.0.1"
            },
            "ClusterAssociation": {
                "ClusterId": "CID12345678-1234-1234-1234-123456789012",
                "State": "ASSOCIATED"
            },
            "NetworkReachability": {
                "State": "REACHABLE"
            },
            "Tags": []
        },
        {
            "DeviceId": "JID12345678-1234-1234-1234-123456789014",
            "ClusterAssociation": {
                "ClusterId": "CID12345678-1234-1234-1234-123456789012",
                "State": "DISASSOCIATED"
            }
        }
    ]
}

```

6. Power off and return the unhealthy device to AWS. For more information, see [Powering off the Snowball Edge](turnitoff.md "turnitoff.md") and [Returning the Snowball Edge Device](return-device.md "return-device.md").
   When the replacement device arrives, use the following procedure to add it to
   the cluster.

###### To add a replacement device

1. Position the replacement device for the cluster such that you have
   access to the front, back, and top of all devices.
2. Power up the node and ensure that the node is connected to the same
   internal network as the rest of the cluster. For more information, see
   [Connecting to Your Local Network](getting-started-connect.md "getting-started-connect.md").
3. Use the `unlock-cluster` command and include the IP address
   of the new node.

```

snowballEdge unlock-cluster --manifest-file `path/to/manifest/file.bin` --unlock-code `unlock-code` --endpoint https://`ip-address-of-cluster-device` --device-ip-addresses `node-1-ip-address node-2-ip-address new-node-ip-address`

```

The state of the new node will be `DEGRADED` until you
associate it with the cluster in the next step. 4. Use the `associate-device` command to associate the
replacement node with the cluster.

```

snowballEdge associate-device --device-ip-address `new-node-ip-address`

```

###### Example of `associate-device` command output

```

Associating your Snowball Edge device with the cluster. Your Snowball Edge device will be associated with the cluster when it is in the ASSOCIATED state. You can use the describe-device command to determine the state of your devices.

```

5. Use the `describe-cluster` command to ensure the new node
   is associated with the cluster.

```

snowballEdge describe-cluster --manifest-file `path/to/manifest/file.bin` --unlock-code `unlock-code` --endpoint https://`node-ip-address`

```

###### Example of `describe-cluster` command output

```

{
    "ClusterId": "CID12345678-1234-1234-1234-123456789012",
    "Devices": [
        {
            "DeviceId": "JID12345678-1234-1234-1234-123456789012",
            "UnlockStatus": {
                "State": "UNLOCKED"
            },
            "ActiveNetworkInterface": {
                "IpAddress": "10.0.0.0"
            },
            "ClusterAssociation": {
                "ClusterId": "CID12345678-1234-1234-1234-123456789012",
                "State": "ASSOCIATED"
            },
            "NetworkReachability": {
                "State": "REACHABLE"
            },
            "Tags": []
        },
        {
            "DeviceId": "JID-CID12345678-1234-1234-1234-123456789013",
            "UnlockStatus": {
                "State": "UNLOCKED"
            },
            "ActiveNetworkInterface": {
                "IpAddress": "10.0.0.1"
            },
            "ClusterAssociation": {
                "ClusterId": "CID12345678-1234-1234-1234-123456789012",
                "State": "ASSOCIATED"
            },
            "NetworkReachability": {
                "State": "REACHABLE"
            },
            "Tags": []
        },
        {
            "DeviceId": "JID-CID12345678-1234-1234-1234-123456789015",
            "UnlockStatus": {
                "State": "UNLOCKED"
            },
            "ActiveNetworkInterface": {
                "IpAddress": "10.0.0.2"
            },
            "ClusterAssociation": {
                "ClusterId": "CID12345678-1234-1234-1234-123456789012",
                "State": "ASSOCIATED"
            },
            "NetworkReachability": {
                "State": "REACHABLE"
            },
            "Tags": []
        }
    }
]
}

```

6. On the new node, create two virtual network interfaces (VNIs). For
   more information, see [Starting the Amazon S3 compatible storage on Snowball Edge
   service](s3-edge-snow-setting-up.md#setting-up-s3-on-snow-cluster "s3-edge-snow-setting-up.md#setting-up-s3-on-snow-cluster")
7. Use the `stop-service` command to stop the s3-snow
   service.

```

snowballEdge stop-service --service-id s3-snow --device-ip-addresses `cluster-device-1-ip-address cluster-device-2-ip-address cluster-device-3-ip-address` --manifest-file `path/to/manifest/file.bin` --unlock-code `unlock-code` --endpoint https://`snow-device-ip-address`

```

###### Example of `stop-service` command output

```

Stopping the AWS service on your Snowball Edge. You can determine the status of the AWS service using the describe-service command.

```

8. Use the `start-service` command to start the s3-snow
   service after adding the new node to the cluster.

```

snowballEdge start-service --service-id s3-snow --device-ip-addresses `cluster-device-1-ip-address cluster-device-2-ip-address cluster-device-3-ip-address` --virtual-network-interface-arns "`device-1-vni-ip-address-a`" "`device-1-vni-ip-address-b`" "`device-2-vni-ip-address-a`" "`device-2-vni-ip-address-b`" "`device-3-vni-ip-address-a`" "`device-3-vni-ip-address-b`" --manifest-file `path/to/manifest/file.bin` --unlock-code `unlock-code` --endpoint https://`snow-device-ip-address`

```

###### Example of `start-service` command output

```

Starting the AWS service on your Snowball Edge. You can determine the status of the AWS service using the describe-service command.

```

9. Use the `describe-service` command to ensure the s3-snow
   service started.

```

snowballEdge describe-service --service-id s3-snow --device-ip-addresses `snow-device-1-address snow-device-2-address snow-device-3-address` --manifest-file `path/to/manifest/file.bin` --unlock-code `unlock-code` --endpoint https://`snow-device-ip-address`

```

###### Example of `descibe-service` command output

```

{
    "ServiceId": "s3-snow",
    "Autostart": true,
    "Status": {
        "State": "ACTIVE"
    },
    "ServiceCapacities": [{
        "Name": "S3 Storage",
        "Unit": "Byte",
        "Used": 38768180432,
        "Available": 82961231819568
    }],
    "Endpoints": [{
            "Protocol": "https",
            "Port": 443,
            "Host": "10.0.0.10",
            "CertificateAssociation": {
                "CertificateArn": "arn:aws:snowball-device:::certificate/7Rg2lP9tQaHnW4sC6xUzF1vGyD3jB5kN8MwEiYpT"
            },
            "Description": "s3-snow bucket API endpoint (for s3control SDK)",
            "DeviceId": "JID12345678-1234-1234-1234-123456789012",
            "Status": {
                "State": "ACTIVE"
            }
        }, {
            "Protocol": "https",
            "Port": 443,
            "Host": "10.0.0.11",
            "CertificateAssociation": {
                "CertificateArn": "arn:aws:snowball-device:::certificate/7Rg2lP9tQaHnW4sC6xUzF1vGyD3jB5kN8MwEiYpT"
            },
            "Description": "s3-snow object & bucket API endpoint (for s3api SDK)",
            "DeviceId": "JID12345678-1234-1234-1234-123456789013",
            "Status": {
                "State": "ACTIVE"
            }
        }, {
            "Protocol": "https",
            "Port": 443,
            "Host": "10.0.0.12",
            "CertificateAssociation": {
                "CertificateArn": "arn:aws:snowball-device:::certificate/7Rg2lP9tQaHnW4sC6xUzF1vGyD3jB5kN8MwEiYpT"
            },
            "Description": "s3-snow bucket API endpoint (for s3control SDK)",
            "DeviceId": "JID12345678-1234-1234-1234-123456789015",
            "Status": {
                "State": "ACTIVE"
            }
        }, {
            "Protocol": "https",
            "Port": 443,
            "Host": "10.0.0.13",
            "CertificateAssociation": {
                "CertificateArn": "arn:aws:snowball-device:::certificate/7Rg2lP9tQaHnW4sC6xUzF1vGyD3jB5kN8MwEiYpT"
            },
            "Description": "s3-snow object & bucket API endpoint (for s3api SDK)",
            "DeviceId": "JID-beta-207012320001-24-02-05-17-17-27",
            "Status": {
                "State": "ACTIVE"
            }
        }, {
            "Protocol": "https",
            "Port": 443,
            "Host": "10.0.0.14",
            "CertificateAssociation": {
                "CertificateArn": "arn:aws:snowball-device:::certificate/7Rg2lP9tQaHnW4sC6xUzF1vGyD3jB5kN8MwEiYpT"
            },
            "Description": "s3-snow bucket API endpoint (for s3control SDK)",
            "DeviceId": "JID-beta-207012240003-24-02-05-17-17-28",
            "Status": {
                "State": "ACTIVE"
            }
        }, {
            "Protocol": "https",
            "Port": 443,
            "Host": "10.0.0.15",
            "CertificateAssociation": {
                "CertificateArn": "arn:aws:snowball-device:::certificate/7Rg2lP9tQaHnW4sC6xUzF1vGyD3jB5kN8MwEiYpT"
            },
            "Description": "s3-snow object & bucket API endpoint (for s3api SDK),
            "DeviceId": "JID-beta-207012320001-24-02-05-17-17-28",
            "Status": {
                "State": "ACTIVE"
            }
        }
    }]
}

```
