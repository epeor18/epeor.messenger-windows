#!C:/msys64/home/appveyor/gajim/win/_build_root/mingw32/bin/python3.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'gajim==1.1.0+335c3e2d3df7','gui_scripts','gajim'
__requires__ = 'gajim==1.1.0+335c3e2d3df7'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('gajim==1.1.0+335c3e2d3df7', 'gui_scripts', 'gajim')()
    )
