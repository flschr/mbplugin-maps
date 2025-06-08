# mbplugin-osm-map

This plugin provides a privacy-friendly shortcode for embedding OpenStreetMap into Micro.blog posts.

## Installation

Install the plugin via the Micro.blog plugin directory or upload it manually as a `.zip` file.

## Usage

Add the following shortcode to a blog post to embed a map:

```markdown
{{< map center="48.1351,11.5820" zoom="14" >}}
```

## Configuration

You can set the following optional parameters in your `config.json` or Micro.blog plugin settings:

```toml
[params]
show_privacy_notice = true
privacy_notice_text = "By loading the map, you accept the privacy policy of OpenStreetMap."
```

## License

MIT