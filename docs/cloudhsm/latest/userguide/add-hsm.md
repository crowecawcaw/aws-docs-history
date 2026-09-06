

# Adding an HSM to an AWS CloudHSM cluster
<a name="add-hsm"></a>

The following figure illustrates the events that occur when you add an HSM to a cluster.

![Animation showing the events that occur when you add an HSM to a cluster.](http://docs.aws.amazon.com/cloudhsm/latest/userguide/images/add-hsm.gif)


1. You add a new HSM to a cluster. The following procedures explain how to do this from the [AWS CloudHSM console](https://console.aws.amazon.com/cloudhsm/), the [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/), and the [AWS CloudHSM API](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/).

   This is the only action that you take. The remaining events occur automatically.

1. AWS CloudHSM makes a backup copy of an existing HSM in the cluster. For more information, see [Backups](backups.md).

1. AWS CloudHSM restores the backup onto the new HSM. This ensures that the HSM is in sync with the others in the cluster.

1. The existing HSMs in the cluster notify the AWS CloudHSM client that there's a new HSM in the cluster.

1. The client establishes a connection to the new HSM.

**To add an HSM (console)**

1. Open the AWS CloudHSM console at [https://console.aws.amazon.com/cloudhsm/home](https://console.aws.amazon.com/cloudhsm/home).

1. Choose a cluster for the HSM that you are adding.

1. On the **HSMs** tab, choose **Create HSM**.

1. Choose an Availability Zone (AZ) for the HSM that you are creating. Then choose **Create**.

**To add an HSM (AWS CLI)**
+ At a command prompt, issue the **[create-hsm](https://docs.aws.amazon.com/cli/latest/reference/cloudhsmv2/create-hsm.html)** command, specifying a cluster ID and an Availability Zone for the HSM that you are creating. If you don't know the cluster ID of your preferred cluster, issue the **[describe-clusters](https://docs.aws.amazon.com/cli/latest/reference/cloudhsmv2/describe-clusters.html)** command. Specify the Availability Zone in the form of `us-east-2a`, `us-east-2b`, etc.

  ```
  $ aws cloudhsmv2 create-hsm --cluster-id {{<cluster ID>}} --availability-zone {{<Availability Zone>}}
  {
      "Hsm": {
          "State": "CREATE_IN_PROGRESS",
          "ClusterId": "cluster-5a73d5qzrdh",
          "HsmId": "hsm-lgavqitns2a",
          "SubnetId": "subnet-0e358c43",
          "AvailabilityZone": "us-east-2c",
          "EniId": "eni-bab18892",
          "EniIp": "10.0.3.10",
          "EniIpV6": "2600:113f:404:be09:310e:ed34:3412:f733"
      }
  }
  ```

**To add an HSM (AWS CloudHSM API)**
+ Send a [CreateHsm](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_CreateHsm.html) request, specifying the cluster ID and an Availability Zone for the HSM that you are creating.