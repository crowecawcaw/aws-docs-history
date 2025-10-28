# Auto-discover reports in CodeBuild

With auto-discovery, CodeBuild searches through all your build files after the build phase has completed, searches for any supported
report file types, and automatically creates new test and code coverage report groups and reports. For any discovered report types,
CodeBuild creates new report groups with the following pattern:

```
`<project-name>`-`<report-file-format>`-AutoDiscovered
```

###### Note

If the discovered report files have the same format type, they will be placed in to the same report group or report.

Report auto-discover is configured by your project environment variables:

_`CODEBUILD_CONFIG_AUTO_DISCOVER`_

This variable determines whether report auto-discover is disabled during the build. By default, report auto-discover is enabled
for all builds. To disable this feature, set `CODEBUILD_CONFIG_AUTO_DISCOVER` to `false`.

_`CODEBUILD_CONFIG_AUTO_DISCOVER_DIR`_

(Optional) This variable determines where CodeBuild searches for potential report files. Note that by default,
CodeBuild searches in `**/*` by default.

These environment variables can be modified during the build phase. For example, if you only want to enable report auto-discover
for builds on the `main` git branch, you can check the git branch during the build process and set `CODEBUILD_CONFIG_AUTO_DISCOVER` to false if the build is
not on the `main` branch. Report auto-discover can be disabled using the console or using project environment variables.

###### Topics

- [Configure report auto-discover using the console](#report-auto-discover-configure-console "#report-auto-discover-configure-console")
- [Configure report auto-discover using project environment variables](#report-auto-discover-configure-variable "#report-auto-discover-configure-variable")

## Configure report auto-discover using the console

Use the following procedure to configure report auto-discovery using the console.

###### To configure report auto-discover using the console

1. Create a build project or choose a build project to edit. For information, see [Create a build project in AWS CodeBuild](create-project.md "create-project.md") or [Change build project settings in AWS CodeBuild](change-project.md "change-project.md").
2. In **Environment**, select **Additional configuration**.
3. To disable report auto-discover, in **Report auto-discover**,
   select **Disable report auto-discover**.
4. (Optional) In **Auto-discover directory - optional**, enter a
   directory pattern for CodeBuild to search for supported report format files. Note that CodeBuild
   searches in `**/*` by default.

## Configure report auto-discover using project environment variables

Use the following procedure to configure report auto-discovery using project environment variables.

###### To configure report auto-discover using project environment variables

1. Create a build project or choose a build project to edit. For information, see [Create a build project in AWS CodeBuild](create-project.md "create-project.md") or [Change build project settings in AWS CodeBuild](change-project.md "change-project.md").
2. In **Environment variables**, do the following:
   1. To disable report auto-discover, for **Name**, enter `CODEBUILD_CONFIG_AUTO_DISCOVER`
      and for **Value**, enter `false`. This disables report auto-discover.
   2. (Optional) For **Name**, enter `CODEBUILD_CONFIG_AUTO_DISCOVER_DIR`
      and for **Value**, enter the directory where CodeBuild should search for supported report format files.
      For example, `output/*xml` searches for `.xml` files in the `output` directory
