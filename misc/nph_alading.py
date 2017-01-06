# encoding: ~*~utf8~*~
"""nph-aladin.py
Fetches AladinLite Survey Data from various sources
Combines to create a JSON file of survey data with https links

author: Robert Pirtle
license: MIT
"""
import urllib.request as request
import json

def main():
    # currently used data
    current_http_url = 'http://aladin.u-strasbg.fr/java/nph-aladin.pl'
    current_http_url += '?frame=aladinLiteDic'

    # list of available survey mirrors
    mirrors_list_url = 'http://alasky.unistra.fr/MocServer/query'
    mirrors_list_url += '?hips_service_url*=https*&fields=ID,hips_service_url*'
    mirrors_list_url += '&fmt=json'

    survey_data = json.loads(request.urlopen(current_http_url).read().decode('utf8'))
    mirror_data = json.loads(request.urlopen(mirrors_list_url).read().decode('utf8'))

    # mirror IDs are prefixed with 'CDS/'
    processed_mirrors = {}
    for mirror in mirror_data:
        survey_id = mirror['ID'][4:]
        processed_mirrors[survey_id] = mirror['hips_service_url_2']

    for i, survey in enumerate(survey_data):
        if survey['id'] in processed_mirrors.keys():
            survey['url'] = processed_mirrors[survey['id']]
        else:
            msg = '* {} not found in available mirrors'.format(str(survey['id']))
            msg += ', [current link]({})'.format(survey['url'])
            del survey_data[i]
            print(msg)

    json_filename = 'data/nph-aladin.json'
    with open(json_filename, 'w') as f:
        f.write(json.dumps(survey_data))
        print('file written to {}'.format(json_filename))

if __name__ == '__main__':
    main()
