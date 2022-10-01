import json

import requests
from .utils import get_connections_link, get_required_cookies


def scrap_connections(user_id_string, password_string):
    # Obtaining required cookies with Selenium login
    required_cookies = get_required_cookies(user_id_string, password_string)

    print('required_cookies', required_cookies)
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}

    all_page_connection_details = {}
    page_count = 0
    print('CONNECTIONS SCRAPING')
    # The request query link runs for every 40 sets of connections until the length of the list of connections in the
    # response equals zero.
    while True:
        page_connection_details = []
        print(f'SCRAPING CONNECTIONS FROM {page_count * 40} TO {page_count + 1 * 40}')
        start = page_count * 40
        page_count += 1
        # Generates the voyager API URL for the next 40 connections
        connections_link = get_connections_link(start)
        req_session = requests.session()
        req_session.cookies['li_at'] = required_cookies['li_at']
        req_session.cookies["JSESSIONID"] = required_cookies['JSESSIONID']
        req_session.headers = headers
        req_session.headers["csrf-token"] = req_session.cookies["JSESSIONID"].strip('"')
        connections_response = req_session.get(connections_link)
        connections_response_dict = connections_response.json()
        connections_elements = connections_response_dict["elements"]
        if len(connections_elements) == 0:
            break
        for ent in connections_elements:
            connection_details = {
                "firstName": '',
                "lastName": '',
                "profession&company": '',
                "emailAddress": ''
            }
            if "connectedMemberResolutionResult" not in ent:
                continue
            connectedMemberResolutionResult = ent["connectedMemberResolutionResult"]
            if "firstName" in connectedMemberResolutionResult:
                connection_details["firstName"] = connectedMemberResolutionResult["firstName"]
            if "lastName" in connectedMemberResolutionResult:
                connection_details["lastName"] = connectedMemberResolutionResult["lastName"]
            if "headline" in connectedMemberResolutionResult:
                connection_details["profession&company"] = connectedMemberResolutionResult["headline"]
            publicIdentifier = ent["connectedMemberResolutionResult"]["publicIdentifier"]

            # Voyager API URL to get specific connection contact information
            get_contact_link = f"https://www.linkedin.com/voyager/api/identity/profiles/{publicIdentifier}/profileContactInfo"
            get_contact_link_response = req_session.get(get_contact_link)
            get_contact_link_res_json = get_contact_link_response.json()
            if "emailAddress" in get_contact_link_res_json:
                connection_details["emailAddress"] = get_contact_link_res_json["emailAddress"]
                # print(get_contact_link_res_json)
            page_connection_details.append(connection_details)
            # print(connection_details)
        all_page_connection_details[page_count]=page_connection_details
    # all_page_connection_details = json.dumps(all_page_connection_details)
    return all_page_connection_details
