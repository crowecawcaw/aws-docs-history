

# Release: AWS Elastic Beanstalk Go platform update on December 14, 2018
<a name="release-2018-12-14-golang"></a>

This release applies security updates to the Go platform for AWS Elastic Beanstalk, and updates platform configuration. The release also includes a Go runtime update, bug fixes, and, for certain AWS Regions, support for additional Amazon EC2 instance types.

**Release date:** December 14, 2018

## Changes
<a name="release-2018-12-14-golang.changes"></a>

Here is a list of the key changes in this release.


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Security updates</b></td><td>Applied all security updates published in the <a href="https://alas.aws.amazon.com/">Amazon Linux Security Center</a> on or before December 7, 2018 to the Go platform.<br />See also the <b>Go updates</b> entry.</td></tr>
  <tr><td><b>Go updates</b></td><td>Applied minor revision 1.11.3. For details, see <a href="https://golang.org/doc/devel/release.html#go1.11">go1.11</a> in <i>The Go Programming Language Release History</i>.<br />Revision 1.11.3 addresses three recently reported security issues. For details, see <a href="https://groups.google.com/forum/#!topic/golang-announce/Kw31K8G7Fi0">[security] Go 1.11.3 and Go 1.10.6 are released</a>.</td></tr>
  <tr><td><b>Instance types</b></td><td>Added support for more Amazon EC2 instance types in some AWS Regions, for the Go platform, as follows:
<table>
<thead>
  <tr><th><b>Instance type</b></th><th><b>Regions</b></th></tr>
</thead>
<tbody>
  <tr><td><b>T3</b></td><td> <ul><li>Asia Pacific (Seoul) – ap-northeast-2</li><li>Europe (Paris) – eu-west-3</li><li>AWS GovCloud (US-West) – us-gov-west-1</li></ul> </td></tr>
  <tr><td><b>C5n</b></td><td> <ul><li>US East (Ohio) – us-east-2</li><li>US East (N. Virginia) – us-east-1</li><li>US West (Oregon) – us-west-2</li><li>Europe (Ireland) – eu-west-1</li><li>AWS GovCloud (US-West) – us-gov-west-1</li></ul> </td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>


## Updated platform configurations
<a name="release-2018-12-14-golang.platforms"></a>

### Go
<a name="release-2018-12-14-golang.platforms.go"></a>



|  Configuration and *Solution Stack Name*   |  AMI  |  Language  |  AWS X‑Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | 
|  **Go 1.11 version 2.9.3** <br /> * 64bit Amazon Linux 2018.03 v2.9.3 running Go 1.11.3 *  | 2018.03.0 | Go 1.11.3 | 2.0.0 | nginx 1.12.1 | 