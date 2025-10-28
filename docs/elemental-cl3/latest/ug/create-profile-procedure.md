# The procedure

Follow this procedure to set up a blue field with a channel parameter.
This procedure assumes that you know how to create a [profile](creating-a-profile-from-scratch.md "creating-a-profile-from-scratch.md") and a [channel](creating-a-channel.md "creating-a-channel.md").

1. Position your cursor in a blue field. The
   **Parameters** panel opens on the page.
2. For the value of the field, enter a name for the parameter in double
   curly brackets:

`{{my_parameter}}`

You can set up the field as a mixture of hardcoded value and
parameter value. For example:

`udp://10.20.110.106:{{port}}`

In the above example, you've created a parameter called
`port`. 3. As
soon as you enter a correctly formatted name, the
parameter appears in the **Parameters** panel. 4. In the **Parameters** panel, enter a validation
value for the parameter. The validation value is a sample value that is
correctly formatted.

When you create a channel using this profile, you will enter a real
value for

For example, assume that the field always takes a URI and that the
protocol must be RTP or UDP. A sample value could look like any of the
following:

`rtp://hostname.com:1234`

`rtp://1.2.3.4.com:1234`

`udp://hostname.com:1234`

Note the following about these sample validation values:

    * `rtp://` is a real value and is correctly
     formatted.
    * `hostname.com` is not a real value, but it is
     correctly formatted.
    * `1234` is not a real value, but it is
     correctly formatted.

5. When you save the profile, Elemental Live verifies that the validation value
   you've entered is valid.
