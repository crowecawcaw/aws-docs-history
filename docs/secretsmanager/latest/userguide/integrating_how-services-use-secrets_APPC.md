# How AWS AppConfig uses

AWS Secrets Manager

AWS AppConfig is a capability of AWS Systems Manager that you can use to create, manage, and quickly
deploy application configurations. A configuration can contain credential data or other
sensitive information stored in Secrets Manager. When you create a freeform configuration profile, you
can choose Secrets Manager as the source of your configuration data. For more information, see [Creating a freeform configuration profile](../../../appconfig/latest/userguide/appconfig-creating-configuration-and-profile.md#appconfig-creating-configuration-and-profile-free-form-configurations "../../../appconfig/latest/userguide/appconfig-creating-configuration-and-profile.md#appconfig-creating-configuration-and-profile-free-form-configurations") in the
_AWS AppConfig User Guide_. For information about how AWS AppConfig handles secrets
that have automatic rotation turned on, see [Secrets Manager key rotation](../../../appconfig/latest/userguide/appconfig-security.md#appconfig-security-secrets-manager-key-rotation "../../../appconfig/latest/userguide/appconfig-security.md#appconfig-security-secrets-manager-key-rotation") in the _AWS AppConfig User Guide_.
