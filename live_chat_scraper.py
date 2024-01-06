import time
import sys
import time
from livechat_scraper.scrapers import livechat_scraper
from livechat_scraper.constants import scraper_constants as sCons


class LiveChatScraper():
    def __init__(self):
        self.video_url = ""
        self.progress = "0"

    def get_live_chat(self, video_url, output_name="static/chat_data/live_chat_data", progress_tracker=None):
        """"livechat scraper, scrapes a video URL and outputs the content 
            to a JSON, txt, and raw file.
        """
        start_time = time.time()
        scraper = livechat_scraper.LiveChatScraper(video_url) # we will seperate this to another func like (set_scraper) to prevent multi unnecessary calling class objects ?
        
        scraper.scrape()
        # saves all messages in a file as a json object
        scraper.write_to_file(sCons.OUTPUT_JSON, output_name)
        # saves all messages in a txt file, each line is a message entry
        #scraper.write_to_file(sCons.OUTPUT_TEXT, output_name)
        # saves all messages in a json file preserving the raw json that comes over when making the request call to youtube
        #scraper.write_to_file(sCons.OUTPUT_RAW, output_name)
        end_time = time.time()
        print(f'program runtime: {end_time - start_time}')
    


    def update_progress(self, progress):
        self.progress = progress
