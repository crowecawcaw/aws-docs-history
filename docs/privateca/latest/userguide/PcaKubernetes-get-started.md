# Get started with AWS Private CA Connector for Kubernetes.

The following topics show how to use AWS Private CA to secure communications in a Kubernetes
cluster. For another example, refer to [Encryption in transit for Kubernetes](https://github.com/aws-samples/sample-encryption-in-transit-for-kubernetes "https://github.com/aws-samples/sample-encryption-in-transit-for-kubernetes") on GitHub.

You can use a private certificate authority to secure communications with your Amazon EKS
clusters. Before you begin, ensure that you have the following:

- An AWS account with appropriate permissions scoped to your security
  policies.

Amazon EKS clusters
JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "IAM",
 "Effect": "Allow",
 "Action": [
 "iam:CreateRole",
 "iam:AttachRolePolicy",
 "iam:GetRole"
 ],
 "Resource": "*"
 },
 {
 "Sid": "EKS",
 "Effect": "Allow",
 "Action": [
 "eks:CreateAddon",
 "eks:DescribeAddon",
 "eks:CreatePodIdentityAssociation",
 "eks:DescribeCluster"
 ],
 "Resource": "*"
 },
 {
 "Sid": "IAMPassRole",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "arn:aws:iam::*:role/CertManagerPrivateCARole"
 }
 ]
}`

```

Other clusters
JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GetAndIssuePCACertificates",
 "Effect": "Allow",
 "Action": [
 "acm-pca:GetCertificate",
 "acm-pca:IssueCertificate"
 ],
 "Resource": "*"
 },
 {
 "Sid": "RolesAnywhere",
 "Effect": "Allow",
 "Action": [
 "rolesanywhere:CreateProfile"
 ],
 "Resource": "*"
 },
 {
 "Sid": "IAM",
 "Effect": "Allow",
 "Action": [
 "iam:CreateRole",
 "iam:AttachRolePolicy"
 ],
 "Resource": "*"
 },
 {
 "Sid": "IAMPassRole",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "arn:aws:iam::*:role/CertManagerPrivateCARole"
 }
 ]
}`

```

- A Kubernetes cluster. To create a Amazon Elastic Kubernetes Service cluster, refer to the [Amazon EKS quickstart
  guide](../../../eks/latest/userguide/quickstart.md "../../../eks/latest/userguide/quickstart.md"). For simplicity, create an environment variable to hold the
  cluster name:

```
export CLUSTER=`aws-privateca-demo`
```

- The AWS Region where your CA and Amazon EKS cluster are located. For simplicity,
  create an environment variable to hold the Region:

```
export REGION=``aws-region``
```

- The Amazon Resource Name (ARN) of a AWS Private CA private certificate authority. For
  simplicity, create an environment variable to hold the private CA ARN:

```
export CA_ARN="arn:aws:acm-pca:`region`:`account`:certificate-authority/`CA_ID`/certificate/`certificate_ID`"
```

To create a private CA, refer to [https://docs.aws.amazon.com/privateca/latest/userguide/create-CA.html](create-CA.md "create-CA.md")Create a
private CA in AWS Private CA

- A computer with the following software installed:
  - [AWS CLI v2](../../../cli/latest/userguide/cli-chap-install.md "../../../cli/latest/userguide/cli-chap-install.md")
    configured
  - [kubectl v1.13+](https://kubernetes.io/docs/tasks/tools/install-kubectl/ "https://kubernetes.io/docs/tasks/tools/install-kubectl/")
  - For non-Amazon EKS clusters, [Helm v3](https://helm.sh/docs/intro/install/ "https://helm.sh/docs/intro/install/")

## Install cert-manager

To use a private CA, you must install the `cert-manager>` add-on that
requests certificates, distributes them, and automates certificate renewal. You must
also install the `aws-private-ca-issuer` plugin that allows you to issue
private certificates from AWS Private CA. Use the following steps to install the add-on and
plugin.

Amazon EKS clusters
Install `cert-manager` as an Amazon EKS add-on:

```
aws eks create-addon \
  --cluster-name `$CLUSTER` \
  --addon-name cert-manager \
  --region $REGION
```

Other clusters
Install `cert-manager` using Helm:

```
helm repo add jetstack https://charts.jetstack.io
helm repo update

helm install cert-manager jetstack/cert-manager \
  --namespace cert-manager \
  --create-namespace \
  --set crds.enabled=true
```

## Configure IAM permissions

The `aws-privateca-issuer` plugin requires permission the interact with
AWS Private CA. For Amazon EKS clusters you use the pod identity. For other clusters you use
AWS Identity and Access Management Roles Anywhere.

Fist, create an IAM policy. The policy uses the
`AWSPrivateCAConnectorForKubernetesPolicy` managed policy. For more
information about the policy, refer to [AWSPrivateCAConnectorForKubernetesPolicy](../../../aws-managed-policy/latest/reference/AWSPrivateCAConnectorForKubernetesPolicy.md "../../../aws-managed-policy/latest/reference/AWSPrivateCAConnectorForKubernetesPolicy.md") in the _AWS Managed
policy reference guide_.

Amazon EKS clusters

1. Create a file named `trust-policy.json` containing the
   following trust policy:

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "TrustPolicyForEKSClusters",
 "Effect": "Allow",
 "Principal": {
 "Service": "pods.eks.amazonaws.com"
 },
 "Action": [
 "sts:AssumeRole",
 "sts:TagSession"
 ]
 }
 ]
}`

```

2. Run the following commands to create an IAM role:

```
ROLE_ARN=$(aws iam create-role \
  --role-name CertManagerPrivateCARole \
  --assume-role-policy-document file://trust-policy.json \
  --region $REGION \
  --output text \
  --query "Role.Arn")

 aws iam attach-role-policy \
  --role-name CertManagerPrivateCARole \
  --policy-arn arn:aws:iam::aws:policy/AWSPrivateCAConnectorForKubernetesPolicy
```

Other clusters

1. Create a trust anchor that trusts the private CA stored in
   `CA_ARN`. For instructions, refer to [Getting started with IAM Roles Anywhere](../../../rolesanywhere/latest/userguide/getting-started.md "../../../rolesanywhere/latest/userguide/getting-started.md"). Create an environment
   variable to store the trust anchor ARN:

```
export TRUST_ANCHOR_ARN=`trustAnchorArn`
```

2. Create a file called `trust-policy.json` containing the
   following trust policy:

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "TrustPolicyForSelfManagedOrOnPremiseClusters",
 "Effect": "Allow",
 "Principal": {
 "Service": "rolesanywhere.amazonaws.com"
 },
 "Action": [
 "sts:AssumeRole",
 "sts:SetSourceIdentity",
 "sts:TagSession"
 ],
 "Condition": {
 "ArnEquals": {
 "aws:SourceArn": [
 "arn:aws:rolesanywhere:us-east-1:123456789012:trust-anchor/TRUST_ANCHOR_ARN"
 ]
 },
 "StringEquals": {
 "aws:PrincipalTag/x509Subject/CN": "aws-privateca-issuer"
 }
 }
 }
 ]
}`

```

3. Run the following commands to create an IAM role:

```
ROLE_ARN=$(aws iam create-role \
  --role-name CertManagerPrivateCARole \
  --assume-role-policy-document file://trust-policy.json \
  --query "Role.Arn" \
  --region $REGION \
  --output text)

 aws iam attach-role-policy \
  --role-name CertManagerPrivateCARole \
  --region $REGION \
  --policy-arn arn:aws:iam::aws:policy/AWSPrivateCAConnectorForKubernetesPolicy
```

## Install and configure

the AWS Private CA cluster issuer

To install the `aws-privateca-connector-for-kubernetes` add-on, use the
following commands:

Amazon EKS clusters
Create the add-on:

```
aws eks create-addon --region $REGION \
  --cluster-name $CLUSTER \
  --addon-name aws-privateca-connector-for-kubernetes \
  --pod-identity-associations "[{
    \"serviceAccount\": \"aws-privateca-issuer\",
    \"roleArn\": \"$ROLE_ARN\"
  }]"
```

Then wait for the add-on to be active:

```
aws eks describe-addon \
  --cluster-name $CLUSTER \
  --addon-name aws-privateca-connector-for-kubernetes \
  --region $REGION \
  --query 'addon.status'
```

Other clusters

1. Create a profile in IAM Roles Anywhere:

```
PROFILE_ARN=$(aws rolesanywhere create-profile \
  --name "privateca-profile" \
  --role-arns "$ROLE_ARN" \
  --region "$REGION" \
  --query 'profile.profileArn' \
  --enabled \
  --output text)
```

2. Generate a client certificate for use with the Connector for Kubernetes and
   IAM Roles Anywhere to authenticate with AWS Private CA:
   1. Generate a private key for the client certificate:

   ```
   openssl genrsa -out client.key 2048
   ```

   2. Generate a certificate signing request (CSR) for the
      client certificate:

   ```
   openssl req -new \
     -key client.key \
     -out client.csr \
     -subj "/CN=aws-privateca-issuer"
   ```

   3. Issue the client certificate from AWS Private CA:

   ```
   CERT_ARN=$(aws acm-pca issue-certificate \
     --signing-algorithm SHA256WITHRSA \
     --csr fileb://client.csr \
     --validity Value=1,Type=DAYS \
     --certificate-authority-arn "$CA_ARN" \
     --region "$REGION" \
     --query 'CertificateArn' \
     --output text)
   ```

   4. Store the client certificate locally:

   ```
   aws acm-pca get-certificate \
     --certificate-authority-arn $CA_ARN \
     --certificate-arn $CERT_ARN \
     --region $REGION \
     --query 'Certificate'
     --output text > pca-issuer-client-cert.pem
   ```

3. Install the AWS Private CA issuer in the cluster with the client
   certificate:
   1. Add the `awspca` Helm repository:

   ```
   helm repo add awspca https://cert-manager.github.io/aws-privateca-issuer
   helm repo update
   ```

   2. Create a namespace:

   ```
   kubectl create namespace aws-privateca-issuer
   ```

   3. Put the certificate created earlier into a secret:

   ```
   kubectl create secret tls aws-privateca-credentials \
     -n aws-privateca-issuer \
     --cert=pca-issuer-client-cert.pem \
     --key=client.key
   ```

4. Install the AWS Private CA issuer with IAM Roles Anywhere:
   1. Create a file named `values.yaml` to configure
      the AWS Private CA issuer plugin to use with IAM Roles Anywhere:

   ```
   cat > values.yaml <<EOF
   env:
     AWS_EC2_METADATA_SERVICE_ENDPOINT: "http://127.0.0.1:9911"

   extraContainers:
     - name: "rolesanywhere-credential-helper"
       image: "public.ecr.aws/rolesanywhere/credential-helper:latest"
       command: ["aws_signing_helper"]
       args:
         - "serve"
         - "--private-key"
         - "/etc/cert/tls.key"
         - "--certificate"
         - "/etc/cert/tls.crt"
         - "--role-arn"
         - "$ROLE_ARN"
         - "--profile-arn"
         - "$PROFILE_ARN"
         - "--trust-anchor-arn"
         - "$TRUST_ANCHOR_ARN"
       volumeMounts:
         - name: cert
           mountPath: /etc/cert/
           readOnly: true

   volumes:
     - name: cert
       secret:
         secretName: aws-privateca-credentials
   EOF
   ```

   2. Install the AWS Private CA issuer with IAM Roles Anywhere:

   ```
   helm install aws-privateca-issuer awspca/aws-privateca-issuer \
     -n aws-privateca-issuer \
     -f values.yaml
   ```

Wait for the issuer to be ready. Use the following command:

```
kubectl wait --for=condition=ready pods --all -n aws-privateca-issuer --timeout=120s
```

And then verify the installation to make sure that all pods have reached the
`READY` state:

```
kubectl -n aws-privateca-issuer get all
```

To configure the `aws-private-ca-cluster-issuer`, create a YAML file named
`cluster-issuer.yaml`containing the configuration of the issuer:

```
cat > cluster-issuer.yaml <<EOF
apiVersion: awspca.cert-manager.io/v1beta1
kind: AWSPCAClusterIssuer
metadata:
  name: aws-privateca-cluster-issuer
spec:
  arn: "$CA_ARN"
  region: "$REGION"
EOF
```

Next, apply the cluster configuration:

```
kubectl apply -f cluster-issuer.yaml
```

Check the status of the issuer:

```
kubectl describe awspcaclusterissuer aws-privateca-cluster-issuer
```

You should see a response similar to the following:

```
Status:
  Conditions:
    Last Transition Time:  2025-08-13T21:00:00Z
    Message:               AWS PCA Issuer is ready
    Reason:                Verified
    Status:                True
    Type:                  Ready
```

## Manage the AWS Private CA client certificate with

cert-manager

If you are not using an Amazon EKS cluster, after you manually bootstrap a trusted certificate in
`aws-privateca-issuer` you can transition to a client authentication
certificate managed by `cert-manager`. This allows `cert-manager`
to automatically renew the client authentication certificate.

1. Create a file called `pca-auth-cert.yaml`:

```
cat > pca-auth-cert.yaml <<EOF
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: aws-privateca-client-cert
  namespace: aws-privateca-issuer
spec:
  secretName: aws-privateca-credentials
  duration: 168h
  renewBefore: 48h
  commonName: aws-privateca-issuer
  privateKey:
    algorithm: ECDSA
    size: 256
    rotationPolicy: Always
  usages:
    - client auth
  issuerRef:
    name: aws-privateca-cluster-issuer
    kind: AWSPCAClusterIssuer
    group: awspca.cert-manager.io
EOF
```

2. Create the new managed client authentication certificate:

```
kubectl apply -f pca-auth-cert.yaml
```

3. Validate that the certificate was created:

```
kubectl get certificate aws-privateca-client-cert -n aws-privateca-issuer
```

You should see a response similar to the following:

```
NAME                        READY   SECRET                      AGE
aws-privateca-client-cert   True    aws-privateca-credentials   19m
```

## Issue your first TLS certificate

Now that the `cert-manager` and `aws-privateca-issuer` are
installed, you can issue a certificate.

Create a YAML file named `certificate.yaml` containing the certificate
resource:

```
cat > certificate.yaml <<EOF
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: example-certificate
  namespace: default
spec:
  secretName: example-certificate-tls
  issuerRef:
    name: aws-privateca-cluster-issuer
    kind: AWSPCAClusterIssuer
    group: awspca.cert-manager.io
  commonName: example.internal
  dnsNames:
    - example.internal
    - api.example.internal
  duration: 2160h # 90 days
  renewBefore: 360h # 15 days
  usages:
    - digital signature
    - key encipherment
    - server auth
EOF
```

Apply the certificate using the following command:

```
kubectl apply -f certificate.yaml
```

You can then check the status of the certificate with the following commands:

```
kubectl get certificate example-certificate
kubectl describe certificate example-certificate
```

You should see a response similar to this:

```
NAME                 READY   SECRET                    AGE
example-certificate  True    example-certificate-tls   30s
```

You can inspect the issued certificate with the following command:

```
kubectl get secret example-certificate-tls -o yaml
```

You can also decode and examine the certificate with the following command:

```
kubectl get secret example-certificate-tls -o jsonpath='{.data.tls\.crt}' | base64 -d | openssl x509 -text -noout
```
