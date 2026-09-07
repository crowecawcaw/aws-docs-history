

This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html) or [AWS Wickr User Guide](https://docs.aws.amazon.com/wickr/latest/userguide/what-is-wickr.html).

# Destroying resources
<a name="destroying-resources"></a>

To delete everything created by this AWS CDK application, you must delete the `WickrRds` stack before all other stacks.

In order for the Amazon RDS resources to properly delete, deletion protection must be disabled, and the removal policy must be set to either `snapshot` or `destroy`. If these are not the current settings, modify the `wickr/rds:deletionProtection` and `wickr/rds:removalPolicy` values in your AWS CDK context and redeploy the Amazon RDS stack by running `npx cdk deploy -e WickrRds`.

Once the deletion protection and removal policy are properly set, run `cdk destroy` for the `WickrRds` stack:

```
npx cdk destroy WickrRds
```

When the `WickrRds` stack has finished destroying, the remaining CloudFormation stacks can be destroyed with the following command:

```
npx cdk destroy --all
```