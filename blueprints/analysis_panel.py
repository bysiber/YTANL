from flask import Blueprint, render_template, request, jsonify, current_app, session, url_for, copy_current_request_context
from threading import Thread
from utils import read_json
analysis_panel = Blueprint('analysis_panel', __name__, url_prefix='/analysis_panel')


@analysis_panel.route('/')
def main():
    return render_template('analysis_panel.html')

@analysis_panel.route('/get_most_active_authors')
def get_most_active_authors():
    #aynı isimde olanları resim aracılığı yada id ile değiştir!
    most_active_authors = current_app.preprocess.get_most_active_authors()
    print(most_active_authors)
    return jsonify(most_active_authors)





@analysis_panel.route('/get_spent_time_authors')
def get_spent_time_authors():
    #aynı isimde olanları resim aracılığı yada id ile değiştir!
    spent_time_authors = current_app.preprocess.get_spent_time_authors()
    return jsonify(spent_time_authors)

@analysis_panel.route('/get_most_repeating_words')
def get_most_repeating_words():
    #aynı isimde olanları resim aracılığı yada id ile değiştir!
    most_repeating_words = current_app.preprocess.get_most_repeating_words()
    return jsonify(most_repeating_words)