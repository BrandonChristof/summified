from .create_campaign import create_campaign
from .send_campaign import send_campaign

def send_all(html, send_campaign=False):
    campaign_id = create_campaign(html) # Returns Int for ID
    if send_campaign:
        send_campaign(campaign_id)
