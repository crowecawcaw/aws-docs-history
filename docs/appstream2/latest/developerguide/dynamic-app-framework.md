# Application Entitlements from a Dynamic App

Provider Using the Dynamic Application Framework

###### Note

Managing application entitlement with the Dynamic Application Framework is
currently not supported for Linux-based stacks.

Amazon WorkSpaces Applications supports dynamically building the application catalog that displays for
your users when they stream from an WorkSpaces Applications stack. You can use the API operations
provided by WorkSpaces Applications to develop a dynamic app provider that modifies, in real time, the
applications that users can access on the streaming instance. Alternatively, you can
implement a third-party dynamic app provider that uses these API operations.

###### Note

This feature requires an WorkSpaces Applications Always-On or On-Demand fleet that is joined to a
Microsoft Active Directory domain. For more information, see [Using Active Directory with WorkSpaces Applications](active-directory.md "active-directory.md"). This feature is
not available on multi-session fleets.

###### Contents

- [Example API Operations WorkFlow](manage-app-entitlement-sample-api-workflow.md "manage-app-entitlement-sample-api-workflow.md")
- [Use the Dynamic Application Framework](build-dynamic-app-provider.md "build-dynamic-app-provider.md")
- [Enable Dynamic App Providers](enable-dynamic-app-providers.md "enable-dynamic-app-providers.md")
- [Test Dynamic App Providers](test-dynamic-app-providers.md "test-dynamic-app-providers.md")
- [Additional Resources](additional-resources-dynamic-app-providers.md "additional-resources-dynamic-app-providers.md")
