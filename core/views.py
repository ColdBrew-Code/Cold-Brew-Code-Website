import random

from django.shortcuts import render
from django.templatetags.static import static


TERMINAL_BACKGROUND_BLOCK = """$ cold-brew-code init
    Initializing Cold Brew Code...
    [████████████████████] 100%
    ✓ Environment ready

$ grind --coarse --weight=150g
    Grinding to coarse setting...
    ✓ 150g ground and ready

$ brew --method=cold --filtered
    Adding grounds to chamber...
    Pouring cold filtered water...
    Sealing vessel...
    ✓ Brew started

$ steep --duration=24h
    [████████████████████] 24:00:00
    ✓ 500ml concentrate extracted

$ strain --filter=fine
    Running through filter...
    Removing all grounds...
    ✓ Clean concentrate ready

$ team --list
    TEAM MEMBERS
    Shanna Graves          Full Stack Developer
    Geoffrey Wortham       Frontend Developer
    Nyx Strong             Backend Developer
    Wilhelmina Vanderpool  Full Stack Developer
    Scarlett Conyers       Graphic Designer
    Laura Kirkpatrick      Backend Developer

$ menu --list
    COLD BREW CODE MENU
    cold_brew.standard     $4.50
    cold_brew.oat_milk     $5.00
    cold_brew.vanilla      $5.25
    cold_brew.lavender     $6.00

$ order --item=cold_brew.oat_milk
    Processing order...
    Order #CBC-042 confirmed
    ✓ Ready in 3 minutes

$ git add --all
$ git commit -m "initial brew"
    [main] initial brew
    6 files changed ✓

$ npm install
    Resolving dependencies...
    248 packages added in 3.2s
    ✓ Dependencies installed

$ deploy --env=production
    Bundling assets...
    Optimizing build...
    [████████████████████] 100%
    ✓ Live at coldbrewcode.dev"""


NOT_FOUND_TAGLINES = [
    'The page you\'re looking for has taken a coffee break.',
    'This page is like a coffee cup after a long day - empty.',
    'This page is as elusive as a perfectly brewed cup of coffee...',
    'Unfortunately, this page has gone cold.',
    'Not all who wander are lost... but this page definitely is.',
    'Looks like someone forgot to start the coffee maker...',
    'Nothing but coffee grounds here...'
]


def build_team_members():
    team_members = [
        {
            'name': 'Shanna Graves',
            'role': 'Full Stack Developer',
            'title': 'Full Stack Developer',
            'bio': 'Shanna is a versatile full stack developer with a creative eye for web design. Their adaptive approach means every software solution is tailor-made to fill a need.',
            'image_path': 'headshots/headshot_shanna_graves.webp',
            'portfolio_url': 'https://gravessoftware.dev',
            'linkedin_url': '',
            'github_url': 'https://github.com/GravesSoftwareDev',
            'email': 'graves_tech@outlook.com',
        },
        {
            'name': 'Geoffrey Wortham',
            'role': 'Frontend Developer',
            'title': 'Frontend Developer',
            'bio': 'Geoffrey is a frontend specialist who thrives on pushing the limits of what interfaces can do. Their drive to explore every corner of the craft means every project is not only beautiful but built to perform.',
            'image_path': 'headshots/headshot_geoffrey_wortham.webp',
            'portfolio_url': '',
            'linkedin_url': 'https://www.linkedin.com/in/geoffreywortham/',
            'github_url': 'https://github.com/shongzahToo',
            'email': '',
        },
        {
            'name': 'Nyx Strong',
            'role': 'Backend Developer',
            'title': 'Backend Developer',
            'bio': 'Nyx is a backend developer who loves to solve complex problems with elegant code. Her skills shine through on every project, ensuring that every solution is functional, efficient, and built to last.',
            'image_path': 'headshots/headshot_nyx_strong.webp',
            'portfolio_url': 'https://github.com/NyxErinys',
            'linkedin_url': '',
            'github_url': 'https://github.com/NyxErinys',
            'email': '',
        },
        {
            'name': 'Wilhelmina Vanderpool',
            'role': 'Full Stack Developer',
            'title': 'Full Stack Developer',
            'bio': 'Mina is a full stack developer specializing in UI/UX and accessible design. She builds practical web applications, databases, and tools with a strong emphasis on usability, maintainability, and user experience. Her goal is to create software that not only works well but is intuitive and enjoyable to use.',
            'image_path': 'headshots/headshot_wilhelmina_vanderpool.webp',
            'portfolio_url': 'https://minasaur.com/',
            'linkedin_url': 'https://www.linkedin.com/in/minasaur/',
            'github_url': 'https://github.com/minasaurv',
            'email': 'mina@minasaur.com',
        },
        {
            'name': 'Scarlett Conyers',
            'role': 'Graphic Designer',
            'title': 'Graphic Designer',
            'bio': 'Scarlett is a prolific graphic designer with a passion for creating visually stunning and impactful designs. She is dedicated to delivering creative solutions that resonate with audiences.',
            'image_path': 'headshots/headshot_scarlett_conyers.webp',
            'portfolio_url': '',
            'linkedin_url': 'https://www.linkedin.com/in/scarlett-conyers/',
            'github_url': '',
            'email': '',
        },
        {
            'name': 'Laura Kirkpatrick',
            'role': 'Backend Developer',
            'title': 'Backend Developer',
            'bio': 'Laura is a software/game developer with a passion for making quality products. She is currently working as a Back End Developer, but is able to fit anywhere in a project. She got her experience with software development projects such as basic websites, frameworks, APIs, mobile apps, video games, and much more.',
            'image_path': 'headshots/headshot_laura_kirkpatrick.webp',
            'portfolio_url': 'https://github.com/Fruity-Patoootie',
            'linkedin_url': 'https://www.linkedin.com/in/laura-b-kirkpatrick/',
            'github_url': 'https://github.com/Fruity-Patoootie',
            'email': '',
        },
    ]

    for member in team_members:
        member['image_url'] = static(member['image_path'])
        member['portfolio_url'] = member.get('portfolio_url', '')
        member['linkedin_url'] = member.get('linkedin_url', '')
        member['github_url'] = member.get('github_url', '')
        member_email = member.get('email', '').strip()
        if member_email:
            member['email_link'] = f"mailto:{member_email}?subject=Message%20for%20{member['name'].replace(' ', '%20')}"
        else:
            member['email_link'] = ''

    return team_members


def build_portfolio_items(team_members):
    contributor_lookup = {
        member['name']: member.get('portfolio_url') or member.get('github_url') or member.get('linkedin_url') or ''
        for member in team_members
    }
    demo_store_image = static('projects/demo-store.webp')
    demo_store2_image = static('projects/demo-store2.webp')
    ecb_image = static('projects/ecb.webp')
    portfolio_items = [
        {
            'title': 'Executive Coach Builders',
            'description': 'Built as a capstone project at OTC, this site for Executive Coach Builders features a custom client portal - giving the ECB team full control over their inventory and site content without touching a line of code.',
            'contributors': ['Shanna Graves', 'Geoffrey Wortham'],
            'url': 'https://executivecoachbuilders-production.up.railway.app/',
            'slides': [
                {'src': ecb_image, 'alt': 'ECB  propreview'},
            ],
        },
        {
            'title': 'Demo Store',
            'description': 'A full-featured e-commerce concept showcasing what ColdBrew can build. It includes a modern storefront design, customizable product listings, and a dashboard for managing form submissions — ready to be tailored for any client.',
            'contributors': ['Shanna Graves', 'Geoffrey Wortham'],
            'url': 'https://web-demo.gravessoftware.dev/',
            'slides': [
                {'src': demo_store_image, 'alt': 'Demo Store homepage preview'},
                {'src': demo_store2_image, 'alt': 'Demo Store product page preview'},
            ],
        },
    ]

    for item in portfolio_items:
        item['contributors'] = [
            {
                'name': contributor_name,
                'url': contributor_lookup.get(contributor_name, ''),
                'image_url': next(
                    (
                        member['image_url']
                        for member in team_members
                        if member['name'] == contributor_name
                    ),
                    '',
                ),
            }
            for contributor_name in item['contributors']
        ]

    return portfolio_items


def build_chalk_terminal_text():
    return "\n\n".join([TERMINAL_BACKGROUND_BLOCK] * 6)


def build_not_found_tagline():
    return random.choice(NOT_FOUND_TAGLINES)


def index(request):
    team_members = build_team_members()

    return render(
        request,
        'index.html',
        {
            'team_members': team_members,
            'chalk_terminal_text': build_chalk_terminal_text(),
        },
    )


def portfolio(request):
    team_members = build_team_members()

    return render(
        request,
        'portfolio.html',
        {
            'chalk_terminal_text': build_chalk_terminal_text(),
            'portfolio_items': build_portfolio_items(team_members),
        },
    )


def not_found(request, exception):
    return render(
        request,
        '404.html',
        {
            'chalk_terminal_text': build_chalk_terminal_text(),
            'not_found_tagline': build_not_found_tagline(),
        },
        status=404,
    )
