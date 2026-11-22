

# IAM permissions for SageMaker Capacity Reservations

Use AWS Identity and Access Management (IAM) policies to control who can view your SageMaker Capacity Reservations, their resource associations, and their usage. To view reservations in the SageMaker AI console or with the AWS CLI, your IAM identity needs the following permissions.


| Action | What it allows | Resource | 
| --- | --- | --- | 
| sagemaker:ListCapacityReservations | List the SageMaker Capacity Reservations in your account. | \* | 
| sagemaker:DescribeCapacityReservation | View the details of a reservation. | The reservation ARN | 
| sagemaker:DescribeResourceAssociations | View the resource associations of a reservation. | The reservation ARN | 
| sagemaker:GetCapacityReservationUsage | View the usage of a reservation. | The reservation ARN | 

`ListCapacityReservations` doesn't support resource-level permissions. For the other actions, you can scope the `Resource` element to a reservation ARN or to all reservations in an account and AWS Region with `arn:aws:sagemaker:{{region}}:{{account-id}}:sm-capacity-reservation/*`.

The following example policy allows an IAM identity to list all SageMaker Capacity Reservations and to view the details, resource associations, and usage of one reservation. In the ARN, replace the AWS Region, the account ID, and {{smcr-0123456789ab}} with your own values.

**Example – IAM policy to list reservations and view one SageMaker Capacity Reservation**  

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ListReservations",
      "Effect": "Allow",
      "Action": "sagemaker:ListCapacityReservations",
      "Resource": "*"
    },
    {
      "Sid": "ViewOneReservation",
      "Effect": "Allow",
      "Action": [
        "sagemaker:DescribeCapacityReservation",
        "sagemaker:DescribeResourceAssociations",
        "sagemaker:GetCapacityReservationUsage"
      ],
      "Resource": "arn:aws:sagemaker:{{us-east-1}}:{{111122223333}}:sm-capacity-reservation/{{smcr-0123456789ab}}"
    }
  ]
}
```