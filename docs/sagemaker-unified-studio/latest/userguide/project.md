# Project

`Project` can be initialized using the following command.

```

from sagemaker_studio import Project
proj = Project()

```

If you are not using the Amazon SageMaker Studio library within the Amazon SageMaker Unified Studio
JupyterLab IDE, you will need to provide either the ID or name of the project you would
like to use and the domain ID of the project.

```

proj = Project(name="my_proj_name", domain_id="123456")

```

## Project properties

A `Project` object has several string properties that can provide
information about the project that you are using.

```

proj.id
proj.name
proj.domain_id,
proj.project_status,
proj.domain_unit_id,
proj.project_profile_id
proj.user_id

```

### IAM Role ARN

To retrieve the project IAM role ARN, you can retrieve the
`iam_role` field. This gets the IAM role ARN of the default IAM
connection within your project.

```

proj.iam_role

```

### AWS KMS Key ARN

If you are using a AWS KMS key within your project, you can retrieve the
`kms_key_arn` field.

```

proj.kms_key_arn

```
