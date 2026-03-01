# Enabling TLS for Amazon ECS Service Connect

You enable traffic encryption when you create or update a Service Connect
service.

###### To enable traffic encryption for a service in an existing namespace using the AWS Management Console

1. You need to have the infrastructure IAM role. For more information about
   this role, see [Amazon ECS infrastructure IAM role](infrastructure_IAM_role.md "infrastructure_IAM_role.md").
2. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
3. In the navigation pane, choose **Namespaces**.
4. Choose the **Namespace** with the
   **Service** you'd like to enable traffic encryption
   for.
5. Choose the **Service** you'd like to enable traffic
   encryption for.
6. Choose **Update Service** in the top right corner and
   scroll down to the Service Connect section.
7. Choose **Turn on traffic encryption** under your service
   information to enable TLS.
8. For **Service Connect TLS role**, choose an existing
   infrastructure IAM role or create a new one.
9. For **Signer certificate authority**, choose an existing
   certificate authority or create a new one.

For more information, see see [AWS Private Certificate Authority certificates and Service Connect](service-connect-tls.md#service-connect-tls-certificates "service-connect-tls.md#service-connect-tls-certificates"). 10. For **Choose an AWS KMS key**, choose an AWS owned
and managed key or you can choose a different key. You can also choose to
create a new one.
For an example of using the AWS CLI to configure TLS for your service, [Configuring Amazon ECS Service Connect with the AWS CLI](create-service-connect.md "create-service-connect.md").
