# Optionally configure auto-enrollment for

accounts

When you enable this feature during setup, or later, accounts that are moved between two registered
OUs, or moved into your AWS Control Tower environment for the first time, no longer show
a state of inheritance drift. The accounts automatically inherit the baselines and controls that are
enabled on the new OU. Controls and baselines from the previous OU are removed.

To opt in for auto-enrollment at any time after setup, navigate to the landing zone
**Settings** page and choose **Update**
landing zone, or call the AWS Control Tower `UpdateLandingZone` API.

You can move an account between OUs by means of the AWS Organizations API, or by means of the
AWS Control Tower console. If you move an account outside an OU that's registered, AWS Control Tower
removes all deployed baselines and controls, automatically. It essentially unenrolls the account from AWS Control Tower.

###### Note

If you choose to enable the auto-enroll capability after initial setup of the landing zone, AWS Control Tower does not retroactively resolve the inheritance drift that was caused by moving accounts between OUs before the auto-enroll capability was enabled. The automatic drift resolution goes into effect for accounts that are moved after you enable this setting.
