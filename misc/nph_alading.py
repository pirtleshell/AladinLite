# encoding: ~*~utf8~*~
"""nph-aladin.py
Fetches AladinLite Survey Data from various sources
Combines to create a JSON file of survey data with https links

author: Robert Pirtle
license: MIT
"""
import urllib.request as request
import json

def not_found(survey):
    msg = '* {} not found in available mirrors'.format(survey['id'])
    msg += ', [current link]({})'.format(survey['url'])
    print(msg)

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

    https_survey_data = []
    for survey in survey_data:
        # check for mirror info on survey
        for mirror in [m for m in mirror_data if survey['id'] in m['ID']]:
            # find https mirror
            urls = [mirror[key] for key in mirror.keys() if key != 'ID']
            https = [url for url in urls if url[:8] == 'https://']
            if len(https) > 0:
                survey['url'] = https[0]
                https_survey_data.append(survey)
            else:
                not_found(survey)

    json_filename = 'data/nph-aladin.json'
    with open(json_filename, 'w') as f:
        f.write(json.dumps(https_survey_data))
        print('file written to {}'.format(json_filename))

if __name__ == '__main__':
    main()
