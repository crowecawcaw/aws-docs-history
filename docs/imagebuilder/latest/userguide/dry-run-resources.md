

# Validate Image Builder resource creation with a dry run
<a name="dry-run-resources"></a>

With a dry run, you can check whether a request to create an Image Builder resource would succeed, without creating the resource. When you set the `dryRun` parameter to `true` in your request, Image Builder validates the required permissions and request parameters, and then stops before it creates anything. The outcome is one of the following:
+ If validation succeeds, the request fails with a `DryRunOperationException` error. This error indicates that the request is valid, and that the resource creation would have succeeded without the `dryRun` parameter.
+ If validation fails, the request returns the same error that it would return without the `dryRun` parameter, for example `InvalidParameterValueException` or `ResourceAlreadyExistsException`.

In both cases, Image Builder doesn't create the resource. Dry runs give you immediate feedback on your resource configurations. This is especially useful for automation and AI agents that create Image Builder resources. Such tools can validate each configuration and correct errors before they create anything.

The following create actions support the `dryRun` parameter:
+ `CreateComponent`
+ `CreateContainerRecipe`
+ `CreateDistributionConfiguration`
+ `CreateImagePipeline`
+ `CreateImageRecipe`
+ `CreateInfrastructureConfiguration`
+ `CreateLifecyclePolicy`
+ `CreateWorkflow`

**Note**  
The `CreateImage` action doesn't support the `dryRun` parameter, because it starts an image build rather than creating a configuration resource.

**Perform a dry run from the AWS CLI**  
The following example shows how to validate an infrastructure configuration with the `create-infrastructure-configuration` command. The `--dry-run` option turns the request into a dry run.

```
aws imagebuilder create-infrastructure-configuration \
    --name {{my-example-infrastructure-configuration}} \
    --instance-profile-name {{EC2InstanceProfileForImageBuilder}} \
    --dry-run
```

If the configuration is valid, the command returns the following error to show that the request would have succeeded.

```
An error occurred (DryRunOperationException) when calling the CreateInfrastructureConfiguration operation: Request would have succeeded, but dryRun flag is set.
```