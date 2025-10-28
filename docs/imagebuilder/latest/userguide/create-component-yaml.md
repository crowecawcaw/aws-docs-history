# Create a YAML component document for custom components in Image Builder

To build a component, you must provide a YAML or JSON application component document. The
document contains the code that runs during the phases and steps that you define to provide customization
for your image.

Some of the examples in this section create a build component that calls the `UpdateOS`
action module in the AWSTOE component management application. The module updates the
operating system. For more information about the `UpdateOS` action module, see
[UpdateOS](toe-action-modules.md#action-modules-updateos "toe-action-modules.md#action-modules-updateos").

The macOS operating system example uses the `ExecuteBash` action module to install
and verify the `wget` utility. The `UpdateOS` action module doesn't support
macOS. For more information about the `ExecuteBash` action module, see [ExecuteBash](toe-action-modules.md#action-modules-executebash "toe-action-modules.md#action-modules-executebash").
For more information about the phases, steps, and syntax for AWSTOE
application component documents, see
[Use documents in AWSTOE](toe-use-documents.md "toe-use-documents.md").

###### Note

Image Builder determines the component type from the phases that are defined in the component
document as follows:

- **Build** – This is the default component type.
  Anything that is not classified as a test component, is a build component. This
  type of component runs during the image _Build stage_. If this
  build component has a `test` phase defined, that phase runs during
  the _Test stage_.
- **Test** – To qualify as a test component, the
  component document must include only one phase, named `test`. For
  tests that are related to build component configurations, we recommend that you
  don't use a standalone test component. Rather, use the `test` phase
  in the associated build component.
  For more information about how Image Builder uses stages and phases to manage component
  workflow in its build process, see [Use components to customize your Image Builder image](manage-components.md "manage-components.md").

To create a YAML application component document for a sample application, follow the steps on
the tab that matches your image operating system.

Linux

###### Create a YAML component file

Use a file editing tool to create your component document.
Documentation examples use a file named
`update-linux-os.yaml`,
with the following content:

```
# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this
# software and associated documentation files (the "Software"), to deal in the Software
# without restriction, including without limitation the rights to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
name: update-linux-os
description: Updates Linux with the latest security updates.
schemaVersion: 1
phases:
  - name: build
    steps:
    - name: UpdateOS
      action: UpdateOS
# Document End
```

###### Tip

Use a tool like this online [YAML
Validator](https://jsonformatter.org/yaml-validator "https://jsonformatter.org/yaml-validator"), or a YAML lint extension in your code environment to verify
that your YAML is well-formed.

Windows

###### Create a YAML component file

Use a file editing tool to create your component document.
Documentation examples use a file named
`update-windows-os.yaml`,
with the following content:

```
# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this
# software and associated documentation files (the "Software"), to deal in the Software
# without restriction, including without limitation the rights to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
name: update-windows-os
description: Updates Windows with the latest security updates.
schemaVersion: 1.0
phases:
  - name: build
    steps:
      - name: UpdateOS
        action: UpdateOS
# Document End
```

###### Tip

Use a tool like this online [YAML
Validator](https://jsonformatter.org/yaml-validator "https://jsonformatter.org/yaml-validator"), or a YAML lint extension in your code environment to verify
that your YAML is well-formed.

macOS

###### Create a YAML component file

Use a file editing tool to create your component document.
Documentation examples use a file named
`wget-macos.yaml`,
with the following content:

```
name: WgetInstallDocument
description: This is wget installation document.
schemaVersion: 1.0

phases:
  - name: build
    steps:
      - name: WgetBuildStep
        action: ExecuteBash
        inputs:
          commands:
            - |
              PATH=/usr/local/bin:$PATH
              sudo -u ec2-user brew install wget


  - name: validate
    steps:
      - name: WgetValidateStep
        action: ExecuteBash
        inputs:
          commands:
            - |
              function error_exit {
                echo $1
                echo "{\"failureMessage\":\"$2\"}"
                exit 1
              }

              type wget
              if [ $? -ne 0 ]; then
                error_exit "$stderr" "Wget installation failed!"
              fi

  - name: test
    steps:
      - name: WgetTestStep
        action: ExecuteBash
        inputs:
          commands:
            - wget -h
```

###### Tip

Use a tool like this online [YAML
Validator](https://jsonformatter.org/yaml-validator "https://jsonformatter.org/yaml-validator"), or a YAML lint extension in your code environment to verify
that your YAML is well-formed.
