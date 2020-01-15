

import os
from newsroom import jsonl

index = 1
cc_num = 0
out_dir = "../data/Newsroom/train"
os.makedirs(out_dir, exist_ok=True)
with jsonl.open("../data/Newsroom/train.jsonl.gz", gzip=True) as train_file:
    for entry in train_file:
        summary_str = entry["summary"].strip()
        content_str = entry["text"].strip()
        # print("************************************")
        # print(summary_str)
        # print("-------------------------------")
        # print(content_str)
        pos = summary_str.find("<?xml:")
        if pos >= 0:
            continue
        if content_str.find(summary_str) >= 0:
            cc_num += 1
        text_file_path = os.path.join(out_dir, "%06d.txt" % index)
        index += 1
        with open(text_file_path, "w") as fw:
            fw.write(summary_str.replace("\n", ".") + "\n" + content_str)


print("summary in content num = %d " % cc_num)          #
print("total txt num = %d " % index)
