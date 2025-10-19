# Privacy-friendly and easy map embeds for Micro.blog

<img src="logo.png" alt="Map embeds for Micro.blog" width="200">

This plugin provides a privacy-friendly shortcode for embedding interactive maps into Micro.blog posts. It uses Leaflet together with OpenStreetMap tiles so that no API key is required. An optional privacy notice overlay can be shown on top of the map.

## Usage

Add the following shortcode to a blog post to embed a map:

```markdown
{{< map loc="48.1351,11.5820" zoom="14" >}}
```

```markdown
{{< map loc="Marienplatz, München" zoom="15" >}}
```

The `loc` parameter accepts either coordinates (e.g. `48.1351,11.5820`) or address strings (e.g. `Marienplatz, München`). If the `zoom` parameter is not set, the default zoom level defined in the plugin settings will be used. Address lookups are performed via [Nominatim](https://nominatim.openstreetmap.org/). You can see the plugin in action here: [Example Post](https://fischr.org/2017/09/03/oben-links-am-lago-di/)

## Configuration

You can configure the following options via your Micro.blog plugin settings:

- Show or hide the overlay message.
- Customize the privacy notice text displayed on the overlay.
- Set the default zoom level (used if no zoom value is set in the shortcode).

## Notes

Because the plugin talks directly to OpenStreetMap and Nominatim servers, please make sure your usage adheres to their respective terms of use. Heavy-traffic sites should consider running their own tile and geocoding services.

## 👤 Author

René Fischer – [https://fischr.org](https://fischr.org)
