**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Troubleshoot Pod Identities for EKS add-ons

If your add-ons are encountering errors while attempting AWS API, SDK, or CLI operations, confirm the following:

- The Pod Identity Agent is installed in your cluster.
  - For information about how to install the Pod Identity Agent, see [Set up the Amazon EKS Pod Identity Agent](pod-id-agent-setup.md "pod-id-agent-setup.md").

- The Add-on has a valid Pod Identity association.
  - Use the AWS CLI to retrieve the associations for the service account name used by the add-on.

  ```
   aws eks list-pod-identity-associations --cluster-name <cluster-name>
  ```

- The IAM role has the required trust policy for Pod Identities.
  - Use the AWS CLI to retrieve the trust policy for an add-on.

  ```
   aws iam get-role --role-name <role-name> --query Role.AssumeRolePolicyDocument
  ```

- The IAM role has the necessary permissions for the add-on.
  - Use AWS CloudTrail to review `AccessDenied` or `UnauthorizedOperation` events .

- The service account name in the pod identity association matches the service account name used by the add-on.
  - For information about the available add-ons, see [AWS add-ons](workloads-add-ons-available-eks.md "workloads-add-ons-available-eks.md").

- Check configuration of MutatingWebhookConfiguration named `pod-identity-webhook`
  - `admissionReviewVersions` of the webhook needs to be `v1beta1` and doesn’t work with `v1`.
