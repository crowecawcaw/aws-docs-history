AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# AWS Mainframe Modernization components lifecycle

Each component of AWS Mainframe Modernization goes through version upgrades and a development lifecycle.
You can use this page as an overview to understand these components, their version upgrade
plans, and how AWS Mainframe Modernization communicates the release or deprecation of these components or their
versions.

## Components lifecycle overview

AWS Mainframe Modernization lifecycle describes the approach and timelines for releasing and supporting
AWS Mainframe Modernization service components throughout their lifecycle. Providing predictable and
consistent lifecycle helps you as you plan, test, and deploy newer versions.

All AWS-provided AWS Mainframe Modernization components benefit from the product support provided by
Support from the time they are released until their retirement per each component's
release calendar table. You can learn more about the Support scope and activities at
[Compare Support
Plans](https://aws.amazon.com/premiumsupport/plans/ "https://aws.amazon.com/premiumsupport/plans/"). During active modernization projects, we typically encourage customer
support to be provided first by professional services delivery teams as per the
statement of work.

AWS Mainframe Modernization releases some components with versions originating from suppliers which can
be AWS itself, select AWS Partners, or communities. For each AWS Mainframe Modernization component, a
version has a major version number and a minor version number. Each component has its
own major and minor version numbering.

For versioned components, we have the following intents:

- To release AWS Mainframe Modernization **components newer versions on a
  regular basis** or per customer demand. If a component's newer
  version is desired and not yet available in the AWS Mainframe Modernization service, you can make
  an explicit request via Support Product Feature Request (PFR).
- To have AWS Mainframe Modernization component-specific versions' **end of
  support and retirement dates align** with the component supplier
  end of support dates.
- To **notify customers** approximately one year
  prior to the retirement of a component's major version.

While we strive to meet these guidelines, in some cases, we may retire specific
versions sooner with shorter notification timeframes. For example, we may retire a
version with security issues promptly with a shorter notification timeframe. We may also
retire minor versions early when a minor version has significant bugs or security issues
that have been resolved in a later minor version. In the unlikely event that such cases
occur, we will notify customers and communicate about the plan and the timeline for
retirement. Specific circumstances may dictate different timelines depending on the
situation.

###### Note

Critical updates to components might be made available at any time. For example, new
versions may be made available promptly for security reasons or to provide fixes for
the production environments. For requests made through Support, the support plan
dictates the processes, severity, and the response times.

When a component version is retired, AWS Mainframe Modernization doesn't distribute these versions to
customers for new deployments. Consequently, these versions are also unsupported by
Support. Customers running existing component deployments past their version retirement
dates should be aware of the risks of doing so. AWS is not responsible to provide
security updates, technical support, or hot fixes for retired component versions. Also,
we don't automatically remove access or delete your environment's resources. We strongly
encourage you check for new versions every 3 months, and upgrade all your AWS Mainframe Modernization
components to recent supported versions.

## Version upgrade

AWS Transform for Mainframe Refactor regularly releases new versions of its transformation engine and supporting components. These updates deliver bug fixes, security improvements, performance enhancements, expanded platform support, and new modernization capabilities.
We strongly recommend upgrading regularly to take advantage of the latest fixes, features, and security updates. When a new version becomes available, you control if and when to apply it to your transformation projects and generated artifacts.
Version releases follow a Major.Minor.Patch numbering scheme and fall into three categories:

- **Major** releases introduce significant new capabilities or structural changes. These typically include:

      + Support for additional legacy platforms (e.g., Fujitsu GS21).
      + New legacy language support (e.g., Natural).
      + New legacy database support (e.g., Adabas, Fujitsu NDB).
      + Major version updates to the target modernization stack (e.g., newer Spring, Java, or PostgreSQL versions).

  Major releases may introduce _breaking changes_ that require adjustments to existing modernized applications, especially when regenerating code or adapting to updated target architecture definitions.

- **Minor** releases deliver evolutionary improvements, bug fixes, and maintenance updates. They keep both the supported legacy platform/language/database definitions
  and the target modernization stack unchanged.

However, minor releases can still include _breaking changes_ in generated source code or runtime classes with internal usage purpose.
This may affect already modernized applications that have undergone manual post-generation maintenance and cannot be safely regenerated from the original legacy sources without additional rework.

- **Patch** releases serve as an emergency channel to quickly address critical regressions or urgent fixes introduced in recent versions while preserving compatibility.
  They are narrowly scoped and aim to restore stability with minimal risk.

To minimize risks during any upgrade:

- Always run comprehensive non-regression tests before applying version changes to live or production-bound projects.
- Leverage DevOps test and deployment pipelines (ideally built during your modernization initiative) to automate validation of generated code and runtime behavior after upgrades.
- Consider blue/green or canary deployment strategies for runtime environments when upgrading components.

For more guidance on deployment strategies and change management,
refer to the [AWS Well-Architected Reliability Pillar](../../../wellarchitected/latest/reliability-pillar/rel_tracking_change_management_immutable_infrastructure.md#implementation-guidance "../../../wellarchitected/latest/reliability-pillar/rel_tracking_change_management_immutable_infrastructure.md#implementation-guidance").

## AWS Mainframe Modernization Refactor with AWS Blu Age release overview

With AWS Blu Age runtime, the version follows a `Major.Minor.Patch` pattern. For
example, for AWS Blu Age runtime version `4.1.0`, the major version is 4, the minor
version is 1, and the patch version is 0.

We intend to release new AWS Blu Age runtime major versions when there are impactful changes
to runtime or their dependencies. AWS Blu Age runtime major versions are supported for at least
12 months unless some **Common Vulnerabilities and Exposures
(CVEs)** appear. The support covers for bugs in the runtime features as
mentioned in our documentation. In case of Critical and High CVEs in the dependencies of
the runtime (Spring, Java, Tomcat, and others), the major version support duration is
reduced to 6 months for High CVEs, and 3 months for Critical CVEs from the release date
of the new runtime version fixing the CVE, unless explicitly stated otherwise.

We intend to release new AWS Blu Age minor versions monthly. Customers are expected to
upgrade versions regularly to obtain the latest security fixes, bug fixes, and feature
enhancements. Active projects not yet in production have to adopt the latest runtime
version as soon as it becomes available.

New fixes are provided in the latest minor version for the particular major version
where an issue is raised. If you require new fixes, you need to upgrade to a new minor
version to apply those fixes.

Patched versions for supported releases are provided only to address critical runtime
defects not present in previous supported minor versions.

Alpha pre-releases are short-lived versions made available for quick iteration during
delivery projects. Fixes for issues identified in alpha pre-releases are provided in the
later minor versions, as no patches are delivered for Alpha pre-release versions.

You can find release dates and details about each runtime version in the [AWS Blu Age release notes](ba-release-notes.md "ba-release-notes.md").

Security scans are performed by [Amazon
Inspector](https://aws.amazon.com/inspector/ "https://aws.amazon.com/inspector/").
