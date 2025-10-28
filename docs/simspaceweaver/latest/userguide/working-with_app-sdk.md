End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# AWS SimSpace Weaver app SDK

The SimSpace Weaver app SDK provides APIs that you can use to control
the entities in your simulation and respond to SimSpace Weaver events. It
includes the following namespace:

- API – core definitions of the API and its use
  Link with the following library:

- `libweaver_app_sdk_cxx_v1_full.so`

###### Important

The library is available for dynamic linking when you run your apps in the AWS Cloud.
You don't need to upload it with your apps.

###### Note

The SimSpace Weaver app SDK APIs control data within your simulation. These APIs
are separate from the SimSpace Weaver service APIs, which control your SimSpace Weaver service
resources (such as simulations, apps, and clocks) in AWS. For more information,
see [SimSpace Weaver API references](api-reference.md "api-reference.md").

###### Topics

- [API methods return a Result](working-with_app-sdk_return-result.md "working-with_app-sdk_return-result.md")
- [Interacting with the app SDK at the top level](working-with_app-sdk_top-level.md "working-with_app-sdk_top-level.md")
- [Simulation management](working-with_app-sdk_sim.md "working-with_app-sdk_sim.md")
- [Subscriptions](working-with_app-sdk_sub.md "working-with_app-sdk_sub.md")
- [Entities](working-with_app-sdk_ent.md "working-with_app-sdk_ent.md")
- [Entity events](working-with_app-sdk_events.md "working-with_app-sdk_events.md")
- [Result and error handling](working-with_app-sdk_result.md "working-with_app-sdk_result.md")
- [Generics and domain types](working-with_app-sdk_generics.md "working-with_app-sdk_generics.md")
- [Miscellaneous app SDK operations](working-with_app-sdk_misc.md "working-with_app-sdk_misc.md")
