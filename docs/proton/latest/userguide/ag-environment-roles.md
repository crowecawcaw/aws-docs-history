End of support notice: On October 7, 2026, AWS will end support for AWS Proton. After October
7, 2026, you will no longer be able to access the AWS Proton console or AWS Proton resources. Your deployed infrastructure
will remain intact. For more information, see [AWS Proton Service Deprecation and Migration
Guide](proton-end-of-support.md "proton-end-of-support.md").

# IAM Roles

With AWS Proton, you supply the IAM roles and AWS KMS keys for the AWS resources that you own and manage. These are later applied to and used by resources
owned and managed by developers. You create an IAM role to control your developer team's access to the AWS Proton API.

## AWS Proton service role

When you create a new environment, you provide a related IAM service role. The role contains all permissions that are necessary to update
all provisioned infrastructure defined in both the environment templates and the service templates. For role examples, see [AWS Proton service role for provisioning using CloudFormation](security_iam_service-role-policy-examples.md#proton-svc-role "security_iam_service-role-policy-examples.md#proton-svc-role"). If you use environment account connections and environment accounts, you create the role in
a selected environment account. For more information, see [Create an environment in one account and
provision in another account](ag-create-env.md#ag-create-env-deploy-other "ag-create-env.md#ag-create-env-deploy-other") and
[Environment account connections](ag-env-account-connections.md "ag-env-account-connections.md").

How you provide this service role, and who assumes the role, depends on your environment's provisioning method.

- _AWS-managed provisioning_ – You provide the role to AWS Proton, either directly while creating an environment, or
  indirectly through account connections. AWS Proton assumes the role in the relevant account to provision environment and service infrastructure.
- _Self-managed provisioning_ – It's your responsibility to configure your provisioning automation to assume an appropriate
  role using appropriate credentials when a pull request (PR) triggers a provisioning action. For an example GitHub Action that assumes a role, see
  [Assuming a Role](https://github.com/aws-actions/configure-aws-credentials#assuming-a-role "https://github.com/aws-actions/configure-aws-credentials#assuming-a-role") in the _"Configure AWS Credentials"
  Action For GitHub Actions_ documentation.

For more information about provisioning methods, see [How AWS Proton provisions infrastructure](ag-works-prov-methods.md "ag-works-prov-methods.md").
