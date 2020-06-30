#!/usr/bin/env python3

import os
import subprocess

install_prefix = os.environ['MESON_INSTALL_PREFIX']
schemadir = os.path.join(install_prefix, 'share/glib-2.0/schemas')
icondir = os.path.join(install_prefix, 'share/icons/hicolor')

if not os.environ.get('DESTDIR'):
    print('compiling the gsettings schemas ... ')
    subprocess.call(['glib-compile-schemas', schemadir])

print('Updating icon cache...')
subprocess.call(['gtk-update-icon-cache', '-q', '-t' ,'-f', icondir])