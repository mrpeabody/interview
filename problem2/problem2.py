from flask import Flask, url_for
from flask import render_template, redirect
from flask import abort
import requests
import dateutil.parser

app = Flask(__name__, static_url_path='/static')


@app.route('/comment/<int:comment_id>',  methods=['GET'])
def comment(comment_id=None):
    """
    This view loads and renders comments found with the <comment_id>
    :param comment_id:
    :return:
    """
    if comment_id is None:
        abort(404)

    try:
        # load comments from API
        comment_info = requests.get(
            'https://mysidewalk.com/api/engagement/v1/comments/{comment_id}.json'.format(comment_id=comment_id)
        ).json()

        # assuming that the comments list and the users list correspond, render comments
        return render_template('comments.html', comments=zip(
            comment_info['comments'],
            comment_info['linked']['users'],
            comment_info['linked']['medias']
        ))
    except Exception as e:
        print(e)
        abort(400)


@app.template_filter('format_date')
def format_date(date_string, date_format='%Y-%m-%d at %H:%m %p'):
    """
    This function represents a custom jinja2 template filter, that converts a string containing date and time in
    the following format: '2014-08-28T05:39:59.554131Z' (UTC) into the format set by the second argument.
    :param date_string: date string to format
    :param date_format: date format to apply to a string
    :return: formatted date string
    """
    return dateutil.parser.parse(date_string).strftime(date_format)


if __name__ == '__main__':
    app.run()
