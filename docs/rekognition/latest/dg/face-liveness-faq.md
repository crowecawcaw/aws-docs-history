# Face Liveness FAQ

Use the following FAQ items to find answers to commonly asked questions about Rekognition
Face Liveness.

- **What are the outputs of a face liveness
  check?**

Rekognition Face Liveness provides the following outputs for every liveness
check:

    + Confidence Score: A numerical score ranging from 0 to 100 is returned.
     This score indicates the likelihood that the selfie video is from a real
     person and not a bad actor using spoof.
    + High-Quality Image: A single high-quality image is extracted from the
     selfie video. This frame can be utilized for various purposes such as
     face comparison, age estimation, or face search.
    + Audit images: Up to four images are returned from the selfie video,
     which can be used for audit trail purposes.

- **Is Rekognition Face Liveness compliant with iBeta Presentation
  Attack Detection (PAD) tests?**

iBeta Quality Assurance’s Presentation Attack Detection (PAD) testing is
conducted in accordance with ISO/IEC 30107-3. iBeta is accredited by NIST/NVLAP
to test and provide results to this PAD standard. Rekognition Face Liveness passed
Level 1 and Level 2 iBeta Presentation Attack Detection (PAD) conformance
testing with a perfect PAD score. Report can be found on iBeta webpage [here](https://www.ibeta.com/wp-content/uploads/2023/10/231019-Amazon-Rekognition-PAD-Level-2-Confirmation-Letter.pdf "https://www.ibeta.com/wp-content/uploads/2023/10/231019-Amazon-Rekognition-PAD-Level-2-Confirmation-Letter.pdf").

- **How can I get high-quality frame and additional frames?**

The high-quality frame and additional frames can be returned as raw bytes or
uploaded to an Amazon S3 bucket you specify, depending on the configurations of your
[CreateFaceLivenessSession](../APIReference/API_CreateFaceLivenessSession.md "../APIReference/API_CreateFaceLivenessSession.md") API request.

- **Can I change the location of the oval and colored
  lights?**

No. The oval location and colored lights are features that enable higher accuracy and therefore
cannot be customized.

- **Can I customize the user interface as per our
  application?**

Yes, you can customize most screen components such as theme, color, language,
text content, and font to align with your application. Details on how to
customize these components can be found in the documentation for our [React](https://ui.docs.amplify.aws/react/connected-components/liveness "https://ui.docs.amplify.aws/react/connected-components/liveness"), [Swift](https://ui.docs.amplify.aws/swift/connected-components/liveness "https://ui.docs.amplify.aws/swift/connected-components/liveness"), and [Android](https://ui.docs.amplify.aws/android/connected-components/liveness "https://ui.docs.amplify.aws/android/connected-components/liveness") UI components.

- **Can I customize the countdown time and time to fit a
  face in oval?**

No, the countdown time and face fit time have been pre-determined based on
large-scale internal studies across 1000s of users, with the goal of providing
an optimal balance between that enable higher accuracy and latency. For this reason, these time
settings cannot be customized.

- **Do the different color lights meet accessibility
  guidelines?**

Yes, the different color lights in our product adhere to the accessibility
guidelines outlined in WCAG 2.1. As verified with over 1000s of user checks, the
user experience displays approximately two colors per second, which complies
with the recommendation of limiting colors to three per second. This reduces the
likelihood of triggering epileptic seizures in the majority of the
population.

- **Does the SDK adjust the screen brightness for optimal
  results?**

The Face Liveness mobile SDKs (for Android and iOS) automatically adjust the
brightness when the check is initiated. However, for the web SDK there are
limitations on webpages that prevent automatic brightness adjustment. In such
cases, we expect the web application to instruct end-users to manually increase
the screen brightness for optimal results.

- **Does it need to be an oval? Could we use other similar
  shapes?**

No, the size, shape, and location of the oval aren’t customizable. The
specific oval design has been carefully chosen for its effectiveness in
accurately capturing and analyzing facial movements. Therefore, the oval shape
can’t be modified.

- **What is the end-to-end latency?**

We measure end-to-end latency from the time the user starts the action
required to complete the liveness check to the time the user gets the result
(pass or fail). In the best case, the latency is 5s. In average case, we expect
it to be about 7s. In the worst case, the latency is 11s. We see variation in
end-to-end latency as it’s dependent on: the time the user to complete the
required action (i.e., move their face into the oval), the network connectivity,
the application latency, etc.

- **Can I use Face Liveness feature without Amplify
  SDK?**

No, the Amplify SDK is required to use the Rekognition Face Liveness
feature.

- **Where can I find the error states associated with Face
  Liveness?**

You can see the different Face Liveness error states [here](https://ui.docs.amplify.aws/react/connected-components/liveness#error-states "https://ui.docs.amplify.aws/react/connected-components/liveness#error-states").

- **Face Liveness is not available in my region. How can I
  use the feature?**

You can choose to call Face Liveness in any of the regions where it is
available, depending on your trafffic load and proximity. Face liveness is
currently available in the following AWS regions:

    + US East (N. Virginia)
    + US West (Oregon)
    + Europe (Ireland)
    + Asia Pacific (Tokyo, Mumbai)

Even if your AWS account is located in a different region, latency
difference is not expected to be significant. You can obtain high-quality selfie
frame and audit images through Amazon S3 location or as raw bytes, but your Amazon S3
bucket must match the AWS region of Face Liveness. If they are different, you
must receive the images as raw bytes.

- **Does Amazon Rekognition Liveness Detection use customer
  content to improve the service?**

You may opt out of having your image and video inputs used to improve or
develop the quality of Rekognition and other Amazon
machine-learning/artificial-intelligence technologies by using an AWS
Organizations opt-out policy. For information about how to opt out, see [Managing AI Services opt-out policy](../../../organizations/latest/userguide/orgs_manage_policies_ai-opt-out.md "../../../organizations/latest/userguide/orgs_manage_policies_ai-opt-out.md").
