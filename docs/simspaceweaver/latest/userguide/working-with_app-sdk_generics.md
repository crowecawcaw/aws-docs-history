End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Generics and domain types

The SimSpace Weaver app SDK provides the single-precision data types `Api::Vector2F32`
and `Api::BoundingBox2F32`, and the double-precision `Api::Vector2F64` and
`Api::BoundingBox2F64`. These data types are passive data structures with no convenience
methods. Note that the API only uses `Api::Vector2F32` and `Api::BoundingBox2F32`.
You can use these data types to create and modify subscriptions.

The SimSpace Weaver demo framework provides a minimal version of the AzCore math
library, which contains `Vector3` and `Aabb` . For more information,
see the header files in:

- ``sdk-folder`/packaging-tools/samples/ext/DemoFramework/include/AzCore/Math`
