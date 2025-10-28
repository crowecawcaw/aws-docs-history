# Initializing Oracle Database@AWS in a trusted account

A trusted account is an AWS account that you designate as eligible to receive resource
shares. It must be another individual AWS account in your AWS organization. Before you can
use shared Oracle Database@AWS resources in a trusted account, you must initialize the service.
Initialization creates the necessary metadata and establishes the connection between your
AWS account and Oracle Cloud Infrastructure.

###### Topics

- [What is Oracle Database@AWS
  initialization?](#initialize-service-overview "#initialize-service-overview")
- [Next steps](#initialize-service-next-steps "#initialize-service-next-steps")

## What is Oracle Database@AWS

initialization?

After a resource has been shared with your account, you must initialize the
Oracle Database@AWS service before you can access or use the shared resource. If you try to
use Oracle Database@AWS APIs without initializing the service first, you receive an
error.

Initialization is a one-time process. It creates the necessary metadata and
establishes a connection between your AWS account and Oracle Cloud Infrastructure.

You can initialize the service using either the AWS Management Console or the AWS CLI.

1. Open the Oracle Database@AWS console at [https://console.aws.amazon.com/odb/](https://console.aws.amazon.com/odb/ "https://console.aws.amazon.com/odb/").
2. If this is your first time accessing the Oracle Database@AWS console in this
   account, you see a welcome page.
3. Choose **Activate account**.
4. The service initialization process begins. This process might take a few
   minutes to complete.
5. Refresh the welcome page periodically until the **Activate
   account** button changes to the **Dashboard**
   button.
6. Choose **Dashboard** to begin using Oracle Database@AWS.
   To initialize Oracle Database@AWS in your trusted account using the AWS CLI, use the
   `initialize-service` command.

```
aws odb initialize-service
```

To check the initialization status, use the `get-oci-onboarding-status`
command.

```
aws odb get-oci-onboarding-status
```

When initialization is complete, the output shows a status of
`ACTIVE_LIMITED`, indicating that your account can access shared
resources but can't create a new Exadata infrastructure or ODB network.

## Next steps

After you initialize Oracle Database@AWS in your trusted account, you can do the
following:

- View shared resources using the `list` and `get` commands or in the AWS console.
- Create VM clusters and Autonomous VM clusters on a shared Exadata infrastructure and ODB network.
- Create an ODB peering connection on a shared ODB network.

For more information about working with shared resources, see [Working with shared Oracle Database@AWS resources
in a trusted account](working-with-shared-resources.md "working-with-shared-resources.md").
