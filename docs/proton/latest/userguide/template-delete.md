End of support notice: On October 7, 2026, AWS will end support for AWS Proton. After October
7, 2026, you will no longer be able to access the AWS Proton console or AWS Proton resources. Your deployed infrastructure
will remain intact. For more information, see [AWS Proton Service Deprecation and Migration
Guide](proton-end-of-support.md "proton-end-of-support.md").

# Delete templates

Templates can be deleted using the console and AWS CLI.

You can delete a minor version of an environment template if there are no environments deployed to that version.

You can delete a minor version of a service template if there are no service instances or pipelines deployed to that version. Your pipeline can be
deployed to a different template version than your service instance. For example, if your service instance is updated to version 1.1 from 1.0 and your
pipeline is still deployed to version 1.0, you can’t delete service template 1.0.

AWS Management Console
You can use the console to delete the entire template or individual minor and major versions of a template.

Use the console to delete templates as follows.

###### Note

###### When using the console to delete templates.

- When you delete the entire template, you also delete the major and minor versions of the template.

###### In the list of (environment or service) templates.

1. In the [AWS Proton console](https://console.aws.amazon.com//proton/ "https://console.aws.amazon.com//proton/"), choose **(Environment or Service)
   Templates**.
2. In the list of templates, select the radio button to the left of the template you want to delete.

You can only delete an entire template if there are no AWS Proton resources deployed to its versions. 3. Choose **Actions** and then **Delete** to delete the entire template. 4. A modal prompts you to confirm the delete action. 5. Follow the instructions and choose **Yes, delete**.

###### In the (environment or service) template detail page.

1. In the [AWS Proton console](https://console.aws.amazon.com//proton/ "https://console.aws.amazon.com//proton/"), choose **(Environment or Service)
   Templates**.
2. In the list of templates, choose the name of the template that you want to entirely delete or delete individual major or minor versions of
   it.
3. ###### To delete the entire template.

You can only delete an entire template if there are no AWS Proton resources deployed to its versions.

    1. Choose **Delete**, top right corner of page.
    2. A modal prompts you to confirm the delete action.
    3. Follow the instructions and choose **Yes, delete**.

4. ###### To delete major or minor versions of a template.

You can only delete a minor version of a template if there are no AWS Proton resources deployed to that version.

    1. In the **Template versions** section, select the radio button to the left of the version that you want to
     delete.
    2. Choose **Delete** in the **Template versions** section.
    3. A modal prompts you to confirm the delete action.
    4. Follow the instructions and choose **Yes, delete**.

AWS CLI
AWS CLI template delete operations _don't_ include the deletion of other versions of a template. When using the AWS CLI, delete
templates with the following conditions.

- Delete an entire template if no minor or major versions of the template exist.
- Delete a major version when you delete the last remaining minor version.
- Delete a minor version of a template if there are no AWS Proton resources deployed to that version.
- Delete the recommended minor version of a template if no other minor versions of the template exist and there are no AWS Proton resources
  deployed to that version.

The following example commands and responses show how to use the AWS CLI to delete templates.

Run the following command:

```
`$` `aws proton delete-environment-template-version \
 --template-name "`simple-env`" \
 --major-version "`1`" \
 --minor-version "`0`"`
```

Response:

```
{
    "environmentTemplateVersion": {
        "arn": "arn:aws:proton:region-id:123456789012:environment-template/simple-env:1.0",
        "createdAt": "2020-11-11T23:02:47.763000+00:00",
        "description": "Version 1",
        "lastModifiedAt": "2020-11-11T23:02:54.610000+00:00",
        "majorVersion": "1",
        "minorVersion": "0",
        "status": "PUBLISHED",
        "statusMessage": "",
        "templateName": "simple-env"
    }
}
```

Run the following command:

```
`$` `aws proton delete-environment-template \
 --name "`simple-env`"`
```

Response:

```
{
    "environmentTemplate": {
        "arn": "arn:aws:proton:region-id:123456789012:environment-template/simple-env",
        "createdAt": "2020-11-11T23:02:45.336000+00:00",
        "description": "VPC with Public Access",
        "displayName": "VPC",
        "lastModifiedAt": "2020-11-12T00:23:22.339000+00:00",
        "name": "simple-env",
        "recommendedVersion": "1.0"
    }
}
```

Run the following command:

```
`$` `aws proton delete-service-template-version \
 --template-name "`fargate-service`" \
 --major-version "`1`" \
 --minor-version "`0`"`
```

Response:

```
{
    "serviceTemplateVersion": {
        "arn": "arn:aws:proton:region-id:123456789012:service-template/fargate-service:1.0",
        "compatibleEnvironmentTemplates": [{"majorVersion": "1", "templateName": "simple-env"}],
        "createdAt": "2020-11-28T22:07:05.798000+00:00",
        "lastModifiedAt": "2020-11-28T22:19:05.368000+00:00",
        "majorVersion": "1",
        "minorVersion": "0",
        "status": "PUBLISHED",
        "statusMessage": "",
        "templateName": "fargate-service"
    }
}
```
