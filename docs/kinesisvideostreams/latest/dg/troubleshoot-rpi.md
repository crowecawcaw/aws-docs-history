# Troubleshooting build issues on C++ producer SDK

for Raspberry Pi

If you encounter a build issue and want to try different CMake arguments, make
sure to perform a clean build. Delete the `open-source`,
`dependency`, and `build` folders before you try
again.

## Build issues with OpenSSL

If you receive output similar to the following, it indicates that OpenSSL has
incorrectly detected your system architecture.

```
crypto/md5/md5-aarch64.S: Assembler messages:
crypto/md5/md5-aarch64.S:3: Error: unrecognized symbol type ""
crypto/md5/md5-aarch64.S:6: Error: bad instruction `stp x19,x20,[sp,#-80]!'
crypto/md5/md5-aarch64.S:7: Error: bad instruction `stp x21,x22,[sp,#16]'
crypto/md5/md5-aarch64.S:8: Error: bad instruction `stp x23,x24,[sp,#32]'
crypto/md5/md5-aarch64.S:9: Error: bad instruction `stp x25,x26,[sp,#48]'
```

In this example, it is attempting to build a 64-bit version
(`linux-aarch64`) when this Raspberry Pi is actually 32-bit. Some
Raspberry Pi devices have a 64-bit kernel, but a 32-bit user space.

Determine which architecture OpenSSL is trying to build for. You can find the log
line during the `configure` step for OpenSSL:

```
[ 33%] Performing update step for 'project_libopenssl'
-- Already at requested tag: OpenSSL_1_1_1t
[ 44%] No patch step for 'project_libopenssl'
[ 55%] Performing configure step for 'project_libopenssl'
Operating system: x86_64-whatever-linux2
Configuring OpenSSL version 1.1.1t (0x1010114fL) for linux-x86_64
Using os-specific seed configuration
Creating configdata.pm
Creating Makefile
```

Verify your system's architecture:

- Review the kernel bit-ness: run `uname -m`
- Review the user space bit-ness: run `getconf LONG_BIT`

You can also review your CPU information with `cat /proc/cpuinfo`
or `lscpu` commands.

**Resolution:**

To resolve this issue, add the following CMake argument when building, to ensure
OpenSSL builds correctly for the 32-bit ARM architecture:

```
-DBUILD_OPENSSL_PLATFORM=linux-armv4
```

## Troubleshoot `kvssink` loading issues in GStreamer

Confirm `GST_PLUGIN_PATH`

Ensure the `GST_PLUGIN_PATH` environment variable in your current shell session points to the directory containing `kvssink`. Environment variables are session-specific, so you'll need to set them for each new session. To make this change permanent, see “Update your shell's start-up script to include setting the GST_PLUGIN_PATH environment variable”.

**Error: Cannot open shared object file: No such file or
directory**

If you encounter the error `Cannot open shared object file: No such file or directory`, run the following command:

```
gst-inspect-1.0 /`path`/`to`/libgstkvssink.so
```

If you receive the following output, it indicates that the dynamic linker can't locate the required libraries for `kvssink`. This typically occurs due to:

- Moving `kvssink` to a different location from where it was built.
- Cross-compiling for the wrong CPU architecture.
- A required dependency is missing.

**Output:**

```
WARNING: erroneous pipeline: no element "kvssink"
error while loading shared libraries: libcproducer.so: cannot open shared object file: No such file or directory
```

**Resolution:**

For **moved libraries**, add the directory
containing the missing libraries to `LD_LIBRARY_PATH`.

From the root directory of the original repository, you can locate the missing
library using the `find` utility. In the terminal, type:

```
find . -name "*`libcproducer`*"
```

**Output:**

```
./`build`/`dependency`/libkvscproducer/kvscproducer-src/libcproducer.so
```

The file path separator on Linux devices is `:`. The command below
appends a new folder path to the existing `LD_LIBRARY_PATH` environment
variable, preserving any previous values.

In your terminal, type:

```
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/`path`/`to`/`build`/`dependency`/libkvscproducer/kvscproducer-src
```

###### Important

Environment variables are session-specific. To persist changes across sessions, modify your shell's startup script.

You may also need to add the `open-source/local/lib` to your
`$LD_LIBRARY_PATH`.

**Error: ./path/to/libcproducer.so.1: invalid ELF header**

If you receive this error while loading **shared
libraries**, it may be due to broken symbolic links
(`symlinks`). Symlinks can break if the host machine's operating
system doesn't match the target machine's. For example, cross-compiling on a MacBook
for a Raspberry Pi.

Another possible cause is that the built binaries were for the wrong architecture.
For example, if the binaries were built for x86 (Raspberry Pi uses ARM CPUs).

Navigate to the library location specified in the error and type: `ls
 -la` to inspect the library `symlinks`.

**Response:**

```
drwxr-xr-x  16 me  staff      512 Sep 10 17:16 .
drwxr-xr-x   7 me  staff      224 Jan  6 23:46 ..
drwxr-xr-x   4 me  staff      128 Sep 10 17:16 engines-1.1
-rwxr-xr-x   1 me  staff  2294496 Sep 10 17:16 libcrypto.1.1.so
-rw-r--r--   1 me  staff  4002848 Sep 10 17:16 libcrypto.a
lrwxr-xr-x   1 me  staff       19 Sep 10 17:16 libcrypto.so -> libcrypto.1.1.so
-rwxr-xr-x   1 me  staff   631176 Sep 10 17:12 liblog4cplus-2.0.3.so
lrwxr-xr-x   1 me  staff       24 Sep 10 17:12 liblog4cplus.so -> liblog4cplus-2.0.3.so
-rwxr-xr-x   1 me  staff     1012 Sep 10 17:12 liblog4cplus.a
-rwxr-xr-x   1 me  staff   694328 Sep 10 17:12 liblog4cplusU-2.0.3.so
lrwxr-xr-x   1 me  staff       25 Sep 10 17:12 liblog4cplusU.dylib -> liblog4cplusU-2.0.3.so
-rwxr-xr-x   1 me  staff     1017 Sep 10 17:12 liblog4cplusU.a
-rwxr-xr-x   1 me  staff   536416 Sep 10 17:16 libssl.1.1.so
-rw-r--r--   1 me  staff   795184 Sep 10 17:16 libssl.a
lrwxr-xr-x   1 me  staff       16 Sep 10 17:16 libssl.so -> libssl.1.1.so
drwxr-xr-x   6 me  staff      192 Sep 10 17:16 pkgconfig
```

In the sample output above, the `symlinks` are not broken. Broken
`symlinks` won't have arrows pointing to their targets.

**Resolution:**

There are two options to fix the symlinks:

- **Recommended:** Recreate the
  `symlink` with the `ln` command. Type:

```
ln -s /path/to/actual/library /path/to/symlink
```

- Copy the actual library file and rename it to match the `symlink`.

###### Note

This option leads to increased storage usage.

As a best practice, compile on the same operating system using tools like Docker to avoid cross-compilation issues.

**Missing dependencies:**

If the missing library name starts with `libkvs`, see the section for
"moved libraries" above to install the Kinesis Video Streams libraries from the host device to the
target device.

Otherwise, follow [Install software prerequisites](producersdk-cpp-rpi-software.md "producersdk-cpp-rpi-software.md") to make sure all the open-source software prerequisites are installed on the target device.
