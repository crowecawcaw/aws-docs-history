

# Getting Started with the IVS Linux Broadcast SDK \| Real-Time Streaming

This document takes you through getting started with the Amazon IVS real-time streaming Linux broadcast SDK. Use it to add headless, audio-only participation in a stage to your Linux application.

## C and Go
<a name="broadcast-linux-c-and-go"></a>

The SDK has one native library and two ways to call it:
+ **C**: Include `aws_ivs_realtime.h` and link against `libaws-ivs-realtime.so`. Every public symbol starts with `aws_ivs_realtime_` or `AWS_IVS_REALTIME_`.
+ **Go**: Import the `realtime` package. It calls the C API through cgo, so it needs cgo and the same shared library.

Both languages expose the same objects. A C handle such as `aws_ivs_realtime_stage` is a Go type such as `Stage`, and a C function such as `aws_ivs_realtime_stage_join` is a Go method such as `Stage.Join`. The two languages differ in these ways:
+ **Errors**: A C function returns `false` on failure and writes the error to its last parameter, `out_error`. A Go function returns an error.
+ **Lifetimes**: In C, you release each handle you create with its `_destroy` function. In Go, you call `Close`.
+ **Callbacks**: In C, you supply function pointers in a callback table, with a `user_data` pointer that the SDK passes back to each callback. In Go, you implement an interface or set function fields.

## Install the Library
<a name="broadcast-linux-install"></a>

Both C and Go use the same native SDK archive. Download the archive for your architecture:
+ x86\_64: [Linux x86\_64 broadcast SDK archive](https://broadcast.live-video.net/1.49.0/aws-ivs-realtime-1.49.0-linux-amd64.tar.gz)
+ arm64: [Linux arm64 broadcast SDK archive](https://broadcast.live-video.net/1.49.0/aws-ivs-realtime-1.49.0-linux-arm64.tar.gz)

Each archive contains the library in `lib`, the headers in `include`, and a pkg-config file in `lib/pkgconfig`. The same folder holds `SHA256SUMS`, to check the download. The following shell commands download, verify, and extract the SDK archive into its own directory. Replace `VERSION` with the SDK version and `ARCH` with your architecture, `amd64` or `arm64`:

```shell
VERSION=1.49.0
ARCH=amd64   # or arm64
curl -fsSLO "https://broadcast.live-video.net/$VERSION/aws-ivs-realtime-$VERSION-linux-$ARCH.tar.gz"
curl -fsSL "https://broadcast.live-video.net/$VERSION/SHA256SUMS" | sha256sum --check --ignore-missing
mkdir -p "ivs-sdk/$VERSION"
tar -xzf "aws-ivs-realtime-$VERSION-linux-$ARCH.tar.gz" -C "ivs-sdk/$VERSION"
```

**C**: Add the include directory to the include path and link against the library. The following shell command compiles and links the C example, setting an rpath so the program finds the library at run time:

```shell
gcc -I "ivs-sdk/$VERSION/include" -o my-app my-app.c \
    -L "ivs-sdk/$VERSION/lib" -laws-ivs-realtime \
    -Wl,-rpath,"$PWD/ivs-sdk/$VERSION/lib"
```

**Go**: Add the module at the same version as the SDK, and point `PKG_CONFIG_PATH` at the SDK's `lib/pkgconfig`:

```shell
go get "github.com/aws/amazon-ivs-client-go/realtime@v$VERSION"
export PKG_CONFIG_PATH="$PWD/ivs-sdk/$VERSION/lib/pkgconfig"
go build
```

Import the package in your code:

```go
import "github.com/aws/amazon-ivs-client-go/realtime"
```

Every Go command that compiles the package needs `PKG_CONFIG_PATH`, including `go test`, `go vet`, and `gopls`. If `pkg-config` cannot find `aws-ivs-realtime-<version>`, check `PKG_CONFIG_PATH` and that the module and SDK versions match.

To run the program on another machine, or for a Docker example, see the [Go module README](https://github.com/aws/amazon-ivs-client-go/blob/main/realtime/README.md).

## Runtime Requirements
<a name="broadcast-linux-runtime-requirements"></a>

The SDK has the following runtime requirements:
+ Linux on x86\_64 or arm64, with glibc 2.34 or later.
+ libcurl 7.68 or later (`libcurl.so.4`). Install it with your distribution's package manager if it is not present.
+ A CA certificate bundle, such as the one in your distribution's `ca-certificates` package. To trust an additional CA, add it to the system trust store with `update-ca-trust` on Amazon Linux or `update-ca-certificates` on Debian and Ubuntu.
+ For Go: Go 1.24 or later, with cgo on, a C compiler, and `pkg-config` on the build machine. The package does not build with `CGO_ENABLED=0`.