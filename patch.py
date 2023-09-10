import fontforge as ff
import toml
import sys

nargs = ['_', 'file', 'out']
args = dict(zip(nargs, sys.argv))

font = ff.open(args.get('file'))
font.fontname = font.familyname + '-Devicons'
font.fullname = font.familyname + ' Devicons'
font.encoding = "UnicodeFull"
mappings = toml.load('./mappings.toml')

def mapping_set_icons(icons, map):
    for name, unicode in map.items():
        filename = f"./icons/{icons}/{name}.svg"
        glyph = font.createChar(unicode, name)
        glyph.importOutlines(filename)

for icons in ['octicons', 'nonicons']:
    mapping_set_icons(icons, mappings[icons])

font.generate(args.get('out', 'patched.ttf'))

