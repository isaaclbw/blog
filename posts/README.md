# Blog Post Template

This template provides a standardized structure for new blog posts with pre-configured imports and utilities.

## Usage

1. **Copy this entire `_template` folder**
2. **Rename it** to your post slug (e.g., `my-new-post`)
3. **Edit the metadata** in the first cell of `main.ipynb`
4. **Replace the placeholder content** with your actual content
5. **Add your image** as `image.jpg` (or update the image filename in metadata)

## Template Features

- ✅ Pre-configured YAML metadata
- ✅ Hidden import cells (won't show in rendered output)
- ✅ Blog utilities automatically imported
- ✅ Standard data science imports included
- ✅ Example usage of blog utility functions
- ✅ Structured content sections

## Quarto Cell Options Used

The template uses these Quarto cell execution options:

### `#| include: false`
- **Hides both code AND output** from rendered document
- Used for setup/import cells
- Code still executes, just not displayed

### Other useful options you can add:

- `#| echo: false` - Hide code, show output only
- `#| output: false` - Show code, hide output
- `#| warning: false` - Hide warnings
- `#| message: false` - Hide messages
- `#| fig-cap: "Your caption"` - Add figure captions

## Customization

### Metadata Fields
Update these in the first cell:
- `title`: Your post title
- `categories`: Array of relevant categories
- `description`: SEO description
- `image`: Filename of your header image

### Categories
Common categories you might use:
- `[economics, analysis]`
- `[data-science, python]`
- `[visualization, tutorial]`
- `[finance, markets]`

### Images
- Add your header image as `image.jpg`
- Or update the `image` field in metadata to match your filename
- Recommended size: 1200x630px for social media

## Quick Start Checklist

- [ ] Copy and rename `_template` folder
- [ ] Update title in metadata
- [ ] Update categories in metadata  
- [ ] Add description in metadata
- [ ] Replace placeholder content
- [ ] Add header image
- [ ] Test blog utilities import
- [ ] Write your content!