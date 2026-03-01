# Recommendations and best practices for Amazon Connect Agent Workspace

Use the following recommendations and best practices to optimize applications in the Amazon Connect agent workspace.

###### Topics

- [Ensuring that apps can only be embedded in the Amazon Connect agent workspace](#recommendations-and-best-practices-embedded "#recommendations-and-best-practices-embedded")
- [Using multiple domains within an app](#recommendations-and-best-practices-multiple-domains "#recommendations-and-best-practices-multiple-domains")
- [Initializing Streams](#recommendations-and-best-practices-streams "#recommendations-and-best-practices-streams")
- [Accessibility](#recommendations-and-best-practices-accessibility "#recommendations-and-best-practices-accessibility")
- [Theming and styling](#recommendations-and-best-practices-theming-and-styling "#recommendations-and-best-practices-theming-and-styling")

## Ensuring that apps can only be embedded in the Amazon Connect agent workspace

It is recommended that apps correctly set the [Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy") header with [frame-ancestors](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/frame-ancestors "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/frame-ancestors") to only allow Amazon Connect instances.

```

Content-Security-Policy: frame-ancestors https://*.awsapps.com https://*.my.connect.aws;

```

## Using multiple domains within an app

Apps that use multiple domains, such as those supporting login flows, must add
additional domains to the approved origins list on the application configuration. Both
the domain specified in the _AccessUrl_ and any additional domains
added to the _Approved Origins_ will be incorporated into the Content
Security Policy for the agent workspace, allowing iframe integration for these
domains.

## Initializing Streams

Initializing the CCP via Streams, even if hidden, is not supported in third-party
applications. You must instead use contact and agent events when they are
available.

## Accessibility

The best practice is for your application to meet accessibility guidelines such as
[WCAG AA 2.1](https://www.w3.org/TR/WCAG21/ "https://www.w3.org/TR/WCAG21/"). The
following are some examples of automated and manual tests that you can conduct to ensure
that your app meets these guidelines.

###### Automated accessibility testing tools

1. **axe**: an open-source accessibility testing
   engine that can be integrated into your development workflow. It provides
   automated testing of web pages and applications for accessibility issues based
   on WCAG 2.1 standards.
2. **Pa11y**: a command-line interface that allows
   you to automate accessibility testing of web pages. It can be integrated into
   your continuous integration (CI) process to catch accessibility issues early in
   the development cycle.
3. **Lighthouse**: an open-source, automated tool
   for improving the quality of web pages. It includes an accessibility audit
   feature that can identify common accessibility issues and provide suggestions
   for improvement.
4. **WAVE**: a suite of evaluation tools that help
   authors make their web content more accessible to individuals with disabilities.
   It provides a browser extension and an online tool for automated accessibility
   testing.

###### Manual accessibility testing tools

1. **Screen Readers**: Use screen readers such as
   NVDA (NonVisual Desktop Access), JAWS (Job Access With Speech), and VoiceOver to
   manually test how users with visual impairments interact with your
   application.
2. **Keyboard Navigation**: Test the application
   using only a keyboard for navigation to ensure that all interactive elements,
   such as links and form controls, can be accessed and used without a
   mouse.
3. **Color Contrast Checkers**: Manual assessment of
   color contrast using tools like WebAIM's Contrast Checker to ensure that text
   and graphical elements have sufficient contrast for readability.
4. **User Testing**: Conduct manual accessibility
   testing with users who have disabilities to gain insights into how they interact
   with your application and to identify any barriers they may encounter. By using
   a combination of automated and manual tools, you can provide a comprehensive
   picture of your application's accessibility compliance. When documenting the
   testing process, be sure to include details about the tools used, the specific
   tests performed, and the results obtained to demonstrate your commitment to
   accessibility.

## Theming and styling

The [Amazon Connect SDK](https://github.com/amazon-connect/AmazonConnectSDK "https://github.com/amazon-connect/AmazonConnectSDK") includes a
standard Amazon Connect theme. We recommend that you use the theming package on top of
Cloudscape, such that third-party applications match the overall look and feel of the
Amazon Connect agent workspace.
