# Starting an evaluation job

The following provides a suggested evaluation instance type and model type
configuration:

```
# Install Dependencies (Helm - https://helm.sh/docs/intro/install/)
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh
rm -f ./get_helm.sh

# Install the SageMaker AI HyperPod CLI
git clone --recurse-submodules https://github.com/aws/sagemaker-hyperpod-cli.git
git checkout -b release_v2
cd sagemaker-hyperpod-cli
pip install .

# Verify the installation
hyperpod --help

# Connect to a SageMaker AI HyperPod Cluster
hyperpod connect-cluster --cluster-name `cluster-name`


# Submit the Job using the recipe for eval
# Namespace by default should be kubeflow
hyperpod start-job [--namespace `namespace`] --recipe evaluation/nova/nova_micro_p5_48xl_general_text_benchmark_eval --override-parameters \
'{
    "instance_type":"p5d.48xlarge",
    "container": "708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-HP-Eval-V2-latest",
    "recipes.run.name": `custom-run-name`,
    "recipes.run.model_type": `model_type`,
    "recipes.run.model_name_or_path" " `model name or finetune checkpoint s3uri`,
    "recipes.run.data_s3_path": `s3 for input data only for genqa and llm_judge, must be full S3 path that include filename`,
}'

# List jobs
hyperpod list-jobs [--namespace `namespace`] [--all-namespaces]

# Getting Job details
hyperpod get-job --job-name `job-name` [--namespace `namespace`] [--verbose]

# Listing Pods
hyperpod list-pods --job-name `job-name` --namespace `namespace`

# Cancel Job
hyperpod cancel-job --job-name `job-name` [--namespace `namespace`]
```

You should also be able to view the job status through Amazon EKS cluster console.
