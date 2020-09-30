import argparse
import os
import re
import pandas as pd
import webbrowser


parser = argparse.ArgumentParser()
parser.add_argument("-s", "--settings", required=False, default="base", help="設定モジュール名")
parser.add_argument("-d", "--data", required=True, help="実行データのパス(DATA_ROOTからの相対パス指定)")
parser.add_argument("-o", "--op", required=False, choices=["viewform", "formResponse"], help="実行命令(表示:viewform, 提出:formResponse)")


SPACE_REP = "+"
ENTRY = "entry."

def make_url(base, op, format, data):
    vals = []
    for key, default in format.items():
        val = data.get(key) or default
        if val:
            # スペースは置換
            val = re.sub(r"\s|\n", SPACE_REP, str(val))
            vals.append(f"{ENTRY}{key}={val}")

    return f"{base}/{op}?{'&'.join(vals)}"


def main(args=parser.parse_args()):
    settings = __import__(f"settings.{args.settings}", fromlist=['*'])
    df = pd.read_csv(
        os.path.join(settings.DATA_ROOT, args.data), 
        dtype=str).fillna("")

    for _, data in df.iterrows():
        url = make_url(
            settings.FORM_URL, 
            args.op or settings.OPERATION, 
            settings.DATA_FORMAT, 
            data)
        webbrowser.open_new(url)

if __name__ == "__main__":
    main()