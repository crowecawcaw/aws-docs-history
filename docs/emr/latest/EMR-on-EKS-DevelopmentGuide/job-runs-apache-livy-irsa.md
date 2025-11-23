# Setting up access permissions with IAM roles for service accounts (IRSA)

By default, the Livy server and Spark application's driver and executors don't have access to AWS resources. The server service account and spark service account
controls access to AWS resources for the Livy server and spark application's pods. To grant access, you need to map the service accounts with an IAM role that has the necessary AWS permissions.

You can set up IRSA mapping before you install Apache Livy, during the installation, or after you finish the installation.

## Setting up IRSA while installing Apache Livy (for server service account)

###### Note

This mapping is supported only for the server service account.

1. Make sure that you have finished [setting up Apache Livy for Amazon EMR on EKS](job-runs-apache-livy-setup.md "job-runs-apache-livy-setup.md") and
   are in the middle of [installing Apache Livy with Amazon EMR on EKS](job-runs-apache-livy-install.md "job-runs-apache-livy-install.md").
2. Create a Kubernetes namespace for the Livy server. In this example, the name of the namespace is `livy-ns`.
3. Create an IAM policy that includes the permissions for the AWS services for which you want your pods to access. The following example creates an IAM policy of getting
   Amazon S3 resources for the Spark entry point.

```
cat >`my-policy.json` <<EOF{
"Version": "2012-10-17",
    "Statement": [
        {
"Effect": "Allow",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::`my-spark-entrypoint-bucket`"
        }
    ]
}
EOF

aws iam create-policy --policy-name `my-policy` --policy-document file://`my-policy.json`
```

4. Use the following command to set your AWS account ID to a variable.

```
account_id=$(aws sts get-caller-identity --query "Account" --output text)
```

5. Set the OpenID Connect (OIDC) identity provider of your cluster to an environment variable.

```
oidc_provider=$(aws eks describe-cluster --name `my-cluster` --region $AWS_REGION --query "cluster.identity.oidc.issuer" --output text | sed -e "s/^https:\/\///")
```

6. Set variables for the namespace and name of the service account. Be sure to use your own values.

```
export namespace=default
export service_account=my-service-account
```

7. Create a trust policy file with the following command. If you want to grant access of the role to all service accounts within a namespace, copy the following command, and replace
   `StringEquals` with `StringLike` and replace `$service_account` with `*`.

```
cat >trust-relationship.json <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Federated": "arn:aws:iam::$account_id:oidc-provider/$oidc_provider"
      },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringEquals": {
          "$oidc_provider:aud": "sts.amazonaws.com",
          "$oidc_provider:sub": "system:serviceaccount:$namespace:$service_account"
        }
      }
    }
  ]
}
EOF

```

8. Create the role.

```
aws iam create-role --role-name `my-role` --assume-role-policy-document file://trust-relationship.json --description "`my-role-description`"
```

9. Use the following Helm install command to set the `serviceAccount.executionRoleArn` to map IRSA. The following is an example of the Helm install command.
   You can find the corresponding `ECR-registry-account` value for your AWS Region from
   [Amazon ECR registry accounts by Region](docker-custom-images-tag.md#docker-custom-images-ECR "docker-custom-images-tag.md#docker-custom-images-ECR").

```
helm install livy-demo \
  oci://895885662937.dkr.ecr.us-west-2.amazonaws.com/livy \
  --version 7.12.0 \
  --namespace `livy-ns` \
  --set image=`ECR-registry-account.dkr.ecr.region-id`.amazonaws.com/livy/emr-7.12.0:latest \
  --set sparkNamespace=`spark-ns` \
  --set serviceAccount.executionRoleArn=arn:aws:iam::123456789012:role/`my-role`
```

## Mapping IRSA to a Spark service account

Before you map IRSA to a Spark service account, make sure that you have completed the following items:

- Make sure that you have finished [setting up Apache Livy for Amazon EMR on EKS](job-runs-apache-livy-setup.md "job-runs-apache-livy-setup.md") and
  are in the middle of [installing Apache Livy with Amazon EMR on EKS](job-runs-apache-livy-install.md "job-runs-apache-livy-install.md").
- You must have an existing IAM OpenID Connect (OIDC) provdider for your cluster. To see if you already have one
  or how to create one, see [Create an IAM OIDC provider for your cluster](../../../eks/latest/userguide/enable-iam-roles-for-service-accounts.md "../../../eks/latest/userguide/enable-iam-roles-for-service-accounts.md").
- Make sure that you have installed version 0.171.0 or later of the `eksctl` CLI installed or AWS CloudShell. To install or update
  `eksctl`, see [Installation](https://eksctl.io/installation/ "https://eksctl.io/installation/") of the `eksctl` documentation.

Follow these steps to map IRSA to your Spark service account:

1. Use the following command to get the Spark service account.

```
SPARK_NAMESPACE=`<spark-ns>`
LIVY_APP_NAME=`<livy-app-name>`
kubectl --namespace $SPARK_NAMESPACE describe sa -l "app.kubernetes.io/instance=$LIVY_APP_NAME" | awk '/^Name:/ {print $2}'
```

2. Set your variables for the namespace and name of the service account.

```
export namespace=`default`
export service_account=`my-service-account`
```

3. Use the following command to create a trust policy file for the IAM role. The following example gives permission to all service accounts
   within the namespace to use the role. To do so, replace `StringEquals` with `StringLike` and replace `$service_account` with \*.

```
cat >trust-relationship.json <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Federated": "arn:aws:iam::$account_id:oidc-provider/$oidc_provider"
      },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringEquals": {
          "$oidc_provider:aud": "sts.amazonaws.com",
          "$oidc_provider:sub": "system:serviceaccount:$namespace:$service_account"
        }
      }
    }
  ]
}
EOF

```

4. Create the role.

```
aws iam create-role --role-name `my-role` --assume-role-policy-document file://`trust-relationship.json` --description "my-role-description"
```

5. Map the server or spark service account with the following `eksctl` command. Make sure to use your own values.

```
 eksctl create iamserviceaccount --name `spark-sa` \
 --namespace spark-namespace --cluster `livy-eks-cluster` \
 --attach-role-arn arn:aws:iam::`0123456789012`:role/`my-role` \
 --approve --override-existing-serviceaccounts
```
