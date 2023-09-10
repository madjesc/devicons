import fontforge as ff
import toml

font = ff.font()
font.familyname = 'Devicons'
font.fontname = 'Devicons'
font.fullname = 'Devicons'
font.encoding = "UnicodeFull"
mappings = toml.load('./mappings.toml')

def mapping_set_icons(icons, map):
    for name, unicode in map.items():
        filename = f"./icons/{icons}/{name}.svg"
        glyph = font.createChar(unicode, name)
        glyph.importOutlines(filename)

for icons in ['octicons', 'nonicons']:
    mapping_set_icons(icons, mappings[icons])

font.generate('devicons.ttf')

