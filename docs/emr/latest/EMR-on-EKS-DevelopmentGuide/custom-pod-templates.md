# Specifying custom pod templates with interactive

endpoints

You can create interactive endpoints where you specify custom pod templates
for drivers and executors. _Pod templates_ are specifications that determine how to run each
pod. You can use pod template files to define the configurations of driver or executor pods
that Spark configurations don't support. Pod templates are currently supported in Amazon EMR
releases 6.3.0 and greater.

For more information about pod templates, see [Using pod
templates](pod-templates.md "pod-templates.md") in the _Amazon EMR on EKS Development
Guide_.

The following example shows how to create an interactive endpoint with pod
templates:

```
aws emr-containers create-managed-endpoint \
    --type JUPYTER_ENTERPRISE_GATEWAY \
    --virtual-cluster-id `virtual-cluster-id` \
    --name `example-endpoint-name` \
    --execution-role-arn arn:aws:iam::`aws-account-id`:role/`EKSClusterRole` \
    --release-label `emr-6.9.0-latest` \
    --configuration-overrides '{
        "applicationConfiguration": [
        {
            "classification": "spark-defaults",
            "properties": {
                "spark.kubernetes.driver.podTemplateFile": "`path/to/driver/template.yaml`",
                "spark.kubernetes.executor.podTemplateFile": "`path/to/executor/template.yaml`"
            }
        }]
    }'
```
