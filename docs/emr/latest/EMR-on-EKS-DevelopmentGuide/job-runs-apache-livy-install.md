# Getting started with Apache Livy on Amazon EMR on EKS

Complete the following steps to install Apache Livy. They include configuring the package manager, creating a namespace for running Spark workloads, installing Livy, setting up
load balancing, and verification steps. You have to complete these steps in order to run a batch job with Spark.

1. If you haven't already, set up [Apache Livy for Amazon EMR on EKS](job-runs-apache-livy-setup.md "job-runs-apache-livy-setup.md").
2. Authenticate your Helm client to the Amazon ECR registry. You can find the corresponding
   `ECR-registry-account` value for your AWS Region from
   [Amazon ECR registry accounts by Region](docker-custom-images-tag.md#docker-custom-images-ECR "docker-custom-images-tag.md#docker-custom-images-ECR").

```
aws ecr get-login-password \--region `<AWS_REGION>` | helm registry login \
--username AWS \
--password-stdin `<ECR-registry-account>`.dkr.ecr.`<region-id>`.amazonaws.com
```

3. Setting up Livy creates a service account for the Livy server and another account for the Spark application. To set up
   IRSA for the service accounts, see [Setting up access permissions with IAM roles for service accounts (IRSA)](job-runs-apache-livy-irsa.md "job-runs-apache-livy-irsa.md").
4. Create a namespace to run your Spark workloads.

```
kubectl create ns `<spark-ns>`
```

5. Use the following command to install Livy.

This Livy endpoint is only internally available to the VPC in the EKS cluster. To enable access
beyond the VPC, set `—-set loadbalancer.internal=false` in your Helm installation command.

###### Note

By default, SSL is not enabled within this Livy endpoint and the endpoint is only visible inside the VPC of the EKS cluster. If you set
`loadbalancer.internal=false` and `ssl.enabled=false`, you are exposing an insecure endpointto outside of your VPC.
To set up a secure Livy endpoint, see [Configuring a secure Apache Livy endpoint with TLS/SSL](job-runs-apache-livy-secure-endpoint.md "job-runs-apache-livy-secure-endpoint.md").

```
helm install livy-demo \
  oci://895885662937.dkr.ecr.region-id.amazonaws.com/livy \
  --version 7.12.0 \
  --namespace livy-ns \
  --set image=ECR-registry-account.dkr.ecr.region-id.amazonaws.com/livy/emr-7.12.0:latest \
  --set sparkNamespace=`<spark-ns>` \
  --create-namespace
```

You should see the following output.

```
NAME: livy-demo
LAST DEPLOYED: Mon Mar 18 09:23:23 2024
NAMESPACE: livy-ns
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
The Livy server has been installed.
Check installation status:
1. Check Livy Server pod is running
  kubectl --namespace livy-ns get pods -l "app.kubernetes.io/instance=livy-demo"
2. Verify created NLB is in Active state and it's target groups are healthy (if loadbalancer.enabled is true)

Access LIVY APIs:
    # Ensure your NLB is active and healthy
    # Get the Livy endpoint using command:
    LIVY_ENDPOINT=$(kubectl get svc -n livy-ns -l app.kubernetes.io/instance=livy-demo,emr-containers.amazonaws.com/type=loadbalancer -o jsonpath='{.items[0].status.loadBalancer.ingress[0].hostname}' |  awk '{printf "%s:8998\n", $0}')
    # Access Livy APIs using http://$LIVY_ENDPOINT or https://$LIVY_ENDPOINT (if SSL is enabled)
    # Note: While uninstalling Livy, makes sure the ingress and NLB are deleted after running the helm command to avoid dangling resources
```

The default service account names for the Livy server and the Spark session are `emr-containers-sa-livy` and
`emr-containers-sa-spark-livy`. To use custom names,
use the `serviceAccounts.name` and `sparkServiceAccount.name` parameters.

```
--set serviceAccounts.name=my-service-account-for-livy
--set sparkServiceAccount.name=my-service-account-for-spark
```

6. Verify that you installed the Helm chart.

```
helm list -n livy-ns -o yaml
```

The `helm list` command should return information about your new Helm chart.

```
app_version: 0.7.1-incubating
chart: livy-emr-7.12.0
name: livy-demo
namespace: livy-ns
revision: "1"
status: deployed
updated: 2024-02-08 22:39:53.539243 -0800 PST
```

7. Verify that the Network Load Balancer is active.

```
LIVY_NAMESPACE=`<livy-ns>`
LIVY_APP_NAME=`<livy-app-name>`
AWS_REGION=`<AWS_REGION>`

# Get the NLB Endpoint URL
NLB_ENDPOINT=$(kubectl --namespace $LIVY_NAMESPACE get svc -l "app.kubernetes.io/instance=$LIVY_APP_NAME,emr-containers.amazonaws.com/type=loadbalancer" -o jsonpath='{.items[0].status.loadBalancer.ingress[0].hostname}')

# Get all the load balancers in the account's region
ELB_LIST=$(aws elbv2 describe-load-balancers --region $AWS_REGION)

# Get the status of the NLB that matching the endpoint from the Kubernetes service
NLB_STATUS=$(echo $ELB_LIST | grep -A 8 "\"DNSName\": \"$NLB_ENDPOINT\"" | awk '/Code/{print $2}/}/' | tr -d '"},\n')
echo $NLB_STATUS
```

8. Now verify that the target group in the Network Load Balancer is healthy.

```
LIVY_NAMESPACE=`<livy-ns>`
LIVY_APP_NAME=`<livy-app-name>`
AWS_REGION=`<AWS_REGION>`

# Get the NLB endpoint
NLB_ENDPOINT=$(kubectl --namespace $LIVY_NAMESPACE get svc -l "app.kubernetes.io/instance=$LIVY_APP_NAME,emr-containers.amazonaws.com/type=loadbalancer" -o jsonpath='{.items[0].status.loadBalancer.ingress[0].hostname}')

# Get all the load balancers in the account's region
ELB_LIST=$(aws elbv2 describe-load-balancers --region $AWS_REGION)

# Get the NLB ARN from the NLB endpoint
NLB_ARN=$(echo $ELB_LIST | grep -B 1 "\"DNSName\": \"$NLB_ENDPOINT\"" | awk '/"LoadBalancerArn":/,/"/'| awk '/:/{print $2}' | tr -d \",)

# Get the target group from the NLB. Livy setup only deploys 1 target group
TARGET_GROUP_ARN=$(aws elbv2 describe-target-groups --load-balancer-arn $NLB_ARN --region $AWS_REGION | awk '/"TargetGroupArn":/,/"/'| awk '/:/{print $2}' | tr -d \",)

# Get health of target group
aws elbv2 describe-target-health --target-group-arn $TARGET_GROUP_ARN
```

The following is sample output that shows the status of the target group:

```
{
    "TargetHealthDescriptions": [
        {
            "Target": {
                "Id": "`<target IP>`",
                "Port": 8998,
                "AvailabilityZone": "`us-west-2d`"
            },
            "HealthCheckPort": "8998",
            "TargetHealth": {
                "State": "healthy"
            }
        }
    ]
}
```

Once the status of your NLB becomes `active` and your target group is `healthy`, you can continue.
It might take a few minutes. 9. Retrieve the Livy endpoint from the Helm installation. Whether or not your Livy endpoint is secure depends on whether you enabled SSL.

```
LIVY_NAMESPACE=`<livy-ns>`
 LIVY_APP_NAME=`livy-app-name`
 LIVY_ENDPOINT=$(kubectl get svc -n livy-ns -l app.kubernetes.io/instance=`livy-app-name`,emr-containers.amazonaws.com/type=loadbalancer -o jsonpath='{.items[0].status.loadBalancer.ingress[0].hostname}' |  awk '{printf "%s:8998\n", $0}')
 echo "$LIVY_ENDPOINT"

```

10. Retrieve the Spark service account from the Helm installation

```
SPARK_NAMESPACE=spark-ns
LIVY_APP_NAME=`<livy-app-name>`
SPARK_SERVICE_ACCOUNT=$(kubectl --namespace $SPARK_NAMESPACE get sa -l "app.kubernetes.io/instance=$LIVY_APP_NAME" -o jsonpath='{.items[0].metadata.name}')
echo "$SPARK_SERVICE_ACCOUNT"
```

You should see something similar to the following output:

```
emr-containers-sa-spark-livy
```

11. If you set `internalALB=true` to enable access from outside of your VPC, create an Amazon EC2 instance
    and make sure the Network Load Balancer allows network traffic coming from the EC2 instance. You must do so for the instance
    to have access to your Livy endpoint. For more information about securely exposing your endpoint outside of your VPC,
    see [Setting up with a secure Apache Livy
    endpoint with TLS/SSL](job-runs-apache-livy-secure-endpoint.md "job-runs-apache-livy-secure-endpoint.md").
12. Installing Livy creates the service account `emr-containers-sa-spark` to run Spark applications. If
    your Spark application uses any AWS resources like S3 or calls AWS API or CLI operations, you must link an
    IAM role with the necessary permissions to your spark service account. For more information, see
    [Setting up access permissions with IAM roles for service accounts (IRSA).](job-runs-apache-livy-irsa.md "job-runs-apache-livy-irsa.md")
    Apache Livy supports additional configurations that you can use while installing Livy. For more information, see
    Installation properties for Apache Livy on Amazon EMR on EKS releases.
