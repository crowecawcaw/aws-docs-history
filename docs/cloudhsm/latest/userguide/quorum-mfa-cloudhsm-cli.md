# Quorum authentication and MFA in AWS CloudHSM
 clusters using CloudHSM CLI

The AWS CloudHSM cluster uses the same key for quorum authentication and for multi-factor
 authentication (MFA). This means a user with MFA enabled is effectively registered for MofN
 or quorum access control. To successfully use MFA and quorum authentication for the same HSM
 user, consider the following points:


* If you are using quorum authentication for a user today, you should use the same key pair you
 created for the quorum user to enable MFA for the user.
* If you add the MFA requirement for a non-MFA user who is not a quorum authentication user, then 
 you register that user as a quorum (MofN) registered user with MFA authentication.
* If you remove the MFA requirement or change the password for an MFA user who is also a registered
 quorum authentication user, you will also remove the user's registration as a quorum (MofN) user.
* If you remove the MFA requirement or change the password for an MFA user who is also a quorum 
 authentication user, *but you still want that user to participate in quorum authentication*, then you
 must register that user again as a Quorum (MofN) user.
For more information about quorum authentication, see [Manage quorum authentication (M of
 N)](quorum-auth-chsm-cli.md "quorum-auth-chsm-cli.md").
