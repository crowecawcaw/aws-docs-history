# Recommendations for Usage of Face

Liveness

We recommend the following best practices when using Rekognition Face Liveness:

- Users should complete the Face Liveness check in environments that aren’t too
  dark or too bright and have fairly uniform lighting.
- Users should increase their display screen's brightness to its maximum level
  when making checks on web browsers. Mobile Native SDKs adjust the display
  brightness automatically.
- Choose a confidence score threshold that reflects the nature of your use case.
  For use cases with greater security concerns, use a high threshold.
- Regularly run human review checks on audit images to make sure that spoof
  attacks are mitigated at the confidence threshold you set.
- Offer an alternative face liveness verification path to your users if they are
  photo-sensitive or do not want to verify their face liveness using Rekognition.
- Do not send or display the liveness check score on the user application. Only
  send a pass or fail signal.
- Allow only five failed liveness checks in three minutes from a single device.
  After five fails, timeout the user for 30–60 minutes. If the pattern is
  seen 3–5 times repeatedly, block the user device from making additional
  calls.
- Implement the get-ready screen in your workflow so that users can more easily
  pass the Face Liveness checks.
- You are responsible for providing legally adequate privacy notices to, and
  obtaining any necessary consent from, your End Users for the processing,
  storage, use, and transfer of content by Face Liveness.
