# Modifying a profile

You can't modify a AWS Elemental Conductor Live profile after it has been created. This rule ensures the
dependability of profiles: a channel that uses profile_A and that was run two weeks ago has the
same profile data as a channel that uses profile_A that was run yesterday.

If you want to modify a profile so that you do not have to recreate it from scratch, take
the following steps.

###### To modify a profile

1. Duplicate the profile. Change values as desired and then save the
   profile.
2. Take the appropriate action:
   - If you duplicated the profile in order to fix errors in a profile you only just
     created, delete the incorrect profile.
   - If you duplicated a profile that is being used by one or more channels, remember to
     associate the channels with the new profile. Then delete the unused profile.
     - To change the association for only one channel, see [Modifying a channel](modifying-a-channel.md "modifying-a-channel.md").
     - To change the association for several channels that use this profile, see [Changing the profile used by
       multiple channels](changing-the-profile-used-by-multiple-channels.md "changing-the-profile-used-by-multiple-channels.md").
