# Launch a Code Editor application using the AWS CLI

To configure and access your Code Editor integrated development environment through the
AWS Command Line Interface (AWS CLI), you must create a Code Editor space. Be sure to meet the [Complete prerequisites](code-editor-admin-prerequisites.md "code-editor-admin-prerequisites.md") before going through the following steps. Use the following procedure to create and run a
Code Editor space.

###### To create and run a Code Editor space

1. Access a space using AWS Identity and Access Management (IAM) or AWS IAM Identity Center authentication. For more
   information about accessing spaces using the AWS CLI, see _Accessing spaces using
   the AWS Command Line Interface_ in [Amazon SageMaker Studio spaces](studio-updated-spaces.md "studio-updated-spaces.md").
2. Create an application and specify `CodeEditor` as the
   `app-type` using the following command.

If you use a GPU instance type when creating your Code Editor application, you must also
use a GPU-based image.

```
aws sagemaker create-app \
--domain-id `domain-id` \
--space-name `space-name` \
--app-type `CodeEditor` \
--app-name `default` \
--resource-spec "SageMakerImageArn=arn:aws:sagemaker:`region`:`account-id`:image/`sagemaker-distribution-cpu`"
```

For more information about available Code Editor image ARNs, see [Code Editor application instances and images](code-editor-use-instances.md "code-editor-use-instances.md"). 3. After the Code Editor application is in service, launch the application using a presigned
URL. You can use the `describe-app` API to check if your application is in
service. Use the `create-presigned-domain-url` API to create a presigned
URL:

```
aws sagemaker create-presigned-domain-url \
--domain-id `domain-id` \
--space-name `space-name` \
--user-profile-name `user-profile-name` \
--session-expiration-duration-in-seconds `43200` \
--landing-uri `app:CodeEditor:`
```

4. Open the generated URL to start working in your Code Editor application.
