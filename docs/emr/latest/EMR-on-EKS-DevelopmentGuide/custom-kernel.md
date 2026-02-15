# Custom kernel image with interactive endpoint

To ensure that you have the correct dependencies for your application when you run
interactive workloads from Amazon EMR Studio, you can customize Docker images for interactive
endpoints and run customized base kernel images. To create an interactive endpoint and
connect it with a custom Docker image, perform the following steps.

###### Note

You can only override base images. You can't add new kernel image types.

1. **Create and publish a customized Docker image.** The
   base image contains the Spark runtime and the notebook kernels that run with it. To
   create the image, you can follow steps 1 through 4 in [How to customize Docker images](docker-custom-images-steps.md "docker-custom-images-steps.md"). In
   step 1, the base image URI in your Docker file must use `notebook-spark` in
   place of `spark`.

```
`ECR-registry-account`.dkr.ecr.`Region`.amazonaws.com/notebook-spark/`container-image-tag`
```

For more information on how to select AWS Regions and container image tags, see
[Details for selecting a base image URI](docker-custom-images-tag.md "docker-custom-images-tag.md"). 2. **Create an interactive endpoint that can be used with the
custom image.**

    1. Create a JSON file `custom-image-managed-endpoint.json` with the
     following contents. This example uses Amazon EMR release 6.9.0.


    ###### Example


    ```
    {
        "name": "`endpoint-name`",
        "virtualClusterId": "`virtual-cluster-id`",
        "type": "JUPYTER_ENTERPRISE_GATEWAY",
        "releaseLabel": "`emr-6.9.0-latest`",
        "executionRoleArn": "`execution-role-arn`",
        "configurationOverrides": {
            "applicationConfiguration": [
                {
                    "classification": "jupyter-kernel-overrides",
                    "configurations": [
                        {
                            "classification": "python3",
                            "properties": {
                                "container-image": "`123456789012.dkr.ecr.us-west-2.amazonaws.com/custom-notebook-python:latest`"
                            }
                        },
                        {
                            "classification": "spark-python-kubernetes",
                            "properties": {
                                "container-image": "`123456789012.dkr.ecr.us-west-2.amazonaws.com/custom-notebook-spark:latest`"
                            }
                        }
                    ]
                }
            ]
        }
    }
    ```
    2. Create an interactive endpoint with the configurations specified in the JSON
     file as shown in the following example. For more information, see [Create an interactive endpoint with the
     create-managed-endpoint command](create-managed-endpoint.md#create-using-json-file "create-managed-endpoint.md#create-using-json-file").



    ```
    aws emr-containers create-managed-endpoint --cli-input-json custom-image-managed-endpoint.json
    ```

3. **Connect to the interactive endpoint via
   EMR Studio.** For more information and steps to complete, see [Connecting from Studio](https://emr-on-eks.workshop.aws/advanced/emr-studio/connecting-from-studio.html "https://emr-on-eks.workshop.aws/advanced/emr-studio/connecting-from-studio.html") in the Amazon EMR on EKS section of the AWS Workshop Studio
   docs.
