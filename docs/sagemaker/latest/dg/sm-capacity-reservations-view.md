

# View SageMaker Capacity Reservations

You can view your SageMaker Capacity Reservations with the SageMaker AI console or the AWS CLI. Set the console or the `--region` option to the AWS Region of the reservation.

------
#### [ SageMaker AI console ]

**To view a SageMaker Capacity Reservation**

1. Open the SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/).

1. In the left navigation pane, choose **Reserved capacity**, and then choose **On-Demand Capacity Reservations**.

1. In the **SageMaker capacity reservation ID** column, choose the ID of the reservation to view its details.

The details page has the following sections:
+ **SageMaker capacity reservation details** shows the instance type, Availability Zone, start and end times, and ARN of the reservation.
+ **Capacity utilization** shows the total, in-use, and available instances. It also shows when the counts were last updated.
+ **Resource associations** shows whether the reservation is associated with SageMaker HyperPod, SageMaker Inference, or both. It also shows the status of each association.
+ If the reservation is associated with SageMaker Inference, **ML reservation associations** lists the ML reservations that are associated with it.

------
#### [ AWS CLI ]

To list your SageMaker Capacity Reservations, use the [list-capacity-reservations](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/list-capacity-reservations.html) command. The following AWS CLI command lists the active reservations in your account:

```sh
aws sagemaker list-capacity-reservations \
  --filters '[{"Name": "Status", "Values": ["Active"]}]' \
  --region {{us-east-1}}
```

To view the details of a reservation, use the [describe-capacity-reservation](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/describe-capacity-reservation.html) command. Replace the example ARN with your own:

```sh
aws sagemaker describe-capacity-reservation \
  --sm-capacity-reservation-arn {{arn:aws:sagemaker:us-east-1:111122223333:sm-capacity-reservation/smcr-0123456789ab}}
```

To view the resource associations of a reservation, use the [describe-resource-associations](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/describe-resource-associations.html) command:

```sh
aws sagemaker describe-resource-associations \
  --sm-capacity-reservation-arn {{arn:aws:sagemaker:us-east-1:111122223333:sm-capacity-reservation/smcr-0123456789ab}}
```

To view the usage of a reservation, use the [get-capacity-reservation-usage](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/get-capacity-reservation-usage.html) command:

```sh
aws sagemaker get-capacity-reservation-usage \
  --sm-capacity-reservation-arn {{arn:aws:sagemaker:us-east-1:111122223333:sm-capacity-reservation/smcr-0123456789ab}}
```

------