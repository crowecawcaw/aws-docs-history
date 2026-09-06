

# Delete CMS on AWS modules in order
<a name="delete-cms-modules-in-order"></a>

Use the provided Makefile targets to tear down all stacks in the correct reverse order. The make targets prompt for confirmation before destroying resources.

For staging:

```
make -C deployment tear-down-staging
```

When prompted, type `destroy-staging` to confirm. This removes all CMS staging stacks from the deployment region and releases all associated costs.

For production, no single make target is provided. Tear down production stacks individually using the reverse-dependency-order `cdk destroy` sequence shown below, substituting `prod` for `<stage>`. This is intentional: production teardown requires deliberate per-stack confirmation.

If you prefer to destroy stacks individually, delete them in reverse dependency order — destroy data-consuming stacks first and the data-processing stack last. The following order is recommended:

```
cdk destroy cms-<stage>-commands --force
cdk destroy cms-<stage>-simulation --force
cdk destroy cms-<stage>-ws-fanout --force
cdk destroy cms-<stage>-connector --force
cdk destroy cms-<stage>-bedrock-agents --force
cdk destroy cms-<stage>-fleetwise --force
cdk destroy cms-<stage>-telemetry-integration --force
cdk destroy cms-<stage>-flink --force
cdk destroy cms-<stage>-iot --force
cdk destroy cms-<stage>-ui --force
cdk destroy cms-<stage>-msk --force
cdk destroy cms-<stage>-tco --force
cdk destroy cms-<stage>-storage --force
cdk destroy cms-<stage>-data-processing --force
```

**Important**  
Always destroy the `data-processing` stack last. It provides shared infrastructure (MSK configuration, transform-manifest S3 bucket) that other stacks depend on at runtime.

![Deleting the stack deletes all resources. You can choose to retain these resources.](http://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/delete-stack.png)
