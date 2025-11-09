# Create an HSM in AWS CloudHSM

After you create a cluster in AWS CloudHSM, you can create a hardware security module (HSM).
However, before you can create an HSM in your cluster, the cluster must be in the
uninitialized state. To determine the cluster's state, view the [clusters page in the AWS CloudHSM console](https://console.aws.amazon.com/cloudhsm/home "https://console.aws.amazon.com/cloudhsm/home"), use
the AWS CLI to run the **[describe-clusters](../../../cli/latest/reference/cloudhsmv2/describe-clusters.md "../../../cli/latest/reference/cloudhsmv2/describe-clusters.md")** command, or send a [DescribeClusters](../APIReference/API_DescribeClusters.md "../APIReference/API_DescribeClusters.md") request in the
AWS CloudHSM API. You can create an HSM from the [AWS CloudHSM
console](https://console.aws.amazon.com/cloudhsm/ "https://console.aws.amazon.com/cloudhsm/"), the [AWS CLI](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/"), or the AWS CloudHSM
API.

###### Important

Only create one HSM while your cluster is in the uninitialized state.

Console###### To create an HSM (console)

1. Open the AWS CloudHSM console at
   [https://console.aws.amazon.com/cloudhsm/home](https://console.aws.amazon.com/cloudhsm/home "https://console.aws.amazon.com/cloudhsm/home").
2. Select the radio button next to the ID of the cluster you want to create an HSM for.
3. Select **Actions**. From the drop down menu, choose **Initialize**.
4. Choose an Availability Zone (AZ) for the HSM that you are creating.
5. Select **Create**.
   After you create a cluster and HSM, you can optionally [verify the identity of the HSM](verify-hsm-identity.md "verify-hsm-identity.md"), or proceed directly to [Initialize the cluster](initialize-cluster.md "initialize-cluster.md").

AWS CLI###### To create an HSM ([AWS CLI](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md"))

- At a command prompt, run the **[create-hsm](../../../cli/latest/reference/cloudhsmv2/create-hsm.md "../../../cli/latest/reference/cloudhsmv2/create-hsm.md")**
  command. Specify the cluster ID of the cluster that you created previously and an
  Availability Zone for the HSM. Specify the Availability Zone in the form of
  `us-west-2a`, `us-west-2b`, etc.

```
`$` `aws cloudhsmv2 create-hsm --cluster-id `<cluster ID>` --availability-zone `<Availability Zone>``
`{
 "Hsm": {
 "HsmId": "hsm-ted36yp5b2x",
 "EniIp": "10.0.1.12",
 "EniIpV6": "2600:113f:404:be09:310e:ed34:3412:f733",
 "AvailabilityZone": "us-west-2a",
 "ClusterId": "cluster-igklspoyj5v",
 "EniId": "eni-5d7ade72",
 "SubnetId": "subnet-fd54af9b",
 "State": "CREATE_IN_PROGRESS"
 }
}`

```

After you create a cluster and HSM, you can optionally [verify the identity of the HSM](verify-hsm-identity.md "verify-hsm-identity.md"), or proceed directly to [Initialize the cluster](initialize-cluster.md "initialize-cluster.md").

AWS CloudHSM API ###### To create an HSM (AWS CloudHSM API)

- Send a [CreateHsm](../APIReference/API_CreateHsm.md "../APIReference/API_CreateHsm.md") request. Specify the cluster ID of the cluster
  that you created previously and an Availability Zone for the HSM.

After you create a cluster and HSM, you can optionally [verify the identity of the HSM](verify-hsm-identity.md "verify-hsm-identity.md"), or proceed directly to [Initialize the cluster](initialize-cluster.md "initialize-cluster.md").
