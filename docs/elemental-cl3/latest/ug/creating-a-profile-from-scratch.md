# Creating a profile from

scratch

###### Topics

- [Design the profile](#crud-profile-create-design "#crud-profile-create-design")
- [Create the profile](#crud-profile-create "#crud-profile-create")

## Design the profile

When you create an AWS Elemental Live profile, you must enter a value for every field that you want
to be useable by the channel.

A created profile will contain all the fields where you entered a value
(or a checkmark, for example) or where you set up a [profile
parameter](creating-a-profile-with-channel-parameters.md "creating-a-profile-with-channel-parameters.md"). All the other fields are deleted from the profile. The
following rules apply:

- You won't be able to add fields from the profile back in.
- You won't be able to delete fields that are in the profile.
- You won't be able to modify or specify a value for any fields, except
  in fields that have profile parameters.
- You won't be able to leave a profile parameter empty.

Therefore, you must plan the profile fields carefully:

- Some fields are required. You must either provide a value, or accept
  the default.

If you provide a value, it must be the permanent value, or you must
set it up as a profile parameter (if that's possible).

If you don't like the default, make sure that you change it, because
you won't be able to change it when you use the profile to create the
channel.

- Some fields are optional. If you want to include the field, you must
  either provide a value or set up the field as a profile parameter (if
  that's possible).
- Pay particular attention to the output groups section. Make sure that
  you include all the output groups, outputs within those groups, and
  streams (encodes) within all the outputs.

You won't be able to add or delete output groups, outputs, or
streams. Therefore, for example, make sure that you create all the audio
encodes that you need in a specific output. For example, if you know that
you will sometimes need two audio encodes and sometimes three audio
encodes, you must create two profiles.

## Create the profile

1.  On the AWS Elemental Conductor Live main menu, choose **Profiles**.
2.  On the **Profiles** page, choose **New
    Profile**. The **New Profile** page
    appears.
3.  Complete the profile. You can accept all the defaults, but you must
    at least complete the following:
    - **Name**: Enter a profile name.
    - **Restart on Failure**: Check to restart the
      channel automatically if it fails (recommended).
    - **Add Input**: Provide information for at least
      one video input: Specify the type , and the source location.

    Note the following:

        + If you do not want to specify the input source in the profile,
         you can specify a “channel parameter” as a placeholder that you
         replace with real information when you create the channel. See [Working with
         channel parameters in a profile](creating-a-profile-with-channel-parameters.md "creating-a-profile-with-channel-parameters.md").


        + If your input is an SDI Direct Input, see [Use case:
         Using SDI direct input in a profile and channel](using-sdi-direct-input-in-a-profile-and-channel.md "using-sdi-direct-input-in-a-profile-and-channel.md") for
         important information.
        + If your input is an SDI Router Input, see [Use case:
         Using SDI router input in a profile and channel](using-sdi-router-input-in-a-profile-and-channel.md "using-sdi-router-input-in-a-profile-and-channel.md") for
         important information.

    - **Output Group**: A channel must always contain at
      least one output group. Set up the output group with all its contents
      and features.
    - **Output** and **Stream**: A
      channel must always contain at least one output and one stream in each
      output group that you want to create. Each output must use one
      stream.

4.  Choose **Save** to save the profile. The profile
    appears in the list on the **Profiles** page.
