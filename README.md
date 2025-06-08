# Privacy-friendly and easy Google Maps embeds for Micro.blog

<img src="logo.png" alt="Google Maps Embeds for Micro.blog" width="200">

This plugin provides a privacy-friendly shortcode for embedding Google Maps into Micro.blog posts. It shows a static picture of the map and after a click, it loads the map from Google Maps. Optionaly a privacy notice can be added as an overlay.

## Usage
Add the following shortcode to a blog post to embed a map:

```markdown
{{< map center="48.1351,11.5820" zoom="14" >}}
```
If the `zoom` parameter is not set, the default zoom level will be used (see Configuration). You can see the plugin in action here: [Example Post](https://fischr.org/2017/09/03/oben-links-am-lago-di/)

## Configuration
You can set the following optional parameters in your Micro.blog plugin settings:

- Show or hide the overlay text before loading the map
- Customize the privacy overlay message.
- Set the default zoom level if none is specified in the shortcode.
- Your Google Maps Static API key (required).

### Obtaining an API Key
To use this plugin, you need a Google Maps Static API key. Follow these steps:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing one.
3. Navigate to **APIs & Services > Library**.
4. Search for **Maps Static API** and enable it.
5. Go to **APIs & Services > Credentials**.
6. Click **+ Create Credentials** > **API key**.
7. Copy the generated key and paste it into the plugin settings under `google_staticmaps_key`.

The Google Maps Static API is free of charge for 10.000 views per month, see [pricing information](https://developers.google.com/maps/billing-and-pricing/pricing). To avoid missuse, it is highly recommended to restrict the key to your domain. 

## Notes
To convert an address into coordinates, you can use:
https://www.latlong.net/

## 👤 Author
René Fischer – [https://fischr.org](https://fischr.org)