# Access to an AWS

service

Many AWS services require that you use roles to control what that service can access. A
role that a service assumes to perform actions on your behalf is called a [service role](id_roles.md#iam-term-service-role "id_roles.md#iam-term-service-role"). When a role serves a specialized purpose
for a service, it can be categorized as a [service-linked
role](id_roles.md#iam-term-service-linked-role "id_roles.md#iam-term-service-linked-role"). See the [AWS documentation](../../../index.md "../../../index.md") for each
service to see if it uses roles and to learn how to assign a role for the service to use.

For details about creating a role to delegate access to a service offered by AWS, see
[Create a role to delegate permissions to an
AWS service](id_roles_create_for-service.md "id_roles_create_for-service.md").
