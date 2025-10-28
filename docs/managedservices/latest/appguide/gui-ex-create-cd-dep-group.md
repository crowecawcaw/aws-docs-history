# Create a CodeDeploy Deployment Group

Create the CodeDeploy deployment group.

A CodeDeploy deployment group defines a set of individual instances targeted for a deployment.

REQUIRED DATA:

- `VpcId`: The VPC that you are using, this should be the same as the previously used VPC.
- `CodeDeployApplicationName`: Use the value you previously created.
- `CodeDeployAutoScalingGroups`: Use the name of the Auto Scaling group that you created previously.
- `CodeDeployDeploymentGroupName`: A name for the deployment group. This name must be unique for each application associated with the deployment group.
- `CodeDeployServiceRoleArn`: Use the formula given in the example.

1. On the **Create RFC** page, select the Category **Deployment**,
   subcategory **Applications**, item **CodeDeploy deployment group**, and operation **Create** from the RFC CT
   pick list. Choose **Advanced** and set the values as shown (only a **Subject** is needed for the RFC). Click **Submit** when finished.

###### Note

Reference the CodeDeploy service role ARN in this format
`"arn:aws:iam::085398962942:role/aws-codedeploy-role"` and use the previously-created Auto scaling group name for "ASG_NAME".

```
**Description**:                      Create CodeDeploy Deployment Group for WP
**CodeDeployApplicationName**:        `WordPress`
**CodeDeployAutoScalingGroups**:      `ASG_NAME`
**CodeDeployDeploymentConfigName**:   CodeDeployDefault.HalfAtATime
**CodeDeployDeploymentGroupName**:    `WP CD Group`
**CodeDeployServiceRoleArn**:         arn:aws:iam::`ACCOUNT_ID`:role/aws-codedeploy-role

**VpcId**:                            `VPC_ID`
**Name**:                             WP Deployment Group
```

2. Click **Submit** when finished.
