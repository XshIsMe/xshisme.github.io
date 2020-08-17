import os
import sys


def del_path(filepath, filename):
    content = ""
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()
    new_content = content.replace("![](" + filename + "/", "![](")
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(new_content)


def add_path(filepath, filename):
    content = ""
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()
    new_content = content.replace("![](", "![](" + filename + "/")
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(new_content)


def handle(folderpath, action="del"):
    for filename in os.listdir(folderpath):
        filepath = os.path.join(folderpath, filename)
        if not os.path.isdir(filepath):
            if "del" == action:
                del_path(filepath, filename.rstrip(".md"))
            elif "add" == action:
                add_path(filepath, filename.rstrip(".md"))


def main():
    folderpath = r"_posts"
    try:
        action = sys.argv[1]
    except:
        action = "del"
    handle(folderpath, action)
    if "del" == action:
        print("INFO  Deleted img path")
    elif "add" == action:
        print("INFO  Add img path")


if __name__ == "__main__":
    main()
