from __future__ import print_function
import time
import datetime
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

def send_campaign(campaign_id):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = '' # Removed for security

    api_instance = sib_api_v3_sdk.EmailCampaignsApi(sib_api_v3_sdk.ApiClient(configuration))

    try:
        api_instance.send_email_campaign_now(campaign_id)
    except ApiException as e:
        print("Exception when calling EmailCampaignsApi->send_email_campaign_now: %s\n" % e)
