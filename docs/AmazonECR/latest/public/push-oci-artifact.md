# Pushing a Helm chart to a public repository in Amazon ECR public

Amazon ECR Public supports pushing Open Container Initiative (OCI) artifacts to your public
repositories. To display this functionality, use the following steps to push a Helm
chart to Amazon ECR Public.

###### To push a Helm chart to an Amazon ECR public repository

1. Install Helm version `3.8.0` or higher of the Helm client. These
   steps were written using Helm version `3.8.0`. For more information,
   see [Installing
   Helm](https://helm.sh/docs/intro/install/ "https://helm.sh/docs/intro/install/").
2. Use the following steps to create a test Helm chart. For more information, see
   [Helm
   Docs - Getting Started](https://helm.sh/docs/chart_template_guide/getting_started/ "https://helm.sh/docs/chart_template_guide/getting_started/").
   1. Create a Helm chart named `helm-test-chart` and clear the
      contents of the `templates` directory.

   ```
   `helm create `helm-test-chart`
   rm -rf ./`helm-test-chart`/templates/*`
   ```

   2. Create a ConfigMap in the `templates` folder.

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

3. Package the chart. The output will contain the filename of the packaged chart
   which you use when pushing the Helm chart.

```
`cd ..
helm package `helm-test-chart``
```

Output

```
Successfully packaged chart and saved it to: /Users/`username`/`helm-test-chart`-0.1.0.tgz
```

4. Create a public repository to store your Helm chart. For more information, see
   [Creating an Amazon ECR public repository to store images](public-repository-create.md "public-repository-create.md").

```
`aws ecr-public create-repository \
 --repository-name `helm-test-chart` \
 --region us-east-1`
```

5. Authenticate your Helm client to the Amazon ECR public registry to which you intend
   to push your Helm chart. Authentication tokens are valid for 12 hours. For more
   information, see [Registry authentication in Amazon ECR public](public-registry-auth.md "public-registry-auth.md").

```
`aws ecr-public get-login-password \
 --region us-east-1 | helm registry login \
 --username AWS \
 --password-stdin public.ecr.aws`
```

6. Push the Helm chart using the **helm push** command. The output
   should include the Amazon ECR repository URI and SHA digest.

```
`helm push `helm-test-chart-0.1.0.tgz` oci://public.ecr.aws/`registry_alias``
```

7. Describe your Helm chart.

```
`aws ecr-public describe-images \
 --repository-name `helm-test-chart` \
 --region us-east-1`
```

```
{
    "imageDetails": [
        {
            "registryId": "`aws_account_id`",
            "repositoryName": "helm-test-chart",
            "imageDigest": "sha256:f23ab9dc0fda33175e465bd694a5f4cade93eaf62715fa9390d9fEXAMPLE",
            "imageTags": [
                "0.1.0"
            ],
            "imageSizeInBytes": 1636,
            "imagePushedAt": "2022-06-01T12:17:39-05:00",
            "imageManifestMediaType": "application/vnd.oci.image.manifest.v1+json"
        }
    ]
}
```
