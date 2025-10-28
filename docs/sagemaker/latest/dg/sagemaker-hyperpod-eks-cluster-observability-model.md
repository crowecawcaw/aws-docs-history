# Model observability

for training jobs on SageMaker HyperPod clusters orchestrated by Amazon EKS

SageMaker HyperPod clusters orchestrated with Amazon EKS can integrate with the [MLflow application on
Amazon SageMaker Studio](mlflow.md "mlflow.md"). Cluster admins set up the MLflow server and connect it with
the SageMaker HyperPod clusters. Data scientists can gain insights into the model.

**To set up an MLflow server using AWS CLI**

A cluster admin must create an MLflow tracking server.

1. Create a SageMaker AI MLflow tracking server, following the instructions at [Create a tracking server using the AWS CLI](mlflow-create-tracking-server-cli.md#mlflow-create-tracking-server-cli-infra-setup "mlflow-create-tracking-server-cli.md#mlflow-create-tracking-server-cli-infra-setup").
2. Make sure that the [`eks-auth:AssumeRoleForPodIdentity`](../../../eks/latest/APIReference/API_auth_AssumeRoleForPodIdentity.md "../../../eks/latest/APIReference/API_auth_AssumeRoleForPodIdentity.md") permission
   exists in the IAM execution role for SageMaker HyperPod.
3. If the `eks-pod-identity-agent` add-on is not already installed on
   your EKS cluster, install the add-on on the EKS cluster.

```
aws eks create-addon \
    --cluster-name `<eks_cluster_name>` \
    --addon-name eks-pod-identity-agent \
    --addon-version `vx.y.z-eksbuild.1`
```

4. Create a `trust-relationship.json` file for a new role for Pod to
   call MLflow APIs.

```
cat >trust-relationship.json <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowEksAuthToAssumeRoleForPodIdentity",
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
EOF
```

Run the following code to create the role and attach the trust
relationship.

```
aws iam create-role --role-name `hyperpod-mlflow-role` \
    --assume-role-policy-document file://trust-relationship.json \
    --description "allow pods to emit mlflow metrics and put data in s3"
```

5. Create the following policy that grants Pod access to call all
   `sagemaker-mlflow` operations and to put model artifacts in S3.
   S3 permission already exists within the tracking server but if the model
   artifacts is too big direct call to s3 is made from the MLflow code to upload
   the artifacts.

```
cat >hyperpod-mlflow-policy.json <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sagemaker-mlflow:AccessUI",
                "sagemaker-mlflow:CreateExperiment",
                "sagemaker-mlflow:SearchExperiments",
                "sagemaker-mlflow:GetExperiment",
                "sagemaker-mlflow:GetExperimentByName",
                "sagemaker-mlflow:DeleteExperiment",
                "sagemaker-mlflow:RestoreExperiment",
                "sagemaker-mlflow:UpdateExperiment",
                "sagemaker-mlflow:CreateRun",
                "sagemaker-mlflow:DeleteRun",
                "sagemaker-mlflow:RestoreRun",
                "sagemaker-mlflow:GetRun",
                "sagemaker-mlflow:LogMetric",
                "sagemaker-mlflow:LogBatch",
                "sagemaker-mlflow:LogModel",
                "sagemaker-mlflow:LogInputs",
                "sagemaker-mlflow:SetExperimentTag",
                "sagemaker-mlflow:SetTag",
                "sagemaker-mlflow:DeleteTag",
                "sagemaker-mlflow:LogParam",
                "sagemaker-mlflow:GetMetricHistory",
                "sagemaker-mlflow:SearchRuns",
                "sagemaker-mlflow:ListArtifacts",
                "sagemaker-mlflow:UpdateRun",
                "sagemaker-mlflow:CreateRegisteredModel",
                "sagemaker-mlflow:GetRegisteredModel",
                "sagemaker-mlflow:RenameRegisteredModel",
                "sagemaker-mlflow:UpdateRegisteredModel",
                "sagemaker-mlflow:DeleteRegisteredModel",
                "sagemaker-mlflow:GetLatestModelVersions",
                "sagemaker-mlflow:CreateModelVersion",
                "sagemaker-mlflow:GetModelVersion",
                "sagemaker-mlflow:UpdateModelVersion",
                "sagemaker-mlflow:DeleteModelVersion",
                "sagemaker-mlflow:SearchModelVersions",
                "sagemaker-mlflow:GetDownloadURIForModelVersionArtifacts",
                "sagemaker-mlflow:TransitionModelVersionStage",
                "sagemaker-mlflow:SearchRegisteredModels",
                "sagemaker-mlflow:SetRegisteredModelTag",
                "sagemaker-mlflow:DeleteRegisteredModelTag",
                "sagemaker-mlflow:DeleteModelVersionTag",
                "sagemaker-mlflow:DeleteRegisteredModelAlias",
                "sagemaker-mlflow:SetRegisteredModelAlias",
                "sagemaker-mlflow:GetModelVersionByAlias"
            ],
            "Resource": "`arn:aws:sagemaker:us-west-2:111122223333:mlflow-tracking-server/<ml tracking server name>`"
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:PutObject"
            ],
            "Resource": "`arn:aws:s3:::<mlflow-s3-bucket_name>`"
        }
    ]
}
EOF
```

###### Note

The ARNs are the one from the MLflow server and the S3 bucket set up with
the MLflow server during the server you created following the instructions
[Set up MLflow infrastructure](mlflow-create-tracking-server-cli.md#mlflow-create-tracking-server-cli-infra-setup "mlflow-create-tracking-server-cli.md#mlflow-create-tracking-server-cli-infra-setup"). 6. Attach the `mlflow-metrics-emit-policy` policy to the
`hyperpod-mlflow-role` using the policy document saved in the
previous step.

```
aws iam put-role-policy \
  --role-name `hyperpod-mlflow-role` \
  --policy-name `mlflow-metrics-emit-policy` \
  --policy-document `file://hyperpod-mlflow-policy.json`
```

7. Create a Kubernetes service account for Pod to access the MLflow server.

```
cat >`mlflow-service-account.yaml` <<EOF
apiVersion: v1
kind: ServiceAccount
metadata:
  name: `mlflow-service-account`
  namespace: `kubeflow`
EOF
```

Run the following command to apply to the EKS cluster.

```
kubectl apply -f `mlflow-service-account.yaml`
```

8. Create a Pod identity association.

```
aws eks create-pod-identity-association \
    --cluster-name `EKS_CLUSTER_NAME` \
    --role-arn `arn:aws:iam::111122223333:role/hyperpod-mlflow-role` \
    --namespace `kubeflow` \
    --service-account `mlflow-service-account`
```

**To collect metrics from training jobs to the MLflow
server**

Data scientists need to set up the training script and docker image to emit metrics to
the MLflow server.

1. Add the following lines at the beginning of your training script.

```
import mlflow

# Set the Tracking Server URI using the ARN of the Tracking Server you created
mlflow.set_tracking_uri(os.environ['MLFLOW_TRACKING_ARN'])
# Enable autologging in MLflow
mlflow.autolog()
```

2. Build a Docker image with the training script and push to Amazon ECR. Get the
   ARN of the ECR container. For more information about building and pushing a
   Docker image, see [Pushing a Docker
   image](../../../AmazonECR/latest/userguide/docker-push-ecr-image.md "../../../AmazonECR/latest/userguide/docker-push-ecr-image.md") in the _ECR User Guide_.

###### Tip

Make sure that you add installation of mlflow and sagemaker-mlflow
packages in the Docker file. To learn more about the installation of the
packages, requirements, and compatible versions of the packages, see [Install MLflow and the SageMaker AI MLflow plugin](mlflow-track-experiments.md#mlflow-track-experiments-install-plugin "mlflow-track-experiments.md#mlflow-track-experiments-install-plugin"). 3. Add a service account in the training job Pods to give them access to
`hyperpod-mlflow-role`. This allows Pods to call MLflow APIs. Run
the following SageMaker HyperPod CLI job submission template. Create this with file
name `mlflow-test.yaml`.

```
defaults:
 - override hydra/job_logging: stdout

hydra:
 run:
  dir: .
 output_subdir: null

training_cfg:
 entry_script: `./train.py`
 script_args: []
 run:
  name: `test-job-with-mlflow` # Current run name
  nodes: `2` # Number of nodes to use for current training
  # ntasks_per_node: `1` # Number of devices to use per node
cluster:
 cluster_type: k8s # currently k8s only
 instance_type: `ml.c5.2xlarge`
 cluster_config:
  # name of service account associated with the namespace
  **service\_account\_name: `mlflow-service-account`**
  # persistent volume, usually used to mount FSx
  persistent_volume_claims: null
  namespace: `kubeflow`
  # required node affinity to select nodes with SageMaker HyperPod
  # labels and passed health check if burn-in enabled
  label_selector:
      required:
          sagemaker.amazonaws.com/node-health-status:
              - Schedulable
      preferred:
          sagemaker.amazonaws.com/deep-health-check-status:
              - Passed
      weights:
          - 100
  pullPolicy: IfNotPresent # policy to pull container, can be Always, IfNotPresent and Never
  restartPolicy: OnFailure # restart policy

base_results_dir: ./result # Location to store the results, checkpoints and logs.
container: `111122223333.dkr.ecr.us-west-2.amazonaws.com/tag` # container to use

env_vars:
 NCCL_DEBUG: INFO # Logging level for NCCL. Set to "INFO" for debug information
 **MLFLOW\_TRACKING\_ARN: `arn:aws:sagemaker:us-west-2:11112223333:mlflow-tracking-server/tracking-server-name`**
```

4. Start the job using the YAML file as follows.

```
hyperpod start-job --config-file `/path/to/mlflow-test.yaml`
```

5. Generate a pre-signed URL for the MLflow tracking server. You can open the
   link on your browser and start tracking your training job.

```
aws sagemaker create-presigned-mlflow-tracking-server-url \
    --tracking-server-name "`tracking-server-name`" \
    --session-expiration-duration-in-seconds `1800` \
    --expires-in-seconds `300` \
    --region `region`
```
