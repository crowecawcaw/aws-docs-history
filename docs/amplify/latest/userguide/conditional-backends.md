# Conditional backend builds (Gen 1 apps only)

###### Note

The information in this section is for Gen 1 apps only. Amplify Gen 2 introduces a
TypeScript-based, code-first developer experience. Therefore, this feature isn't
necessary for Gen 2 backends.

Amplify supports conditional backend builds on all branches in a Gen 1 app. To
configure conditional backend builds, set the `AMPLIFY_DIFF_BACKEND` environment
variable to `true`. Enabling conditional backend builds will help speed up
builds where changes are made only to the frontend.

When you enable diff based backend builds, at the start of each build, Amplify
attempts to run a diff on the `amplify` folder in your repository. If Amplify
doesn't find any differences, it skips the backend build step, and doesn't update your
backend resources. If your project doesn't have an `amplify` folder in your
repository, Amplify ignores the value of the `AMPLIFY_DIFF_BACKEND`
environment variable. For instructions on setting the `AMPLIFY_DIFF_BACKEND`
environment variable, see [Configuring diff based backend builds for a Gen 1
app](edit-build-settings.md#enable-diff-backend "edit-build-settings.md#enable-diff-backend").

If you currently have custom commands specified in the build settings of your backend
phase, conditional backend builds won't work. If you want those custom commands to run, you
must move them to the frontend phase of your build settings in your app's
`amplify.yml` file. For more information about updating the
`amplify.yml` file, see [Build specification reference](yml-specification-syntax.md "yml-specification-syntax.md").
