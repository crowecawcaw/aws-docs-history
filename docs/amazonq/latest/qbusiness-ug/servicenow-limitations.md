Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](qbusiness-availability-change.md "qbusiness-availability-change.md").

# Known limitations for the Amazon Q Business ServiceNow Online connector

The ServiceNow Online connector has the following known limitations:

- There is no REST API to wake up your ServiceNow instance. To activate it when
  it's in hibernation mode, log in to the your ServiceNow instance.
- Because Amazon Q Business uses email address as unique identifiers,
  each user must have a unique email address.
- We don't support ServiceNow access controls.
- We don't support ServiceNow user criteria.
- Only the following ServiceNow roles are supported for incidents:

  - ITIL: This role provides broad access to incident management
    functionality.
  - Custom roles: You can create custom roles with specific incident
    access permissions.
