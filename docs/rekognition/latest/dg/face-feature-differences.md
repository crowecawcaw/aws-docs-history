# Overview of face detection and face

comparison

Amazon Rekognition provides users access to two primary machine learning applications for
images containing faces: face detection and face comparison. They empower crucial
features like facial analysis and identity verification, making them vital for various
applications from security to personal photo organization.

**Face Detection**

A face detection systems address the question: "Is there a face in this picture?" Key
aspects of face detection include:

- **Location and orientation**: Determines the
  presence, location, scale, and orientation of faces in images or video
  frames.
- **Face attributes**: Detects faces regardless of
  attributes like gender, age, or facial hair.
- **Additional Information**: Provides details on
  face occlusion and eye gaze direction.
  **Face Comparison**

A face comparison systems focus on the question: "Does the face in one image match a
face in another image?" Face comparison system functionalities include:

- **Face matching predictions**: Compares a face in
  an image against a face in a provided database to predict matches.
- **Face attribute handling**: Handles attributes
  to compares faces regardless of expression, facial hair, and age.
  **Confidence scores and missed detections**

Both face detection and face comparison systems utilize confidence scores. A
confidence score indicates the likelihood of predictions, such as the presence of a face
or a match between faces. Higher scores indicate greater likelihood. For instance, 90%
confidence suggests a higher probability of a correct detection or match than
60%.

If a face detection system doesn’t properly detect a face, or provides a low
confidence prediction for an actual face, this is a missed detection/false negative. If
the system incorrectly predicts the presence of a face at a high confidence level, this
is a false alarm/false positive.

Similarly, a facial comparison system may not match two faces which belong to the same
person (missed detection/false negative) or may incorrectly predict that two faces from
different people are the same person (false alarm/false positive).

**Application design and threshold setting**

- You can set a threshold that specifies the minimum confidence level required
  to return a result. Choosing appropriate confidence thresholds is essential for
  application design and decision-making based on the system outputs.
- Your chosen confidence level should reflect your use case. Some examples of
  use cases and confidence thresholds:
- - **Photo Applications**: A lower threshold
    (e.g., 80%) might suffice for identifying family members in
    photos. + **High-Stakes Scenarios**: In use cases
    where the risk of missed detection or false alarm is higher, such as
    security applications, the system should use a higher confidence level.
    In such cases, a higher threshold (e.g., 99%) is recommended for
    accurate facial matches.
    For more information on setting and understanding confidence thresholds, see [Searching faces in a collection](collections.md "collections.md").
