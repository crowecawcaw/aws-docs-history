# Step 1: Configure the Amazon EKS cluster and setup IAM permissions

###### Configure the Amazon EKS cluster and create the IAM resources that are required to allow an Amazon EKS service account to connect to your Amazon Keyspaces

table

1.  Create an Open ID Connect (OIDC) provider for the Amazon EKS cluster. This is needed to use IAM roles for service accounts.
    For more information about OIDC providers and how to create them, see [Creating an IAM OIDC provider for your cluster](../../../eks/latest/userguide/enable-iam-roles-for-service-accounts.md "../../../eks/latest/userguide/enable-iam-roles-for-service-accounts.md") in the _Amazon EKS User Guide_.
    1. Create an IAM OIDC identity provider for your cluster with the following command. This example assumes that your cluster name is
       `my-eks-cluster`. If you have a cluster with a different name, remember to update the name in all future commands.

    ```
    eksctl utils associate-iam-oidc-provider --cluster `my-eks-cluster` --approve
    ```

    2. Confirm that the OIDC identity provider has been registered with IAM with the following command.

    ```
    aws iam list-open-id-connect-providers --region `us-east-1`
    ```

    The output should look similar to this. Take note of the OIDC's Amazon Resource Name (ARN), you need it in the next step when you create
    a trust policy for the service account.

    ```
    `{
     "OpenIDConnectProviderList": [
     ..
     {
     "Arn": "arn:aws:iam::111122223333:oidc-provider/oidc.eks.us-east-1.amazonaws.com/id/EXAMPLED539D4633E53DE1B71EXAMPLE"
     }
     ]
    }`
    ```

2.  Create a service account for the Amazon EKS cluster. Service accounts provide an identity for processes that run in a _Pod_.
    A Pod is the smallest and simplest Kubernetes object that you can use to deploy a containerized application. Next, create an IAM role
    that the service account can assume to obtain permissions to resources. You can access any AWS service from a Pod that has been configured
    to use a service account that can assume an IAM role with access permissions to that service.
    1. Create a new namespace for the service account. A namespace helps to isolate cluster resources created for this
       tutorial. You can create a new namespace using the following command.

    ```
    kubectl create namespace `my-eks-namespace`
    ```

    2. To use a custom namespace, you have to associate it with a Fargate profile. The following code is an example of this.

    ```
    eksctl create fargateprofile \
        --cluster `my-eks-cluster` \
        --name `my-fargate-profile` \
        --namespace `my-eks-namespace` \
        --labels `*`=`*`
    ```

    3. Create a service account with the name `my-eks-serviceaccount` in the namespace `my-eks-namespace`
       for your Amazon EKS cluster by using the following command.

    ```
    cat >my-serviceaccount.yaml <<EOF
    apiVersion: v1
    kind: ServiceAccount
    metadata:
      name: my-eks-serviceaccount
      namespace: my-eks-namespace
    EOF
    kubectl apply -f my-serviceaccount.yaml
    ```

    4.  Run the following command to create a trust policy file that instructs the IAM role to trust
        your service account. This trust relationship is required before a
        principal can assume a role. You need to make the following edits to the file:

            * For the `Principal`, enter the ARN that IAM returned to the `list-open-id-connect-providers`
             command. The ARN contains your account number and Region.
            * In the `condition` statement, replace the AWS Region and the OIDC id.
            * Confirm that the service account name and namespace are correct.

        You need to attach the trust policy file in
        the next step when you create the IAM role.

    ```
    cat >trust-relationship.json <<EOF
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Federated": "arn:aws:iam::`111122223333`:oidc-provider/oidc.eks.`us-east-1`.amazonaws.com/id/`EXAMPLED539D4633E53DE1B71EXAMPLE`"
                },
                "Action": "sts:AssumeRoleWithWebIdentity",
                "Condition": {
                    "StringEquals": {
                        "oidc.eks.`us-east-1`.amazonaws.com/id/`EXAMPLED539D4633E53DE1B71EXAMPLE`:sub": "system:serviceaccount:`my-eks-namespace`:`my-eks-serviceaccount`",
                        "oidc.eks.`us-east-1`.amazonaws.com/id/`EXAMPLED539D4633E53DE1B71EXAMPLE`:aud": "sts.amazonaws.com"
                    }
                }
            }
        ]
    }
    EOF
    ```

    Optional: You can also add multiple entries in the `StringEquals` or `StringLike` conditions to allow multiple
    service accounts or namespaces to assume the role. To allow your service account to assume an IAM role in a different AWS
    account, see [Cross-account IAM permissions](../../../eks/latest/userguide/cross-account-access.md "../../../eks/latest/userguide/cross-account-access.md") in the _Amazon EKS User Guide_.

3.  Create an IAM role with the name `my-iam-role` for the
    Amazon EKS service account to assume. Attach the trust policy file created in the
    last step to the role. The trust policy specifies the service account and OIDC provider that
    the IAM role can trust.

```
aws iam create-role --role-name `my-iam-role` --assume-role-policy-document file://trust-relationship.json --description "EKS service account role"
```

4.  Assign the IAM role permissions to Amazon Keyspaces by attaching an access policy.
    1. Attach an access policy to define the actions the IAM role can perform on specific Amazon Keyspaces
       resources. For this tutorial we use the AWS managed policy
       `AmazonKeyspacesFullAccess`, because our application is
       going to write data to your Amazon Keyspaces table. As a best practise however, it's recommended
       to create custom access policies that implement the least privileges
       principle. For more information, see [How Amazon Keyspaces works with
       IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md").

    ```
    aws iam attach-role-policy --role-name `my-iam-role` --policy-arn=arn:aws:iam::aws:policy/AmazonKeyspacesFullAccess
    ```

    Confirm that the policy was successfully attached to the IAM role with the following statement.

    ```
    aws iam list-attached-role-policies --role-name `my-iam-role`
    ```

    The output should look like this.

    ```
    `{
     "AttachedPolicies": [
     {
     "PolicyName": "AmazonKeyspacesFullAccess",
     "PolicyArn": "arn:aws:iam::aws:policy/AmazonKeyspacesFullAccess"
     }
     ]
    }`
    ```

    2. Annotate the service account with the Amazon Resource Name (ARN) of the IAM role it can assume. Make sure to update the role ARN with your account ID.

    ```
    kubectl annotate serviceaccount -n `my-eks-namespace` `my-eks-serviceaccount` eks.amazonaws.com/role-arn=arn:aws:iam::`111122223333`:role/`my-iam-role`
    ```

5.  Confirm that the IAM role and the service account are correctly configured.

        1. Confirm that the IAM role's trust policy is correctly configured with the following statement.



        ```
        aws iam get-role --role-name `my-iam-role` --query Role.AssumeRolePolicyDocument
        ```

        The output should look similar to this.



        ```
        `{
         "Version": "2012-10-17",
         "Statement": [
         {
         "Effect": "Allow",
         "Principal": {
         "Federated": "arn:aws:iam::111122223333:oidc-provider/oidc.eks.us-east-1.amazonaws.com/id/EXAMPLED539D4633E53DE1B71EXAMPLE"
         },
         "Action": "sts:AssumeRoleWithWebIdentity",
         "Condition": {
         "StringEquals": {
         "oidc.eks.us-east-1/id/EXAMPLED539D4633E53DE1B71EXAMPLE:aud": "sts.amazonaws.com",
         "oidc.eks.us-east-1.amazonaws.com/id/EXAMPLED539D4633E53DE1B71EXAMPLE:sub": "system:serviceaccount:my-eks-namespace:my-eks-serviceaccount"
         }
         }
         }
         ]
        }`
        ```
        2. Confirm that the Amazon EKS service account is annotated with the IAM role.



        ```
        kubectl describe serviceaccount `my-eks-serviceaccount` -n `my-eks-namespace`
        ```

        The output should look similar to this.



        ```
        `Name: my-eks-serviceaccount
        Namespace:my-eks-namespace
        Labels: <none>
        Annotations: eks.amazonaws.com/role-arn: arn:aws:iam::111122223333:role/my-iam-role
        Image pull secrets: <none>
        Mountable secrets: <none>
        Tokens: <none>
        [...]`
        ```

    After you created the Amazon EKS service account, the IAM role, and configured the required
    relationships and permissions, proceed to [Step 2: Configure the application](EKS-tutorial-step2.md "EKS-tutorial-step2.md").
