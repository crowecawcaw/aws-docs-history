# Removing an HSM from an AWS CloudHSM cluster

You can remove an HSM by using the [AWS CloudHSM
console](https://console.aws.amazon.com/cloudhsm/ "https://console.aws.amazon.com/cloudhsm/"), the [AWS CLI](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/"), or the AWS CloudHSM API.

###### To remove an HSM (console)

1. Open the AWS CloudHSM console at
   [https://console.aws.amazon.com/cloudhsm/home](https://console.aws.amazon.com/cloudhsm/home "https://console.aws.amazon.com/cloudhsm/home").
2. Choose the cluster that contains the HSM that you are removing.
3. On the **HSMs** tab, choose the HSM that you are removing. Then
   choose **Delete HSM**.
4. Confirm that you want to delete the HSM. Then choose
   **Delete**.

###### To remove an HSM (AWS CLI)

- At a command prompt, issue the **[delete-hsm](../../../cli/latest/reference/cloudhsmv2/delete-hsm.md "../../../cli/latest/reference/cloudhsmv2/delete-hsm.md")** command. Pass
  the ID of the cluster that contains the HSM that you are deleting and one of the following
  HSM identifiers:

      + The HSM ID (`--hsm-id`)
      + The HSM IP address (`--eni-ip`)
      + The HSM's elastic network interface ID (`--eni-id`)

  If you don't know the values for these identifiers, issue the **[describe-clusters](../../../cli/latest/reference/cloudhsmv2/describe-clusters.md "../../../cli/latest/reference/cloudhsmv2/describe-clusters.md")**
  command.

```
`$` `aws cloudhsmv2 delete-hsm --cluster-id `<cluster ID>` --eni-ip `<HSM IP address>``
`{
 "HsmId": "hsm-lgavqitns2a"
}`
```

###### To remove an HSM (AWS CloudHSM API)

- Send a [DeleteHsm](../APIReference/API_DeleteHsm.md "../APIReference/API_DeleteHsm.md")
  request, specifying the cluster ID and an identifier for the HSM that you are
  deleting.
