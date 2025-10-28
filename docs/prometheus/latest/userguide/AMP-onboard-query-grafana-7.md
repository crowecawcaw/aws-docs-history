# Query using Grafana running in an Amazon EKS

cluster

Amazon Managed Service for Prometheus supports the use of Grafana version 7.3.5 and later to query metrics in a
Amazon Managed Service for Prometheus workspace. Versions 7.3.5 and later include support for AWS Signature
Version 4 (SigV4) authentication.

To set up Grafana to work with Amazon Managed Service for Prometheus, you must be logged on to an account that has
the **AmazonPrometheusQueryAccess** policy or the
`aps:QueryMetrics`, `aps:GetMetricMetadata`,
`aps:GetSeries`, and `aps:GetLabels` permissions. For more
information, see [IAM permissions and policies](AMP-and-IAM.md "AMP-and-IAM.md").

## Set up AWS SigV4

Grafana has added a new feature to support AWS Signature Version 4 (SigV4)
authentication. For more information, see [Signature Version 4 signing process](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md"). This feature is not enabled by
default on Grafana servers. The following instructions for enabling this feature
assume that you are using Helm to deploy Grafana on a Kubernetes cluster.

###### To enable SigV4 on your Grafana 7.3.5 or later server

1. Create a new update file to override your Grafana configuration, and name
   it `amp_query_override_values.yaml`.
2. Enter the following content into the file, and save the file. Replace
   `account-id` with the AWS account ID where
   the Grafana server is running.

```
serviceAccount:
    name: "amp-iamproxy-query-service-account"
    annotations:
        eks.amazonaws.com/role-arn: "arn:aws:iam::`account-id`:role/amp-iamproxy-query-role"
grafana.ini:
  auth:
    sigv4_auth_enabled: true
```

In that YAML file content, `amp-iamproxy-query-role` is the
name of the role that you will create in the next section, [Set up IAM roles for service
accounts](#AMP-onboard-query-grafana-7.3-IRSA "#AMP-onboard-query-grafana-7.3-IRSA"). You can replace
this role with your own role name if you already have a role created for
querying your workspace.

You will use this file later, in [Upgrade the Grafana server using
Helm](#AMP-onboard-query-upgrade-grafana "#AMP-onboard-query-upgrade-grafana").

## Set up IAM roles for service

accounts

If you are using a Grafana server in an Amazon EKS cluster, we recommend that you use
IAM roles for service accounts, also known as service roles, for your access
control. When you do this to associate an IAM role with a Kubernetes service
account, the service account can then provide AWS permissions to the containers in
any pod that uses that service account. For more information, see [IAM roles for
service accounts](../../../eks/latest/userguide/iam-roles-for-service-accounts.md "../../../eks/latest/userguide/iam-roles-for-service-accounts.md").

If you have not already set up these service roles for querying, follow the
instructions at [Set up IAM roles for service accounts for the
querying of metrics](set-up-irsa.md#set-up-irsa-query "set-up-irsa.md#set-up-irsa-query") to set up the roles.

You then need to add the Grafana service account in the conditions of the trust
relationship.

###### To add the Grafana service account in the conditions of the trust

relationship

1. From a terminal window, determine the namespace and the service account
   name for your Grafana server. For example, you could use the following
   command.

```
kubectl get serviceaccounts -n `grafana_namespace`
```

2. In the Amazon EKS console, open the IAM role for service accounts that is
   associated with the EKS cluster.
3. Choose **Edit trust relationship**.
4. Update the **Condition** to include the Grafana namespace
   and the Grafana service account name that you found in the output of the
   command in step 1. The following is an example.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Federated": "arn:aws:iam::`111122223333`:oidc-provider/oidc.eks.`us-east-1`.amazonaws.com/id/`EXAMPLED539D4633E53DE1B71EXAMPLE`"
 },
 "Action": "sts:AssumeRoleWithWebIdentity",
 "Condition": {
 "StringEquals": {
 "oidc.eks.`us-east-1`.amazonaws.com/id/`EXAMPLED539D4633E53DE1B71EXAMPLE`:sub": [
 "system:serviceaccount:aws-amp:amp-iamproxy-query-service-account",
 "system:serviceaccount:`grafana-namespace`:`grafana-service-account-name`"
 ],
 "oidc.eks.`us-east-1`.amazonaws.com/id/`EXAMPLED539D4633E53DE1B71EXAMPLE`:aud": "sts.amazonaws.com"
 }
 }
 }
 ]
}`

```

5. Choose **Update trust policy**.

## Upgrade the Grafana server using

Helm

This step upgrades the Grafana server to use the entries that you added to the
`amp_query_override_values.yaml` file in the previous
section.

Run the following commands. For more information about Helm charts for Grafana,
see [Grafana Community Kubernetes
Helm Charts](https://grafana.github.io/helm-charts "https://grafana.github.io/helm-charts").

```
helm repo add grafana https://grafana.github.io/helm-charts
```

```
helm upgrade --install grafana grafana/grafana -n `grafana_namespace` -f ./amp_query_override_values.yaml
```

## Add the Prometheus data

source in Grafana

The following steps explain how to set up the Prometheus data source in Grafana to
query your Amazon Managed Service for Prometheus metrics.

###### To add the Prometheus data source in your Grafana server

1. Open the Grafana console.
2. Under **Configurations**, choose **Data
   sources**.
3. Choose **Add data source**.
4. Choose **Prometheus**.
5. For the HTTP URL, specify the **Endpoint - query URL**
   displayed in the workspace details page in the Amazon Managed Service for Prometheus console.
6. In the HTTP URL that you just specified, remove the
   `/api/v1/query` string that is appended to the URL, because
   the Prometheus data source will automatically append it.
7. Under **Auth**, select the toggle for **SigV4
   Auth** to enable it.

Leave the **Assume Role ARN** and **External
ID** fields blank. Then for **Default
Region**, select the Region where your Amazon Managed Service for Prometheus workspace
is. 8. Choose **Save & Test**.

You should see the following message: **Data source is
working** 9. Test a PromQL query against the new data source:

    1. Choose **Explore**.
    2. Run a sample PromQL query such as:



    ```
    prometheus_tsdb_head_series
    ```
