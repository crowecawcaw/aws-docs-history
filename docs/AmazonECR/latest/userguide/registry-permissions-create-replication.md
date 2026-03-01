# Granting registry permissions for cross account replication in Amazon ECR

The cross account policy type is used to grant permissions to an AWS principal,
allowing the replication of the repositories from a source registry to your
registry. By default, you have permission to configure cross-Region replication
within your own registry. You only need to configure the registry policy if you're
granting another account permission to replicate contents to your registry.

A registry policy must grant permission for the `ecr:ReplicateImage`
API action. This API is an internal Amazon ECR API that can replicate images between
Regions or accounts. You can also grant permission for the `ecr:CreateRepository` permission, which allows Amazon ECR to create repositories in
your registry if they don't exist already. If the `ecr:CreateRepository`
permission isn't provided, a repository with the same name as the source repository
must be created manually in your registry. If neither is done, replication fails.
Any failed `CreateRepository` or `ReplicateImage` API actions
show up in CloudTrail.

1. Open the Amazon ECR console at
   [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/ "https://console.aws.amazon.com/ecr/").
2. From the navigation bar, choose the Region to configure your
   registry policy in.
3. In the navigation pane, choose **Private
   registry**, choose **Features &
   Settings**, and then choose **Permissions**
   .
4. On the **Registry permissions** page, choose **Generate
   statement**.
5. Complete the following steps to define your policy statement using
   the policy generator.
   1. For **Policy type**, choose \*\*Replication
   - cross account\*\*.
   2. For **Statement id**, enter a unique
      statement ID. This field is used as the `Sid` on
      the registry policy.
   3. For **Accounts**, enter the account IDs
      for each account you want to grant permissions to. When
      specifying multiple account IDs, separate them with a comma.

6. Choose **Save**.
7. Create a file named `registry_policy.json` and populate
   it with a registry policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"ReplicationAccessCrossAccount",
 "Effect":"Allow",
 "Principal":{
 "AWS":"arn:aws:iam::`111122223333`:`root`"
 },
 "Action":[
 "ecr:CreateRepository",
 "ecr:ReplicateImage"
 ],
 "Resource": [
 "arn:aws:ecr:us-west-2:`444455556666`:repository/`*`"
 ]
 }
 ]
}`

```

2. Create the registry policy using the policy file.

```
`aws ecr put-registry-policy \
 --policy-text file://`registry_policy.json` \
 --region `us-west-2``
```

3. Retrieve the policy for your registry to confirm.

```
`aws ecr get-registry-policy \
 --region `us-west-2``
```
