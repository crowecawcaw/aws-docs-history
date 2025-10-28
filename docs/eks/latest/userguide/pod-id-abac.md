**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Grant Pods access to AWS resources based on tags

Attribute-based access control (ABAC) grants rights to users through policies which combine attributes together. EKS Pod Identity attaches tags to the temporary credentials to each Pod with attributes such as cluster name, namespace, and service account name. These role session tags enable administrators to author a single role that can work across service accounts by allowing access to AWS resources based on matching tags. By adding support for role session tags, you can enforce tighter security boundaries between clusters, and workloads within clusters, while reusing the same IAM roles and IAM policies.

## Sample policy with tags

Below is an IAM policy example that grants `s3:GetObject` permissions when the corresponding object is tagged with the EKS cluster name.

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:GetObjectTagging"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "s3:ExistingObjectTag/eks-cluster-name": "${aws:PrincipalTag/eks-cluster-name}"
                }
            }
        }
    ]
}
```

## Enable or disable session tags

EKS Pod Identity adds a pre-defined set of session tags when it assumes the role. These session tags enable administrators to author a single role that can work across resources by allowing access to AWS resources based on matching tags.

### Enable session tags

Session tags are automatically enabled with EKS Pod Identity—​no action is required on your part. By default, EKS Pod Identity attaches a set of predefined tags to your session. To reference these tags in policies, use the syntax `${aws:PrincipalTag/` followed by the tag key. For example, `${aws:PrincipalTag/kubernetes-namespace}`.

- `eks-cluster-arn`
- `eks-cluster-name`
- `kubernetes-namespace`
- `kubernetes-service-account`
- `kubernetes-pod-name`
- `kubernetes-pod-uid`

### Disable session tags

AWS compresses inline session policies, managed policy ARNs, and session tags into a packed binary format that has a separate limit. If you receive a `PackedPolicyTooLarge` error indicating the packed binary format has exceeded the size limit, you can attempt to reduce the size by disabling the session tags added by EKS Pod Identity. To disable these session tags, follow these steps:

1. Open the [Amazon EKS console](https://console.aws.amazon.com/eks/home#/clusters "https://console.aws.amazon.com/eks/home#/clusters").
2. In the left navigation pane, select **Clusters**, and then select the name of the cluster that you want to modify.
3. Choose the **Access** tab.
4. In the **Pod Identity associations**, choose the association ID you would like to modify in **Association ID**, then choose **Edit**.
5. Under **Session tags**, choose **Disable session tags**.
6. Choose **Save changes**.

## Cross-account tags

All of the session tags that are added by EKS Pod Identity are _transitive_; the tag keys and values are passed to any `AssumeRole` actions that your workloads use to switch roles into another account. You can use these tags in policies in other accounts to limit access in cross-account scenarios. For more infromation, see [Chaining roles with session tags](../../../IAM/latest/UserGuide/id_session-tags.md#id_session-tags_role-chaining "../../../IAM/latest/UserGuide/id_session-tags.md#id_session-tags_role-chaining") in the _IAM User Guide_.

## Custom tags

EKS Pod Identity can’t add additional custom tags to the `AssumeRole` action that it performs. However, tags that you apply to the IAM role are always available through the same format: `${aws:PrincipalTag/` followed by the key, for example `${aws:PrincipalTag/MyCustomTag}`.

###### Note

Tags added to the session through the `sts:AssumeRole` request take precedence in the case of conflict. For example, say that:

- Amazon EKS adds a key `eks-cluster-name` and value `my-cluster` to the session when EKS assumes the customer role and
- You add an `eks-cluster-name` tag to the IAM role with the value `my-own-cluster`.
  In this case, the former takes precedence and the value for the `eks-cluster-name` tag will be `my-cluster`.
