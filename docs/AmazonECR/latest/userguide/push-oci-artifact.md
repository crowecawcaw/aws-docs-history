# Pushing a Helm chart to an Amazon ECR private

repository

You can push Open Container Initiative (OCI) artifacts to an Amazon ECR repository. To
see an example of this functionality, use the following steps to push a Helm chart
to Amazon ECR.

For information about using your Amazon ECR hosted Helm charts with Amazon EKS, see [Installing a Helm chart on an
Amazon EKS cluster](using-helm-charts-eks.md "using-helm-charts-eks.md").

###### To push a Helm chart to an Amazon ECR repository

1. Install the latest version of the Helm client. These steps were written
   using Helm version `3.18.6`. For compatibility with Amazon EKS
   supported Kubernetes versions, use Helm version 3.9 or later. For more
   information, see [Installing
   Helm](https://helm.sh/docs/intro/install/ "https://helm.sh/docs/intro/install/").
2. Use the following steps to create a test Helm chart. For more information,
   see [Helm Docs - Getting Started](https://helm.sh/docs/chart_template_guide/getting_started/ "https://helm.sh/docs/chart_template_guide/getting_started/").
   1. Create a Helm chart named `helm-test-chart` and clear
      the contents of the `templates` directory.

   ```
   `helm create `helm-test-chart`
   rm -rf ./`helm-test-chart`/templates/*`
   ```

   2. Create a `ConfigMap` in the `templates`
      folder.

   ```
   `cd `helm-test-chart`/templates
   cat <<EOF > configmap.yaml
   apiVersion: v1
   kind: ConfigMap
   metadata:
    name: `helm-test-chart`-configmap
   data:
    myvalue: "Hello World"
   EOF`
   ```

3. Package the chart. The output will contain the filename of the packaged
   chart which you use when pushing the Helm chart.

```
`cd ../..
helm package `helm-test-chart``
```

Output

```
Successfully packaged chart and saved it to: /Users/`username`/`helm-test-chart`-0.1.0.tgz
```

4. Create a repository to store your Helm chart. The name of your repository
   should match the name you used when creating the Helm chart in step 2. For
   more information, see [Creating an Amazon ECR private repository to store
   images](repository-create.md "repository-create.md").

```
`aws ecr create-repository \
 --repository-name `helm-test-chart` \
 --region `us-west-2``
```

5. Authenticate your Helm client to the Amazon ECR registry to which you intend to
   push your Helm chart. Authentication tokens must be obtained for each
   registry used, and the tokens are valid for 12 hours. For more information,
   see [Private registry authentication in Amazon ECR](registry_auth.md "registry_auth.md").

```
`aws ecr get-login-password \
 --region `us-west-2` | helm registry login \
 --username AWS \
 --password-stdin ``aws_account_id`.dkr.ecr.`region`.amazonaws.com``
```

6. Push the Helm chart using the **helm push** command. The
   output should include the Amazon ECR repository URI and SHA digest.

```
`helm push `helm-test-chart-0.1.0.tgz` oci://``aws_account_id`.dkr.ecr.`region`.amazonaws.com`/`
```

7. Describe your Helm chart.

```
`aws ecr describe-images \
 --repository-name `helm-test-chart` \
 --region `us-west-2``
```

In the output, verify that the `artifactMediaType` parameter
indicates the proper artifact type.

```
{
    "imageDetails": [
        {
            "registryId": "`aws_account_id`",
            "repositoryName": "helm-test-chart",
            "imageDigest": "sha256:dd8aebdda7df991a0ffe0b3d6c0cf315fd582cd26f9755a347a52adEXAMPLE",
            "imageTags": [
                "0.1.0"
            ],
            "imageSizeInBytes": 1620,
            "imagePushedAt": "2021-09-23T11:39:30-05:00",
            "imageManifestMediaType": "application/vnd.oci.image.manifest.v1+json",
            "artifactMediaType": "application/vnd.cncf.helm.config.v1+json"
        }
    ]
}
```

8. (Optional) For additional steps, install the Helm `ConfigMap`
   and get started with Amazon EKS. For more information, see [Installing a Helm chart on an
   Amazon EKS cluster](using-helm-charts-eks.md "using-helm-charts-eks.md").
