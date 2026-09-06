

# Release: Elastic Beanstalk Amazon Linux AMI platforms are deprecated on July 8, 2021
<a name="release-2021-07-08-linux"></a>

This release announces the deprecation of AWS Elastic Beanstalk platforms based on Amazon Linux AMI (aka AL1). Final retirement date is set to June 30, 2022.

**Release date:** July 8, 2021

## Changes
<a name="release-2021-07-08-linux.changes"></a>

AWS Elastic Beanstalk is announcing today that our platform branches based on Amazon Linux AMI (aka AL1) *will retire on June 30, 2022*. With today's release, *all remaining Amazon Linux AMI platform branches, which haven't been deprecated before, are now deprecated.* For consistency and clarity, we've aligned the retirement date of all deprecated Amazon Linux AMI platform branches to be June 30, 2022, pushing out some previous retirement announcements by two months.

On June 30, 2022 these retiring branches will be marked **retired**. At that point, you will no longer be able to create new environments based on the retired platform branches. Elastic Beanstalk will stop providing new maintenance updates for these platform branches, and might also stop managing resources for your existing environments that use these platform branches.

There is no change before the retirement date. We will keep providing maintenance updates to the retiring platform branches, to allow for ample migration time. If you currently use any of these retiring platform branches, we strongly recommend that you start planning your migration from each one of them to a current, fully supported version.

After today, we will stop issuing release notes for Amazon Linux AMI platform updates. You can still find the latest software versions for any retiring platform branch in the [Retiring platform versions](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-retiring.html) page of the *AWS Elastic Beanstalk Platforms* guide.