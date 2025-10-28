# Create a notebook with your JupyterLab version

###### Important

JupyterLab 1 and JupyterLab 3 are no longer supported as of June 30, 2025. You can no longer create new or restart stopped notebook instances using these versions. Existing in-service instances may continue to function but will not receive security updates or bug fixes. Migrate to JupyterLab 4 notebook instances for continued support. For more information, see [JupyterLab version maintenance](nbi-jl.md#nbi-jl-version-maintenance "nbi-jl.md#nbi-jl-version-maintenance").

You can select the JupyterLab version when creating your notebook instance from the
console following the steps in [Create an Amazon SageMaker notebook instance](howitworks-create-ws.md "howitworks-create-ws.md").

You can also select the JupyterLab version by passing the
`platform-identifier` parameter when creating your notebook instance using the
AWS CLI as follows:

```
create-notebook-instance --notebook-instance-name `<NEW_NOTEBOOK_NAME>` \
--instance-type `<INSTANCE_TYPE>` \
--role-arn `<YOUR_ROLE_ARN>` \
--platform-identifier notebook-al2-v3
```
