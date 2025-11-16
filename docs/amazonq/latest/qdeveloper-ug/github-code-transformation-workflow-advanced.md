# Dynamically selecting a Java

version for GitHub workflow

The following dynamically code snippet dynamically chooses Java 17 when jobs are running
on a pull request created by the **Amazon Q code transform agent**. When you
decide to merge the open pull request to your default branch, you need to modify your
workflow file in the `.github/workflows/` directory to use Java 17 by
default.

```
name: Q Code Transformation

on:
  push:
    branches:
      - 'Q-TRANSFORM-issue-*'

env:
   MAVEN_CLI_OPTS: >-
     -Djava.version=${{ contains(github.event.head_commit.message, 'Code transformation completed') &&  '17' || '1.8' }}

jobs:
  q-code-transformation:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-java@v3
        with:
          java-version: ${{ contains(github.event.head_commit.message, 'Code transformation completed') && '17' || '8' }}

          distribution: 'adopt'

      - name: Build and copy dependencies
        run: |
          mvn ${{ env.MAVEN_CLI_OPTS }} verify
          mvn ${{ env.MAVEN_CLI_OPTS }} dependency:copy-dependencies -DoutputDirectory=dependencies -Dmdep.useRepositoryLayout=true -Dmdep.copyPom=true -Dmdep.addParentPoms=true

      - name: Upload artifacts
        uses: actions/upload-artifact@v4
        with:
          name: q-code-transformation-dependencies
          path: dependencies
```
