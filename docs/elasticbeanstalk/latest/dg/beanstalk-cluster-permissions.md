

# Permissions for Beanstalk Cluster
<a name="beanstalk-cluster-permissions"></a>

A Beanstalk Cluster environment does not use the Amazon Elastic Compute Cloud (Amazon EC2) instance profile from Beanstalk Standard. You provide the IAM roles that Amazon EKS requires for its cluster and nodes, and the role that Elastic Beanstalk uses to publish the environment's metrics, logs, and traces. You can optionally provide an application role for the running application. Elastic Beanstalk uses a service-linked role for its own operation of the environment.

## Roles that you provide
<a name="beanstalk-cluster-permissions-customer-roles"></a>

A Beanstalk Cluster environment uses a cluster role, a node role, and an observability role. When you create an environment in the Elastic Beanstalk console and accept the default service access settings, the console creates all three for you, with the names in [Name, trusted service, and permissions for each role](#beanstalk-cluster-permissions-role-details), when they don't already exist in your account:
+ **Cluster role** – Amazon EKS assumes this role for the cluster that Elastic Beanstalk creates. Pass its ARN in the `cluster-role` setting of the `aws:elasticbeanstalk:eks` namespace.
+ **Node role** – The cluster's Amazon EC2 nodes assume this role, which must allow them to pull application images from Amazon ECR. Pass its ARN in the `node-role` setting of the `aws:elasticbeanstalk:eks` namespace.
+ **Observability role** – The components that publish the environment's metrics, logs, and traces assume this role through Amazon EKS Pod Identity. Pass its ARN in the `observability-role` setting of the `aws:elasticbeanstalk:eks:environment` namespace.

If you create these roles outside the Elastic Beanstalk console, we highly recommend that you create them exactly as specified in [Name, trusted service, and permissions for each role](#beanstalk-cluster-permissions-role-details). Then, when you create an environment, pass each role ARN in its configuration option. For a worked example, see [Getting started with Beanstalk Cluster](beanstalk-cluster-getting-started.md).

If you supply source for Elastic Beanstalk to build into a container image, you also provide an **image build role**. AWS CodeBuild assumes it to run the build in your account. This role belongs to the application-version build rather than to the running environment. See [Building container images for Beanstalk Cluster environments](beanstalk-cluster-app-versions.md).

You can also provide an optional **application role**, which your running application uses to call AWS services. See [Application permissions](#beanstalk-cluster-permissions-application).

**Important**  
Use the role names in the following table. The console selects existing roles by name, so it doesn't select a role that you created under a different name, and you have to choose that role yourself. Names matter for cluster reuse as well: Elastic Beanstalk registers the cluster, node, and observability roles with the cluster it creates, and a later environment on the same subnet set must supply the same three roles. Elastic Beanstalk rejects an environment whose roles differ, rather than placing it on another cluster. See [Environment grouping](beanstalk-cluster-concepts.md#beanstalk-cluster-clusters-sharing).

Each role trusts a different service and carries its own permissions:


**Name, trusted service, and permissions for each role**  

| Role | Role name | Trusted service | AWS managed policies | 
| --- | --- | --- | --- | 
| Cluster role | aws-elasticbeanstalk-eks-cluster-role | eks.amazonaws.com | AmazonEKSClusterPolicy, AmazonEKSNetworkingPolicy, AmazonEKSComputePolicy, AmazonEKSBlockStoragePolicy, AmazonEKSLoadBalancingPolicy, AWSElasticBeanstalkEKSTagging | 
| Node role | aws-elasticbeanstalk-eks-node-role | ec2.amazonaws.com | AmazonEKSWorkerNodeMinimalPolicy, AmazonEC2ContainerRegistryPullOnly, AmazonSSMManagedInstanceCore | 
| Observability role | aws-elasticbeanstalk-eks-observability-role | pods.eks.amazonaws.com | CloudWatchAgentServerPolicy, AWSElasticBeanstalkEKSObservability | 
| Image build role | aws-elasticbeanstalk-eks-image-build-role | codebuild.amazonaws.com | AWSElasticBeanstalkEKSImageBuild | 
| Application role (optional) | You choose the name | pods.eks.amazonaws.com | None. You grant only the permissions that your application needs. See [Configure an application role](#beanstalk-cluster-permissions-application-role). | 

**To provide the cluster, node, and observability roles**

1. If you create your environment in the Elastic Beanstalk console, you don't need to prepare anything. The console looks for the three roles by name, using the names in the preceding table, selects them when they already exist in your account, and creates them when they don't. It matches on the role name alone, not on the full ARN, and because IAM role names are unique within an account, the path that a role sits at doesn't affect the match.

1. If you use the AWS CLI or the API, create the three roles first. Neither client creates them for you. Give each role the name and trusted service in the preceding table, and attach the listed policies. The roles must be in the same AWS account as the environment.

1. Supply all three ARNs in the `cluster-role`, `node-role`, and `observability-role` settings when you create the environment. Supply the observability role explicitly rather than relying on a default, so that every environment on a subnet set registers the same roles.

1. If your application calls AWS services, configure the optional application role as described in [Configure an application role](#beanstalk-cluster-permissions-application-role).

The subnet set alone selects the cluster, so use a different subnet set when you need a separate cluster with different infrastructure roles. You cannot change the subnets or the cluster, node, and observability roles of an existing Beanstalk Cluster environment. See [Environment grouping](beanstalk-cluster-concepts.md#beanstalk-cluster-clusters-sharing). The optional application role is specific to an environment and can differ between environments; see [Configure an application role](#beanstalk-cluster-permissions-application-role).

## Permissions to create the environment
<a name="beanstalk-cluster-permissions-caller"></a>

Because you hand these roles to Elastic Beanstalk, the principal that creates the environment needs permission to pass them. Elastic Beanstalk verifies this before it provisions anything, so grant the following to that principal:
+ `iam:GetRole` and `iam:PassRole` on every role that you pass: the cluster, node, and observability roles, and also the application role and the image build role if you use them. Scope `iam:PassRole` with the `iam:PassedToService` condition key. Its values are the services that receive the roles: `eks.amazonaws.com` for the cluster role, `ec2.amazonaws.com` for the node role, `pods.eks.amazonaws.com` for the observability and application roles, `codebuild.amazonaws.com` for the image build role, and `elasticbeanstalk.amazonaws.com` because Elastic Beanstalk passes these roles on your behalf.
+ `iam:CreateServiceLinkedRole`, which the first Beanstalk Cluster environment in an account needs so that Elastic Beanstalk and Amazon EKS can create their service-linked roles. Scope it with the `iam:AWSServiceName` condition key, whose values are `elasticbeanstalk.amazonaws.com` and `eks.amazonaws.com`.

The following policy grants all of this. Replace the account ID with your own, use your application role's name, and remove any role that you don't pass. The role names shown are the ones in the preceding table, which the console creates and selects.

Unlike the console, which selects a role by name, a policy matches a role by its full ARN, so each `Resource` entry has to include the role's IAM path. The roles that the console creates sit at `/service-role/`, as shown here. If you created a role another way it might have no path, in which case its ARN is `arn:aws:iam::{{111122223333}}:role/{{role-name}}`. To read a role's ARN, run `aws iam get-role --role-name {{role-name}} --query Role.Arn --output text`.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "InspectTheRoles",
      "Effect": "Allow",
      "Action": "iam:GetRole",
      "Resource": [
        "arn:aws:iam::{{111122223333}}:role/service-role/aws-elasticbeanstalk-eks-cluster-role",
        "arn:aws:iam::{{111122223333}}:role/service-role/aws-elasticbeanstalk-eks-node-role",
        "arn:aws:iam::{{111122223333}}:role/service-role/aws-elasticbeanstalk-eks-observability-role",
        "arn:aws:iam::{{111122223333}}:role/service-role/aws-elasticbeanstalk-eks-image-build-role",
        "arn:aws:iam::{{111122223333}}:role/{{my-application-role}}"
      ]
    },
    {
      "Sid": "PassTheRolesToBeanstalk",
      "Effect": "Allow",
      "Action": "iam:PassRole",
      "Resource": [
        "arn:aws:iam::{{111122223333}}:role/service-role/aws-elasticbeanstalk-eks-cluster-role",
        "arn:aws:iam::{{111122223333}}:role/service-role/aws-elasticbeanstalk-eks-node-role",
        "arn:aws:iam::{{111122223333}}:role/service-role/aws-elasticbeanstalk-eks-observability-role",
        "arn:aws:iam::{{111122223333}}:role/service-role/aws-elasticbeanstalk-eks-image-build-role",
        "arn:aws:iam::{{111122223333}}:role/{{my-application-role}}"
      ],
      "Condition": {
        "StringEquals": {
          "iam:PassedToService": [
            "eks.amazonaws.com",
            "ec2.amazonaws.com",
            "pods.eks.amazonaws.com",
            "codebuild.amazonaws.com",
            "elasticbeanstalk.amazonaws.com"
          ]
        }
      }
    },
    {
      "Sid": "CreateServiceLinkedRolesOnFirstEnvironment",
      "Effect": "Allow",
      "Action": "iam:CreateServiceLinkedRole",
      "Resource": "arn:aws:iam::{{111122223333}}:role/aws-service-role/*",
      "Condition": {
        "StringEquals": {
          "iam:AWSServiceName": [
            "elasticbeanstalk.amazonaws.com",
            "eks.amazonaws.com"
          ]
        }
      }
    }
  ]
}
```

`iam:GetRole` is in its own statement because the `iam:PassedToService` condition key exists only in a `PassRole` request. Applying it to `iam:GetRole` in the same statement would prevent that permission from being granted at all.

This policy covers passing the roles only. It doesn't grant the Elastic Beanstalk actions that creating an application and an environment require.

Without these permissions, `CreateEnvironment` fails with an `AccessDenied` error naming the action it could not perform. For more information, see [Grant a principal permission to pass a role to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html) and [`CreateEnvironment`](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CreateEnvironment.html).

## Roles that Elastic Beanstalk manages
<a name="beanstalk-cluster-permissions-service-roles"></a>

Elastic Beanstalk operates a Beanstalk Cluster environment through the `AWSServiceRoleForElasticBeanstalk` service-linked role, which it creates in your account. You do not create, configure, or pass this role. Amazon EKS likewise uses its own service-linked role, `AWSServiceRoleForAmazonEKS`. For how Elastic Beanstalk uses service-linked roles, see [Using service-linked roles for Elastic Beanstalk](using-service-linked-roles.md).

## Confirm the roles that the environment uses
<a name="beanstalk-cluster-permissions-verify"></a>

After the environment reaches the `Ready` state, read its resolved configuration:

```
$ aws elasticbeanstalk describe-configuration-settings \
    --application-name my-app \
    --environment-name my-cluster-env \
    --query "ConfigurationSettings[0].OptionSettings[?OptionName=='cluster-role' || OptionName=='node-role' || OptionName=='observability-role'].[Namespace,OptionName,Value]" \
    --output table
```

Confirm that the cluster, node, and observability role entries contain the ARNs supplied during creation. If the environment uses an application role, run the credential-identity check in [Configure an application role](#beanstalk-cluster-permissions-application-role) and confirm that the returned ARN identifies the selected role. For a source-based application version, wait for the version to report `PROCESSED`; that state confirms that AWS CodeBuild could use the build role and complete the image build. See [Building container images for Beanstalk Cluster environments](beanstalk-cluster-app-versions.md).

## Application permissions
<a name="beanstalk-cluster-permissions-application"></a>

Use an application role when the running application must call AWS services. Configure the role before creating the environment and grant only the permissions required by the application. The application receives the role through Amazon EKS Pod Identity rather than through an Amazon EC2 instance profile.

Pass the role's ARN in the `application-role` setting of the `aws:elasticbeanstalk:eks:environment` namespace, or select the role in the Elastic Beanstalk console when you create the environment.

The application role is also the role that reads the credentials for a third-party observability backend. If you set any observability backend to `custom`, grant the application role `secretsmanager:GetSecretValue` and `secretsmanager:DescribeSecret` on the Secrets Manager secret named by `custom-credentials`. See [Sending observability data to a third-party backend](monitoring-cluster-environments.md#monitoring-cluster-environments-custom-backend).

### Configure an application role
<a name="beanstalk-cluster-permissions-application-role"></a>

Create the application role before you create the environment. Grant the role only the actions and resources that the application requires. Configure its trust policy for Amazon EKS Pod Identity, including `sts:AssumeRole` and `sts:TagSession` for the `pods.eks.amazonaws.com` service principal:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "pods.eks.amazonaws.com"
      },
      "Action": [
        "sts:AssumeRole",
        "sts:TagSession"
      ]
    }
  ]
}
```

1. Create the role with the preceding trust policy.

1. Attach an identity-based policy that grants only the service actions and resources required by the application.

1. In the Elastic Beanstalk console, start the environment creation workflow and expand **Service access**.

1. Choose the role under **Application role - optional**. Complete the remaining environment configuration, and then create the environment.

   With the AWS CLI or the API, choose the role by adding the `application-role` option to your `create-environment` request instead:

   ```
   --option-settings \
       Namespace=aws:elasticbeanstalk:eks:environment,OptionName=application-role,Value={{arn:aws:iam::111122223333:role/my-application-role}}
   ```

1. After the application is deployed, call the required AWS service from the application. To verify the credential identity independently of the service policy, call AWS STS `GetCallerIdentity` and confirm that the returned ARN identifies the selected application role.

If the application receives `AccessDenied`, verify that you selected the intended role during environment creation, that its trust policy allows Amazon EKS Pod Identity, and that its identity-based policy permits the requested action and resource. Correct the trust or permissions policy and repeat both the credential-identity check and the application service call. If the wrong role was selected, create a replacement environment with the intended role instead of adding application permissions to the wrong role. Use separate application roles when environments require different access. Do not grant application permissions to the cluster or node role.

## Diagnose role failures
<a name="beanstalk-cluster-permissions-diagnosis"></a>

Start with the Elastic Beanstalk events for the environment. Set `operation_start` to the timestamp recorded immediately before the failed request:

```
$ operation_start='{{timestamp-recorded-before-the-request}}'
$ aws elasticbeanstalk describe-events \
    --environment-name my-cluster-env \
    --severity ERROR \
    --start-time "$operation_start" \
    --max-items 20
```

Environment creation rejects an infrastructure role  
Confirm that the role is in the environment account, its trust policy and attached policies match the current Amazon EKS Auto Mode guidance, and its ARN is complete. If the requested subnet set already has a registered cluster, use its registered cluster and node roles. The operation error identifies conflicting requested and registered values. Correct the request and create the environment again. You cannot replace these roles on an existing environment.

The application image cannot be retrieved  
Verify that the node role has the documented Amazon ECR retrieval permissions and trust policy. Also verify the image URI and any repository policy that restricts access. Correct the role or repository policy, then deploy the application version again.

A source build reports `FAILED`  
Verify the build role in the application-version build configuration and inspect the build diagnostics. Correct the role trust or permissions policy before creating a new application version. See [Building container images for Beanstalk Cluster environments](beanstalk-cluster-app-versions.md).

The running application receives `AccessDenied`  
Use the application-role checks in [Configure an application role](#beanstalk-cluster-permissions-application-role). Confirm the credential identity first, then compare the denied action and resource in the application logs and CloudTrail event with the role policy.