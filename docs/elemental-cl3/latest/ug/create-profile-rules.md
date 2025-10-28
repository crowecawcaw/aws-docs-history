# Rules for channel parameters

There are two rules associated with channel parameters in the
profile:

- Generally, if a field is blue on the profile, setting up as a channel
  parameter is optional. On the profile, you could also enter a permanent
  value or no value.

There are two exceptions to this rule: the SDI Direct Input field and
the SDI Router Input field must be set up as channel parameters. See [Use case:
Using SDI direct input in a profile and channel](using-sdi-direct-input-in-a-profile-and-channel.md "using-sdi-direct-input-in-a-profile-and-channel.md") and [Use case:
Using SDI router input in a profile and channel](using-sdi-router-input-in-a-profile-and-channel.md "using-sdi-router-input-in-a-profile-and-channel.md").

- You shouldn't set up non-blue fields with a parameter. If you try to
  do so, you receive an error when you save the profile.

###### Warning

It is possible to create profiles with parameters in fields that
aren't blue. But doing so can cause problems when you create channels from
these profiles or when you import profiles after upgrades.
