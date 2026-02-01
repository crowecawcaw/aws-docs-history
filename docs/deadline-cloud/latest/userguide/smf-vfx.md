# VFX Reference Platform compatibility

The VFX Reference Platform is a common target platform for the VFX industry. To use the standard
service-managed fleet Amazon EC2 instance running Amazon Linux 2023 with software that supports
the VFX Reference Platform, you should keep in mind the following considerations when using a
service-managed fleet.

The VFX Reference Platform is updated annually. These considerations for using an AL2023 including
Deadline Cloud service-managed fleets are based on the calendar year (CY) 2022 through 2024
Reference Platforms. For more information, see [VFX Reference Platform](https://vfxplatform.com/ "https://vfxplatform.com/").

###### Note

If you are creating a custom Amazon Machine Image (AMI) for a customer-managed fleet, you
can add these requirements when you prepare the Amazon EC2 instance.

To use VFX Reference Platform supported software on an AL2023 Amazon EC2 instance, consider the
following:

- The glibc version installed with AL2023 is compatible for runtime use, but
  not for building software compatible with the VFX Reference Platform CY2024 or earlier.
- Python 3.9 and 3.11 are provided with the service-managed fleet making it
  compatible with VFX Reference Platform CY2022 and CY2024. Python 3.7 and 3.10 are not provided
  in the service-managed fleet. Software requiring them must provide the Python
  installation in the queue or job environment.
- Some Boost library components provided in the service-managed fleet are
  version 1.75, which is not compatible with the VFX Reference Platform. If your application uses
  Boost, you must provide your own version of the library for
  compatibility.
- Intel TBB update 3 is provided in the service-managed fleet. This version is
  compatible with VFX Reference Platform CY2022, CY2023, and CY2024.
- Other libraries with versions specified by the VFX Reference Platform are not provided by the
  service-managed fleet. You must provide the library with any application used on
  a service-managed fleet. For a list of libraries, see the [reference platform](https://vfxplatform.com/ "https://vfxplatform.com/").
