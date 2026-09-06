

# Deploy Enhanced Container Insights (Classic) with CloudFormation or Helm
<a name="container-insights-eks-classic-iac"></a>

You can deploy Enhanced Container Insights (Classic) as infrastructure as code by using CloudFormation templates or Helm charts. This approach installs the `amazon-cloudwatch-observability` add-on with a version prior to v6.2.0 to enable the Classic metric pipeline. Choose this approach if you manage clusters through IaC pipelines and want repeatable, version-controlled deployments.

**Recommendation**  
For new deployments, we recommend [OTel Container Insights (Recommended)](container-insights-eks-otel.md), which uses add-on version 6.2.0 or later with the OTel-based pipeline.

## Prerequisites
<a name="container-insights-eks-classic-iac-prereqs"></a>

Before you deploy Enhanced Container Insights (Classic) with CloudFormation or Helm, verify that you meet the following requirements.
+ An existing Amazon EKS cluster running Kubernetes version 1.25 or later
+ AWS CLI version 2.12.0 or later
+ `kubectl` configured to communicate with your target cluster
+ IAM permissions for CloudFormation stack creation (for the CloudFormation method)
+ Helm v3.8 or later (for the Helm method)
+ Outbound internet access from the cluster to CloudWatch endpoints

## Deploy with CloudFormation
<a name="container-insights-eks-classic-iac-cloudformation"></a>

Use a CloudFormation template to deploy the CloudWatch Observability add-on with the Classic configuration. This template uses the `AWS::EKS::Addon` resource to install the add-on with a version prior to v6.2.0.

### CloudFormation template
<a name="container-insights-eks-classic-iac-cfn-template"></a>

The following template creates the resources that you need to enable Enhanced Container Insights (Classic) on your Amazon EKS cluster.

```
AWSTemplateFormatVersion: '2010-09-09'
Description: Deploy Enhanced Container Insights (Classic) on an EKS cluster

Parameters:
  ClusterName:
    Type: String
    Description: The name of your EKS cluster

Resources:
  CloudWatchAgentRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: EKS-CloudWatch-Agent-Role
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
      AddonVersion: v5.4.0-eksbuild.1
      ServiceAccountRoleArn: !GetAtt CloudWatchAgentRole.Arn
      ResolveConflicts: OVERWRITE
```

This template creates the following resources:
+ An IAM role with the `CloudWatchAgentServerPolicy` managed policy attached
+ An EKS Pod Identity association that maps the role to the CloudWatch agent service account
+ The `amazon-cloudwatch-observability` EKS add-on with a Classic version (prior to v6.2.0)

### To deploy the CloudFormation stack
<a name="container-insights-eks-classic-iac-cfn-deploy"></a>

Use the AWS CLI to create the CloudFormation stack from the template.

**To deploy the stack**

1. Save the preceding template to a file named `classic-container-insights.yaml`.

1. Run the following command. Replace {{cluster-name}} with the name of your Amazon EKS cluster.

   ```
   aws cloudformation create-stack \
     --stack-name classic-container-insights \
     --template-body file://classic-container-insights.yaml \
     --parameters ParameterKey=ClusterName,ParameterValue={{cluster-name}} \
     --capabilities CAPABILITY_NAMED_IAM
   ```

1. Wait for the stack creation to complete.

   ```
   aws cloudformation wait stack-create-complete \
     --stack-name classic-container-insights
   ```

1. Verify that the stack status is `CREATE_COMPLETE`.

   ```
   aws cloudformation describe-stacks \
     --stack-name classic-container-insights \
     --query "Stacks[0].StackStatus" \
     --output text
   ```

## Deploy with Helm
<a name="container-insights-eks-classic-iac-helm"></a>

Use the Helm chart to deploy Enhanced Container Insights (Classic) if you manage Kubernetes workloads with Helm. The chart installs the CloudWatch Observability operator with the Classic metric pipeline.

**Note**  
When you use Helm, you must create the IAM role and Pod Identity association separately. The Helm chart installs only the Kubernetes resources.

### Step 1: Create the IAM role
<a name="container-insights-eks-classic-iac-helm-iam"></a>

Create an IAM role for the CloudWatch agent before you install the Helm chart.

**To create the IAM role and Pod Identity association**

1. Run the following command to create the role with a trust policy for EKS Pod Identity.

   ```
   aws iam create-role \
     --role-name EKS-CloudWatch-Agent-Role \
     --assume-role-policy-document '{
       "Version": "2012-10-17",
       "Statement": [{
         "Effect": "Allow",
         "Principal": { "Service": "pods.eks.amazonaws.com" },
         "Action": ["sts:AssumeRole", "sts:TagSession"]
       }]
     }'
   ```

1. Attach the `CloudWatchAgentServerPolicy` managed policy to the role.

   ```
   aws iam attach-role-policy \
     --role-name EKS-CloudWatch-Agent-Role \
     --policy-arn arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy
   ```

1. Create the Pod Identity association. Replace {{cluster-name}} with the name of your Amazon EKS cluster and {{account-id}} with your AWS account ID.

   ```
   aws eks create-pod-identity-association \
     --cluster-name {{cluster-name}} \
     --namespace amazon-cloudwatch \
     --service-account cloudwatch-agent \
     --role-arn arn:aws:iam::{{account-id}}:role/EKS-CloudWatch-Agent-Role
   ```

### Step 2: Install the Helm chart
<a name="container-insights-eks-classic-iac-helm-install"></a>

Install the CloudWatch Observability Helm chart with a Classic version (prior to v6.2.0).

**To install the Helm chart**

1. Run the following command. Replace {{cluster-name}} with the name of your Amazon EKS cluster and {{region}} with your AWS Region.

   ```
   helm install amazon-cloudwatch-observability \
     oci://public.ecr.aws/cloudwatch-agent/amazon-cloudwatch-observability-helm-chart \
     --namespace amazon-cloudwatch \
     --create-namespace \
     --set clusterName={{cluster-name}} \
     --set region={{region}} \
     --version 5.4.0
   ```

1. Verify that the Helm release deployed successfully.

   ```
   helm list -n amazon-cloudwatch
   ```

   The status must show `deployed`.

## Verify the deployment
<a name="container-insights-eks-classic-iac-verify"></a>

After the CloudFormation stack creation or Helm installation completes, verify that the add-on is running and sending data to CloudWatch.

**To verify the deployment**

1. Confirm that the CloudWatch agent pods are running.

   ```
   kubectl get pods -n amazon-cloudwatch -l app.kubernetes.io/name=cloudwatch-agent
   ```

   All pods must show `Running` status.

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Metrics**, and then choose **Classic metrics**.

1. Verify that metrics appear in the `ContainerInsights` namespace for your cluster.

Metrics typically appear in CloudWatch within 3 to 5 minutes after the deployment completes.

## Next steps
<a name="container-insights-eks-classic-iac-next"></a>

After you deploy Enhanced Container Insights (Classic), you can explore the following topics.
+ For console-based setup, see [Enable Enhanced Container Insights (Classic) from the console](container-insights-eks-classic-console.md).
+ For AWS CLI-based setup, see [Setup guide (AWS CLI)](container-insights-eks-classic-setup.md).
+ For information about the metrics that Enhanced Container Insights (Classic) collects, see [Enhanced Container Insights (Classic) metric reference](container-insights-eks-classic-metrics.md).
+ To migrate to OTel Container Insights, see [Migrate from Enhanced Container Insights (Classic) to OTel Container Insights](container-insights-eks-migrate-from-classic.md).
+ For more information about OTel Container Insights, see [OTel Container Insights (Recommended)](container-insights-eks-otel.md).