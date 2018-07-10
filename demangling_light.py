import subprocess

demangle_cache = {}

def get_demangled(s):
    if s not in demangle_cache:
        demangle_cache[s] = subprocess.check_output(['c++filt', '-n', s]).strip()
    return demangle_cache[s]