# Privacy-friendly and easy Google Maps embeds for Micro.blog

<img src="logo.png" alt="Google Maps Embeds for Micro.blog" width="200">

This plugin provides a privacy-friendly shortcode for embedding Google Maps into Micro.blog posts with click-to-load behavior and optional privacy notice.

## Installation

Install the plugin via the Micro.blog plugin directory or upload it manually as a `.zip` file.

## Usage

Add the following shortcode to a blog post to embed a map:

```markdown
{{< map center="48.1351,11.5820" zoom="14" >}}
```

If the `zoom` parameter is not set, the default zoom level will be used (see Configuration).

## Configuration

You can set the following optional parameters in your Micro.blog plugin settings:

- `show_privacy_notice`: Show or hide the overlay text before loading the map.
- `privacy_notice_text`: Customize the privacy overlay message.
- `default_map_zoom`: Set the default zoom level if none is specified in the shortcode.
- `google_staticmaps_key`: Your Google Maps Static API key (required).

### Obtaining an API Key

To use this plugin, you need a Google Maps Static API key. Follow these steps:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing one.
3. Navigate to **APIs & Services > Library**.
4. Search for **Maps Static API** and enable it.
5. Go to **APIs & Services > Credentials**.
6. Click **+ Create Credentials** > **API key**.
7. Copy the generated key and paste it into the plugin settings under `google_staticmaps_key`.

For production use, it's highly recommended to restrict the key to referrers or IP addresses.

## License

MIT

## Notes

To convert an address into coordinates, you can use:
https://www.latlong.net/