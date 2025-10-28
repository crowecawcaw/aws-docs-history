# Domain

`Domain` can be initialized using the following command.

```

from sagemaker_studio import Domain
dom = Domain()

```

If you are not using the Amazon SageMaker Studio within Amazon SageMaker Unified Studio JupyterLab IDE, you will need to provide the ID of the domain you want to use.

```

dom = Domain(id="123456")

```

## Domain Properties

A `Domain` object has several string properties that can provide information about the domain that you are using.

```

dom.id
dom.root_domain_unit_id
dom.name
dom.domain_execution_role
dom.status
dom.portal_url

```
