# Edit a shared space

You can only edit the details for an Amazon SageMaker Studio Classic or JupyterLab shared space using the AWS CLI. You can't edit the details of a shared space from the Amazon SageMaker AI console.
You can only update workspace attributes when there are no running applications in the shared space.

Studio Classic
To edit the details of a Studio Classic shared space from the AWS CLI, run the following one of the following commands from the terminal
of your local machine. shared spaces only support the use of JupyterLab 3 image ARNs. For more
information, see [JupyterLab Versioning in Amazon SageMaker Studio Classic](studio-jl.md "studio-jl.md").

```

aws --region `region` \
sagemaker update-space \
--domain-id `domain-id` \
--space-name `space-name` \
--query SpaceArn --output text \
--space-settings '{
  "JupyterServerAppSettings": {
    "DefaultResourceSpec": {
      "SageMakerImageArn": "`sagemaker-image-arn`",
      "InstanceType": "system"
    }
  }
}'

```

JupyterLab
To edit the details of a JupyterLab shared space from the AWS CLI, run the following one of the following commands from the terminal
of your local machine. shared spaces only support the use of JupyterLab 4 image ARNs. For more
information, see [SageMaker JupyterLab](studio-updated-jl.md "studio-updated-jl.md").

```

aws --region `region` \
sagemaker update-space \
--domain-id `domain-id` \
--space-name `space-name` \
--space-settings "{
      "SpaceStorageSettings": {
      "EbsStorageSettings": {
      "EbsVolumeSizeInGb":100
    }
    }
  }
}"

```
