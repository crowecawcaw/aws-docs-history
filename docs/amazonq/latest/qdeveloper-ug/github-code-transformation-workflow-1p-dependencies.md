# Handling first-party

dependencies in GitHub workflows

You can enhance your GitHub workflow to handle first-party dependencies when using
Amazon Q Developer for code transformation.

The standard Amazon Q Developer workflow handles projects with public Maven dependencies.
However, enterprise projects often include first-party dependencies, including private Java
ARchive (JAR files) not available in public repositories. This enhanced workflow extends the
standard configuration to support both public and private dependencies.

## Use cases

for enhanced workflow

Use the enhanced GitHub workflow configuration if your project has:

- Private or internal JAR dependencies
- Custom utility libraries not available in Maven Central
- Build failures with `Could not resolve dependencies` errors

## Example Configuration

The following example shows a complete workflow configuration that handles first-party
dependencies:

```
name: Q Code Transformation

on:
  push:
    branches:
      - 'Q-TRANSFORM-issue-*'

env:
   MAVEN_CLI_OPTS: >-
     -Djava.version=${{ contains(github.event.head_commit.message, 'Code transformation completed') && '17' || '1.8' }}
     -Dmaven.compiler.source=${{ contains(github.event.head_commit.message, 'Code transformation completed') && '17' || '1.8' }}
     -Dmaven.compiler.target=${{ contains(github.event.head_commit.message, 'Code transformation completed') && '17' || '1.8' }}

jobs:
  q-code-transformation:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with:
          java-version: ${{ contains(github.event.head_commit.message, 'Code transformation completed') && '17' || '8' }}
          distribution: 'temurin'

      - name: Cache Maven dependencies
        uses: actions/cache@v4
        with:
          path: ~/.m2
          key: ${{ runner.os }}-m2-${{ hashFiles('**/pom.xml') }}
          restore-keys: ${{ runner.os }}-m2

      - name: Install First-Party Dependencies
        run: |
          mvn install:install-file \
            -Dfile=./your-library/built-library/1.0.0/your-library-1.0.0.jar \
            -DgroupId=com.yourcompany.samples \
            -DartifactId=your-library \
            -Dversion=1.0.0 \
            -Dpackaging=jar

      - name: Build and copy dependencies
        run: |
          mvn ${{ env.MAVEN_CLI_OPTS }} verify
          mvn ${{ env.MAVEN_CLI_OPTS }} dependency:copy-dependencies -DoutputDirectory=dependencies -Dmdep.useRepositoryLayout=true -Dmdep.copyPom=true -Dmdep.addParentPoms=true

      - name: Upload artifacts
        uses: actions/upload-artifact@v4
        with:
          name: q-code-transformation-dependencies
          path: dependencies

      - name: Debug information
        if: failure()
        run: |
          echo "Branch: ${{ github.ref_name }}"
          echo "Commit message: ${{ github.event.head_commit.message }}"
          echo "Java version logic result: ${{ contains(github.event.head_commit.message, 'Code transformation completed') && '17' || '8' }}"
          echo "Local Maven repository contents:"
          find ~/.m2/repository/com/yourcompany/samples -name "*.jar" 2>/dev/null || echo "No your-library found in local repo"
          java -version
          mvn -version

```

## Key

components of enhanced workflow

The enhanced GitHub workflow has several key components:

- **First-party dependency installation**

The workflow includes a critical step for installing private dependencies using
the Maven `install:install-file` command. This ensures your private
dependencies are available in the local Maven repository during transformation.

- **Dynamic Java version handling**

The workflow automatically switches between Java 8 and Java 17 based on the
transformation state, using environment variables to manage compiler
properties.

- **Maven configuration**

The enhanced workflow includes comprehensive Maven configuration with:

    + Dependency caching for improved performance
    + Complete compiler property management
    + Repository layout preservation
    + POM file handling

- **Implementation steps**
  - Identify your private dependencies in `pom.xml`
  - Organize JAR files in your repository structure
  - Customize the workflow with your specific paths and coordinates
  - Test the workflow on a branch matching the pattern
    `Q-TRANSFORM-issue-*`

- **Troubleshooting**

The workflow includes a debug information step that activates on failure,
providing:

    + Branch information
    + Commit message details
    + Java version configuration
    + Local Maven repository contents
    + Java and Maven version information
