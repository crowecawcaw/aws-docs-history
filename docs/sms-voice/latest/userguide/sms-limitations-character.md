

# SMS character limits
<a name="sms-limitations-character"></a>

A single SMS message can contain up to 140 bytes of information. The number of characters you can include in a single SMS message depends on the type of characters the message contains.

If your message uses only characters in the GSM 03.38 character set, also known as the GSM 7-bit alphabet, it can contain up to 160 characters. If your message contains any characters that are outside of the GSM 03.38 character set, it can have up to 70 characters. When you send an SMS message, AWS End User Messaging SMS automatically determines the most efficient encoding to use.

When a message contains more than the maximum number of characters, the message is split into multiple parts. When messages are split into multiple parts, each part contains additional information about the message part that precedes it. When the recipient's device receives message parts that are separated in this way, it uses this additional information to confirm that all of the message parts are displayed in the correct order. Depending on the recipient's mobile carrier and device, multiple messages might be displayed as a single message, or as a sequence of separate messages. As a result, the number of characters in each message part is reduced to 153 for messages that only contain GSM 03.38 characters, or 67 for messages that contain other characters. You can estimate how many message parts your message contains before you send it by using SMS length calculator tools, several of which are available online. The maximum supported size of any message is 1530 GSM characters or 630 non-GSM characters. If the message size is greater than the supported size, the message will fail and AWS End User Messaging SMS will return an **Invalid Message Exception**. For more information about throughput and message size, see [What are the Message Parts per Second (MPS) limits](sms-limitations-mps.md).

AWS End User Messaging SMS does support all languages, however, depending on the recipient's mobile carrier and their regulations, certain symbols may be restricted on a case to case basis. When sending messages in languages that contain characters outside of the GSM 03.38 alphabet, the characters in each message part are reduced to 67.

**Important**  
When you send a message that contains more than one message parts, you're charged for the number of message parts contained in the message. For more information about throughput and message size, see [What are the Message Parts per Second (MPS) limits](sms-limitations-mps.md).

## GSM 03.38 character set
<a name="sms-limitations-characters-gsm-alphabet"></a>

The following table lists all of the characters that are present in the GSM 03.38 character set. If you send a message that includes only the characters shown in the following table, then the message can contain up to 160 characters. 


<table>
<thead>
  <tr><th colspan="13">GSM 03.38 standard characters</th></tr>
</thead>
<tbody>
  <tr><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td><td>H</td><td>I</td><td>J</td><td>K</td><td>L</td><td>M</td></tr>
  <tr><td>N</td><td>O</td><td>P</td><td>Q</td><td>R</td><td>S</td><td>T</td><td>U</td><td>V</td><td>W</td><td>X</td><td>Y</td><td>Z</td></tr>
  <tr><td>a</td><td>b</td><td>c</td><td>d</td><td>e</td><td>f</td><td>g</td><td>h</td><td>i</td><td>j</td><td>k</td><td>l</td><td>m</td></tr>
  <tr><td>n</td><td>o</td><td>p</td><td>q</td><td>r</td><td>s</td><td>t</td><td>u</td><td>v</td><td>w</td><td>x</td><td>y</td><td>z</td></tr>
  <tr><td>à</td><td>Å</td><td>å</td><td>Ä</td><td>ä</td><td>Ç</td><td>É</td><td>é</td><td>è</td><td>ì</td><td>Ñ</td><td>ñ</td><td>ò</td></tr>
  <tr><td>Ø</td><td>ø</td><td>Ö</td><td>ö</td><td>ù</td><td>Ü</td><td>ü</td><td>Æ</td><td>æ</td><td>ß</td><td>0</td><td>1</td><td>2</td></tr>
  <tr><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>&amp;</td><td>*</td><td>@</td><td>:</td><td>,</td><td>¤</td></tr>
  <tr><td>$</td><td>=</td><td>!</td><td>&gt;</td><td>#</td><td>-</td><td>¡</td><td>¿</td><td>(</td><td>&lt;</td><td>%</td><td>.</td><td>+</td></tr>
  <tr><td>£</td><td>?</td><td>"</td><td>)</td><td>§</td><td>;</td><td>'</td><td>/</td><td>_</td><td>¥</td><td>Δ</td><td>Φ</td><td>Γ</td></tr>
  <tr><td>Λ</td><td>Ω</td><td>Π</td><td>Ψ</td><td>Σ</td><td>Θ</td><td>Ξ</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
</tbody>
</table>


The GSM 03.38 character set includes several symbols in addition to those shown in the preceding table. However, each of these characters is counted as two characters because it also includes an invisible escape character:
+ ^
+ {
+ }
+ \\
+ [
+ ]
+ \~
+ \|
+ €

Finally, the GSM 03.38 character set also includes the following nonprinted characters:
+ A space character.
+ A line feed control, which signifies the end of one line of text and the beginning of another.
+ A carriage return control, which moves to the beginning of a line of text (usually following a line feed character).
+ An escape control, which is automatically added to the characters in the preceding list.

## Example messages
<a name="sms-limitations-characters-example-messages"></a>

This section contains several example SMS messages. For each example, this section shows the total number of characters, and the number of message parts for the message.

**Example 1: A long message that only contains characters in the GSM 03.38 alphabet**  
The following message contains only characters that are in the GSM 03.38 alphabet.

`Hello Carlos. Your Example Corp. bill of $100 is now available. Autopay is scheduled for next Thursday, April 9. To view the details of your bill, go to https://example.com/bill1.`

The preceding message contains 180 characters, so it has to be split into multiple message parts. When a message is split into multiple message parts, each part can contain 153 GSM 03.38 characters. As a result, this message is sent as two message parts.

**Example 2: A message that contains multi-byte characters**  
The following message contains several Chinese characters, all of which are outside of the GSM 03.38 alphabet. 

`亚马逊公司是一家总部位于美国西雅图的跨国电子商务企业，业务起始于线上书店，不久之后商品走向多元化。杰夫·贝佐斯于1994年7月创建了这家公司。`

The preceding message contains 71 characters. However, because almost all of the characters in the message are outside of the GSM 03.38 alphabet, it's sent as two message parts. Each of these message parts can contain a maximum of 67 characters.

**Example 3: A message that contains a single non-GSM character**  
The following message contains a single character that isn't part of the GSM 03.38 alphabet. In this example, the character is a closing single quote (’), which is a different character from a regular apostrophe ('). Word processing applications, such as Microsoft Word, often automatically replace apostrophes with closing single quotes. If you draft your SMS messages in Microsoft Word and paste them into AWS End User Messaging SMS, remove these special characters and replace them with apostrophes.

`John: Your appointment with Dr. Salazar’s office is scheduled for next Thursday at 4:30pm. Reply YES to confirm, NO to reschedule.`

The preceding message contains 130 characters. However, because it contains the closing single quote character, which isn't part of the GSM 03.38 alphabet, it's sent as two message parts.

If you replace the closing single quote character in this message with an apostrophe, which is part of the GSM 03.38 alphabet, then the message is sent as a single message part.