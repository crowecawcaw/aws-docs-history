

AWS App Runner will no longer be open to new customers starting April 30, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

# Release: App Runner runtime updates on April 29, 2024
<a name="release-2024-04-29-monthly-rt-release"></a>

This release provides minor version updates for the Python, Node.js Corretto (Java SE), .NET Core, and PHP language runtimes. It also provides package updates to the Python, Node.js, .NET Core, and Ruby platforms.

**Release date:** April 29, 2024

## App Runner managed platforms
<a name="release-2024-04-29-monthly-rt-release.managed-platforms"></a>

App Runner provides convenient platform-specific managed runtimes. When you use a managed runtime, App Runner starts with a managed runtime base image to build a container image from your source code. For more information, see [ App Runner managed platforms](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code.html#service-source-code.managed-platforms) in the *AWS App Runner Developer Guide*.

## Changes
<a name="release-2024-04-29-monthly-rt-release.changes"></a>

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
  <tr><td>Base container image for AL2023 </td><td>Updated base container image to version <b>2023.4.20240416.0</b>. This image only applies to Node.js 18 and Python 3.11 runtimes. </td></tr>
  <tr><td>Base container image for AL2</td><td>Updated base container image to version <b>2.0.20240412.0</b>. This image applies to all runtimes, except for Node.js 18 and Python 3.11. </td></tr>
</tbody>
</table>
<br /> To view the Amazon Linux container image on the <i>Amazon ECR Public Gallery,</i> see the <i>Image tags</i> tab on <a href="https://gallery.ecr.aws/amazonlinux/amazonlinux">Amazon ECR Public Gallery - amazonlinux</a>. <br /></td></tr>
  <tr><td><b>Platform-specific updates</b></td><td>Made these platform-specific updates:
<table>
<thead>
  <tr><th><b>Platform</b></th><th><b>Update</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Corretto</b></td><td>Language runtime updates:<ul><li> Updated Corretto 11 to version <a href="https://github.com/corretto/corretto-11/blob/develop/CHANGELOG.md">11.0.23.9.1</a>. </li><li> Updated Corretto 8 to version <a href="https://github.com/corretto/corretto-8/blob/develop/CHANGELOG.md">8.412.08.1</a>. </li></ul></td></tr>
  <tr><td><b>.NET Core</b><br /><a href="https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-net6-releases.html">Supported runtimes </a></td><td>Updated <b>.NET Core 6.0</b> to version <a href="https://github.com/dotnet/core/blob/main/release-notes/6.0/6.0.29/6.0.29.md">6.0.29</a>.<br />Package updates:<ul><li> Updated <b>dotnet6-sdk</b> package to version <b>6.0.421</b>. For more information see <a href="https://github.com/dotnet/core/blob/main/release-notes/6.0/6.0.29/6.0.29.md">6.0.29</a> Release Notes. </li></ul></td></tr>
  <tr><td><b>Node.js</b><br /><a href="https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-nodejs-releases.html">Supported runtimes </a></td><td>Updated Node.js 18 to version <a href="https://nodejs.org/en/blog/release/v18.20.2">18.20.2</a><br />Tools Updates:<ul><li> Updated npm to version 10.5.0. </li></ul></td></tr>
  <tr><td><b>PHP</b><br /><a href="https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-php-releases.html">Supported runtimes </a></td><td>Updated <b>PHP 8.1</b> to version <a href="https://www.php.net/releases/8_1_28.php">8.1.28</a>.<br />No package updates.</td></tr>
  <tr><td><b>Python</b><br /><a href="https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-python-releases.html">Supported runtimes</a></td><td>Updated Python 3.11 from version 3.11.8 to <a href="https://docs.python.org/release/3.11.9/whatsnew/changelog.html#changelog">Python 3.11.9</a>.<br />No updates to language versions.<br />Package updates:<ul><li> Updated <b>SQLite </b>package to version <b>3.45.3</b> for <b>Python 3.7</b>, <b>Python 3.8</b>, and <b>Python 3.11</b>. For more information see <a href="https://www.sqlite.org/chronology.html">SQLite Release History</a>. </li></ul></td></tr>
  <tr><td><b>Ruby</b><br /><a href="https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code-ruby-releases.html">Supported runtimes </a></td><td>No updates to language versions.<br />Package updates:<ul><li> Updated <b>SQLite </b>package to version <b>3.45.3</b> for <b>Ruby 3.1</b>. For more information see <a href="https://www.sqlite.org/chronology.html">SQLite Release History</a>. </li></ul></td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>
