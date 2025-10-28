# Using modular code with the @remote

decorator

You can organize your code into modules for ease of workspace management during
development and still use the @remote function to invoke a function. You can also
replicate the local modules from your development environment to the remote job
environment. To do so, set the parameter `include_local_workdir` to
`True`, as shown in the following code example.

```
@remote(
  include_local_workdir=True,
)
```

###### Note

The @remote decorator and parameter must appear in the main file, rather than in
any of the dependent files.

When `include_local_workdir` is set to `True`, SageMaker AI packages
all of the Python scripts while maintaining the directory structure in the process'
current directory. It also makes the dependencies available in the job's working
directory.

For example, suppose your Python script which processes the
MNIST dataset is divided into a `main.py` script and a dependent
`pytorch_mnist.py` script. `main.py` calls the
dependent script. Also, the `main.py` script contains
code to import the dependency as shown.

```
from mnist_impl.pytorch_mnist import ...
```

The `main.py` file must also contain the `@remote` decorator, and it must set
the `include_local_workdir` parameter to `True`.

The `include_local_workdir` parameter by default includes
all the Python scripts in the directory. You can customize which files you want to upload
to the job by using this parameter in conjunction with the `custom_file_filter`
parameter. You can either pass a function that filters job dependencies to be uploaded to S3,
or a `CustomFileFilter` object that specifies the local directories and files to
ignore in the remote function. You can use `custom_file_filter` only if
`include_local_workdir` is set to `True`—otherwise the parameter is ignored.

The following example uses `CustomFileFilter` to ignore all notebook
files and folders or files named `data` when uploading files to S3.

```
@remote(
   include_local_workdir=True,
   custom_file_filter=CustomFileFilter(
      ignore_name_patterns=[ # files or directories to ignore
        "*.ipynb", # all notebook files
        "data", # folter or file named data
      ]
   )
)
```

The following example demonstrates how you can package an entire workspace.

```
@remote(
   include_local_workdir=True,
   custom_file_filter=CustomFileFilter(
      ignore_pattern_names=[] # package whole workspace
   )
)
```

The following example shows how you can use a function to filter files.

```
import os

def my_filter(path: str, files: List[str]) -> List[str]:
    to_ignore = []
   for file in files:
       if file.endswith(".txt") or file.endswith(".ipynb"):
           to_ignore.append(file)
   return to_ignore

@remote(
   include_local_workdir=True,
   custom_file_filter=my_filter
)
```

## Best practices in

structuring your working directory

The following best practices suggest how you can organize your directory structure
while using the `@remote` decorator in
your modular code.

- Put the @remote decorator in a file that resides at the root level
  directory of the workspace.
- Structure the local modules at the root level.

The following example image shows the recommended directory structure. In this
example structure, the `main.py` script is located at the root level directory.

```
.
├── config.yaml
├── data/
├── main.py <----------------- @remote used here
├── mnist_impl
│ ├── __pycache__/
│ │ └── pytorch_mnist.cpython-310.pyc
│ ├── pytorch_mnist.py <-------- dependency of main.py
├── requirements.txt
```

The following example image shows a directory structure that will result in
inconsistent behavior when it is used to annotate your code with an @remote
decorator.

In this example structure, the `main.py` script that contains the
@remote decorator is **not** located at the root level
directory. The following structure is **NOT** recommended.

```
.
├── config.yaml
├── entrypoint
│ ├── data
│ └── main.py <----------------- @remote used here
├── mnist_impl
│ ├── __pycache__
│ │ └── pytorch_mnist.cpython-310.pyc
│ └── pytorch_mnist.py <-------- dependency of main.py
├── requirements.txt
```
