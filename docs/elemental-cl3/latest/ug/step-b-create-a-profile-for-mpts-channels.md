# Creating a

profile for an SPTS channel

An SPTS channel is a channel that you plan to use in an MPTS that you will run on
AWS Elemental Statmux.

A profile for an SPTS channel must include a UDP/TS output group that
has one output that is set up for statmux. The UDP/TS output group can also
include non-statmux outputs. The profile itself can include other types of
output groups.

1. On the AWS Elemental Conductor Live main menu, choose **Profiles**. On the
   **Profiles** page, choose **New Profile** (on the top right
   corner of the page).
2. Create the profile in the usual way for everything except the UDP/TS
   output group.
3. To set up the UDP/TS output group, scroll down to **Output
   Groups** and choose the **UDP/TS** tab.
4. In the **New Output** section, choose the
   **Add Output** button.
5. For **MPTS membership**, choose
   **Remote**. This output section changes to display
   different fields. Complete the fields as follows:
   - Note that the destination fields are removed because you set the
     destination in the MPTS, not in the channel profile.
   - Note that the **PAT** and **PMT**
     fields are enabled because Elemental Statmux always creates these tables. You can
     set the interval to specify how often each table is inserted in the
     transport stream.
   - Set the **NIT** and **TDT** fields
     if you want to create these tables for this program.
   - Set the **SDT** fields to specify how you want
     Elemental Statmux to handle the program in this table. There is an option to not
     include this program in the SDT.

6. In the **Streams** section, in the
   **Video** section, choose **Advanced**
   to display more fields. Set the following field:

**Rate Control Mode**: Set to
**Statmux**. This value indicates that the muxer will
control the rate control for the output.

Note that when you set this value, the **Bitrate**,
**Max Bitrate**, and **Min Bitrate**
fields don't apply, so these fields become disabled. 7. Choose **Save**.
The profile that you created is listed on the
**Profiles** page:

- Conductor Live assigns a unique numerical ID to the profile.
- Under the **Channels** column, the profile displays
  **0 0**. This indicates that the profile is not yet being
  used by any channels.
