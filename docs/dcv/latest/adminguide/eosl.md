# Amazon DCV end of support life

The Amazon DCV End of Support Life (EOSL) defines the point in time after which a specific major version (and
all of its minor versions) of Amazon DCV no longer receives support and is no longer tested for compatibility with
newer versions.

Before the EOSL date, the Amazon DCV support team continues to provide full support for configuration issues.
Defect resolutions and feature requests are implemented for the most recent versions of the Amazon DCV server and
Amazon DCV client only. They are not implemented for older versions.

After the EOSL date, no further support or maintenance is provided. We will also stop testing for compatibility
issues. For continued support, you must upgrade to the latest Amazon DCV version.

Backward compatibility is preserved, applying the same EOSL rules. This means that an Amazon DCV client
can connect to a Amazon DCV Server and a DCV Client/Viewer can connect to an Amazon DCV Server, if both the server
and client are supported

###### Topics

- [EOSL timeline](#dates "#dates")
- [EOSL paths for customers](#paths "#paths")
- [EOSL FAQs](#faq "#faq")

## EOSL timeline

The following table shows the EOSL timeline for the Amazon DCV major versions.

| Amazon DCV major version | Initial release date | EOSL date         |
| ------------------------ | -------------------- | ----------------- |
| **Amazon DCV 2016.x**    | December 31, 2015    | March 31, 2021    |
| **Amazon DCV 2017.x**    | December 18, 2017    | December 31, 2021 |
| **Amazon DCV 2019.x**    | August 5, 2019       | December 31, 2022 |
| **Amazon DCV 2020.x**    | April 16, 2020       | December 31, 2023 |
| **Amazon DCV 2021.x**    | April 12, 2021       | December 31, 2024 |
| **Amazon DCV 2022.x**    | February 23, 2022    | December 31, 2025 |
| **Amazon DCV 2023.x**    | May 3, 2023          | December 31, 2026 |
| **Amazon DCV 2024.x**    | Oct 2, 2024          | December 31, 2027 |
| **Amazon DCV 2025.x**    | Oct 7, 2025          | December 31, 2028 |

###### Note

Starting March 31st 2025, the following Amazon DCV versions will no longer be supported:

- Windows client version 2023.1.8993 or older
- Linux/MacOS client 2023.1.6203 or older

## EOSL paths for customers

If you are running Amazon DCV on AWS, you do not need a license for Amazon DCV. You pay only for the underlying AWS
resources that you use for your workloads. If you are currently using a Amazon DCV version that is past its EOSL date,
upgrade to the latest Amazon DCV version using the [Amazon DCV download
page](http://download.amazondcv.com "http://download.amazondcv.com") to continue receiving support.

If you are running Amazon DCV on-premises or using a third-party cloud service providers, and the version of Amazon DCV
that you are currently using is past its EOSL date, contact your reseller or distributor to evaluate your available
upgrade paths. If you have an active support contract, you can upgrade to the latest version of Amazon DCV at no cost.
For information about the Amazon DCV distributors and resellers, see the [NICE website.](https://www.nice-software.com/ "https://www.nice-software.com/").

## EOSL FAQs

###### 1. I’m using a version of Amazon DCV that has reached its EOSL on-premises or with a third-party cloud service provider,

but I have an existing support contract. Will I be impacted by the EOSL?

If you have an active support contract, the terms of the Amazon DCV support contract enable you to upgrade your Amazon DCV
licenses to the latest version at no additional charge. In this situation, there is minimal impact. If your support
contract is expired, you can use one of the following methods to continue receiving full support:

1. Upgrade to the latest version of Amazon DCV version with a new paid license.
2. Renew your support contract before the EOSL timeline to, which gives you an upgrade path to the latest
   versions of Amazon DCV.
3. Reinstate an old support contract by paying a reinstatement fee, which is equal to 70% of the current
   charge for support services for the period of time since your support contract expired.

###### 2. I’m using a version of Amazon DCV that has reached its EOSL on Amazon EC2, what should I do to upgrade to a supported

version?

Upgrading to fully supported versions of Amazon DCV for use on Amazon EC2 is available to customers at all times for
no additional charge.

###### 3. Can I use a version of the Amazon DCV client that has reached its EOSL with a supported Amazon DCV server, or vice versa?

Yes, but we strongly recommend that you upgrade both your client and server software to the latest versions as
bug fixes are no longer applied to versions that have reached their EOSL.
