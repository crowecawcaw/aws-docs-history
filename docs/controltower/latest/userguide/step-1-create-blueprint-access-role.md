# Step 1. Create the required

role

Before you begin to customize accounts, you must set up a role that contains a
trust relationship between AWS Control Tower and your hub account. When assumed, the role
grants AWS Control Tower access to administer the resources in the hub account. The role must
be named **AWSControlTowerBlueprintAccess**.

AWS Control Tower assumes this role to create a Portfolio resource on your behalf in AWS Service Catalog,
then to add your blueprint as a Service Catalog Product to this Portfolio, and then
to share this Portfolio, and your blueprint, with your member account during account
provisioning.

You'll create the `AWSControlTowerBlueprintAccess` role, as explained
in the following sections. You can set up the role in an enrolled or an unenrolled account.

###### Navigate to the IAM console to set up the required role.

###### To set up the AWSControlTowerBlueprintAccess role in an enrolled AWS Control Tower account

1. Federate or sign in as the principal in the AWS Control Tower management
   account.
2. From the federated principal in the management account, assume or switch
   roles to the `AWSControlTowerExecution` role in the enrolled
   AWS Control Tower account that you select to serve as the blueprint hub account.
3. From the `AWSControlTowerExecution` role in the enrolled
   AWS Control Tower account, create the `AWSControlTowerBlueprintAccess`
   role with proper permissions and trust relationships.

###### Important

To comply with AWS best practices guidance, it's important that you sign out
of the `AWSControlTowerExecution` role immediately after you create
the `AWSControlTowerBlueprintAccess` role.

To prevent unintended changes to resources, the
`AWSControlTowerExecution` role is intended for use by AWS Control Tower
only.

If your blueprint hub account isn't enrolled in AWS Control Tower, the
`AWSControlTowerExecution` role won't exist in the account, and
there's no need to assume it before you continue with setting up the
`AWSControlTowerBlueprintAccess` role.

###### To set up the AWSControlTowerBlueprintAccess role in an unenrolled member account

1. Federate or sign in as a principal in the account that you wish to
   designate as the hub account, by means of your preferred method.
2. When signed in as the principal in the account, create the
   `AWSControlTowerBlueprintAccess` role with proper permissions
   and trust relationships.
   The **AWSControlTowerBlueprintAccess** role must be set up to
   grant trust to two principals:

- The principal (user) that runs AWS Control Tower in the AWS Control Tower management
  account.
- The role named `AWSControlTowerAdmin` in the AWS Control Tower
  management account.
  Here's an example trust policy, similar to one you will need to include for your
  role. This policy demonstrates the best practice of granting least-privilege access.
  When you make your own policy, replace the term
  `YourManagementAccountId` with the
  actual acccount ID of your AWS Control Tower management account, and replace the term
  `YourControlTowerUserRole` with the
  identifier of the IAM role for your management account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "arn:aws:iam::`111122223333`:role/service-role/AWSControlTowerAdmin",
 "arn:aws:iam::`111122223333`:role/YourControlTowerUserRole"
 ]
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

**Required permissions policy**

AWS Control Tower requires that the managed policy named
`AWSServiceCatalogAdminFullAccess` must be attached to the
`AWSControlTowerBlueprintAccess` role. This policy provides
permissions that AWS Service Catalog looks for when it allows AWS Control Tower to administer your portfolio
and AWS Service Catalog Product resources. You can attach this policy when you're creating the role
in the IAM console.

###### Additional permissions may be required

- If you store your blueprints in Amazon S3, AWS Control Tower also requires the `AmazonS3ReadOnlyAccess` permission policy for the `AWSControlTowerBlueprintAccess` role.
- The AWS Service Catalog Terraform type of product requires you to add some additional permissions to the AFC custom IAM policy, if you don't utilize the default **Admin** policy. It requires these in addition to the permissions required to create the resources that you define in your terraform template.
