

# Supported countries and regions for SMS messaging with AWS End User Messaging SMS
<a name="phone-numbers-sms-by-country"></a>

You can use AWS End User Messaging SMS to send SMS messages to the countries, regions, and territories listed in the following table. This table also lists the countries and regions that support Sender IDs and two-way SMS messaging.

If you are unsure of which origination identity will work best for you then see [Choosing an origination identity](phone-number-types.md) for each origination types advantages and disadvantages. Depending on your use case you can also use [General considerations for choosing an origination identity](phone-number-types.md#phone-number-types-choosing-general), [Choosing an origination identity for one-way messaging use cases](phone-number-types.md#phone-number-types-choosing-oneway) and [Choosing an origination identity for two-way messaging use cases](phone-number-types.md#phone-number-types-choosing-twoway) to help choose the correct origination identity for your use case. 

**Note**  
**Important:** Phone numbers for SMS delivery are provisioned through a single carrier partner in each region/country. This creates a single point of failure if that partner experiences issues. For business-critical messaging, we recommend implementing redundant communication channels such as:  
[WhatsApp](https://aws.amazon.com/end-user-messaging/whatsapp/), [Push notifications](https://aws.amazon.com/end-user-messaging/push/), and [outbound voice calls](https://docs.aws.amazon.com/sms-voice/latest/userguide/what-is-sms-mms.html) via AWS End User Messaging.
[Email notifications](https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity-using-notifications.html) via Amazon Simple Email Service (SES).
For countries that support both dedicated numbers and sender IDs, you can fallback to one option if the other experiences issues.
Using [phone pools](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-pool.html) in End User Messaging Service allows you to quickly add or remove problematic originators from your sending pools, helping maintain message delivery reliability.
This multi-channel approach helps ensure message delivery even if one channel experiences disruption.

For the rules of which sender ID is displayed when you send SMS messages to countries where Sender IDs are supported, compared to those where Sender IDs aren't supported, see [Sender ID display name rules](sender-id.md#channels-sms-countries-sender-id).

Before you can use two-way SMS messaging to receive messages, you have to obtain either a dedicated short code or a dedicated long code. 

**Note**  
You can purchase long codes for some countries directly through the AWS End User Messaging SMS console. The long codes that you purchase through the console are intended for use with the voice channel. However, if you purchase a long code that is based in the United States (including Puerto Rico) or Canada, you can also use it to send SMS messages.



<table>
<thead>
  <tr><th>Country or region</th><th>ISO code</th><th>Dialing code</th><th>Supports short codes</th><th>Supports long codes</th><th>Supports Sender IDs</th><th>Supports two-way SMS</th><th>International sending<a href="#sms-support-note-10">10</a></th></tr>
</thead>
<tbody>
  <tr><td colspan="8"> <b>A</b></td></tr>
  <tr><td>Afghanistan</td><td>AF</td><td>93</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Albania</td><td>AL</td><td>355</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Algeria</td><td>DZ</td><td>213</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Andorra</td><td>AD</td><td>376</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>No</td></tr>
  <tr><td>Angola</td><td>AO</td><td>244</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Anguilla</td><td>AI</td><td>1-264</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Antigua and Barbuda</td><td>AG</td><td>1-268</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Argentina </td><td>AR</td><td>54</td><td>Yes</td><td>No</td><td>No </td><td>No</td><td>Yes</td></tr>
  <tr><td>Armenia</td><td>AM</td><td>374</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Aruba</td><td>AW</td><td>297</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>No</td></tr>
  <tr><td>Australia</td><td>AU</td><td>61</td><td>No</td><td>Yes</td><td>Registration required<a href="#sms-support-note-8">8</a></td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Austria</td><td>AT</td><td>43</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Azerbaijan</td><td>AZ</td><td>994</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td colspan="8"> <b>B</b></td></tr>
  <tr><td>Bahamas</td><td>BS</td><td>1-242</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td></tr>
  <tr><td>Bahrain</td><td>BH</td><td>973</td><td>No</td><td>No </td><td>Yes </td><td>No</td><td>Yes</td></tr>
  <tr><td>Bangladesh</td><td>BD</td><td>880</td><td>No</td><td>No </td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Barbados</td><td>BB</td><td>1-246</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Belarus</td><td>BY</td><td>375</td><td>No</td><td>No</td><td>Registration required<a href="#sms-support-note-8">8</a></td><td>No</td><td>Yes</td></tr>
  <tr><td>Belgium</td><td>BE</td><td>32</td><td>Yes</td><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Belize</td><td>BZ</td><td>501</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Bermuda</td><td>BM</td><td>1-441</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Bhutan</td><td>BT</td><td>975</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Bolivia</td><td>BO</td><td>591</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Bosnia and Herzegovina</td><td>BA</td><td>387</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Botswana</td><td>BW</td><td>267</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Brazil</td><td>BR</td><td>55</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Brunei</td><td>BN</td><td>673</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Bulgaria</td><td>BG</td><td>359</td><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Burkina Faso</td><td>BF</td><td>226</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Burundi</td><td>BI</td><td>257</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td colspan="8"> <b>C</b></td></tr>
  <tr><td>Cambodia</td><td>KH</td><td>855</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Cameroon</td><td>CM</td><td>237</td><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Canada</td><td>CA</td><td>1</td><td>Yes</td><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Cape Verde</td><td>CV</td><td>238</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Cayman Islands</td><td>KY</td><td>1-345</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Central African Republic</td><td>CF</td><td>236</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Chad</td><td>TD</td><td>235</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>No</td></tr>
  <tr><td>Chile</td><td>CL</td><td>56</td><td>Yes</td><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>China</td><td>CN</td><td>86</td><td>Yes</td><td>No</td><td>No <a href="#sms-support-note-2">2</a> </td><td>Yes</td><td>No</td></tr>
  <tr><td>Colombia</td><td>CO</td><td>57</td><td>Yes</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Comoros</td><td>KM</td><td>269</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Cook Islands</td><td>CK</td><td>682</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Costa Rica</td><td>CR</td><td>506</td><td>Yes</td><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Croatia</td><td>HR</td><td>385</td><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Cyprus</td><td>CY</td><td>357</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Czechia (Czech Republic)</td><td>CZ</td><td>420</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td colspan="8"> <b>D</b></td></tr>
  <tr><td>Democratic Republic of the Congo</td><td>CD</td><td>243</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Denmark</td><td>DK</td><td>45</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Djibouti</td><td>DJ</td><td>253</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Dominica</td><td>DM</td><td>1-767</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Dominican Republic</td><td>DO</td><td>1-809, 1-829, 1-849</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td></tr>
  <tr><td colspan="8"> <b>E</b></td></tr>
  <tr><td>Ecuador</td><td>EC</td><td>593</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Egypt</td><td>EG</td><td>20</td><td>Yes</td><td>No</td><td>Registration required<a href="#sms-support-note-8">8</a></td><td>Yes</td><td>Yes</td></tr>
  <tr><td>El Salvador</td><td>SV</td><td>503</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Equatorial Guinea</td><td>GQ</td><td>240</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>No</td></tr>
  <tr><td>Eritrea</td><td>ER</td><td>291</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Estonia</td><td>EE</td><td>372</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Eswatini</td><td>SZ</td><td>268</td><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td><td>No</td></tr>
  <tr><td>Ethiopia</td><td>ET</td><td>251</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>No</td></tr>
  <tr><td colspan="8"> <b>F</b></td></tr>
  <tr><td>Faroe Islands</td><td>FO</td><td>298</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Fiji</td><td>FJ</td><td>679</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Finland</td><td>FI</td><td>358</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>France</td><td>FR</td><td>33</td><td>Yes</td><td>No</td><td>Yes<a href="#sms-support-note-11">11</a></td><td>Yes</td><td>Yes</td></tr>
  <tr><td>French Guiana</td><td>GF</td><td>594</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>French Polynesia</td><td>PF</td><td>689</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>No</td></tr>
  <tr><td colspan="8"> <b>G</b></td></tr>
  <tr><td>Gabon</td><td>GA</td><td>241</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Gambia</td><td>GM</td><td>220</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Georgia</td><td>GE</td><td>995</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Germany</td><td>DE</td><td>49</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Ghana</td><td>GH</td><td>233</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Gibraltar</td><td>GI</td><td>350</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>No</td></tr>
  <tr><td>Greece</td><td>GR</td><td>30</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td><td>No</td></tr>
  <tr><td>Greenland</td><td>GL</td><td>299</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Grenada</td><td>GD</td><td>1-473</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Guadeloupe</td><td>GP</td><td>590</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Guam</td><td>GU</td><td>1-671</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Guatemala</td><td>GT</td><td>502</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Guernsey</td><td>GG</td><td>44-1481</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>No</td></tr>
  <tr><td>Guinea</td><td>GN</td><td>224</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Guinea-Bissau</td><td>GW</td><td>245</td><td>No</td><td>No</td><td>Yes</td><td>N/A</td><td>No</td></tr>
  <tr><td>Guyana</td><td>GY</td><td>592</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td colspan="8"> <b>H</b></td></tr>
  <tr><td>Haiti</td><td>HT</td><td>509</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Honduras</td><td>HN</td><td>504</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Hong Kong</td><td>HK</td><td>852</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Hungary</td><td>HU</td><td>36</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td></tr>
  <tr><td colspan="8"> <b>I</b></td></tr>
  <tr><td>Iceland</td><td>IS</td><td>354</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>India</td><td>IN</td><td>91</td><td>Yes</td><td>Yes<a href="#sms-support-note-4">4</a></td><td>Registration required<a href="#sms-support-note-3">3</a> </td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Indonesia</td><td>ID</td><td>62</td><td>No</td><td>No</td><td>Registration required<a href="#sms-support-note-8">8</a></td><td>No</td><td>Yes</td></tr>
  <tr><td>Iraq</td><td>IQ</td><td>964</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Ireland</td><td>IE</td><td>353</td><td>No</td><td>Yes</td><td>Registration required<a href="#sms-support-note-9">9</a></td><td>Yes</td><td>No</td></tr>
  <tr><td>Isle of Man</td><td>IM</td><td>44-1624</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>No</td></tr>
  <tr><td>Israel</td><td>IL</td><td>972</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Italy</td><td>IT</td><td>39</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Ivory Coast</td><td>CI</td><td>225</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td colspan="8"> <b>J</b></td></tr>
  <tr><td>Jamaica</td><td>JM</td><td>1-876</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Japan</td><td>JP</td><td>81</td><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Jersey</td><td>JE</td><td>44-1434</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td><td>No</td></tr>
  <tr><td>Jordan</td><td>JO</td><td>962</td><td>No</td><td>No</td><td>Registration required<a href="#sms-support-note-8">8</a></td><td>No</td><td>Yes</td></tr>
  <tr><td colspan="8"> <b>K</b></td></tr>
  <tr><td>Kazakhstan</td><td>KZ</td><td>7</td><td>No</td><td>No</td><td>Registration required<a href="#sms-support-note-8">8</a></td><td>No</td><td>Yes</td></tr>
  <tr><td>Kenya</td><td>KE</td><td>254</td><td>Yes</td><td>Yes</td><td>Registration required<a href="#sms-support-note-8">8</a></td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Kosovo</td><td>XK</td><td>383</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>No</td></tr>
  <tr><td>Kuwait</td><td>KW</td><td>965</td><td>No</td><td>Yes</td><td>Registration required<a href="#sms-support-note-8">8</a></td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Kyrgyzstan</td><td>KG</td><td>996</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td colspan="8"><b>L</b></td></tr>
  <tr><td>Laos</td><td>LA</td><td>856</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Latvia</td><td>LV</td><td>371</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Lebanon</td><td>LB</td><td>961</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Lesotho</td><td>LS</td><td>266</td><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Liberia</td><td>LR</td><td>231</td><td>No</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Libya</td><td>LY</td><td>218</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Liechtenstein</td><td>LI</td><td>423</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Lithuania</td><td>LT</td><td>370</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Luxembourg</td><td>LU</td><td>352</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td colspan="8"><b>M</b></td></tr>
  <tr><td>Macau</td><td>MO</td><td>853</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Macedonia</td><td>MK</td><td>389</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Madagascar</td><td>MG</td><td>261</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Malawi</td><td>MW</td><td>265</td><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Malaysia</td><td>MY</td><td>60</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Maldives</td><td>MV</td><td>960</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Mali</td><td>ML</td><td>223</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Malta</td><td>MT</td><td>356</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Marshall Islands, The</td><td>MH</td><td>692</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td></tr>
  <tr><td>Martinique</td><td>MQ</td><td>596</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>No</td></tr>
  <tr><td>Mauritania</td><td>MR</td><td>222</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Mauritius</td><td>MU</td><td>230</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Mayotte</td><td>YT</td><td>262</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>No</td></tr>
  <tr><td>Mexico</td><td>MX</td><td>52</td><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Micronesia (Federated States of)</td><td>FM</td><td>691</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td></tr>
  <tr><td>Moldova</td><td>MD</td><td>373</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Monaco</td><td>MC</td><td>377</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Mongolia</td><td>MN</td><td>976</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Montenegro</td><td>ME</td><td>382</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Montserrat</td><td>MS</td><td>1-664</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>No</td></tr>
  <tr><td>Morocco</td><td>MA</td><td>212</td><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Mozambique</td><td>MZ</td><td>258</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Myanmar</td><td>MM</td><td>95</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td colspan="8"><b>N</b></td></tr>
  <tr><td>Namibia</td><td>NA</td><td>264</td><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Nepal</td><td>NP</td><td>977</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>No</td></tr>
  <tr><td>Netherlands</td><td>NL</td><td>31</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>New Caledonia</td><td>NC</td><td>687</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>New Zealand<a href="#sms-support-note-6">6</a></td><td>NZ</td><td>64</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Nicaragua</td><td>NI</td><td>505</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Niger</td><td>NE</td><td>227</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Nigeria</td><td>NG</td><td>234</td><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Niue</td><td>NU</td><td>683</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Norfolk Island</td><td>NF</td><td>672</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>No</td></tr>
  <tr><td>Norway</td><td>NO</td><td>47</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td colspan="8"><b>O</b></td></tr>
  <tr><td>Oman</td><td>OM</td><td>968</td><td>No</td><td>No</td><td>Registration required<a href="#sms-support-note-8">8</a></td><td>No</td><td>Yes</td></tr>
  <tr><td colspan="8"><b>P</b></td></tr>
  <tr><td>Pakistan</td><td>PK</td><td>92</td><td>No</td><td>Yes<a href="#sms-support-note-4">4</a></td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Palestine</td><td>PS</td><td>970</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Panama</td><td>PA</td><td>507</td><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Palau</td><td>PW</td><td>680</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>No</td></tr>
  <tr><td>Papua New Guinea</td><td>PG</td><td>675</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Paraguay</td><td>PY</td><td>595</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Peru</td><td>PE</td><td>51</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Philippines</td><td>PH</td><td>63</td><td>No</td><td>Yes<a href="#sms-support-note-4">4</a></td><td>Registration required<a href="#sms-support-note-8">8</a></td><td>No</td><td>Yes</td></tr>
  <tr><td>Poland</td><td>PL</td><td>48</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Portugal</td><td>PT</td><td>351</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Puerto Rico</td><td>PR</td><td>1-787, 1-939</td><td>Yes</td><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td></tr>
  <tr><td colspan="8"><b>Q</b></td></tr>
  <tr><td>Qatar</td><td>QA</td><td>974</td><td>Yes</td><td>No</td><td>Registration required<a href="#sms-support-note-8">8</a></td><td>Yes</td><td>Yes</td></tr>
  <tr><td colspan="8"><b>R</b></td></tr>
  <tr><td>Republic of the Congo</td><td>CG</td><td>242</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td></tr>
  <tr><td>Réunion (France)</td><td>RE</td><td>262</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Romania</td><td>RO</td><td>40</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Russia</td><td>RU</td><td>7</td><td>Yes</td><td>No</td><td>Registration required<a href="#sms-support-note-8">8</a></td><td>Yes</td><td>No</td></tr>
  <tr><td>Rwanda</td><td>RW</td><td>250</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td colspan="8"><b>S</b></td></tr>
  <tr><td>Saint Kitts and Nevis</td><td>KN</td><td>1-869</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td></tr>
  <tr><td>Saint Lucia</td><td>LC</td><td>1-758</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Samoa</td><td>WS</td><td>685</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>No</td></tr>
  <tr><td>San Marino</td><td>SM</td><td>378</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>No</td></tr>
  <tr><td>São Tomé and Príncipe</td><td>ST</td><td>239</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>No</td></tr>
  <tr><td>Saudi Arabia</td><td>SA</td><td>966</td><td>No</td><td>Yes<a href="#sms-support-note-4">4</a></td><td>Registration required<a href="#sms-support-note-8">8</a></td><td>No</td><td>No</td></tr>
  <tr><td>Senegal</td><td>SN</td><td>221</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>No</td></tr>
  <tr><td>Serbia</td><td>RS</td><td>381</td><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Seychelles</td><td>SC</td><td>248</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Sierra Leone</td><td>SL</td><td>232</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Singapore</td><td>SG</td><td>65</td><td>Yes</td><td>Yes</td><td>Yes<a href="#sms-support-note-5">5</a></td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Slovakia</td><td>SK</td><td>421</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Slovenia</td><td>SI</td><td>386</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Solomon Islands</td><td>SB</td><td>677</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Somalia</td><td>SO</td><td>252</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>South Africa</td><td>ZA</td><td>27</td><td>Yes</td><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>South Korea</td><td>KR</td><td>82</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>South Sudan</td><td>SS</td><td>211</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>No</td></tr>
  <tr><td>Spain</td><td>ES</td><td>34</td><td>Yes</td><td>Yes</td><td>Registration required<a href="#sms-support-note-8">8</a></td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Sri Lanka</td><td>LK</td><td>94</td><td>Yes</td><td>Yes</td><td>Registration required<a href="#sms-support-note-8">8</a></td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Suriname</td><td>SR</td><td>597</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Sweden</td><td>SE</td><td>46</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Switzerland</td><td>CH</td><td>41</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td colspan="8"><b>T</b></td></tr>
  <tr><td>Taiwan</td><td>TW</td><td>886</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Tajikistan</td><td>TJ</td><td>992</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Tanzania</td><td>TZ</td><td>255</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td><td>No</td></tr>
  <tr><td>Thailand</td><td>TH</td><td>66</td><td>No</td><td>Yes</td><td>Registration required<a href="#sms-support-note-8">8</a></td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Timor-Leste</td><td>TL</td><td>670</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Togo</td><td>TG</td><td>228</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>No</td></tr>
  <tr><td>Tonga</td><td>TO</td><td>676</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>No</td></tr>
  <tr><td>Trinidad and Tobago</td><td>TT</td><td>1-868</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Tunisia</td><td>TN</td><td>216</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Turkey</td><td>TR</td><td>90</td><td>No</td><td>No</td><td>Registration required<a href="#sms-support-note-8">8</a></td><td>No</td><td>Yes</td></tr>
  <tr><td>Turkmenistan</td><td>TM</td><td>993</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Turks and Caicos Islands</td><td>TC</td><td>1-649</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Tuvalu</td><td>TV</td><td>688</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>No</td></tr>
  <tr><td colspan="8"><b>U</b></td></tr>
  <tr><td>Uganda</td><td>UG</td><td>256</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td>Ukraine</td><td>UA</td><td>380</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>United Arab Emirates (UAE)</td><td>AE</td><td>971</td><td>Yes</td><td>Yes<a href="#sms-support-note-4">4</a></td><td>Registration required<a href="#sms-support-note-8">8</a></td><td>Yes</td><td>No</td></tr>
  <tr><td>United Kingdom</td><td>GB</td><td>44</td><td>Yes</td><td>Yes</td><td>Registration required<a href="#sms-support-note-7">7</a></td><td>Yes</td><td>No</td></tr>
  <tr><td>United States</td><td>US</td><td>1</td><td>Yes</td><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Uruguay</td><td>UY</td><td>598</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Uzbekistan</td><td>UZ</td><td>998</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr>
  <tr><td colspan="8"><b>V</b></td></tr>
  <tr><td>Vanuatu</td><td>VU</td><td>678</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>No</td></tr>
  <tr><td>Venezuela</td><td>VE</td><td>58</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr>
  <tr><td>Vietnam</td><td>VN</td><td>84</td><td>No</td><td>No</td><td>Registration required<a href="#sms-support-note-8">8</a></td><td>No</td><td>Yes</td></tr>
  <tr><td>Virgin Islands, British</td><td>VG</td><td>1-284</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>No</td></tr>
  <tr><td>Virgin Islands, US</td><td>VI</td><td>1-340</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td><td>No</td></tr>
  <tr><td colspan="8"><b>W</b></td></tr>
  <tr><td colspan="8"><b>X</b></td></tr>
  <tr><td colspan="8"><b>Y</b></td></tr>
  <tr><td>Yemen</td><td>YE</td><td>967</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>No</td></tr>
  <tr><td colspan="8"><b>Z</b></td></tr>
  <tr><td>Zambia</td><td>ZM</td><td>260</td><td>No</td><td>No</td><td>Registration required<a href="#sms-support-note-8">8</a></td><td>No</td><td>Yes</td></tr>
  <tr><td>Zimbabwe</td><td>ZW</td><td>263</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>No</td></tr>
</tbody>
</table>


**Notes**

1. <a name="sms-support-note-1"></a>You must use a pre-registered alphabetic Sender ID. All countries with sender ID registration requirements have self-service registration forms available in the console. For more information, see [Registration forms](registrations-country.md).

1. <a name="sms-support-note-2"></a>Senders are required to use a pre-registered template for each type of message that they plan to send. If a sender doesn’t meet this requirement, their messages will be blocked. To register a template, [China SMS template registration form](phone-numbers-sms-template-registration.md). Some countries require senders to meet additional, specific requirements or abide by certain restrictions to obtain approval. In these cases, Support might ask you for additional information.
**Note**  
To send messages to China, you must first register your templates through Support for approval.

1. <a name="sms-support-note-3"></a>You must use a pre-registered alphabetic Sender ID. Additional registration steps are required. For more information, see [India sender ID registration process in AWS End User Messaging SMS](registrations-sms-senderid-india.md).

1. <a name="sms-support-note-4"></a>Long codes in these countries only support inbound messaging. In other words, you can't use these long codes to send messages *to* your recipients, but you can use them to receive messages *from* your recipients. These long codes are useful way to allow your recipients to opt-out if you send messages using an alphabetic Sender ID, because Sender IDs only support outbound messages.

1. <a name="sms-support-note-5"></a>AWS End User Messaging SMS can send SMS traffic to Singapore using a sender ID that has been registered on the Singapore SMS Sender ID Registry (SSIR), a registry created by the [Info-communications Media Development Authority (IMDA)](https://www.imda.gov.sg/) of Singapore. For more information on requirements to use a Singapore Sender ID, see [Singapore sender ID registration process](registrations-sg.md). You can also send SMS traffic in Singapore using an alternative origination identity types such as Short Codes or Long Codes.

   If you do not register your sender ID any message sent using a sender ID will have its ID changed to **LIKELY-SCAM** per regulatory agency rules. Regulators will filter or block unregistered traffic at their discretion. 

1. <a name="sms-support-note-6"></a>Without a dedicated short code, AWS End User Messaging SMS still attempts to send messages to New Zealand recipients using a shared pool of short codes. Due to local carrier restrictions around shared numbers, deliverability over these shared numbers are made on a best-effort basis. Therefore, AWS End User Messaging SMS highly recommends procuring a dedicated short code for all traffic being sent to New Zealand. Messages containing URLs must be allow-listed through the dedicated short code process. For more information on purchasing a short code, see [Requesting dedicated short codes](phone-numbers-request-short-code.md).

1. <a name="sms-support-note-7"></a>Sender IDs for the United Kingdom are required to be registered. For more information on registering a sender ID, see [United Kingdom sender ID registration](registrations-uk.md).

1. <a name="sms-support-note-8"></a>Registration is required for the sender ID. For more information on completing the registration through the AWS End User Messaging SMS console see [Origination identity registration in AWS End User Messaging SMS](registrations.md). 

1. <a name="sms-support-note-9"></a>AWS End User Messaging SMS can send SMS traffic to Ireland using a sender ID that has been registered on the [ComReg SMS Sender ID Registry](https://www.comreg.ie/industry/electronic-communications/nuisance-communications/sms-sender-id-registry/). For more information on requirements to use a Ireland sender ID, see [Ireland sender ID registration in AWS End User Messaging SMS](registrations-ireland.md).

   If you do not register your sender ID, any message sent using a sender ID will have its ID changed to **Likely Scam** according to regulatory agency rules. Regulators filter or block unregistered traffic at their discretion.

1. <a name="sms-support-note-10"></a>Messages sent from internationally enabled numbers such as toll-free numbers are sent on a best effort basis and may be replaced downstream from AWS to send from a shared phone number or sender ID.

1. <a name="sms-support-note-11"></a>As of March 1, 2026, France does not support the dash character (-) in sender IDs. Sender IDs for France must only contain alphanumeric characters (a-z, A-Z, 0-9) without any special characters or spaces.