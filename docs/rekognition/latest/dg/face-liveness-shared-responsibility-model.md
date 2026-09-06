

# Face Liveness Shared Responsibility Model
<a name="face-liveness-shared-responsibility-model"></a>

 

Security and Compliance is a shared responsibility between AWS and you, the customer. Read more about AWS shared responsibility model [here](https://aws.amazon.com/compliance/shared-responsibility-model/).

1.  All calls to the AWS service (via client application or customer backend) are authenticated and authorized with AWS Auth (AWS Authentication). It’s the responsibility of Face Liveness service owners to ensure this happens. 

1.  All calls to the customer backend (from the client application) are authenticated and authorized via the customer. This responsibility falls on the customer. The customer must ensure that calls from the client application are authenticated and haven’t been manipulated in any way. 

1.  The customer backend must identify the end user performing the Face Liveness challenge. It’s the customer’s responsibility to tie an end user to a Face Liveness session. The Face Liveness service does not distinguish between end users. It is only able to identify the calling AWS identity (which the customer handles). 

1. AWS recommends customers apply additional validation checks, such as location geolocation (e.g. based on IP), One Time Pass codes (OTPs) etc. in addition to Face Liveness that aligns with their use case requirements and security posture.

The 'FaceMovementAndLightChallenge' setting delivers the highest accuracy for Rekognition Liveness by requiring users to move their face toward the screen and hold still for a series of flashing lights. We recommend that customers use this default setting. Alternatively, customers can enable the 'FaceMovementChallenge' setting, which reduces the check time by several seconds by eliminating the flashing lights. While 'FaceMovementAndLightChallenge' remains the best setting to maximize accuracy , 'FaceMovementChallenge' allows customers to prioritize faster liveness checks. When selecting between these settings, customers should consider their use case requirements including expected attack types, desired false accept and false reject rates, and also implement additional checks such as geolocation (e.g. based on IP), One Time Pass codes (OTPs), etc. Customers should make this decision after testing Liveness performance with various confidence score thresholds depending on their use case. Customers are responsible to implement controls to secure the device of which the video is sent from

The following flow diagram shows which calls are authenticated by the AWS service or by the customer:

![Liveness detection flow showing interactions between client app, face liveness detector component, customer's backend, Rekognition service, and Rekognition streaming service for secure face liveness session.](http://docs.aws.amazon.com/rekognition/latest/dg/images/SequenceDiagramLivenessFlow-v5.png)


All calls to the Amazon Rekognition Face Liveness service are protected by AWS Auth (using AWS signing mechanism). This includes the following calls:
+  [3] [CreateFaceLivenessSession](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateFaceLivenessSession.html) API call (from customer’s backend) 
+  [7] [StartFaceLivenessSession](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_rekognitionstreaming_StartFaceLivenessSession.html) API call (from client application) 
+  [11] [GetFaceLivenessSessionResults](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetFaceLivenessSessionResults.html) API call (from customer’s backend) 

All calls to customer’s backend need to have an authentication and authorization mechanism. Customers need to ensure that the third-party code/library/etc used is being actively maintained and developed. Customers also need to ensure that the correct end user is making calls to the correct Face Liveness session. Customers must authenticate and authorize the following flows:
+  [2] Create Face Liveness session (from client application) 
+  [10] Get Face Liveness session result (from client application) 

Customers can follow the [STRIDE](https://owasp.org/www-community/Threat_Modeling_Process#stride-threat-list) security model to make sure that their API calls are protected.


| 
| 
| Type | Description | Security Control | 
| --- |--- |--- |
| Spoofing | Threat action aimed at accessing and use of another user’s credentials, such as username and password. | Authentication | 
| Tampering | Threat action intending to maliciously change or modify persistent data. Examples include records in a database, and the alteration of data in transit between two computers over an open network, such as the internet. | Integrity | 
| Repudiation | Threat action aimed at performing prohibited operations in a system that lacks the ability to trace the operations. | Non-Repudiation | 
| Information disclosure | Threat action intending to read a file that one was not granted access to, or to read data in transit. | Confidentiality | 
| Denial of service | Threat action attempting to deny access to valid users, such as by making a web server temporarily unavailable or unusable. | Availability | 
| Elevation of privilege | Threat action intending to gain privileged access to resources in order to gain unauthorized access to information or to compromise a system. | Authorization | 

AWS secures its connections in the following ways:

1.  Calculating the request signature and then verifying the signature at the service side. Requests are * **authenticated** * using this signature. 

1.  AWS customers are required to setup proper IAM roles to * **authorize** * certain actions/operations. These IAM roles are needed to make calls to the AWS service. 

1.  Only HTTPS requests to AWS service are allowed. Requests are encrypted in the open network using TLS. This protects the * **confidentiality** * of the requests and maintains request * **integrity** *. 

1. AWS service logs sufficient data to identify calls made by customers. This prevents * **repudiation** * attacks.

1.  AWS service owns maintaining sufficient * **availability** * 

Customer is responsible for securing their service and API calls in the following ways:

1.  Customer must ensure that they follow a proper mechanism for authentication. There are various authentication mechanisms that can be used to authenticate a request. Customers can explore [ digest based authentication ](https://en.wikipedia.org/wiki/Digest_access_authentication), [ OAuth ](https://oauth.net/), [ OpenID connect ](https://openid.net/connect/), and other mechanisms. 

1.  Customers must make sure that their service supports proper encryption channels (like TLS/HTTPS) for making service API calls. 

1.  Customers must make sure that they log the data necessary to uniquely identify an API call and the caller. They should be able to identify the client calling their API with defined parameters and the time of the calls. 

1.  Customers must make sure that their system's available, and that they’re protected against [DDoS attacks](https://en.wikipedia.org/wiki/Denial-of-service_attack). Here are some examples of [defense techniques](https://en.wikipedia.org/wiki/Denial-of-service_attack#Defense_techniques) against DDoS attacks.

Customers are responsible for keeping their applications up-to-date. For more information, see [Face Liveness update guidelines](face-liveness-update-guidelines.md).