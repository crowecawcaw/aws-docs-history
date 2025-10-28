# Create a lifecycle

configuration to clone repositories into a Code Editor application

This section shows how to clone a repository and create a Code Editor application with the
lifecycle configuration attached.

1. From your local machine, create a file named `my-script.sh` with the
   following content:

```
#!/bin/bash
set -eux
```

2. Clone the repository of your choice in your lifecycle configuration script.

```
export REPOSITORY_URL="`https://github.com/aws-samples/sagemaker-studio-lifecycle-config-examples.git`"
git -C `/home/sagemaker-user` clone $REPOSITORY_URL
```

3. After finalizing your script, create and attach your lifecycle configuration. For
   more information, see [Create and attach
   lifecycle configurations in Studio](code-editor-use-lifecycle-configurations-studio-create.md "code-editor-use-lifecycle-configurations-studio-create.md").
4. Create your Code Editor application with the lifecycle configuration attached.

```
aws sagemaker create-app \
--domain-id `domain-id` \
--space-name `space-name` \
--app-type `CodeEditor` \
--app-name `default` \
--resource-spec "SageMakerImageArn=arn:aws:sagemaker:`region`:`image-account-id`:image/`sagemaker-distribution-cpu`,LifecycleConfigArn=arn:aws:sagemaker:`region`:`user-account-id`:studio-lifecycle-config/`my-code-editor-lcc`,InstanceType=`ml.t3.large`"
```

For more information about available Code Editor image ARNs, see [Code Editor application instances and images](code-editor-use-instances.md "code-editor-use-instances.md").
