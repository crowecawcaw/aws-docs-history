# Set up custom domains after RES installation

###### Note

_Prerequisites_: You must store Certificate and PrivateKey
contents in a Secrets Manager secret before performing these steps.

###### Add certs to the web client

1. Update the cert attached to the listener of the external-alb load balancer:
   1. Navigate to the RES external load balancer in the AWS console under
      **EC2** > **Load Balancing** >
      **Load Balancers**.
   2. Search for the load balancer that follows the naming convention
      ``<env-name>`-external-alb`.
   3. Check the listeners attached to the load balancer.
   4. Update the listener that has a Default SSL/TLS certificate attached with
      the new certificate details.
   5. Save your changes.

2. In the cluster-settings table:
   1. Find the cluster-settings table in DynamoDB -> Tables ->
      ``<env-name>`.cluster-settings`.
   2. Go to **Explore Items** and **Filter by Attribute**
      – name "key", Type "string", condition "contains", and value
      "external_alb".
   3. Set `cluster.load_balancers.external_alb.certificates.provided`
      to True.
   4. Update the value of
      `cluster.load_balancers.external_alb.certificates.custom_dns_name`.
      This is the custom domain name for web user interface.
   5. Update the value of
      `cluster.load_balancers.external_alb.certificates.acm_certificate_arn`.
      This is the Amazon Resource Name (ARN) for the corresponding certificate stored
      in Amazon Certificate Manager (ACM).

3. Update the corresponding Route53 subdomain record you created for your web client
   to point to the DNS name of the external alb load balancer
   `<env-name>-external-alb`.
4. If SSO is already configured in the environment, re-configure SSO with the same
   inputs as you used initially from the **Environment Management** >
   **Identity management** > **Single Sign-On** >
   **Status** > **Edit** button in the RES
   web portal.

###### Add certs to the VDIs

1. Grant the RES application permission to perform a GetSecret operation on the
   secret by adding the following tags to the secrets:
   - `res:EnvironmentName` :
     `<env-name>`
   - `res:ModuleName` :
     `virtual-desktop-controller`

2. In the cluster-settings table:
   1. Find the cluster-settings table in DynamoDB -> Tables ->
      ``<env-name>`.cluster-settings`.
   2. Go to **Explore Items** and **Filter by Attribute**
      – name "key", Type "string", condition "contains", and value
      "dcv_connection_gateway".
   3. Set `vdc.dcv_connection_gateway.certificate.provided` to
      True.
   4. Update the value of
      `vdc.dcv_connection_gateway.certificate.custom_dns_name`.
      This is the custom domain name for VDI access.
   5. Update the value of
      `vdc.dcv_connection_gateway.certificate.certificate_secret_arn`.
      This is the ARN for the secret that holds the Certificate contents.
   6. Update the value of
      `vdc.dcv_connection_gateway.certificate.private_key_secret_arn`.
      This is the ARN for the secret that holds the Private Key contents.

3. Update the launch template used for the gateway instance:
   1. Open the Auto Scaling group in the AWS Console under **EC2**
      > **Auto Scaling** >
      > **Auto Scaling Groups**.
   2. Select the gateway auto scaling group that corresponds to the RES
      environment. The name follows the naming convention
      ``<env-name>`-vdc-gateway-asg`.
   3. Find and open the Launch Template in the details section.
   4. Under **Details** > **Actions** >
      choose **Modify template** (Create new version).
   5. Scroll down to **Advanced details**.
   6. Scroll to the very bottom, to **User data**.
   7. Look for the words `CERTIFICATE_SECRET_ARN` and
      `PRIVATE_KEY_SECRET_ARN`. Update these values with the ARNs
      given to the secrets that hold the Certificate (see step 2.c) and Private
      Key (see step 2.d) contents.
   8. Ensure the Auto Scaling group is configured to use the recently created
      version of the launch template (from the Auto Scaling group page).

4. Update the corresponding Route53 subdomain record you created for your virtual
   desktops to point to the DNS name of the external nlb load balancer:
   ``<env-name>`-external-nlb`.
5. Terminate the existing dcv-gateway instance:
   ``<env-name>`-vdc-gateway` and wait
   for a new one to spin up.
