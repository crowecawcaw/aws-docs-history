# Features and Capabilities

## Supported Technologies

- **Languages**: Python and Scala applications
- **Build Systems**: Maven and SBT for Scala projects; requirements.txt, Pipfile, and Setuptools for Python projects
- **Target Platforms**: Amazon EMR and EMR Serverless
- **Supported Versions**: We support Apache Spark upgrades from version 2.4 to 3.5. The corresponding deployment mode mappings are as follows
  - **For EMR-EC2**
    - **Source Version:** EMR 5.20.0 and later
    - **Target Version:** EMR 7.12.0 and earlier, should be newer than EMR 5.20.0

  - **For EMR Serverless**
    - **Source Version:** EMR Serverless 6.6.0 and later
    - **Target Version:** EMR Serverless 7.12.0 and earlier

## What We Upgrade

The upgrade agent provide comprehensive Spark application upgrades:

- **Build Configuration**: Automatically updates dependency management files (pom.xml, requirements.txt, etc.)
- **Source Code**: Fixes API compatibility issues and deprecated method usage
- **Test Code**: Ensures unit and integration tests work with the target Spark version
- **Dependencies**: Upgrades packaged dependencies to versions compatible with target EMR version
- **Validation**: Compiles and validates applications on target EMR clusters
- **Data Quality Analysis**: Detects schema differences, value-level statistical drifts (min/max/mean), and aggregate row-count mismatches, with detailed impact reporting.

## Available Regions

The Spark Upgrade Agent is available in the following regions:

- **Asia Pacific**: Tokyo (ap-northeast-1), Seoul (ap-northeast-2), Singapore (ap-southeast-1), Sydney (ap-southeast-2), and Mumbai (ap-south-1)
- **North America**: Canada (ca-central-1)
- **Europe**: Stockholm (eu-north-1), Ireland (eu-west-1), London (eu-west-2), Paris (eu-west-3), and Frankfurt (eu-central-1)
- **South America**: São Paulo (sa-east-1)
- **United States**: North Virginia (us-east-1), Ohio (us-east-2), and Oregon (us-west-2)

## Scope of Upgrades and User Requirements

- **Cluster Management**: Spark Upgrade Agent focuses on application code upgrades. Target EMR clusters for new versions must be created and managed by users.
- **Bootstrap Actions**: Spark Upgrade Agent does not upgrade custom bootstrap scripts outside of Spark application code. They need to be upgraded by the user.
- **Upgrade for Build and Tests**: The upgrade agent will perform build and run your unit and integration tests on your development environment locally to validate that applications compile successfully with the target Spark version. If you have restrictions (security policies, resource limitations, network restrictions, or corporate guidelines) for Spark application code for local execution, consider using
  [Amazon SageMaker Unified Studio VSCode IDE Spaces](../../../sagemaker-unified-studio/latest/userguide/create-space.md "../../../sagemaker-unified-studio/latest/userguide/create-space.md") or EC2 to run the upgrade agent. The upgrade agent uses your target EMR-EC2 cluster or EMR-S applications to validate and upgrade end-to-end.
- **Error-Driven Approach**: The upgrade agent uses an error-driven methodology, making one fix at a time based on compilation or runtime errors rather than multiple fixes at once. This iterative approach ensures each issue is properly addressed before proceeding to the next.
- **Private Dependencies**: Dependencies installed from private artifact repositories cannot be automatically upgraded as part of this process. They must be upgraded by the user.
- **Regional resources**: Spark upgrade agent is regional and uses the underlying EMR resources in that region for the upgrade process. Cross-region upgrades are not supported.
