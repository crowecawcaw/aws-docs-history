# Starting a training job using the HyperPod

CLI

SageMaker HyperPod CLI is a command-line interface tool for managing Amazon SageMaker HyperPod clusters.
You can use the HyperPod CLI to create, configure, and monitor HyperPod
clusters for machine learning workloads. For more information, see the [sagemaker-hyperpod-cli](https://github.com/aws/sagemaker-hyperpod-cli "https://github.com/aws/sagemaker-hyperpod-cli") GitHub
repository.

## Prerequisites

- [Install the
  HyperPod CLI](sagemaker-hyperpod-eks-run-jobs-access-nodes.md "sagemaker-hyperpod-eks-run-jobs-access-nodes.md"). For Amazon Nova customization on Amazon SageMaker HyperPod, you must
  check out the `release_v2` branch to use the SageMaker HyperPod CLI.
- Verify that the Nova output bucket exists before submitting jobs. To verify, run
  `aws s3 ls s3://nova-111122223333/`.

The bucket name is the value you specified for
`recipes.run.output_s3_path` in the recipe. This output bucket will store a
manifest file generated after training, which will contain S3 paths to the output
artifacts stored in the service-managed Amazon S3 bucket. Additionally, it might optionally
store TensorBoard files or evaluation results.

- Understanding Amazon FSx data sync requirements. Amazon FSx needs time to sync Amazon S3 training

data before jobs can run.

## Set up the HyperPod CLI for Amazon Nova

customization

###### To set up the HyperPod CLI for Amazon Nova customization, follow these

steps.

1. Clone the [sagemaker-hyperpod-cli](https://github.com/aws/sagemaker-hyperpod-cli/tree/release_v2 "https://github.com/aws/sagemaker-hyperpod-cli/tree/release_v2") GitHub repository with branch
   `release_v2`.

```
git clone --recurse-submodules https://github.com/aws/sagemaker-hyperpod-cli.git --branch release_v2
```

2. Navigate to the `sagemaker-hyperpod-cli` folder.

```
cd sagemaker-hyperpod-cli
```

3. Check that you have all the prerequisites in [Prerequisites](https://github.com/aws/sagemaker-hyperpod-cli/tree/release_v2?tab=readme-ov-file#prerequisitesagemaker-hyperpod-cli "https://github.com/aws/sagemaker-hyperpod-cli/tree/release_v2?tab=readme-ov-file#prerequisitesagemaker-hyperpod-cli").
4. To set up Helm, follow these steps.
   1. To download the Helm installation script, run:

   ```
   curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
   ```

   2. To make the script executable, run:

   ```
   chmod 700 get_helm.sh
   ```

   This command changes permissions to make the script executable. 3. To run the Helm installation script, run:

   ```
   ./get_helm.sh
   ```

   4. To remove the installation script, run:

   ```
   rm -f ./get_helm.sh
   ```

5. To install HyperPod dependencies with restricted instance group (RIG) support, follow these steps.

###### Note

Before installing the dependencies, you must have a HyperPod EKS cluster
with RIG. If you don't have one already, follow [these
instructions](nova-hp-cluster.md "nova-hp-cluster.md") to create one.

    1. To connect to your HyperPod EKS cluster, run:



    ```
    aws eks update-kubeconfig --name <eks_cluster_name> --region us-east-1
    ```
    2. To verify connection to your HyperPod EKS cluster, run:



    ```
    kubectl config current-context
    ```
    3. To pull updates for standard HyperPod dependencies, run:



    ```
    helm dependencies update helm_chart/HyperPodHelmChart
    ```
    4. To install standard HyperPod dependencies, run:



    ```
    helm install dependencies helm_chart/HyperPodHelmChart --namespace kube-system
    ```
    5. To navigate to Helm chart directory, run:



    ```
    cd helm_chart
    ```
    6. To install RIG specific HyperPod dependencies, run the following
     command.


    ###### Note

    Before installing the dependencies, consider the following:



    	* You should only run this command once per cluster after it's
    	 created.
    	* You should ensure the yq utility is installed with version at least 4
    	 (such as v4). There is a built-in check to confirm yq >=4 is available in the
    	 installation script.
    	* You will need to confirm installation by entering `y` when prompted.
    	 Optionally, before confirmation, view the intended installation at `./rig-dependencies.yaml`.

    ```
    chmod 700 ./install_rig_dependencies.sh && ./install_rig_dependencies.sh
    ```
    7. To navigate back to the root of `codesagemaker-hyperpod-cli` repo, run:



    ```
    cd ..
    ```

6. To proceed with installing the HyperPod CLI in
   `sagemaker-hyperpod-cli`, follow these steps.
   1. Install the CLI using pip:

   ```
   pip install -e .
   ```

   2. Verify the installation:

   ```
   hyperpod --help
   ```

## Submit a job

You can use the HyperPod CLI to submit a training job.

**To submit a job using a recipe, run the following
command.**

```
hyperpod start-job [--namespace <namespace>] --recipe {{fine-tuning | evaluation | training}}/nova/<Your_Recipe_Name> --override-parameters \
  '{
      "instance_type":"p5d.48xlarge",
      "container": <Docker Image>,
      "recipes.run.name": <custom-run-name>,
      "recipes.run.output_s3_path": "<customer-s3-path>"
  }'
```

- `--recipe`: The type of the job you are running using the recipe. Valid values
  are: `fine-tuning` | `evaluation` | `training`.

| Job type              | Value                                                                                  |
| --------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SFT/PEFT/PPO/DPO jobs | `fine-tuning`                                                                          |
| Evaluation jobs       | `evaluation`                                                                           |
| CPT jobs              | `training`                                                                             | <br>• Recipe name: You can find the name in the repository under the directory:`/src/hyperpod_cli/sagemaker_hyperpod_recipes/recipe_collection/recipes/`. <br>• Example recipe: `--recipe evaluation/nova/nova_lite_g5_12xl_bring_your_own_dataset_eval`. <br>• Container: This field is required. To find your images for the job types, see the following table.                                                                                                                                                                                                                                     |
| Technique             | Container                                                                              |
| ---                   | ---                                                                                    |
| DPO                   | 708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-HP-DPO-latest      |
| Evaluation jobs       | 708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-HP-Eval-latest    |
| CPT                   | 708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:HP-CPT-latest         |
| PPO                   | 708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SMHP-PPO-TRAIN-latest |
| SFT/PEFT              | 708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-HP-SFT-latest      | <br>• Custom run name: There are definition constraints on the `custom-run-time` input, for example, no capitals, no spaces, no underscores. For more information, see [Object Names and IDs](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-label-names "https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-label-names"). **[Optional] If you already have a training job and want to target a specific node for your next job, follow these steps.** 1. To get all free nodes, run the following command. ``` kubectl get nodes —no-headers | awk '$2 != "NotReady" && $3 != "SchedulingDisabled" {print $1}' ``2. Add the following to the `src\hyperpod_cli\sagemaker_hyperpod_recipes\recipes_collection\cluster\k8s.yaml`file for label selector.`` label_selector: required: kubernetes.io/hostname: <br>• <node_name> `3. On the root directory, run the following command. This ensures SageMaker HyperPod is installed on the user's system, enabling them to use the "hyperpod" keyword for job submission and other functions. You should run this command from the root folder where the HyperPod CLI code is.` pip install . `## List jobs To list jobs, run the following command.` hyperpod list-jobs [--namespace <namespace>] [--all-namespaces] `The command lists all jobs in the specified namespace or across all namespaces. ## Get job details To get the details of a job, run the following command.` hyperpod get-job --job-name <job-name> [--namespace <namespace>] [--verbose] `The command retrieves detailed information about a specific job. ## List pods To list pods, run the following command.` hyperpod list-pods --job-name <job-name> [--namespace <namespace>] `The command lists all pods associated with a specific job in the specified namespace. ## Cancel jobs To cancel a job, run the following command.` hyperpod cancel-job --job-name <job-name> [--namespace <namespace>] ``` This command cancels and deletes a running training job in the specified namespace. |
