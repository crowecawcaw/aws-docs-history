# (Optional) Try out Application Signals with a sample app

To try out CloudWatch Application Signals on a sample app before you instrument your own
applications with it, follow the instructions in this section. These instructions use
scripts to help you create an Amazon EKS cluster, install a sample application, and instrument
the sample application to work with Application Signals.

The sample application is a Spring "Pet Clinic" application that is composed of four
microservices. These services run on Amazon EKS on Amazon EC2 and leverage Application Signals
enablement scripts to enable the cluster with the Java, Python, or .NET auto-instrumentation
agent.

**Requirements**

- Application Signals monitors only Java, Python, or .NET applications.
- You must have the AWS CLI installed on the instance. We recommend AWS CLI version 2, but version 1
  should also work. For more information about installing the AWS CLI, see
  [Install or update the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").
- The scripts in this section are intended to be run in Linux and macOS environments. For
  Windows instances, we recommend that you use an AWS Cloud9 environment to run
  these scripts. For more information about AWS Cloud9, see [What is
  AWS Cloud9?](../../../cloud9/latest/user-guide/welcome.md "../../../cloud9/latest/user-guide/welcome.md").
- Install a supported version of `kubectl`. You must use a version of `kubectl`
  within one minor version difference of your Amazon EKS cluster control plane. For example, a 1.26 `kubectl` client
  works with Kubernetes 1.25, 1.26, and 1.27 clusters. If you already have an Amazon EKS cluster, you might
  need to configure AWS credentials for `kubectl`. For more information, see
  [Creating or updating a `kubeconfig` file for an Amazon EKS cluster](../../../eks/latest/userguide/create-kubeconfig.md "../../../eks/latest/userguide/create-kubeconfig.md").
- Install `eksctl`. `eksctl` uses the AWS CLI to interact with AWS, which
  means it uses the same AWS credentials as the AWS CLI. For more information, see [Installing or updating
  `eksctl`](../../../eks/latest/userguide/eksctl.md "../../../eks/latest/userguide/eksctl.md").
- Install `jq`. `jq` is required to run the Application Signals enablement
  scripts. For more information, see [Download jq](https://jqlang.github.io/jq/download/ "https://jqlang.github.io/jq/download/").

## Step 1: Download the scripts

To download the scripts to set up CloudWatch Application Signals with a sample app,
you can download and uncompress the zipped GitHub project file to a local drive,
or you can clone the GitHub project.

To clone the project, open a terminal window and enter the following Git command in a given working directory.

```
git clone https://github.com/aws-observability/application-signals-demo.git
```

## Step 2: Build and deploy the sample application

To build and push the sample application images,
[follow these instructions](https://github.com/aws-observability/application-signals-demo?tab=readme-ov-file#build-the-sample-application-images-and-push-to-ecr "https://github.com/aws-observability/application-signals-demo?tab=readme-ov-file#build-the-sample-application-images-and-push-to-ecr").

### Step 3: Deploy and enable Application Signals and the sample application

Be sure that you have completed the requirements listed in [(Optional) Try out Application Signals with a sample app](CloudWatch-Application-Signals-Enable-EKS-sample.md "CloudWatch-Application-Signals-Enable-EKS-sample.md") before you complete the
following steps.

###### To deploy and enable Application Signals and the sample application

1. Enter the following command.
   Replace `new-cluster-name` with the name that you want to use
   for the new cluster. Replace `region-name` with the name of
   the AWS Region, such as `us-west-1`.

This command sets up the sample app running in a new Amazon EKS cluster with Application Signals enabled.

```
# this script sets up a new cluster, enables Application Signals, and deploys the
# sample application
cd application-signals-demo/scripts/eks/appsignals/one-step && ./setup.sh `new-cluster-name` `region-name`
```

The setup script takes about 30 minutes to run, and does the following:

    * Creates a new Amazon EKS cluster in the specified Region.
    * Creates the necessary IAM permissions for Application Signals
     (`arn:aws:iam::aws:policy/AWSXrayWriteOnlyAccess` and `arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy`).
    * Enables Application Signals by installing the CloudWatch agent and Auto-instrumenting the sample
     application for CloudWatch metrics and X-Ray traces.
    * Deploys the PetClinic Spring sample application in the same Amazon EKS cluster.
    * Creates five CloudWatch Synthetics canaries, named `pc-add-vist`, `pc-create-owners`,
     `pc-visit-pet`, `pc-visit-vet`, `pc-clinic-traffic`. These canaries will run at a
     one-minute frequency to generate synthetic traffic for the sample app and demonstrate how Synthetics canaries appear in Application
     Signals.
    * Creates four service level objectives (SLOs) for the PetClinic application with the following names:




    	+ **Availability for Searching an Owner**
    	+ **Latency for Searching an Owner**
    	+ **Availability for Registering an Owner**
    	+ **Latency for Registering an Owner**
    * Creates the required IAM role with a custom trust policy granting Application Signals the following permissions:




    	+ `cloudwatch:PutMetricData`
    	+ `cloudwatch:GetMetricData`
    	+ `xray:GetServiceGraph`
    	+ `logs:StartQuery`
    	+ `logs:GetQueryResults`

2. (Optional) If you want to review the source code for the PetClinic sample application, you can
   find them under the root folder.

```
- application-signals-demo
  - spring-petclinic-admin-server
  - spring-petclinic-api-gateway
  - spring-petclinic-config-server
  - spring-petclinic-customers-service
  - spring-petclinic-discovery-server
  - spring-petclinic-vets-service
  - spring-petclinic-visits-service
```

3. To view the deployed PetClinic sample application, run the following command to find the URL:

```
kubectl get ingress
```

### Step 4: Monitor the sample application

After completing the steps in the previous section to create the Amazon EKS cluster and deploy the sample
application, you can use Application Signals to monitor the application.

###### Note

For the Application Signals console to start populating, some traffic must reach the sample
application. Part of the previous steps created CloudWatch Synthetics canaries that generate
traffic to the sample application.

#### Service health monitoring

After it is enabled, CloudWatch Application Signals automatically discovers and populates a list of services without requiring any
additional setup.

###### To view the list of discovered services and monitor their health

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Application Signals**, **Services**.
3. To view a service, its operations, and its dependencies, choose the name of one of the
   services in the list.

This unified, application-centric view helps provide a full perspective of how
users are interacting with your service. This can help you triage issues if
performance anomalies occur. For complete details about the
**Services** view, see [Monitor the operational health of your applications with Application Signals](Services.md "Services.md"). 4. Choose the **Service Operations** tab to see the standard application metrics
for that service's operations. The operations are the API operations that the
service calls, for example.

Then, to view the graphs for a single operation of that service, choose that operation name. 5. Choose the **Dependencies** tab to see the dependencies that your application has, along
with the critical application metrics for each dependency. Dependencies include AWS services and third-party
services that your application calls. 6. To view correlated traces from the service details page, choose a data point in one of the
three graphs above the table. This populates a new pane with filtered traces from
the time period. These traces are sorted and filtered based on the graph that you
chose. For example, if you chose the **Latency** graph, the traces
are sorted by service response time. 7. In the CloudWatch console navigation pane, choose **SLOs**. You see the SLOs that
the script created for the sample application. For more information about SLOs, see
[Service level objectives (SLOs)](CloudWatch-ServiceLevelObjectives.md "CloudWatch-ServiceLevelObjectives.md").

### (Optional) Step 5: Cleanup

When you're finished testing Application signals, you can use a script provided by Amazon
to clean up and delete the artifacts created in your account for the
sample application. To perform the cleanup, enter the following command. Replace
`new-cluster-name` with the name of the cluster that you created for
the sample app, and replace `region`-name with the name of the AWS Region, such
as `us-west-1`.

```
cd application-signals-demo/scripts/eks/appsignals/one-step && ./cleanup.sh new-cluster-name region-name
```
