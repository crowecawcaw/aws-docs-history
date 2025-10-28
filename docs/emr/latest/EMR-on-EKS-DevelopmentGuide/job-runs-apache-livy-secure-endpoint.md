# Setting up a secure Apache Livy endpoint with TLS/SSL

See the following sections to learn more about setting up Apache Livy for Amazon EMR on EKS with end-to-end TLS and SSL encryption.

## Setting up TLS and SSL encryption

To set up SSL encryption on your Apache Livy endpoint, follow these steps.

- [Install the Secrets Store CSI Driver and AWS Secrets and Configuration Provider (ASCP)](../../../secretsmanager/latest/userguide/integrating_csi_driver.md "../../../secretsmanager/latest/userguide/integrating_csi_driver.md") – the
  Secrets Store CSI Driver and ASCP securely store Livy's
  JKS certificates and passwords that the Livy server pod needs to enable SSL. You can also install
  just the Secrets Store CSI Driver and use any other supported secrets provider.
- [Create an ACM certificate](../../../acm/latest/userguide/gs-acm-request-public.md "../../../acm/latest/userguide/gs-acm-request-public.md") – this certificate
  is required to secure the connection between the client and the ALB endpoint.
- Set up a JKS certificate, key password, and keystore password for AWS Secrets Manager – required to secure
  the connection between the ALB endpoint and the Livy server.
- Add permissions to the Livy service account to retrieve secrets from AWS Secrets Manager –
  the Livy server needs these permissions to retrieve secrets from ASCP and add the Livy configurations
  to secure the Livy server. To add IAM permissions to a service account, see Setting up access permissions with IAM roles for service accounts (IRSA).

### Setting up a JKS certificate with a key and a keystore password for AWS Secrets Manager

Follow these steps to set up a JKS certificate with a key and a keystore password.

1. Generate a keystore file for the Livy server.

```
keytool -genkey -alias `<host>` -keyalg RSA -keysize 2048 –dname CN=`<host>`,OU=hw,O=hw,L=`<your_location>`,ST=`<state>`,C=`<country>` –keypass `<keyPassword>` -keystore `<keystore_file>` -storepass `<storePassword>` --validity 3650
```

2. Create a certificate.

```
keytool -export -alias `<host>` -keystore mykeystore.jks -rfc -file `mycertificate.cert` -storepass `<storePassword>`
```

3. Create a truststore file.

```
keytool -import -noprompt -alias `<host>`-file `<cert_file>` -keystore `<truststore_file>` -storepass `<truststorePassword>`
```

4. Save the JKS certificate in AWS Secrets Manager. Replace `livy-jks-secret`
   with your secret and `fileb://mykeystore.jks` with the path to your keystore JKS certificate.

```
aws secretsmanager create-secret \
--name `livy-jks-secret` \
--description "My Livy keystore JKS secret" \
--secret-binary `fileb://mykeystore.jks`
```

5. Save the keystore and key password in Secrets Manager. Make sure to use your own parameters.

```
aws secretsmanager create-secret \
--name `livy-jks-secret` \
--description "My Livy key and keystore password secret" \
--secret-string "{\"keyPassword\":\"`<test-key-password>`\",\"keyStorePassword\":\"`<test-key-store-password>`\"}"
```

6. Create a Livy server namespace with the following command.

```
kubectl create ns `<livy-ns>`
```

7. Create the `ServiceProviderClass` object for the Livy server that has the JKS certificate and the passwords.

```
cat >livy-secret-provider-class.yaml << EOF
apiVersion: secrets-store.csi.x-k8s.io/v1
kind: SecretProviderClass
metadata:
  name: aws-secrets
spec:
  provider: aws
  parameters:
    objects: |
        - objectName: "livy-jks-secret"
          objectType: "secretsmanager"
        - objectName: "livy-passwords"
          objectType: "secretsmanager"

EOF
kubectl apply -f livy-secret-provider-class.yaml -n `<livy-ns>`
```

## Getting started with SSL-enabled Apache Livy

After enabling SSL on your Livy server, you must set up the `serviceAccount` to have access to
the `keyStore` and `keyPasswords` secrets on AWS Secrets Manager.

1. Create the Livy server namespace.

```
kubectl create namespace `<livy-ns>`
```

2. Set up the Livy service account to have access to the secrets in Secrets Manager. For more information about setting up IRSA, see
   [Setting up IRSA while installing Apache Livy](job-runs-apache-livy-irsa.md#job-runs-apache-livy-irsa "job-runs-apache-livy-irsa.md#job-runs-apache-livy-irsa").

```
aws ecr get-login-password \--region region-id | helm registry login \
--username AWS \
--password-stdin ECR-registry-account.dkr.ecr.region-id.amazonaws.com
```

3. Install Livy. For the Helm chart --version parameter, use your Amazon EMR release label, such as `7.1.0`. You must also replace
   the Amazon ECR registry account ID and Region ID with your own IDs. You can find the corresponding
   `ECR-registry-account` value for your AWS Region from
   [Amazon ECR registry accounts by Region](docker-custom-images-tag.md#docker-custom-images-ECR "docker-custom-images-tag.md#docker-custom-images-ECR").

```
helm install `<livy-app-name>` \
  oci://895885662937.dkr.ecr.region-id.amazonaws.com/livy \
  --version 7.10.0 \
  --namespace `livy-namespace-name` \
  --set image=`<ECR-registry-account.dkr.ecr>.<region>`.amazonaws.com/livy/emr-7.10.0:latest \
  --set sparkNamespace=`spark-namespace` \
  --set ssl.enabled=true
  --set ssl.CertificateArn=livy-acm-certificate-arn
  --set ssl.secretProviderClassName=aws-secrets
  --set ssl.keyStoreObjectName=livy-jks-secret
  --set ssl.keyPasswordsObjectName=livy-passwords
  --create-namespace
```

4. Continue from step 5 of the [Installing Apache Livy on Amazon EMR on EKS](job-runs-apache-livy-setup.md#job-runs-apache-livy-install "job-runs-apache-livy-setup.md#job-runs-apache-livy-install").
