import os

# Data for portfolio items
portfolio_items = [
    {"file": "item-aemond-vhagar.html", "img": "img/Aemond.png", "alt": "Aemond & Vhagar", "text": "Aemond & Vhagar"},
    {"file": "item-traston-calamity.html", "img": "img/Traston - Calamity.jpg", "alt": "Traston & Calamity", "text": "Traston & Calamity"},
    {"file": "item-dyer.html", "img": "img/Dyer.jpg", "alt": "Dyer", "text": "Dyer"},
    {"file": "item-vicer.html", "img": "img/Vicer.jpg", "alt": "Vicer", "text": "Vicer"},
    {"file": "item-lyssa.html", "img": "img/Lyssa.jpg", "alt": "Lyssa", "text": "Lyssa"},
    {"file": "item-traston.html", "img": "img/Traston - Version 2.jpg", "alt": "Traston", "text": "Traston"},
    {"file": "item-teryn-aetherson.html", "img": "img/Teryn Aetherson.jpg", "alt": "Teryn Aetherson", "text": "Teryn Aetherson"},
    {"file": "item-hush.html", "img": "img/Hush.jpg", "alt": "Hush", "text": "Hush"},
    {"file": "item-walton-parthall.html", "img": "img/Walton Parthall.jpg", "alt": "Walton Parthall", "text": "Walton Parthall"},
    {"file": "item-valthos.html", "img": "img/Valthos - Version 1.jpg", "alt": "Valthos", "text": "Valthos"},
    {"file": "item-carmilla.html", "img": "img/Carmilla.jpg", "alt": "Carmilla", "text": "Carmilla"},
    {"file": "item-the-masque.html", "img": "img/The Masque.jpg", "alt": "The Masque", "text": "The Masque"},
]

# HTML template
html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{text} - Berkan Cetinbag</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="stylesheet" href="flexboxgrid.min.css" type="text/css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
</head>
<body>
    <div class="container">
        <header class="row center-xs">
            <div class="header-content col-xs-12 col-md-4 center-xs">
                <nav>
                    <ul>
                        <li><a href="index.html">Works</a></li>
                        <li><a href="about.html">About Me</a></li>
                    </ul>
                </nav>
                <h1>BERKAN CETINBAG</h1>
            </div>
            <a href="https://www.instagram.com/berkancet/" class="instagram-icon" target="_blank" rel="noopener noreferrer"></a>
        </header>

        <main>
            <div class="portfolio-item-page">
                <img src="{img}" alt="{alt}">
                <div class="text-container">
                    <span class="left-text">{text}</span>
                </div>
            </div>
        </main>

        <footer>
            <p>Copyright 2023-2024 Berkan Cetinbag. All rights reserved.</p>
        </footer>
    </div>
</body>
</html>
"""

# Generate HTML files
for item in portfolio_items:
    file_name = item['file']
    html_content = html_template.format(
        text=item['text'],
        img=item['img'],
        alt=item['alt']
    )
    
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Generated {file_name}")

print("All files have been generated successfully.")