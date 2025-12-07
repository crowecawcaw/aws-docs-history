# How to set a preferred language for

a map

Amazon Location Service enables you to set the preferred language at the client-side by updating the
style descriptor for a specific language. You can set a preferred language and display
content in that language where embedded. Otherwise, it will fall back to another
language.

###### Note

For more information, see [Localization and internationalization](maps-localization-internationalization.md "maps-localization-internationalization.md").

## Set preferred language to Japanese

and show map of Japan

In this example, you will set update style to show map labels in Japanese
(ja).

index.html

```

<html>
<head>
    <link href="https://unpkg.com/maplibre-gl@4.x/dist/maplibre-gl.css" rel="stylesheet" />
    <script src="https://unpkg.com/maplibre-gl@4.x/dist/maplibre-gl.js"></script>
    <link href="style.css" rel="stylesheet" />
    <script src="main.js"></script>
</head>
<body>
    <div id="map" />
    <script>
        const apiKey = "Add Your Api Key";
        const mapStyle = "Standard";
        const awsRegion = "eu-central-1";
        const initialLocation = [139.76694, 35.68085]; //Japan

        async function initializeMap() {
            // get updated style object for preferred language.
            const styleObject = await getStyleWithPreferredLanguage("ja");
            // Initialize the MapLibre map with the fetched style object
            const map = new maplibregl.Map({
                container: 'map',
                style: styleObject,
                center: initialLocation,
                zoom: 15,
                hash:true,
            });
            map.addControl(new maplibregl.NavigationControl(), "top-left");

            return map;
        }

        initializeMap();
    </script>
</body>
</html>

```

style.css

```

body { margin: 0; }
#map { height: 100vh; }

```

main.js

```

async function getStyleWithPreferredLanguage(preferredLanguage) {
    const styleUrl = `https://maps.geo.${awsRegion}.amazonaws.com/v2/styles/${mapStyle}/descriptor?key=${apiKey}`;

    return fetch(styleUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(styleObject => {
            if (preferredLanguage !== "en") {
                styleObject = setPreferredLanguage(styleObject, preferredLanguage);
            }

            return styleObject;
        })
        .catch(error => {
            console.error('Error fetching style:', error);
        });
}

const setPreferredLanguage = (style, language) => {
    let nextStyle = { ...style };

    nextStyle.layers = nextStyle.layers.map(l => {
        if (l.type !== 'symbol' || !l?.layout?.['text-field']) return l;
        return updateLayer(l, /^name:([A-Za-z\-\_]+)$/g, `name:${language}`);
    });

    return nextStyle;
};

const updateLayer = (layer, prevPropertyRegex, nextProperty) => {
    const nextLayer = {
        ...layer,
        layout: {
            ...layer.layout,
            'text-field': recurseExpression(
                layer.layout['text-field'],
                prevPropertyRegex,
                nextProperty
            )
        }
    };
    return nextLayer;
};

const recurseExpression = (exp, prevPropertyRegex, nextProperty) => {
    if (!Array.isArray(exp)) return exp;
    if (exp[0] !== 'coalesce') return exp.map(v =>
        recurseExpression(v, prevPropertyRegex, nextProperty)
    );

    const first = exp[1];
    const second = exp[2];

    let isMatch =
    Array.isArray(first) &&
    first[0] === 'get' &&
    !!first[1].match(prevPropertyRegex)?.[0];

    isMatch = isMatch && Array.isArray(second) && second[0] === 'get';
    isMatch = isMatch && !exp?.[4];

    if (!isMatch) return exp.map(v =>
        recurseExpression(v, prevPropertyRegex, nextProperty)
    );

    return [
        'coalesce',
        ['get', nextProperty],
        ['get', 'name:en'],
        ['get', 'name']
    ];
};

```

## Set preferred language based on end

user's browser language

In this example, you will set update style to show map labels in user's device
language.

index.html

```

<html>
<head>
    <link href="https://unpkg.com/maplibre-gl@4.x/dist/maplibre-gl.css" rel="stylesheet" />
    <script src="https://unpkg.com/maplibre-gl@4.x/dist/maplibre-gl.js"></script>
    <link href="style.css" rel="stylesheet" />
    <script src="main.js"></script>
</head>
<body>
    <div id="map" />
    <script>
        const apiKey = "Add Your Api Key";
        const mapStyle = "Standard";
        const awsRegion = "eu-central-1";
        const initialLocation = [139.76694, 35.68085]; //Japan
        const userLanguage = navigator.language || navigator.userLanguage;
        const languageCode = userLanguage.split('-')[0];

        async function initializeMap() {
             const styleObject = await getStyleWithPreferredLanguage(languageCode);
             const map = new maplibregl.Map({
                 container: 'map',
                 style: styleObject,
                 center: initialLocation,
                 zoom: 15,
                 hash:true,
             });
             map.addControl(new maplibregl.NavigationControl(), "top-left");
             return map;
        }

        initializeMap();
    </script>
</body>
</html>

```

style.css

```

body { margin: 0; }
#map { height: 100vh; }

```

main.js

```

async function getStyleWithPreferredLanguage(preferredLanguage) {
    const styleUrl = `https://maps.geo.${awsRegion}.amazonaws.com/v2/styles/${mapStyle}/descriptor?key=${apiKey}`;

    return fetch(styleUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(styleObject => {
            if (preferredLanguage !== "en") {
                styleObject = setPreferredLanguage(styleObject, preferredLanguage);
            }

            return styleObject;
        })
        .catch(error => {
            console.error('Error fetching style:', error);
        });
}

const setPreferredLanguage = (style, language) => {
    let nextStyle = { ...style };

    nextStyle.layers = nextStyle.layers.map(l => {
        if (l.type !== 'symbol' || !l?.layout?.['text-field']) return l;
        return updateLayer(l, /^name:([A-Za-z\-\_]+)$/g, `name:${language}`);
    });

    return nextStyle;
};

const updateLayer = (layer, prevPropertyRegex, nextProperty) => {
    const nextLayer = {
        ...layer,
        layout: {
            ...layer.layout,
            'text-field': recurseExpression(
                layer.layout['text-field'],
                prevPropertyRegex,
                nextProperty
            )
        }
    };
    return nextLayer;
};

const recurseExpression = (exp, prevPropertyRegex, nextProperty) => {
    if (!Array.isArray(exp)) return exp;
    if (exp[0] !== 'coalesce') return exp.map(v =>
        recurseExpression(v, prevPropertyRegex, nextProperty)
    );

    const first = exp[1];
    const second = exp[2];

    let isMatch =
    Array.isArray(first) &&
    first[0] === 'get' &&
    !!first[1].match(prevPropertyRegex)?.[0];

    isMatch = isMatch && Array.isArray(second) && second[0] === 'get';
    isMatch = isMatch && !exp?.[4];

    if (!isMatch) return exp.map(v =>
        recurseExpression(v, prevPropertyRegex, nextProperty)
    );

    return [
        'coalesce',
        ['get', nextProperty],
        ['get', 'name:en'],
        ['get', 'name']
    ];
};

```
