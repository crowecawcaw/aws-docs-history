

# Getting started with Beanstalk Cluster
<a name="beanstalk-cluster-getting-started"></a>

In this tutorial, you create an Elastic Beanstalk application and a Beanstalk Cluster environment. You omit the application version so that Elastic Beanstalk deploys its prebuilt sample container image. You then wait for the environment to become ready, retrieve its URL, and terminate it. Alternatively, you can get started in the AWS Management Console, which provides a fully guided experience, or point your AI agent at the [Beanstalk Cluster](beanstalk-cluster.md) documentation.

Estimated duration: **15–20 minutes**

**Important**  
There is no additional charge for Elastic Beanstalk, but you pay for the AWS resources that the environment uses, including Amazon EKS and its compute. For more information, see [Elastic Beanstalk Pricing](https://aws.amazon.com/elasticbeanstalk/pricing/). Complete the cleanup steps when you finish this tutorial.

## Before you begin
<a name="beanstalk-cluster-getting-started-prerequisites"></a>

Complete the following prerequisites:
+ Install and configure the AWS CLI. For instructions, see [Get started with the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS Command Line Interface User Guide*.
+ Use an IAM principal that can create and manage Elastic Beanstalk applications and environments, and that can pass the cluster, node, and observability roles when creating an environment. For the exact permissions, see [Permissions to create the environment](beanstalk-cluster-permissions.md#beanstalk-cluster-permissions-caller).
+ Create the cluster role that Amazon EKS assumes, the node role that the cluster's Amazon EC2 nodes assume, and the observability role that publishes the environment's metrics, logs, and traces, as described in [Create the IAM roles](#beanstalk-cluster-getting-started-roles). To choose the VPC subnets that the environment uses, see [Configuring networking for Beanstalk Cluster environments](configuring-cluster-networking.md).
+ Choose an AWS Region in which Beanstalk Cluster is available. The commands use the Region from your AWS CLI configuration.

## Create the IAM roles
<a name="beanstalk-cluster-getting-started-roles"></a>

A Beanstalk Cluster environment needs three IAM roles that you provide: a cluster role, a node role, and an observability role. The Elastic Beanstalk console creates them for you, but this tutorial uses the AWS CLI, so create them first. Use these names, because the console selects existing roles by name. For what each role is for, and for the caller permissions you need to pass them, see [Permissions for Beanstalk Cluster](beanstalk-cluster-permissions.md).

**To create the cluster, node, and observability roles**

1. Create a trust policy file for each service that assumes a role. The cluster role trusts Amazon EKS, the node role trusts Amazon EC2, and the observability role trusts Amazon EKS Pod Identity.

   ```
   $ cat > eks-trust.json <<'EOF'
   {
     "Version": "2012-10-17",
     "Statement": [{
       "Effect": "Allow",
       "Principal": {"Service": "eks.amazonaws.com"},
       "Action": ["sts:AssumeRole", "sts:TagSession"]
     }]
   }
   EOF
   ```

   ```
   $ cat > ec2-trust.json <<'EOF'
   {
     "Version": "2012-10-17",
     "Statement": [{
       "Effect": "Allow",
       "Principal": {"Service": "ec2.amazonaws.com"},
       "Action": "sts:AssumeRole"
     }]
   }
   EOF
   ```

   ```
   $ cat > pods-trust.json <<'EOF'
   {
     "Version": "2012-10-17",
     "Statement": [{
       "Effect": "Allow",
       "Principal": {"Service": "pods.eks.amazonaws.com"},
       "Action": ["sts:AssumeRole", "sts:TagSession"]
     }]
   }
   EOF
   ```

1. Create the cluster role and attach its policies.

   ```
   $ aws iam create-role \
       --role-name aws-elasticbeanstalk-eks-cluster-role \
       --assume-role-policy-document file://eks-trust.json
   $ for p in AmazonEKSClusterPolicy AmazonEKSNetworkingPolicy AmazonEKSComputePolicy \
            AmazonEKSBlockStoragePolicy AmazonEKSLoadBalancingPolicy AWSElasticBeanstalkEKSTagging; do
       aws iam attach-role-policy \
           --role-name aws-elasticbeanstalk-eks-cluster-role \
           --policy-arn arn:aws:iam::aws:policy/$p
   done
   ```

1. Create the node role and attach its policies.

   ```
   $ aws iam create-role \
       --role-name aws-elasticbeanstalk-eks-node-role \
       --assume-role-policy-document file://ec2-trust.json
   $ for p in AmazonEKSWorkerNodeMinimalPolicy AmazonEC2ContainerRegistryPullOnly \
            AmazonSSMManagedInstanceCore; do
       aws iam attach-role-policy \
           --role-name aws-elasticbeanstalk-eks-node-role \
           --policy-arn arn:aws:iam::aws:policy/$p
   done
   ```

1. Create the observability role and attach its policies.

   ```
   $ aws iam create-role \
       --role-name aws-elasticbeanstalk-eks-observability-role \
       --assume-role-policy-document file://pods-trust.json
   $ for p in CloudWatchAgentServerPolicy AWSElasticBeanstalkEKSObservability; do
       aws iam attach-role-policy \
           --role-name aws-elasticbeanstalk-eks-observability-role \
           --policy-arn arn:aws:iam::aws:policy/$p
   done
   ```

1. Record the three role ARNs. You pass them when you create the environment.

   ```
   $ for r in cluster node observability; do
       aws iam get-role --role-name aws-elasticbeanstalk-eks-$r-role \
           --query 'Role.Arn' --output text
   done
   ```

## Choose a supported provisioning tool
<a name="beanstalk-cluster-getting-started-tools"></a>

You can create and manage a Beanstalk Cluster environment with the Elastic Beanstalk console, the Elastic Beanstalk API, or the AWS CLI. This tutorial uses the AWS CLI so that each request is visible and repeatable.

You can also deploy with the official GitHub Action, and you can define your environments as infrastructure as code with Terraform through the AWS provider. For the GitHub Action, see [Using GitHub Actions to deploy to Elastic Beanstalk](deploying-github-actions.md).

## Create the application and deploy the sample
<a name="beanstalk-cluster-getting-started-deploy"></a>

1. Create an Elastic Beanstalk application to contain the environment.

   ```
   $ aws elasticbeanstalk create-application \
       --application-name getting-started-cluster-app
   ```

1. Create the environment. The `Cluster` tier selects Beanstalk Cluster. Because this request has no version label, Elastic Beanstalk deploys the sample application.

   ```
   $ aws elasticbeanstalk create-environment \
       --application-name getting-started-cluster-app \
       --environment-name getting-started-cluster-env \
       --tier Name=Cluster,Type=EKS \
       --option-settings \
           Namespace=aws:elasticbeanstalk:eks,OptionName=cluster-role,Value={{cluster-role-arn}} \
           Namespace=aws:elasticbeanstalk:eks,OptionName=node-role,Value={{node-role-arn}} \
           Namespace=aws:elasticbeanstalk:eks:environment,OptionName=observability-role,Value={{observability-role-arn}}
   ```

   Replace the role ARN placeholders with the roles that you prepared. The request omits `service-port` and `load-balancer-type`. Elastic Beanstalk resolves those settings to their defaults, `8080` and `ALB`. To choose different values, pass them with `--option-settings`. For the complete option reference, see [Configuration options for Beanstalk Cluster environments](command-options-general-eks.md).

1. Wait for the environment to become ready. A first environment can take 15 to 20 minutes while Elastic Beanstalk creates the Amazon EKS cluster and deploys the sample. The AWS CLI provides a built-in waiter that polls until the environment reports `Ready`. The waiter polls at most 20 times at 20-second intervals, about 6 minutes 40 seconds, so on a first environment expect it to report `Max attempts exceeded`. Run it again until it reports success.

   ```
   $ aws elasticbeanstalk wait environment-exists \
       --environment-names getting-started-cluster-env
   ```

   The waiter reports `Max attempts exceeded` both when the environment is still being created and when creation has failed. If it does not report success after a few runs, inspect the environment's recent events and resolve the reported error before continuing.

   ```
   $ aws elasticbeanstalk describe-events \
       --environment-name getting-started-cluster-env \
       --query 'Events[].[EventDate,Severity,Message]' \
       --output table
   ```

1. Inspect the environment status, health color, health status, and URL.

   ```
   $ aws elasticbeanstalk describe-environments \
       --application-name getting-started-cluster-app \
       --environment-names getting-started-cluster-env \
       --query 'Environments[0].[Status,Health,HealthStatus,CNAME]' \
       --output table
   ```

   Confirm that the environment reports `Ready` and returns a nonempty `CNAME`. Open `https://` followed by the CNAME in a web browser and confirm that the sample application responds. The load balancer answers on HTTPS only, so a request to `http://` waits until it times out. To accept HTTP requests and have Elastic Beanstalk redirect them to HTTPS, see [Configuring networking for Beanstalk Cluster environments](configuring-cluster-networking.md). An idle environment can initially report `Grey` and `NoData` because it has received too few requests to determine application health; health events display this status as `No Data`. This does not indicate a failed deployment. After the application receives enough successful requests, health normally moves to `Green` and `Ok`. If the CNAME is empty, the application does not respond, or health reports a failure, inspect the environment's recent events before continuing:

   ```
   $ aws elasticbeanstalk describe-events \
       --environment-name getting-started-cluster-env \
       --query 'Events[].[EventDate,Severity,Message]' \
       --output table
   ```

   For the Cluster health model, see [Monitoring Beanstalk Cluster environments](monitoring-cluster-environments.md).

## Deploy your own container image
<a name="beanstalk-cluster-getting-started-deploy-own"></a>

The environment is running the sample application because the create request carried no version label. To run your own application, create an *application version* that names your container image, then deploy that version to the environment. This is the normal Elastic Beanstalk flow: an application version is the deployable artifact, and the sample is what Elastic Beanstalk deploys when you don't supply one.

Before you start, you need a container image that you have already pushed to a registry, such as an Amazon Elastic Container Registry (Amazon ECR) repository in your account, and the image must listen on the environment's `service-port`, which is `8080` unless you changed it. Deploying your own version replaces the sample application. To have Elastic Beanstalk build the image from your source instead, and for the build options, see [Building container images for Beanstalk Cluster environments](beanstalk-cluster-app-versions.md).

1. Create an application version that points at your image.

   ```
   $ aws elasticbeanstalk create-application-version \
       --application-name getting-started-cluster-app \
       --version-label v1 \
       --image-configuration Source={Uri={{your-image-uri}}}
   ```

   Replace {{your-image-uri}} with your image, for example `111122223333.dkr.ecr.us-east-1.amazonaws.com/my-app:v1`. Because the image is already built, the version needs no build step and is ready to deploy.

1. Deploy the version to the environment.

   ```
   $ aws elasticbeanstalk update-environment \
       --environment-name getting-started-cluster-env \
       --version-label v1
   ```

1. Confirm that the deployment finished and the environment is serving your application.

   ```
   $ aws elasticbeanstalk describe-events \
       --environment-name getting-started-cluster-env \
       --query 'Events[].[EventDate,Severity,Message]' \
       --output table
   ```

   Open `https://` followed by the environment's CNAME in a web browser and confirm that your application responds. If it doesn't, check the events for a deployment failure, and confirm that the image listens on the environment's `service-port`.

## Clean up the tutorial resources
<a name="beanstalk-cluster-getting-started-cleanup"></a>

1. Terminate the environment.

   ```
   $ aws elasticbeanstalk terminate-environment \
       --environment-name getting-started-cluster-env
   ```

1. Wait for the environment to reach the `Terminated` status. The AWS CLI provides a built-in waiter that polls until termination completes. This waiter has the same 20-attempt limit, so run it again until it reports success.

   ```
   $ aws elasticbeanstalk wait environment-terminated \
       --environment-names getting-started-cluster-env
   ```

   The waiter reports `Max attempts exceeded` both when termination is still in progress and when it has failed. If it does not report success after a few runs, resolve the error in the environment's events. Do not delete the application while the environment still exists.

1. Delete the application and its application versions, including the sample version that Elastic Beanstalk created and any version that you added. This does not delete a container image that you supplied or the repository that holds it; see [Building container images for Beanstalk Cluster environments](beanstalk-cluster-app-versions.md).

   ```
   $ aws elasticbeanstalk delete-application \
       --application-name getting-started-cluster-app
   ```

Elastic Beanstalk deletes a shared Amazon EKS cluster only after you terminate the last environment that uses it. Cluster deletion can take up to three hours; Amazon EKS and other resource charges continue until deletion completes. Termination does not delete the customer-provided cluster, node, and observability IAM roles. Verify cluster deletion as described in [Cluster deletion](beanstalk-cluster-concepts.md#beanstalk-cluster-clusters-lifecycle).

## Next steps
<a name="beanstalk-cluster-getting-started-next"></a>
+ Deploy your own container image or source by creating an application version. See [Building container images for Beanstalk Cluster environments](beanstalk-cluster-app-versions.md).
+ Configure resource limits, scaling, deployment behavior, load balancing, and observability. See [Configuration options for Beanstalk Cluster environments](command-options-general-eks.md).
+ Learn how to update and monitor the environment. See [Managing Elastic Beanstalk environments](using-features.managing.md) and [Monitoring Beanstalk Cluster environments](monitoring-cluster-environments.md).