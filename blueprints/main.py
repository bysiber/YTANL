from flask import Blueprint, render_template, request, jsonify, current_app, session, url_for, copy_current_request_context
from threading import Thread
from utils import read_json
main = Blueprint('main', __name__, url_prefix='/main')


@main.route('/')
def main_page():
    return render_template('main.html')

def get_live_chat_thread(video_link):
    @copy_current_request_context
    def _run_manager():
        current_app.live_chat_scraper.get_live_chat(video_link)
        current_app.preprocess.set_data(path="static/chat_data/live_chat_data.json")

    run_manager_thread = Thread(target=_run_manager)
    run_manager_thread.daemon = True
    run_manager_thread.start()


@main.route('/scrape_live_chat', methods=['POST'])
def scrape_chat_data():
    data = request.json  # JSON veriyi al
    video_link = data["videoLink"]
    get_live_chat_thread(video_link)
    return jsonify({'success': True}), 200


@main.route('/get_live_chat', methods=['GET'])
def get_chat_data():
    path = "static/chat_data/live_chat_data.json"
    data = read_json(path)

    return jsonify(data), 200


