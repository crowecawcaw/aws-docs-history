

# Requirements for the contextual metadata output

To add customer decisions, add a `customQuestions` object to a contextual metadata output. The output must meet the following requirements. Otherwise, the request fails with a `ValidationException`.
+ **Extended analysis is disabled** – You must explicitly set `extendedAnalysis` to `DISABLED` on the output. If you omit `extendedAnalysis`, Elemental Inference treats it as `ENABLED`, and the request fails. As a result, an output that has customer decisions doesn't return the `people`, `environments`, `brands`, and `onScreenTexts` labels.
+ **At least one of shot or scene** – The `customQuestions` object must contain `shot`, `scene`, or both.
+ **The version exists** – Each reference must name a question set in your account, and a version that exists. The version must be `DRAFT`, or a published version that you haven't deleted. If not, the error message names the question set, the version, and the output.