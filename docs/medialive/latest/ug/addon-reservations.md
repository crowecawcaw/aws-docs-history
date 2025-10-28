# Add-on reservations

Reservations are available for those items in [the MediaLive price list](https://aws.amazon.com/medialive/pricing/ "https://aws.amazon.com/medialive/pricing/")
that
are considered to be add-ons, such as codec licenses.

An add-on reservation applies to the cost of the add-on for the entire
channel. The reservation reduces the cost of the add-on regardless of how
many times the add-on applies to the channel. For example, if three
outputs in the same channel both use an advanced audio codec, you need
only one reservation to reduce the cost of the add-on. You don't need
three reservations for this channel.

###### Topics

- [Reservation
  attributes](#addon-reservation-attributes "#addon-reservation-attributes")
- [How an add-on
  reservation is applied](#how-addon-reservation-applied "#how-addon-reservation-applied")

## Reservation

attributes

The add-on reservations have these attributes:

- Add-on
  (Advanced
  Audio or Audio
  Normalization)
- Region (in which the channel is running)

## How an add-on

reservation is applied

At the start of each monthly billing cycle, AWS replenishes each
add-on reservation with the pool of minutes for the month.

At the end of the cycle, AWS applies the minutes from a given
reservation to reduce the cost for channels that use the add-on. For
each minute in the month, it determines if one or more matching channels
were running. A channel matches the reservation if the add-on feature is
enabled.

AWS accumulates these running minutes within the hour, up to a
maximum of 60 minutes. After the reservation minutes are used up for the
hour, AWS charges the regular rate-per-minute for the remainder of
those channels for that hour.

### Add-ons are per

channel

A channel matches the reservation if the add-on feature is
enabled one or more times. Within one channel, the number of outputs
that use the add-on isn't relevant. The reservation is consumed only
once for the entire channel. For example, if there are two outputs
in one channel that enable audio normalization, only one reservation
is consumed.

### Running

minutes can be allocated over channels

The rule applies that applies to [input and output
reservations](input-output-reservations.md#how-inputoutput-reservation-applied "input-output-reservations.md#how-inputoutput-reservation-applied") also applies to add-ons, except that the item
is always a channel. For example, you start Channel A with two
outputs that match the Advanced Audio reservation. You have
purchased only one instance of this reservation. After 45 minutes,
you start Channel B that has one output that matches the same
reservation. After 15 more minutes, you stop Channel A. The running
minutes are accumulated as shown by the shading in the following
illustration.

![A graphic representation of 80 minutes with two channels, one channel running for 60 minutes and one channel running for 35 minutes. The second channel has a 15 minute overlap with the first channel. A bar runs across the top of the image and is divided into eight segments representing 10 minute blocks, totalling 80 minutes. Below the top bar, a block labelled channel is aligned underneath the first six 10 minute blocks, representing 60 minutes beginning at the start of the total 80 minute period. This first channel block is fully shaded, showing it fully matches the reservation. Below the first channel block is another block labelled channel. This block begins after the first 45 minutes represented by the 10 minute blocks. On the second channel block, only the final 20 minutes, of 35, are shaded. The shading that represents running minutes does not overlap between the two channel blocks.](images/reservations-addon-shared2channels.png)

Here is another example of how different channels can consume
the running minutes. Suppose that in one hour you run only channels
that match the Advanced Audio reservation. You have purchased only
one instance of this reservation. You run these four matching
outputs simultaneously for 15 minutes each. During that hour, you
don't run any other matching outputs. Those four outputs would all
contribute to the 60 minutes.

![A graphic representation of 60 minutes with four channels, each channel running for 15 minutes. A bar runs across the top of the image and is divided into six segments representing 10 minute blocks, totalling 60 minutes. Below the top bar, four block are labelled as channels. Each output block occupies 15 minutes of space. Each channel block starts at the first 10 minute block. All four channel blocks are fully shaded to represent the entire channel is considered running minutes.](images/reservations-addon-shared4channels.png)

### Licensing bursts are

not supported

The bursting rule that applies to [input and output
reservations](input-output-reservations.md#how-inputoutput-reservation-applied "input-output-reservations.md#how-inputoutput-reservation-applied") also applies to add-on reservations, except
that the item is always a channel. For example, in one hour you run
four channels that match the Advanced Audio reservation. You have
purchased only one instance of this reservation. You run these four
matching channels simultaneously for 60 minutes each. Only one of
these channels is eligible for the reservation because one channel
is enough to use up the 60 running minutes per hour.

![A graphic representation of 60 minutes with four channels, each channel running for 60 total minutes. A bar runs across the top of the image and is divided into six segments representing 10 minute blocks, totalling 60 minutes. Below the top bar, four block are labelled as channels. Each channel block occupies 60 minutes of space, running the entire length of the 60 minute bar. Only the first channel block is shaded, representing that only one of the four channels is consuming the 60 minutes of running minutes.](images/reservations-addon-bursts.png)

### Unused minutes

At the end of the cycle, if some or all of the minutes in the
add-on reservation are not used, those minutes are lost. Minutes are
not transferred to the next month.
