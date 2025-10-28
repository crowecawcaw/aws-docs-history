# Guidelines on face attributes

Here are specifics regarding how Amazon Rekognition processes and returns face
attributes.

- **FaceDetail Object**: For each detected face, a
  FaceDetail object is returned. This FaceDetail contains data on face landmarks,
  quality, pose, and more.
- **Attribute Predictions**: Attributes like
  emotion, gender, age, and others are predicted. A confidence level is assigned
  for each prediction, and the predictions are returned with the respective
  confidence score. A 99% confidence threshold is recommended for sensitive use
  cases. For age estimation, the midpoint of the predicted age range offers the
  best approximation.
  Note that gender and emotion predictions are based on physical appearance and should
  not be used for determining actual gender identity or emotional state. A gender binary
  (male/female) prediction is based on the physical appearance of a face in a particular
  image. It doesn't indicate a person’s gender identity, and you shouldn't use Rekognition to make such a determination. We don't recommend using gender binary
  predictions to make decisions that impact an individual's rights, privacy, or access to
  services. Similarly, a prediction of an emotional doesn't indicate a person’s actual
  internal emotional state, and you shouldn't use Rekognition to make such a
  determination. A person pretending to have a happy face in a picture might look happy,
  but might not be experiencing happiness.

**Application and Use Cases**

Here are some practical applications and use cases for these attributes:

- **Applications**: Attributes like Smile, Pose,
  and Sharpness can be utilized for selecting profile pictures or estimating
  demographics anonymously.
- **Common Use Cases**: Social media applications
  and demographic estimation at events or retail stores are typical
  examples.
  For more detailed information about each attribute, see [FaceDetail](../APIReference/API_FaceDetail.md "../APIReference/API_FaceDetail.md").
