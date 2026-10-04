

# Delete CMS on AWS modules in order
<a name="delete-cms-modules-in-order"></a>

Use the provided Makefile targets to tear down all stacks in the correct reverse order. The make targets prompt for confirmation before destroying resources.

**Note**  
This guidance now ships as a single-environment deployment (`staging`). The former `cms-prod-*` stacks in `us-east-1` were removed as part of the v0.4.0 release. All `cdk destroy` commands and Makefile targets below assume `<stage>` is the environment you deployed against (typically `staging`).

For staging:

```
make -C deployment tear-down-staging
```

When prompted, type `destroy-staging` to confirm. This removes all CMS staging stacks from the deployment region and releases all associated costs.

If you prefer to destroy stacks individually, delete them in reverse dependency order — destroy data-consuming stacks first and the data-processing stack last. The following order is recommended:

```
cdk destroy cms-<stage>-connected-services-consumer --force
cdk destroy cms-<stage>-connected-services-ui --force
cdk destroy cms-<stage>-subscriptions --force
cdk destroy cms-<stage>-dms-service-events --force
cdk destroy cms-<stage>-commands --force
cdk destroy cms-<stage>-simulation --force
cdk destroy cms-<stage>-ws-fanout --force
cdk destroy cms-<stage>-connector --force
cdk destroy cms-<stage>-fleetwise --force
cdk destroy cms-<stage>-fwe-telemetry --force
cdk destroy cms-<stage>-telemetry-integration --force
cdk destroy cms-<stage>-flink --force
cdk destroy cms-<stage>-fleet-intelligence-analytics --force
cdk destroy cms-<stage>-iot --force
cdk destroy cms-<stage>-ui --force
cdk destroy cms-<stage>-msk --force
cdk destroy cms-<stage>-storage --force
cdk destroy cms-<stage>-data-processing --force
```

**Note**  
The optional stacks (`connected-services-consumer`, `connected-services-ui`, `subscriptions`, `dms-service-events`, `connector`, `ws-fanout`) are gated on `DEPLOY_*` environment variables during deploy. Skip the `cdk destroy` line for any stack you did not deploy — `cdk destroy` on a nonexistent stack returns a benign error.

**Important**  
Always destroy the `data-processing` stack last. It provides shared infrastructure (MSK configuration, transform-manifest S3 bucket) that other stacks depend on at runtime.

![Deleting the stack deletes all resources. You can choose to retain these resources.](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/delete-stack.png)
