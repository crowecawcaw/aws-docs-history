

# Managing teams
<a name="managing-teams"></a>

You can add, update, and remove teams by using the Amazon MWAA console or the AWS CLI. Before you start, review the prerequisites and the team name and DAG folder rules in [Multi-team environments](multi-team-environments.md).

**Contents**
+ [Adding teams (console)](#managing-teams-console-create)
  + [Adding teams to a new environment](#managing-teams-console-new-env)
  + [Adding teams to an existing environment](#managing-teams-console-existing-env)
+ [Adding and updating teams (AWS CLI)](#managing-teams-api-create)
  + [Adding teams to a new environment](#managing-teams-api-create-new)
  + [Adding or updating teams in an existing environment](#managing-teams-api-add-update)
+ [Removing teams](#managing-teams-removing)
  + [Removing teams (console)](#managing-teams-removing-console)
  + [Removing teams (AWS CLI)](#managing-teams-removing-api)
  + [Returning to single-team mode](#managing-teams-returning-single-team)

## Adding teams (console)
<a name="managing-teams-console-create"></a>

You can add teams when you create an environment or when you edit an existing environment.

### Adding teams to a new environment
<a name="managing-teams-console-new-env"></a>

**To add teams when you create an environment**

1. Open the [Environments](https://console.aws.amazon.com/mwaa/home#/environments) page on the Amazon MWAA console.

1. Choose **Create environment**.

1. On the **Specify details** page, configure the environment name and the DAG code settings. The DAG folder that you specify becomes the global DAG folder.

1. On the **Configure advanced settings** page, expand **Identity Center configuration**.

1. Turn on **Enable IAM Identity Center integration**, and then enter the **AWS access portal URL** and **Identity Store ID**.

   You can't disable IAM Identity Center integration after you enable it.

1. Expand **Teams**.

1. Choose **Add new team**.

1. For **Team name**, enter the display name of the team's IAM Identity Center group.

1. For **DAGs folder**, keep the default location or enter a different Amazon S3 URI. You can also choose **Browse S3**. The default location is a folder named after the team in the bucket that you chose on the **Specify details** page, such as `s3://amzn-s3-demo-bucket/data-engineering/`.

1. To add more teams, repeat the previous three steps.

1. Finish configuring the environment, and then choose **Create environment**.

### Adding teams to an existing environment
<a name="managing-teams-console-existing-env"></a>

**To add teams to an existing environment**

1. Open the [Environments](https://console.aws.amazon.com/mwaa/home#/environments) page on the Amazon MWAA console.

1. Choose the environment, and then choose **Edit**.

1. Choose **Next** to go to the **Configure advanced settings** page.

1. Under **Identity Center configuration**, make sure that **Enable IAM Identity Center integration** is turned on, and then expand **Teams**.

   If the environment doesn't use IAM Identity Center yet, enabling it is permanent. Before you enable it, see [Alternative: enable IAM Identity Center on an existing environment](identity-center-integration.md#iic-integration-enabling-existing-env).

1. Choose **Add new team**, and then enter the team name and DAG folder as described in the previous procedure.

1. Choose **Next** until you are on the **Review and save** page, review your changes, and then choose **Save**.

## Adding and updating teams (AWS CLI)
<a name="managing-teams-api-create"></a>

Use the `--teams` parameter of the `create-environment` and `update-environment` commands. The parameter has a different format for each command:
+ `create-environment` takes a map of teams. Each key is a team name, and each value specifies the team's Amazon S3 bucket ARN (`SourceBucketArn`) and DAG folder path (`DagS3Path`). Each team can use a different bucket, as long as the environment's execution role can read from it.
+ `update-environment` takes an object with two optional fields. `AddOrUpdate` is a map of teams in the same format as `create-environment`. `Remove` is a list of team names to remove.

### Adding teams to a new environment
<a name="managing-teams-api-create-new"></a>

**Example Create an environment with two teams**  <a name="managing-teams-api-create-example"></a>

```
aws mwaa create-environment \
  --name {{my-multi-team-environment}} \
  --airflow-version 3.3.1 \
  --source-bucket-arn arn:aws:s3:::{{amzn-s3-demo-bucket}} \
  --dag-s3-path dags \
  --execution-role-arn arn:aws:iam::{{123456789012}}:role/{{MyMWAAExecutionRole}} \
  --network-configuration SubnetIds={{subnet-12345}},{{subnet-67890}},SecurityGroupIds={{sg-12345}} \
  --identity-center-configuration StartUrl={{https://my-org.awsapps.com/start}},IdentityStoreId={{d-1234567890}} \
  --teams '{
    "data-engineering": {
      "SourceBucketArn": "arn:aws:s3:::{{amzn-s3-demo-bucket}}",
      "DagS3Path": "teams/data-engineering/"
    },
    "analytics": {
      "SourceBucketArn": "arn:aws:s3:::{{amzn-s3-demo-bucket}}",
      "DagS3Path": "teams/analytics/"
    }
  }'
```

### Adding or updating teams in an existing environment
<a name="managing-teams-api-add-update"></a>

**Example Add a team to an existing environment**  <a name="managing-teams-api-update-example"></a>

```
aws mwaa update-environment \
  --name {{my-multi-team-environment}} \
  --teams '{
    "AddOrUpdate": {
      "ml-ops": {
        "SourceBucketArn": "arn:aws:s3:::{{amzn-s3-demo-bucket}}",
        "DagS3Path": "teams/ml-ops/"
      }
    }
  }'
```

## Removing teams
<a name="managing-teams-removing"></a>

When you save the change, Amazon MWAA stops processing the team's DAGs. Existing DAG runs remain in the metadata database, but the team's DAGs, variables, and connections become inaccessible. You can't undo this action. Amazon MWAA doesn't delete the team's DAG files in Amazon S3.

You can't rename a team. To change a team's name, remove the team and add a new one. You can't remove a team and add a team with the same name in the same update.

### Removing teams (console)
<a name="managing-teams-removing-console"></a>

**To remove a team**

1. Open the [Environments](https://console.aws.amazon.com/mwaa/home#/environments) page on the Amazon MWAA console.

1. Choose the environment, and then choose **Edit**.

1. Choose **Next** to go to the **Configure advanced settings** page, and then expand **Teams**.

1. Choose the remove icon (**✕**) next to the team that you want to remove.

1. In the **Remove team?** dialog box, enter the team name to confirm, and then choose **Remove team**.

1. Choose **Next** until you are on the **Review and save** page, review your changes, and then choose **Save**.

### Removing teams (AWS CLI)
<a name="managing-teams-removing-api"></a>

Use the `Remove` field of the `--teams` parameter.

**Example Remove two teams**  <a name="managing-teams-api-remove-example"></a>

```
aws mwaa update-environment \
  --name {{my-multi-team-environment}} \
  --teams '{
    "Remove": ["ml-ops", "analytics"]
  }'
```

### Returning to single-team mode
<a name="managing-teams-returning-single-team"></a>

When you remove all teams, the environment returns to single-team mode. Users still sign in through IAM Identity Center, and all users see the DAGs in the environment's DAG folder. IAM Identity Center integration stays enabled, because you can't disable it.