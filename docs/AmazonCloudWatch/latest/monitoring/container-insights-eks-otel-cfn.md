

# Deploy OTel Container Insights with CloudFormation
<a name="container-insights-eks-otel-cfn"></a>

You can deploy OTel Container Insights as infrastructure as code by using a CloudFormation template. This approach is best for teams that manage clusters through IaC pipelines and want repeatable, version-controlled deployments.

The template installs the `amazon-cloudwatch-observability` EKS add-on with OTel Container Insights enabled. If you prefer Kubernetes-native package management, see [Deploy OTel Container Insights with Helm](container-insights-eks-otel-helm.md).

## Prerequisites
<a name="container-insights-eks-otel-cfn-prereqs"></a>

Before you deploy OTel Container Insights with CloudFormation, verify that you meet the following requirements.
+ An existing Amazon EKS cluster running Kubernetes version 1.28 or later
+ AWS CLI version 2.15.0 or later
+ `kubectl` configured to communicate with your target cluster
+ IAM permissions for CloudFormation stack creation
+ Outbound internet access from the cluster to CloudWatch endpoints

## Deploy with CloudFormation
<a name="container-insights-eks-otel-cfn-cloudformation"></a>

Use a CloudFormation template to deploy the CloudWatch Observability add-on, the required IAM role, and the Pod Identity association in a single stack. This template uses the `AWS::EKS::Addon` resource to install the add-on with OTel Container Insights enabled.

### CloudFormation template
<a name="container-insights-eks-otel-cfn-template"></a>

The following template creates the complete set of resources that you need to enable OTel Container Insights on your Amazon EKS cluster.

```
AWSTemplateFormatVersion: '2010-09-09'
Description: Deploy OTel Container Insights on an EKS cluster

Parameters:
  ClusterName:
    Type: String
    Description: The name of your EKS cluster

Resources:
  CloudWatchAgentRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: EKS-CloudWatch-Observability-Role
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service: pods.eks.amazonaws.com
            Action:
              - sts:AssumeRole
              - sts:TagSession
      ManagedPolicyArns:
        - arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy

  PodIdentityAssociation:
    Type: AWS::EKS::PodIdentityAssociation
    Properties:
      ClusterName: !Ref ClusterName
      Namespace: amazon-cloudwatch
      ServiceAccount: cloudwatch-agent
      RoleArn: !GetAtt CloudWatchAgentRole.Arn

  CloudWatchObservabilityAddon:
    Type: AWS::EKS::Addon
    DependsOn: PodIdentityAssociation
    Properties:
      ClusterName: !Ref ClusterName
      AddonName: amazon-cloudwatch-observability
      AddonVersion: v6.2.0-eksbuild.1
      ConfigurationValues: '{"otelContainerInsights":{"enabled":true}}'
      ServiceAccountRoleArn: !GetAtt CloudWatchAgentRole.Arn
      ResolveConflicts: OVERWRITE
```

This template creates the following resources:
+ An IAM role with the `CloudWatchAgentServerPolicy` managed policy attached
+ An EKS Pod Identity association that maps the role to the CloudWatch agent service account
+ The `amazon-cloudwatch-observability` EKS add-on with OTel Container Insights enabled

### To deploy the CloudFormation stack
<a name="container-insights-eks-otel-cfn-deploy-stack"></a>

Use the AWS CLI to create the CloudFormation stack from the template.

**To deploy the stack**

1. Save the preceding template to a file named `otel-container-insights.yaml`.

1. Run the following command. Replace {{cluster-name}} with the name of your Amazon EKS cluster.

   ```
   aws cloudformation create-stack \
     --stack-name otel-container-insights \
     --template-body file://otel-container-insights.yaml \
     --parameters ParameterKey=ClusterName,ParameterValue={{cluster-name}} \
     --capabilities CAPABILITY_NAMED_IAM
   ```

1. Wait for the stack creation to complete.

   ```
   aws cloudformation wait stack-create-complete \
     --stack-name otel-container-insights
   ```

1. Verify that the stack status is `CREATE_COMPLETE`.

   ```
   aws cloudformation describe-stacks \
     --stack-name otel-container-insights \
     --query "Stacks[0].StackStatus" \
     --output text
   ```

## Verify the deployment
<a name="container-insights-eks-otel-cfn-verify"></a>

After the CloudFormation stack creation completes, verify that the add-on is running and sending data to CloudWatch.

**To verify the deployment**

1. Confirm that the CloudWatch agent pods are running.

   ```
   kubectl get pods -n amazon-cloudwatch -l app.kubernetes.io/name=cloudwatch-agent
   ```

   All pods must show `Running` status.

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Container Insights**.

1. Verify that your cluster appears in the cluster list and that metrics are populating.

Metrics typically appear in CloudWatch within 3 to 5 minutes after the deployment completes.

## Remove the deployment
<a name="container-insights-eks-otel-cfn-cleanup"></a>

To remove all resources that the CloudFormation template created, delete the stack.

```
aws cloudformation delete-stack \
  --stack-name otel-container-insights
```