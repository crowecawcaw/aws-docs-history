# Generate code for devices

Create customized C code for your devices using the managed integrations code generation tools.
This section describes how to generate code from sample files included with the SDK or from
your own specifications. Learn how to use the generation scripts, understand the
workflow process, and create code that matches your device requirements.

###### Topics

- [Prerequisites](#managedintegrations-sdk-codegen-genprereq "#managedintegrations-sdk-codegen-genprereq")
- [Generate code for custom
  .matter files](#managedintegrations-sdk-codegen-genspecfile "#managedintegrations-sdk-codegen-genspecfile")
- [Code generation
  workflow](#managedintegrations-sdk-codegen-genworkflow "#managedintegrations-sdk-codegen-genworkflow")

## Prerequisites

1. Python 3.10 or higher.

2. Start with a .matter file for code generation. The
   End device SDK provides two sample files in the `codgen/matter_files
folder`:

- `custom-air-purifier.matter`
- `aws_camera.matter`

###### Note

These sample files generate code for demo application clusters.

###### Generate code

Run this command to generate code in the out folder:

```
bash ./gen-data-model-api.sh
```

## Generate code for custom

.matter files

To generate the code for a specific `.matter` file or provide your own
`.matter` file, perform the following tasks.

###### To generate the code for custom .matter files

1. Prepare your .matter file
2. Run the generation command:

```
./codegen.sh [--format] configs/dm_basic.json `path-to-matter-file` `output-directory`
```

###### (Optional) To generate code with custom schema

1. Prepare your custom schema in `JSON` format
2. Run the generation command:

```
./codegen.sh [--format] configs/dm_basic.json `path-to-matter-file` `output-directory` --custom-schemas-dir `path-to-custom-schema-directory`
```

The above commands uses several components to transform your `.matter` file into `C` code:

- `codegen.py` from the **ConnectedHomeIP**
  project
- Python plugin located at
  `codegen/py_scripts/iotmi_data_model.py`
- Jinja2 templates from the `codegen/py_scripts/templates`
  folder

The plugin defines the variables to pass to the Jinja2 templates, which are then used
to generate the final C code output. Adding the `--format` flag applies the
Clang format to the generated code.

## Code generation

workflow

The code generation process organizes your .matter file data structures using utility
functions and topological sorting through `topsort.py`. This ensures
proper ordering of data types and their dependencies.

The script then combines your .matter file specifications with Python plugin processing
to extract and format the necessary information. Finally, it applies Jinja2 template
formatting to create the final C code output.

This workflow ensures that your device-specific requirements from the .matter file are
accurately translated into functional C code that integrates with the managed integrations
system.
