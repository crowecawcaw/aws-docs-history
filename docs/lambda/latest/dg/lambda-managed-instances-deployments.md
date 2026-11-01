

# Deploying and updating Lambda Managed Instances functions
<a name="lambda-managed-instances-deployments"></a>

When you update a Lambda Managed Instances function, Lambda provisions execution environments for the new function version on your managed instances before shifting traffic to it. You can control deployment speed and safety by selecting a deployment strategy. This topic describes the deployment strategies available for Lambda Managed Instances functions and how to define them with infrastructure as code (IaC).

**Note**  
Before you deploy a function, you must have a capacity provider. For more information, see [capacity providers for Lambda Managed Instances](lambda-managed-instances-capacity-providers.md).

## Deployment strategies
<a name="lambda-managed-instances-deployments-strategies"></a>

Lambda Managed Instances supports the following strategies for releasing a new function version. Choose the strategy that matches how much control you want to retain over the rollout. Rolling updates are the simplest option. Blue/green and canary deployments give you more control over how traffic moves to the new version.

### Rolling updates
<a name="lambda-managed-instances-deployments-rolling"></a>

To perform a rolling update, you publish your changes to the `$LATEST.PUBLISHED` version of your function. `$LATEST.PUBLISHED` is a version type specific to Lambda Managed Instances that you republish with new code or configuration instead of maintaining numbered versions. When you invoke a Lambda Managed Instances function with its unqualified Amazon Resource Name (ARN), Lambda invokes the `$LATEST.PUBLISHED` version. For more information, see [$LATEST.PUBLISHED version in Lambda Managed Instances](lambda-managed-instances-version-publishing.md).

Each time you republish `$LATEST.PUBLISHED`, Lambda gradually replaces the execution environments on your managed instances with the new version, without requiring you to manage traffic shifting directly through a function alias. This is the simplest strategy.

Use rolling updates when you want an automated gradual shift of traffic from the old version to the new version, and you don't need direct control of the percentage of traffic sent to each version to manage the deployment or rollback.

### Blue/green deployments with a weighted alias
<a name="lambda-managed-instances-deployments-blue-green"></a>

In a blue/green deployment, you publish the new version alongside the current version and use an [alias](configuration-aliases.md) with a routing configuration to send a percentage of traffic to the new version. You invoke the function through the alias-qualified ARN. To roll the deployment forward, you increase the weight on the new version; to roll it back, you shift the weight back to the previous version.

The following example uses the AWS CLI to send 10 percent of traffic to version `2` while version `1` continues to serve the remaining 90 percent.

```
aws lambda update-alias \
  --function-name my-managed-instance-function \
  --name production \
  --function-version 1 \
  --routing-config AdditionalVersionWeights={"2"=0.1}
```

In this command:
+ `my-managed-instance-function` is the name of your function.
+ `production` is the name of the alias that you invoke.
+ `--function-version 1` is the version that continues to receive the remaining traffic.
+ `AdditionalVersionWeights={"2"=0.1}` sends 10 percent of traffic to version `2`.

To roll back, clear the routing configuration so that all traffic returns to the stable version.

```
aws lambda update-alias \
  --function-name my-managed-instance-function \
  --name production \
  --function-version 1 \
  --routing-config '{}'
```

In this command, `--routing-config '{}'` clears the routing configuration so that all traffic returns to the version in `--function-version`, version `1`.

### Canary deployments with AWS CodeDeploy
<a name="lambda-managed-instances-deployments-canary"></a>

To automate a blue/green traffic shift, use AWS CodeDeploy. CodeDeploy shifts traffic from the current version to the new version according to a deployment configuration—for example, sending 10 percent of traffic to the new version, waiting five minutes, and then shifting the remainder. If a CloudWatch alarm associated with the deployment enters an alarm state during the shift, CodeDeploy rolls the deployment back automatically.

For more information about CodeDeploy deployment configurations for Lambda, see [Deployment configurations on an Lambda compute platform](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations.html) in the *AWS CodeDeploy User Guide*.

## Choosing between $LATEST.PUBLISHED and numeric versions with aliases
<a name="lambda-managed-instances-deployments-choosing"></a>

Both deployment models roll out changes *gradually*. Whether you update `$LATEST.PUBLISHED` or shift traffic with a weighted alias, Lambda Managed Instances replaces the old version's execution environments with the new version in steps, rather than all at once. This approach keeps instance utilization efficient during the rollout. Instead of provisioning a full second set of execution environments up front, Lambda replaces them in increments: at each step it reclaims capacity from the old version before bringing up the next batch of the new version, so the rollout avoids reaching double the baseline capacity.

### How $LATEST.PUBLISHED rollouts progress
<a name="lambda-managed-instances-deployments-choosing-latest-published"></a>

When you publish an update to `$LATEST.PUBLISHED`, Lambda begins rolling out the new version in steps. At each step, Lambda creates new execution environments—up to 20 percent of the old version's total—and gradually replaces the old version's execution environments.

Two factors determine how long the rollout takes:
+ **Initialization time** - Each step waits for the new execution environments to initialize before it proceeds. If initialization takes 10 minutes, each step waits at least 10 minutes.
+ **Invoke duration** - Before Lambda can remove an old execution environment, its in-flight invocations must finish (drain). If your average invoke duration is 5 minutes, draining takes about 5 minutes on average at each step.

Because Lambda Managed Instances keeps instance utilization high, both initialization and draining contribute to the total deployment time. Functions with long initialization or long-running invocations take longer to fully roll out.

### How numeric versions with aliases progress
<a name="lambda-managed-instances-deployments-choosing-numeric-versions"></a>

Weighted alias updates are gradual in the same way. When you change the routing weights on an alias—for example, from 90 percent version 1 and 10 percent version 2 to 100 percent version 2—Lambda Managed Instances slowly replaces the version 1 execution environments with version 2, without provisioning excess instance capacity.

Use numeric versions with an alias when you want tighter control over the gradual rollout and version-specific observability. Because each version is a distinct qualifier, you can compare per-version metrics for the canary and the stable version before you promote a change. For more information, see [viewing metrics for your Lambda functions](monitoring-metrics-view.md).

## Configuring scaling after a deployment
<a name="lambda-managed-instances-deployments-scaling-config"></a>

Each function version that you deploy has its own scaling configuration, which controls the minimum and maximum number of execution environments that Lambda maintains for that version. Set the scaling configuration after you publish a version so that the new version can serve traffic at the capacity you expect.

The following example sets the scaling configuration for a specific version. Replace `2` with your version number or with `$LATEST.PUBLISHED`.

```
aws lambda put-function-scaling-config \
  --function-name my-managed-instance-function \
  --qualifier 2 \
  --function-scaling-config MinExecutionEnvironments=3,MaxExecutionEnvironments=20
```

## Managing deployments with infrastructure as code
<a name="lambda-managed-instances-deployments-iac"></a>

You can define and deploy Lambda Managed Instances functions and their capacity providers with infrastructure as code, including AWS CloudFormation, the AWS Cloud Development Kit (AWS CDK), and third-party tools such as HashiCorp Terraform. Model your capacity provider, function, versions, and alias as resources so that your deployment strategy is reproducible and reviewable.

Keep the following considerations in mind when you manage Lambda Managed Instances deployments with IaC:
+ **Publish a version to activate a change.** A new function version becomes active on the capacity provider's instances only after it is published. Model each version you want to keep in service—for example, both sides of a blue/green shift—as its own resource.
+ **Scaling configuration is per version.** Apply the minimum and maximum execution environment settings to each version or to `$LATEST.PUBLISHED`. If your IaC tool does not model scaling configuration directly, set it with the `put-function-scaling-config` AWS CLI command after deployment.
+ **Deployment packages must come from Amazon S3 when you use the AWS Cloud Control API.** The AWS Cloud Control API accepts a function's code only as an Amazon S3 location or a container image URI, not as a locally uploaded .zip file. If your IaC tool uses this API, upload your deployment package to an S3 bucket first and reference it by bucket and key. Use a versioned bucket so that updates to the object are detected.

### Example: CloudFormation template
<a name="lambda-managed-instances-deployments-cfn-example"></a>

The following CloudFormation template shows a blue/green deployment. It creates a capacity provider, a Lambda Managed Instances function, two published versions (each with its own function scaling configuration), and an alias named `production` that routes 90 percent of traffic to the stable version and 10 percent to the canary version. To promote the canary, set the alias `FunctionVersion` to the canary version and remove the `RoutingConfig`. To roll back, remove the `RoutingConfig` so that all traffic returns to the stable version. Replace the subnet, security group, role, and Amazon S3 values with your own.

```
AWSTemplateFormatVersion: '2010-09-09'
Description: Lambda Managed Instances blue/green deployment with a weighted alias

Resources:
  MyCapacityProvider:
    Type: AWS::Lambda::CapacityProvider
    Properties:
      CapacityProviderName: my-capacity-provider
      VpcConfig:
        SubnetIds:
          - subnet-0123456789abcdef0
        SecurityGroupIds:
          - sg-0123456789abcdef0
      PermissionsConfig:
        CapacityProviderOperatorRoleArn: arn:aws:iam::111122223333:role/my-capacity-provider-operator-role
      InstanceRequirements:
        Architectures:
          - arm64

  MyFunction:
    Type: AWS::Lambda::Function
    Properties:
      FunctionName: my-managed-instance-function
      Role: arn:aws:iam::111122223333:role/my-function-execution-role
      Runtime: python3.13
      Handler: index.lambda_handler
      Architectures:
        - arm64
      Code:
        S3Bucket: my-deployment-bucket
        S3Key: function.zip
      CapacityProviderConfig:
        LambdaManagedInstancesCapacityProviderConfig:
          CapacityProviderArn: !GetAtt MyCapacityProvider.Arn

  # Stable version - receives the majority of traffic
  StableVersion:
    Type: AWS::Lambda::Version
    Properties:
      FunctionName: !Ref MyFunction
      FunctionScalingConfig:
        MinExecutionEnvironments: 10
        MaxExecutionEnvironments: 50

  # Canary version - receives a small percentage of traffic
  CanaryVersion:
    Type: AWS::Lambda::Version
    Properties:
      FunctionName: !Ref MyFunction
      FunctionScalingConfig:
        MinExecutionEnvironments: 3
        MaxExecutionEnvironments: 20

  ProductionAlias:
    Type: AWS::Lambda::Alias
    Properties:
      FunctionName: !Ref MyFunction
      Name: production
      FunctionVersion: !GetAtt StableVersion.Version
      RoutingConfig:
        AdditionalVersionWeights:
          - FunctionVersion: !GetAtt CanaryVersion.Version
            FunctionWeight: 0.1
```

### Example: CDK
<a name="lambda-managed-instances-deployments-cdk-example"></a>

The following CDK example (TypeScript) defines the same capacity provider and function using the level 1 (L1) constructs from the `aws-cdk-lib/aws-lambda` module. `operatorRole` and `executionRole` are IAM roles defined elsewhere in your stack.

```
import * as cdk from 'aws-cdk-lib';
import * as lambda from 'aws-cdk-lib/aws-lambda';

const capacityProvider = new lambda.CfnCapacityProvider(this, 'MyCapacityProvider', {
  capacityProviderName: 'my-capacity-provider',
  vpcConfig: {
    subnetIds: ['subnet-0123456789abcdef0'],
    securityGroupIds: ['sg-0123456789abcdef0'],
  },
  permissionsConfig: {
    capacityProviderOperatorRoleArn: operatorRole.roleArn,
  },
  instanceRequirements: {
    architectures: ['arm64'],
  },
});

const fn = new lambda.CfnFunction(this, 'MyFunction', {
  functionName: 'my-managed-instance-function',
  role: executionRole.roleArn,
  runtime: 'python3.13',
  handler: 'index.lambda_handler',
  architectures: ['arm64'],
  code: { s3Bucket: 'my-deployment-bucket', s3Key: 'function.zip' },
  capacityProviderConfig: {
    lambdaManagedInstancesCapacityProviderConfig: {
      capacityProviderArn: capacityProvider.attrArn,
    },
  },
  functionScalingConfig: {
    minExecutionEnvironments: 3,
    maxExecutionEnvironments: 20,
  },
  publishToLatestPublished: true,
});
fn.addDependency(capacityProvider);
```

### Example: canary deployment with AWS CodeDeploy
<a name="lambda-managed-instances-deployments-codedeploy-example"></a>

The following CDK example (TypeScript) uses AWS CodeDeploy to shift traffic to a new function version automatically. The `LambdaDeploymentGroup` sends 10 percent of traffic to the new version for five minutes and then shifts the rest. If the CloudWatch alarm enters an alarm state during the deployment, CodeDeploy rolls back to the previous version.

`fn` is the L1 `CfnFunction` from the previous example. Because CodeDeploy's `LambdaDeploymentGroup` works with the level 2 (L2) alias and function constructs, import the L1 function by ARN and build the version and alias from it.

```
import * as cdk from 'aws-cdk-lib';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as codedeploy from 'aws-cdk-lib/aws-codedeploy';
import * as cloudwatch from 'aws-cdk-lib/aws-cloudwatch';

// Import the L1 function so that L2 constructs can reference it.
const importedFn = lambda.Function.fromFunctionArn(this, 'ImportedFunction', fn.attrArn);

// Publish the version that CodeDeploy shifts traffic to.
const canaryVersion = new lambda.CfnVersion(this, 'CanaryVersion', {
  functionName: fn.ref,
});

// Create the alias that CodeDeploy shifts traffic on.
const alias = new lambda.Alias(this, 'ProductionAlias', {
  aliasName: 'production',
  version: lambda.Version.fromVersionAttributes(this, 'CanaryVersionRef', {
    lambda: importedFn,
    version: canaryVersion.attrVersion,
  }),
});

// Roll back automatically if this alarm fires during the deployment.
const errorAlarm = new cloudwatch.Alarm(this, 'ErrorAlarm', {
  metric: importedFn.metricErrors({ period: cdk.Duration.minutes(1) }),
  threshold: 5,
  evaluationPeriods: 1,
  comparisonOperator: cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
});

new codedeploy.LambdaDeploymentGroup(this, 'CanaryDeployment', {
  alias,
  deploymentConfig: codedeploy.LambdaDeploymentConfig.CANARY_10PERCENT_5MINUTES,
  alarms: [errorAlarm],
  autoRollback: {
    failedDeployment: true,
    deploymentInAlarm: true,
  },
});
```

## Next steps
<a name="lambda-managed-instances-deployments-next-steps"></a>
+ Understand [scaling for Lambda Managed Instances](lambda-managed-instances-scaling.md)
+ Learn about [capacity providers for Lambda Managed Instances](lambda-managed-instances-capacity-providers.md)
+ Review [best practices for Lambda Managed Instances](lambda-managed-instances-best-practices.md)