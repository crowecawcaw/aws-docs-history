

# Using the meeting roster
<a name="attendees-panel"></a>

The meeting roster appears in the **Attendees** panel during a meeting. The roster lists everyone on the meeting invitation, including anyone added during the meeting. You can use the panel to take several actions, such as adding or searching for attendees, or sending messages directly to a specific attendee.

**Topics**
+ [About meeting roster sections](#roster-sections)
+ [About the icons in the roster](#attendee-icons)
+ [Opening or closing the Attendees panel](#open-close-attendees)
+ [Adding an attendee](#add-attendee-panel)
+ [Searching for attendees](#search-attendees)
+ [Using the Waiting Room](#use-wr)
+ [Messaging attendees directly](#message-direct)
+ [Muting attendees](#mute-attendees)

## About meeting roster sections
<a name="roster-sections"></a>

The meeting roster groups attendees into several sections. The sections you see during a meeting vary based on an attendee's status. An attendee can have one of the following statuses:

**Note**  
You can open or close the sections in the meeting roster by choosing the caret (**^**) next to the section name.

**Speaker**  
Displays the name of the person currently speaking.

**Waiting Room**  
Displays a list of anonymous attendees, meaning attendees who don't have Amazon Chime accounts, or who have accounts but don't sign in with their account credentials. For more information about the waiting room, see [Using the Waiting Room](waiting-room.md).

**Guests**  
Lists the attendees who don't have Amazon Chime accounts, who join without signing in, who dial in to the meeting, or who use the CallMe feature.  
Attendees must belong to the same Amazon Chime account as the host in order to appear as guests.

**Present**  
Lists the authenticated users who join the meeting. By default, the roster displays attendees signed in to their Amazon Chime account by the name listed on their account.   
Names appear in angle brackets (for example, **<Mary Major>**) when:   
+ An attendee enters a different name from the one on their Amazon Chime account when they join the meeting.
+ An attendee joins a meeting without signing in to their Amazon Chime account.
+ An attendee without an Amazon Chime account joins a meeting.
Attendees who dial in appear as phone numbers surrounded by angle brackets, such as **<2075551212>**.

**Invited**  
Lists the attendees invited to the meeting but who aren't **Present** yet.

**Running late**  
Lists the attendees who mark themselves as late, along with an estimated time until they join the meeting.

**Left**  
Lists the attendees who leave the meeting.

**Dropped**  
Lists the attendees who were disconnected due to a network connection problem.

## About the icons in the roster
<a name="attendee-icons"></a>

The roster displays icons next to each attendee's name to indicate certain statuses about that attendee. These icons can change throughout the meeting, depending on actions attendees take. For example, when someone shares a window or screen, the screen share icon appears next to the attendee's name. If another attendee takes over the screen share, the icon appears next to that attendee's name.

The following table lists and describes the icons.


| Icon | Status | 
| --- | --- | 
| ![An icon of a crown.](http://docs.aws.amazon.com/chime/latest/ug/images/icon-mtg-organizer.png)  | Indicates the meeting organizer. | 
| ![A line drawing of a video camera.](http://docs.aws.amazon.com/chime/latest/ug/images/icon-video-on.png)  | The attendee's camera is on. | 
| ![A line drawing of a blue microphone.](http://docs.aws.amazon.com/chime/latest/ug/images/icon-audio-on.png) | The attendee's microphone is on. The inside of the microphone icon displays the audio level as that attendee talks. | 
| ![A line drawing of a gray microphone with a diagonal slash.](http://docs.aws.amazon.com/chime/latest/ug/images/icon-audio-muted.png) | The attendee's microphone is muted. Changes to a ![Line drawing of a blue microphone.](http://docs.aws.amazon.com/chime/latest/ug/images/icon-audio-on.png) when the attendee unmutes their microphone.  | 
| ![A console style phone.](http://docs.aws.amazon.com/chime/latest/ug/images/icon-dial-in.png) | Indicates that the attendee dialed in from a phone. | 
| ![A line drawing of a computer screen.](http://docs.aws.amazon.com/chime/latest/ug/images/icon-screen-share.png) | Indicates the attendee currently sharing their screen. | 

## Opening or closing the Attendees panel
<a name="open-close-attendees"></a>

You can open or close the **Attendees** panel at any time during a meeting. Closing the panel hides the meeting roster.

**To open or close the panel**
+ Choose the **Attendee panel** icon (![Icon of two figures surrounded by a blue circle.](http://docs.aws.amazon.com/chime/latest/ug/images/left-control-2.png)).

  —OR—

  Choose the **Close attendees panel** icon (![Icon of an X inside a square box.](http://docs.aws.amazon.com/chime/latest/ug/images/attendees-close-icon.png) ) to close the panel.

## Adding an attendee
<a name="add-attendee-panel"></a>

You can add an attendee at any time during a meeting. However, the attendee must belong to your list of contacts. They must also accept your invitation. For more information about contacts, see [Add contacts](contacts.md) in the *Getting started* section of this guide.

**To add an attendee**

1. Choose the **Add attendee** icon at the top of the panel ( ![An icon showing a plus sign surrounded by a square.](http://docs.aws.amazon.com/chime/latest/ug/images/attendees-add-icon.png)), or press  Ctrl N .

1. In the **Add attendees** dialog box, enter and select the name of the attendee you want to add. Then, choose **Add**.

## Searching for attendees
<a name="search-attendees"></a>

You can search for specific attendees during a meeting. When you search for an attendee, you can view their contact information or send them a direct message.

**To search for an attendee**
+ Choose the **Search attendees** icon at the top of the **Attendees** panel (![Icon of a magnifying glass.](http://docs.aws.amazon.com/chime/latest/ug/images/attendees-search-icon.png)).

## Using the Waiting Room
<a name="use-wr"></a>

The Waiting Room appears in the **Attendee** panel whenever an anonymous user tries to join a meeting. You can admit anonymous users to the meeting. For more information, see [Using the Waiting Room](waiting-room.md).

![Image of the Turn off Waiting Room link.](http://docs.aws.amazon.com/chime/latest/ug/images/turn-off-wr-from-attendee-panel.png)


## Messaging attendees directly
<a name="message-direct"></a>

When you use in-meeting chat, everyone in the meeting sees your message. If you want to communicate with a specific attendee, use regular Chime chat to message them directly.

**To message directly**
+ Open the horizontal ellipsis menu next to the attendee that you want to message, and then choose **Message directly**.

## Muting attendees
<a name="mute-attendees"></a>

If needed, you can mute an attendee's microphone.

**To mute an attendee**
+ Open the horizontal ellipsis menu next to the attendee that you want to mute, and then choose **Mute**. To unmute the attendee, open the menu and choose **Unmute**.