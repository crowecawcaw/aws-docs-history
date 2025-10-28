# Rules for ingesting

MPEG-TS programs

For video, each AWS Elemental Live event can extract only one video from
only one program. Elemental Live will not reject MPTS inputs, but it will
handle only one program. There are fields in the event that specify which
video to extract.

For audio, each Elemental Live event can extract audio that is in the
same program as the video. It can extract more than one audio from that
program. It cannot extract audio from another program. There are fields in
the event that specify which audio to extract.
