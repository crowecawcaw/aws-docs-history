

# Localization and internationalization
<a name="maps-localization-internationalization"></a>

Amazon Location Service supports localization features that enable you to customize maps for specific languages and regions. This includes support for local place names and the ability to render maps in different languages.


| Style | Political View | Languages | 
| --- | --- | --- | 
| Standard | Argentina, Brazil, Cyprus, Egypt, Georgia, Greece, India, Israel, Kenya, Morocco, Palestine, Serbia, Russia, Sudan, Suriname, Syria, Türkiye, Tanzania, United States, Uruguay, Vietnam | Supported through client-side library | 
| Monochrome | Argentina, Brazil, Cyprus, Egypt, Georgia, Greece, India, Israel, Kenya, Morocco, Palestine, Serbia, Russia, Sudan, Suriname, Syria, Türkiye, Tanzania, United States, Uruguay, Vietnam | Supported through client-side library | 
| Hybrid | Argentina, Brazil, Cyprus, Egypt, Georgia, Greece, India, Israel, Kenya, Morocco, Palestine, Serbia, Russia, Sudan, Suriname, Syria, Türkiye, Tanzania, United States, Uruguay, Vietnam | Supported through client-side library | 
| Satellite | Not supported | Not supported | 

## Languages
<a name="maps-languages"></a>

Amazon Location Service provides Maps APIs that enable you to customize the language of map labels and text elements. This capability helps your applications cater to a global audience or regions with multiple languages. By displaying maps in the user's preferred language, you enhance the overall user experience, making the maps more accessible and relevant to your diverse user base.

For more information, see [How to set a preferred language for a map](how-to-set-preferred-language-map.md).

![Animated demonstration of the Amazon Location Service language switcher, cycling through map labels in different languages on a map of Taiwan.](https://docs.aws.amazon.com/location/latest/developerguide/images/standard-language-switcher.gif)


## Political view
<a name="maps-political"></a>

By default, Amazon Location Service presents an international perspective, which visually represents disputed territories with dashed borders. To switch from the international perspective to a country-specific geopolitical view, use the *political view* parameter in your API query. This helps businesses comply with local laws, as certain countries require adherence to their specific geopolitical views for maps and map data.

In addition to the default international perspective, Amazon Location Service supports the geopolitical views of the following countries: Argentina, Brazil, Cyprus, Egypt, Georgia, Greece, India, Israel, Kenya, Morocco, Palestine, Serbia, Russia, Sudan, Suriname, Syria, Türkiye, Tanzania, United States, Uruguay, Vietnam. To activate a geopolitical view, pass the appropriate value to the *political view* parameter.

The following table lists the political view values that are currently available, and the perspective that each one applies.


| Political view value | Description | 
| --- | --- | 
| `ARG` | Argentina's view on the Southern Patagonian Ice Field and Tierra Del Fuego, including the Falkland Islands, South Georgia, and South Sandwich Islands | 
| `BRA` | Brazil's view on Rincon de Artigas in the Brazil/Uruguay dispute | 
| `EGY` | Egypt's view on Bir Tawil | 
| `IND` | India's view on Gilgit-Baltistan | 
| `ISR` | Israel's view on the West Bank and Gaza Strip | 
| `KEN` | Kenya's view on the Ilemi Triangle | 
| `MAR` | Morocco's view on Western Sahara | 
| `PSE` | Palestine's view on the West Bank and Gaza Strip | 
| `RUS` | Russia's view on Crimea | 
| `SDN` | Sudan's view on the Halaib Triangle | 
| `SRB` | Serbia's view on Kosovo, Vukovar, and Sarengrad Islands | 
| `SUR` | Suriname's view on the Courantyne Headwaters and Lawa Headwaters | 
| `SYR` | Syria's view on the Golan Heights | 
| `TUR` | Türkiye's view on Cyprus and Northern Cyprus | 
| `TZA` | Tanzania's view on Lake Malawi | 
| `URY` | Uruguay's view on Rincon de Artigas in the Brazil/Uruguay dispute | 
| `USA` | United States' names for Lake Ontario and the Gulf of Mexico | 
| `VNM` | Vietnam's view on the Paracel Islands and Spratly Islands | 

For more information, see [How to set the political view of a map](how-to-set-political-view-map.md).

![Two maps of Cyprus demonstrating Amazon Location Service political view options, showing how disputed territorial boundaries render differently based on country-specific perspectives.](https://docs.aws.amazon.com/location/latest/developerguide/images/maps-political-view.png)
