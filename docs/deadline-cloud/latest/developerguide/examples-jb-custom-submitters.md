# Build a custom submitter for Deadline Cloud

The
[custom\_submitters](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/custom_submitters "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/custom_submitters")
directory on the GitHub website holds reference submitters that go beyond what bundle
editing and the integrated submitters support. Use these as starting
points when your team needs UI controls, custom handlers, or fleet
attributes that the integrated submitter doesn't expose:

- [fuzzypixel\_maya](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/custom_submitters/fuzzypixel_maya "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/custom_submitters/fuzzypixel_maya")
  — The Maya custom submitter the AWS FuzzyPixel team developed
  for production. The submitter consolidates render settings into a
  single tab, exposes a QTree widget for activating individual render
  layers and overriding their resolution and frame range, surfaces
  custom fleet attributes (for example, `spot` or
  `onDemand`) as user-selectable options, and runs custom
  handlers that update `template.yaml` after the user
  clicks Submit.
  Custom submitters can co-exist with the integrated submitter, but
  they don't receive updates or patches that ship with the integrated
  submitter.
