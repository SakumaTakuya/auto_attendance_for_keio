import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfB_54t-lyRdwl0KRqu-eaHMhgm5hMhnHmEqJkVj7J7t1LntA"

# viewform | formResponse
OPERATION = "viewform"

DATA_ROOT = os.path.join(BASE_DIR, "data")

DATA_FORMAT = {
    # entry key : default value
    # 教職員番号
    "675230857" : None,
    # 氏名
    "1488617142" : None,
    # 勤務形態
    "1143174674" : None,
    # 報告内容
    "1897951779" : None,
    # 日付
    "603641719" : None,
    # 時間
    "909280450" : None,
    # 資金源
    "1821789362" : None,
    # 業務内容
    "1258127436" : None,
    # 所属長の氏名
    "1730775372" : None,
    # 所属長のメールアドレス
    "1143336214" : None,
    # その他
    "1172543321" : None,
} 