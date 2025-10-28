# Providing files and Python libraries to Ray jobs

This section provides information that you need for using Python libraries with AWS Glue Ray jobs. You can use
certain common libraries included by default in all Ray jobs. You can also provide your own Python libraries to
your Ray job.

## Modules provided with Ray jobs

You can perform data integration workflows in a Ray job with the following provided packages. These
packages are available by default in Ray jobs.

AWS Glue version 4.0
In AWS Glue 4.0, the Ray (`Ray2.4` runtime) environment provides the following
packages:

- boto3 == 1.26.133
- ray == 2.4.0
- pyarrow == 11.0.0
- pandas == 1.5.3
- numpy == 1.24.3
- fsspec == 2023.4.0

This list includes all packages that would be installed with `ray[data] == 2.4.0`.
Ray Data is supported out of box.

## Providing files to your Ray job

You can provide files to your Ray job with the `--working-dir` parameter. Provide this
parameter with a path to a .zip file hosted on Amazon S3. Within the .zip file, your files must be contained in a
single top-level directory. No other files should be at the top level.

Your files will be distributed to each Ray node before your script begins to run. Consider how this might
impact the disk space that's available to each Ray node. Available disk space is determined by the
WorkerType set in the job configuration. If you want to provide your job data at scale, this mechanism is
not the right solution. For more information on providing data to your job, see [Connecting to data in Ray jobs](edit-script-ray-connections-formats.md "edit-script-ray-connections-formats.md").

Your files will be accessible as if the directory was provided to Ray through the `working_dir`
parameter. For example, to read a file named `sample.txt` in your .zip file's top-level
directory, you could call:

```
@ray.remote
def do_work():
    f = open("sample.txt", "r")
    print(f.read())
```

For more information about `working_dir`, see the [Ray documentation](https://docs.ray.io/en/latest/ray-core/handling-dependencies.html#remote-uris "https://docs.ray.io/en/latest/ray-core/handling-dependencies.html#remote-uris"). This feature behaves
similarly to
Ray's native capabilities.

## Additional Python modules for Ray

jobs

**Additional modules from PyPI**

Ray jobs use the Python Package Installer (pip3) to install additional modules to be used by a Ray script.
You can use the `--pip-install` parameter with a list of comma-separated Python
modules to add a new module or change the version of an existing module.

For example, to update or add a new `scikit-learn` module, use the following key-value pair:

`"--pip-install", "scikit-learn==0.21.3"`

If you have custom modules or custom patches, you can distribute your own libraries from Amazon S3 with the
`--s3-py-modules` parameter. Before uploading your distribution, it might need to be
repackaged and rebuilt. Follow the guidelines in in [Including Python code in Ray jobs](#edit-script-ray-packaging "#edit-script-ray-packaging").

**Custom distributions from Amazon S3**

Custom distributions should adhere to Ray packaging guidelines for dependencies. You can find out how to
build these distributions in the following section. For more information about how Ray sets up dependencies,
see [Environment
Dependencies](https://docs.ray.io/en/latest/ray-core/handling-dependencies.html "https://docs.ray.io/en/latest/ray-core/handling-dependencies.html") in the Ray documentation.

To include a custom distributable after assessing its contents, upload your distributable to a bucket
available to the job's IAM role. Specify the Amazon S3 path to a Python zip archive in your parameter
configuration. If you're providing multiple distributables, separate them by comma. For example:

`"--s3-py-modules", 
 "s3://`s3bucket`/`pythonPackage`.zip"`

**Limitations**

Ray jobs do not support compiling native code in the job environment. You can be limited by this if
your Python dependencies transitively depend on native, compiled code. Ray jobs can run provided binaries,
but they must be compiled for Linux on ARM64. This means you might be able to use the contents of
`aarch64``manylinux` wheels. You can provide your native dependencies in a compiled
form by repackaging a wheel to Ray standards. Typically, this means removing `dist-info` folders
so that there is only one folder at the root at the archive.

You cannot upgrade the version of `ray` or `ray[data]` using this parameter. In
order to use a new version of Ray, you will need to change the runtime field on your job, after we have
released support for it. For more information about supported Ray versions, see [AWS Glue versions](release-notes.md#release-notes-versions "release-notes.md#release-notes-versions").

## Including Python code in Ray jobs

The Python Software Foundation offers standardized behaviors for packaging Python files for use across
different runtimes. Ray introduces limitations to packaging standards that you should be aware of. AWS Glue
does not specify packaging standards beyond those specified to Ray. The following instructions provide
standard guidance on packaging simple Python packages.

Package your files in a `.zip` archive. A directory should be at the root of the archive.
**There should be no other files at the root level of the archive, or this may lead to
unexpected behavior.** The root directory is the package, and its name is used to refer to your
Python code when importing it.

If you provide a distribution in this form to a Ray job with `--s3-py-modules`, you
will be able to import Python code from your package in your Ray script.

Your package can provide a single Python module with some Python files, or you can package together many
modules. When repackaging dependencies, such as libraries from PyPI, **check for
hidden files and metadata directories** inside of those packages.

###### Warning

Certain OS behaviors make make it difficult to properly follow these packaging instructions.

- OSX may add hidden files such as `__MACOSX` to your zip file at the top
  level.
- Windows may add your files to a folder inside the zip automatically, unintentionally creating
  a nested folder.

The following procedures assume you are interacting with your files in Amazon Linux 2 or a similar OS that provides
a distribution of the Info-ZIP `zip` and `zipinfo` utilities. We recommend using these tools
to prevent unexpected behaviors.

To package Python files for use in Ray

1. Create a temporary directory with your package name, then confirm your working directory is its
   parent directory. You can do this with the following commands:

```
cd `parent_directory`
mkdir `temp_dir`
```

2. Copy your files into the temporary directory, then confirm your directory structure. The contents
   of this directory will be directly accessed as your Python module. You can do this with the
   following command:

```
ls -AR `temp_dir`
# my_file_1.py
# my_file_2.py
```

3. Compress your temporary folder using zip. You can do this with the following commands:

```
zip -r `zip_file`.zip `temp_dir`

```

4. Confirm your file is properly packaged. ``zip_file`.zip`
   should now be found in your working directory. You can inspect it with the following command:

```
zipinfo -1 `zip_file`.zip
# temp_dir/
# temp_dir/my_file_1.py
# temp_dir/my_file_2.py
```

To repackage a Python package for use in Ray.

1. Create a temporary directory with your package name, then confirm your working directory is its
   parent directory. You can do this with the following commands:

```
cd `parent_directory`
mkdir `temp_dir`
```

2. Decompress your package and copy the contents into your temporary directory. Remove files related
   to your previous packaging standard, leaving only the contents of the module. Confirm your file
   structure looks correct with the following command:

```
ls -AR `temp_dir`
# my_module
# my_module/__init__.py
# my_module/my_file_1.py
# my_module/my_submodule/__init__.py
# my_module/my_submodule/my_file_2.py
# my_module/my_submodule/my_file_3.py
```

3. Compress your temporary folder using zip. You can do this with the following commands:

```
zip -r `zip_file`.zip `temp_dir`

```

4. Confirm your file is properly packaged. ``zip_file`.zip`
   should now be found in your working directory. You can inspect it with the following command:

```
zipinfo -1 `zip_file`.zip
# temp_dir/my_module/
# temp_dir/my_module/__init__.py
# temp_dir/my_module/my_file_1.py
# temp_dir/my_module/my_submodule/
# temp_dir/my_module/my_submodule/__init__.py
# temp_dir/my_module/my_submodule/my_file_2.py
# temp_dir/my_module/my_submodule/my_file_3.py
```
