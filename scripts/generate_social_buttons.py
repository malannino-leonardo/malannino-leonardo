#!/usr/bin/env python3
"""
Generate sleek dark terminal-style SVG button assets for social links.
Consistent with the GitHub dark theme (#0d1117, #161b22, #30363d).
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, "..", "assets")
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 200, 48

BUTTONS = [
    {
        "file": "linkedin.svg",
        "title": "LinkedIn",
        "sub": "Leonardo Malannino",
        "accent": "#0a66c2",
        "icon": (
            '<path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z" '
            'fill="none" stroke="#0a66c2" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'
            '<rect width="4" height="12" x="2" y="9" fill="none" stroke="#0a66c2" stroke-width="2" '
            'stroke-linecap="round" stroke-linejoin="round"/>'
            '<circle cx="4" cy="4" r="2" fill="none" stroke="#0a66c2" stroke-width="2"/>'
        ),
    },
    {
        "file": "x.svg",
        "title": "X",
        "sub": "@Cronixey",
        "accent": "#e6edf3",
        "icon": (
            '<path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 '
            '2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z" fill="#e6edf3"/>'
        ),
    },
    {
        "file": "instagram.svg",
        "title": "Instagram",
        "sub": "@leonardo.malannino",
        "accent": "#e1306c",
        "icon": (
            '<rect width="20" height="20" x="2" y="2" rx="5" ry="5" fill="none" stroke="#e1306c" '
            'stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'
            '<path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z" fill="none" stroke="#e1306c" '
            'stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'
            '<line x1="17.5" x2="17.51" y1="6.5" y2="6.5" stroke="#e1306c" stroke-width="2" '
            'stroke-linecap="round" stroke-linejoin="round"/>'
        ),
    },
    {
        "file": "portfolio.svg",
        "title": "Portfolio",
        "sub": "leomal.it",
        "accent": "#22d3ee",
        "icon": (
            '<circle cx="12" cy="12" r="10" fill="none" stroke="#22d3ee" stroke-width="2"/>'
            '<path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20" fill="none" stroke="#22d3ee" stroke-width="2"/>'
            '<path d="M2 12h20" fill="none" stroke="#22d3ee" stroke-width="2"/>'
        ),
    },
]


def render_button(b):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#161b22"/>
      <stop offset="100%" stop-color="#0d1117"/>
    </linearGradient>
  </defs>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="8" fill="url(#bg)" stroke="#30363d" stroke-width="1"/>
  <g transform="translate(14, 12)">
    {b["icon"]}
  </g>
  <text x="46" y="22" fill="#e6edf3" font-size="13" font-weight="600" letter-spacing="0.2px">{b["title"]}</text>
  <text x="46" y="37" fill="#7d8590" font-size="11" font-family="ui-monospace, SFMono-Regular, Menlo, monospace">{b["sub"]}</text>
  <path d="M{W-18} 21 L{W-13} 24 L{W-18} 27" stroke="#7d8590" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
</svg>"""


def main():
    for b in BUTTONS:
        svg = render_button(b)
        path = os.path.join(OUT_DIR, b["file"])
        with open(path, "w", encoding="utf-8") as f:
            f.write(svg)
        print(f"Wrote {path} ({len(svg)} bytes)")


if __name__ == "__main__":
    main()

