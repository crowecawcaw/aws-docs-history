

AWS App Runner will no longer be open to new customers starting April 30, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

# Performance changes for code-based services on Jun 14, 2024
<a name="release-2024-06-14-performance-changes-runtimes"></a>

**Release date:** Jun 14, 2024

## Changes
<a name="release-2024-06-14-performance-changes-runtimes.changes"></a>

Starting from 17 Jun, 2024, customers using the following runtimes are expected to see an increase in build time by approximately 240 seconds.
+ Node.js 12
+ Node.js 14
+ Corretto 8
+ Corretto 11
+ Python 3.7
+ Python 3.8

To maintain similar build times, we recommend that Node.js 12 and Node.js 14 users migrate to Node.js 18 and that Python 3.7 and Python 3.8 users migrate to Python 3.11. Otherwise, since builds are billed by time, expect an associated increase in cost. For more information about App Runner pricing, see  [App Runner Pricing](https://aws.amazon.com/apprunner/pricing). 