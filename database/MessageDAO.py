from database.Message import Message
from database.DAO import DAO


class MessageDAO(DAO):
    def __init__(self):
        DAO.__init__(self)

    def insert(self, item):
        command_string = "INSERT INTO MESSAGE (HANDLE_ID,TEXT_MESSAGE,IS_FROM_ME,DATE_OF_TEXT)\
         VALUES  (:1,:2,:3,:4)"
        self.cur.execute(command_string, (str(item.get_handle_id()), str(item.get_text_message()), \
                                          str(item.get_is_from_me()), str(item.get_date_of_text())))
        self.con.commit()

    def select(self, message_id):
        command_string = "SELECT * FROM MESSAGE where MESSAGE_ID =" + str(message_id)
        self.cur.execute(command_string)
        rows = self.cur.fetchall()
        message = Message()
        message.set_values_from_row(rows)
        return message

    def delete(self, message_id):
        command_string = "DELETE FROM MESSAGE WHERE MESSAGE_ID= :1"
        self.cur.execute(command_string, (str(message_id)))
        self.con.commit()
