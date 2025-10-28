End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# AWS SimSpace Weaver demo framework

The AWS SimSpace Weaver demo framework (demo framework) is a library of utilities
that you can use to develop SimSpace Weaver apps.

###### The demo framework provides

- Code samples and programming patterns for you to use and examine
- Abstractions and utility functions that streamline development for simple apps
- A simpler way to test experimental features of the SimSpace Weaver app SDK
  We designed the SimSpace Weaver app SDK with low-level access to SimSpace Weaver APIs in
  order to deliver higher performance. In contrast, we designed the demo framework
  to provide higher-level abstractions and access to APIs that make SimSpace Weaver
  easier to use. The cost of ease of use is a lower level of performance compared to directly
  using the SimSpace Weaver app SDK. Simulations that can tolerate lower performance (such as
  those without real-time performance requirements) might be good candidates to use the
  demo framework. We recommend that you use the native functionality in the
  SimSpace Weaver app SDK for complex applications because the demo framework
  isn't a complete toolkit.

###### The demo framework includes

- Working code samples that support and demonstrate:
  - App flow management
  - Callback-driven entity event processing

- A set of third-party utility libraries:
  - spdlog (a logging library)
  - A minimal version of AZCore (a math library) that contains only:
    - Vector3
    - Aabb

  - cxxopts (a command line option parser library)

- Utility functions specific to SimSpace Weaver
  The demo framework consists of a library, source files, and CMakeLists.
  The files are included in the SimSpace Weaver app SDK distributable package.
