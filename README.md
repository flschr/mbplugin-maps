# Privacy-friendly and easy Google Maps embeds for Micro.blog

<img src="logo.png" alt="Google Maps Embeds for Micro.blog" width="200">

This plugin provides a privacy-friendly shortcode for embedding Google Maps into Micro.blog posts. It displays a static image of the map and only loads the interactive map from Google Maps after the user clicks on it. An optional privacy notice overlay can be shown before loading the map.

## Usage

Add the following shortcode to a blog post to embed a map:

```markdown
{{< map loc="48.1351,11.5820" zoom="14" >}}
```

```markdown
{{< map loc="Marienplatz, München" zoom="15" >}}
```

The `loc` parameter accepts either coordinates (e.g. `48.1351,11.5820`) or address strings (e.g. `Marienplatz, München`). If the `zoom` parameter is not set, the default zoom level defined in the plugin settings will be used. You can see the plugin in action here: [Example Post](https://fischr.org/2017/09/03/oben-links-am-lago-di/)

## Configuration

You can configure the following options via your Micro.blog plugin settings:

- Show or hide the overlay message before the map loads.
- Customize the privacy notice text.
- Set the default zoom level (used if no zoom value is set in the shortcode).
- Enter your Google Maps Static API key (required).

### Obtaining an API Key

To use this plugin, you'll need a Google Maps Static API key. Here's how to get one:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing one.
3. Navigate to **APIs & Services > Library**.
4. Search for **Maps Static API** and enable it.
5. Go to **APIs & Services > Credentials**.
6. Click **+ Create Credentials** > **API key**.
7. Copy the generated key and paste it into the plugin settings under `google_staticmaps_key`.

> ⚠️ The Google Maps Static API includes $200 of free usage per month (~100,000 map views). See [pricing information](https://developers.google.com/maps/billing-and-pricing/pricing) for details.  
> 🔒 To prevent abuse, it’s highly recommended to restrict your API key to your domain.

## Notes

To convert an address to coordinates, you can use:
[https://www.latlong.net](https://www.latlong.net)

## 👤 Author

René Fischer – [https://fischr.org](https://fischr.org)