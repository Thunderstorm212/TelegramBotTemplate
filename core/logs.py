import logging


class log:
    def __init__(self, message, user, user_id):
        logging.info(f"USER {user} {str(user_id)} {message.text}")
