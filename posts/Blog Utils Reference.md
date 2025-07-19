---
title: "Blogging Module Guide"
author: "Isaac Beight-Welland"
date: date-modified
---

# Blog Utils Reference Guide

Complete reference for all functions in `blog_utils.py` - your comprehensive toolkit for creating rich, interactive blog content.

## Quick Import Setup

```python
# Add this to the beginning of your notebooks
import sys
import os
posts_dir = os.path.dirname(os.getcwd())
if posts_dir not in sys.path:
    sys.path.insert(0, posts_dir)

from blog_utils import *
```

## 📢 Callouts & Alerts

### Quarto-Style Callouts
```python
create_callout("Your message", callout_type="note", title="Custom Title")
# Types: "note", "tip", "warning", "caution", "important"
# Optional: collapsible=True, collapsed=True
```

### Bootstrap Alerts
```python
create_alert_box("Alert message", alert_type="success", title="Success!")
# Types: "info", "success", "warning", "danger", "primary", "secondary"
# Optional: dismissible=True
```

### Custom Info Boxes
```python
create_info_box("Custom message", icon="💡", background_color="#fff3cd")
```

## 🎬 Media Embeds

### YouTube Videos
```python
embed_youtube("dQw4w9WgXcQ")
# Optional: start_time=30, autoplay=True, controls=False
```

### Responsive iFrames
```python
create_responsive_iframe("https://example.com", aspect_ratio=0.5625)
# Perfect for embedding interactive content
```

### Other Media
```python
embed_vimeo("123456789")
embed_twitter_tweet("https://twitter.com/user/status/123")
embed_codepen("abc123", "username")
embed_plotly_chart("https://plotly.com/~user/chart.embed")
```

## 📊 Data Display

### Styled Tables
```python
create_styled_table(df, title="My Data", max_rows=10)
# Features: striped=True, hover=True, responsive=True
```

### Summary Statistics
```python
create_summary_stats(df, columns=["col1", "col2"])
# Automatically formats describe() output
```

### Comparison Tables
```python
data = {"Method A": [95, 87, 92], "Method B": [88, 91, 89]}
create_comparison_table(data, highlight_best=True)
```

## 🎛️ Interactive Elements

### Tabs
```python
tabs = {
    "Overview": "<p>Overview content</p>",
    "Details": "<p>Detailed information</p>",
    "Code": "<pre>code here</pre>"
}
create_tabs(tabs)
```

### Accordions
```python
sections = {
    "Section 1": "Content for section 1",
    "Section 2": "Content for section 2"
}
create_accordion(sections, allow_multiple=True)
```

## 📈 Progress & Metrics

### Progress Bars
```python
create_progress_bar(75, max_value=100, label="75% Complete", color="success")
# Colors: "primary", "success", "info", "warning", "danger"
# Optional: striped=True, animated=True
```

### Metric Cards
```python
create_metric_card(
    title="Revenue",
    value="$125K",
    change="+12.5%",
    change_type="positive",
    icon="💰"
)
```

## 🛠️ Utility Components

### Timeline
```python
events = [
    {"date": "2024-01", "title": "Project Start", "description": "Initial planning"},
    {"date": "2024-06", "title": "Milestone 1", "description": "First deliverable"}
]
create_timeline(events, title="Project Timeline")
```

### Quote Blocks
```python
create_quote_block(
    "The best time to plant a tree was 20 years ago. The second best time is now.",
    author="Chinese Proverb"
)
```

### Button Links
```python
create_button_link("Visit Site", "https://example.com", style="primary", size="lg")
# Styles: "primary", "secondary", "success", "info", "warning", "danger"
# Sizes: "sm", "md", "lg"
```

### Code Blocks
```python
create_code_block(
    "def hello():\n    print('Hello World')",
    language="python",
    title="Example Function"
)
```

### Two-Column Layout
```python
create_two_column_layout(
    left_content="<h4>Left Side</h4><p>Content here</p>",
    right_content="<h4>Right Side</h4><p>More content</p>",
    left_width=8,
    right_width=4
)
```

### Image Gallery
```python
images = [
    {"src": "image1.jpg", "alt": "Description", "caption": "Image 1"},
    {"src": "image2.jpg", "alt": "Description", "caption": "Image 2"}
]
create_image_gallery(images, columns=2, title="My Gallery")
```

## ⚡ Quick Helpers

For common use cases, use these shortcuts:

```python
quick_note("This is a note")
quick_tip("Pro tip: Use shortcuts!")
quick_warning("Be careful here")
quick_success("Great job!")
quick_info("FYI: This is useful")

quick_youtube("dQw4w9WgXcQ")
quick_iframe("https://example.com")
quick_quote("Life is what happens when you're busy making other plans", "John Lennon")
```

## 🎨 Styling Tips

### Color Schemes
- **Primary**: Blue theme (default)
- **Success**: Green for positive actions
- **Warning**: Yellow for cautions
- **Danger**: Red for errors/alerts
- **Info**: Light blue for information
- **Secondary**: Gray for neutral content

### Responsive Design
All components are mobile-friendly and will adapt to different screen sizes automatically.

### Customization
Most functions accept custom styling parameters. Check the function docstrings for all available options.

## 💡 Best Practices

1. **Use semantic colors** - Success for achievements, warning for cautions
2. **Keep content scannable** - Use callouts and alerts to highlight key points
3. **Optimize media** - Use appropriate aspect ratios for embedded content
4. **Test responsiveness** - Preview on different screen sizes
5. **Combine components** - Mix tables, charts, and callouts for rich content

## 🔧 Troubleshooting

**Import Issues**: Make sure the path setup code runs first
**Styling Problems**: Check that Bootstrap CSS is loaded in your Quarto theme
**Media Not Loading**: Verify URLs are accessible and properly formatted

## Examples in Action

Check the `_template` directory for a complete example notebook showing these utilities in use!