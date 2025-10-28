End of support notice: On May 31, 2026, AWS will end support for
AWS Panorama. After May 31, 2026, you will no longer be able to access the AWS Panorama console or AWS Panorama
resources. For more information, see [AWS Panorama end of support](panorama-end-of-support.md "panorama-end-of-support.md").

# AWS Panorama end of support

After careful consideration, we decided to end support for the AWS Panorama, effective May 31, 2026. AWS Panorama will
no longer accept new customers beginning May 20, 2025. As an existing customer with an account signed up for the service before May 20, 2025, you can continue
to use AWS Panorama features. After May 31, 2026, you will no longer be able to use AWS Panorama.

## Alternatives to AWS Panorama

If you're interested in an alternative to AWS Panorama, AWS has options for both buyers and builders.

For an out-of-the-box solution, the [AWS Partner Network](https://partners.amazonaws.com/ "https://partners.amazonaws.com/") offers solutions from multiple partners. You can browse solutions on the [AWS Solutions Library](https://aws.amazon.com/solutions/ "https://aws.amazon.com/solutions/") from many of our partners. These partner solutions include options for hardware, software, software as a service (SaaS) applications, managed solutions, or custom implementations based on your needs. This approach provides a solution that addresses your use case without requiring you to have expertise in computer vision, AI, or application development. This typically provides faster time to value by taking advantage of the specialized expertise of the AWS Partners.

If you prefer to build your own solution, AWS offers AI tools and services to help you develop an AI-based computer vision application and manage the applications and devices at the edge. [Amazon SageMaker](https://aws.amazon.com/pm/sagemaker "https://aws.amazon.com/pm/sagemaker") provides a set of tools to build, train, and deploy ML models for your use case with fully managed infrastructure, tools, and workflows. In addition to enabling you to build your own models, [Amazon SageMaker JumpStart](https://aws.amazon.com/sagemaker/jumpstart/ "https://aws.amazon.com/sagemaker/jumpstart/") offers built-in [computer vision algorithms](../../../sagemaker/latest/dg/algorithms-vision.md "../../../sagemaker/latest/dg/algorithms-vision.md") that can be fine-tuned to your specific use case.

For managing devices and applications at the edge, [AWS IoT Greengrass](https://aws.amazon.com/greengrass/ "https://aws.amazon.com/greengrass/") is a proven and secure solution to deploy and update applications for IoT devices. For a server-based implementation, [AWS Systems Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/") provides a suite of tools for managing servers and Amazon [EKS Anywhere](https://aws.amazon.com/eks/eks-anywhere/ "https://aws.amazon.com/eks/eks-anywhere/") or [ECS Anywhere](https://aws.amazon.com/ecs/anywhere/ "https://aws.amazon.com/ecs/anywhere/") can manage application containers on edge servers. Amazon provides some guidelines for managing edge devices, along with additional resources in [Section 4](../../../whitepapers/latest/securing-iot-with-aws/define-appropriate-update-mechanisms-for-updates.md "../../../whitepapers/latest/securing-iot-with-aws/define-appropriate-update-mechanisms-for-updates.md") of the [Securing Internet of Things (IoT) with AWS](../../../whitepapers/latest/securing-iot-with-aws/securing-iot-with-aws.md "../../../whitepapers/latest/securing-iot-with-aws/securing-iot-with-aws.md") whitepaper. This builder approach provides you the tools to accelerate your AI and device management development while providing complete flexibility to build a solution that meets your exact requirements and integrates with your existing hardware and software infrastructure. This typically provides lower operating costs for a solution.

## Migrating from AWS Panorama

To move an existing application from AWS Panorama to an alternative implementation, you will need to replace the existing hardware device, migrate the application from the AWS Panorama service, and implement edge management and security for the new solution. Each of those areas will be explored in detail below:

### Hardware Replacement

The existing AWS Panorama appliance is based on the Nvidia Jetson Xavier platform. The hardware can be replaced with a similar [off-the-shelf device](https://developer.nvidia.com/embedded/jetson-partner-products?t1_other-interfaces=rugged "https://developer.nvidia.com/embedded/jetson-partner-products?t1_other-interfaces=rugged") based on the current generation Nvidia Jetson platform that meets your requirements, or an edge server. While most AWS Panorama deployments can be replaced with a similar device, we have seen some customers who utilize a large number of cameras in a single location find that a server is a better alternative.

### Application Migration

AWS Panorama applications need to be rewritten to eliminate the use of any AWS Panorama-specific API calls. AWS Panorama applications only support video input through Real-Time Streaming Protocol (RTSP) feeds using H.264 and those video inputs are provided using camera nodes in the AWS Panorama device SDK.

To port an existing application, you will need to implement an application class similar to AWS Panorama so that the existing code can be mostly re-used. Sample code is available in the [banner-code.zip](samples/banner-code.md "samples/banner-code.md") file that shows an example of this implementation using both PyAV and OpenCV.

This is a simple approach with a minimal amount of code changes, but has many of the same limitations as the current AWS Panorama based implementation in terms of the types of video streams supported.

Another option would be to re-architect the application to make better use of system resources and to support new application capabilities. For this option, you use [GStreamer](https://gstreamer.freedesktop.org/ "https://gstreamer.freedesktop.org/") or [DeepStream](https://developer.nvidia.com/deepstream-sdk "https://developer.nvidia.com/deepstream-sdk") to implement the media pipeline from media source to inference results and business logic, or use a more feature rich and better performing machine learning (ML) runtime implementation, like the [Nvidia Triton](https://developer.nvidia.com/triton-inference-server "https://developer.nvidia.com/triton-inference-server") inference server. This approach requires changes to more of the video processing pipeline, but is both more efficient and allows more flexibility to support a wider range of codecs, camera types, and other sensors.

### Edge Management and Security

Regardless of the media pipeline, you will also have to implement a secure store for credentials, e.g. RTSP stream username and password. AWS provides different ways of securely storing parameters for applications:

- [AWS IoT Device Shadow service](../../../iot/latest/developerguide/iot-device-shadows.md "../../../iot/latest/developerguide/iot-device-shadows.md") is used to store parameters that are passed to applications, as well as to track the status of the applications on the edge device.
- [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/ "https://aws.amazon.com/secrets-manager/") is used to store such credentials to better protect the credentials to access media streams.
- If you use [Amazon EKS](https://aws.amazon.com/eks/ "https://aws.amazon.com/eks/") or [Amazon ECS](https://aws.amazon.com/ecs/ "https://aws.amazon.com/ecs/"), then you can also use the secure [AWS System Manager Parameter store](../../../systems-manager/latest/userguide/systems-manager-parameter-store.md "../../../systems-manager/latest/userguide/systems-manager-parameter-store.md") for credentials and other application parameters.

The choice depends on the security requirements of the application, as well as which other AWS products you plan to use to implement your application.

When you replace the AWS Panorama appliance with a generic edge device, you must also implement required security features for your applications and configure the devices to comply with your security requirements. AWS provides guidance on this in the [Security Pillar](../../../wellarchitected/latest/security-pillar/welcome.md "../../../wellarchitected/latest/security-pillar/welcome.md") of the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/ "https://aws.amazon.com/architecture/well-architected/"). While the framework primarily focuses on cloud applications, most principles also apply to edge devices. In addition, you should use hardware security features of the chosen solution, such as [AWS IoT Greengrass V2 hardware security integration](../../../greengrass/v2/developerguide/hardware-security.md "../../../greengrass/v2/developerguide/hardware-security.md"), and use security features provided by the chosen OS and/or device, such as full disk encryption.

## Summary

Although AWS Panorama is planning to shut down on May 31, 2026, AWS offers a powerful set of AI/ML services and solutions in the form of Amazon SageMaker tools to build computer vision models and device management services, such as AWS IoT Greengrass, Amazon EKS and [Amazon ECS Anywhere](https://aws.amazon.com/ecs/anywhere/ "https://aws.amazon.com/ecs/anywhere/") and [AWS System Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/") to support the development of similar solutions. AWS also has a range of offerings from partners in the AWS Partner Network if you prefer to buy instead of build a solution. Example code and implementation guidance is provided to help to migrate to an alternate solution if you so choose. You should explore these options to determine what works best for your specific needs.

For more details, refer to the following resources:

- [Amazon SageMaker Developer Guide](../../../sagemaker/latest/dg/whatis.md "../../../sagemaker/latest/dg/whatis.md") – Detailed documentation on how to [build a model](../../../sagemaker/latest/dg/machine-learning-environments.md "../../../sagemaker/latest/dg/machine-learning-environments.md") or work with [built-in computer vision algorithms](../../../sagemaker/latest/dg/algorithms-vision.md "../../../sagemaker/latest/dg/algorithms-vision.md") available in [SageMaker JumpStart](https://aws.amazon.com/sagemaker/jumpstart/ "https://aws.amazon.com/sagemaker/jumpstart/").
- [AWS IoT Core Developer Guide](../../../iot/latest/developerguide/what-is-aws-iot.md "../../../iot/latest/developerguide/what-is-aws-iot.md") - Detailed documentation on how to connect and manage IoT Devices.
- [AWS IoT Greengrass V2 Developer Guide](../../../greengrass/v2/developerguide/what-is-iot-greengrass.md "../../../greengrass/v2/developerguide/what-is-iot-greengrass.md") – Detailed documentation on how to build, deploy and manage IoT applications on your devices.
- [ECS Anywhere Developer Guide](../../../AmazonECS/latest/developerguide/ecs-anywhere.md "../../../AmazonECS/latest/developerguide/ecs-anywhere.md") - Detailed documentation on running ECS at the edge.
- [EKS Anywhere Best Practices Guide](../../../eks/latest/best-practices/hybrid.md "../../../eks/latest/best-practices/hybrid.md") - Detailed documentation on running EKS at the edge.
- [AWS Solutions Library](https://aws.amazon.com/solutions/ "https://aws.amazon.com/solutions/") – Partner offerings from a range of providers offering pre-built or customized computer vision solutions.
- [Panorama FAQs](https://aws.amazon.com/panorama/faqs/ "https://aws.amazon.com/panorama/faqs/") - Additional Panorama Information.

## Frequently Asked Questions

### What is the timing for the Panorama discontinuation?

The announcement was made on May 20, 2025. After this date, customers who are not active on the service will no longer have access to Panorama. Active customers will be able to continue to use the service normally until May 31, 2026. Customers have until that time to move their application to an alternative solution and migrate applications of Panorama. After May 31, 2026, any application that tries to access the Panorama service will no longer work and Panorama devices will no longer function.

### How will existing customers be impacted?

Existing customers can continue to use the service normally until May 31, 2026. After that, applications that try to access Panorama will no longer work. Panorama devices will also no longer work after that date.

### Are new customers being accepted?

No. As of May 20, 2025, only customers who are active users of Panorama will have access to the service. If a customer has applications in the service from prior usage that they need to access, they can create a case with customer support to request access for their account. If a customer does not have prior usage of the service, they will not be granted access.

### What are alternatives customers can explore?

AWS offers a range of services which can replace the Panorama capabilities. We recommend customers utilize off-the-shelf hardware and manage the device and application via the combination of AWS IoT Core, AWS IoT Greengrass, Amazon AKS Anywhere, Amazon ECS Anywhere, and / or AWS System Manager that meets their requirements. The AWS Partner Network also has several solutions available from partners with specific Computer Visions expertise that customers can consider.

### How can customers migrate off Panorama?

Panorama applications need to be modified to remove any dependencies on Panorama-specific APIs, which primarily relate to camera connection and streaming. AWS has provided sample code to show how to make these changes. Once those dependencies are removed, the application can be moved to an alternative hardware platform.

### If I am having issues on or after May 20, 2025, what support will be available?

AWS will continue to provide support for Panorama up until the end of the discontinuation notification period (May 31, 2026). For any support requirements, customers should enter a support case through their normal support channels. AWS will provide security updates, bug fixes, and availability enhancements.

### I cannot migrate before May 31, 2026. Can the date be extended?

We are confident that the alternatives that are available for Panorama enable customers to migrate to an alternative solution by May 31, 2026 and we have no plans to extend availability of the service past that date.

### Will my edge application continue to function after the service has ended?

No. The Panorama device and applications are dependent on connectivity to the Panorama cloud service. Once that service is discontinued on May 31, 2026, neither the Panorama application nor the Panorama device will continue to function.
