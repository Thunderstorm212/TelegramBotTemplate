from collections import namedtuple
from core.ui.btn import btn_dict
from core.ui.answer import answer_dict
from core.ui.error import error_dict


def customDictDecoder(dict1):
    for key, value in dict1.items():
        if type(value) is dict:
            dict1[key] = customDictDecoder(value)
    return namedtuple('X', dict1.keys())(*dict1.values())


ui_text = {}
ui_text.update({"answer": customDictDecoder(answer_dict)})
ui_text.update({"btn": customDictDecoder(btn_dict)})
ui_text.update({"error": customDictDecoder(error_dict)})



