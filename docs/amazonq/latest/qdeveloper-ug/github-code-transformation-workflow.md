# Customizing a workflow for code transformation

###### Note

Amazon Q Developer for GitHub is in preview release and is subject to change.

When the Amazon Q Developer code transformation agent creates a pull request in GitHub after completing the task, your
project pipeline runs the jobs that are configured to run for pull requests. Since the updated code targets Java 17,
the jobs encounter build errors if the job attempts to build them using Java 8 or Java 11.

Before you apply the **Amazon Q transform agent** label to a GitHub issue, you need to create and
configure a workflow file in the `.github/workflows/` directory to handle code transformation
tasks.

###### To customize a workflow for code transformation

1. If your repository doesn't already have a workflow, create a GitHub Actions workflow file. For more information,
   see [Quickstart
   for GitHub actions](https://docs.github.com/en/actions/writing-workflows/quickstart "https://docs.github.com/en/actions/writing-workflows/quickstart") and [Creating
   an example workflow](https://docs.github.com/en/actions/use-cases-and-examples/creating-an-example-workflow "https://docs.github.com/en/actions/use-cases-and-examples/creating-an-example-workflow") in the _GitHub documentation_.
2. Update your workflow file with the following job:

```
q-code-transformation:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-java@v3
        with:
          java-version: '17'
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
