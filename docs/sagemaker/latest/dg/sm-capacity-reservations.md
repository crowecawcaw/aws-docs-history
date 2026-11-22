

# SageMaker Capacity Reservations

A SageMaker Capacity Reservation is compute capacity that SageMaker AI reserves for your AWS account through an On-Demand Capacity Reservation. SageMaker Capacity Reservations are available to enterprise customers who reserve capacity with SageMaker AI. Each reservation appears in your account as a SageMaker Capacity Reservation with its own Amazon Resource Name (ARN).

You can use the SageMaker AI console, the AWS CLI, or the SageMaker AI API to view your SageMaker Capacity Reservations, the SageMaker AI resources that use them, and how many of their instances are in use.

## Reviewing reservation details
<a name="sm-capacity-reservations-details"></a>

Each SageMaker Capacity Reservation has the following details:
+ **Instance type** – The SageMaker AI instance type of the reserved instances, for example `ml.p5.48xlarge`.
+ **Availability Zone and Availability Zone ID** – Where the reserved instances are. An Availability Zone ID, such as `use1-az1`, identifies the same zone in every account.
+ **Total instances** – The number of instances in the reservation.
+ **Start time and end time** – When the reserved instances are available. A reservation can have no end time.
+ **Status** – SageMaker AI sets the status from the start and end times. The status is `Scheduled` before the start time, `Active` between the start and end times, and `Expired` after the end time.

The ARN of a SageMaker Capacity Reservation has the following format:

```
arn:aws:sagemaker:{{region}}:{{account-id}}:sm-capacity-reservation/{{smcr-id}}
```

## Reviewing resource associations
<a name="sm-capacity-reservations-resources"></a>

A SageMaker Capacity Reservation can be associated with SageMaker HyperPod, SageMaker Inference, or both. If a reservation is associated with SageMaker Inference, its details page also lists the ML reservations that are associated with it.

The status of an association is `Active` when the service can use the reservation. Otherwise, the status is `Pending` or `Inactive`.

## Monitoring reservation usage
<a name="sm-capacity-reservations-usage"></a>

For each SageMaker Capacity Reservation, SageMaker AI reports the number of instances that are in use and the number that are available. An instance is in use when an endpoint runs on it, or when it's part of a HyperPod cluster, even if the cluster isn't running a workload. Usage is broken down by resource type.

SageMaker AI refreshes the usage counts periodically. The console shows when the counts were last updated. The API returns this time in `LastRefreshTime`.