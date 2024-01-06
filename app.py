from flask import Flask, render_template, request, jsonify
from threading import Thread
import sys
import os
import sys
import time
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.join(current_dir, '..')
sys.path.append(project_dir)

from live_chat_scraper import LiveChatScraper
from text_analyzer.preprocess import Preprocess




from blueprints.main import main
from blueprints.analysis_panel import analysis_panel

app = Flask(__name__)
app.register_blueprint(main)
app.register_blueprint(analysis_panel)




CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = CURRENT_PATH + "\live_chat_data.json"
if os.environ.get('WERKZEUG_RUN_MAIN') != 'true': # this is to prevent the code from running twice in debug mode
    pass
else:
    print("[++++++++++++++++++++++++CODE:200:RUNNING!++++++++++++++++++++++++]")
    proc = Preprocess(lang="turkish")
    app.live_chat_scraper = LiveChatScraper()
    app.preprocess = Preprocess()
    



if __name__ == '__main__':
    #call run_bot_manager() in a thread
    print("ok wi.starting.........")
    app.run(host="0.0.0.0",debug=True)