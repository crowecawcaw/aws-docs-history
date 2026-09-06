

# Customer onboarding for SPEKE
<a name="customer-onboarding"></a>

Protect your content from unauthorized use by combining a Secure Packager and Encoder Key Exchange (SPEKE) digital rights management (DRM) key provider with your encryptor and with your media players. SPEKE defines the standard for communication between encryptors and packagers of media content and digital rights management (DRM) key providers. To onboard, you choose a DRM platform key provider and configure the communication between the key provider and your encryptors and players.

**Topics**
+ [Get started with a DRM platform provider](#choose-drm-provider)
+ [SPEKE support in AWS services and products](#check-supported-technologies)
+ [SPEKE support in AWS Partner services and products](#check-supported-partners-technologies)

## Get started with a DRM platform provider
<a name="choose-drm-provider"></a>

The following Amazon partners provide third-party DRM platform implementations for SPEKE. For details about their offerings and information about how to contact them, follow the links to their Amazon Partner Network pages. Partners that don’t have a link don’t currently have an Amazon Partner Network page, but you can contact them directly. The partners can help you get set up to use their platforms.


| DRM platform provider | SPEKE v1 support | SPEKE v2 support | 
| --- | --- | --- | 
|  **Axinom**  | √ | √ | 
|  **BuyDRM**  | √ | √ | 
|  **castLabs**  | √ | √ | 
|  **EZDRM**  | √ | √ | 
|  **Inisoft**  | √ | √ | 
|  **DOVERUNNER**  | √ | √ | 
|  **Insys Cloud DRM**  | √ | √ | 
|  **Intertrust Technologies**  | √ | √ | 
|  **Irdeto**  | √ | √ | 
|  **JW Player **  | √ | √ | 
|  **Kaltura**  | √ |  | 
|  **NAGRA**  | √ | √ | 
|  **NEXTSCAPE, Inc.**  | √ | √ | 
|  **SeaChange**  | √ |  | 
|  **Verimatrix**  | √ | √ | 
|  **Viaccess-Orca**  | √ |  | 
|  **WebStream**  | √ | √ | 

## SPEKE support in AWS services and products
<a name="check-supported-technologies"></a>

This section lists the SPEKE support that is provided by AWS Media Services that run in the AWS Cloud and by AWS on-premises media products. These services and products are the encryptors in the SPEKE content encryption architecture. Verify that your streaming protocol and the DRM system that you want are available for your service or product.


| AWS service or product | SPEKE v1 support | SPEKE v2 support | Supported DRM technologies | 
| --- | --- | --- | --- | 
|  **AWS Elemental MediaConvert - Service that runs in the AWS Cloud**  | √ | √ |  ** [Documentation](https://docs.aws.amazon.com/mediaconvert/latest/ug/encryption-choosing-speke-version.html) **  | 
|  **AWS Elemental MediaPackage - Service that runs in the AWS Cloud**  | √ | √ |  ** [Documentation](https://docs.aws.amazon.com/mediapackage/latest/ug/encryption-choosing-speke-version.html) **  | 
|  **AWS Elemental Live - On-premises product**  | √ |  |  **Documentation: [MPEG-DASH](https://docs.aws.amazon.com/elemental-live/latest/ug/drm-dash-output.html) / [HLS](https://docs.aws.amazon.com/elemental-live/latest/ug/drm-hls-applefairplay.html) **  | 
|  **AWS Elemental Server - On-premises product**  | √ |  |  ** [Documentation](https://docs.aws.amazon.com/elemental-server/latest/ug/drm-support-solutions.html) **  | 

## SPEKE support in AWS Partner services and products
<a name="check-supported-partners-technologies"></a>

This section lists the SPEKE support that is provided by AWS Partner services and products that run in the AWS Cloud. These services and products are the encryptors in the SPEKE content encryption architecture. Verify that your streaming protocol and the DRM system that you want are available for your service or product.


| AWS service or product | SPEKE v1 support | SPEKE v2 support | Supported DRM technologies | 
| --- | --- | --- | --- | 
|  **Bitmovin Live Video Encoding**  | √ |  |  ** [Documentation](https://developer.bitmovin.com/encoding/docs/using-speke-for-drm) **  | 
|  **Bitmovin Video on demand (VOD) Encoding**  | √ |  |  ** [Documentation](https://developer.bitmovin.com/encoding/docs/using-speke-for-drm) **  | 