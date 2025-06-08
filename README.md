# Privacy-friendly and easy OSM embedds for Micro.blog

![Plugin Logo](logo.png)

This plugin provides a privacy-friendly shortcode for embedding OpenStreetMap into Micro.blog posts with click-to-load behavior and optional privacy notice.

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

## License

MIT

## Notes

To convert an address into coordinates, you can use:
https://nominatim.openstreetmap.org/ui/search.html

MIT