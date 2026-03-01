# Creating a feature flag configuration profile in AWS AppConfig

You can use feature flags to enable or disable features within your applications or to
configure different characteristics of your application features using flag attributes.
AWS AppConfig stores feature flag configurations in the AWS AppConfig hosted configuration store in a
feature flag format that contains data and metadata about your flags and the flag
attributes.

###### Note

When you create a feature flag configuration profile, you can create a basic feature
flag as part of the configuration profile workflow. AWS AppConfig also supports multi-variant
feature flags. _Multi-variant feature flags_ enable you to define a set
of possible flag values to return for a request. When requesting a flag configured with
variants, your application provides context that AWS AppConfig evaluates against a set of
user-defined rules. Depending on the context specified in the request and the rules
defined for the variant, AWS AppConfig returns different flag values to the application.

To create multi-variant feature flags, create a configuration profile first, and then
edit any flags within the configuration profile to add variants. For more information, see
[Creating multi-variant feature flags](appconfig-creating-multi-variant-feature-flags.md "appconfig-creating-multi-variant-feature-flags.md").

###### Topics

- [Understanding feature flag attributes](#appconfig-creating-configuration-profile-feature-flag-attributes "#appconfig-creating-configuration-profile-feature-flag-attributes")
- [Creating a feature flag configuration profile (console)](appconfig-creating-feature-flag-configuration-create-console.md "appconfig-creating-feature-flag-configuration-create-console.md")
- [Creating a feature flag configuration profile (command line)](appconfig-creating-feature-flag-configuration-commandline.md "appconfig-creating-feature-flag-configuration-commandline.md")
- [Creating multi-variant feature flags](appconfig-creating-multi-variant-feature-flags.md "appconfig-creating-multi-variant-feature-flags.md")
- [Understanding the type reference for AWS.AppConfig.FeatureFlags](appconfig-type-reference-feature-flags.md "appconfig-type-reference-feature-flags.md")
- [Saving a previous feature flag version to a new version](appconfig-creating-configuration-profile-feature-flags-editing-version.md "appconfig-creating-configuration-profile-feature-flags-editing-version.md")

## Understanding feature flag attributes

When you create a feature flag configuration profile—or create a new flag
within an existing configuration profile—you can specify attributes and
corresponding constraints for the flag. An attribute is a field that you associate with
your feature flag to express properties related to your feature flag. Attributes are
delivered to your application with your flag key and the `enable` or
`disable` value of the flag.

Constraints ensure that any unexpected attribute values are not deployed to your
application. The following image shows an example.

![Example of flag attributes for an AWS AppConfig feature flag](images/appconfig-flag-attributes.png)

###### Note

Note the following information about flag attributes.

- For attribute names, the word "enabled" is reserved. You can't create a feature
  flag attribute called "enabled". There are no other reserved words.
- The attributes of a feature flag are only included in the
  `GetLatestConfiguration` response if that flag is enabled.
- Flag attribute keys for a given flag must be unique.

AWS AppConfig supports the following types of flag attributes and their corresponding
constraints.

| Type             | Constraint                                              | Description                                         |
| ---------------- | ------------------------------------------------------- | --------------------------------------------------- |
| **String**       | Regular Expression                                      | Regex pattern for the string                        |
| Enum             | List of acceptable values for the string                |
| **Number**       | Minimum                                                 | Minimum numeric value for the attribute             |
| Maximum          | Maximum numeric value for the attribute                 |
| **Boolean**      | None                                                    | None                                                |
| **String array** | Regular Expression                                      | Regex pattern for the elements of the array         |
| Enum             | List of acceptable values for the elements of the array |
| **Number array** | Minimum                                                 | Minimum numeric value for the elements of the array |
| Maximum          | Maximum numeric value for the elements of the array     |
