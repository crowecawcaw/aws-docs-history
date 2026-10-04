

# IAM policy for Amazon CloudWatch
<a name="nx-features-configuration-sets-cloudwatch-creating-role"></a>

Use the following example to create a policy for sending events to a CloudWatch group.

**Note**  
Use the AWS End User Messaging console to generate the example IAM policy for this event destination.

For more information about IAM policies, see [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *IAM User Guide*.

The following example statement uses the, optional but recommended, `SourceAccount` and `SourceArn` conditions to check that only the AWS End User Messaging owner account has access to the configuration set. In this example, replace {{accountId}} with your AWS account id, {{region}} with the AWS Region name and {{ConfigSetName}} with the name of the Configuration Set.

After you create the policy, create a new IAM role, and then attach the policy to it. When you create the role, also add the following trust policy to it:

**Note**  
Use the AWS End User Messaging console to generate the example IAM policy for this event destination.

For more information about creating IAM roles, see [Creating IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html) in the *IAM User Guide*.