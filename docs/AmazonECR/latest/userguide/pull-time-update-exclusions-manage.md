# Managing pull-time update exclusions

To manage pull-time update exclusions, you need the following IAM permissions:

- `ecr:CreatePullTimeUpdateExclusion` – Grants permission to add a role ARN to the exclusion list.
- `ecr:DeletePullTimeUpdateExclusion` – Grants permission to remove a role ARN from the exclusion list.
- `ecr:ListPullTimeUpdateExclusions` – Grants permission to list all role ARNs in the exclusion list.

###### Note

You don't need `iam:PassRole` permission. Amazon ECR doesn't assume the role to perform an action; it only uses the exclusion configuration ARNs to determine if the pull time of the image should be updated.

You can manage pull-time update exclusions using the Amazon ECR console or the AWS CLI.

AWS Management Console

###### To manage pull-time update exclusions (AWS Management Console)

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/private-registry/repositories](https://console.aws.amazon.com/ecr/private-registry/repositories "https://console.aws.amazon.com/ecr/private-registry/repositories")
2. From the navigation bar, choose the Region.
3. In the navigation pane, choose **Private registry**, **Features & Settings**, and then choose **Pull-time update exclusions**.
4. To add an exclusion, choose **Add exclusion**, enter the role ARN, and then choose **Add**.
5. To remove an exclusion, select the role ARN from the list and choose **Delete**.
6. To view all exclusions, the list displays all configured role ARNs.

AWS CLI

###### To create a pull-time update exclusion

- Use the **create-pull-time-update-exclusion** command to add a role ARN to the exclusion list:

```
`aws ecr create-pull-time-update-exclusion \
 --role-arn `arn:aws:iam::123456789012:role/scanner-role``
```

The command returns the role ARN and creation timestamp:

```
{
   "roleArn": "arn:aws:iam::123456789012:role/scanner-role",
   "createdAt": 1745531331.0
}
```

###### To delete a pull-time update exclusion

- Use the **delete-pull-time-update-exclusion** command to remove a role ARN from the exclusion list:

```
`aws ecr delete-pull-time-update-exclusion \
 --role-arn `arn:aws:iam::123456789012:role/scanner-role``
```

The command returns the role ARN that was deleted:

```
{
  "roleArn": "arn:aws:iam::123456789012:role/scanner-role"
}
```

###### To list pull-time update exclusions

1. Use the **list-pull-time-update-exclusions** command to list all role ARNs in the exclusion list:

```
`aws ecr list-pull-time-update-exclusions`
```

If no exclusions are configured, the command returns an empty list:

```
{
   "pullTimeUpdateExclusions": []
}
```

If exclusions are configured, the command returns the list of role ARNs:

```
{
   "pullTimeUpdateExclusions": [
        "arn:aws:iam::123456789012:role/security-role"
    ]
}
```

2. To paginate results, use the `--max-results` and `--next-token` parameters:

```
`aws ecr list-pull-time-update-exclusions \
 --max-results 4`
```

The command returns up to the specified number of results and a `nextToken` if more results are available:

```
{
   "pullTimeUpdateExclusions": [
        "arn:aws:iam::123456789012:role/security-role1",
        "arn:aws:iam::123456789012:role/security-role2",
        "arn:aws:iam::123456789012:role/security-role3",
        "arn:aws:iam::123456789012:role/security-role4"
    ],
    "nextToken": "ukD72mdD/mC8b5xV3susmJzzaTgp3hKwR9nRUW1yZZ79..."
}
```

To retrieve the next page of results, use the `nextToken` from the previous response:

```
`aws ecr list-pull-time-update-exclusions \
 --max-results 4 \
 --next-token `ukD72mdD/mC8b5xV3susmJzzaTgp3hKwR9nRUW1yZZ79...``
```
