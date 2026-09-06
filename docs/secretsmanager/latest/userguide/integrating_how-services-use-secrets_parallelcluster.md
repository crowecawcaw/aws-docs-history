

# How AWS ParallelCluster uses AWS Secrets Manager
<a name="integrating_how-services-use-secrets_parallelcluster"></a>

AWS ParallelCluster is an open source cluster management tool that you can use to deploy and manage high performance computing (HPC) clusters in the AWS Cloud. You can create a multiple user environment that includes an AWS ParallelCluster that's integrated with an AWS Managed Microsoft AD (Active Directory). The AWS ParallelCluster uses a Secrets Manager secret for validating logins to Active Directory. For more information, see [Integrating Active Directory](https://docs.aws.amazon.com/parallelcluster/latest/ug/tutorials_05_multi-user-ad.html) in the *AWS ParallelCluster User Guide*.