End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Modify a project

to use a custom container

These instructions assume that you already know how to use AWS SimSpace Weaver and want
to make your app storage and development workflows in the AWS Cloud
more efficient.

###### Prerequisites

- You have a custom container in Amazon Elastic Container Registry (Amazon ECR). For more information about creating a custom
  container, see [Create a custom container](working-with_custom-containers_create.md "working-with_custom-containers_create.md").

###### To modify your project to use a custom container

1. Add permissions to your project's simulation app role to use Amazon ECR.
   1. If you don't already have an IAM policy with following permissions,
      create the policy. We suggest the policy name `simspaceweaver-ecr`.
      For more information about how to create an IAM policy, see
      [Creating
      IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the _AWS Identity and Access Management User Guide_.

   ```
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Sid": "Statement",
               "Effect": "Allow",
               "Action": [
                   "ecr:BatchGetImage",
                   "ecr:GetDownloadUrlForLayer",
                   "ecr:GetAuthorizationToken"
               ],
               "Resource": "*"
           }
       ]
   }

   ```

   2. Find the name of your project's simulation app role:
      1. In a text editor, open the CloudFormation template:

      ```
      `sdk-folder`\PackagingTools\sample-stack-template.yaml
      ```

      2. Find the `RoleName` property
         under `WeaverAppRole`. The value is the name
         of your project's simulation app role.

      ###### Example

      ```
      AWSTemplateFormatVersion: "2010-09-09"
      Resources:
        WeaverAppRole:
          Type: 'AWS::IAM::Role'
          Properties:
            RoleName: **'weaver-MySimulation-app-role'**
            AssumeRolePolicyDocument:
              Version: "2012-10-17"
              Statement:
              - Effect: Allow
                Principal:
                  Service:
                    - 'simspaceweaver.amazonaws.com'

      ```

   3. Attach the `simspaceweaver-ecr` policy to the project's simulation app role.
      For more information about how to attach a policy, see [Adding and
      removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") in the _AWS Identity and Access Management User Guide_.
   4. Navigate to `sdk-folder` and run the following command to update the sample SimSpace Weaver stack:

   ```
   python setup.py --cloudformation
   ```

2. Specify your container images in the project's simulation schema.
   - You can add the optional `default_image` property under `simulation_properties`
     to specify a default custom container image for all domains.
   - Add the `image` property in the `app_config` for a domain that you
     want to use a custom container image. Specify the Amazon ECR repository URI as the value. You can
     specify a different image for each domain.
     - If `image` isn't specified for a domain and
       `default_image` is specified, apps in that domain use the default image.
     - If `image` isn't specified for a domain and
       `default_image` isn't specified, apps in that domain run in a standard SimSpace Weaver container.

###### Example Schema snippet that includes custom container settings

```
sdk_version: "1.17.0"
simulation_properties:
  log_destination_service: "logs"
  log_destination_resource_name: "MySimulationLogs"
  default_entity_index_key_type: "Vector3<f32>"
  **default\_image: "111122223333.dkr.ecr.us-west-2.amazonaws.com/my-ecr-repository:latest"** # image to use if no image specified for a domain
domains:
  MyCustomDomain:
    launch_apps_via_start_app_call: {}
    app_config:
      package: "s3://weaver-myproject-111122223333-us-west-2/MyViewApp.zip"
      launch_command: ["MyViewApp"]
      required_resource_units:
        compute: 1
      endpoint_config:
        ingress_ports:
          - 7000
      **image: "111122223333.dkr.ecr.us-west-2.amazonaws.com/my-ecr-repository:latest"** # custom container image to use for this domain
  MySpatialDomain:
    launch_apps_by_partitioning_strategy:
      partitioning_strategy: "MyGridPartitioning"
      grid_partition:
        x: 2
        y: 2
    app_config:
      package: "s3://weaver-myproject-111122223333-us-west-2/MySpatialApp.zip"
      launch_command: ["MySpatialApp"]
      required_resource_units:
        compute: 1
      **image: "111122223333.dkr.ecr.us-west-2.amazonaws.com/my-ecr-repository:latest"** # custom container image to use for this domain

```

3. Build and upload your project as usual.
