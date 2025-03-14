from datetime import datetime


extensions = []
templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"

project = u"photonsphinx"
year = datetime.now().year
copyright = u"%d phi ARCHITECT" % year

exclude_patterns = ["_build"]

html_theme = "photonsphinx"
html_sidebars = {
    "**": [
        "about.html",
        "navigation.html",
        "relations.html",
        "searchbox.html",
        "donate.html",
    ]
}
html_theme_options = {
    "description": "A light, configurable Sphinx theme",
    "github_user": "photon-platform",
    "github_repo": "photonsphinx",
    "fixed_sidebar": True,
    #  "tidelift_url": "https://tidelift.com/subscription/pkg/pypi-alabaster?utm_source=pypi-alabaster&utm_medium=referral&utm_campaign=docs",  # noqa
}

extensions.append("releases")
releases_github_path = "photon-platform/photonsphinx"
# Our pre-0.x releases are unstable / mix bugs+features
releases_unstable_prehistory = True
