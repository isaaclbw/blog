"""
Comprehensive blog utilities module for Quarto blog posts.

This module provides a wide range of functions for creating formatted content
including callouts, iframes, media embeds, data displays, and interactive elements.
"""

from IPython.display import IFrame, HTML, display, Markdown
from typing import Optional, Union, List, Dict, Any
import pandas as pd
import json
import base64
from datetime import datetime


# =============================================================================
# CALLOUTS & ALERTS
# =============================================================================

def create_callout(
    content: str,
    callout_type: str = "note",
    title: Optional[str] = None,
    collapsible: bool = False,
    collapsed: bool = False
) -> HTML:
    """
    Create a Quarto-style callout box.
    
    Args:
        content: Callout content (supports markdown)
        callout_type: "note", "tip", "warning", "caution", "important" (default: "note")
        title: Optional custom title
        collapsible: Make callout collapsible (default: False)
        collapsed: Start collapsed if collapsible (default: False)
    
    Returns:
        IPython HTML object with Quarto callout
    """
    display_title = title or callout_type.title()
    collapse_class = "callout-collapse" if collapsible else ""
    collapse_state = "collapsed" if collapsed and collapsible else ""
    
    callout_html = f"""
    <div class="callout callout-style-default callout-{callout_type} {collapse_class} {collapse_state}">
        <div class="callout-header d-flex align-content-center">
            <div class="callout-icon-container">
                <i class="callout-icon"></i>
            </div>
            <div class="callout-title-container flex-fill">
                {display_title}
            </div>
        </div>
        <div class="callout-body-container callout-body">
            {content}
        </div>
    </div>
    """
    
    return HTML(callout_html)


def create_alert_box(
    content: str,
    alert_type: str = "info",
    title: Optional[str] = None,
    dismissible: bool = False
) -> HTML:
    """
    Create a Bootstrap-style alert box.
    
    Args:
        content: Alert content text
        alert_type: "info", "success", "warning", "danger", "primary", "secondary" (default: "info")
        title: Optional title for the alert
        dismissible: Add close button (default: False)
    
    Returns:
        IPython HTML object with styled alert
    """
    alert_classes = {
        "info": "alert-info",
        "success": "alert-success", 
        "warning": "alert-warning",
        "danger": "alert-danger",
        "primary": "alert-primary",
        "secondary": "alert-secondary"
    }
    
    alert_class = alert_classes.get(alert_type, "alert-info")
    title_html = f"<strong>{title}</strong><br>" if title else ""
    dismiss_class = " alert-dismissible" if dismissible else ""
    dismiss_button = """
    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    """ if dismissible else ""
    
    alert_html = f"""
    <div class="alert {alert_class}{dismiss_class}" role="alert">
        {title_html}{content}
        {dismiss_button}
    </div>
    """
    
    return HTML(alert_html)


def create_info_box(
    content: str,
    icon: str = "ℹ️",
    background_color: str = "#e3f2fd",
    border_color: str = "#2196f3"
) -> HTML:
    """
    Create a custom styled info box.
    
    Args:
        content: Box content
        icon: Icon or emoji (default: "ℹ️")
        background_color: Background color (default: light blue)
        border_color: Border color (default: blue)
    
    Returns:
        IPython HTML object with custom info box
    """
    box_html = f"""
    <div style="
        background-color: {background_color};
        border-left: 4px solid {border_color};
        padding: 15px;
        margin: 15px 0;
        border-radius: 4px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    ">
        <div style="display: flex; align-items: flex-start;">
            <div style="font-size: 1.2em; margin-right: 10px;">{icon}</div>
            <div style="flex: 1;">{content}</div>
        </div>
    </div>
    """
    
    return HTML(box_html)


# =============================================================================
# IFRAMES & EMBEDS
# =============================================================================

def create_responsive_iframe(
    src: str,
    aspect_ratio: float = 0.5625,  # 16:9 default
    max_width: str = "100%",
    border: str = "0",
    allowfullscreen: bool = True,
    loading: str = "lazy"
) -> HTML:
    """
    Create a responsive iframe that scales with container width.
    
    Args:
        src: URL to embed
        aspect_ratio: Height/width ratio (default: 0.5625 for 16:9)
        max_width: Maximum width of container (default: "100%")
        border: Border style (default: "0")
        allowfullscreen: Allow fullscreen (default: True)
        loading: Loading behavior - "lazy" or "eager" (default: "lazy")
    
    Returns:
        IPython HTML object with responsive iframe
    """
    padding_bottom = f"{aspect_ratio * 100}%"
    allowfullscreen_attr = "allowfullscreen" if allowfullscreen else ""
    
    iframe_html = f"""
    <div style="position: relative; width: {max_width}; height: 0; padding-bottom: {padding_bottom}; overflow: hidden; border-radius: 8px;">
        <iframe src="{src}" 
                style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: {border};"
                loading="{loading}"
                {allowfullscreen_attr}>
        </iframe>
    </div>
    """
    
    return HTML(iframe_html)


def embed_youtube(
    video_id: str,
    width: str = "100%",
    aspect_ratio: float = 0.5625,
    start_time: Optional[int] = None,
    autoplay: bool = False,
    controls: bool = True
) -> HTML:
    """
    Embed a YouTube video responsively.
    
    Args:
        video_id: YouTube video ID
        width: Container width (default: "100%")
        aspect_ratio: Height/width ratio (default: 0.5625 for 16:9)
        start_time: Start time in seconds (optional)
        autoplay: Auto-play video (default: False)
        controls: Show video controls (default: True)
    
    Returns:
        IPython HTML object with responsive YouTube embed
    """
    params = []
    if start_time:
        params.append(f"start={start_time}")
    if autoplay:
        params.append("autoplay=1")
    if not controls:
        params.append("controls=0")
    
    param_string = "&" + "&".join(params) if params else ""
    
    return create_responsive_iframe(
        src=f"https://www.youtube.com/embed/{video_id}?{param_string}",
        aspect_ratio=aspect_ratio,
        max_width=width
    )


def embed_vimeo(video_id: str, width: str = "100%", aspect_ratio: float = 0.5625) -> HTML:
    """Embed a Vimeo video responsively."""
    return create_responsive_iframe(
        src=f"https://player.vimeo.com/video/{video_id}",
        aspect_ratio=aspect_ratio,
        max_width=width
    )


def embed_twitter_tweet(tweet_url: str, theme: str = "light") -> HTML:
    """
    Embed a Twitter tweet.
    
    Args:
        tweet_url: Full Twitter tweet URL
        theme: "light" or "dark" (default: "light")
    
    Returns:
        IPython HTML object with Twitter embed
    """
    tweet_html = f"""
    <blockquote class="twitter-tweet" data-theme="{theme}">
        <a href="{tweet_url}"></a>
    </blockquote>
    <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
    """
    
    return HTML(tweet_html)


def embed_codepen(pen_id: str, user: str, height: int = 400, theme: str = "default") -> HTML:
    """
    Embed a CodePen.
    
    Args:
        pen_id: CodePen ID
        user: CodePen username
        height: Height in pixels (default: 400)
        theme: CodePen theme (default: "default")
    
    Returns:
        IPython HTML object with CodePen embed
    """
    return create_responsive_iframe(
        src=f"https://codepen.io/{user}/embed/{pen_id}?height={height}&theme-id={theme}&default-tab=result",
        aspect_ratio=height/800,  # Approximate ratio
        max_width="100%"
    )


def embed_plotly_chart(
    chart_url: str,
    height: int = 500,
    width: str = "100%"
) -> HTML:
    """
    Embed a Plotly chart from a sharing URL.
    
    Args:
        chart_url: Plotly chart sharing URL
        height: Height in pixels (default: 500)
        width: Width (default: "100%")
    
    Returns:
        IPython HTML object with Plotly embed
    """
    iframe_html = f"""
    <iframe src="{chart_url}" 
            width="{width}" 
            height="{height}" 
            frameborder="0" 
            style="border: 0; border-radius: 8px;">
    </iframe>
    """
    
    return HTML(iframe_html)
# =============================================================================
# DATA DISPLAY & TABLES
# =============================================================================

def create_styled_table(
    df: pd.DataFrame,
    title: Optional[str] = None,
    caption: Optional[str] = None,
    max_rows: Optional[int] = None,
    striped: bool = True,
    hover: bool = True,
    responsive: bool = True
) -> HTML:
    """
    Create a styled HTML table from a pandas DataFrame.
    
    Args:
        df: Pandas DataFrame
        title: Optional table title
        caption: Optional table caption
        max_rows: Maximum rows to display (default: None for all)
        striped: Striped rows (default: True)
        hover: Hover effect (default: True)
        responsive: Responsive table (default: True)
    
    Returns:
        IPython HTML object with styled table
    """
    display_df = df.head(max_rows) if max_rows else df
    
    table_classes = ["table"]
    if striped:
        table_classes.append("table-striped")
    if hover:
        table_classes.append("table-hover")
    
    table_class_str = " ".join(table_classes)
    
    title_html = f"<h4>{title}</h4>" if title else ""
    caption_html = f"<caption>{caption}</caption>" if caption else ""
    
    table_html = display_df.to_html(classes=table_class_str, escape=False, table_id="styled-table")
    
    if responsive:
        table_html = f'<div class="table-responsive">{table_html}</div>'
    
    final_html = f"""
    <div style="margin: 20px 0;">
        {title_html}
        {table_html}
        {caption_html}
    </div>
    """
    
    return HTML(final_html)


def create_summary_stats(
    df: pd.DataFrame,
    columns: Optional[List[str]] = None,
    title: str = "Summary Statistics"
) -> HTML:
    """
    Create a formatted summary statistics table.
    
    Args:
        df: Pandas DataFrame
        columns: Specific columns to summarize (default: all numeric)
        title: Table title (default: "Summary Statistics")
    
    Returns:
        IPython HTML object with summary stats table
    """
    if columns:
        summary_df = df[columns].describe()
    else:
        summary_df = df.select_dtypes(include=['number']).describe()
    
    return create_styled_table(
        summary_df.round(3),
        title=title,
        striped=True,
        hover=True
    )


def create_comparison_table(
    data: Dict[str, List],
    title: str = "Comparison",
    highlight_best: bool = True
) -> HTML:
    """
    Create a comparison table with optional highlighting.
    
    Args:
        data: Dictionary with column names as keys and lists as values
        title: Table title
        highlight_best: Highlight best values (default: True)
    
    Returns:
        IPython HTML object with comparison table
    """
    df = pd.DataFrame(data)
    
    if highlight_best:
        # Simple highlighting for numeric columns
        styled_html = df.style.highlight_max(axis=0, color='lightgreen').to_html()
    else:
        styled_html = df.to_html(classes="table table-striped table-hover")
    
    final_html = f"""
    <div style="margin: 20px 0;">
        <h4>{title}</h4>
        <div class="table-responsive">
            {styled_html}
        </div>
    </div>
    """
    
    return HTML(final_html)

# =============================================================================
# INTERACTIVE ELEMENTS
# =============================================================================

def create_tabs(
    tabs_content: Dict[str, str],
    tab_id: str = "custom-tabs"
) -> HTML:
    """
    Create Bootstrap-style tabs.
    
    Args:
        tabs_content: Dictionary with tab names as keys and content as values
        tab_id: Unique ID for the tab group (default: "custom-tabs")
    
    Returns:
        IPython HTML object with tabs
    """
    tab_nav = []
    tab_content = []
    
    for i, (tab_name, content) in enumerate(tabs_content.items()):
        active_class = "active" if i == 0 else ""
        tab_id_clean = tab_name.lower().replace(" ", "-")
        
        tab_nav.append(f'''
        <li class="nav-item" role="presentation">
            <button class="nav-link {active_class}" id="{tab_id}-{tab_id_clean}-tab" 
                    data-bs-toggle="tab" data-bs-target="#{tab_id}-{tab_id_clean}" 
                    type="button" role="tab">
                {tab_name}
            </button>
        </li>
        ''')
        
        tab_content.append(f'''
        <div class="tab-pane fade {'show active' if i == 0 else ''}" 
             id="{tab_id}-{tab_id_clean}" role="tabpanel">
            {content}
        </div>
        ''')
    
    tabs_html = f'''
    <div>
        <ul class="nav nav-tabs" id="{tab_id}" role="tablist">
            {"".join(tab_nav)}
        </ul>
        <div class="tab-content" id="{tab_id}-content">
            {"".join(tab_content)}
        </div>
    </div>
    '''
    
    return HTML(tabs_html)


def create_accordion(
    accordion_items: Dict[str, str],
    accordion_id: str = "custom-accordion",
    allow_multiple: bool = False
) -> HTML:
    """
    Create Bootstrap-style accordion.
    
    Args:
        accordion_items: Dictionary with section titles as keys and content as values
        accordion_id: Unique ID for the accordion (default: "custom-accordion")
        allow_multiple: Allow multiple sections open (default: False)
    
    Returns:
        IPython HTML object with accordion
    """
    accordion_sections = []
    
    for i, (title, content) in enumerate(accordion_items.items()):
        section_id = f"{accordion_id}-section-{i}"
        show_class = "show" if i == 0 else ""
        collapsed_class = "" if i == 0 else "collapsed"
        
        accordion_sections.append(f'''
        <div class="accordion-item">
            <h2 class="accordion-header" id="{section_id}-heading">
                <button class="accordion-button {collapsed_class}" type="button" 
                        data-bs-toggle="collapse" data-bs-target="#{section_id}" 
                        aria-expanded="{'true' if i == 0 else 'false'}">
                    {title}
                </button>
            </h2>
            <div id="{section_id}" class="accordion-collapse collapse {show_class}" 
                 data-bs-parent="#{accordion_id if not allow_multiple else ''}">
                <div class="accordion-body">
                    {content}
                </div>
            </div>
        </div>
        ''')
    
    accordion_html = f'''
    <div class="accordion" id="{accordion_id}">
        {"".join(accordion_sections)}
    </div>
    '''
    
    return HTML(accordion_html)
# =============================================================================
# PROGRESS & METRICS
# =============================================================================

def create_progress_bar(
    value: float,
    max_value: float = 100,
    label: Optional[str] = None,
    color: str = "primary",
    striped: bool = False,
    animated: bool = False
) -> HTML:
    """
    Create a progress bar.
    
    Args:
        value: Current value
        max_value: Maximum value (default: 100)
        label: Optional label text
        color: Bootstrap color - "primary", "success", "info", "warning", "danger" (default: "primary")
        striped: Striped appearance (default: False)
        animated: Animated stripes (default: False)
    
    Returns:
        IPython HTML object with progress bar
    """
    percentage = (value / max_value) * 100
    
    progress_classes = [f"bg-{color}"]
    if striped:
        progress_classes.append("progress-bar-striped")
    if animated:
        progress_classes.append("progress-bar-animated")
    
    progress_class_str = " ".join(progress_classes)
    label_text = label or f"{percentage:.1f}%"
    
    progress_html = f'''
    <div class="progress" style="height: 25px; margin: 10px 0;">
        <div class="progress-bar {progress_class_str}" role="progressbar" 
             style="width: {percentage}%" aria-valuenow="{value}" 
             aria-valuemin="0" aria-valuemax="{max_value}">
            {label_text}
        </div>
    </div>
    '''
    
    return HTML(progress_html)


def create_metric_card(
    title: str,
    value: Union[str, int, float],
    subtitle: Optional[str] = None,
    change: Optional[str] = None,
    change_type: str = "neutral",
    icon: Optional[str] = None
) -> HTML:
    """
    Create a metric display card.
    
    Args:
        title: Metric title
        value: Metric value
        subtitle: Optional subtitle
        change: Optional change indicator (e.g., "+5.2%")
        change_type: "positive", "negative", "neutral" (default: "neutral")
        icon: Optional icon/emoji
    
    Returns:
        IPython HTML object with metric card
    """
    change_colors = {
        "positive": "#28a745",
        "negative": "#dc3545",
        "neutral": "#6c757d"
    }
    
    change_color = change_colors.get(change_type, "#6c757d")
    
    icon_html = f'<div style="font-size: 2em; margin-bottom: 10px;">{icon}</div>' if icon else ""
    subtitle_html = f'<div style="color: #6c757d; font-size: 0.9em;">{subtitle}</div>' if subtitle else ""
    change_html = f'<div style="color: {change_color}; font-weight: bold; margin-top: 5px;">{change}</div>' if change else ""
    
    card_html = f'''
    <div style="
        border: 1px solid #dee2e6;
        border-radius: 8px;
        padding: 20px;
        margin: 10px 0;
        text-align: center;
        background: white;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    ">
        {icon_html}
        <div style="font-size: 0.9em; color: #6c757d; margin-bottom: 5px;">{title}</div>
        <div style="font-size: 2em; font-weight: bold; color: #212529;">{value}</div>
        {subtitle_html}
        {change_html}
    </div>
    '''
    
    return HTML(card_html)
# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

def create_timeline(
    events: List[Dict[str, str]],
    title: str = "Timeline"
) -> HTML:
    """
    Create a vertical timeline.
    
    Args:
        events: List of dictionaries with 'date', 'title', and 'description' keys
        title: Timeline title
    
    Returns:
        IPython HTML object with timeline
    """
    timeline_items = []
    
    for event in events:
        timeline_items.append(f'''
        <div style="
            position: relative;
            padding-left: 30px;
            margin-bottom: 30px;
            border-left: 2px solid #007bff;
        ">
            <div style="
                position: absolute;
                left: -8px;
                top: 0;
                width: 14px;
                height: 14px;
                border-radius: 50%;
                background: #007bff;
            "></div>
            <div style="font-weight: bold; color: #007bff; font-size: 0.9em;">
                {event.get('date', '')}
            </div>
            <div style="font-weight: bold; margin: 5px 0;">
                {event.get('title', '')}
            </div>
            <div style="color: #6c757d;">
                {event.get('description', '')}
            </div>
        </div>
        ''')
    
    timeline_html = f'''
    <div style="margin: 20px 0;">
        <h4>{title}</h4>
        <div style="margin-top: 20px;">
            {"".join(timeline_items)}
        </div>
    </div>
    '''
    
    return HTML(timeline_html)


def create_quote_block(
    quote: str,
    author: Optional[str] = None,
    source: Optional[str] = None
) -> HTML:
    """
    Create a styled quote block.
    
    Args:
        quote: Quote text
        author: Quote author (optional)
        source: Quote source (optional)
    
    Returns:
        IPython HTML object with quote block
    """
    author_html = f"<cite>— {author}</cite>" if author else ""
    source_html = f"<small>, {source}</small>" if source else ""
    
    quote_html = f'''
    <blockquote style="
        border-left: 4px solid #007bff;
        padding: 20px;
        margin: 20px 0;
        background: #f8f9fa;
        font-style: italic;
        font-size: 1.1em;
    ">
        <p style="margin-bottom: 10px;">"{quote}"</p>
        <footer style="text-align: right; font-size: 0.9em;">
            {author_html}{source_html}
        </footer>
    </blockquote>
    '''
    
    return HTML(quote_html)


def create_button_link(
    text: str,
    url: str,
    style: str = "primary",
    size: str = "md",
    new_tab: bool = True
) -> HTML:
    """
    Create a styled button link.
    
    Args:
        text: Button text
        url: Link URL
        style: Bootstrap button style - "primary", "secondary", "success", etc. (default: "primary")
        size: Button size - "sm", "md", "lg" (default: "md")
        new_tab: Open in new tab (default: True)
    
    Returns:
        IPython HTML object with button link
    """
    size_class = f"btn-{size}" if size != "md" else ""
    target = 'target="_blank" rel="noopener noreferrer"' if new_tab else ""
    
    button_html = f'''
    <a href="{url}" class="btn btn-{style} {size_class}" {target} 
       style="margin: 10px 5px; text-decoration: none;">
        {text}
    </a>
    '''
    
    return HTML(button_html)


def create_code_block(
    code: str,
    language: str = "python",
    title: Optional[str] = None,
    line_numbers: bool = False
) -> HTML:
    """
    Create a syntax-highlighted code block.
    
    Args:
        code: Code content
        language: Programming language (default: "python")
        title: Optional code block title
        line_numbers: Show line numbers (default: False)
    
    Returns:
        IPython HTML object with code block
    """
    title_html = f'<div style="background: #f1f3f4; padding: 8px 12px; font-weight: bold; border-bottom: 1px solid #ddd;">{title}</div>' if title else ""
    
    code_html = f'''
    <div style="border: 1px solid #ddd; border-radius: 4px; margin: 15px 0; overflow: hidden;">
        {title_html}
        <pre style="margin: 0; padding: 15px; background: #f8f9fa; overflow-x: auto;"><code class="language-{language}">{code}</code></pre>
    </div>
    '''
    
    return HTML(code_html)


def create_two_column_layout(
    left_content: str,
    right_content: str,
    left_width: int = 6,
    right_width: int = 6
) -> HTML:
    """
    Create a two-column layout using Bootstrap grid.
    
    Args:
        left_content: Content for left column
        right_content: Content for right column
        left_width: Left column width (1-12, default: 6)
        right_width: Right column width (1-12, default: 6)
    
    Returns:
        IPython HTML object with two-column layout
    """
    layout_html = f'''
    <div class="row" style="margin: 20px 0;">
        <div class="col-md-{left_width}">
            {left_content}
        </div>
        <div class="col-md-{right_width}">
            {right_content}
        </div>
    </div>
    '''
    
    return HTML(layout_html)


def create_image_gallery(
    images: List[Dict[str, str]],
    columns: int = 3,
    title: Optional[str] = None
) -> HTML:
    """
    Create an image gallery.
    
    Args:
        images: List of dicts with 'src', 'alt', and optional 'caption' keys
        columns: Number of columns (default: 3)
        title: Optional gallery title
    
    Returns:
        IPython HTML object with image gallery
    """
    col_width = 12 // columns
    title_html = f"<h4>{title}</h4>" if title else ""
    
    image_items = []
    for img in images:
        caption_html = f'<div class="text-center mt-2"><small>{img.get("caption", "")}</small></div>' if img.get("caption") else ""
        
        image_items.append(f'''
        <div class="col-md-{col_width} mb-4">
            <div class="card">
                <img src="{img['src']}" class="card-img-top" alt="{img.get('alt', '')}" style="height: 200px; object-fit: cover;">
                <div class="card-body">
                    {caption_html}
                </div>
            </div>
        </div>
        ''')
    
    gallery_html = f'''
    <div style="margin: 20px 0;">
        {title_html}
        <div class="row">
            {"".join(image_items)}
        </div>
    </div>
    '''
    
    return HTML(gallery_html)


# =============================================================================
# QUICK HELPERS
# =============================================================================

def quick_note(content: str) -> HTML:
    """Quick note callout."""
    return create_callout(content, "note")

def quick_tip(content: str) -> HTML:
    """Quick tip callout."""
    return create_callout(content, "tip")

def quick_warning(content: str) -> HTML:
    """Quick warning callout."""
    return create_callout(content, "warning")

def quick_success(content: str) -> HTML:
    """Quick success alert."""
    return create_alert_box(content, "success")

def quick_info(content: str) -> HTML:
    """Quick info alert."""
    return create_alert_box(content, "info")

def quick_youtube(video_id: str) -> HTML:
    """Quick YouTube embed with standard settings."""
    return embed_youtube(video_id)

def quick_iframe(url: str, aspect_ratio: float = 0.5625) -> HTML:
    """Quick responsive iframe."""
    return create_responsive_iframe(url, aspect_ratio)

def quick_quote(quote: str, author: Optional[str] = None) -> HTML:
    """Quick quote block."""
    return create_quote_block(quote, author)