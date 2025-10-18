# HSM users in AWS CloudHSM

Before you can use your AWS CloudHSM cluster for cryptoprocessing, you must create users and [keys](manage-keys.md "manage-keys.md")
 on the hardware security modules (HSM) in your cluster.

###### Note

HSM users are distinct from IAM users. IAM users who have the correct credentials can
 create HSMs by interacting with resources through the AWS API. After the HSM is created, you
 must use HSM user credentials to authenticate operations on the HSM.

 In AWS CloudHSM, you must use [CloudHSM CLI](cloudhsm_cli-getting-started.md "cloudhsm_cli-getting-started.md") or [CloudHSM
 Management Utility (CMU)](cloudhsm_mgmt_util-getting-started.md "cloudhsm_mgmt_util-getting-started.md") command line tools to create and manage the users on your
 HSM. CloudHSM CLI is designed to be used with [the latest SDK version series](use-hsm.md "use-hsm.md"), while the CMU is designed to be used with [the previous SDK version series](choose-client-sdk.md "choose-client-sdk.md").

See the following topics for more information about managing HSM users in AWS CloudHSM. You can
 also learn how to use quorum authentication (also known as M of N access control).

###### Topics

* [User management with
 CloudHSM CLI](manage-hsm-users-chsm-cli.md "manage-hsm-users-chsm-cli.md")
* [User management with CMU](manage-hsm-users-cmu.md "manage-hsm-users-cmu.md")
