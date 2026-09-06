

# Amazon SageMaker AI MLOps troubleshooting
<a name="mlopsfaq"></a>

Use the following to troubleshoot issues with MLOps in SageMaker AI. This topic provides information about common errors and how to resolve them. 

## If I try to delete a SageMaker AI project created from a SageMaker AI template and receive an error due to non-empty Amazon S3 buckets or Amazon ECR repositories, how can I delete the project?
<a name="collapsible-section-14"></a>

If you try to delete your SageMaker AI project and get one of the following error messages:

```
The bucket you tried to delete is not empty
```

```
The repository with name '{{repository-name}}' in registry 
        with id '{{id}}' cannot be deleted because it still contains images
```

then you have non-empty Amazon S3 buckets or Amazon ECR repositories which you need to manually delete before you delete the SageMaker AI project. CloudFormation does not automatically delete non-empty Amazon S3 buckets or Amazon ECR repositories for you.