

AWS App Runner will no longer be open to new customers starting April 30, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

# Release: App Runner runtime updates on July 31, 2024
<a name="release-2024-07-31-monthly-rt-release"></a>

This release provides minor version updates for the following language runtimes: Java, .NET, Node.js. It also provides package updates to the following platforms: .NET. 

**Release date:** July 31, 2024

## App Runner managed platforms
<a name="release-2024-07-31-monthly-rt-release.managed-platforms"></a>

App Runner provides convenient platform-specific managed runtimes. When you use a managed runtime, App Runner starts with a managed runtime base image to build a container image from your source code. For more information, see [ App Runner managed platforms](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code.html#service-source-code.managed-platforms) in the *AWS App Runner Developer Guide*.

## Changes
<a name="release-2024-07-31-monthly-rt-release.changes"></a>

The following table lists the changes included in this release.


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Base container image updates</b></td><td>Made the following updates to the base container images: 
<table>
<thead>
  <tr><th><b>Component</b></th><th><b>Update</b></th></tr>
</thead>
<tbody>
  <tr><td>Base container image for AL2023 </td><td>Updated base container image to version <b>2023.5.20240722.0</b>. This image only applies to Node.js 18 and Python 3.11 runtimes. </td></tr>
  <tr><td>Base container image for AL2</td><td>Updated base container image to version <b>2.0.20240719.0</b>. This image applies to all runtimes, except for Node.js 18 and Python 3.11. </td></tr>
</tbody>
</table>
<br /> To view the Amazon Linux container image on the <i>Amazon ECR Public Gallery,</i> see the <i>Image tags</i> tab on <a href="https://gallery.ecr.aws/amazonlinux/amazonlinux">Amazon ECR Public Gallery - amazonlinux</a>. <br /></td></tr>
  <tr><td><b>Platform-specific updates</b></td><td>Made these platform-specific updates:
<table>
<thead>
  <tr><th><b>Platform</b></th><th><b>Update</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Corretto</b></td><td>Language version updates:<ul><li> Updated Corretto 11 to 11.0.24.8.1. For more information, see the <a href="https://github.com/corretto/corretto-11/blob/develop/CHANGELOG.md">release notes</a>. </li><li> Updated Corretto 8 to 8.422.05.1. For more information, see the <a href="https://github.com/corretto/corretto-8/blob/develop/CHANGELOG.md">release notes</a>. </li></ul><br />No package updates.</td></tr>
  <tr><td><b>.NET Core</b><br /><a href="https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-dotnet-releases.html">Supported runtimes </a></td><td>Updated <b>.NET Core 6.0</b> to 6.0.32. <br />Package updates:<ul><li> Updated .NET SDK to 6.0.424.  </li></ul></td></tr>
  <tr><td><b>Node.js</b><br /><a href="https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-nodejs-releases.html">Supported runtimes </a></td><td>Updated Node.js 18 to 18.20.4. <br />No package updates.</td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>
