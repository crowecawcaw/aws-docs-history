# Creating multi-variant

feature flags

Feature flag variants enable you to define a set of possible flag values to return for
a request. You can also configure different statuses (enabled or disabled) for
multi-variant flags. When requesting a flag configured with variants, your application
provides context that AWS AppConfig evaluates against a set of user-defined rules. Depending on
the context specified in the request and the rules defined for the variant, AWS AppConfig returns
different flag values to the application.

The following screenshot shows an example of a feature flag with three user-defined
variants and the default variant.

![An example screenshot of a feature flag with variants.](images/flag-variant-example.png)

###### Topics

- [Understanding
  multi-variant feature flag concepts and common use cases](appconfig-creating-multi-variant-feature-flags-concepts.md "appconfig-creating-multi-variant-feature-flags-concepts.md")
- [Understanding
  multi-variant feature flag rules](appconfig-creating-multi-variant-feature-flags-rules.md "appconfig-creating-multi-variant-feature-flags-rules.md")
- [Creating a
  multi-variant feature flag](appconfig-creating-multi-variant-feature-flags-procedures.md "appconfig-creating-multi-variant-feature-flags-procedures.md")
