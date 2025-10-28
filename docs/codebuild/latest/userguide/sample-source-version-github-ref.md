# Specify a GitHub

repository version with a reference and commit ID

You can specify a source version with a reference and a commit ID in this format:
``refs`/`heads`/`branchname`^{`full-commit-SHA`}` (for example,`refs/heads/main^{12345678901234567890123467890123456789}`). If
you do this, CodeBuild downloads only the specified branch to find the version.

###### To specify a GitHub repository version with a reference and commit ID.

1. Complete the steps in [Specify a GitHub
   repository version with a commit ID](sample-source-version-github.md "sample-source-version-github.md").
2. From the left navigation pane, choose **Build projects**,
   and then choose the project you created earlier.
3. Choose **Start build**.
4. In **Source version**, enter
   `refs/heads/main^{046e8b67481d53bdc86c3f6affdd5d1afae6d369}`.
   This is the same commit ID and a reference to a branch in the format
   ``refs`/`heads`/`branchname`^{`full-commit-SHA`}`.
5. Choose **Start build**.
6. When the build is complete, you should see the following:
   - On the **Build logs** tab, which version of the
     project source was used. Here is an example.

   ```
   [Container] Date Time Running command echo $CODEBUILD_RESOLVED_SOURCE_VERSION
   046e8b67481d53bdc86c3f6affdd5d1afae6d369

   [Container] Date Time Phase complete: BUILD State: SUCCEEDED
   ```

   - On the **Environment variables** tab, the
     **Resolved source version** matches the commit ID
     used to create the build.
   - On the **Phase details** tab, the duration of the
     `DOWNLOAD_SOURCE` phase should be shorter than the
     duration when you used only the commit ID to specify the version of your
     source.
