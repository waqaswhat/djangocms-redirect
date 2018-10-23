# -*- coding: utf-8 -*-

def get_key_from_path_and_site(path, site_id):
    key = '{0}_{1}'.format(path, site_id)
    # FIX memcache.Client.MemcachedKeyLengthError --------------------------------------------------
    import hashlib
    key = hashlib.sha224(key.encode('utf-8')).hexdigest()
    # /FIX memcache.Client.MemcachedKeyLengthError -------------------------------------------------
    return key