# Failure recovery

The CLI stops at the point of failure and reports the error with a detailed stack trace. Resources provisioned before the failure remain in place. To recover:

1. Fix the issue identified in the error output.
2. Run `aws-smus-cicd-cli describe --connect` to confirm which resources exist and which permissions are missing.
3. Rerun `aws-smus-cicd-cli deploy`, or redeploy a previous bundle for bundle-based deployments.
4. To clean up a failed deployment, use `aws-smus-cicd-cli destroy --targets <target>` to remove deployed resources.
   For detailed rollback procedures, see the [Rollback Guide](https://github.com/aws/CICD-for-SageMakerUnifiedStudio/blob/main/docs/rollback-guide.md "https://github.com/aws/CICD-for-SageMakerUnifiedStudio/blob/main/docs/rollback-guide.md") on the GitHub website.
