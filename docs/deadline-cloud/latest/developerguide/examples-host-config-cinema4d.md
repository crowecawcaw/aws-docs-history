# Install Cinema 4D with Red Giant on Deadline Cloud Windows workers

The
[cinema4d\_redgiant](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/host_configuration_scripts/cinema4d/cinema4d_redgiant "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/host_configuration_scripts/cinema4d/cinema4d_redgiant")
host configuration script on the GitHub website installs Cinema 4D with Red Giant plugins on
Windows GPU service-managed fleet workers. The script fetches the
installers from Amazon S3 and runs each one in silent mode on each worker
launch.

###### Important

This script adds about 5-10 minutes to worker launch time, depending
on instance size. Plan accordingly for fleet scaling and job
scheduling.

To use this script, you need:

- A Maxon account to download the Red Giant and Maxon App
  installers.
- The Microsoft Edge WebView2 Runtime installer (required by the
  Maxon App installation).
- An Amazon S3 bucket where you upload the installers, and IAM
  permissions for the fleet to read them.
- A Windows GPU service-managed fleet with the latest GPU driver.
- Red Giant licenses, available on SMF and CMF through a license
  endpoint.
