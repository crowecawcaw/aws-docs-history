# How AWS OpsWorks for Chef Automate uses

AWS Secrets Manager

OpsWorks is a configuration management service that helps you configure and operate
applications in a cloud enterprise by using OpsWorks for Puppet Enterprise or AWS OpsWorks for Chef Automate.

When you create a new server in AWS OpsWorks CM, OpsWorks CM stores information for the server in
a Secrets Manager [managed secret](service-linked-secrets.md "service-linked-secrets.md") with the prefix
`opsworks-cm`. The cost of the secret is included in the charge for OpsWorks. For
more information, see [Integration with AWS Secrets Manager](../../../opsworks/latest/userguide/data-protection.md#data-protection-secrets-manager "../../../opsworks/latest/userguide/data-protection.md#data-protection-secrets-manager") in the _OpsWorks User Guide_.
