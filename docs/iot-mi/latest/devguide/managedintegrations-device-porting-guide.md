# Port the End device SDK to your

device

Port the End device SDK to your device platform. Follow these steps to connect your devices with
AWS IoT Device Management.

## Download and verify the

End device SDK

1. Download the latest version of the End device SDK from the
   [managed integrations console](https://console.aws.amazon.com/iot/home#/managed-integrations/intro "https://console.aws.amazon.com/iot/home#/managed-integrations/intro").
2. Verify that your platform is in the list of supported platforms in [Reference: Supported
   platforms](managedintegrations-sdk-device-appendix.md#managedintegrations-sdk-device-appendixA "managedintegrations-sdk-device-appendix.md#managedintegrations-sdk-device-appendixA").

###### Note

The End device SDK has been tested on the specified platforms. Other platforms might
work, but haven't been tested. 3. Extract (unzip) the SDK files to your workspace. 4. Configure your build environment with the following settings:

    * Source file paths
    * Header file directories
    * Required libraries
    * Compiler and linker flags

5. Before you port the Platform Abstraction Layer (PAL), make sure your platform’s
   basic functionalities are initialized. Functionalities include:
   - Operating system tasks
   - Peripherals
   - Network interfaces
   - Platform-specific requirements

## Port the PAL to your device

1. Create a new directory for your platform-specific implementations in the existing
   platform directory. For example, if you use FreeRTOS, create a directory at
   `platform/freertos`.

###### Example SDK directory structure

```

├── <SDK_ROOT_FOLDER>
│   ├── CMakeLists.txt
│   ├── LICENSE.txt
│   ├── cmake
│   ├── commonDependencies
│   ├── components
│   ├── docs
│   ├── examples
│   ├── include
│   ├── lib
│   ├── platform
│   ├── test
│   └── tools
```

2. Copy the POSIX reference implementation files (.c and .h) from the posix folder to
   your new platform directory. These files provide a template for the functions you’ll
   need to implement.
   - Flash memory management for credential storage
   - PKCS#11 implementation
   - Network transport interface
   - Time synchronization
   - System reboot and reset functions
   - Logging mechanisms
   - Device-specific configurations

3. Set up Transport Layer Security (TLS) authentication with MBedTLS.
   - Use the provided POSIX implementation if you already have an MBedTLS version
     that matches the SDK version on your platform.
   - With a different TLS version, you implement the transport hooks for your TLS
     stack with TCP/IP stack.

4. Compare your platform's MbedTLS configuration with the SDK requirements in
   `platform/posix/mbedtls/mbedtls_config.h` . Make sure all of the
   required options are enabled.
5. The SDK relies on the coreMQTT to interact with cloud. Therefore, you must implement
   a network transport layer that uses the following structure:

```

typedef struct TransportInterface
{
    TransportRecv_t recv;
    TransportSend_t send;
    NetworkContext_t * pNetworkContext;
} TransportInterface_t;
```

For more information, see [Transport interface documentation](https://www.freertos.org/Documentation/03-Libraries/03-FreeRTOS-core/06-Transport-Interface/01-Transport-interface "https://www.freertos.org/Documentation/03-Libraries/03-FreeRTOS-core/06-Transport-Interface/01-Transport-interface") on the _FreeRTOS_
website. 6. (Optional) The SDK uses the PCKS#11 API to handle certificate operations. corePKCS
is a non hardware specific PKCS#11 implementation for prototyping. We recommend you use
secure cryptoprocessors such as Trusted Platform Module (TPM), Hardware Security Module
(HSM), or Secure Element in your production environment:

    * Review the sample PKCS#11 implementation that uses the Linux file system for
     credential management at
     `platform/posix/corePKCS11-mbedtls`.
    * Implement the PKCS#11 PAL layer at
     `commonDependencies/core_pkcs11/corePKCS11/source/include/core_pkcs11.h`.
    * Implement the Linux file system at
     `platform/posix/corePKCS11-mbedtls/source/iotmi_pal_Pkcs11Operations.c`.
    * Implement the store and load function of your storage type at
     `platform/include/iotmi_pal_Nvm.h`.
    * Implement the standard file access at
     `platform/posix/source/iotmi_pal_Nvm.c`.

For detailed porting instructions, see [Porting the corePKCS11
library](../../../freertos/latest/portingguide/afr-porting-pkcs.md "../../../freertos/latest/portingguide/afr-porting-pkcs.md") in the _FreeRTOS User Guide_. 7. Add the SDK static libraries to your build environment:

    * Set up the library paths to resolve any linker issues or symbol conflicts
    * Verify all dependencies are properly linked

## Test your

port

You can use the existing example application to test your port. The compilation must
complete without any errors or warnings.

###### Note

We recommend that you start with the simplest possible multitasking application. The
example application provides a multitasking equivalent.

1. Find the example application in
   `examples/[device_type_sample]`.
2. Convert the `main.c` file to your project, and add an entry to call the existing
   main() function.
3. Verify that you can compile the demo application successfully.
