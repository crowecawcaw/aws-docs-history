

AWS App Runner will no longer be open to new customers starting April 30, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

# Release: App Runner runtime updates on January 18, 2024
<a name="release-2024-01-18-monthly-rt-release"></a>

This release provides minor version updates for the .NET Core and PHP language runtimes. It also provides package updates to the Python and Ruby platforms.

**Release date:** January 18, 2024

## App Runner managed platforms
<a name="release-2024-01-18-monthly-rt-release.managed-platforms"></a>

App Runner provides convenient platform-specific managed runtimes. When you use a managed runtime, App Runner starts with a managed runtime base image to build a container image from your source code. For more information, see [ App Runner managed platforms](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code.html#service-source-code.managed-platforms) in the *AWS App Runner Developer Guide*.

## Changes
<a name="release-2024-01-18-monthly-rt-release.changes"></a>

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
  <tr><td>Base container image for AL2023 </td><td>Updated base container image to version <b>2023.3.20240108.0</b>. This image only applies to Node.js 18 and Python 3.11 runtimes. </td></tr>
  <tr><td>Base container image for AL2</td><td>Updated base container image to version <b>2.0.20240109.0</b>. This image applies to all runtimes, except for Node.js 18 and Python 3.11. </td></tr>
</tbody>
</table>
<br /> To view the Amazon Linux container image on the <i>Amazon ECR Public Gallery,</i> see the <i>Image tags</i> tab on <a href="https://gallery.ecr.aws/amazonlinux/amazonlinux">Amazon ECR Public Gallery - amazonlinux</a>. <br /></td></tr>
  <tr><td><b>Platform-specific updates</b></td><td>Made these platform-specific updates:
<table>
<thead>
  <tr><th><b>Platform</b></th><th><b>Update</b></th></tr>
</thead>
<tbody>
  <tr><td><b>.NET Core</b><br /><a href="https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-net6-releases.html">Supported runtimes </a></td><td>Updated <b>.NET Core 6.0</b> to version <a href="https://github.com/dotnet/core/blob/main/release-notes/6.0/6.0.26/6.0.26.md">6.0.26</a>.<br />Package updates:<ul><li> Updated <b>dotnet6-sdk</b> package to version <b>6.0.418</b>. For more information see <a href="https://github.com/dotnet/core/blob/main/release-notes/6.0/6.0.26/6.0.26.md">6.0.26</a> Release Notes. </li></ul></td></tr>
  <tr><td><b>PHP</b><br /><a href="https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-php-releases.html">Supported runtimes </a></td><td>Updated <b>PHP 8.1</b> to version <a href="https://www.php.net/releases/8_1_27.php">8.1.27</a>.<br />No package updates.</td></tr>
  <tr><td><b>Python</b><br /><a href="https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-python-releases.html">Supported runtimes</a></td><td>No updates to language versions.<br />Package updates:<ul><li> Updated <b>SQLite </b>package to version <b>3.44.2</b> for <b>Python 3.7</b> and <b>Python 3.8</b>. For more information see <a href="https://www.sqlite.org/chronology.html">SQLite Release History</a>. </li></ul></td></tr>
  <tr><td><b>Ruby</b><br /><a href="https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-ruby-releases.html">Supported runtimes </a></td><td>No updates to language versions.<br />Package updates:<ul><li> Updated <b>SQLite </b>package to version <b>3.44.2</b> for <b>Ruby 3.1</b>. For more information see <a href="https://www.sqlite.org/chronology.html">SQLite Release History</a>. </li></ul></td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>
