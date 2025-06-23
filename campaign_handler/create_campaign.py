from __future__ import print_function
import time
import datetime
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

def create_campaign(html):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = '' # Removed for security

    api_instance = sib_api_v3_sdk.EmailCampaignsApi(sib_api_v3_sdk.ApiClient(configuration))
    tag = 'summary'
    sender = {"name": 'Summified News', "email": ''}  # Removed for security
    name = 'New Campaign'
    subject = 'New Summary!'
    reply_to = ''  # Removed for security
    recipients = {"listIds": [5]}
    inline_image_activation = False
    mirror_active = False
    header = 'If you are not able to see this mail, click {here}'
    footer = 'If you wish to unsubscribe from our newsletter, click {here}'
    utm_campaign = 'UTM Campaign'
    email_campaign  = sib_api_v3_sdk.CreateEmailCampaign(   tag=tag, sender=sender,
                                                            name=name, html_content=html, subject=subject,
                                                            reply_to=reply_to,
                                                            recipients=recipients,
                                                            inline_image_activation=inline_image_activation,
                                                            mirror_active=mirror_active, header=header,
                                                            footer=footer, utm_campaign=utm_campaign)

    try:
        api_response = api_instance.create_email_campaign(email_campaign)
        pprint(api_response)
        return api_response.id
    except ApiException as e:
        print("Exception when calling EmailCampaignsApi->create_email_campaign: %s\n" % e)
