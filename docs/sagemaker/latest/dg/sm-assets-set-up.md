# Set up SageMaker Assets (administrator guide)

###### Important

SageMaker Assets is only available in Amazon SageMaker Studio. If you're using Amazon SageMaker Studio Classic, you
must migrate to Studio. For more information about Studio and Studio Classic,
see [Machine learning environments offered by Amazon SageMaker AI](machine-learning-environments.md "machine-learning-environments.md"). For information about
migrating, see [Migration from Amazon SageMaker Studio Classic](studio-updated-migrate.md "studio-updated-migrate.md").

As business needs change, your users need to collaborate effectively to solve business
problems as they arise. To solve them, users must share data and models with each
other.

SageMaker Assets integrates Amazon SageMaker Studio with Amazon DataZone, a data management service. SageMaker Assets
is a platform that helps your users share models and data with each other. You can use
the following information to set up the integration between SageMaker Assets and
Amazon DataZone.

You create an Amazon DataZone domain for your business line or organization. The
_domain_ is the core feature of Amazon DataZone. All of your users'
data and models exist within the domain.

Within the Amazon DataZone domain, a subset of your users work on specific
_projects_. A project typically corresponds to a particular
business problem. Within the project, members can create datasets and models. By
default, project members only have access to the data and models within the project.
They can provide access to their data and models to other users within the
organization.

Within the project, you create environments. For SageMaker Assets specifically, an environment
is a collection of configured resources used to launch Amazon SageMaker Studio. For more
information about the terminology used in Amazon DataZone, see [Terminology and
concepts](../../../datazone/latest/userguide/datazone-concepts.md "../../../datazone/latest/userguide/datazone-concepts.md").

###### Important

Depending on the set up you choose, Amazon SageMaker Studio uses one of the
following:

- An Amazon SageMaker AI domain that Amazon DataZone creates as part of your SageMaker AI
  environment.
- Your existing Amazon SageMaker AI domain that you migrate to Amazon DataZone
  You can access Studio from the Amazon SageMaker AI domain, but we recommend accessing it
  from the project you've created. For information about accessing Studio, see
  [Work with assets (user guide)](sm-assets-user-guide.md "sm-assets-user-guide.md").

Use the steps in the following list and the documentation it references to set
up Amazon DataZone with an Amazon SageMaker AI domain that it creates.

1. Create an Amazon DataZone domain that corresponds to your users'
   organization or business line. For information about creating an
   Amazon DataZone domain, see [Create
   domains](../../../datazone/latest/userguide/create-domain.md "../../../datazone/latest/userguide/create-domain.md").
2. Enable the SageMaker AI blueprint within Amazon DataZone. For information about
   enabling the SageMaker AI blueprint, see [Enable built-in blueprints in the AWS account that owns the
   Amazon DataZone domain](../../../datazone/latest/userguide/working-with-blueprints.md#enable-default-blueprints "../../../datazone/latest/userguide/working-with-blueprints.md#enable-default-blueprints").
3. Create a project within the domain that corresponds to the business
   problem that users in your domain are solving. For information about
   creating a project, see [Create a new
   project](../../../datazone/latest/userguide/create-new-project.md "../../../datazone/latest/userguide/create-new-project.md").
4. Create an environment profile that you can use as a template to create
   SageMaker AI environments for your users. For information about creating an
   environment profile, see [Create an environment profile](../../../datazone/latest/userguide/create-environment-profile.md "../../../datazone/latest/userguide/create-environment-profile.md").
5. Create a SageMaker AI environment. Within the project, your users use the SageMaker AI
   environment to launch Amazon SageMaker Studio. Within Studio, they can
   create assets and use SageMaker Assets to share them. For information about
   creating an environment, see [Create a new environment](../../../datazone/latest/userguide/create-environment-profile.md "../../../datazone/latest/userguide/create-environment-profile.md").
6. Add SageMaker AI as one of the trusted services within Amazon DataZone. To add SageMaker AI
   as one of the services, see [Add SageMaker AI as a trusted service in the AWS account that owns the
   Amazon DataZone domain](../../../datazone/latest/userguide/working-with-blueprints.md#add-sagemaker-as-trusted-service "../../../datazone/latest/userguide/working-with-blueprints.md#add-sagemaker-as-trusted-service").
   Use the steps in the following list and the documentation it references to set
   up Amazon DataZone with an existing Amazon SageMaker AI domain.

7. Create an Amazon DataZone domain that corresponds to your users'
   organization or business line. For information about creating an
   Amazon DataZone domain, see [Create
   domains](../../../datazone/latest/userguide/create-domain.md "../../../datazone/latest/userguide/create-domain.md").
8. Enable the SageMaker AI blueprint within Amazon DataZone. For information about
   enabling a custom blueprint, see [Amazon DataZone custom AWS service blueprints](../../../datazone/latest/userguide/working-with-custom-blueprint.md "../../../datazone/latest/userguide/working-with-custom-blueprint.md").
9. Create a project within the domain that corresponds to the business
   problem that users in your domain are solving. For information about
   creating a project, see [Create a new
   project](../../../datazone/latest/userguide/create-new-project.md "../../../datazone/latest/userguide/create-new-project.md").
10. Enable SageMaker AI as one of the trusted services within Amazon DataZone. To
    enable SageMaker AI as one of the services, see [Add Amazon SageMaker AI as a trusted service in the AWS account that owns
    the Amazon DataZone domain](../../../datazone/latest/userguide/working-with-blueprints.md#add-sagemaker-as-trusted-service "../../../datazone/latest/userguide/working-with-blueprints.md#add-sagemaker-as-trusted-service") .
11. Create Amazon DataZone users within the SageMaker AI domain.
12. Onboard existing users to the Amazon DataZone domain.

###### Note

If your SageMaker AI users are SSO and your Amazon DataZone domain is SSO, you can
automatically map the users from the Amazon SageMaker AI domain to the Amazon DataZone
domain.

To onboard existing SageMaker AI users, run the [Amazon DataZone Import SageMaker AI Domain](https://github.com/aws/amazon-sagemaker-examples/tree/default/%20%20%20ml_ops/sm-datazone_import "https://github.com/aws/amazon-sagemaker-examples/tree/default/%20%20%20ml_ops/sm-datazone_import") script in your environment.
You must pass the name of your AWS Region and the AWS account ID of your
Amazon SageMaker AI domain as arguments. The following is an example AWS CLI command that runs
the script.

```

python `example-script` `AWS Region` `111122223333`

```

The script does the following:

1. Asks you for your Amazon SageMaker AI domain ID.
2. Asks you for your Amazon DataZone domain ID.
3. Asks you for your Amazon DataZone project.
4. Prompts you to specify the users that you're importing.
5. Adds tags to your users and the Amazon SageMaker AI domain.
6. Map your Amazon DataZone users to your SageMaker AI user profiles. For each SageMaker AI
   user profile, the script will prompt you for a Amazon DataZone user ID. You
   can modify the script for your own use case.
7. Attaches a federation role to the environment, so that Amazon DataZone can
   access your Amazon SageMaker AI domain domain and migrate it.
   The script goes through each user in the Amazon SageMaker AI domain and prompts you to
   specify the corresponding user in the Amazon DataZone domain. It automatically adds
   tags for the user in the Amazon DataZone domain to the users in the corresponding
   SageMaker AI domain. It also updates the custom environment blueprint with the
   mapping between users in each domain.

###### Note

The SageMaker AI environment uses the latest version of the SageMaker Distribution Image. SageMaker AI
Distribution Images have popular libraries packages for machine learning. For more
information, see [SageMaker Studio image support policy](sagemaker-distribution.md "sagemaker-distribution.md").

After you've created the environment, you can create AWS Glue and Amazon Redshift tables and
databases. For more information, see [Query
data in Athena or Amazon Redshift](../../../datazone/latest/userguide/query-athena-with-deep-link-in-project.md "../../../datazone/latest/userguide/query-athena-with-deep-link-in-project.md").

## Viewing and modifying your users'

permissions

After you create a SageMaker AI environment, you can change your users' permissions to
suit the needs of your organization. The SageMaker AI blueprint specifies permissions for
all of your users. They can perform actions with all of the SageMaker AI services, but the
permissions are scoped down to resources created within the Amazon DataZone
domain.

###### Important

The environment that you create uses an IAM role that has limited
permissions and a permissions boundary. To change your users' permissions, you
can modify or replace the permissions boundary. For example, you can change the
permissions boundary if your users need access to a resource such as an Amazon S3
bucket that has been created within the environment.

You can view the permissions in the ARN of the IAM role used to create the SageMaker AI
domain.

Use the following procedure to view or edit the permissions of the IAM role of
your users.

###### To view or edit the permissions of your users

1. Open the [Amazon SageMaker AI
   console](https://console.aws.amazon.com/sagemaker "https://console.aws.amazon.com/sagemaker").
2. Choose **Domains**.
3. Choose the name of the domain that has the same name as your Amazon DataZone
   domain.
4. Choose **Domain settings**.
5. Under **Execution role**, copy the ARN of the execution
   role.
6. Open the [IAM console](https://console.aws.amazon.com/IAM "https://console.aws.amazon.com/IAM").
7. Choose **Roles**.
8. Paste the ARN and delete everything except the role name after the last
   forward slash.
9. Choose the role to view the permissions.
10. Under **Permissions**, modify the policies to suit the
    needs of your organization.
11. (Optional) Select **Permissions boundary**, and choose
    **Set permissions boundary**.
12. Select a policy to set as the permissions boundary.
