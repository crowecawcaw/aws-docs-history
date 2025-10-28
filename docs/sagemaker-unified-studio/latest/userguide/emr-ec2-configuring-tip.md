# Configuring trusted identity propagation

You or your admin
add an inline policy to the instance profile role to enable
trusted identity propagation for that cluster in Amazon SageMaker Unified Studio. Before doing this, make sure
you have followed the steps to [add a new EMR on EC2 cluster to your project](adding-new-emr-on-ec2-clusters.md "adding-new-emr-on-ec2-clusters.md").

###### Note

Trusted identity propagation is supported for EMR on EC2 clusters that you create using Amazon SageMaker Unified Studio.

To find the name of the instance profile role for an EMR on EC2 cluster, complete the following steps:

1. Navigate to the project that contains the compute connection. You can
   do this by using the center menu at the top of the page and choosing
   **Browse all projects**, then choosing the name of the
   project that you want to navigate to.
2. On the **Compute** page, go to the **Data processing** tab.
3. Choose the name of the compute you want
   to configure TIP for. This takes you to a page with details about the cluster. The instance profile role is
   on this page and the admin can then search for it in the IAM console.
   As an admin user who could edit IAM policies in the account that owns the project, add the following inline policy to the instance profile role.

```

  {

    "Statement": [
        {
            "Sid": "IdCPermissions",
            "Effect": "Allow",
          "Action": [
                "sso-oauth:CreateTokenWithIAM",
                "sso-oauth:IntrospectTokenWithIAM",
                "sso-oauth:RevokeTokenWithIAM"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AllowAssumeRole",
            "Effect": "Allow",
            "Action": [
                "sts:AssumeRole"
            ],
            "Resource": [
                "`instance-profile-role-ARN`"
            ]
        }
    ]
}

```

After updating the role’s policy, you can use the EMR on EC2 connection to initiate interactive Spark sessions.
