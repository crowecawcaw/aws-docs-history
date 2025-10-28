# Nitro Enclaves application development

on Linux instances

This section provides information for Nitro Enclaves application development on Linux
instances.

## Getting started with the vsock: Vsock tutorial

###### Important

The vsock sample application is supported on Linux instances only.

The vsock sample application is a simple client-server application that
exchanges information between the parent instance and the enclave using the
vsock socket.

The vsock sample application includes a client application and a server
application. The client application runs on the parent instance, while the
server application runs in the enclave. The client application sends a simple
text message over the vsock to the server application. The server application
listens to the vsock and prints the message to the console.

The vsock sample application is available in both Rust and Python. This
tutorial shows you how to set up and run the Rust vsock sample application. For
more information about setting up and running the Python vsock sample
application, see the [AWS Nitro Enclaves samples GitHub repository](https://github.com/aws/aws-nitro-enclaves-samples/tree/main/vsock_sample/py "https://github.com/aws/aws-nitro-enclaves-samples/tree/main/vsock_sample/py").

###### Note

The application source is also freely available from the [AWS Nitro Enclaves samples GitHub repository](https://github.com/aws/aws-nitro-enclaves-samples/tree/main/vsock_sample "https://github.com/aws/aws-nitro-enclaves-samples/tree/main/vsock_sample"). You can use the
application source as a reference for building your own applications.

###### Prerequisites

Ensure the following prerequisites are met to configure and test the
sample application.

- To test the sample application using the Nitro CLI, configure an
  enclave-enabled parent instance as detailed in [Step 1: Prepare the enclave-enabled parent instance](getting-started.md#launch-instance "getting-started.md#launch-instance"). This is
  the only step required from the getting started guide required to create
  the sample application.
- To clone the sample repository from GitHub, install a Git client on
  the parent instance. For more information, see [Install Git](https://github.com/git-guides/install-git "https://github.com/git-guides/install-git")
  in the GitHub documentation.
- To compile the Rust vsock sample application, you must have Cargo,
  Rust’s build system and package manager installed. You must also add the
  `x86_64-unknown-linux-musl target` or
  `aarch64-unknown-linux-musl target`. To install and
  configure Rust, use the following commands.

```
`$` curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf | sh
```

###### Important

You must disconnect from the instance and then reconnect before
running the following commands.

After you reconnect to the instance, determine the architecture of the
operating system to configure and test the sample application. The
architecture will be either `x86_64` or `aarch64`.
Run the following command to display the architecture of the operating
system.

```
echo $(uname -m)
```

Run the following commands to finish installing and configuring
Rust.

```
`$` rustup target add `x86_64`-unknown-linux-musl
```

```
`$` sudo yum -y install gcc
```

###### To try the vsock sample application

1. Download the application source and navigate into the
   directory.

```
`$` git clone https://github.com/aws/aws-nitro-enclaves-samples.git
```

```
`$` cd aws-nitro-enclaves-samples/vsock_sample/rs
```

2. Compile the application code using Cargo.

```
`$` cargo build --target=`x86_64`-unknown-linux-musl --release
```

The compiled binary is located in
`vsock_sample/rs/target/`x86_64`-unknown-linux-musl/release/vsock-sample`. 3. Navigate two levels up.

```
`$` cd ../..
```

4. Create a new file named `Dockerfile` and then add the
   following.

```
# start the Docker image from the Alpine Linux distribution
FROM alpine:latest
# copy the vsock-sample binary to the Docker file
COPY vsock_sample/rs/target/`x86_64`-unknown-linux-musl/release/vsock-sample .
# start the server application inside the enclave
CMD ./vsock-sample server --port 5005

```

5. Convert the Docker file to an enclave image file.

```
`$` nitro-cli build-enclave --docker-dir ./ --docker-uri vsock-sample-server --output-file vsock_sample.eif
```

6. Boot the enclave using the enclave image file. You need to access the
   enclave console to see the server application output, so you must
   include the `--debug-mode` option.

```
`$` nitro-cli run-enclave --eif-path vsock_sample.eif --cpu-count 2 --enclave-cid 6 --memory 256 --debug-mode
```

Make a note of the enclave ID, because you'll need this to connect to
the enclave console. 7. Open the enclave console. The console provides a view of what's
happening on the server side of the application.

```
`$` nitro-cli console --enclave-id `enclave_id`
```

8. Open an SSH terminal window for the parent instance. You'll use this
   terminal to run the client application.
9. In the parent instance terminal, run the client application. When you
   start the client application, it automatically sends some text over the
   vsock to the server application running in the enclave. Watch the
   enclave console terminal for the output.

```
`$` ./aws-nitro-enclaves-samples/vsock_sample/rs/target/`x86_64`-unknown-linux-musl/release/vsock-sample client --cid 6 --port 5005
```

10. When the server application receives the text over the vsock, it
    prints the text to the console.

```
`$` [    0.127079] Freeing unused kernel memory: 476K
[    0.127631] nsm: loading out-of-tree module taints kernel.
[    0.128055] nsm: module verification failed: signature and/or required key missing - tainting kernel
[    0.154010] random: vsock-sample: uninitialized urandom read (16 bytes read)
Hello, world!

```

Now that you understand how the sample application works, download and
customize the source code to suit your use case.
