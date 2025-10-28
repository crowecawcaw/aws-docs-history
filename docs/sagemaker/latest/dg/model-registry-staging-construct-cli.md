# Invoke ModelLifeCycle

using the AWS CLI examples

You can use the AWS CLI tool to manage your AWS resources. A few AWS CLI
commands include [search](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudsearchdomain/search.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudsearchdomain/search.html") and [list-actions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/list-actions.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/list-actions.html"). The following page will provide examples on how to
use `ModelPackage` while using these commands. For information and
examples on setting up your stage construct, see [Set up Staging
Construct Examples](model-registry-staging-construct-set-up.md "model-registry-staging-construct-set-up.md").

The examples on this page uses the following variables.

- `region` is the region that your
  model package exists in.
- `stage-name` is the name of your
  defined stage.
- `stage-status` is the name of
  your defined stage status.
  The following are example AWS CLI commands using ModelLifeCycle.

Search for your model packages with a `stage-name`
you have already defined.

```
aws sagemaker search --region '`region`' --resource ModelPackage --search-expression '{"Filters": [{"Name": "ModelLifeCycle.Stage","Value": "`stage-name`"}]}'
```

List the actions associated with `ModelLifeCycle`.

```
aws sagemaker list-actions --region '`region`' --action-type ModelLifeCycle
```

Create a model package with ModelLifeCycle.

```
aws sagemaker create-model-package --model-package-group-name '`model-package-group-name`' --source-uri '`source-uri`' --region '`region`' --model-life-cycle '{"Stage":"`stage-name`", "StageStatus":"`stage-status`", "StageDescription":"`Your Staging Comment`"}'
```

Update a model package with ModelLifeCycle.

```
aws sagemaker update-model-package --model-package '`model-package-arn`' --region '`region`' --model-life-cycle '{"Stage":"`stage-name`", "StageStatus":"`stage-status`"}'
```

Search via the ModelLifeCycle field.

```
aws sagemaker search --region '`region`' --resource ModelPackage --search-expression '{"Filters": [{"Name": "ModelLifeCycle.Stage","Value": "`stage-name`"}]}'
```

Fetch audit records for ModelLifeField updates via [Amazon SageMaker ML Lineage Tracking](lineage-tracking.md "lineage-tracking.md") APIs.

```
aws sagemaker list-actions --region '`region`' --action-type ModelLifeCycle
```

```
aws sagemaker describe-action --region '`region`' --action-name '`action-arn or action-name`'
```
