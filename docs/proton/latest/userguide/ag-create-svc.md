End of support notice: On October 7, 2026, AWS will end support for AWS Proton. After October
7, 2026, you will no longer be able to access the AWS Proton console or AWS Proton resources. Your deployed infrastructure
will remain intact. For more information, see [AWS Proton Service Deprecation and Migration
Guide](proton-end-of-support.md "proton-end-of-support.md").

# Create a service

To deploy an application with AWS Proton, as a developer, you create a service and provide the following inputs.

1. The name of an AWS Proton service template that's published by the platform team.
2. A name for the service.
3. The number of service instances that you want to deploy.
4. A selection of environments that you want to use.
5. A connection to your code repository if you're using a service template that includes a service pipeline (optional).

## What's in a service?

When you create an AWS Proton service, you can choose from two different types of service templates:

- A service template that includes a service pipeline (default).
- A service template that _doesn't_ include a service pipeline.

You must create at least one service instance when you create your service.

A service instance and optional pipeline are associated with a service. You can only create or delete a pipeline within the context of service
_create_ and _delete_ actions. To learn how to add and remove instances from a service, see [Edit a service](ag-svc-update.md "ag-svc-update.md").

###### Note

Your environment is configured for either AWS- or self-managed provisioning. AWS Proton provisions services in an environment using the same
provisioning method as the environment uses. The developer creating or updating service instances doesn't see the difference and their experience is
the same in both case.

For more information about provisioning methods, see [How AWS Proton provisions infrastructure](ag-works-prov-methods.md "ag-works-prov-methods.md").

## Service templates

Both major and minor versions of service templates are available. When you use the console, you select the latest `Recommended` major and
minor version of the service template. When you use the AWS CLI and you specify only the major version of the service template, you implicitly specify its
latest `Recommended` minor version.

The following describes the difference between major and minor template versions and their use.

- New versions of a template become `Recommended` as soon as they're approved by a member of the platform team. This means that new
  services are created using that version, and you're prompted to update existing services to the new version.
- Through AWS Proton, the platform team can automatically update service instances to a new minor version of a service template. Minor versions must
  be backward compatible.
- Because major versions require you to provide new inputs as part of the update process, you need to update your service to a major version of
  its service template. Major versions _aren't_ backward compatible.

## Create a service

The following procedures show how to use the AWS Proton console or AWS CLI to create a service with or without a service pipeline.

AWS Management Console

###### Create a service as shown in the following console steps.

1. In the [AWS Proton console](https://console.aws.amazon.com//proton/ "https://console.aws.amazon.com//proton/"), choose **Services**.
2. Choose **Create service**.
3. In the **Choose a service template** page, select a template and choose **Configure**.

When you _don't_ want to use an enabled pipeline, choose a template marked with _Excludes pipeline_
for your service. 4. In the **Configure service** page, in the **Service settings** section, enter an **Service
name**. 5. (Optional) Enter a description for the service. 6. ###### In the **Service repository settings** section:

    1. For **CodeStar Connection**, choose your connection from the list.
    2. For **Repository ID**, choose the name of your source code repository from the list.
    3. For **Branch name**, choose the name of your source code repository branch from the list.

7. (Optional) In the **Tags** section, choose **Add new tag** and enter a key and value to create a
   customer managed tag.
8. Choose **Next**.
9. In the **Configure custom settings** page, in the **Service instances** section, in the **New
   instance** section. You must enter values for the `required` parameters. You can enter values for the
   `optional` parameters or use the defaults when given.
10. In the **Pipeline inputs** section, you must enter values for the `required` parameters. You can enter values
    for the `optional` parameters or use the defaults when given.
11. Choose **Next** and review your inputs.
12. Choose **Create**.

View the service details and status, as well as the AWS managed tags and customer managed tags for your service. 13. In the navigation pane, choose **Services**.

A new page displays a list of your services along with the status and other service details.

AWS CLI
When you use the AWS CLI, you specify service inputs in a YAML formatted `spec` file, `.aws-proton/service.yaml`, located
in your source code directory.

You can use the CLI `get-service-template-minor-version` command to view the schema required and optional parameters that you
provide values for in your spec file.

If you want to use a service template that has `pipelineProvisioning: "CUSTOMER_MANAGED"`, _don’t_ include the
`pipeline:` section in your spec and _don’t_ include `-repository-connection-arn`,
`-repository-id`, and `-branch-name` parameters in your `create-service` command.

Create a service with a service pipeline as shown in the following CLI steps.

1. Set up the [service role](security_iam_service-role-policy-examples.md#codepipeline-proton-svc-role "security_iam_service-role-policy-examples.md#codepipeline-proton-svc-role") for the pipeline as shown in the
   following CLI example command.

Command:

```
`$` `aws proton update-account-settings \
 --pipeline-service-role-arn "arn:aws:iam::`123456789012`:role/`AWSProtonServiceRole`"`
```

2. The following listing shows an example spec, based on the service template schema, that includes the service pipeline and instance
   inputs.

Spec:

```
proton: ServiceSpec

pipeline:
  my_sample_pipeline_required_input: "hello"
  my_sample_pipeline_optional_input: "bye"

instances:
  - name: "acme-network-dev"
    environment: "ENV_NAME"
    spec:
      my_sample_service_instance_required_input: "hi"
      my_sample_service_instance_optional_input: "ho"

```

Create a service with a pipeline as shown in the following CLI example command and response.

Command:

```
`$` `aws proton create-service \
 --name "`MySimpleService`" \
 --branch-name "`mainline`" \
 --template-major-version "`1`" \
 --template-name "`fargate-service`" \
 --repository-connection-arn "arn:aws:codestar-connections:`region-id`:`123456789012`:connection/`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`" \
 --repository-id "`myorg/myapp`" \
 --spec "`file://spec.yaml`"`
```

Response:

```
{
    "service": {
        "arn": "arn:aws:proton:region-id:123456789012:service/MySimpleService",
        "createdAt": "2020-11-18T19:50:27.460000+00:00",
        "lastModifiedAt": "2020-11-18T19:50:27.460000+00:00",
        "name": "MySimpleService",
        "repositoryConnectionArn": "arn:aws:codestar-connections:region-id:123456789012:connection/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "repositoryId": "myorg/myapp",
        "status": "CREATE_IN_PROGRESS",
        "templateName": "fargate-service"
    }
}
```

Create a service without a service pipeline as shown in the following CLI example command and response.

The following shows an example spec that _doesn't_ include service pipeline inputs.

Spec:

```
proton: ServiceSpec

instances:
  - name: "acme-network-dev"
    environment: "ENV_NAME"
    spec:
      my_sample_service_instance_required_input: "hi"
      my_sample_service_instance_optional_input: "ho"

```

To create a service _without_ a provisioned service pipeline, you provide the path to a
`spec.yaml` and you _don't_ include repository parameters as shown in the following CLI example command and
response.

Command:

```
`$` `aws proton create-service \
 --name "`MySimpleServiceNoPipeline`" \
 --template-major-version "`1`" \
 --template-name "`fargate-service`" \
 --spec "`file://spec-no-pipeline.yaml`"`
```

Response:

```
{
    "service": {
        "arn": "arn:aws:proton:region-id:123456789012:service/MySimpleServiceNoPipeline",
        "createdAt": "2020-11-18T19:50:27.460000+00:00",
        "lastModifiedAt": "2020-11-18T19:50:27.460000+00:00",
        "name": "MySimpleServiceNoPipeline",
        "status": "CREATE_IN_PROGRESS",
        "templateName": "fargate-service-no-pipeline"
    }
}
```
