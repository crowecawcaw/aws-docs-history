# Important Notes

Creating an AWS Control Tower environment establishes a trusted relationship with AWS Organizations, enabling drift detection
for preventive controls, and tracking of account and OU changes. During setup, AWS Control Tower creates a landing zone
configuration that serves as the foundation for your managed controls environment.

To create your controls-dedicated environment via APIs please see:
[Get started with AWS Control Tower using APIs](getting-started-apis.md "getting-started-apis.md").
Note that the manifest field is now optional with landing zone 4.0.
