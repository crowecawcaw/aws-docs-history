# Setting custom headers for an Amplify app

Custom HTTP headers enable you to specify headers for every HTTP response. Response headers
can be used for debugging, security, and informational purposes. You can specify headers in the
Amplify console, or by downloading and editing an app's `customHttp.yml`
file and saving it in the project's root directory. For detailed procedures, see [Setting custom headers](setting-custom-headers.md "setting-custom-headers.md").

Previously, custom HTTP headers were specified for an app either by editing the build
specification (buildspec) in the Amplify console or by downloading and
updating the `amplify.yml` file and saving it in the project's root
directory. We highly recommend migrating custom headers specified in this way out of the buildspec and the
`amplify.yml` file. For instructions, see [Migrating custom headers out of the build specification and amplify.yml](migrate-custom-headers.md "migrate-custom-headers.md").

###### Topics

- [Custom header YAML reference](custom-header-YAML-format.md "custom-header-YAML-format.md")
- [Setting custom headers](setting-custom-headers.md "setting-custom-headers.md")
- [Migrating custom headers out of the build specification and amplify.yml](migrate-custom-headers.md "migrate-custom-headers.md")
- [Monorepo custom header requirements](monorepo-custom-headers.md "monorepo-custom-headers.md")
