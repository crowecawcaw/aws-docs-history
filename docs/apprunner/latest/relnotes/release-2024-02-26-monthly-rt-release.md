

AWS App Runner will no longer be open to new customers starting April 30, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

# Release: App Runner runtime updates on February 26, 2024
<a name="release-2024-02-26-monthly-rt-release"></a>

This release provides minor version updates for the Python and Corretto (Java SE) language runtimes. It also provides package updates to the Python and Ruby platforms.

**Release date:** February 26, 2024

## App Runner managed platforms
<a name="release-2024-02-26-monthly-rt-release.managed-platforms"></a>

App Runner provides convenient platform-specific managed runtimes. When you use a managed runtime, App Runner starts with a managed runtime base image to build a container image from your source code. For more information, see [ App Runner managed platforms](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code.html#service-source-code.managed-platforms) in the *AWS App Runner Developer Guide*.

## Changes
<a name="release-2024-02-26-monthly-rt-release.changes"></a>

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
  <tr><td>Base container image for AL2023</td><td>Updated base container image to version <b>2023.3.20240205.2.</b> This image only applies to Node.js 18 and Python 3.11 runtimes. </td></tr>
  <tr><td>Base container image for AL2</td><td>Updated base container image to version <b>2.0.20240131.0</b>. This image applies to all runtimes, except for Node.js 18 and Python 3.11. </td></tr>
</tbody>
</table>
<br />To view the Amazon Linux container image on the <i>Amazon ECR Public Gallery,</i> see the <i>Image tags</i> tab on <a href="https://gallery.ecr.aws/amazonlinux/amazonlinux">Amazon ECR Public Gallery - amazonlinux</a>. <br /></td></tr>
  <tr><td><b>Platform-specific updates</b></td><td>Made these platform-specific updates:
<table>
<thead>
  <tr><th><b>Platform</b></th><th><b>Update</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Python</b><br /> <a href="https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-python-releases.html">Supported runtimes</a> </td><td>Language runtime updates:<ul><li> Updated <b>Python 3.11</b> to version <a href="https://docs.python.org/release/3.11.8/whatsnew/changelog.html#changelog">3.11.8</a>. </li></ul><br />Package updates:<ul><li> Updated <b>SQLite </b>package to version <b>3.45.1</b> for <b>Python 3.11</b>, <b>Python 3.8</b>, and <b>Python 3.7</b>. For more information see <a href="https://www.sqlite.org/chronology.html">SQLite Release History</a>. </li></ul></td></tr>
  <tr><td><b>Corretto</b><br /><a href="https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-java-releases.html">Supported runtimes</a></td><td>Language runtime updates:<ul><li> Updated <b>Corretto 11</b> to version <a href="https://github.com/corretto/corretto-11/blob/develop/CHANGELOG.md">11.0.22.7.1</a>. </li><li> Updated <b>Corretto 8</b> to version <a href="https://github.com/corretto/corretto-8/blob/develop/CHANGELOG.md">8.402.08.1</a>. </li></ul><br />No package updates.</td></tr>
  <tr><td><b>Ruby</b><br /><a href="https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-ruby-releases.html">Supported runtimes </a></td><td>No updates to language versions.<br />Package updates:<ul><li> Updated <b>SQLite</b>package to version <b>3.45.1</b> for <b>Ruby 3.1</b>. For more information see <a href="https://www.sqlite.org/chronology.html">SQLite Release History</a>. </li></ul></td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>
