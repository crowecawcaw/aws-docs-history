End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Launching the Unreal Engine view client

Navigate to:

```
`sdk-folder`/Samples/PathfindingSample/tools/cloud
```

1. Run one of the following commands:
   - Docker: `python quick-start.py`
   - WSL: `python quick-start.py --al2`

2. Get the IP address and “Actual” port number. These will be in the console output from running quick-start.py, or get them
   by following the procedures at [Get the IP address and port number of a custom app](working-with_get-ip.md "working-with_get-ip.md").
3. Navigate to:

```
sdk-folder/Clients/TCP/UnrealClient/lib
```

4. Run the following commands to build the NNG library:

```
cmake -S . -B build
cmake --build build --config RelWithDebInfo
cmake --install build
```

5. In a **text editor**, open `view_app_url.txt`.
6. Update the URL with the IP address and port number for your view app: `tcp://ip-address:actual-port-number` (it should look like `tcp://198.51.100.135:1234`).
7. In **Unreal editor**, choose **play**.

## Troubleshooting

- **NNG CMake install step fails with “Maybe need administrative privileges“:**

```
CMake Error at build/_deps/nng-build/src/cmake_install.cmake:39 (file):
  file cannot create directory: C:/Program Files
  (x86)/ThirdPartyNngBuild/lib.  Maybe need administrative privileges.
Call Stack (most recent call first):
  build/_deps/nng-build/cmake_install.cmake:37 (include)
  build/cmake_install.cmake:73 (include)
```

    + **Resolution:** If `nng.lib` or `nng.so` exist in the UnrealClient/lib directory, this error can be safely ignored. If not, then try running the cmake build commands in a terminal with administrator privileges.

- **“CMake to find a package configuration file provided by nng”:**

```
CMake Error at CMakeLists.txt:23 (find_package):
By not providing "Findnng.cmake" in CMAKE_MODULE_PATH this project has
 asked CMake to find a package configuration file provided by "nng", but
 CMake did not find one.
```

    + **Resolution:** CMake is having trouble finding the `Findnng.cmake` file. When building with CMake, add the argument `-DTHIRD_PARTY_LIB_PATH sdk-folder/ThirdParty`. Ensure the `Findnng.cmake` file is still in the `ThirdParty` directory before rerunning the CMake build.




    ```
    cmake -S . -B build -DTHIRD_PARTY_LIB_PATH sdk-folder/ThirdParty
    cmake --build build --config RelWithDebInfo
    cmake --install build
    ```
