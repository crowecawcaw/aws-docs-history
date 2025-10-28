# Users in AWS CloudHSM

Unlike most AWS services and resources, you do not use AWS Identity and Access Management (IAM) users or IAM
policies to access resources within your AWS CloudHSM cluster. Instead, you use _HSM users_ directly on HSMs in your AWS CloudHSM cluster.

HSM users are distinct from IAM users. IAM users who have the correct credentials can create HSMs by interacting with resources through the AWS API.
Since E2E encryption is not visible to AWS, you must use HSM user credentials to authenticate operations on the HSM because credentials takes place directly on the HSM. The HSM
authenticates each HSM user by means of credentials that you define and manage. Each HSM user has a _type_ that determines which operations
that user can perform on the HSM. Each HSM authenticates each HSM user by means of credentials that you define using [CloudHSM CLI](cloudhsm_cli.md "cloudhsm_cli.md").

If you are using the [previous SDK version series](choose-client-sdk.md "choose-client-sdk.md"), then you will use [CloudHSM Management Utility (CMU)](cloudhsm_mgmt_util.md "cloudhsm_mgmt_util.md").
