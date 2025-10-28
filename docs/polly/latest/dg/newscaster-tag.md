# Newscaster speaking style

_<amazon:domain name="news">_

The newscaster style is available only for the Matthew or
Joanna voices, which are available only in American English
(en-US), Lupe, in US Spanish (es-US) and Amy, in British English
(en-GB). It is only supported when using `Neural`
format.

To use the newscaster style, you use SSML tags and the
following syntax::

```
<amazon:domain name="news">`text`</amazon:domain>
```

For example, you might use the newscaster style with the Amy
voice as follows:

```
<speak>
<amazon:domain name="news">
From the Tuesday, April 16th, 1912 edition of The Guardian newspaper:

The maiden voyage of the White Star liner Titanic, the largest ship ever launched, has ended in disaster.

The Titanic started her trip from Southampton for New York on Wednesday. Late on Sunday night she struck
an iceberg off the Grand Banks of Newfoundland. By wireless telegraphy she sent out signals of distress,
and several liners were near enough to catch and respond to the call.
</amazon:domain>
</speak>
```
