End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# AWS SimSpace Weaver version 1.15.1

This release is a **required** update
for the Python SDK that was originally released in SimSpace Weaver
version 1.15.0. It fixes a version mismatch issue that caused
Python-based simulations to fail in the AWS Cloud. Use
this version instead of 1.15.0.

## Update an existing Python project to 1.15.1

If you have an existing Python project that you created with
the version 1.15.0 Python SDK, you must perform the following steps
to update it to 1.15.1 so that it can run in the AWS Cloud.

Instead of following this procedure, you can also create a new
Python project with the 1.15.1 Python SDK and move your custom
code to the new project.

###### To update a 1.15.0 Python project to 1.15.1

1. Go to your Python project's folder.
2. In `src/PythonBubblesSample/bin/run-python` change the following line:

```
export PYTHONPATH=$PYTHONPATH:/roapp/lib
```

To the following:

```
export PYTHONPATH=$PYTHONPATH:$LD_LIBRARY_PATH:/roapp/lib
```

3. In `CMakeLists.txt` delete the following lines:
   - ```
     file(COPY "${SDK_PATH}/libweaver_app_sdk_python_v1_$ENV{PYTHON_VERSION}.so" DESTINATION "${ZIP_FILES_DIR}/lib/weaver_app_sdk_v1")
     ```

   ````
   * ```
   file(RENAME "${ZIP_FILES_DIR}/lib/weaver_app_sdk_v1/libweaver_app_sdk_python_v1_$ENV{PYTHON_VERSION}.so" "${ZIP_FILES_DIR}/lib/weaver_app_sdk_v1/libweaver_app_sdk_python_v1.so")
   ````

   - ```
     message("    * COPYING WEAVER PYTHON SDK TO BUILD DIR ${ZIP_FILES_DIR}....")
     ```

   ````
   * ```
   file(COPY ${SDK_DIR} DESTINATION ${ZIP_FILES_DIR}/lib/weaver_app_sdk_v1)
   ````

## Troubleshooting for version 1.15.1

### After updating a 1.15.0 Python simulation,

it fails to start in the AWS Cloud

Symptoms: After approximately 5-10 minutes after you start the simulation,
the simulation management log reports an `internal error` and the simulation status
is `FAILED`.

This can happen if a library file from the 1.15.0 Python SDK is included in an app zip file. Make sure
that you completed the steps to update your project,
and make sure that `libweaver_app_sdk_python_v1.so` isn't in your zip files or
referenced in any way.

## Frequently asked questions about version 1.15.1

###### Does this release affect anything other than the Python SDK?

No.

###### Do I have to update to version 1.15.1?

You don't have to update to 1.15.1 if you don't intend to use Python for your spatial apps.
If you updated to 1.15.0, your Python-based simulations won't run in the AWS Cloud. We recommend
that you update to 1.15.1 if you use 1.15.0.

###### What is `$LD_LIBRARY_PATH`?

It's the location of the Python SDK when your simulation runs in the AWS Cloud. This
is new for 1.15.1. We made this change to avoid Python version problems in the future. Linking
to that directory is functionally the same as linking to
`libweaver_app_sdk_python_v1.so` in 1.15.0.
