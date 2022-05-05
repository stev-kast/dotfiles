# Imports 
import dracula.draw

# load theme 
dracula.draw.blood(c, {
    'spacing': {
    'vertical': 6,
    'horizontal': 8
    }
})


## Documentation:
##   qute://help/configuring.html
##   qute://help/settings.html

## This is here so configs done via the GUI are still loaded.
## Remove it to not load settings done via the GUI.
config.load_autoconfig(False)


## Time interval (in milliseconds) between auto-saves of
## config/cookies/etc.
## Type: Int
c.auto_save.interval = 15000

## Always restore open sites when qutebrowser is reopened. Without this
## option set, `:wq` (`:quit --save`) needs to be used to save open tabs
## (and restore them), while quitting qutebrowser in any other way will
## not save/restore the session. By default, this will save to the
## session which was last loaded. This behavior can be customized via the
## `session.default_name` setting.
## Type: Bool
c.auto_save.session = True

## Search engines which can be used via the address bar.  Maps a search
## engine name (such as `DEFAULT`, or `ddg`) to a URL with a `{}`
## placeholder. The placeholder will be replaced by the search term, use
## `{{` and `}}` for literal `{`/`}` braces.  The following further
## placeholds are defined to configure how special characters in the
## search terms are replaced by safe characters (called 'quoting'):  *
## `{}` and `{semiquoted}` quote everything except slashes; this is the
## most   sensible choice for almost all search engines (for the search
## term   `slash/and&amp` this placeholder expands to `slash/and%26amp`).
## * `{quoted}` quotes all characters (for `slash/and&amp` this
## placeholder   expands to `slash%2Fand%26amp`). * `{unquoted}` quotes
## nothing (for `slash/and&amp` this placeholder   expands to
## `slash/and&amp`). * `{0}` means the same as `{}`, but can be used
## multiple times.  The search engine named `DEFAULT` is used when
## `url.auto_search` is turned on and something else than a URL was
## entered to be opened. Other search engines can be used by prepending
## the search engine name to the search term, e.g. `:open google
## qutebrowser`.
## Type: Dict
c.url.searchengines = {
    'DEFAULT': 'https://www.google.com/search?q={}',
    'dd':'https://duckduckgo.com/?q={}'}


## Page to open if :open -t/-b/-w is used without URL. Use `about:blank`
## for a blank page.
## Type: FuzzyUrl
c.url.default_page = 'about:blank'#'https://start.duckduckgo.com/'

## Page(s) to open at the start.
## Type: List of FuzzyUrl, or FuzzyUrl
c.url.start_pages = ['about:blank']

# Bit Warden Manager
config.bind('pe','spawn --userscript qute-bitwarden')
config.bind('po','spawn --userscript qute-bitwarden --password-only')
config.bind('eo','spawn --userscript qute-bitwarden --username-only')

# Show downloads Rofi
config.bind('sd','spawn --userscript open_downloads')

# Custom bindings
config.bind('<Alt-q>', 'tab-close')

# default editor
c.editor.command = ['alacritty','-e','vim','{file}']
