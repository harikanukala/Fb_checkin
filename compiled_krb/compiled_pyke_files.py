# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('', '', 'fb_checkin_fc.krb'):
           [1482184790.704972, 'fb_checkin_fc_fc.py'],
         ('', '', 'fb_checkin.kfb'):
           [1482184790.737429, 'fb_checkin.fbc'],
        },
        compiler_version)

